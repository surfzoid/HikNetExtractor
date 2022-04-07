Provides functionality to extract perodicly only new or missing record event from Hikvion camera or NVR with ISAPI and HTTPDigestAuth enable.  
The script will create a new dir peer day.  
# Add this script to an scheduled tasks and you will keep records durring the number of day you put in the config.py  
See also: http://www.hikvision.com/en/download.asp
After wath you can backup video files throught the local network or the net, for example with rsyncd. Use QtVsPlayer, https://github.com/surfzoid/QtVsPlayer to read the video with green and red vector like in the web interface BUT Localy.  

# My personal usage  

mkdir -p ~/script/cam1  
cd ~/script/cam1  
git clone https://github.com/surfzoid/HikNetExtractor.git  

mkdir -p ~/script/NVR  
cd ~/script/NVR  
git clone https://github.com/surfzoid/HikNetExtractor.git  

##edit conf.py in cam1/HikNextractor and NVR/HikNextractor  

crontab -e  
3,18,33,48 * * * * ~/script/HikNetExtractor/NVR/HikNetExtractor.py  
3,18,33,48 * * * * ~/script/HikNetExtractor/cam1/HikNetExtractor.py  
3,18,33,48 * * * * ~/script/rsyncfbx.sh #sauvegarde des videos de la camera vers la maison  
 
# Enjoy  

The Software is licensed, THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
