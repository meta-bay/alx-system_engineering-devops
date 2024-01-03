#!/usr/bin/env ruby

def extract_info(log)
  sender = log.match(/\[from:(.+?)\]/)&.captures&.first
  receiver = log.match(/\[to:(.+?)\]/)&.captures&.first
  flags = log.match(/\[flags:(.+?)\]/)&.captures&.first
  "#{sender},#{receiver},#{flags}"
end

ARGV.each do |log|
  puts extract_info(log)
end

