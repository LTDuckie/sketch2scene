# In[1]:

from gradio_client import Client



# # In[3]:


sketch_to_image_client = Client("http://127.0.0.1:7860/")


# # In[5]:


with open("UserPrompt.txt", "r") as f:
    Prompt = f.read().strip()


# # In[ ]:

with open("sketch_path.txt", "r") as f:
    sketch_path = f.read().strip()


sketch_to_image_result = sketch_to_image_client.predict(
				Prompt,	# str in 'Prompt' Textbox component
				sketch_path,	# str (filepath or URL to image)
								# in 'parameter_14' Image component
				4,	# int | float (numeric value between 4 and 8)
								# in 'steps' Slider component
				1,	# int | float (numeric value between 0.1 and 3)
								# in 'cfg' Slider component
				0.9,	# int | float (numeric value between 0.1 and 0.9)
								# in 'sketch strength' Slider component
				-1,	# int | float in 'seed' Number component
				fn_index=0
)


# # In[11]:


with open("output.txt", "w") as f:
    f.write(sketch_to_image_result)


# # In[ ]:




