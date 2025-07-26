"""
@author: yangxin6
@contact: yangxinnc@163.com
@license: Apache Licence
@file: txt_2_pth.py
@time: 2025/7/26 19:40
"""

import os
from shutil import copy
import open3d as o3d
import numpy as np
import torch
from tqdm import tqdm


def calculate_normals(coords, k_neighbors=10, radius=None):
    """
    计算点云的法线。

    参数:
    - coords: Nx3的NumPy数组，表示点云的坐标。
    - k_neighbors: 用于估计每个点法线的最近邻的数量。
    - radius: 搜索半径，用于估计每个点的法线。如果指定了radius，则使用半径搜索而不是k最近邻搜索。

    返回:
    - normals: Nx3的NumPy数组，表示每个点的法线向量。
    """
    # 将coords数组转换为Open3D的点云对象
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(coords)

    # 计算法线
    if radius is not None:
        # 使用半径搜索来计算法线
        pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=radius, max_nn=k_neighbors))
    else:
        # 使用k最近邻搜索来计算法线
        pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamKNN(knn=k_neighbors))

    # 可选：根据视点方向翻转法线
    # pcd.orient_normals_towards_camera_location(camera_location=np.array([0, 0, 0]))

    # 从点云对象中提取法线并转换为NumPy数组
    normals = np.asarray(pcd.normals)

    return normals
def txt_2_pth():
    data_root = "/home/yangxin/datasets/data_public/"
    target_root = "/home/yangxin/datasets/data_public/pth"
    os.makedirs(target_root, exist_ok=True)

    for item in tqdm(os.listdir(data_root)):
        data = np.loadtxt(os.path.join(data_root, item))
        xyz = data[:, :3]

        color = np.zeros_like(xyz)
        scene_id = item[:-4]
        instance = data[:, -1]
        _, instance = np.unique(instance, return_inverse=True)
        instance = instance.reshape([-1])
        segment = np.zeros_like(instance)

        normal = calculate_normals(xyz)
        torch.save(
            {
                "coord": xyz,
                "color": color,
                "normal": normal,
                "semantic_gt": segment,
                "instance_gt": instance,
                "scene_id": scene_id,
                # "superpoint": get_superpoint(group_plant_shuffled, normal)
            },
            os.path.join(target_root, item.replace(".txt", ".pth"))
        )
