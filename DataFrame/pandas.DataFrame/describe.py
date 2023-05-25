"""
class pandas.DataFrame(
                        data=None,
                        index=None,
                        columns=None,
                        dtype=None,
                        copy=None)
二维的、大小可变的、可能是异质的表格数据。

数据结构也包含有标签的轴（行和列）。
算术运算在行和列的标签上对齐。
可以被认为是一个类似于Dict的Series对象的容器。
主要的pandas数据结构。

Parameters:
    data: ndarray (structured or homogeneous), Iterable, dict, or DataFrame
        Dict可以包含系列、数组、常数、数据类或列表类对象。
        如果数据是一个dict，列的顺序遵循插入顺序。
        如果dict包含有定义了索引的Series，它将按照其索引对齐。

        在0.25.0版本中有所改变: 如果数据是一个dict的列表，列的顺序遵循插入顺序。

    index: Index or array-like
        对结果框架使用的索引。
        如果输入数据中没有索引信息，并且没有提供索引，则默认为RangeIndex。

    columns: Index or array-like
        当数据没有柱状标签时，在结果框架中使用柱状标签，默认为RangeIndex(0, 1, 2, ..., n)。
        如果数据包含列标签，将执行列选择。

    dtype: dtype, default None
        要强制执行的数据类型。
        只允许有一个单一的dtype。
        如果没有，则推断。

    copy: bool或None，默认为None
        从输入中复制数据。
        对于dict数据，默认为None的行为就像copy=True。
        对于DataFrame或2d ndarray输入，默认为None，表现为copy=False。

        在1.3.0版本中有所改变。

"""