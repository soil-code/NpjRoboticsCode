function [features,label,filename] = txt2data(path)

file_path = path;
file_index = [path 'index.txt'];
pairs = importdata(file_index);

file_num = size(pairs.data,1);

dataset = {};
for sample_i= 1:file_num
    name = pairs.textdata{sample_i};
    sample_path = fullfile(file_path,name);
    delimiterIn = ' ';
    headerlinesIn = 0;
    sample = importdata(sample_path,delimiterIn, headerlinesIn);
    A = sample(:,1:3);

    dataset{end+1,1} = A';
end

features = dataset;
label = pairs.data;
filename = pairs.textdata;
end