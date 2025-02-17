import genesis as gs
import torch

# initialize
gs.init(backend=gs.gpu)

# create scene
scene = gs.Scene(
    show_viewer= False,
    # viewer_options= gs.options.ViewerOptions(
    #     camera_pos = (3.5, -1.0, 2.5),
    #     camera_lookat = (0.0, 0.0, 0.5),
    #     camera_fov = 40.0,
    # ),
    rigid_options= gs.options.RigidOptions(
        dt = 0.01,
    ),
)

# add entities
plane = scene.add_entity(
    gs.morphs.Plane(),
)
franka = scene.add_entity(
    gs.morphs.MJCF(
        file="xml/franka_emika_panda/panda.xml",
    ),
)

# build scene
B = 30000
scene.build(
    n_envs=B,
    # env_spacing=(1.0, 1.0),
)

# set target position
franka.control_dofs_position(
    torch.tile(
        torch.tensor([0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.02, 0.02], device=gs.device),
        (B, 1),
    )
)

# run simulation
for i in range(1000):
    scene.step()