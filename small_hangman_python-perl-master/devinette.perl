#!/usr/bin/perl -w

@mots=qw(pomme fraise kiwi cerise orange);
@devines=();
$faux=0;

$choix=$mots[rand @mots];
$pendu="O-|--<";

@lettres=split(//, $choix);
@pendu=split(//, $pendu);

@motblanc=(0) x scalar(@pendu);
EXTER:
    while($faux < @pendu) {
	foreach $i (0..$#lettres) {
	    if($motblanc[$i]) {
		print $motblanc[$i];
	    }else {
		print "-";
	    }
	}
	print "\n";
	if($faux) {
	    print @pendu[0..$faux-1]
	}
	print "\nDevinez :";
	$devine=<STDIN>;
	chomp $devine;
	foreach(@devines) {
	    nex EXTER if($_ eq $devine);
	}

	$correct=0;
	for($i=0; $i<@lettres; $i++) {
	    if($lettres[$i] eq $devine) {
		$motblanc[$i]=$devine;
		$correct=1;
	    }
	}
	$faux++ unless($correct);
	if(join('', @motblanc) eq $choix) {
	    print "BRAVO ! c'est correct !\n";
	    exit;
	}
}	
print "$pendu\nDommage, le mot est $choix.\n";

