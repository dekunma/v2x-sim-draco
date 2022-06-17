import numpy as np
import open3d as o3d
import os

def convert_bin_pcd_to_ply(input_file_name, output_dir='ply_data'):
    scan = np.fromfile(input_file_name, dtype=np.float32)
    points = scan.reshape((-1, 5))[:, :4]
    xyz = points[:, 0:3]
    pcd = o3d.t.geometry.PointCloud()
    pcd.point["positions"] = o3d.core.Tensor(xyz)
    
    # i = [[i] for i in points[:, 3]]
    # pcd.point["intensities"] = o3d.core.Tensor(i)
    
    file_name_no_extension = os.path.basename(input_file_name).split('.')[0]
    parent_dir = input_file_name.split('/')[-2]

    output_file_name = f'{file_name_no_extension}.ply'
    output_path = os.path.join(output_dir, parent_dir)
    os.makedirs(output_path, exist_ok=True)
    output_path = os.path.join(output_path, output_file_name)
    o3d.t.io.write_point_cloud(output_path, pcd)
    return output_file_name

def draco_compress(input_file_name, input_file_dir, output_dir='draco_intermediate', compress_level=10):
    output_file_name = input_file_name.split('.')[0] + '.drc'
    agent_dir = input_file_dir.split('/')[1]
    output_path = os.path.join(output_dir, agent_dir)
    os.makedirs(output_path, exist_ok=True)
    output_path = os.path.join(output_path, output_file_name)
    os.system(f'./draco/build/draco_encoder -point_cloud -i {input_file_dir}/{input_file_name} -o {output_path} -cl {compress_level}')
    return output_file_name

def draco_decompress(input_file_name, input_file_dir, output_dir='draco_output'):
    output_file_name = input_file_name.split('.')[0] + '.ply'
    agent_dir = input_file_dir.split('/')[1]
    output_path = os.path.join(output_dir, agent_dir)
    os.makedirs(output_path, exist_ok=True)
    output_path = os.path.join(output_path, output_file_name)
    os.system(f'./draco/build/draco_decoder -i {input_file_dir}/{input_file_name} -o {output_path}')
    return output_file_name

def convert_ply_to_bin_pcd(input_file_name, input_file_dir, output_dir='final_output'):
    pcd = o3d.io.read_point_cloud(os.path.join(input_file_dir, input_file_name))
    points = np.asarray(pcd.points)
    points = np.concatenate((points, np.ones(points.shape[0] * 2).reshape(-1, 2)), axis=1)
    points = points.reshape(-1, )
    output_file_name = input_file_name.split('.')[0] + '.pcd.bin'
    agent_dir = input_file_dir.split('/')[1]
    output_path = os.path.join(output_dir, agent_dir)
    os.makedirs(output_path, exist_ok=True)
    output_path = os.path.join(output_path, output_file_name)
    points.astype(np.float32).tofile(output_path)