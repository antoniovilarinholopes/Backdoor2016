#!/bin/perl -w

use strict;


foreach my $i (1..199) {
 my $j = $i+1;
 my $out = `git diff HEAD~$i HEAD~$j`;
 print $out;

}



