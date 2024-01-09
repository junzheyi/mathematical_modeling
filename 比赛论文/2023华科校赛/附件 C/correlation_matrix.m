% 读取CSV文件数据
data = readmatrix("C:\Users\86183\Desktop\数模校赛\C题附件.csv");

% 提取变量属性和"shares"的数据列
variables = data(:, 3:end-1);
shares = data(:, end);

% 计算相关性
correlation = corrcoef([variables shares]);

% 提取变量属性与"shares"的相关性
variable_correlation = correlation(1:end-1, end);

% 打印相关系数
for i = 1:numel(variable_correlation)
    fprintf('变量属性 %d 与"shares"的相关系数: %.2f\n', i, variable_correlation(i));
end

% 绘制条形图
figure;
bar(variable_correlation, 'FaceColor', '#0072BD', 'BarWidth', 0.5);
title('变量属性与"shares"的相关性', 'FontSize', 14);
xlabel('变量属性', 'FontSize', 12);
ylabel('相关系数', 'FontSize', 12);
grid on;
set(gca, 'FontSize', 12);
% 添加网格线
yline(-1:0.3:1, '--', 'Color', 'gray', 'LineWidth', 0.5);
hold off;