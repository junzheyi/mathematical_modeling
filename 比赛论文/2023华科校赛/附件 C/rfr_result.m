% 读取CSV文件
data = readmatrix("C:\Users\86183\Desktop\数模校赛\compare_actual.csv");

% 提取数据列
difference = data(:, 3);
predicted = data(:, 2);
testData = data(:, 1);

% 随机抽样100组数据
numSamples = 150;
indices = datasample(1:length(predicted), numSamples, 'Replace', true);
predicted_sample = predicted(indices);
testData_sample = testData(indices);

% 绘制数据
plot(predicted_sample, 'r-', 'LineWidth', 2); % 绘制预测值
hold on;
plot(testData_sample, 'b--', 'LineWidth', 2); % 绘制测试数据
hold off;

% 设置图形标题和轴标签
title('Predicted vs Test Data (Random Sample)');
xlabel('Sample');
ylabel('Value');

% 添加图例
legend('Predicted', 'Test Data');