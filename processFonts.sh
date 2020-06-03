
targetFolder=compiledFonts
woff2Dir=$targetFolder"/WOFF2"
base64Dir=$targetFolder"/BASE64"
#clean up
#rm -rf $compiledFonts/
mkdir -p $woff2Dir $base64Dir

# find all otf ad ttf
for font in $(find . -type f -name "*.*tf") 
do
  filename=$(basename -- "$font")
  extension="${filename##*.}"
  filename="${filename%.*}"
  echo $font
  echo $filename

  fonttools ttLib.woff2 compress $font -o $woff2Dir/$filename.woff2 # gen woff2 out of otf
  base64 $woff2Dir/$filename.woff2 > $base64Dir/$filename.b64
done