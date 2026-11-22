import pytest
import render.gaussian_splat_render as mod

CASES = [
    ("per_point_sort", (1.0, 2.0)),
    ("gpu_sort", (1000000, 2)),
    ("distance_projection", (2.0, 3.0)),
    ("depth_read_only", (1, 2)),
    ("linear_blend", (0.5, 0.2)),
    ("per_point_cull", (1, 2)),
    ("lod_tier", (100.0, 3)),
    ("covariance_update", (1.0, 2.0)),
    ("scene_order", (1, 2)),
    ("float32_pos", (1000000.0, 1000000.0)),
    ("splat_scale", (0.5, 2.0)),
    ("opacity_blend", (0.3, 0.7)),
    ("tile_bounds", (16, 16)),
    ("sort_key", (1.0, 2.0)),
    ("cull_bounds", (2.0, 3.0)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
