"""
 This should give you a dictionary indexed by EXIF numeric tags.
If you want the dictionary indexed by the actual EXIF tag name strings, try something like:
"""
import pprint

import PIL.Image
import PIL.ExifTags
import fire


def get_exif(filename):
    img = PIL.Image.open(filename)
    exif_data = img._getexif()
   
    exif = {PIL.ExifTags.TAGS[k]: v
             for k, v in exif_data.items()
                if k in PIL.ExifTags.TAGS
           }
    return exif


def report(filename):
    pprint.pprint(get_exif(filename))


def main():
    fire.Fire(report, name='getexif')


if __name__ == '__main__':
    main()