%Brandon Hansen CS323 Homework 2 Problem 1
A = [21, 32, 14, 8, 6, 9, 11, 3, 5; 17, 2, 8, 14, 55, 23, 19, 1, 6; 41, 23, 13, 5, 11, 22, 26, 7, 9; 12, 11, 5, 8, 3, 15, 7, 25, 19; 14, 7, 3, 5, 11, 23, 8, 7, 9; 2, 8, 5, 7, 1, 13, 23, 11, 17; 11, 7, 9, 5, 3, 8, 26, 13, 17; 23, 1, 5, 19, 11, 7, 9, 4, 16; 31, 5, 12, 7, 13, 17, 24, 3, 11];

B = [2; 5; 7; 1; 6; 9; 4; 8; 3];

disp("Inverse of A = ")
disp(inv(A))

disp("X = A^-1B = ")
disp(inv(A)*B)
%{
function [L, U] = LUcalculator(A, dim1, dim2)
    M_inv = eye(dim1);
    U = A;
    for j = 1:dim1
        m = U(j, j); % the element in the diagonal
        for i = (j+1):dim1
            n = U(i, j); % the elements under the diagonal
            a = - (n / m);
            tmp_inv = eye(dim1);
            tmp_inv(i, j) = -a;
            M_inv = M_inv * tmp_inv;
            U(i, :) = U(i, :) + U(j, :) * a; %j-th row * a + i-th row
        end
    end
    L = M_inv;
 end
%}
[L, U] = LUcalculator(A, 9, 9);
%{
function Y=forward_subsitution (L,B,dim1, dim2)
    Y = [];
    tmp_L = L;
    tmp_B = B;
    for j = 1:dim1
        m = tmp_L(j, j); % the element in the diagonal
        y_j = tmp_B(j, 1) / m;
        Y = [Y, y_j];
        for i = (j+1):dim1
            n = tmp_L(i, j); % the elements under the diagonal
            a = - (n / m);
            M = eye(dim1);
            M(i, j) = a;    %j-th row * a + i-th row
            tmp_L = M * tmp_L;
            tmp_B = M * tmp_B;
        end
    end    
Y = Y';
%}
Y=forward_subsitution (L,B,9, 9);
%{
function X=backward_subsitution(U,Y,dim1, dim2)
      X = [];     
     tmp_U = U;
     tmp_Y = Y;
     for j = dim1:-1:1
        m = tmp_U(j, j); % the element in the diagonal
        x_j = tmp_Y(j, 1) / m;
        X = [x_j, X];
        for i = (j-1):-1:1
            n = tmp_U(i, j); % the elements under the diagonal
            
            a = - (n / m);
            M = eye(dim1);
            M(i, j) = a;    %j-th row * a + i-th row
                        
            tmp_U = M * tmp_U;
            tmp_Y = M * tmp_Y;
        end
    end
    X = X';
end
%}
X=backward_subsitution(U,Y,9, 9);


disp("L = ")
disp(L)
disp("U = ")
disp(U)
disp("After forward sub we get Y = ")
disp(Y)
disp("After backward sub we get X = ")
disp(X)

disp("Relative error between the two norms = ")
disp(abs(((norm(inv(A)*B) - norm(X)) / (norm(inv(A)*B)))))




