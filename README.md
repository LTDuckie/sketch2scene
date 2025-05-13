## Please download and set up these projects in the parent folder.

sketch2scene  
├── flowty-realtime-lcm-canvas  
├── Stable Diffusion WebUI  
├── MIDI-3D  
├── ...  
...  

### flowty-realtime-lcm-canvas: 
repository: https://github.com/flowtyone/flowty-realtime-lcm-canvas.git  

### Stable Diffusion WebUI
repository: https://github.com/AUTOMATIC1111/stable-diffusion-webui  

### MIDI: Multi-Instance Diffusion for Single Image to 3D Scene Generation: 
repository: https://github.com/VAST-AI-Research/MIDI-3D.git  

### Libraries Preparation
run `pip install -r requirements`  

## Note:
It is suggested that you must build a virtual env for **flowty-realtime-lcm-canvas** with gradio version 3.44.1.  
Please run **Stable Diffusion WebUI** with port 7862 and **flowty-realtime-lcm-canvas** with 7860.  

## Launch:
### Automatically
Open notebook file _sketch2scene.ipynb_ and run.  
Paths of Windows flowty_env␣ and sketch_path should be set as yours.  
It is suggested that you run the segmentation in MIDI-3D webui so that you could manually set the number of objects and their positions.  

**Demo:**  
See Notebook file _sketch2scene.ipynb_.  

### Manually
Run ui.py in **flowty-realtime-lcm-canvas**, webui-user.py in **Stable Diffusion WebUI** and gradio_demo.py in **MIDI**.  
Draw your sketch in **flowty-realtime-lcm-canvas** web, do img2img for image refinement in **Stable Diffusion WebUI** and then run image segmentations and model generations in **MIDI-3D**.  
Save your glb file.

**Demo:**  
In stage 1  
![ab3ccd44d64fc6fec4fcb3323e04f9e](https://github.com/user-attachments/assets/6dcc83a1-b1ba-42f0-bda5-3187e994c9a0)  
In stage 2  
![7260b300ee0f96aab0e4707e56557aa](https://github.com/user-attachments/assets/54e2715b-96da-4458-848f-acb97c36eec2)  
In stage 3 & 4  
![b4ce8e3544ffd066bc887824360488b](https://github.com/user-attachments/assets/a96b3920-91cd-4b9b-ba82-e70efce781b3)  
![be84716d18cb0c6c13fb75fff311be2](https://github.com/user-attachments/assets/de4b4925-ddc9-4366-a240-cf6400e7d44c)  


## refs
@article{huang2024midi,  
  title={MIDI: Multi-Instance Diffusion for Single Image to 3D Scene Generation},  
  author={Huang, Zehuan and Guo, Yuanchen and An, Xingqiao and Yang, Yunhan and Li, Yangguang and Zou, Zixin and Liang, Ding and Liu, Xihui and Cao, Yanpei and Sheng, Lu},  
  journal={arXiv preprint arXiv:2412.03558},  
  year={2024}  
}

