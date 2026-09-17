# 代码与数据清单 — Xenium 数据Utility优化

## 一、代码清单

| 资源 | URL | 许可证 | 备注 |
|------|-----|--------|------|
| Xenium_benchmarking | https://github.com/Moldia/Xenium_benchmarking v1.2.0 | MIT | 主要分析代码 |
| Python packages | 详见下方列表 | 混合 | 完整依赖列表 |
| R packages | Seurat (4.3.0), SeuratObject (4.1.3), Giotto (1.1.2) | 混合 | 统计分析 |

### Python 包完整列表
```
affine==2.4.0
anndata==0.8.0
alohashape==1.3.1
biopython==1.81
click==8.1.5
click-log==0.4.0
click-plugins==1.1.1
cloudpickle==2.1.0
contextily==1.3.0
cython==3.0.2
dask==2022.2.0
dask-image==2021.12.0
descartes==1.1.0
doubletdetection==4.2
fiona==1.9.5
geographiclib==2.0
geopandas==0.10.2
geopy==2.4.0
gprofiler-official==1.0.0
hspy==3.7.0
holoviews==1.16.2
igraph==0.9.11
imagecodecs==2021.11.20
imageio==2.21.0
leidenalg==0.8.10
libpysal==4.7.0
louvain==0.7.2
matplotlib==3.5.2
matplotlib-scalebar==0.8.1
matplotlib-venn==0.11.9
mygene==3.2.2
naivede==1.2.0
networkx==2.6.3
numba==0.56.0
numpy==1.21.6
omnipath==1.0.5
pandas==1.3.5
phenograph==1.5.7
pooch==1.7.0
pydantic==1.9.1
pynndescent==0.5.7
pyparsing==3.0.9
pyproj==3.2.1
rasterio==1.2.10
rtree==1.0.1
scanpy==1.9.1
scikit-image==0.19.3
scikit-learn==1.0.2
scipy==1.7.3
seaborn==0.11.2
shapely==2.0.1
spatialde==1.1.3
spatialdm==0.1.0
squidpy==1.2.2
statsmodels==0.13.2
tifffile==2021.11.2
toolz==0.12.0
tqdm==4.64.0
umap-learn==0.5.3
xarray==0.20.2
zarr==2.12.0
```

---

## 二、数据清单

| 数据类型 | 存储位置 | 访问号/URL | 说明 |
|----------|----------|------------|------|
| Xenium 原始数据 | 10X Genomics | https://www.10xgenomics.com/datasets | 商业平台数据 |
| Mouse brain 新鲜数据 | Zenodo | https://doi.org/10.5281/zenodo.10566172 | 4个小鼠脑组织切片 |
| AnnData objects (1) | Zenodo | https://doi.org/10.5281/zenodo.11124988 | 预处理后的AnnData |
| AnnData objects (2) | Zenodo | https://doi.org/10.5281/zenodo.11121221 | 预处理后的AnnData |
| AnnData objects (3) | Zenodo | https://doi.org/10.5281/zenodo.11120307 | 预处理后的AnnData |
| Resegmented datasets | Zenodo | https://doi.org/10.5281/zenodo.11619309 | 重分割和区域注释数据 |
| MERSCOPE data | Vizgen | https://vizgen.com/data-release-program/ | 商业平台数据门户 |
| CosMx data | NanoString | https://nanostring.com/products/cosmx-spatial-molecular-imager/ffpe-dataset/ | FFPE数据集 |
| Molecular Cartography | Resolve Biosciences | https://resolvebiosciences.com/datasets/ | 多重荧光原位杂交 |
| MERFISH data | 原发表文献 | 原始发表文献(3,4) | 来自原始出版物 |
| HS-ISS data | 原发表文献 | 原始发表文献(3,4) | 来自原始出版物 |
| Allen brain atlas | Allen Institute | https://portal.brain-map.org/atlases-and-data/bkp/abc-atlas | ABC atlas单细胞数据 |

---

## 三、复现可行性

| 分析 | 状态 | 说明 |
|------|------|------|
| Xenium数据预处理 | ✅ 可完全复现 | GitHub代码开源，Scanpy处理流程 |
| 分割算法比较 | ✅ 可完全复现 | Cellpose/Baysor/Watershed均开源 |
| 预处理流程优化 | ✅ 可完全复现 | 参数搜索代码可获取 |
| SVF识别算法 | ⚠️ 部分受限 | 部分算法(如Seurat)计算成本高 |
| SRT平台比较 | ⚠️ 部分受限 | 需访问各平台数据门户 |
| 新鲜组织实验 | ❌ 无法直接复现 | 需原始Xenium仪器和样本 |

---

## 状态说明

- ✅ **可完全复现**（工具/代码开源可获取）
- ⚠️ **部分受限**（需注册/需商业许可）
- ❌ **无法直接复现**（需原始样本/仪器）
