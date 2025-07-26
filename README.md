# 3D Point Cloud Paired-Attention Central Axis Aggregation Network

## Network

![PACANet](imgs%2FFig4.jpg)

![3DPA](imgs%2FFig5.jpg)

## Environment

- Ubuntu 22.04
- Python 3.8
- Pytorch 2.1.0


```bash
sudo apt-get install libsparsehash-dev

conda env create -f environment.yaml 

cd libs/pointgroup_ops
python setup.py install
cd ../..


# PTv1 & PTv2 or precise eval
cd libs/pointops
# usual
python setup.py install


cd libs/pointgroup_ops
python setup.py install
cd ../..


# PTv1 & PTv2 or precise eval
cd libs/pointops
# usual
python setup.py install


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
|              | Average                  | 0.9246 |
| $E^1$        | DjiV4_clean_gt.txt       | 0.9011 |
| $E^2$        | StPaulV3_clean.txt       | 0.9675 |
| $E^3$        | StPaulV6_clean.txt       | 0.5403 |
| $E^4$        | WasecaV5_clean.txt       | 0.6561 |
| $A^1_{test}$ | 2-lidar__a.txt           | 0.7549 |
| $A^2_{test}$ | 2-lidar__b.txt           | 0.7822 |
| $A^3_{test}$ | 2-lidar__c.txt           | 0.8396 |
| $A^4_{test}$ | 2-lidar__d.txt           | 0.9203 |





The ground truth of the test data and prediction results are published at the following address: 
- datasets: [link](https://www.kaggle.com/datasets/yangxin6/mazie-population-datasets)
- pred label: [link](https://www.kaggle.com/datasets/yangxin6/pacanet-pred)


Additionally, we express our gratitude to several scholars who shared their data with us. We processed and annotated these data for testing purposes. The original links to these data include:
- [other__grou_maize_gd](https://linkinghub.elsevier.com/retrieve/pii/S2214514121002191)
- [other__Maize-04_gt](https://www.mdpi.com/2077-0472/12/9/1450)
- [uav__*](http://arxiv.org/abs/2107.10950)


## Train

```bash
python tools/train.py --config-file configs/corn3d_group/insseg-pointgroup-v2m1-0-pt3m2-base.py
```

## Test
1. Change the `configs/corn3d_group/insseg-pointgroup-v2m1-0-pt3m2-base.py` `test=True` in `model` dict.

2. run
```bash
python tools/test.py --config-file configs/corn3d_group/insseg-pointgroup-v2m1-0-pt3m2-base.py  --options save_path="{weight_path}"  weight="{weight_path}/model_best.pth"
```
We provide our best model weights here: [model_pth](https://www.kaggle.com/datasets/yangxin6/pacanet-model-pth)



## Reference
- [Pointcept](https://github.com/Pointcept/Pointcept)

## Citation

If you find this project useful in your research, please consider cite:

