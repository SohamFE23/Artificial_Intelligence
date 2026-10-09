from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

credentials = Credentials(
    url = "https://us-south.ml.cloud.ibm.com",
    api_key = "iuuIpeG0NpVXX6zKqr5beSLN70UVrXyp_M3JGDFQl9st"
)
params = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
	GenTextParamsMetaNames.MAX_NEW_TOKENS: 100
}
model = ModelInference(
    model_id='ibm/granite-4-h-small',
    params=params,
    credentials=credentials,
    project_id="skills-network"
)
text = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an expert asssitant who provides concise and accurate answers. <|eot_id|>

<|start_header_id|>user<|end_header_id|>
What is the capital of Canada?|eot_id|>

<|start_header_id|>assistant<|end_header|>
"""

print(model.generate(text)['results'][0]['generated_text'])
