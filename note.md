
# Environment Setup

```bash
export CMAKE_PREFIX_PATH="$CMAKE_PREFIX_PATH:/eigen/path/under/conda"

export CMAKE_PREFIX_PATH="$CMAKE_PREFIX_PATH:/home/tiger/ProgramFiles/miniconda3/envs/foundationpose/include/eigen3"

CMAKE_PREFIX_PATH=$CONDA_PREFIX/lib/python3.9/site-packages/pybind11/share/cmake/pybind11 bash build_all_conda.sh

python -m pip install --no-index --no-cache-dir pytorch3d -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py39_cu121_pyt251/download.html
```


"ModuleNotFoundError: No module named 'torch'"
更改setuptools版本
```bash
pip uninstall setuptools && pip install setuptools==69.5.1
```

cuda版本不匹配
查看电脑cuda版本为12.5，装cu121适配的torch

找不到eigen
修改FoundationPose/bundlesdf/mycuda/setup.中的include_dirs=，添加
"/home/tiger/ProgramFiles/miniconda3/envs/foundationpose/include/eigen3"注意不能把用户主目录省略为~


pretty error 把conda搞坏了：
删干净/home/tiger/ProgramFiles/miniconda3/lib/python3.11/site-packages/sitecustomize.py 文件内容


ImportError: libcudart.so.11.0: cannot open shared object file: No such file or directory

当前的 PyTorch3D 安装是基于 CUDA 11.0 编译的，而您的系统中没有安装对应的 CUDA 运行时



run_nerf.py 98 行 ：use_refined_mask=False


可以正常cmake的配置
torch                     2.5.1+cu121              pypi_0    pypi
torchaudio                2.5.1+cu121              pypi_0    pypi
torchnet                  0.0.4                    pypi_0    pypi
torchvision               0.20.1+cu121             pypi_0    pypi


跑bundlesdf/run_nerf.py, import gridencoder报错
torch==2.0.0+cu118
torchvision==0.15.1+cu118
torchaudio==2.0.1+cu118




**最终解决办法**：安装cuda11.8，在home目录写一个脚本一键切换cuda版本

**自由切换cuda版本**
https://www.bilibili.com/opus/952516543885869090?from=search

export LD_PRELOAD=/home/tiger/ProgramFiles/miniconda3/envs/env_isaaclab/lib/python3.10/site-packages/omni/libcarb.so


按这个教程用pip安装sim和lab，正常。
https://isaac-sim.github.io/IsaacLab/release/2.1.0/source/setup/installation/pip_installation.html


# Run Commands

## linemod dataset Download
1. 在https://bop.felk.cvut.cz/datasets/ 找到linemod数据集
在此 https://huggingface.co/datasets/bop-benchmark/lm/resolve/main/lm_test_all.zip 下载`lm_test_all` 
下载LM的两个压缩包：`All test images`解压到`lm_test_all`文件夹，`Object models`解压到`models`文件夹
2. 在 https://drive.google.com/drive/folders/19ivHpaKm9dOrr12fzC8IDFczWRPFxho7 下载`Linemod_preprocessed`

`/home/tiger/Downloads/Dataset`之下的文件结构为

```bash
LINEMOD
    lm_test_all
        test
    models
    Linemod_preprocessed
```

## Commands
### demo
命令行指定mesh_file和test_scene_dir（或者直接在代码中修改默认路径）切换识别不同物体（手钻和芥末瓶）




### linemod dataset
```bash
# 1 model-based version
python run_linemod.py --linemod_dir /home/tiger/Disk/Downloads/Dataset/LINEMOD --use_reconstructed_mesh 0
#下载正确的数据集后能正常运行 

# 2 model-free few-shot version
#使用bundlesdf生成物体3d模型
python bundlesdf/run_nerf.py --ref_view_dir /home/tiger/Disk/Downloads/Dataset/LINEMOD/ref_views --dataset linemode 
#已经训练过

python run_linemod.py --linemod_dir /home/tiger/Disk/Downloads/Dataset/LINEMOD --use_reconstructed_mesh 1 --ref_view_dir /home/tiger/Disk/Downloads/Dataset/LINEMOD/ref_views
#正常运行，没有可视化
```


### ycb数据集
```bash
python run_ycb_video.py --ycbv_dir /mnt/9a72c439-d0a7-45e8-8d20-d7a235d02763/DATASET/YCB_Video --use_reconstructed_mesh 0
#还没下载ycb数据集
```