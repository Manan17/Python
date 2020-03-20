import imageio
import os

clip = os.path.abspath('BirdNoSound_Trim.mp4')

def convert(inputPath,targetFormat):
    output = os.path.splitext(inputPath)[0] + targetFormat
    
    print(f'converting {inputPath} \n to {output}')
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(output,fps=fps)

    for frames in reader:
        writer.append_data(frames)

    print('Done')
    writer.close()

convert(clip,'.gif')





