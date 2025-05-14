## Preparations
Please download and set up these projects in the parent folder.  
  
sketch2scene  
├── flowty-realtime-lcm-canvas  
├── Stable Diffusion WebUI  
├── MIDI-3D  
├── ...  
...  
If you run Stable Diffusion WebUI as a background process and use API during this pipeline, you could also install it anywhere you like as long as you have the web link(port).  
  
### flowty-realtime-lcm-canvas: 
repository: https://github.com/flowtyone/flowty-realtime-lcm-canvas.git  
  
### Stable Diffusion WebUI
repository: https://github.com/AUTOMATIC1111/stable-diffusion-webui  
click-to-start version in bilibili: https://www.bilibili.com/video/BV1iM4y1y7oA
  
### MIDI: Multi-Instance Diffusion for Single Image to 3D Scene Generation: 
repository: https://github.com/VAST-AI-Research/MIDI-3D.git  
  
### Libraries Preparation
run `pip install -r requirements`  
These are libraries you need apart from requirements of the three given repositories.  
If there are some issues with that, you could instead run `pip install library1, library2, ...` in _imports_ in notebook file _sketch2scene.ipynb_.  
  
## Note:
- It is suggested that you must build a virtual env for **flowty-realtime-lcm-canvas** with gradio version 3.44.1.  
- Please run **Stable Diffusion WebUI** with port 7862 and **flowty-realtime-lcm-canvas** with 7860.  
- Conda is needed for this project.  
- It would be better if your input sketch image has nearly equivelant width and height.  
- Auto-segmentation doesn't reach the effect of manual one. In comparison, see this case(the former is the auto one):  
<img src="https://github.com/user-attachments/assets/a6954143-39a0-4073-8422-b83327e655be"  width="300" />
<img src="https://github.com/user-attachments/assets/36e60e71-403b-4a5e-8b72-21072c416f5d"  width="300" />   
  
## Launch:
### Automatically
I recommend this way when your sketch is not complex and not is without occlusion.  
  
Open notebook file _sketch2scene.ipynb_ and run.  
#### Imports
Paths of Windows flowty_env␣ and sketch_path should be set as yours.  
In the second cell: `flowty_env = r"Your flowty_env Python path"`  
In the third cell: `sketch_path = "Your sketch image path"`   
<img src="https://github.com/user-attachments/assets/f0a61e62-d762-4dc7-93e2-4b1e563525e7"  width="300" />   

  
#### Sketch to Image Stage
In "Prompts": `Prompt = input('Please simply describe your sketch with few words: ')`, input is required.  
In "Sketch to Image": If  
```
subprocess.run(
    'conda run -n flowty_env python sketch_to_image.py',
    # capture_output=True,
    text=True,
    check=True
)
```  
returncode != 0, you could wait for some time until _sketch_to_image_process_ is fully started.  
If the port of your _sketch_to_image_client_ is not 7860, you could open _sketch_to_image.py_ and edit `sketch_to_image_client = Client("Your client web link")`  
If you are not satisfied with the initial result, you could open _sketch_to_image.py_ and edit parameters in `sketch_to_image_result = sketch_to_image_client.predict...`  or edit your prompts.  
<img src="https://github.com/user-attachments/assets/9106dcba-be82-4baa-a651-4ca83d91f427"  width="300" />   

  
#### Image refinement Stage
If you don't have sdwebui as a Background Process at the moment, activate the cell and run  
```
sketch_to_image_process = subprocess.Popen(
    'conda run python stable-diffusion-webui/webui-user.py',
    # capture_output=True,
    text=True,
    shell=True
)
await asyncio.sleep(10)
```
To avoid some mistakes, you could also start running webui-user.py in cmd/shell so that the following process could go on.  
In "Image refinement with StableDiffusion", if the port of your _stable_diffusion_webui_ is not 7862, you could edit `url = "your sd-webui web link"`  
If you are not satisfied with the result, you could reset up sd-webui api with new parameters. The instructions are in the cell in raw.  
<img src="https://github.com/user-attachments/assets/f80187be-dca5-43c1-9c11-de48520891eb"  width="300" />   
  
#### Segmentation Stage
It is suggested that you run the segmentation in MIDI-3D webui so that you could manually set the number of objects and their positions.  
<img src="https://github.com/user-attachments/assets/7b6eec44-3dd6-4412-97ba-ee9568219683"  width="300" />   
Auto-segmentation doesn't reach the effect of manual one. In comparison, see the "manually" part.  
  
#### Model generation Stage
If you skip the auto-segmentation and manually get one, please edit:  
```
# source
src_seg_image = your_new_seg_img_path
```
You'll get a path of the generated glb file of your sketch in the output of the last cell.  
e.g: glb file generated at MIDI-3D/output/2025-05-13 16_51_42/output.glb  
<img src="https://github.com/user-attachments/assets/a5c54e81-9291-4bdd-8de9-3ccc57f583bd"  width="300" />  
<img src="https://github.com/user-attachments/assets/96dd2250-32e8-4cc4-9623-70d927004b56"  width="300" />  

  
**Demo:**  
See Notebook file _sketch2scene.ipynb_.  

### Manually
I recommend this way when you target at complex tasks which means there are many objects and occlusion in your sketch.  
  
Run ui.py in **flowty-realtime-lcm-canvas**, webui-user.py in **Stable Diffusion WebUI** and gradio_demo.py in **MIDI**.  
Draw your sketch in **flowty-realtime-lcm-canvas** web, do img2img for image refinement in **Stable Diffusion WebUI** and then run image segmentations and model generations in **MIDI-3D**.  
Save your glb file.  

**Demo:**  
Draw Sketch in **flowty-realtime-lcm-canvas**:    
<img src="https://github.com/user-attachments/assets/6dcc83a1-b1ba-42f0-bda5-3187e994c9a0"  width="300" />  
  
After **Sketch to Image Stage** you get:    
<img src="https://github.com/user-attachments/assets/54e2715b-96da-4458-848f-acb97c36eec2"  width="300" />  
  
Put it into **Stable Diffusion WebUI**, you get:  
<img src="https://github.com/user-attachments/assets/a96b3920-91cd-4b9b-ba82-e70efce781b3"  width="300" />  
  
With this refined image, in  **MIDI**, you get:  
<img src="https://github.com/user-attachments/assets/de4b4925-ddc9-4366-a240-cf6400e7d44c"  width="600" />  
  
## refs
@article{huang2024midi,  
  title={MIDI: Multi-Instance Diffusion for Single Image to 3D Scene Generation},  
  author={Huang, Zehuan and Guo, Yuanchen and An, Xingqiao and Yang, Yunhan and Li, Yangguang and Zou, Zixin and Liang, Ding and Liu, Xihui and Cao, Yanpei and Sheng, Lu},  
  journal={arXiv preprint arXiv:2412.03558},  
  year={2024}  
}

