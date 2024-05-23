If you need to isolate vocals, drums, bass, and other instruments into seperate tracks and do it from withing a Python script
this is for you.

Example of how to use the demucs audio processing library *within* Python.  
I figured out after a few hours of teeth gnashing. It was actually pretty simple as the library is only meant to be  
called from the commandline.

I found the `mdx_extra_q` model is the only one that works with my setup but your versions may be different. So, you may
want to try the `htdemucs` or `htdemucs_ft` models because they are newer. Though I have tried both and didn't notice a difference.
