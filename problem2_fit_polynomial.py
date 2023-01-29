def problem2_fit_polynomial(x, y, degree, regularization = None):
    X = [[x[i]**j for j in range(degree + 1)] for i in range(len(x))]
    print(X)
    print(np.shape(X))
    # Find the transpose of X
    X_transpose = np.linalg.linalg.transpose(X)
    print(np.shape(X_transpose))
    # Multiply X_transpose with X
    XTX = np.dot(X_transpose, X)

    print(np.shape(XTX))
    # Multiply X_transpose with y
    XTY = np.dot(X_transpose, y)
    print(np.shape(XTY))
    # Inverse of X_transpose_X
    XTX_inv = np.linalg.inv(XTX)
    print(np.shape(XTX_inv))
    # Multiply X_transpose_X_inv with X_transpose_y
    if (regularization == None):
        w = np.dot(XTX_inv, XTY)
        print(w)
    else:
        w = np.dot(XTX_inv + regularization*np.eye(degree + 1), XTY)
        print(w)
