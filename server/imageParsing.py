# Google Vertex AI is used to describe picture

# TODO:
#
# You can either run
# $ export GOOGLE_APPLICATION_CREDENTIALS="$PWD/server/visual-captions-7c09483c6cc4.json"
#
# or we can try:
import os
import dotenv

dotenv.load_dotenv()
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/Mimi/Developer/insta_autofill/server/visual-captions-7c09483c6cc4.json'

## check compatibility with google service and python versionvenv
import vertexai
from vertexai.vision_models import ImageTextModel, Image
from google.cloud import aiplatform_v1
from typing import Optional
# from generateInstaCaption import generate_instagram_caption



def image_to_text(source_image_bytes):

    def init_sample(
        project: Optional[str] = 'visual-captions',
        location: Optional[str] = 'us-central1',
        experiment: Optional[str] = None,
        staging_bucket: Optional[str] = None,
        # credentials: Optional[auth_credentials.Credentials] = None,
        credentials = None,
        encryption_spec_key_name: Optional[str] = None,
        service_account: Optional[str] = None,
    ):

        from google.cloud import aiplatform

        aiplatform.init(
            project=project,
            location=location,
            experiment=experiment,
            staging_bucket=staging_bucket,
            credentials=credentials,
            encryption_spec_key_name=encryption_spec_key_name,
            service_account=service_account,
        )






    PROJECT_ID = 'visual-captions' # @param {type:"string"}
    LOCATION = 'us-central1'  # @param {type:"string"}


    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = ImageTextModel.from_pretrained("imagetext@001")

    source_image = Image(image_bytes=source_image_bytes)
    # print('The bytes', source_image, source_image_bytes)
    captions = model.get_captions(
        image=source_image,
        # Optional:
        number_of_results=2,
        language="en",
    )
    # print('image-to-text', captions)
    return captions
