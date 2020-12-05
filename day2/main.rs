use std::{
    fs::File,
    io::{prelude::*, BufReader}
};

fn read_file(filepath: &str) -> Vec<String> {
    let file = File::open(filepath).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines().map(|l| l.expect("couldn't parse line")).collect()
}

fn parse_line(line: String) -> bool{
    let v: Vec<&str> = line.split(':').map(|c| c.trim()).collect();
    let password = v[1];
    let rules: Vec<&str> = v[0].split(' ').map(|c| c.trim()).collect();
    if rules.len() != 2 {
        return false;
    }
    let bounds: Vec<usize> = rules[0].split('-').map(|x| x.parse::<usize>().unwrap()).collect();
    let letter_count = password.matches(rules[1]).count(); 
    return bounds[0] <= letter_count && letter_count <= bounds[1];
}

fn main() {
    let lines = read_file("input.txt");
    let mut valid_password = 0;
    for line in lines {
        if parse_line(line) {
            valid_password += 1;
        }
    }
    println!("{}", valid_password);
}
