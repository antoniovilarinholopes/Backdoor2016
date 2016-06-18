#!/bin/perl -w

use strict;


foreach my $i (1..199) {
 `git stash`;
 `git checkout HEAD~$i`;
 my $out = `cat 982hud0q3rhua`;
 print $out;

}



