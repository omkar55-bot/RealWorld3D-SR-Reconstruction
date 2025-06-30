import json
import numpy as np
from scipy.spatial.transform import Rotation as R

def nerf_to_ngp(xf):
    mat = np.copy(xf)
    mat = mat[:-1, :]
    mat[:, 1] *= -1  # flip Y
    mat[:, 2] *= -1  # flip Z
    mat[:, 3] *= 0.33
    mat[:, 3] += [0.5, 0.5, 0.5]
    mat = mat[[1, 2, 0], :]
    rm = R.from_matrix(mat[:, :3])
    return rm.as_quat(), mat[:, 3] + 0.025

def full_camera_path(path_to_transforms):
    out = {"path": [], "time": 1.0}

    with open(f"{path_to_transforms}/transforms1.json") as f:
        data = json.load(f)

    for frame in data["frames"]:
        xf = np.array(frame["transform_matrix"])
        q, t = nerf_to_ngp(xf)
        out["path"].append({
            "R": list(q),
            "T": list(t),
            "dof": 0.0,
            "fov": 43,
            "scale": 0,
            "slice": 0.0
        })

    with open(f"{path_to_transforms}/base_cam.json", "w") as f:
        json.dump(out, f, indent=2)

    print(f"✅ base_cam102.json written with {len(out['path'])} cameras.")

# Run the script
full_camera_path('new/')
