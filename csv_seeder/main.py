import inspect
import os

import gradio as gr
import pandas as pd
from mimesis import Address, Generic, Locale, Person, Text
from pydash import snake_case

DEFUALT_METHOD_NAME = "word"
provider_class_list = []
provider_name_provider_dict = {}
method_name_method_dict = {}
method_name_list = []


def generate_mimesis_method_dict_for_locale(value):
	global provider_class_list
	global provider_name_provider_dict
	global method_name_method_dict
	global method_name_list

	generic = Generic(locale=value)
	# generic = Generic(locale=Locale[value])
	# person = Person()
	# address = Address()
	# text = Text()

	# List of Mimesis providers to introspect
	# providers = [generic, person, address, text]
	provider_class_list = [generic]
	provider_name_provider_dict = {
		provider_name: provider
		for provider_class in provider_class_list
		for provider_name, provider in inspect.getmembers(provider_class)
	}

	method_name_method_dict = {
		method_name: method
		for provider in provider_name_provider_dict.values()
		for method_name, method in inspect.getmembers(provider, predicate=inspect.ismethod)
		if not method_name.startswith("_")
	}
	method_name_list = list(method_name_method_dict.keys())


def generate_csv(*args):
	method_name_list = args[:-3]
	locale = args[-3]
	no_of_records = args[-2]
	meta = args[-1]
	headers = meta.get("headers")
	filename_with_extension = meta.get("filename_with_extension")
	filename, _ = os.path.splitext(filename_with_extension)
	records = []

	generate_mimesis_method_dict_for_locale(locale)
	for _ in range(no_of_records):
		record = {}
		for index, method_name in enumerate(method_name_list):
			method = method_name_method_dict.get(method_name, DEFUALT_METHOD_NAME)
			record[headers[index]] = method()
		records.append(record)

	df = pd.DataFrame(records)
	csv_path = f"temp/{no_of_records} Records of {filename} ({locale}).csv"
	df.to_csv(csv_path, index=False, encoding="utf-8")

	return csv_path


def get_csv_headers(filepath):
	df = pd.read_csv(filepath)
	return list(df.columns)


def get_method_name_for_header(header):
	method_name = DEFUALT_METHOD_NAME
	if header in method_name_list:
		method_name = header
	else:
		for name in method_name_list:
			if header in name:
				method_name = name
				break

	return method_name


with gr.Blocks() as demo:
	# generate_mimesis_method_dict_for_locale(Locale.EN.name)
	generate_mimesis_method_dict_for_locale(Locale.EN)
	file_input = gr.File(label="Upload CSV File", file_types=["csv"])
	upload_btn = gr.Button("Upload")

	@gr.render(inputs=file_input, triggers=[upload_btn.click])
	def process_csv_upload(file):
		gr.Label(value="Select type of each Headers")

		filepath = file.name
		filename_with_extension = os.path.basename(filepath)
		headers = get_csv_headers(filepath)

		meta = gr.State({})
		meta.value = {
			"headers": headers,
			"filename_with_extension": filename_with_extension,
		}

		dropdown_options = method_name_list
		dropdowns = []
		with gr.Row() as row:
			for header in headers:
				lower_header = snake_case(header)
				default_value = get_method_name_for_header(lower_header)
				dropdown = gr.Dropdown(
					choices=dropdown_options,
					value=default_value,
					label=f"{header}",
					interactive=True,
					elem_id=f"{lower_header}",
				)
				dropdowns.append(dropdown)

		with gr.Row() as row:
			no_of_records = gr.Number(label="No. of records to Generate", value=1)

			locale_choices = [locale.value for locale in Locale]
			default_locale_value = Locale.EN.value
			# locale_choices = [locale.name for locale in Locale]
			# default_locale_value = Locale.EN.name
			locale = gr.Dropdown(
				choices=locale_choices,
				value=default_locale_value,
				label="Choose the Locale",
				interactive=True,
				elem_id="locale",
			)
		generate_records_btn = gr.Button("Generate Records")

		@generate_records_btn.click(
			inputs=[*dropdowns, locale, no_of_records, meta],
			outputs=[gr.File(label="Download CSV", visible=False)],
		)
		def on_generate_records_btn_click(*args):
			csv_path = generate_csv(*args)
			return gr.File(value=csv_path, visible=True)


demo.launch(share=True)
