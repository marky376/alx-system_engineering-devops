#!/usr/bin/env ruby

if ARGV.length != 1
	puts "Usage: #{$PROGRAM_NAME} <text>"
	exit 1

end

pattern = /school/

text = ARGV[0]

match = text.match(pattern)

puts match ? match[0] : "$"
