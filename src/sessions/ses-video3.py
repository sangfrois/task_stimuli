from ..tasks import images, video, memory, task_base

TASKS = [

    video.SingleVideo(
        'data/videos/Oceans_fs_10m/Inscapes_sound_normed.mp4', name='Inscapes'),
    video.SingleVideo(
        'data/videos/Oceans_fs_10m/Inscapes_sound_normed.mp4', name='Inscapes'),

    task_base.Pause(),

    video.SingleVideo(
        'data/videos/Oceans_fs_10m_filt/Oceans_fs_10m_8_filt.mp4',
        name='Oceans_fs_10m_8'),
    video.SingleVideo(
        'data/videos/Oceans_fs_10m_filt/Oceans_fs_10m_9_filt.mp4',
        name='Oceans_fs_10m_9'),
    video.SingleVideo(
        'data/videos/Oceans_fs_10m_filt/Oceans_fs_10m_10_filt.mp4',
        name='Oceans_fs_10m_10'),
    video.SingleVideo(
        'data/videos/Oceans_fs_10m_filt/Oceans_fs_10m_11_filt.mp4',
        name='Oceans_fs_10m_11'),

]
