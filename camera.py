import os
import shutil

try:
    from gi.repository import Gst
    Gst.init(None)

    v4l2_device = "/dev/video1"
    pipeline_str = "v4l2src device={device} num-buffers=1 ! jpegenc ! filesink location={{img}}".format(device=v4l2_device)

    def take_pic(file_path):

        # Build the pipeline
        pipeline = Gst.parse_launch(pipeline_str.format(img=file_path))

        # Start playing
        pipeline.set_state(Gst.State.PLAYING)

        # Wait until error or EOS
        bus = pipeline.get_bus()
        msg = bus.timed_pop_filtered(
            Gst.CLOCK_TIME_NONE, Gst.MessageType.ERROR | Gst.MessageType.EOS)

        # Free resources
        pipeline.set_state(Gst.State.NULL)
    
except ImportError:
    
    def take_pic(file_path):
        fake = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'file.jpeg')
        shutil.copyfile(fake , file_path)


if __name__ == "__main__":
    take_pic("test.jpeg")
