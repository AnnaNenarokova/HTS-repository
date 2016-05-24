#!/usr/bin/ruby
require 'thread/pool'

def process_folders(folders)
    files = []
    folders.each do |folder|
        Dir.glob("#{folder}/fastqc_results/zip/trimmed_reads/*.zip").each do |file|
            files << file
        end
    end
    return files
end

def run_in_pool(files, threads)
    pool = Thread.pool(threads)
    files.each do |file|
        pool.process do
            `unzip #{file}`
        end
    end
    pool.shutdown
end

folders = [
    '/media/4TB1/kinetoplastids_hinxton/illumina/miseq',
    '/media/4TB1/kinetoplastids_hinxton/illumina/hiseq'
        ]

threads = 32

run_in_pool(process_folders(folders), threads)
