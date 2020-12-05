use std::{
    fs::File,
    io::{prelude::*, BufReader},
    collections::HashSet,
    iter::FromIterator
};

fn read_file(filepath: &str) -> HashSet<u32> {
    let file = File::open(filepath).expect("no such file");
    let buf = BufReader::new(file);
    let lines: Vec<u32> = buf.lines().map(|l| l.unwrap().parse::<u32>().unwrap()).collect();
    HashSet::from_iter(lines.iter().cloned())
}

fn main() {
    let lines = read_file("input.txt");
    for line in lines.iter() {
        if lines.contains(&(2020 - line)) {
            println!("{}", line * (2020 - line));
            break;
        }
    }
}

