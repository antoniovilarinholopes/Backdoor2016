# Clue

This was a web challenge that required some git and github knowledge. We are given a page and are asked to find the flag.
First we searched for known files in a directory that could leak any information, particularly robots.txt. However robots.txt didn't exist, so we had to search for other common files. 

At this point we thought that using Nikto was a good approach. As Nikto was running we saw that the E-tag was leaking inodes, our thoughts immediatly jumped to thinking that the solution to the challenge had something to do with this information. Although we couldn't find an attack for this challenge with this information, in the meantime Nikto ended its search and leaked a file ".git/index". 

From here we looked at index and saw that there were 4 files (besides index.html): vampire, flag(txt/html) and 982hud0q3rhua. Looking in their server these 4 files are there and vampire.txt has the content " Flag should be present in 982hud0q3rhua at some time
N2QxYzJiOTIzODMxMDEyZDg1YzVmZTY0". We checked the file in the server and thought maybe it would be there. Furthermore, we thought that we just had to wait for some event and the flag would appear. After some more thinking, we eventually decided that the way to go was to rebuild the repo with everything that was on .git folder.

To rebuild the repo we had to retrieve some essencial files and folders such as: config, index, info/, logs/, objects/, and refs/.
Additionally, we also added HEAD and ORIG\_HEAD to the .git folder with the last known commit.

To retrieve the objects we went to .git/logs/refs/heads/master and looked at the commits. After running some shell commands (awk mostly) we get the individual commits and start downloading them into an objects folder, which then copied into .git (retrieve-commits-obj.py script).

Then we got stuck, first we tought that the modified file we saw using git status would give us the flag, we lost a lot of time doing some git commands to try to recover that file. We got nothing. Then, we started checking if in the last commits one of the 982hud0q3rhua contained the flag (we did this manually). After some hours we decided that we should just see the differences between each commit and save it to a file, regardless of the file edited between commits. 

Therefore, we tried to see the result of ``git diff HEAD HEAD~1``, as we didn't have all the objects it failed. As a result, we did 3 scripts, one to see the git diffs between HEAD~i and HEAD~i+1, one that given the missing commits gets the object to a temporary objects folder (via the third script) and then copies into the .git/objects, and the third to do a wget and place the object in the proper place. We run the first script to get all the missing objects and then use the second and third script to retrieve them.

After, we run the first script again and search in the diff file for something out of place: "That time is Fri Jun 3 14:00:00 2016 +0530".

What? How can that be? The last commit we have access to is way before that one and the repo seems to be deleted. We surely can't do a git pull. After talking to the admin, we were told that the repo exists but is private.

So now we have to figure out how to leak information from a private repo. We thought maybe .ssh was there, nope. We searched for some more common files that leak info and nothing. After some thinking we tought, what feature does github has that could allow private files to be leaked? And after realizing that we had some .html files maybe through github io we can find something.

Finally, our thought was correct and we find the flag, first blood!
``
echo hash("sha256", "617hub_h0575_p4635_3v3n_f0r_pr1v473_r3p05170r135");
``

We ended up spending too much time in this task and should have done some others that were in our reach.

