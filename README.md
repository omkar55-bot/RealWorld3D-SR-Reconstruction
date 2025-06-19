# 📸 Real-World 3D Super-Resolution Reconstruction

This repository presents my research on enabling **3D reconstruction from low-resolution real-world images** using the following state-of-the-art neural rendering techniques:
- [3D Gaussian Splatting (3DGS)](https://github.com/graphdeco-inria/gaussian-splatting)
- [Instant-NGP (NeRF)](https://github.com/NVlabs/instant-ngp)
- [NeRF-SR (Super-Resolution NeRF)](https://github.com/jxkaye/NeRF-SR)

> 🧪 Research conducted at Clemson University – Advanced Imaging Lab  
> 📝 Co-authored paper submitted to NeurIPS 2025

---

## 🧠 Research Motivation & Technical Contributions

This research project focuses on **adapting and patching 3DGS, Instant-NGP, and NeRF-SR** to support **3D reconstruction from low-resolution input images** — a critical capability for applications where high-resolution image capture is not feasible (e.g., mobile, embedded, or real-time capture systems).

### 🔧 Blender vs LLFF Dataset Handling

- The **Blender Synthetic Dataset** supports resolution changes easily, as it only depends on a single camera parameter: `camera_angle_x`.
- The remaining intrinsics (`focal_x`, `cx`, `cy`) are **hardcoded** inside Blender dataset loaders for:
  - ✅ 3D Gaussian Splatting (3DGS)
  - ✅ NeRF-SR
  - ✅ Instant-NGP

- In contrast, **LLFF datasets** require explicit and accurate intrinsics (full `fl_x`, `fl_y`, `cx`, `cy`, and `image dimensions`). Without correcting these values during downsampling, **rendering artifacts and distortions** occur — especially with resolutions like 100×100 or 200×200.

### 🛠 Key Contributions

- ✅ **Patched the data loaders** in 3DGS, Instant-NGP, and NeRF-SR to:
  - Load LLFF datasets at arbitrary resolutions
  - Rescale camera intrinsics properly to preserve field-of-view
  - Eliminate distortions caused by mismatched intrinsics
- ✅ Enabled training these models on **real-world LLFF-style datasets** captured with simple handheld cameras
- ✅ Significantly improved rendering quality on low-resolution data, enabling **super-resolution 3D reconstruction pipelines** from everyday image sources

---

## 🚀 Super-Resolution with 3D Gaussian Splatting

In addition to dataset preprocessing, I also **modified the 3DGS training pipeline** to perform a **super-resolution learning task**:

- 🎯 The model is trained using **low-resolution images** as input
- 🧠 The **loss function** is computed using the corresponding **high-resolution images** as targets
- 🖼️ This results in **blurry but high-resolution renderings**, made possible by 3DGS’s rasterization framework
- 📈 Even without explicit VSR priors, this setup enables **upsampled 3D outputs**, leveraging geometry-aware splatting as an inductive bias

---

## 🎯 Why This Matters

| Challenge                              | Solution                                 |
|----------------------------------------|------------------------------------------|
| Real-world low-res input images        | ✅ Patched loaders & preprocessing        |
| Distorted rendering from incorrect intrinsics | ✅ Intrinsics scaling logic             |
| No super-resolution support in 3DGS    | ✅ Modified loss computation pipeline     |

This pipeline enables **high-quality 3D reconstruction from low-resolution real-world imagery**, making modern neural rendering significantly more **accessible, deployable, and robust**.

---

## 🛠 Scripts

| Script                       | Description                              |
|-----------------------------|------------------------------------------|
| `train_3dgs_lowres.sh`      | Train 3DGS on low-resolution LLFF inputs |
| `train_ngp_lowres.sh`       | Train Instant-NGP with downsampled data  |
| `train_nerf_sr.sh`          | Train NeRF-SR with low-res to high-res   |
| `upscale_realbasicvsr.py`   | Upscale input images using RealBasicVSR  |
| `generate_camera_path.py`   | Create spiral path for rendering         |

```bash
# Example usage
bash scripts/train_3dgs_lowres.sh
python scripts/upscale_realbasicvsr.py --input input_dir --output output_dir

