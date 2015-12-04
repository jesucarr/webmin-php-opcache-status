#!/usr/bin/perl

use LWP::UserAgent;
use WebminCore;

my $ua = new LWP::UserAgent;
&init_config();

$url = $config{'link'};
if ($url) {
  PrintHeader();
  my $response = $ua->get($url);
  print $response->content;
} else {
  &ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1);
  print &text('config_missing');
}



