import chainlit as cl
import google.generativeai as genai
import PIL 



model = genai.GenerativeModel('models/gemini-pro-vision')

@cl.on_chat_start
def on_chat_start():

    print("This chat is optimized for vision!")



@cl.on_message
async def on_message(message: cl.Message):
    for element in message.elements:
        print(element)

    img = PIL.Image.open(message.elements[0].path)

    response = model.generate_content([message.content,img])

    await cl.Message(response.text).send()


        