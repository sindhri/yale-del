#!/usr/bin/perl


read(STDIN,$in,$ENV{'CONTENT_LENGTH'});
  @in = split(/&/,$in);
  foreach $i (0 .. $#in) {
    $in[$i] =~ s/\+/ /g;
    # Split into key and value.
    ($key, $val) = split(/=/,$in[$i],2); 
    # Convert %XX from hex numbers to alphanumeric
    $key =~ s/%(..)/pack("c",hex($1))/ge;
    $val =~ s/%(..)/pack("c",hex($1))/ge;
    # Associate key and value
    $in{$key} .= "\0" if (defined($in{$key})); 
    $in{$key} .= $val;
   }

($SECONDS, $MINUTES, $HOURS, $MDAY, $MON, $YEAR, $WDAY, $YDAY, $ISDST) = localtime(time);

#print "Content-type: text/html\n\n";






$in{'from'} = "visitor\@info.med.yale.edu/chldstdy/mayes/index.htm";
$in{'to'}="linda.mayes\@yale.edu";
$in{'sub'} = "Email from YCSC: Laboratory for Cognitive-Emotional Development Website";
open(MAILER, "|/usr/lib/sendmail $in{'to'}") || die "Error: can not open mail pipe.\n"; 
print MAILER "To: $in{'to'}\n";
print MAILER "From: $in{'from'}\n";
print MAILER "Name:     $in{'Name'}\n\n";
print MAILER "Email:     $in{'Email'}\n\n";
print MAILER "Subject:     $in{'Subject'}\n\n";
print MAILER "Comment:     $in{'Comments'}";

close MAILER;
$dest = "http://info.med.yale.edu/chldstdy/mayes/thanks.htm";
print "Location: $dest\n\n";






exit;