#!/bin/perl -w

use strict;

use Cwd;

my $pwd = cwd();

open(H, "<", "missing-commits.txt") or die "OOPS";

while(my $line = <H>) {
  my $t = substr($line,0,2);
  my $e = substr($line, 2, length($line));
  print "$e :: $t"; 
  chdir("../objects");
  `sh get-object.sh $t $e`;
  chdir($pwd);
  `cp -a ../objects/$t/ .git/objects`;
}


close H;



