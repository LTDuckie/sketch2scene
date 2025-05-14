# Project Report: Sketch to Scene

## 1. Project Overview
### 1.1 Project Introduction
The "Sketch to Scene" project aims to transform hand - drawn sketches into 3D scenes. It involves multiple stages including sketch to image conversion, image refinement, image segmentation and 3D model generation. This project combines different technologies and libraries to achieve the goal, providing an innovative way to bring 2D sketches to life in a 3D space.

### 1.2 GitHub Repository
The project's source code and documentation are available on GitHub at [https://github.com/LTDuckie/sketch2scene/blob/master/README.md](https://github.com/LTDuckie/sketch2scene/blob/master/README.md).

## 2. Background Research
### 2.1 Related Work
The field of converting 2D sketches to 3D models has seen significant development in recent years. Technologies like Stable Diffusion have been widely used for image generation and refinement. For example, the Stable Diffusion WebUI is a popular tool that allows users to generate high - quality images based on text prompts and input images. 

Image to Model:  
The MIDI (Multi - Instance Diffusion for Single Image to 3D Scene Generation) approach introduced in the paper [@article{huang2024midi,  
  title={MIDI: Multi-Instance Diffusion for Single Image to 3D Scene Generation},  
  author={Huang, Zehuan and Guo, Yuanchen and An, Xingqiao and Yang, Yunhan and Li, Yangguang and Zou, Zixin and Liang, Ding and Liu, Xihui and Cao, Yanpei and Sheng, Lu},  
  journal={arXiv preprint arXiv:2412.03558},  
  year={2024}  
}] is also a key reference for this project. It provides a method for generating 3D scenes from a single image.  

Sketch to model： 
Sketch2Model: View-Aware 3D Modeling from Single Free-Hand Sketches  

Sketch to scene： 
Sketch2Scene: Sketch-based Co-retrieval and Co-placement of 3D Models  

Sketch to image: 
flowty - realtime - lcm - canvas  

Depth and segmentation of Image:  
  
Image to Image generation:  


### 2.2 Motivation
The motivation behind this project is to simplify the process of 3D scene creation. Traditional 3D modeling methods often require professional skills and a significant amount of time. By using sketches as input, users with basic drawing skills can quickly generate 3D scenes, which has potential applications in fields such as game development, interior design, and virtual reality.

## 3. Methodology and Experiments
### 3.1 Preparations
#### 3.1.1 Project Setup
The project requires the download and setup of several external repositories:
- **flowty - realtime - lcm - canvas**: Repository: [https://github.com/flowtyone/flowty - realtime - lcm - canvas.git](https://github.com/flowtyone/flowty - realtime - lcm - canvas.git)
- **Stable Diffusion WebUI**: Repository: [https://github.com/AUTOMATIC1111/stable - diffusion - webui](https://github.com/AUTOMATIC1111/stable - diffusion - webui). There is also a click - to - start version available on Bilibili: [https://www.bilibili.com/video/BV1iM4y1y7oA](https://www.bilibili.com/video/BV1iM4y1y7oA)
- **MIDI - 3D**: Repository: [https://github.com/VAST - AI - Research/MIDI - 3D.git](https://github.com/VAST - AI - Research/MIDI - 3D.git)

#### 3.1.2 Libraries Installation
The necessary libraries are listed in the `requirements.txt` file. Users can run `pip install -r requirements` to install them. If there are issues, they can install the libraries individually in the `imports` section of the `sketch2scene.ipynb` notebook. Some of the key libraries include `gradio`, `diffusers`, `torch`, etc.

### 3.2 Launching the Project
#### 3.2.1 Automatic Launch
- **Imports**: Users need to set the paths of the Windows `flowty_env` and the sketch image according to their own environments. In the `sketch2scene.ipynb` notebook, they should set `flowty_env = r"Your flowty_env Python path"` and `sketch_path = "Your sketch image path"`.
- **Sketch to Image Stage**:
    - In the "Prompts" section, users need to describe their sketch with a few words. The prompt is read from the `UserPrompt.txt` file.
    - The `sketch_to_image.py` script is used to convert the sketch to an image. It uses the `gradio_client` to interact with a local server (`http://127.0.0.1:7860/` by default). If the port is different, users can edit the `sketch_to_image_client` in the `sketch_to_image.py` file.
- **Image refinement Stage**: If the Stable Diffusion WebUI is not running as a background process, users can activate a cell in the notebook to start it using `subprocess.Popen`. They can also start it manually in the command line. If the port of the Stable Diffusion WebUI is not 7862, they can edit the relevant URL.
- **Model generation Stage**: If users skip the auto - segmentation and have a manual segmentation, they need to edit the `src_seg_image` variable with the new segmentation image path. The final output is a glb file of the 3D model.

#### 3.2.2 Manual Launch
This method is recommended for complex sketches with many objects and occlusion. Users need to run `ui.py` in `flowty - realtime - lcm - canvas`, `webui - user.py` in `Stable Diffusion WebUI`, and `gradio_demo.py` in `MIDI`. They draw the sketch in the `flowty - realtime - lcm - canvas` web, perform image refinement in the `Stable Diffusion WebUI`, and then run image segmentations and model generations in `MIDI - 3D`. Finally, they save the generated glb file.

### 3.3 Experiments
We conducted experiments using different types of sketches, including simple sketches without occlusion and complex sketches with multiple objects. For simple sketches, the automatic launch method worked well, generating 3D models in a relatively short time. However, for complex sketches, the manual launch method provided better results as it allowed for more control over the segmentation and generation process.  
![3fb5bdbf3b12972c0b56bd6cf5b062f](https://github.com/user-attachments/assets/2c7d60b6-6254-4f5c-8487-7492227c35af)  
![064c50753637540f5344409db3ddd8f](https://github.com/user-attachments/assets/98fe1f8a-5f63-4610-a57c-229086639a97)  


![ea39b746ebaccc2a8384736f43111b6](https://github.com/user-attachments/assets/5cf046b9-81b7-478f-abd9-7862bab14748)  
![67361373137bed683171385fe03de15](https://github.com/user-attachments/assets/3198ef11-6b6e-46f3-b232-86ff24654503)  
![d059dff9ca61344a3c14c20be6ba019](https://github.com/user-attachments/assets/c1554f07-6da8-435a-944f-bfbd72aafdb8)  
![cce1eccc4ea0dada2c5216ad7504421](https://github.com/user-attachments/assets/48328513-d4ef-45b4-8206-969a0445d76e)  

## 4. Critical Self - Evaluation
### 4.1 Strengths
- **User - friendly**: The project provides both automatic and manual launch methods, catering to users with different levels of skills and sketch complexity.
- **Modularity**: The use of external repositories and APIs makes the project modular and easy to extend. For example, users can replace the Stable Diffusion WebUI with other image generation tools if needed.
- **Documentation**: The README file in the GitHub repository provides detailed instructions on project setup, launch methods, and related notes, which is helpful for new users.

### 4.2 Weaknesses
- **Dependency on External Tools**: The project relies on several external repositories and libraries. Any changes or issues in these dependencies can affect the project's functionality. For example, if the Stable Diffusion WebUI updates its API, the `sketch_to_image.py` script may need to be modified.
- **Segmentation Quality**: The auto - segmentation in the project does not achieve the same effect as manual segmentation. This can lead to inaccurate 3D model generation, especially for complex sketches.
- **Performance**: The image generation and 3D model generation processes can be time - consuming, especially for high - resolution sketches or when using complex models.

### 4.3 Future Improvements
- **Improve Segmentation Algorithm**: Investigate and implement more advanced segmentation algorithms to improve the accuracy of auto - segmentation.
- **Optimize Performance**: Explore techniques such as model quantization and parallel processing to reduce the processing time of image generation and 3D model generation.
- **Enhance User Interface**: Develop a more intuitive and user - friendly interface to simplify the interaction process, especially for non - technical users.
