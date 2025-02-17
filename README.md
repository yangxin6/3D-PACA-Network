# 3D Point Cloud Central Axis Aggregation Network

## Network

![Fig4.jpg](imgs%2FFig4.jpg)
![Fig5.jpg](imgs%2FFig5.jpg)
## Environment

- Ubuntu 22.04
- Python 3.8
- Pytorch 2.1.0


```bash
conda create -n pointcept2 python=3.8 -y
conda activate pointcept2
conda install ninja -y
# Choose version you want here: https://pytorch.org/get-started/previous-versions/
# We use CUDA 11.8 and PyTorch 2.1.0 for our development of PTv3
conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=11.8 -c pytorch -c nvidia
conda install h5py pyyaml -c anaconda -y
conda install sharedarray tensorboard tensorboardx yapf addict einops scipy plyfile termcolor timm -c conda-forge -y
conda install pytorch-cluster pytorch-scatter pytorch-sparse -c pyg -y
pip install torch-geometric

cd libs/pointgroup_ops
python setup.py install
cd ../..


# PTv1 & PTv2 or precise eval
cd libs/pointops
# usual
python setup.py install

# spconv (SparseUNet)
# refer https://github.com/traveller59/spconv
pip install spconv-cu118  # choose version match your local cuda version

# Open3D (visualization, optional)
pip install open3d
```

FlashAttention

```bash
pip install flash-attn --no-build-isolation
```

## Dataset Prepare

Simulation Method of Point Cloud Data for Maize Populations：

1. Download: Physically Based Deformation of Single Maize Point Cloud Datasets \
    [link](https://www.kaggle.com/datasets/yangxin6/simulatio-maize-point-cloud-datasets)
2. run
```
python project/multi_gen_group_data_no_land.py
```


## Ground Truth Dataset
We conducted tests on a total of 17 datasets obtained from four types of sensors. The data catalog and test results are as follows:


| Data ID      | Data Name                | AP     |
| ------------ | ------------------------ |--------|
| $A^1$        | lidar__a.txt             | 0.7340 |
| $A^2$        | lidar__b.txt             | 0.7948 |
| $A^3$        | lidar__c.txt             | 0.8495 |
| $A^4$        | lidar__d.txt             | 0.9037 |
| $B^1$        | other__Maize-04_gt.txt   | 0.9808 |
| $B^2$        | other__grou_maize_gd.txt | 1.0    |
| $C^1$        | slam__slam_all.txt       | 0.9868 |
| $D^1$        | rgb__0707_Tian_30_gt.txt | 1.0    |
| $D^2$        | rgb__0707_502_30_gt.txt  | 1.0    |
| $D^3$        | rgb__0709_XY_20_gt.txt   | 0.8367 |
| $D^4$        | rgb__0709_XY_30_gt.txt   | 1.0    |
| $D^5$        | rgb__0721_Tian_20_gt.txt | 1.0    |
| $D^6$        | rgb__0729_Tian_30_gt.txt | 0.9738 |
| $E^1$        | DjiV4_clean_gt.txt       | 0.9011 |
| $E^2$        | StPaulV3_clean.txt       | 0.9675 |
| $E^3$        | StPaulV6_clean.txt       | 0.5403 |
| $E^4$        | WasecaV5_clean.txt       | 0.6561 |
|              | Average                  | 0.8897 |
| $A^1_{test}$ | 2-lidar__a.txt           | 0.7549 |
| $A^2_{test}$ | 2-lidar__b.txt           | 0.7822 |
| $A^3_{test}$ | 2-lidar__c.txt           | 0.8396 |
| $A^4_{test}$ | 2-lidar__d.txt           | 0.9203 |





The ground truth of the test data and our model’s prediction results are published at the following address: 
datasets [link](https://www.kaggle.com/datasets/yangxin6/test-point-cloud-datasets-of-mazie-population)



Additionally, we express our gratitude to several scholars who shared their data with us. We processed and annotated these data for testing purposes. The original links to these data include:
- [other__grou_maize_gd](https://linkinghub.elsevier.com/retrieve/pii/S2214514121002191)
- [other__Maize-04_gt](https://www.mdpi.com/2077-0472/12/9/1450)
- [uav__*](http://arxiv.org/abs/2107.10950)


## Train

```bash
python tools/train.py --config-file configs/corn3d_group/insseg-pointgroup-v2m1-0-pt3-base_no_land.py
```

## Test
1. Change the `configs/corn3d_group/insseg-pointgroup-v2m1-0-pt3-base.py` `test=True` in `model` dict.

2. run
```bash
python tools/test.py --config-file configs/corn3d_group/insseg-pointgroup-v2m1-0-pt3-base.py  --options save_path="{weight_path}"  weight="{weight_path}/model_best.pth"
```
We provide our best model weights here: [model_pth](https://www.kaggle.com/datasets/yangxin6/3d-point-cloud-central-axis-aggregation-network)



## Reference
- [Pointcept](https://github.com/Pointcept/Pointcept)

## Citation

If you find this project useful in your research, please consider cite:

