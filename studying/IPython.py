import genesis as gs

# 初期化
gs.init(backend=gs.gpu)

# シーンの作成
scene = gs.Scene(show_viewer=False)

# シーンにエンティティを追加
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(
    gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
)
cam_0 = scene.add_camera()

# シーンのビルド
scene.build()

# IPythonのインタラクティブモードに入る
import IPython; IPython.embed()