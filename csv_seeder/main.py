import inspect
import os

import gradio as gr
import pandas as pd
from mimesis import Address, Generic, Person, Text
from pydash import snake_case

# Instantiate Mimesis providers
generic = Generic()
default_method_name = "word"
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


with gr.Blocks() as demo:
	file_input = gr.File(label="Upload CSV File")
	upload_btn = gr.Button("Upload")

	@gr.render(inputs=file_input, triggers=[upload_btn.click])
	def process_csv_upload(file):
		gr.Label(value="Select type of each Headers")
		df = pd.read_csv(file.name)
		filename = os.path.basename(file.name)
		headers = list(df.columns)
		options = method_name_list
		meta = gr.State({})
		dropdowns = []
		with gr.Row() as row:
			for header in headers:
				lower_header = snake_case(header)
				value = lower_header if lower_header in options else default_method_name
				dropdown = gr.Dropdown(
					choices=options,
					value=value,
					label=f"{header}",
					interactive=True,
					elem_id=f"{lower_header}",
				)
				dropdowns.append(dropdown)

		no_of_records = gr.Number(label="No. of records to Generate", value=1)
		generate_records_btn = gr.Button("Generate Records")

		meta.value = {
			"headers": headers,
			"filename": filename,
		}

		@generate_records_btn.click(
			inputs=[*dropdowns, no_of_records, meta],
			outputs=gr.File(label="Download CSV"),
		)
		def generate_csv(*data):
			method_name_list = data[:-2]
			no_of_records = data[-2]
			meta = data[-1]
			headers = meta.get("headers")
			filename = meta.get("filename")
			records = []
			for _ in range(no_of_records):
				record = {}
				for index, method_name in enumerate(method_name_list):
					method = method_name_method_dict.get(method_name, default_method_name)
					record[headers[index]] = method()
				records.append(record)

			df = pd.DataFrame(records)
			csv_file = f"temp/{no_of_records} Records of {filename}"
			df.to_csv(csv_file, index=False)

			return csv_file


demo.launch()
