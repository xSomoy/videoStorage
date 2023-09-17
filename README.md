# Storing data as video in youtube
--- 


## Concept:
```
All the files are basically 0 and 1.
Every frame of a video is an image.
<<
We can encode every pixel of a frame/image by colour white as 1 and black as 0.
Then generate a video with all the binary data encoded in every single frame.
Then upload the video on youtube.
>>
Later we can download the video and split every frame into images,
And take data from every pixel to re-create the original file. 
```
> This concept is not new. Already [DvorakDwarf](https://github.com/DvorakDwarf) created a Rust Based POC named [Infinite-Storage-Glitch](https://github.com/DvorakDwarf/Infinite-Storage-Glitch) . But They **achived the repo on Mar 16, 2023**. Even tho I forked the [repo](https://github.com/xSomoy/Infinite-Storage-Glitch). And followed their setps by using Docker but Slapped by this error
> 
> ***`./isg_4real: error while loading shared libraries: libopencv_barcode.so.4.5d: cannot open shared object file: No such file or directory`***
>
> Maybe building from source with manually installing dependencies might resolve the issue.