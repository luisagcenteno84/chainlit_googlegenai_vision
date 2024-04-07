import io
import chainlit as cl
import google.generativeai as genai
from google.cloud import storage
import PIL 
import requests


model = genai.GenerativeModel('models/gemini-pro-vision')

@cl.on_chat_start
def on_chat_start():

    print("This chat is optimized for vision!")



@cl.on_message
async def on_message(message: cl.Message):

    #print("Message:")
    #print(message)
    #print("Message Elements:")
    #print(message.elements)
    #for element in message.elements:
    #    print("Element:")
    #    print(element)
    # Get the BlobReader

    storage_client = storage.Client()
    bucket = storage_client.bucket('chainlit-genai-vision-bucket')
    blob = bucket.blob(message.elements[0].name)

    blob.upload_from_filename(message.elements[0].path)

    blob_as_string = blob.download_as_string()

    bytes = io.BytesIO(blob_as_string)
    img = PIL.Image.open(bytes)


    response = model.generate_content([message.content,img])

    await cl.Message(response.text).send()

    #await cl.Message("").send()