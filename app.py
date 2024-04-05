import chainlit as cl
import google.generativeai as genai

model = genai.GenerativeModel('models/gemini-pro-vision')

@cl.on_chat_start
def on_chat_start():

    print("This chat is optimized for vision!")



@cl.on_message
async def on_message(message: cl.Message):
    response = model.generate_content(message.content)
    await cl.Message(response.text).send()


        