import inspect
import types

import pandas as pd
from mimesis import Address, Generic, Person, Text
from pydash import snake_case
from symbol import parameters

# Instantiate Mimesis providers
generic = Generic()
# person = Person()
# address = Address()
# text = Text()

# List of Mimesis providers to introspect
# providers = [generic, person, address, text]
# providers = [generic]
provider_name_provider_dict = {
	provider_name: provider for provider_name, provider in inspect.getmembers(generic)
}
# provider=list(provider_name_provider_dict.values())[15]

method_name_method_dict = {
	method_name: method
	for method_name, method in inspect.getmembers(
		list(provider_name_provider_dict.values())[15], predicate=inspect.ismethod
	)
	if not method_name.startswith("_")
}
method = list(method_name_method_dict.values())[15]
parameters_dict = inspect.signature(method).parameters


def is_callable_method(obj):
	"""Check if the attribute is a callable and has no required parameters."""
	if not callable(obj):
		return False

	if inspect.isclass(obj):
		return False

	# if isinstance(obj, types.BuiltinMethodType | types.MethodWrapperType | types.MethodType):
	if isinstance(obj, types.BuiltinMethodType | types.MethodWrapperType):
		return False

	try:
		signature = inspect.signature(obj)
		for param in signature.parameters.values():
			if param.default == inspect.Parameter.empty:
				return False
	except ValueError as e:
		print(e)
		return False

	return True


def auto_generate_mimesis_methods(providers):
	"""Auto-generate a dictionary of callable Mimesis methods from given providers."""
	methods = {}

	for provider in providers:
		for attribute_name in dir(provider):
			attribute = getattr(provider, attribute_name)

			if (
				is_callable_method(attribute)
				and not attribute_name.startswith("_")
				and attribute_name not in methods
			):
				# Use the attribute name directly as the key here; modify if needed
				methods[attribute_name] = attribute

	return methods


# Dynamically generate mappings
mimesis_methods = auto_generate_mimesis_methods(providers)
mimesis_attribute_list = [key for key, _ in mimesis_methods.items()]


def get_data_generator(header):
	lower_header = snake_case(header)
	if lower_header in mimesis_attribute_list:
		return mimesis_methods[lower_header]
	# for key, method in mimesis_methods.items():
	# 	if key in lower_header:
	# 		return method
	# Default fallback
	return text.word


def get_header_generator_dict(headers):
	generator_dict = {}
	for header in headers:
		generator_dict[header] = get_data_generator(header)

	return generator_dict


def generate_records(headers, count, locale="en"):
	records = []

	header_generator_dict = get_header_generator_dict(headers)
	for _ in range(count):
		record = {}
		for header in headers:
			generator = header_generator_dict[header]
			record[header] = generator()
		records.append(record)

	return records


def main(file_path, record_count, locale="en"):
	try:
		# Read the CSV file and extract headers
		df = pd.read_csv(file_path)
		headers = df.columns.tolist()

		# Generate records based on headers
		records = generate_records(headers, record_count, locale)

		for record in records:
			print(record)

	except Exception as e:
		print(f"An error occurred: {e}")


# Usage example
if __name__ == "__main__":
	file_path = "downloads/CRM Lead.csv"
	record_count = 10
	locale = "en"  # You can change this to another locale if needed
	main(file_path, record_count, locale)
