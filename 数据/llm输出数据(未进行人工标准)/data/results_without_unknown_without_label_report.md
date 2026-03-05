# LLM 分类结果分析报告

- **分析文件**：`results_without_unknown_without_label.json`
- **完整路径**：`/home/lg/Documents/projects/毕设/大仓/匹配/llm-match/output/results_without_unknown_without_label.json`
- **生成时间**：2026-03-05 23:16:33

---

## 1. 数据总览

| 指标 | 数值 |
|---|---|
| 数据总条数 | 2510 |
| 有效条目数（含 label / llm_label） | 2510 |
| 跳过条目数（字段缺失或无效） | 0 |
| Unknown 条目数 | 0 |
| Unknown 比率 | 0.0% |
| 已判定条目数（非 Unknown） | 2510 |
| 判定一致数 | 1832 |
| 判定不一致数 | 678 |

## 2. 算法标注（label）分布

| label | 数量 | 占比 |
|---|---|---|
| TP | 218 | 8.7% |
| FP | 2292 | 91.3% |

## 3. label × llm_label 交叉矩阵

| label \ llm_label | TP | FP | Unknown | **合计** |
|---|---|---|---|---|
| **TP** | 105 | 113 | 0 | **218** |
| **FP** | 565 | 1727 | 0 | **2292** |
| **合计** | 670 | 1840 | 0 | **2510** |

## 4. 汇总指标

> 以下指标仅基于**已判定（非 Unknown）**条目计算。

| 指标 | 数值 |
|---|---|
| 准确率（Accuracy） | 73.0% |
| 精确率（Precision，以 TP 为正类） | 15.7% |
| 召回率（Recall，以 TP 为正类） | 48.2% |
| F1 分数（以 TP 为正类） | 23.6% |

## 5. 各分类条目详情

### 5.1 一致：算法=TP，LLM=TP（共 105 条）

> 算法与 LLM 均判定为真阳性（True Positive）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 678 | vim-9.1.1591 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | TP | TP | getcell函数可能返回NULL，但调用后未检查返回值就直接解引用cell->chars，存在空指针解引用风险。切片中未见任何防护机制。 |
| 680 | vim-9.1.1591 | get_isolated_shell_name | cpp/inconsistent-null-check | 2754 | TP | TP | 函数 `vim_strnsave` 可能返回 NULL，但调用后未检查返回值，直接赋值给指针 `p` 并在函数末尾返回，存在空指针解引用风险。切片中未见任何针对该返回值的空值检查。 |
| 697 | vim-9.1.1591 | prt_line_number | cpp/overrunning-write | 387 | TP | TP | sprintf 使用格式字符串 "%6ld" 写入一个长整数，在目标缓冲区 tbuf[20] 中最多可能产生 6位数字加1位符号位和1位空终止符，共8字节，不会溢出。但告警提示需要21字节，这可能是工具误算了格式字符串的长度或考虑了不... |
| 698 | vim-9.1.1591 | highlight_color | cpp/overrunning-write | 3278 | TP | TP | sprintf 目标缓冲区 'buf' 大小为10字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少10字节，当三个颜色分量均为最大值（0xff）时，生成的字符串 "#ffffffff" 恰好为9个字符加上终止符... |
| 699 | vim-9.1.1591 | msg_outnum | cpp/overrunning-write | 1651 | TP | TP | 目标缓冲区 `buf` 大小为20字节，但 `sprintf` 格式化长整型 `%ld` 时，对于某些负数值（如 -9223372036854775808）可能产生21个字符（包括负号和数字），导致缓冲区溢出。切片中未见任何输入范围检... |
| 701 | vim-9.1.1591 | ga_concat_strings | cpp/unbounded-write | 788 | TP | TP | 代码使用不安全的strcpy函数，将动态长度的字符串复制到固定大小的缓冲区中，且切片内未见对源字符串长度的校验或对目标缓冲区边界的检查，存在缓冲区溢出风险。 |
| 702 | vim-9.1.1591 | maketitle | cpp/unbounded-write | 4239 | TP | TP | 代码使用STRCPY（即strcpy）将不确定长度的字符串`name`复制到固定大小的缓冲区`buf`中，且切片内未见对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 703 | vim-9.1.1591 | buf_write | cpp/unbounded-write | 1208 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将fname复制到固定大小的IObuff缓冲区，未检查fname长度是否超过IObuff大小，存在缓冲区溢出风险。切片中未见对源字符串长度的验证或使用安全函数。 |
| 706 | vim-9.1.1591 | transstr | cpp/unbounded-write | 400 | TP | TP | 切片代码显示，`res` 缓冲区通过 `alloc(len + 1)` 分配，其大小 `len` 是计算出的字符显示宽度，而非字节长度。随后循环中使用 `STRCAT(res, transchar_byte(*p++))`（即 `st... |
| 707 | vim-9.1.1591 | globpath | cpp/unbounded-write | 4180 | TP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区buf的大小为MAXPATHL。虽然存在条件'pathlen + seplen + filelen + 1 <= MAXPATHL'检查，但该检查未考虑file参数可能被外... |
| 708 | vim-9.1.1591 | expand_shellcmd | cpp/unbounded-write | 3902 | TP | TP | 代码使用STRCPY（即strcpy）将可变长度的字符串'pat'复制到固定大小的缓冲区'buf'中，且切片内未见对'pat'长度进行前置检查以确保不超过目标缓冲区剩余容量，存在缓冲区溢出风险。 |
| 711 | vim-9.1.1591 | debuggy_find | cpp/unbounded-write | 1067 | TP | TP | 代码使用STRCPY宏（即strcpy）将fname复制到新分配的缓冲区name中，未检查fname的长度是否超过name的分配大小（STRLEN(fname) + 3），存在缓冲区溢出风险。 |
| 712 | vim-9.1.1591 | has_profiling | cpp/unbounded-write | 973 | TP | TP | 代码使用STRCPY宏（即strcpy）将未经验证长度的源字符串fname复制到固定大小的目标缓冲区pe->pen_name，存在缓冲区溢出风险。切片中未见对fname长度的前置校验或使用安全函数。 |
| 713 | vim-9.1.1591 | ex_diffpatch | cpp/unbounded-write | 1512 | TP | TP | 代码使用不安全的 STRCPY 宏（即 strcpy）将 tmp_new 复制到固定大小的缓冲区 buf 中，而 buf 的大小是根据其他字符串长度计算的，但 tmp_new 是临时文件名，其长度可能超过 buf 的剩余空间，导致缓冲... |
| 714 | vim-9.1.1591 | do_string_sub | cpp/unbounded-write | 8057 | TP | TP | 切片代码中，STRCPY宏被直接展开为strcpy，用于将'tail'指向的字符串复制到动态分配的缓冲区'ga.ga_data'的末尾。虽然缓冲区大小通过ga_grow进行了检查，但strcpy的目标地址是'ga.ga_data + ... |
| 715 | vim-9.1.1591 | set_var_const | cpp/unbounded-write | 4300 | TP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname是用户提供的变量名，其长度未在切片中验证，存在缓冲区溢出风险。 |
| 716 | vim-9.1.1591 | cat_prefix_varname | cpp/unbounded-write | 2578 | TP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到缓冲区`varnamebuf+2`，虽然缓冲区大小`len`根据`name`的长度计算并分配，但未考虑`prefix`和分隔符已占用2字节，可能导致目标缓冲区溢出。 |
| 720 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 795 | TP | TP | 切片代码显示STRCPY宏直接展开为strcpy，且目标缓冲区sortbuf1的大小为maxlen+1，而源数据&s[start_col]的长度可能超过maxlen（例如当start_col不为0时），存在缓冲区溢出风险。 |
| 721 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 815 | TP | TP | 切片代码中，`STRCPY` 宏被直接展开为 `strcpy`，且目标缓冲区 `sortbuf1` 的大小为 `maxlen + 1`，而源字符串 `&s[start_col]` 的长度可能超过 `maxlen`（因为 `maxlen... |
| 722 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 833 | TP | TP | 切片代码中，`STRCPY` 宏被展开为 `strcpy`，且目标缓冲区 `sortbuf1` 的大小为 `maxlen + 1`，而源数据 `&s[start_col]` 的长度可能超过 `maxlen`（因为 `maxlen` 是... |
| 723 | vim-9.1.1591 | ex_sort | cpp/unbounded-write | 605 | TP | TP | 代码使用STRCPY宏（即strcpy）将未知长度的字符串`s`复制到固定大小的缓冲区`sortbuf1`中，而`sortbuf1`的大小仅基于之前计算的最大行长`maxlen`分配，无法保证`s`的长度不超过`maxlen`，存在缓... |
| 724 | vim-9.1.1591 | expand_sfile | cpp/unbounded-write | 10143 | TP | TP | 代码使用STRCPY宏（即strcpy）将可变长度的字符串复制到固定大小的缓冲区，未进行边界检查。切片中未见对repl或p+srclen长度的验证，存在缓冲区溢出风险。 |
| 725 | vim-9.1.1591 | repl_cmdline | cpp/unbounded-write | 5330 | TP | TP | 切片代码显示使用STRCPY（即strcpy）复制未经验证长度的字符串（src + srclen），目标缓冲区new_cmdline的大小i虽经计算，但未确保复制前目标缓冲区有足够的空间容纳源字符串，存在缓冲区溢出风险。 |
| 726 | vim-9.1.1591 | repl_cmdline | cpp/unbounded-write | 5336 | TP | TP | 切片代码中 STRCPY 宏直接展开为不安全的 strcpy 函数，目标缓冲区 new_cmdline 的大小 i 由多个长度计算而来，但复制源 eap->nextcmd 是外部输入且长度未知，没有可见的长度检查或使用安全函数，存在缓... |
| 727 | vim-9.1.1591 | replace_makeprg | cpp/unbounded-write | 5037 | TP | TP | 代码使用STRCPY（即strcpy）宏将未经验证的用户输入（`p`）复制到固定大小的缓冲区（`ptr`），而`p`的长度`len`可能超过目标缓冲区剩余空间，存在缓冲区溢出风险。切片中未见对`len`或目标缓冲区大小的边界检查。 |
| 728 | vim-9.1.1591 | replace_makeprg | cpp/unbounded-write | 5052 | TP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串（如程序变量program和参数p）复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小是基于STRLEN计算分配的，但STRCPY本身不检查边界... |
| 729 | vim-9.1.1591 | do_one_cmd | cpp/unbounded-write | 2686 | TP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将未知长度的字符串复制到固定大小的IObuff缓冲区，存在缓冲区溢出风险。切片中未见对源字符串长度的检查或限制。 |
| 731 | vim-9.1.1591 | get_exception_string | cpp/unbounded-write | 473 | TP | TP | 切片代码中，`val`指向的缓冲区大小由`vim_strnsave`分配，其大小计算涉及`STRLEN(mesg)`等变量，但后续`STRCAT(val, mesg)`或`STRCAT(val, p)`调用时，未检查拼接后字符串长度是... |
| 732 | vim-9.1.1591 | get_exception_string | cpp/unbounded-write | 484 | TP | TP | sprintf 使用来自 mesg 的未受控输入（可能包含用户提供的文件名）直接格式化到 val 缓冲区，而 val 缓冲区的大小是基于 mesg 长度预先分配的，但 sprintf 的格式化操作（添加括号和前缀）可能导致总长度超过分... |
| 733 | vim-9.1.1591 | escape_fname | cpp/unbounded-write | 4193 | TP | TP | 代码使用strcpy将源字符串(*pp)复制到目标缓冲区(p+1)，目标缓冲区大小仅为源字符串长度加2，但strcpy会复制包括终止空字符在内的所有字符，这可能导致目标缓冲区溢出，因为分配的空间仅够容纳源字符串字符和一个额外的前缀字符... |
| 734 | vim-9.1.1591 | cmdline_browse_history | cpp/unbounded-write | 1528 | TP | TP | 切片代码显示 STRCPY 宏直接展开为 strcpy，将源字符串 p 复制到目标缓冲区 ccline.cmdbuff，而目标缓冲区大小由 alloc_cmdbuff 根据 plen 分配，但未检查源字符串长度是否超过分配的大小，存在... |
| 735 | vim-9.1.1591 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 879 | TP | TP | 代码使用STRCPY宏（即strcpy）将动态获取的字符串p复制到固定缓冲区ccline.cmdbuff，虽然之前调用了realloc_cmdbuff(len + 1)来确保缓冲区大小，但该函数仅当len小于当前缓冲区长度时才不重新分... |
| 736 | vim-9.1.1591 | vim_settempdir | cpp/unbounded-write | 5293 | TP | TP | 切片代码显示，当`vim_FullName`函数调用失败时，会使用`STRCPY`（即`strcpy`）将未知长度的`tempdir`参数直接复制到固定大小的缓冲区`buf`中。`buf`的大小为`MAXPATHL + 2`，但`te... |
| 738 | vim-9.1.1591 | buf_modname | cpp/unbounded-write | 3643 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的fname复制到新分配的缓冲区retval中，虽然retval的大小基于fnamelen计算，但fname来自外部输入（如环境变量、文件读取），其长度可能超过目标缓冲区大小，存在缓... |
| 739 | vim-9.1.1591 | addfile | cpp/unbounded-write | 4219 | TP | TP | 代码使用STRCPY（即strcpy）将参数f复制到新分配的内存p中，虽然p的大小根据f的长度（STRLEN(f) + 1 + isdir）分配，但strcpy本身不检查目标缓冲区大小，若f在分配后被修改或存在并发问题，理论上可能导致... |
| 741 | vim-9.1.1591 | concat_fnames | cpp/unbounded-write | 3137 | TP | TP | 代码使用strcat拼接两个字符串，虽然为目标缓冲区分配了基于两个输入字符串长度的内存，但未考虑空字符的额外空间（仅+3可能不足），且strcat本身不检查目标缓冲区边界，存在缓冲区溢出的风险。 |
| 742 | vim-9.1.1591 | uniquefy_paths | cpp/unbounded-write | 2568 | TP | TP | 代码使用STRCPY（即strcpy）将用户提供的pattern复制到新分配的缓冲区file_pattern中，file_pattern的大小为len+2，而STRCPY的目标地址偏移了1字节（file_pattern+1），这可能导... |
| 743 | vim-9.1.1591 | uniquefy_paths | cpp/unbounded-write | 2685 | TP | TP | 代码在行`STRCPY(fnames[i], short_name);`处使用了不安全的`strcpy`宏，将`short_name`复制到`fnames[i]`指向的缓冲区中。切片中未显示对`short_name`长度的检查，也未显... |
| 744 | vim-9.1.1591 | find_file_in_path_option | cpp/unbounded-write | 1911 | TP | TP | 代码使用STRCPY宏（即strcpy）将外部输入`*file_to_find`复制到固定大小的缓冲区`NameBuff`中，而`*file_to_find`可能来自环境变量或文件读取，其长度未经验证，存在缓冲区溢出风险。 |
| 745 | vim-9.1.1591 | ff_check_visited | cpp/unbounded-write | 1537 | TP | TP | 代码使用STRCPY宏（即strcpy）将ff_expand_buffer.string复制到vp->ffv_fname，目标缓冲区大小由alloc分配，其大小基于ff_expand_buffer.length（源字符串长度）计算，未... |
| 746 | vim-9.1.1591 | <global> | cpp/unbounded-write | 3794 | TP | TP | 代码使用strcat将未经验证长度的字符串s追加到缓冲区r，而r的大小是基于对txt、dashes和s的STRLEN计算分配的，但s来自文件内容，其长度可能超过分配时预留的空间，导致缓冲区溢出。 |
| 747 | vim-9.1.1591 | foldDelMarker | cpp/unbounded-write | 1897 | TP | TP | 代码使用STRCPY宏（即strcpy）将源字符串复制到新分配的缓冲区，未检查目标缓冲区大小，且切片中未见任何边界检查或安全复制机制，存在缓冲区溢出风险。 |
| 748 | vim-9.1.1591 | foldAddMarker | cpp/unbounded-write | 1815 | TP | TP | 切片代码中 STRCPY 宏直接展开为 strcpy，且目标缓冲区 newline 的大小由 alloc(line_len + markerlen + STRLEN(cms) + 1) 分配，但 strcpy 的源（如 line、cm... |
| 749 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2899 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_prolog->title复制到固定大小的buffer[256]中，而title来自外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 750 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2901 | TP | TP | 代码使用STRCAT宏（即strcat）将res_prolog->title和res_prolog->version拼接到固定大小的buffer[256]中，未检查目标缓冲区长度，存在缓冲区溢出风险。 |
| 751 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2905 | TP | TP | 代码使用STRCPY（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，但切片内未显示对title长度的任何验证或限制，存在缓冲区溢出风险。 |
| 752 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2907 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的源字符串（res_cidfont->title和res_cidfont->version）长度在切片内未经验证，存在缓冲区溢出的风险。 |
| 753 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2912 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_cmap->title复制到固定大小的buffer[256]中，切片内未见对res_cmap->title长度的校验，存在缓冲区溢出风险。 |
| 754 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2914 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer追加内容，而buffer的大小为256字节。切片中未显示对res_cmap->title和res_cmap->version的长度进行任何校验，存在缓冲区溢出的风险。 |
| 756 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2922 | TP | TP | 切片代码显示使用STRCAT宏（即strcat）将res_encoding->title和res_encoding->version拼接到固定大小的buffer[256]中，未检查目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 758 | vim-9.1.1591 | do_helptags | cpp/unbounded-write | 1210 | TP | TP | 代码使用STRCPY（即strcpy）将参数dirname复制到固定大小的缓冲区NameBuff中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对dirname长度的验证或使用安全函数。 |
| 759 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 975 | TP | TP | 代码使用STRCAT宏（即strcat）向NameBuff缓冲区拼接未经验证长度的字符串，存在缓冲区溢出的风险。切片中未见对NameBuff大小或拼接后总长度的检查。 |
| 761 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 1112 | TP | TP | sprintf函数使用未经验证的用户输入（p1和fname）作为格式化字符串的参数，目标缓冲区s的大小计算（p2 - p1 + STRLEN(fname) + 2）可能不足以防止缓冲区溢出，因为p1和p2来自文件内容，其长度未受限制。 |
| 763 | vim-9.1.1591 | load_colors | cpp/unbounded-write | 609 | TP | TP | sprintf 使用未经验证的用户输入 `name` 拼接字符串到固定大小的缓冲区 `buf` 中，缓冲区大小仅比 `name` 长度多12字节，若 `name` 长度过长或包含路径遍历字符可能导致缓冲区溢出。切片中未见对 `name... |
| 770 | vim-9.1.1591 | ins_compl_infercase_gettext | cpp/unbounded-write | 723 | TP | TP | 代码使用STRCPY宏（即strcpy）将IObuff的内容复制到gap.ga_data中，而IObuff是一个固定大小的缓冲区（IOSIZE），但切片中未显示对源字符串长度的检查，存在缓冲区溢出的风险。 |
| 771 | vim-9.1.1591 | <global> | cpp/unbounded-write | 3140 | TP | TP | 代码使用`sprintf`将`transchar(from)`的结果格式化到固定大小的缓冲区`args->os_errbuf`中，但切片内未显示对`transchar`返回值的长度限制或对目标缓冲区大小的检查，存在缓冲区溢出风险。 |
| 774 | vim-9.1.1591 | <global> | cpp/unbounded-write | 811 | TP | TP | 代码使用STRCPY宏（即strcpy）将call_data复制到新分配的缓冲区，但分配的大小为STRLEN(call_data) + 5，未考虑call_data可能为NULL或未验证其长度，存在缓冲区溢出风险。切片中未见对call... |
| 775 | vim-9.1.1591 | <global> | cpp/unbounded-write | 815 | TP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将call_data复制到固定大小的缓冲区menu->strings[i]中，而menu->strings[i]的大小仅通过alloc(STRLEN(call_data) + 5)分配... |
| 776 | vim-9.1.1591 | msg_show_console_dialog | cpp/unbounded-write | 4505 | TP | TP | 切片代码显示，STRCPY宏直接调用了strcpy，将未经验证长度的message字符串复制到固定大小的confirm_msg缓冲区，且切片中未见对message长度的前置校验，存在缓冲区溢出风险。 |
| 778 | vim-9.1.1591 | get_emsg_source | cpp/unbounded-write | 500 | TP | TP | sprintf 使用未受控的源文件名 sname 和格式字符串 p 进行格式化，目标缓冲区 Buf 的大小由 STRLEN(sname) + STRLEN(p) 分配，但 sprintf 写入的字符串长度可能超过此值，因为格式说明符 ... |
| 783 | vim-9.1.1591 | push_showcmd | cpp/unbounded-write | 1809 | TP | TP | 切片代码显示使用不安全的strcpy宏将showcmd_buf复制到old_showcmd_buf，未对源缓冲区大小进行任何检查，存在缓冲区溢出风险。 |
| 785 | vim-9.1.1591 | op_change | cpp/unbounded-write | 2003 | TP | TP | 代码中使用了不安全的STRCPY宏（即strcpy），将源字符串（ins_text或oldp + bd.textcol）复制到目标缓冲区（newp + newlen + ins_len），未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 786 | vim-9.1.1591 | op_replace | cpp/unbounded-write | 1299 | TP | TP | 切片代码中 STRCPY 宏展开为 strcpy，将源字符串 oldp + bd.textcol + bd.textlen 复制到目标缓冲区 newp + newlen + bd.endspaces，目标缓冲区大小由 alloc(ol... |
| 787 | vim-9.1.1591 | op_replace | cpp/unbounded-write | 1308 | TP | TP | 切片代码中直接使用STRCPY（即strcpy）将未知长度的源字符串复制到固定大小的目标缓冲区，且未见对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 789 | vim-9.1.1591 | block_insert | cpp/unbounded-write | 743 | TP | TP | 代码使用STRCPY（即strcpy）将字符串oldp复制到newp + offset位置，未检查目标缓冲区newp的大小，且oldp是来自文件行的可变长度字符串，存在缓冲区溢出的风险。 |
| 791 | vim-9.1.1591 | option_value2string | cpp/unbounded-write | 8461 | TP | TP | 切片代码中 STRCPY 宏展开为 strcpy，将 get_special_key_name 或 transchar 的返回值复制到 NameBuff，但未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 792 | vim-9.1.1591 | stropt_expand_envvar | cpp/unbounded-write | 1803 | TP | TP | 代码使用STRCPY（即strcpy）将源字符串`s`复制到目标缓冲区`newval`，而`newval`的大小`newlen`仅基于源字符串长度计算，未考虑目标缓冲区大小限制。若`s`长度超过`newval`分配的大小，将导致缓冲区... |
| 793 | vim-9.1.1591 | mch_expand_wildcards | cpp/unbounded-write | 7445 | TP | TP | 切片代码中，`STRCPY(p, (*file)[i])` 宏展开为 `strcpy`，目标缓冲区 `p` 的大小为 `STRLEN((*file)[i]) + 1 + dir`，而源字符串 `(*file)[i]` 的长度可能大于该... |
| 794 | vim-9.1.1591 | mch_FullName | cpp/unbounded-write | 2846 | TP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区大小由参数len约束。在调用STRCPY前，虽然检查了`(int)(buflen + STRLEN(fname)) >= len`，但此检查仅确保总长度不超过len，未验证... |
| 795 | vim-9.1.1591 | qf_store_title | cpp/unbounded-write | 1940 | TP | TP | 代码使用STRCPY（即strcpy）将外部传入的title字符串复制到新分配的内存中，虽然分配的大小基于STRLEN(title)+2，但strcpy本身不检查目标缓冲区大小，若title字符串在分配后、复制前被恶意修改或存在并发问... |
| 796 | vim-9.1.1591 | reg_submatch | cpp/unbounded-write | 2723 | TP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的目标缓冲区，未进行边界检查。目标缓冲区retval的大小由alloc(len)分配，但STRCPY调用时未验证源字符串长度是否小于len，存在缓冲区... |
| 797 | vim-9.1.1591 | reg_submatch | cpp/unbounded-write | 2732 | TP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区retval的大小len由外部输入（如匹配位置）动态计算，未在复制前检查目标缓冲区retval是否足以容纳源字符串s，存在缓冲区溢出的风险。 |
| 798 | vim-9.1.1591 | regtilde | cpp/unbounded-write | 1959 | TP | TP | STRCPY宏展开为strcpy，目标缓冲区tmpsub的大小为tmpsublen+1，源字符串postfix的长度未在切片中验证，存在缓冲区溢出的风险。切片中未见对postfix长度的校验或使用安全复制函数。 |
| 799 | vim-9.1.1591 | match_with_backref | cpp/unbounded-write | 1600 | TP | TP | 代码使用STRCPY（即strcpy）将长度未知的rex.line复制到固定大小的reg_tofree缓冲区，虽然reg_tofree会根据rex.line的长度重新分配，但分配大小仅比STRLEN(rex.line)多50字节，若r... |
| 800 | vim-9.1.1591 | get_reg_contents | cpp/unbounded-write | 2743 | TP | TP | 代码使用STRCPY宏（即strcpy）将y_current->y_array[i].string复制到目标缓冲区，未检查源字符串长度是否超过目标缓冲区大小。目标缓冲区retval的大小由alloc(len + 1)分配，但复制前未验... |
| 801 | vim-9.1.1591 | do_put | cpp/unbounded-write | 2166 | TP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将y_array[y_size - 1].string复制到缓冲区newp，未检查目标缓冲区大小，且源字符串长度来自外部输入（如环境变量、文件读取等），存在缓冲区溢出风险。 |
| 802 | vim-9.1.1591 | do_put | cpp/unbounded-write | 2167 | TP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将y_array[i].string等源字符串复制到固定大小的缓冲区newp中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 804 | vim-9.1.1591 | op_yank | cpp/unbounded-write | 1319 | TP | TP | 切片代码中，STRCPY宏被直接用于拼接两个字符串，且目标缓冲区大小由两个源字符串长度之和加1计算得出，但未考虑strcpy函数本身不检查目标缓冲区边界，若源字符串长度计算有误或未以空字符结尾，可能导致缓冲区溢出。切片内未见任何边界检... |
| 805 | vim-9.1.1591 | stuff_yank | cpp/unbounded-write | 471 | TP | TP | 切片代码显示使用不安全的STRCPY（即strcpy）宏，将源字符串复制到固定大小的目标缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 806 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2850 | TP | TP | 代码使用strcat将可变长度的输入字符串拼接到固定大小的缓冲区中，且切片内未见对目标缓冲区大小的边界检查，存在缓冲区溢出的风险。 |
| 807 | vim-9.1.1591 | ExpandPackAddDir | cpp/unbounded-write | 1321 | TP | TP | sprintf 使用未经验证的用户输入 `pat` 作为格式化字符串的一部分，目标缓冲区 `s` 的大小为 `pat_len + 26`，但格式化字符串 `"pack/*/opt/%s*"` 的长度加上 `pat` 的长度可能超过缓冲... |
| 808 | vim-9.1.1591 | sign_jump | cpp/unbounded-write | 1313 | TP | TP | sprintf 使用未受控的缓冲区文件名 buf->b_fname 和行号 lnum 作为输入，目标缓冲区 cmd 的大小计算仅基于 buf->b_fname 的长度，未考虑格式化字符串 'e +%ld %s' 的额外开销，存在缓冲区... |
| 809 | vim-9.1.1591 | dump_word | cpp/unbounded-write | 4187 | TP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或处理后的单词，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 811 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2998 | TP | TP | 代码使用STRCPY宏（即strcpy）将repl_to复制到新分配的缓冲区p中，未检查目标缓冲区大小，且repl_to是外部输入（来自环境变量或文件读取），存在缓冲区溢出风险。切片中未见对repl_to长度的校验或使用安全复制函数。 |
| 812 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2999 | TP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p，但p的大小是基于ml_get_curline_len() + addlen + 1分配的，未考虑拼接后总长度可能超过分配大小，存在缓冲区溢出风险。切片中未见对目标缓... |
| 813 | vim-9.1.1591 | count_common_word | cpp/unbounded-write | 1919 | TP | TP | 代码使用STRCPY宏（即strcpy）将未知长度的字符串p复制到固定大小的缓冲区wc->wc_word中，而wc->wc_word的大小基于STRLEN(p)+1分配，但STRCPY本身不检查边界，存在缓冲区溢出的理论风险。切片中未... |
| 814 | vim-9.1.1591 | spell_load_lang | cpp/unbounded-write | 1632 | TP | TP | 代码使用STRCPY（即strcpy）将参数lang复制到固定大小的数组sl.sl_lang中，但切片内未显示对lang的长度进行任何校验或限制。由于lang是外部传入的变量，可能超出目标缓冲区大小，存在缓冲区溢出风险。 |
| 817 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2369 | TP | TP | 切片代码中，STRCAT宏直接调用strcat，将来自fgets读取的字符串（items[0]和items[1]）拼接到缓冲区p中，而p的大小是通过动态计算分配，但未检查拼接后的总长度是否超过p的分配大小，存在缓冲区溢出的风险。 |
| 819 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2464 | TP | TP | 代码使用STRCPY宏（即strcpy）将items[1]复制到缓冲区p，而p的大小仅为STRLEN(items[1]) + 2，但items[1]来自外部文件行，若其长度超过目标缓冲区大小则会导致缓冲区溢出。切片中未见对items[... |
| 820 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2495 | TP | TP | 代码在拼接字符串时使用STRCAT宏（即strcat），目标缓冲区大小未知，且输入来自fgets读取的items[1]，存在缓冲区溢出风险。切片中未见对目标缓冲区大小或输入长度的检查。 |
| 821 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2644 | TP | TP | 切片代码中，STRCPY宏被用于将items[1]复制到p指向的缓冲区，而p是通过getroom(spin, STRLEN(items[1]) + 2, FALSE)分配的，其大小仅比源字符串长度大2。若items[1]长度接近或等于... |
| 822 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2746 | TP | TP | 切片代码中第2746行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，未检查长度，可能导致缓冲区溢出。 |
| 823 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2748 | TP | TP | 切片代码中第2748行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，未检查长度，可能导致缓冲区溢出。 |
| 827 | vim-9.1.1591 | concat_str | cpp/unbounded-write | 794 | TP | TP | 代码使用strcpy复制未知长度的源字符串（str2）到目标缓冲区，虽然目标缓冲区大小通过alloc分配，但分配长度依赖于str1和str2的长度计算，若str2在调用后被恶意修改或非空字符结尾，STRCPY操作仍可能溢出目标缓冲区。... |
| 829 | vim-9.1.1591 | expand_tag_fname | cpp/unbounded-write | 4141 | TP | TP | 代码使用不安全的STRCPY（即strcpy）将tag_fname复制到固定大小的缓冲区retval（大小为MAXPATHL），而tag_fname可能来自外部输入（如环境变量、文件读取），其长度未经验证，存在缓冲区溢出风险。 |
| 830 | vim-9.1.1591 | get_tagfname | cpp/unbounded-write | 3436 | TP | TP | 代码在行'STRCPY(buf, fname);'处使用strcpy宏，将变量fname（可能来自外部文件搜索）复制到固定大小的缓冲区buf中，切片内未见对fname长度的检查或限制，存在缓冲区溢出风险。 |
| 831 | vim-9.1.1591 | findtags_add_match | cpp/unbounded-write | 2625 | TP | TP | 切片代码中 STRCPY 宏直接展开为 strcpy，且目标缓冲区 mfp 的大小由 alloc 分配，但 strcpy 的源字符串 st->help_lang 来自环境变量，其长度未经验证，可能导致缓冲区溢出。 |
| 832 | vim-9.1.1591 | findtags_add_match | cpp/unbounded-write | 2704 | TP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串（如st->tag_fname、st->ebuf、st->lbuf）复制到固定大小的缓冲区，未进行边界检查，存在缓冲区溢出风险。 |
| 834 | vim-9.1.1591 | current_tagblock | cpp/unbounded-write | 1392 | TP | TP | sprintf函数使用用户控制的字符串p和长度len格式化输出到固定大小的缓冲区spat和epat，但缓冲区大小仅由len加上固定常数决定，未对p的内容进行限制，存在缓冲区溢出风险。 |
| 835 | vim-9.1.1591 | uc_check_code | cpp/unbounded-write | 1810 | TP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将外部输入（如eap->arg）复制到缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 839 | vim-9.1.1591 | generate_PUSHFUNC | cpp/unbounded-write | 1042 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证的字符串name复制到固定大小的缓冲区funcname中，而funcname的大小仅基于STRLEN(name)+3分配，未对源字符串长度进行限制，存在缓冲区溢出风险。 |
| 840 | vim-9.1.1591 | update_vim9_script_var | cpp/unbounded-write | 947 | TP | TP | 代码使用STRCPY（即strcpy）将变量`name`复制到新分配的内存`newsav->sav_key`中，而`name`是函数参数，其长度未在切片内进行验证。分配的内存大小基于`STRLEN(name) + 1`，但strcpy... |
| 841 | vim-9.1.1591 | find_exported | cpp/unbounded-write | 756 | TP | TP | 代码使用sprintf将外部可控的字符串（如环境变量、文件读取内容）拼接到固定大小的缓冲区中，未对源字符串长度进行限制，存在缓冲区溢出风险。切片中未见对输入长度的校验或使用安全函数。 |
| 843 | vim-9.1.1591 | xxdline | cpp/unbounded-write | 600 | TP | TP | strcpy 的目标缓冲区 z 是固定大小的静态数组，而源字符串 l 是外部输入（命令行参数），切片中未见对 l 长度的校验或限制，存在缓冲区溢出风险。 |
| 1583 | redis-7.2.5 | auxHumanNodenameSetter | Dereference of null pointer | 281 | TP | TP | 在`if (n)`为假的`else if`分支中，代码直接访问`n->human_nodename`以调用`sdslen`，此时`n`为NULL，导致空指针解引用。切片中未见任何防护机制能阻止此路径下的解引用操作。 |

### 5.2 一致：算法=FP，LLM=FP（共 1727 条）

> 算法与 LLM 均判定为假阳性（False Positive）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 1 | ffmpeg-6.1.1 | upcase_string | cpp/offset-use-before-range-check | 1053 | FP | FP | 切片代码显示循环条件 `src[i] && i < dst_size-1` 确保了在访问 `src[i]` 之前，`i` 已通过 `i < dst_size-1` 进行了范围检查，因此不存在偏移量在范围检查前使用的问题。 |
| 2 | ffmpeg-6.1.1 | capture_screen | cpp/offset-use-before-range-check | 479 | FP | FP | 切片代码显示，在告警行使用变量`j`之前，它已在循环条件`j < tab`中被检查，且`j`在循环内部递增，其值受`tab`限制。`tab`的值由前一个循环计算得出，且`j`的初始值为0，因此访问`row[j]`和`charset[j... |
| 3 | ffmpeg-6.1.1 | capture_screen | cpp/offset-use-before-range-check | 479 | FP | FP | 在告警行所在的while循环条件中，变量j的使用已通过'j < tab'进行了范围检查，确保了访问的安全性，因此该告警为误报。 |
| 4 | ffmpeg-6.1.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码中，在警告所在行的循环条件 `i<w_r` 已经对索引 `i` 进行了范围检查，确保了 `dst[i]` 的访问不会越界。该条件与地址对齐检查 `(((x86_reg)&dst[i]) & 0x1F)` 共同构成了有效的防护。 |
| 5 | ffmpeg-6.1.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警行使用变量`i`的循环条件`i<w_r`中，`i`的初始值为0，且`w_r`在函数开头被定义为`w2 - 1`，这是一个明确的边界。循环体内部没有修改`w_r`，且`i`在循环中仅通过`i++`递增，因此`i`的使... |
| 6 | ffmpeg-6.1.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | FP | 切片代码中，while循环的条件 `m < b && m < nb_entries - 1` 已经对变量 `m` 进行了范围检查，确保其不会越界访问 `entries` 数组。因此，该告警是误报。 |
| 7 | ffmpeg-6.1.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 215 | FP | FP | 切片代码中，在访问 `q->subs[i + 1]` 之前，已经通过条件 `i < q->nb_subs - 1` 进行了明确的数组边界检查，确保了 `i+1` 是有效索引，因此不存在越界访问风险。 |
| 8 | ffmpeg-6.1.1 | choose_out_timebase | cpp/inconsistent-null-check | 1850 | FP | FP | 切片代码显示，在调用frame_data后，其返回值fd被直接用于访问成员（如fd->dec.tb），这表明调用者假设fd不为NULL。结合frame_data函数定义，当frame->opaque_ref分配失败时才会返回NULL，... |
| 9 | ffmpeg-6.1.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | 函数 skip_space 的返回值是一个指向输入字符串的指针，它不会返回 NULL。该函数仅跳过空格并返回指向下一个字符的指针，因此无需检查其返回值是否为 NULL。 |
| 11 | ffmpeg-6.1.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1392 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 12 | ffmpeg-6.1.1 | intercept_id3 | cpp/inconsistent-null-check | 1185 | FP | FP | 切片代码中，`seg` 指针在后续使用前，通过 `seg->size` 的访问进行了隐式空指针检查；如果 `seg` 为 NULL，`seg->size` 的访问将导致未定义行为，但代码逻辑表明 `seg->size >= 0` 的检... |
| 14 | ffmpeg-6.1.1 | init_muxer | cpp/inconsistent-null-check | 189 | FP | FP | ffofmt 是一个简单的内联转换函数，仅执行类型转换，不会返回空指针。切片代码中多处直接使用 of 指针访问其成员，表明其非空是安全的。 |
| 16 | ffmpeg-7.1.1 | upcase_string | cpp/offset-use-before-range-check | 1109 | FP | FP | 切片代码显示，for循环的条件 `src[i] && i < dst_size-1` 确保了只有当 `i` 小于 `dst_size-1` 时才会进入循环体，循环结束后 `i` 的值要么等于 `dst_size-1`，要么小于它（如果... |
| 17 | ffmpeg-7.1.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 切片代码中，在警告所在行（while循环条件）已经包含了对变量`j`的范围检查`j < tab`，这确保了`j`在访问数组`charset`和`row`时不会越界，因此该告警是误报。 |
| 18 | ffmpeg-7.1.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 切片代码中，变量 `j` 在 while 循环条件 `j < tab` 之前已被初始化为 0，且 `tab` 的值由前一个循环计算得出，确保 `j` 的访问在有效范围内。循环条件 `j < tab` 提供了范围检查，防止越界访问。 |
| 19 | ffmpeg-7.1.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码中，在警告所在行的循环条件 `i<w_r` 已经对索引 `i` 进行了范围检查，确保 `i` 不会超过 `w_r`，因此不存在越界访问的风险。 |
| 20 | ffmpeg-7.1.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警所在的for循环条件中，变量'i'的使用（`i<w_r`）与范围检查（`i<w_r`）是同时进行的，且循环体内部没有对'i'进行可能导致越界的修改。因此，'i'的使用并未先于范围检查，告警不成立。 |
| 21 | ffmpeg-7.1.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 148 | FP | FP | 切片代码中，while循环条件 `m < b && m < nb_entries - 1` 已经对变量 `m` 进行了范围检查，确保其不会越界访问 `entries` 数组。因此，该告警是误报。 |
| 22 | ffmpeg-7.1.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 223 | FP | FP | 切片代码中，在访问 `q->subs[i + 1]` 之前，已通过条件 `i < q->nb_subs - 1` 进行了明确的数组边界检查，确保了索引 `i+1` 的有效性，因此不存在越界访问风险。 |
| 23 | ffmpeg-7.1.1 | enc_open | cpp/inconsistent-null-check | 189 | FP | FP | 切片代码中，`desc` 指针在后续的 `if (!(desc->props & AV_SIDE_DATA_PROP_GLOBAL))` 条件中被直接解引用，这表明代码逻辑假设 `av_frame_side_data_desc` 的返... |
| 24 | ffmpeg-7.1.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部实现仅跳过空格字符，不涉及内存分配或可能返回NULL的复杂操作，其返回值始终是有效的指针（输入字符串的偏移位置），因此无需进行NULL检查。告警是基于调用模式统计的误报。 |
| 26 | ffmpeg-7.1.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1461 | FP | FP | 切片代码显示，在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有可用帧，且 `ff_framequeue_peek` 内部包含 `av_as... |
| 27 | ffmpeg-7.1.1 | hls_read_header | cpp/inconsistent-null-check | 2158 | FP | FP | 切片代码显示，在调用av_find_input_format后，其返回值in_fmt被直接用于后续的avformat_open_input等函数，但切片中未包含对in_fmt是否为NULL的显式检查。然而，根据告警规则，该警告是基于统... |
| 28 | ffmpeg-7.1.1 | intercept_id3 | cpp/inconsistent-null-check | 1240 | FP | FP | 在切片代码中，`seg` 指针在后续使用前（如 `seg->size`）未进行空指针检查，但 `current_segment` 函数可能返回 NULL 的逻辑并未在切片中直接导致解引用空指针。告警仅基于统计模式（87%的调用检查了N... |
| 29 | ffmpeg-7.1.1 | init_muxer | cpp/inconsistent-null-check | 190 | FP | FP | 切片代码显示 `ffofmt` 是一个简单的内联类型转换函数，它直接返回转换后的指针，不会返回 NULL。因此，调用结果不需要进行空指针检查，告警属于误报。 |
| 30 | ffmpeg-7.1.1 | cmp_dm_level0 | cpp/overflow-buffer | 294 | FP | FP | 切片代码显示，memcmp操作的大小是通过结构体总大小减去成员偏移量计算得出的，这确保了比较范围不会超出结构体边界，是安全的缓冲区操作。 |
| 32 | ffmpeg-7.0.1 | upcase_string | cpp/offset-use-before-range-check | 1108 | FP | FP | 切片代码显示，for循环的条件 `src[i] && i < dst_size-1` 已经对索引 `i` 进行了范围检查，确保在访问 `dst[i]` 和 `src[i]` 时 `i` 不会越界。循环结束后，`i` 的值是安全的，因此... |
| 33 | ffmpeg-7.0.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在切片代码中，变量 `j` 在 `while` 循环条件 `j < tab` 之前已被初始化为0，且循环条件本身包含了 `j < tab` 的范围检查，确保了 `j` 不会超过 `tab` 的值。因此，该告警是误报。 |
| 34 | ffmpeg-7.0.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 切片代码中，在警告所在行（while循环条件）已经包含了对变量j的范围检查（j < tab），这确保了j不会超出tab的边界，因此该告警是误报。 |
| 35 | ffmpeg-7.0.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码中，在警告所在行的循环条件 `i<w_r` 已经对变量 `i` 进行了范围检查，确保其不会超出 `w_r` 的边界，因此不存在越界访问的风险。 |
| 36 | ffmpeg-7.0.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警行使用变量 `i` 的循环条件 `i<w_r` 中，`i` 的值（初始化为0）已先于其数组访问 `temp[i]` 和 `src[i]` 进行了范围检查，确保了索引不会越界。代码逻辑是安全的。 |
| 37 | ffmpeg-7.0.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | FP | 切片代码中，while循环条件 `m < b && m < nb_entries - 1` 已经对变量 `m` 进行了范围检查，确保其不会越界访问 `entries` 数组。因此，在访问 `entries[m]` 之前，`m` 的值是... |
| 38 | ffmpeg-7.0.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 215 | FP | FP | 切片代码显示，在访问 `q->subs[i + 1]` 之前，已经通过条件 `i < q->nb_subs - 1` 进行了明确的数组边界检查，确保了索引 `i+1` 的有效性，因此不存在越界访问风险。 |
| 39 | ffmpeg-7.0.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部逻辑保证其返回值不会为NULL，它只是跳过空格并返回移动后的指针，因此无需进行NULL检查。 |
| 41 | ffmpeg-7.0.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1455 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 42 | ffmpeg-7.0.1 | hls_read_header | cpp/inconsistent-null-check | 2107 | FP | FP | 切片代码显示，在调用 `av_find_input_format` 后，其返回值 `in_fmt` 被直接用于后续的 `strstr(in_fmt->name, "mov")` 和 `avformat_open_input` 调用。然... |
| 43 | ffmpeg-7.0.1 | intercept_id3 | cpp/inconsistent-null-check | 1190 | FP | FP | 切片代码中，`seg` 指针在后续使用前，通过 `seg->size >= 0` 等条件进行了间接校验，且 `read_from_url` 函数内部也安全地处理了 `seg` 指针，表明代码逻辑已隐含了对空指针的防护。 |
| 45 | ffmpeg-7.0.1 | init_muxer | cpp/inconsistent-null-check | 189 | FP | FP | ffofmt函数是一个简单的内联类型转换函数，它只是将AVOutputFormat指针转换为FFOutputFormat指针，不会返回NULL。切片代码中多处直接使用返回的指针访问成员，表明调用者信任其非空。 |
| 47 | ffmpeg-7.1 | upcase_string | cpp/offset-use-before-range-check | 1109 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了当 `i` 被用于访问 `dst[i]` 和赋值 `dst[i] = 0` 时，`i` 的值严格小于 `dst_size-1`，因此 `dst[i] = 0` 的访... |
| 48 | ffmpeg-7.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 切片代码显示，在告警所在的while循环条件中，变量j的使用已包含范围检查'j < tab'，这确保了j不会超出有效范围，因此该告警是误报。 |
| 49 | ffmpeg-7.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 切片代码中，变量 `j` 在 while 循环条件 `j < tab` 之前已被初始化为 0，且 `tab` 的值由前一个循环计算得出，确保 `j` 的访问在 `row` 和 `charset` 数组范围内。循环条件 `j < tab... |
| 50 | ffmpeg-7.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码显示，在警告所在行的循环条件 `i<w_r` 中，变量 `i` 的使用（在条件判断中）与范围检查 `i<w_r` 是同时进行的，这确保了 `i` 在后续数组访问 `dst[i]` 和 `b[i]` 时不会越界。因此，该告警是误报。 |
| 51 | ffmpeg-7.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在警告所在行的循环条件 `i<w_r` 中，变量 `i` 的使用（在地址计算中）发生在与 `w_r` 的范围检查之前，但该检查是循环条件的一部分，确保了 `i` 在有效范围内。循环的逻辑保证了 `i` 不会超出 `w_r... |
| 53 | ffmpeg-7.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 223 | FP | FP | 切片代码显示，在访问 `q->subs[i + 1]` 之前，已经通过条件 `i < q->nb_subs - 1` 进行了范围检查，确保了 `i+1` 是有效索引，因此不存在越界访问风险。 |
| 54 | ffmpeg-7.1 | enc_open | cpp/inconsistent-null-check | 189 | FP | FP | 切片代码中，在调用`av_frame_side_data_desc`后，其返回值`desc`被直接用于访问`desc->props`，这隐含了对`desc`非空的假设。结合告警规则`cpp/inconsistent-null-chec... |
| 55 | ffmpeg-7.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部逻辑保证其返回值不会为NULL，它只是跳过空格并返回移动后的指针，因此无需进行NULL检查。 |
| 57 | ffmpeg-7.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1461 | FP | FP | 切片代码显示，在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_ass... |
| 58 | ffmpeg-7.1 | hls_read_header | cpp/inconsistent-null-check | 2109 | FP | FP | 切片代码显示，在调用`av_find_input_format`后，其返回值`in_fmt`被直接用于后续的`strstr(in_fmt->name, "mov")`和`avformat_open_input`调用。然而，这些使用都发... |
| 59 | ffmpeg-7.1 | intercept_id3 | cpp/inconsistent-null-check | 1191 | FP | FP | 切片代码中，`seg` 指针在后续使用前（如 `seg->size`）未进行空指针检查，但 `current_segment` 函数可能返回 NULL 的逻辑并未在切片中直接导致解引用错误。告警基于统计模式（87%的调用检查了NULL... |
| 61 | ffmpeg-7.1 | init_muxer | cpp/inconsistent-null-check | 190 | FP | FP | ffofmt函数是一个简单的内联类型转换函数，它直接返回转换后的指针，不会返回NULL。在切片代码中，该函数的返回值被直接使用，没有空指针检查是安全的，因为输入s->oformat本身是有效的。 |
| 64 | ffmpeg-6.0 | upcase_string | cpp/offset-use-before-range-check | 1044 | FP | FP | 切片代码显示，for循环的条件 `src[i] && i < dst_size-1` 已经对偏移量 `i` 进行了范围检查，确保在访问 `src[i]` 和 `dst[i]` 之前 `i` 是有效的。循环后的 `dst[i] = 0;... |
| 65 | ffmpeg-6.0 | capture_screen | cpp/offset-use-before-range-check | 485 | FP | FP | 切片代码中，在警告所在行 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 已经对 `j` 进行了范围检查 `j < tab`，这确保了循... |
| 66 | ffmpeg-6.0 | capture_screen | cpp/offset-use-before-range-check | 485 | FP | FP | 切片代码中，在告警行使用变量 `j` 之前，已经通过 `j = 0;` 进行了初始化，并且在 `while` 循环条件中包含了 `j < tab` 的范围检查，确保了 `j` 在访问数组 `row` 和 `charset` 时不会越界。 |
| 67 | ffmpeg-6.0 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | FP | 切片代码中，while循环的条件 `m < b && m < nb_entries - 1` 已经对变量 `m` 进行了范围检查，确保其在访问 `entries[m]` 之前不会越界。因此，该告警是误报。 |
| 68 | ffmpeg-6.0 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 207 | FP | FP | 切片代码中，在访问 `q->subs[i + 1]` 之前，已经通过条件 `i < q->nb_subs - 1` 进行了明确的数组下标范围检查，确保了 `i+1` 不会越界。因此该告警为误报。 |
| 69 | ffmpeg-6.0 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数是一个简单的内联函数，它只是跳过空格并返回移动后的指针，不会返回NULL。因此，检查其返回值是否为NULL是没有意义的，工具基于调用模式统计的告警在此处是误报。 |
| 71 | ffmpeg-6.0 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1373 | FP | FP | 切片代码显示，在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_ass... |
| 72 | ffmpeg-6.0 | intercept_id3 | cpp/inconsistent-null-check | 1184 | FP | FP | 切片代码显示，`seg` 指针在后续使用前（如 `seg->size`）未进行空指针检查，但 `current_segment` 函数可能返回 NULL 的逻辑并未在切片中直接导致解引用空指针。告警基于统计模式（80%的调用检查了NU... |
| 74 | ffmpeg-6.0 | init_muxer | cpp/inconsistent-null-check | 185 | FP | FP | 切片代码显示 `ffofmt` 是一个简单的内联类型转换函数，它直接返回转换后的指针，不会返回空值。该函数没有失败路径，因此无需进行空值检查。 |
| 75 | ffmpeg-6.0 | url_alloc_for_protocol | cpp/unbounded-write | 102 | FP | FP | 切片代码显示，目标缓冲区 `uc->filename` 的大小是通过 `strlen(filename) + 1` 精确分配的，`strcpy` 操作不会导致缓冲区溢出。 |
| 76 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1194 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后分配新内存并检查成功后才进行解引用和赋值，不存在对已释放内存的访问。 |
| 77 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1195 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，但随后立即用 `OPENSSL_malloc` 的结果重新赋值。警告所指的 `sc->ext.s... |
| 78 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1196 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，并且新分配的内存地址已正确赋值给sc->ext.session_ticket->data，不存在对已释放内存的访问。 |
| 79 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1196 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，并且sc->ext.session_ticket指针在分配内存后进行了非空检查，未发现对已释放内存的访问。告警可能源于工具对指针运算（sc->ext... |
| 80 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1198 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后检查新分配的内存是否为 NULL，并在 `ext_data` 为 ... |
| 81 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1199 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后分配新内存，并在分配失败时返回，确保了后续对 `sc->ext.... |
| 83 | openssl-openssl-3.5.1 | tls_parse_stoc_npn | cpp/use-after-free | 1660 | FP | FP | 切片代码显示，在调用memcpy之前，s->ext.npn已被释放并立即重新分配了新内存，不存在对已释放内存的访问。告警点处的指针指向新分配的内存，因此是误报。 |
| 84 | openssl-openssl-3.5.1 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 切片代码显示，在告警行之前的代码路径中，`keySpec` 可能已被 `sk_OSSL_CMP_ATAV_pop_free(*keySpec, OSSL_CMP_ATAV_free);` 释放并设置为 NULL，因此后续的 `if (... |
| 85 | openssl-openssl-3.5.1 | <global> | cpp/offset-use-before-range-check | 266 | FP | FP | 切片代码显示，在for循环的条件中，对数组访问'src[i]'的检查'src[i] != '\0''与对索引'i'的范围检查'i < len'是同时进行的，这确保了索引'i'在访问前已通过范围检查，因此不存在越界访问风险。 |
| 86 | openssl-openssl-3.5.1 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 切片代码显示，变量'i'在循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'中被使用，但其值在循环初始化时被设置为0，且循环体为空，仅用于递增'i'直到条件不满足。'i'的使用始终在循环条件自身的范围检... |
| 87 | openssl-openssl-3.5.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 345 | FP | FP | 切片代码中，在调用 `CRYPTO_THREAD_get_local` 后，立即使用 `assert(data != NULL)` 对返回值进行了非空断言。这表明代码逻辑假设并强制要求该返回值非空，若为空则程序会中止，因此该告警点在实... |
| 88 | openssl-openssl-3.5.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 切片代码显示，在调用`ossl_qrl_enc_level_set_get`后，其返回值`el`被直接用于访问成员`el->state`和`el->cctx`，但在此之前，函数`ossl_qrl_enc_level_set_has_k... |
| 90 | openssl-openssl-3.5.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 切片代码中，在调用`ossl_list_uint_set_head(s)`获取指针`f`后，立即在`if (start <= f->range.start ...)`中解引用`f->range.start`，这表明代码逻辑假设`f`不... |
| 91 | openssl-openssl-3.5.1 | ts_check_status_info | cpp/unsafe-strcat | 385 | FP | FP | 切片代码显示，`failure_text` 数组的大小为 `TS_STATUS_BUF_SIZE`，且 `strcat` 操作的目标字符串 `ts_failure_info[i].text` 来自一个编译时已知的静态数组 `ts_fa... |
| 92 | openssl-openssl-3.5.1 | <global> | cpp/unbounded-write | 30 | FP | FP | 切片代码显示，在调用strcpy之前，已通过CRYPTO_malloc分配了strlen(str) + 1大小的内存，确保了目标缓冲区大小足以容纳源字符串（包括终止空字符），因此不存在缓冲区溢出的风险。 |
| 93 | openssl-openssl-3.5.1 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的大小检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而防止缓冲区溢出。 |
| 94 | openssl-openssl-3.5.1 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的大小检查（`if (len + 1 >= size)` 和 `if (len + 1 + strlen(RFILE) + 1 >= size)`），如果环境变量字符串长度超过目标缓冲区大小... |
| 96 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3468 | FP | FP | 切片代码显示告警点是对宏 QUIC_RAISE_NON_NORMAL_ERROR 的调用，该宏已明确定义并展开为对 quic_raise_non_normal_error 函数的调用，参数传递完整且符合宏定义，未见明显的未终止可变参数... |
| 97 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3477 | FP | FP | 告警指出对quic_raise_non_normal_error的调用应使用0作为终止符，但切片中显示的宏QUIC_RAISE_NON_NORMAL_ERROR已正确封装了该调用，其参数列表是完整的，未见明显的格式错误或安全风险。 |
| 98 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3487 | FP | FP | 告警指出的调用使用了两个参数，而宏定义显示该调用是合法的，且切片中未发现可变参数列表使用不当的证据；该告警可能是工具对宏展开模式的误判。 |
| 99 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3493 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它调用 quic_raise_non_normal_error 函数，其参数列表在宏定义中是明确的，没有使用可变参数（variadic）的迹象。告警提示缺... |
| 100 | openssl-openssl-3.5.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3409 | FP | FP | 告警提示调用`quic_raise_non_normal_error`应使用0作为终止符，但切片代码显示是通过宏`QUIC_RAISE_NON_NORMAL_ERROR`调用，该宏已固定传递`(ctx), OPENSSL_FILE, ... |
| 101 | openssl-openssl-3.5.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3421 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确展开为 `quic_raise_non_normal_error` 函数，其参数列表在切片中可见且完整，未发现未终止的可变参数调用问题。 |
| 102 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1846 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它被正确展开为对 quic_raise_non_normal_error 的调用，并传递了所有必需的参数（包括文件、行号、函数名、原因和消息）。没有证据表... |
| 103 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1853 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，展开为对 quic_raise_non_normal_error 的调用，其参数列表在宏定义中已明确终止，不存在未终止的可变参数调用风险。 |
| 104 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1861 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它调用 `quic_raise_non_normal_error` 函数，其参数列表在宏定义中是明确的，没有使用可变参数（variadic）的迹象。告警提... |
| 105 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 切片代码显示，在循环读取 `from` 指针前，已通过 `mask = ~constant_time_is_zero(flen);` 和 `flen -= 1 & mask;` 等操作确保 `flen` 非负时才进行指针递减和读取，这... |
| 106 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 切片代码显示告警点 `good = constant_time_is_zero(em[0]);` 中的 `em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，且后续循环 `for ... |
| 107 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 切片代码显示，指针运算和访问受`mask`变量和`flen`递减逻辑的保护，`mask`由`constant_time_is_zero(flen)`计算，当`flen`耗尽时`mask`为0，从而阻止越界读取。这是恒定时间安全代码模式... |
| 108 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 切片代码显示，对指针 `em` 的访问（`em[0]`）发生在循环 `for (from += flen, em += num, i = 0; i < num; i++)` 之后，该循环已将 `em` 指针递减 `num` 次，使其指... |
| 109 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 切片代码显示，在访问 `em[1]` 之前，`em` 指针已通过 `OPENSSL_malloc(num)` 分配了 `num` 字节的内存，并且后续循环 `for (i = 0; i < num; i++)` 确保了 `em` 指向... |
| 110 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1171 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后对新分配的内存进行了空指针检查，访问 `sc->ext.sessi... |
| 111 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1172 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后，新分配的内存地址被赋值给同一个指针变量，因此警告行 `sc->e... |
| 112 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1173 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，并且新分配的内存指针sc->ext.session_ticket已成功分配（否则函数提前返回0）。因此，memcpy操作是安全的，不存在对已释放内存... |
| 113 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1173 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，并且新分配的内存地址已成功赋值给sc->ext.session_ticket->data，不存在对已释放内存的访问。 |
| 114 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1175 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其设置为 NULL。随后分配新内存，并检查分配是否成功。在 `ext_data` 为 N... |
| 115 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1176 | FP | FP | 切片代码显示，在将`sc->ext.session_ticket->data`设置为NULL之前，已经通过`OPENSSL_free`释放了旧指针并分配了新内存，这是对结构体成员的正确初始化，不存在对已释放内存的访问。 |
| 116 | openssl-openssl-3.3.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1626 | FP | FP | 切片代码显示，在调用memcmp比较`s->session->ext.alpn_selected`之前，已经通过`ossl_assert`和条件判断确保该指针非空且长度匹配，且`s->s3.alpn_selected`在分配失败时已提... |
| 117 | openssl-openssl-3.3.1 | tls_parse_stoc_npn | cpp/use-after-free | 1581 | FP | FP | 切片代码显示，在调用memcpy之前，已通过OPENSSL_malloc为s->ext.npn分配了新内存，并检查了分配结果。对同一指针的释放和重新分配是安全的操作序列，不存在对已释放内存的访问。 |
| 118 | openssl-openssl-3.3.1 | RSA_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 109 | FP | FP | 切片代码显示变量'i'在for循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'中被使用，但该条件已包含对'i'的范围检查（i < (maskedDBLen - 1)），确保在访问DB[i]之前'i'不... |
| 119 | openssl-openssl-3.3.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 447 | FP | FP | 切片代码显示函数体为空，未调用CRYPTO_THREAD_get_local，因此工具报告的未检查空指针的问题在可见上下文中不存在，属于误报。 |
| 120 | openssl-openssl-3.3.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 切片代码显示，在调用`ossl_qrl_enc_level_set_get`后，其返回值`el`被直接用于访问成员（如`el->state`），这表明调用者预期返回值非空。此外，被调用的`ossl_qrl_enc_level_set_... |
| 122 | openssl-openssl-3.3.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在切片代码中，变量 `f` 在解引用前（`f->range.start`）已被用于条件判断 `if (start <= f->range.start && end >= z->range.end)`，这表明 `f` 被假定为非空。此外... |
| 123 | openssl-openssl-3.3.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | 切片代码显示，目标缓冲区 `failure_text` 的大小为 `TS_STATUS_BUF_SIZE`，且循环拼接的源字符串 `ts_failure_info[i].text` 是静态定义的常量数组元素，其长度在编译时已知。通过循... |
| 125 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 2860 | FP | FP | 切片代码显示，目标缓冲区 `evp_cmac_name` 是通过 `app_malloc` 精确分配了 `sizeof("cmac()") + strlen(evp_mac_ciphername)` 大小的内存，`sprintf` 写... |
| 126 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 29 | FP | FP | 切片代码显示，在调用strcpy之前，已通过CRYPTO_malloc分配了strlen(str) + 1大小的内存，目标缓冲区大小与源字符串长度精确匹配，因此不会发生缓冲区溢出。 |
| 127 | openssl-openssl-3.3.1 | RAND_file_name | cpp/unbounded-write | 309 | FP | FP | 切片代码在调用strcpy前，已通过条件`len + 1 >= size`检查了目标缓冲区大小，确保不会发生溢出。该防护机制使告警无效。 |
| 128 | openssl-openssl-3.3.1 | RAND_file_name | cpp/unbounded-write | 313 | FP | FP | 切片代码中，在调用strcpy之前，已通过条件`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`对目标缓冲区大小进行了检查，确保不会发生溢出。 |
| 129 | openssl-openssl-3.3.1 | main | cpp/unbounded-write | 82 | FP | FP | 目标缓冲区 `pathname` 是通过 `malloc(PATH_MAX)` 分配的，其大小固定为 `PATH_MAX`，而源字符串 `argv[n]` 是命令行参数，其长度在切片中未见限制。虽然存在潜在的缓冲区溢出风险，但 `PA... |
| 130 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3131 | FP | FP | 切片代码显示，QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，其展开的函数调用参数列表在切片中已明确终止，未发现未终止的可变参数调用风险。告警提示的终止符使用问题在提供的上下文中不成立。 |
| 131 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3140 | FP | FP | 告警提示未使用0作为可变参数调用的终止符，但切片代码中`QUIC_RAISE_NON_NORMAL_ERROR`宏的调用参数数量固定，且被调用函数`quic_raise_non_normal_error`的定义未在切片中显示需要0作为... |
| 132 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3150 | FP | FP | 告警指出的调用是宏 `QUIC_RAISE_NON_NORMAL_ERROR` 的展开，该宏已正确传递了 `(msg)` 参数，且切片中未显示该宏或底层函数 `quic_raise_non_normal_error` 存在可变参数列表... |
| 133 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3156 | FP | FP | 切片代码显示，宏QUIC_RAISE_NON_NORMAL_ERROR的调用格式与定义一致，其最后一个参数`msg`是一个字符串字面量或NULL，并非可变参数列表，因此不存在未终止的可变参数调用问题。告警是基于统计模式（81/90次调... |
| 134 | openssl-openssl-3.3.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3072 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确传递了所有参数（包括一个 `NULL` 消息），其展开的函数 `quic_raise_non_normal_error` 的参数列表在切片中不可见，但... |
| 135 | openssl-openssl-3.3.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3084 | FP | FP | 告警提示对`quic_raise_non_normal_error`的调用应使用0作为终止符，但切片代码显示该调用是通过宏`QUIC_RAISE_NON_NORMAL_ERROR`进行的，其参数列表是固定的，且切片中未见可变参数（va... |
| 136 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1544 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 宏被正确调用，其参数数量与宏定义匹配，且告警信息本身是关于函数调用习惯的统计性提示（81 of 90 calls do），而非代码中实际存在未终止的可变参数调用错误。 |
| 137 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1551 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，展开为对 `quic_raise_non_normal_error` 的调用，其参数列表是固定的，包含 `(ctx), OPENSSL_FILE, OPE... |
| 138 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1561 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，展开为对 `quic_raise_non_normal_error` 的调用，其参数列表是固定的，不存在可变参数列表（variadic）未正确终止的风险。... |
| 139 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 221 | FP | FP | 切片代码显示，在循环读取数据前，指针`from`和`em`的移动以及循环条件`i < num`和掩码`mask`的计算共同确保了内存访问不会越界。`mask`由`constant_time_is_zero(flen)`生成，当`fle... |
| 140 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 229 | FP | FP | 切片代码显示告警点 `good = constant_time_is_zero(em[0]);` 中的 `em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，且后续循环 `for ... |
| 141 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 切片代码显示，循环访问指针 `from` 和 `em` 时使用了掩码 `mask` 进行条件控制，`mask` 的值由 `constant_time_is_zero(flen)` 决定，当 `flen` 耗尽时，`mask` 为0，从... |
| 142 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 切片代码显示，指针 `em` 是通过 `OPENSSL_malloc(num)` 分配的内存，其大小为 `num`。在循环 `for (from += flen, em += num, i = 0; i < num; i++)` 中，... |
| 143 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 切片代码显示，对指针'em'的访问（em[0], em[1]）发生在循环'for (i = 0; i < num; i++)'之后，该循环已确保'em'指针被正确递减并指向分配内存的有效起始位置，因此访问是安全的，不会越界。 |
| 144 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1182 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后，`OPENSSL_malloc` 的返回值被赋给同一个指针变量，... |
| 145 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1183 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已使用 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后，新分配的内存地址被赋值给同一个指针变量，不存在对已释放内存的访问... |
| 146 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且已为新分配的sc->ext.session_ticket检查了内存分配成功。代码逻辑在切片内是安全的，不存在对已释放内存的访问。 |
| 147 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保sc->ext.session_ticket不为NULL，并且数据指针sc->ext.session_ticket->data被正确指向新分配的内存区域，不存在对已释放内存的访问。 |
| 148 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1186 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后分配新内存并检查成功后才访问其成员，不存在对已释放内存的访问。 |
| 149 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1187 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后分配新内存，并根据 `ext_data` 是否为 NULL 来设置... |
| 150 | openssl-openssl-3.4.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1689 | FP | FP | 切片代码显示，在调用memcmp比较`s->session->ext.alpn_selected`和`s->s3.alpn_selected`之前，`s->s3.alpn_selected`已通过OPENSSL_malloc分配内存，... |
| 151 | openssl-openssl-3.4.1 | tls_parse_stoc_npn | cpp/use-after-free | 1620 | FP | FP | 切片代码显示，在调用memcpy之前，s->ext.npn已被释放并立即通过OPENSSL_malloc重新分配了新内存。对同一指针的释放和重新分配是连续且原子性的操作，不存在在memcpy时使用已释放内存的路径。 |
| 152 | openssl-openssl-3.4.1 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 切片代码显示，在告警行之前的代码路径中，`keySpec` 指针可能已被 `sk_OSSL_CMP_ATAV_pop_free(*keySpec, OSSL_CMP_ATAV_free);` 释放并置为悬空，后续的 `if (keyS... |
| 153 | openssl-openssl-3.4.1 | <global> | cpp/offset-use-before-range-check | 246 | FP | FP | 切片代码显示，在for循环的条件中，对数组索引'i'的使用（src[i]）与范围检查（i < len）是同时进行的，且检查位于访问之前，这确保了访问的安全性，因此是误报。 |
| 154 | openssl-openssl-3.4.1 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 切片代码显示，变量'i'在for循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'中已与范围'(maskedDBLen - 1)'进行了比较，其后续使用'DB[i++]'是在该范围检查之后，因此是安全的。 |
| 155 | openssl-openssl-3.4.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 489 | FP | FP | 切片代码中，在调用CRYPTO_THREAD_get_local后，立即使用`assert(data != NULL);`对返回值进行了非空断言，这表明代码逻辑假设并强制要求该值非空，因此无需额外的空值检查。 |
| 156 | openssl-openssl-3.4.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 切片代码显示，在调用`ossl_qrl_enc_level_set_get`后，其返回值`el`被直接用于访问成员`el->state`和`el->cctx`，但在此之前，函数`ossl_qrl_enc_level_set_has_k... |
| 157 | openssl-openssl-3.4.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在切片代码中显示，当 `enc_level` 参数有效且 `require_prov` 为0时，它保证返回一个指向有效数组元素的非空指针。因此，在 `ossl_q... |
| 158 | openssl-openssl-3.4.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在切片代码中，对 `f` 的首次使用位于条件 `if (start <= f->range.start && end >= z->range.end)` 中，该条件仅在 `f` 和 `z` 均非空时才有意义，且后续代码逻辑表明 `f`... |
| 159 | openssl-openssl-3.4.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | 切片代码显示，`failure_text` 数组的大小由 `TS_STATUS_BUF_SIZE` 宏定义，且拼接的源字符串 `ts_failure_info[i].text` 来自编译时常量数组 `ts_failure_info`，... |
| 160 | openssl-openssl-3.4.1 | <global> | cpp/unbounded-write | 30 | FP | FP | 切片代码显示，在调用strcpy之前，已通过CRYPTO_malloc分配了精确的strlen(str) + 1字节内存，目标缓冲区大小与源字符串长度完全匹配，因此不会发生缓冲区溢出。 |
| 161 | openssl-openssl-3.4.1 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的长度检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而避免了缓冲区溢出。 |
| 162 | openssl-openssl-3.4.1 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的大小检查（`len + 1 >= size` 或 `len + 1 + strlen(RFILE) + 1 >= size`），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NU... |
| 164 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3149 | FP | FP | 切片代码显示，QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，其展开的函数调用参数列表是固定的，由宏定义确保格式正确。告警提示的“未终止的可变参数调用”在此上下文中不适用，因为宏调用提供了所有必需的参数，没有使用可变... |
| 165 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3158 | FP | FP | 告警指出对quic_raise_non_normal_error的调用应使用0作为终止符，但切片代码中QUIC_RAISE_NON_NORMAL_ERROR宏的定义和调用均未使用可变参数列表，其参数数量固定，因此不存在未终止的可变参数... |
| 166 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3168 | FP | FP | 告警提示调用 quic_raise_non_normal_error 时应使用 0 作为终止符，但切片代码中 QUIC_RAISE_NON_NORMAL_ERROR 宏的定义显示其参数列表是固定的（包含 ctx, reason, ms... |
| 167 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3174 | FP | FP | 切片代码中，QUIC_RAISE_NON_NORMAL_ERROR 宏的调用格式与告警点一致，且其定义明确接受两个参数（reason 和 msg），不存在未终止的可变参数调用问题。告警是基于统计模式（81/90 调用使用 0 作为终止... |
| 168 | openssl-openssl-3.4.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3090 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数，与宏定义匹配，切片中未见未终止的可变参数调用问题。该告警可能是工具对宏展开模式的误判。 |
| 169 | openssl-openssl-3.4.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3102 | FP | FP | 告警提示调用 quic_raise_non_normal_error 时应使用 0 作为终止符，但切片代码中 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，其展开后调用 quic_raise_non_normal_... |
| 170 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1546 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它被正确调用并传递了固定数量的参数（ctx, reason, msg），没有使用可变参数列表，因此不存在未终止的可变参数调用问题。 |
| 171 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1553 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，展开为对 quic_raise_non_normal_error 的调用，其参数列表在宏定义中是完整的，没有使用可变参数，因此不存在未终止的可变参数调用问题。 |
| 172 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1563 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 调用在切片代码中是一个宏，其展开为 `quic_raise_non_normal_error` 函数。该宏调用提供了三个参数（ctx, reason, msg），... |
| 173 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 切片代码显示，在循环读取 `from` 指针时，使用了 `flen` 递减和 `mask` 掩码进行边界控制，确保不会越界访问。告警点 `*--em = *from & mask;` 的访问受 `mask` 保护，当 `flen` 耗... |
| 174 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 切片代码显示告警点 `good = constant_time_is_zero(em[0]);` 中的 `em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，且后续循环 `for ... |
| 175 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 切片代码显示，循环访问 `from` 指针时使用了 `mask` 变量进行条件控制，该 `mask` 由 `constant_time_is_zero(flen)` 计算得出，确保在 `flen` 耗尽后不会进行越界读取。代码使用了恒... |
| 176 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 切片代码显示，指针 `em` 是通过 `OPENSSL_malloc(num)` 分配的有效内存，且后续循环 `for (i = 0; i < num; i++)` 确保了对 `em` 数组的写入在边界内。告警点 `em[0]` 的访... |
| 177 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 切片代码显示，对指针 `em` 的访问（如 `em[0]`）发生在 `em = OPENSSL_malloc(num)` 分配内存之后，且访问索引为常量0和1，在分配的内存范围内。代码使用常数时间函数进行边界和值检查（如 `const... |
| 178 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1138 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，但随后立即为其分配了新内存并检查了分配结果。在后续使用 `sc->ext.session_tic... |
| 179 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1139 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后，`OPENSSL_malloc` 的返回值被赋给同一个指针，不存... |
| 180 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1140 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且已为新分配的sc->ext.session_ticket检查了内存分配成功。数据源ext_data是函数参数，其内容被安全复制到新分配的内存中，不... |
| 181 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1140 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且已为新分配的sc->ext.session_ticket分配了内存，不存在对已释放内存的访问。 |
| 182 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1142 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后，新分配的内存被赋值给同一个指针变量，不存在对已释放内存的解引用... |
| 183 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1143 | FP | FP | 切片代码显示，在将`sc->ext.session_ticket->data`设置为NULL之前，已经通过`OPENSSL_free`释放了旧指针并分配了新内存，新指针`sc->ext.session_ticket`被重新赋值。对`d... |
| 184 | openssl-openssl-3.2.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1626 | FP | FP | 切片代码显示，在调用memcmp比较s->session->ext.alpn_selected之前，s->s3.alpn_selected已通过OPENSSL_malloc分配内存，且分配失败时函数已提前返回，因此memcmp使用的指... |
| 185 | openssl-openssl-3.2.1 | tls_parse_stoc_npn | cpp/use-after-free | 1581 | FP | FP | 切片代码显示，在调用memcpy之前，s->ext.npn已被释放并立即通过OPENSSL_malloc重新分配了新内存，不存在对已释放内存的访问。告警点memcpy使用的是新分配的内存指针，因此是误报。 |
| 186 | openssl-openssl-3.2.1 | RSA_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 109 | FP | FP | 切片代码显示，变量'i'在for循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'中被使用，但该条件本身包含了范围检查'i < (maskedDBLen - 1)'，确保在访问DB[i]之前'i'不会越... |
| 187 | openssl-openssl-3.2.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 切片代码显示，在调用 `ossl_qrl_enc_level_set_get` 后，其返回值 `el` 被直接用于访问成员 `el->state`，这隐含了 `el` 非空的假设。结合被调用函数 `ossl_qrl_enc_level... |
| 189 | openssl-openssl-3.2.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在切片代码中，对 `f` 的首次使用位于条件 `if (start <= f->range.start && end >= z->range.end)` 中，该条件仅在 `f` 和 `z` 均不为 NULL 时才会被评估。由于 `z`... |
| 192 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 2826 | FP | FP | 切片代码显示，目标缓冲区 `evp_cmac_name` 是通过 `app_malloc` 动态分配的，其大小精确计算为 `sizeof("cmac()") + strlen(evp_mac_ciphername)`，足以容纳格式化字... |
| 193 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 29 | FP | FP | 切片代码显示，在调用strcpy之前，已通过CRYPTO_malloc分配了strlen(str) + 1大小的内存，目标缓冲区大小与源字符串长度精确匹配，因此不会发生缓冲区溢出。 |
| 194 | openssl-openssl-3.2.1 | RAND_file_name | cpp/unbounded-write | 309 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的大小检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而避免了缓冲区溢出。 |
| 195 | openssl-openssl-3.2.1 | RAND_file_name | cpp/unbounded-write | 313 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的大小检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而防止了缓冲区溢出。 |
| 197 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3054 | FP | FP | 切片代码显示，QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，其展开后调用 `quic_raise_non_normal_error` 函数。该宏的最后一个参数 `(msg)` 是一个字符串字面量，并非可变参数列表的... |
| 198 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3063 | FP | FP | 切片代码显示告警点调用的宏 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确展开为 `quic_raise_non_normal_error` 函数，且该函数为可变参数函数，其定义未在切片中提供，但调用格式与宏定义一... |
| 199 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3073 | FP | FP | 告警提示调用 `quic_raise_non_normal_error` 应使用值0作为终止符，但切片代码中该函数是通过宏 `QUIC_RAISE_NON_NORMAL_ERROR` 调用的，其参数列表已明确包含 `(ctx), OP... |
| 200 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3079 | FP | FP | 切片代码显示，QUIC_RAISE_NON_NORMAL_ERROR 宏的调用格式与宏定义一致，传递了正确数量的参数（ctx, reason, msg），未见未终止的可变参数调用问题。告警可能源于工具对宏展开模式的误判。 |
| 201 | openssl-openssl-3.2.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 2995 | FP | FP | 切片代码显示告警点是对宏 QUIC_RAISE_NON_NORMAL_ERROR 的调用，该宏已正确展开为对 quic_raise_non_normal_error 函数的调用，并传递了所有必需的参数（包括文件、行号、函数名、原因和消... |
| 202 | openssl-openssl-3.2.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3007 | FP | FP | 告警提示调用`quic_raise_non_normal_error`应使用0作为终止符，但切片代码中`QUIC_RAISE_NON_NORMAL_ERROR`是一个宏，其展开后调用`quic_raise_non_normal_err... |
| 203 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1520 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它被展开为对 `quic_raise_non_normal_error` 的调用，其参数列表在宏定义中是明确的，并且告警点提供的参数数量与宏定义匹配，不存... |
| 204 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1527 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它调用 quic_raise_non_normal_error 函数，但切片中未提供该函数的定义，无法确认其是否为可变参数函数以及是否需要终止符。基于告警... |
| 205 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1537 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它调用 quic_raise_non_normal_error 函数，但切片中未提供该函数的定义，无法确认其是否为可变参数函数以及是否缺少终止符。基于告警... |
| 206 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 221 | FP | FP | 切片代码显示，在循环读取数据前，已通过条件判断确保指针访问在边界内（使用mask变量和flen递减控制），且使用了恒定时间操作来避免时序侧信道，这表明代码已包含防护机制，不会发生越界读取。 |
| 207 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 229 | FP | FP | 切片代码显示告警点 `good = constant_time_is_zero(em[0]);` 中的 `em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，且后续循环 `for ... |
| 208 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 切片代码显示，指针运算和数组访问均在循环条件 `i < num` 和 `flen` 的动态掩码 `mask` 控制下进行，`mask` 由 `constant_time_is_zero(flen)` 生成，确保当 `flen` 耗尽时... |
| 209 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 切片代码显示，对指针 `em` 的访问 `em[0]` 发生在 `em` 被分配内存 (`OPENSSL_malloc(num)`) 之后，且循环 `for (from += flen, em += num, i = 0; i < n... |
| 210 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 切片代码显示，对指针'em'的访问（如em[0], em[1]）发生在循环'for (i = 0; i < num; i++)'之后，该循环已确保'em'指针被正确递减并初始化了'num'个元素，因此访问em[0]和em[1]在边界内... |
| 211 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1182 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后，代码检查了新分配的内存是否为 NULL，并在分配失败时提前返回。... |
| 212 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1183 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后，新分配的内存地址被赋值给同一个指针变量，不存在对已释放内存的访... |
| 213 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件`if (ext_data != NULL)`进行了检查，并且`sc->ext.session_ticket`指针在分配内存后也进行了非空校验，因此不会发生对已释放内存的访问。 |
| 214 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保sc->ext.session_ticket不为NULL，并且对ext_data进行了非空检查。代码逻辑在切片可见范围内是安全的，不存在对已释放内存的访问。 |
| 215 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1186 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其设置为 NULL。随后对新分配的内存进行了空指针检查，并在 `ext_data` 为 ... |
| 216 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1187 | FP | FP | 切片代码显示，在将 `sc->ext.session_ticket->data` 设置为 NULL 之前，已经通过 `OPENSSL_free` 释放了旧指针并分配了新内存，不存在对已释放内存的访问。告警点是对新分配结构体成员的初始化... |
| 217 | openssl-openssl-3.4.0 | tls_parse_stoc_alpn | cpp/use-after-free | 1688 | FP | FP | 切片代码显示，在调用memcmp比较s->session->ext.alpn_selected和s->s3.alpn_selected之前，s->s3.alpn_selected已通过OPENSSL_malloc分配内存，且分配失败时... |
| 218 | openssl-openssl-3.4.0 | tls_parse_stoc_npn | cpp/use-after-free | 1619 | FP | FP | 切片代码显示，在调用memcpy之前，已通过OPENSSL_malloc为s->ext.npn分配了新的内存，并检查了分配结果。对s->ext.npn的释放和重新分配是连续且受控的，不存在对已释放内存的访问。 |
| 219 | openssl-openssl-3.4.0 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 切片代码显示，在告警行之前的代码路径中，`*keySpec` 可能已被 `sk_OSSL_CMP_ATAV_pop_free` 释放并设置为 NULL，因此后续的 `if (keySpec != NULL) *keySpec = NU... |
| 220 | openssl-openssl-3.4.0 | <global> | cpp/offset-use-before-range-check | 246 | FP | FP | 切片代码显示，在for循环条件中，对数组访问'src[i]'之前，已经通过'i < len'进行了范围检查，并且循环条件确保了在访问前会检查字符串终止符，因此不存在越界访问风险。 |
| 221 | openssl-openssl-3.4.0 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 切片代码显示，变量'i'在for循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'中与范围检查同时使用，且后续访问'DB[i++]'发生在循环之后，此时'i'的值由循环逻辑保证不会超出'maskedDB... |
| 222 | openssl-openssl-3.4.0 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 470 | FP | FP | 切片代码中，在调用`CRYPTO_THREAD_get_local`后，立即使用`assert(data != NULL)`对返回值进行了严格的非空断言检查，这确保了后续代码不会在空指针上操作。因此，虽然返回值未在条件语句中显式检查，... |
| 223 | openssl-openssl-3.4.0 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 切片代码显示，在调用`ossl_qrl_enc_level_set_get`后，其返回值`el`被直接用于访问成员`el->state`和`el->cctx`，这表明调用者假设返回值非空。此外，被调用的`ossl_qrl_enc_le... |
| 225 | openssl-openssl-3.4.0 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 切片代码中，在调用 `ossl_list_uint_set_head(s)` 并将其赋值给 `f` 后，立即在 `if (start <= f->range.start ...)` 中解引用了 `f->range.start`，这表明... |
| 227 | openssl-openssl-3.4.0 | <global> | cpp/unbounded-write | 30 | FP | FP | 切片代码显示，在调用strcpy之前，已通过CRYPTO_malloc分配了strlen(str) + 1字节的内存，大小与源字符串长度精确匹配，因此不会发生缓冲区溢出。 |
| 228 | openssl-openssl-3.4.0 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的大小检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而防止缓冲区溢出。 |
| 229 | openssl-openssl-3.4.0 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的大小检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而避免了缓冲区溢出。 |
| 231 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3136 | FP | FP | 切片代码显示，宏 QUIC_RAISE_NON_NORMAL_ERROR 的调用格式正确，其参数列表以 NULL 作为最后一个参数，这符合可变参数函数调用需要显式终止符的规则，因此告警是误报。 |
| 232 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3145 | FP | FP | 切片代码显示，宏 QUIC_RAISE_NON_NORMAL_ERROR 被正确调用，其参数数量与宏定义匹配，且告警所指的调用位置（传递两个参数）与同一宏的其他调用（如传递三个参数）在语法上均有效，未见实际的未终止可变参数调用错误。 |
| 233 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3155 | FP | FP | 告警指出的调用使用了两个参数（reason和msg），而宏定义显示该调用实际传递了五个参数（包括ctx、文件、行号、函数名），符合宏的预期格式，不存在未终止的可变参数问题。 |
| 234 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3161 | FP | FP | 告警指出的调用是宏 `QUIC_RAISE_NON_NORMAL_ERROR` 的展开，该宏已正确传递了所有参数（包括一个字符串消息），且切片中未见可变参数列表的错误使用。该调用模式与代码库中其他调用一致，属于工具对宏展开的误判。 |
| 235 | openssl-openssl-3.4.0 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3077 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确传递了 `(msg)` 参数，切片中未发现变参调用缺少终止符 `0` 的证据；该宏展开后调用 `quic_raise_non_normal_error... |
| 236 | openssl-openssl-3.4.0 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3089 | FP | FP | 告警提示调用`quic_raise_non_normal_error`应使用0作为终止符，但切片代码显示该调用是通过宏`QUIC_RAISE_NON_NORMAL_ERROR`进行的，该宏的参数列表是固定的，且切片中未见可变参数调用。... |
| 237 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1546 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它被正确调用并传递了固定数量的参数（ctx, reason, msg），没有使用可变参数列表，因此不存在未终止的可变参数调用问题。 |
| 238 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1553 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它被正确调用并传递了三个参数（ctx, reason, msg），符合其定义。没有证据表明存在未终止的可变参数调用问题，该告警可能是工具对宏展开模式的误判。 |
| 239 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1563 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，它被展开为对 `quic_raise_non_normal_error` 的调用，并且该宏的最后一个参数 `(msg)` 是一个字符串字面量，并非可变参数... |
| 240 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 切片代码显示，在循环 `for (from += flen, em += num, i = 0; i < num; i++)` 中，指针 `from` 和 `em` 的移动以及数据复制操作受到 `mask` 和 `flen` 的精确控... |
| 241 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 切片代码显示，对指针 `em` 的访问 `em[0]` 发生在 `em = OPENSSL_malloc(num);` 成功分配内存之后，且 `em` 指针在循环中被正确递减和赋值，访问其索引0是安全的。告警所担心的指针越界情况在切片... |
| 242 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 切片代码显示，指针运算和数组访问均在循环条件 `i < num` 和 `flen` 的动态掩码 `mask` 控制下进行，`constant_time` 系列函数确保了操作的安全性，没有越界访问的证据。 |
| 243 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 切片代码显示，指针 `em` 是通过 `OPENSSL_malloc(num)` 分配的内存，其大小为 `num`。在循环 `for (from += flen, em += num, i = 0; i < num; i++)` 中，... |
| 244 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 切片代码显示，对指针`em`的访问（如`em[0]`、`em[1]`）发生在`em = OPENSSL_malloc(num)`分配内存之后，且循环和条件检查确保了索引访问在分配的内存边界内。告警指出的潜在越界读在切片可见的上下文中被... |
| 245 | git-2.47.1 | is_command | cpp/redundant-null-check-simple | 2602 | FP | FP | 告警指出的冗余空值检查是针对变量 `nick`，该变量是从静态数组 `todo_command_info` 中获取的字符，并非用户输入或可能为空的指针，其值在编译时已确定，因此空值检查是多余的，不构成安全问题。 |
| 246 | git-2.47.1 | refname_is_safe | cpp/no-space-for-terminator | 350 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，而 `restlen` 是 `strlen(rest)` 的结果，不包含空终止符。但 `xmallocz` 函数内部（通过 `do_xmallocz`）通常会为字符串分配额... |
| 247 | git-2.47.1 | fill_es_indent_data | cpp/offset-use-before-range-check | 894 | FP | FP | 在第一个while循环的条件中，对`s[off] == '\r'`的访问已通过`off < len - 1`进行了范围检查，确保了off不会越界访问数组`s`。切片代码中可见的防护机制表明该告警是误报。 |
| 248 | git-2.47.1 | ce_write_entry | cpp/offset-use-before-range-check | 2687 | FP | FP | 切片代码显示，在for循环的条件中，对变量'common'的使用（ce->name[common]）之前，已经通过'common < previous_name->len'进行了范围检查，确保了访问的安全性。 |
| 249 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 757 | FP | FP | 在for循环条件中，变量'pos'的使用已通过'pos < len'检查进行了范围保护，确保其不会超出有效边界，因此该告警为误报。 |
| 250 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 757 | FP | FP | 在for循环条件中，变量'pos'的使用（s1[pos] == s2[pos]）与范围检查（pos < len）是同时进行的，且'pos'的初始值为0，这确保了访问不会超出'len'指定的边界。切片代码显示这是一个安全的比较循环。 |
| 251 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 792 | FP | FP | 在切片代码的for循环条件中，变量'pos'在访问数组'wcs1[pos]'和'wcs2[pos]'之前，已经通过'pos < len'进行了范围检查，确保了访问不会越界。 |
| 252 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 792 | FP | FP | 在切片代码的for循环条件中，变量'pos'的使用已与'len'进行了范围检查（pos < len），确保了访问不会越界，因此该告警是误报。 |
| 253 | git-2.47.1 | setup_scoreboard | cpp/inconsistent-null-check | 2857 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，该条件已确保 `sb->final` 非空且其 OID 为空。`get_blame_suspects` 函数定义显示它可能返回 ... |
| 254 | git-2.47.1 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的函数 `branch_get` 在切片中明确显示，对于任何输入（包括NULL或空字符串）都会返回一个有效的 `struct branch` 指针（例如 `the_repository->remote_state->curren... |
| 256 | git-2.47.1 | update_head | cpp/inconsistent-null-check | 685 | FP | FP | 切片代码显示，调用 refs_update_ref 时使用了 UPDATE_REFS_DIE_ON_ERR 标志，这意味着如果更新失败（例如由于空指针），程序会调用 die() 函数终止，从而防止了空指针解引用。因此，即使 looku... |
| 258 | git-2.47.1 | do_fetch | cpp/inconsistent-null-check | 1628 | FP | FP | 切片代码中，在调用 branch_get(NULL) 后，其返回值 'branch' 被立即用于条件判断 'branch_has_merge_config(branch)'，该函数内部已包含对空指针的检查（'return branch... |
| 259 | git-2.47.1 | get_ref_map | cpp/inconsistent-null-check | 552 | FP | FP | 切片代码显示，在调用branch_get(NULL)后，其返回值`branch`被立即传递给`branch_has_merge_config`函数，该函数内部已包含对`branch`指针是否为空的检查（`return branch &... |
| 260 | git-2.47.1 | refspec_append_mapped | cpp/inconsistent-null-check | 90 | FP | FP | 切片代码显示，调用branch_get的参数branch_name来自skip_prefix对matched->name的处理，而matched是函数参数，其有效性由调用者保证。更重要的是，branch_get函数内部对name参数进... |
| 261 | git-2.47.1 | do_create_stash | cpp/inconsistent-null-check | 1390 | FP | FP | 切片代码显示，`head_commit` 在后续被 `repo_find_unique_abbrev` 和 `pp_commit_easy` 等函数直接解引用，这表明调用者预期 `lookup_commit` 总能成功返回一个有效的提... |
| 262 | git-2.47.1 | reset_tree | cpp/inconsistent-null-check | 285 | FP | FP | 切片代码显示，parse_tree_indirect的返回值tree在下一行立即被parse_tree(tree)检查，该检查会处理NULL情况并返回错误。因此，虽然没有显式的NULL指针检查，但存在等效的错误处理机制，使得代码是安全的。 |
| 264 | git-2.47.1 | write_bundle_refs | cpp/inconsistent-null-check | 435 | FP | FP | 在切片代码中，`lookup_commit_reference` 返回的指针 `one` 在解引用前（`one->object`）被使用，但该使用位于 `if (e->item == &(one->object))` 条件判断中。此条... |
| 265 | git-2.47.1 | update_one | cpp/inconsistent-null-check | 328 | FP | FP | 在切片代码中，调用find_subtree时传入的create参数为1，这确保了函数在找不到子树时会创建并返回一个新的非空子树指针，因此返回值不可能为NULL，无需进行空指针检查。 |
| 266 | git-2.47.1 | verify_one_commit_graph | cpp/inconsistent-null-check | 2774 | FP | FP | 切片代码显示，`lookup_commit` 的返回值 `graph_commit` 在后续被直接用于 `parse_commit_in_graph_one` 和 `get_commit_tree_in_graph_one` 等函数调... |
| 267 | git-2.47.1 | unparse_commit | cpp/inconsistent-null-check | 188 | FP | FP | 切片代码显示，lookup_commit函数内部已处理了空对象情况，当obj为空时会创建并返回一个新对象，因此调用者无需进行空指针检查。 |
| 269 | git-2.47.1 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 143 | FP | FP | 在切片代码中，对parse_object的返回值tag进行了后续访问（tag->tagged），这隐含了对指针非空的假设。如果parse_object返回NULL，解引用将导致崩溃，但该函数在调用前已通过oid_object_info... |
| 270 | git-2.47.1 | find_merge_parents | cpp/inconsistent-null-check | 616 | FP | FP | 告警点`obj = parse_object(...)`的返回值在后续代码中直接传递给`repo_peel_to_type`函数，而该函数内部（切片已包含）会检查对象是否为NULL并处理，因此存在有效的防护机制，使得直接检查返回值变得... |
| 271 | git-2.47.1 | get_parent | cpp/inconsistent-null-check | 1107 | FP | FP | 切片代码显示，在调用 `lookup_commit_reference` 后，其返回值 `commit` 被立即传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 的调用本身隐含了对 `c... |
| 272 | git-2.47.1 | show_ambiguous_object | cpp/inconsistent-null-check | 442 | FP | FP | 切片代码显示，在调用 `lookup_tag` 后，其返回值 `tag` 被直接传递给 `parse_tag(tag)` 使用。`parse_tag` 函数内部会检查 `tag` 是否为 NULL（通过 `item->object.p... |
| 273 | git-2.47.1 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3344 | FP | FP | 函数 `lookup_decoration` 在内部已对空指针 `n->size` 进行了检查，并在未找到匹配项时返回 NULL。调用方 `leave_one_treesame_to_parent` 虽未显式检查返回值，但后续循环仅遍... |
| 274 | git-2.47.1 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 701 | FP | FP | 切片代码显示，lookup_commit函数内部已处理了空对象指针的情况（若obj为空则创建新对象），因此调用处不检查null是安全的，符合该函数的预期行为。 |
| 275 | git-2.47.1 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在内部已处理了空对象指针的情况，若 `lookup_object` 返回 NULL，它会调用 `create_object` 创建新对象并返回，因此调用者无需额外检查返回值是否为 NULL。 |
| 287 | git-2.47.1 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1660 | FP | FP | 切片代码显示，`buffer` 是通过 `xmallocz_gently(size)` 分配的，该函数分配了 `size + 1` 字节的内存，因此 `buffer[size] = '\0';` 的写入是在分配的内存边界内，不会发生越界。 |
| 288 | git-2.47.1 | should_prune_worktree | cpp/invalid-pointer-deref | 788 | FP | FP | 指针 `path` 由 `xmallocz(len)` 分配，该函数分配了 `len+1` 字节的内存，确保有空间存放终止符。代码在 `while` 循环后执行 `path[len] = '\0'`，其中 `len` 已递减以去除换行... |
| 289 | git-2.50.1 | refname_is_safe | cpp/no-space-for-terminator | 353 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，而 `restlen` 是 `strlen(rest)` 的结果，不包含空终止符。但 `normalize_path_copy` 函数要求目标缓冲区足够容纳源字符串及其空终... |
| 290 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在切片代码中，变量 `pos` 在 `for` 循环条件 `s1[pos] == s2[pos] && pos < len` 中被使用，但其访问发生在 `pos < len` 的范围检查之前。然而，`pos` 的初始值为 0，且循环在... |
| 291 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，对`s1[pos]`和`s2[pos]`的访问发生在`pos < len`的检查之前，这违反了先检查后使用的原则。然而，该循环的目的是在`len... |
| 292 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 切片代码中，变量 `pos` 在 `for` 循环条件 `pos < len` 中已进行范围检查，确保其不会超出 `len` 边界，因此后续在 `p_snprintf` 中使用 `pos` 是安全的。 |
| 293 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 切片代码中，变量'pos'在for循环条件'pos < len'中已进行范围检查，确保其值在有效范围内后才被用于格式化字符串，因此不存在越界使用风险。 |
| 294 | git-2.50.1 | setup_scoreboard | cpp/inconsistent-null-check | 2858 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，该条件已确保 `sb->final` 非空且其 OID 为空。`get_blame_suspects` 函数定义显示其可能返回 ... |
| 295 | git-2.50.1 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的函数 `branch_get` 在切片代码中明确显示，对于任何有效的输入（包括NULL或空字符串）都会返回一个有效的 `struct branch` 指针（例如 `the_repository->remote_state->c... |
| 296 | git-2.50.1 | write_index_patch | cpp/inconsistent-null-check | 1435 | FP | FP | lookup_tree 被调用时传入的是已知的、有效的空树对象哈希值（the_repository->hash_algo->empty_tree），该调用不会返回 NULL。因此，无需进行 NULL 检查，告警为误报。 |
| 297 | git-2.50.1 | bisect_successful | cpp/inconsistent-null-check | 648 | FP | FP | 切片代码显示，在调用 `lookup_commit_reference_by_name` 之前，已经通过 `refs_read_ref` 读取了引用并获取了对象ID，这确保了 `bad_ref` 是一个有效的引用，因此后续的 `com... |
| 299 | git-2.50.1 | <global> | cpp/inconsistent-null-check | 547 | FP | FP | lookup_tree 调用使用 the_repository->hash_algo->empty_tree 作为参数，这是一个已知的、有效的内部常量对象ID，不可能返回 NULL。因此，对返回值的空值检查是不必要的，该告警是误报。 |
| 300 | git-2.50.1 | get_ref_map | cpp/inconsistent-null-check | 550 | FP | FP | 切片代码中，branch_get(NULL)的返回值被立即传递给branch_has_merge_config函数，该函数内部已包含对NULL指针的检查（`return branch && !!branch->merge;`），因此后... |
| 301 | git-2.50.1 | refspec_append_mapped | cpp/inconsistent-null-check | 92 | FP | FP | 切片代码显示，`branch_get`函数内部已对`name`参数进行了空指针和空字符串检查，并返回有效的`struct branch`指针，调用后直接访问其成员`branch->merge_nr`是安全的，因此告警为误报。 |
| 302 | git-2.50.1 | do_create_stash | cpp/inconsistent-null-check | 1397 | FP | FP | 切片代码显示 `head_commit` 在后续被 `repo_find_unique_abbrev` 和 `pp_commit_easy` 等函数直接解引用，这表明调用者预期 `lookup_commit` 返回非空值。结合上下文，... |
| 303 | git-2.50.1 | reset_tree | cpp/inconsistent-null-check | 286 | FP | FP | 切片代码中，parse_tree_indirect的返回值tree在下一行立即作为参数传递给parse_tree函数，该函数内部会检查其有效性并返回错误码。调用者检查了parse_tree的返回值，并在错误时返回-1，这构成了对tre... |
| 305 | git-2.50.1 | update_one | cpp/inconsistent-null-check | 333 | FP | FP | find_subtree函数在create参数为1时（如告警行调用）保证返回非空指针，因为它在找不到子树时会创建新子树并返回。切片中后续代码直接访问sub->cache_tree，未检查NULL，这符合create=1时的预期行为，因... |
| 306 | git-2.50.1 | verify_one_commit_graph | cpp/inconsistent-null-check | 2798 | FP | FP | 切片代码显示，lookup_commit 的返回值 graph_commit 在后续被直接使用（例如访问 graph_commit->parents），这表明代码逻辑假设 lookup_commit 总是成功返回有效的 commit ... |
| 307 | git-2.50.1 | unparse_commit | cpp/inconsistent-null-check | 189 | FP | FP | 切片代码显示，lookup_commit函数内部已处理了空对象情况，若obj为空会创建新对象并返回，因此调用者无需额外检查NULL。函数逻辑保证了返回的指针有效。 |
| 309 | git-2.50.1 | deref_without_lazy_fetch | cpp/inconsistent-null-check | 156 | FP | FP | 在调用 parse_object 之前，代码已通过 oid_object_info_extended 检查了对象类型，并确认其为 OBJ_TAG。对于标签对象，parse_object 预期返回有效指针，且后续代码直接访问 tag->... |
| 310 | git-2.50.1 | find_merge_parents | cpp/inconsistent-null-check | 617 | FP | FP | 切片代码显示，`parse_object` 返回的 `obj` 指针在后续代码中仅用于调用 `add_merge_parent` 函数，该函数内部仅使用 `obj->oid` 字段。`obj` 在解引用前已通过 `parse_oid_... |
| 311 | git-2.50.1 | get_parent | cpp/inconsistent-null-check | 1110 | FP | FP | 切片代码显示，在调用 `lookup_commit_reference` 后，其返回值 `commit` 被立即传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 函数会检查 `commi... |
| 312 | git-2.50.1 | show_ambiguous_object | cpp/inconsistent-null-check | 443 | FP | FP | 切片代码显示，在调用 `lookup_tag` 后，其返回值 `tag` 被立即传递给 `parse_tag(tag)` 进行解析检查。`parse_tag` 函数内部会处理空指针或无效对象的情况并返回错误，因此代码逻辑已包含对返回值... |
| 313 | git-2.50.1 | setup_pending_objects | cpp/inconsistent-null-check | 333 | FP | FP | 切片代码显示，在后续使用 root_tree_list 之前，存在对 info->trees 的检查，如果 info->trees 为假，则 root_tree_list 保持为初始值 NULL，且后续使用 root_tree_lis... |
| 314 | git-2.50.1 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3351 | FP | FP | 切片代码显示，在调用 `lookup_decoration` 后，其返回值 `ts` 并未被直接解引用或用于可能导致空指针解引用的操作。该告警仅基于调用模式统计，而切片内未提供任何证据表明此处的空值会导致实际的安全漏洞或崩溃。 |
| 315 | git-2.50.1 | add_cache_tree | cpp/inconsistent-null-check | 1775 | FP | FP | 切片代码显示，`lookup_tree`函数内部已处理空指针情况，若`lookup_object`返回NULL，它会调用`create_object`创建新对象并返回，因此调用者无需额外检查NULL。 |
| 316 | git-2.50.1 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 706 | FP | FP | 切片代码显示，lookup_commit函数内部已处理空对象情况（若obj为NULL则创建新对象），因此调用处无需显式检查NULL。代码逻辑保证了返回的commit指针有效，告警为误报。 |
| 317 | git-2.50.1 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 根据lookup_commit函数的定义，当查找对象失败时，函数会调用create_object创建一个新对象并返回，因此该函数不会返回NULL。切片代码中对该函数的调用无需进行NULL检查是安全的。 |
| 318 | git-2.50.1 | has_uncommitted_changes | cpp/inconsistent-null-check | 2642 | FP | FP | lookup_tree 被调用时传入的是 the_hash_algo->empty_tree，这是一个已知的、有效的内置对象标识符，不会返回 NULL。因此，无需进行空指针检查，告警为误报。 |
| 319 | git-2.50.1 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 操作仅在 `ARRAY_SIZE(string) > 0` 的编译时断言通过时才会执行，且 `string` 是字面量 `D... |
| 320 | git-2.50.1 | test_ctype__ispunct | cpp/overflow-buffer | 91 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含了 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数 `PUNCT`，其具体内容未在切片中给出。然而，宏内包含 `BUIL... |
| 321 | git-2.50.1 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 操作仅在 `ARRAY_SIZE(string) > 0` 时执行，且该条件由 `BUILD_ASSERT_OR_ZERO`... |
| 322 | git-2.50.1 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 操作仅在 `ARRAY_SIZE(string) > 0` 的编译时断言通过时才会执行，且 `string` 是一个字面量字... |
| 323 | git-2.50.1 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | FP | FP | 切片代码显示，宏 `ARRAY_SIZE(string)` 用于计算长度，且 `BUILD_ASSERT_OR_ZERO` 确保数组大小大于0，因此 `len` 的计算不会导致负索引访问。告警源于对宏展开的静态分析误解，实际运行时不会... |
| 324 | git-2.50.1 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 操作仅在 `ARRAY_SIZE(string) > 0` 的编译时断言通过时才会执行，且传入的字符串字面量 `"*?[\\... |
| 325 | git-2.50.1 | test_ctype__isalnum | cpp/overflow-buffer | 51 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含了 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数，在调用处为 `LOWER UPPER DIGIT`，这是一个字符串字... |
| 326 | git-2.50.1 | test_ctype__isalpha | cpp/overflow-buffer | 46 | FP | FP | 宏定义中 `ARRAY_SIZE(string) - 1` 仅在数组大小为0时结果为-1，但宏内包含 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)` 断言，确保数组大小大于0，因此不会发生... |
| 327 | git-2.50.1 | test_ctype__isdigit | cpp/overflow-buffer | 41 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string) > 0` 的编译时断言通过时才会执行，这确保了数组大小至少为1，因此索引 `-... |
| 328 | git-2.50.1 | <global> | cpp/overflow-buffer | 36 | FP | FP | 切片代码显示函数体为空，没有数组定义或索引操作，工具报告的负索引访问在可见上下文中不存在。 |
| 330 | git-2.50.1 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1684 | FP | FP | 告警指向的写入操作 `buffer[size] = '\0';` 是安全的，因为 `buffer` 由 `xmallocz_gently(size)` 分配，该函数分配了 `size + 1` 字节的内存，确保索引 `size` 在边... |
| 331 | git-2.50.1 | should_prune_worktree | cpp/invalid-pointer-deref | 965 | FP | FP | 切片代码显示，在写入 `path[len] = '\0';` 之前，存在一个 while 循环，当 `len` 大于 0 且末尾字符为换行符时，`len` 会递减。这确保了写入操作不会超出 `xmallocz(len)` 分配的原始缓... |
| 332 | git-2.49.0 | is_command | cpp/redundant-null-check-simple | 2614 | FP | FP | 切片代码显示，变量 `nick` 是从结构体数组 `todo_command_info` 中读取的字符，其值在编译时已知，且 `nick` 在逻辑表达式中先于空指针检查被使用（`nick && *p++ == nick`），因此对 `... |
| 333 | git-2.49.0 | refname_is_safe | cpp/no-space-for-terminator | 353 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，而 `restlen` 是 `strlen(rest)` 的结果，不包含空终止符。但 `normalize_path_copy` 函数要求目标缓冲区足够容纳源字符串及其空终... |
| 334 | git-2.49.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 895 | FP | FP | 切片代码中，在第一个while循环的条件 `s[off] == '\r'` 之后，明确包含了 `off < len - 1` 的边界检查，这确保了在访问 `s[off]` 之前，`off` 不会超出有效范围。因此，该告警是误报。 |
| 335 | git-2.49.0 | ce_write_entry | cpp/offset-use-before-range-check | 2689 | FP | FP | 变量 `common` 在 for 循环条件中已通过 `common < previous_name->len` 进行了范围检查，确保其不会超过 `previous_name->len`，后续使用 `ce->name + common... |
| 336 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在切片代码中，变量 `pos` 在 `for` 循环条件 `s1[pos] == s2[pos] && pos < len` 中被使用，但其访问 `s1[pos]` 和 `s2[pos]` 发生在 `pos < len` 的边界检查之... |
| 337 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在切片代码的for循环条件中，变量'pos'的递增和边界检查（pos < len）是同时进行的，这确保了'pos'在后续的p_snprintf调用中不会超出字符串长度'len'的范围。因此，该告警是误报。 |
| 338 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 切片代码中，变量 `pos` 在 `for` 循环条件 `pos < len` 中已进行范围检查，确保其值不会超过 `len`，然后才在 `p_snprintf` 中使用，因此不存在越界风险。 |
| 339 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 切片代码中，变量 `pos` 在 `for` 循环条件 `pos < len` 中已进行范围检查，确保其值不会超过 `len`，然后才在 `p_snprintf` 中使用，因此不存在越界风险。 |
| 340 | git-2.49.0 | setup_scoreboard | cpp/inconsistent-null-check | 2858 | FP | FP | 告警点位于条件分支 `if (is_null_oid(&sb->final->object.oid))` 内部，该条件已确保 `sb->final` 非空，且 `get_blame_suspects` 函数定义明确返回 `NULL` ... |
| 341 | git-2.49.0 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的函数 `branch_get` 在切片代码中明确显示，对于任何输入（包括NULL或空字符串）都会返回一个有效的 `struct branch` 指针，它要么返回 `the_repository->remote_state->c... |
| 342 | git-2.49.0 | write_index_patch | cpp/inconsistent-null-check | 1433 | FP | FP | lookup_tree函数在切片中被调用时，其参数是已知的、固定的空树哈希值（the_repository->hash_algo->empty_tree），这保证了函数会返回一个有效的树对象，不会返回NULL。因此，无需进行NULL检... |
| 345 | git-2.49.0 | <global> | cpp/inconsistent-null-check | 546 | FP | FP | lookup_tree 返回的 tree 指针被直接用于 add_pending_object，而 add_pending_object 的参数要求是非空对象；更重要的是，在切片代码的后续逻辑中，如果 obj 为空，会调用 die 函... |
| 346 | git-2.49.0 | do_fetch | cpp/inconsistent-null-check | 1756 | FP | FP | 切片代码显示，在调用 `branch_has_merge_config(branch)` 之前，对 `branch` 指针进行了显式检查（`branch && !!branch->merge`），这构成了有效的空指针防护，使得后续对 ... |
| 347 | git-2.49.0 | get_ref_map | cpp/inconsistent-null-check | 551 | FP | FP | 切片代码显示，在调用branch_get(NULL)后，其返回值`branch`被立即传递给`branch_has_merge_config`函数，该函数内部已包含对`branch`指针是否为空的检查（`return branch &... |
| 348 | git-2.49.0 | refspec_append_mapped | cpp/inconsistent-null-check | 92 | FP | FP | 切片代码显示，branch_get函数内部已对name参数进行了空指针和空字符串检查，并返回有效的branch结构体指针或通过make_branch创建，函数本身保证不会返回NULL。调用后直接访问branch->merge_nr是安全的。 |
| 349 | git-2.49.0 | do_create_stash | cpp/inconsistent-null-check | 1398 | FP | FP | 切片代码显示 `head_commit` 在后续被 `repo_find_unique_abbrev` 和 `pp_commit_easy` 等函数直接解引用，这表明调用者预期 `lookup_commit` 返回非空值。结合上下文，... |
| 350 | git-2.49.0 | reset_tree | cpp/inconsistent-null-check | 287 | FP | FP | 切片代码显示，parse_tree_indirect的返回值被立即传递给parse_tree函数，后者会检查其有效性并返回错误。代码逻辑在切片可见范围内确保了空指针会被捕获并处理，因此告警是误报。 |
| 352 | git-2.49.0 | update_one | cpp/inconsistent-null-check | 329 | FP | FP | find_subtree函数在create参数为1时保证返回非空指针（通过ALLOC_GROW和FLEX_ALLOC_MEM分配内存），切片中调用时create=1，因此无需空值检查。 |
| 353 | git-2.49.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2788 | FP | FP | 切片代码显示，`lookup_commit` 的返回值 `graph_commit` 在后续被直接用于 `parse_commit_in_graph_one` 和 `get_commit_tree_in_graph_one` 等函数调... |
| 354 | git-2.49.0 | unparse_commit | cpp/inconsistent-null-check | 188 | FP | FP | 切片代码显示，lookup_commit函数内部已处理了空对象情况，若obj为空则创建新对象并返回，因此调用处不检查null是安全的。 |
| 356 | git-2.49.0 | deref_without_lazy_fetch | cpp/inconsistent-null-check | 156 | FP | FP | 在调用 parse_object 后，代码立即访问了 tag->tagged，这隐含了对返回指针的非空检查；如果 parse_object 返回 NULL，解引用会导致崩溃，但代码逻辑表明此路径仅在 oid_object_info_e... |
| 357 | git-2.49.0 | find_merge_parents | cpp/inconsistent-null-check | 617 | FP | FP | 切片代码显示，parse_object 返回的 obj 指针在后续的 repo_peel_to_type 调用中被直接使用，而 repo_peel_to_type 函数内部会检查对象是否有效，若无效则返回 NULL，且后续代码有 `i... |
| 358 | git-2.49.0 | get_parent | cpp/inconsistent-null-check | 1108 | FP | FP | 切片代码中，`lookup_commit_reference` 的返回值 `commit` 在下一行立即作为 `repo_parse_commit` 的参数使用，后者会检查其有效性并返回错误（MISSING_OBJECT）。这表明代码... |
| 359 | git-2.49.0 | show_ambiguous_object | cpp/inconsistent-null-check | 443 | FP | FP | 切片代码显示，在调用 `lookup_tag` 后，其返回值 `tag` 被直接传递给 `parse_tag(tag)` 使用。`parse_tag` 函数内部会检查 `item` 参数的有效性，如果 `item` 为 NULL，`i... |
| 360 | git-2.49.0 | setup_pending_objects | cpp/inconsistent-null-check | 333 | FP | FP | 切片代码显示，在调用 `strmap_get` 获取 `root_tree_list` 后，后续使用该指针前（`oid_array_append(&root_tree_list->oids, &obj->oid)`）存在对 `info... |
| 361 | git-2.49.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3357 | FP | FP | 切片代码显示，在调用 `lookup_decoration` 后，其返回值 `ts` 被直接使用，但后续循环并未解引用 `ts`。结合告警信息，此规则仅基于统计模式（80%的调用检查了空值）触发，而当前切片中未显示存在因空值解引用导致... |
| 362 | git-2.49.0 | add_cache_tree | cpp/inconsistent-null-check | 1783 | FP | FP | 切片代码显示，`lookup_tree`函数内部已处理了空指针情况（若`lookup_object`返回NULL，则调用`create_object`创建新对象并返回），因此调用处无需额外检查NULL。此外，后续使用`tree->ob... |
| 363 | git-2.49.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 703 | FP | FP | 切片代码显示，lookup_commit函数内部已处理了空对象指针的情况（若obj为NULL则创建新对象），因此调用处不检查NULL是安全的，属于工具误报。 |
| 364 | git-2.49.0 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 切片代码显示，lookup_commit函数在内部已处理了空对象指针的情况（若obj为NULL则创建新对象），因此其返回值不会为NULL。后续对c->date的访问是安全的，该告警为误报。 |
| 365 | git-2.49.0 | has_uncommitted_changes | cpp/inconsistent-null-check | 2642 | FP | FP | lookup_tree 被调用时传入的是常量哈希值 the_hash_algo->empty_tree，该对象在仓库中始终存在，因此函数不会返回 NULL，无需检查。 |
| 366 | git-2.49.0 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的循环索引 `i` 范围固定为 0 到 255，不会产生负索引。告警所提示的负索引访问在给定的代码上下文中不可触发。 |
| 367 | git-2.49.0 | test_ctype__ispunct | cpp/overflow-buffer | 91 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)` 保... |
| 368 | git-2.49.0 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数 `CNTRL`，其具体内容未知。然而，宏内包含 `BUILD_ASSE... |
| 369 | git-2.49.0 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | FP | FP | 切片代码显示，宏 `ARRAY_SIZE(string)` 用于计算数组大小，`ARRAY_SIZE(string) - 1` 仅在数组大小为0时可能产生负索引，但宏 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(... |
| 370 | git-2.49.0 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string)` 用于计算长度，其中 `string` 是字符串字面量 `"$()*+.?[\\^{｜"`，其大小肯定大于0，因此 `ARRAY_SI... |
| 371 | git-2.49.0 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中 `ARRAY_SIZE(string) - 1` 的 `string` 是字面量 `"*?[\\"`，其大小固定且大于0，因此索引操作不会导致负索引访问。 |
| 372 | git-2.49.0 | test_ctype__isalnum | cpp/overflow-buffer | 51 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含了 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数，在调用处 `TEST_CHAR_CLASS(isalnum, LOW... |
| 373 | git-2.49.0 | test_ctype__isalpha | cpp/overflow-buffer | 46 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string) > 0` 时才会执行，且该条件由 `BUILD_ASSERT_OR_ZERO`... |
| 374 | git-2.49.0 | test_ctype__isdigit | cpp/overflow-buffer | 41 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string) > 0` 时执行，且 `BUILD_ASSERT_OR_ZERO` 宏在数组大... |
| 375 | git-2.49.0 | <global> | cpp/overflow-buffer | 36 | FP | FP | 切片代码显示函数体为空，不存在任何数组访问操作，因此工具报告的负索引访问告警不成立。 |
| 377 | git-2.49.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1677 | FP | FP | 切片代码显示，`buffer` 是通过 `xmallocz_gently(size)` 分配的，该函数分配 `size + 1` 字节的内存，而 `buffer[size] = '\0'` 写入的是该分配缓冲区的最后一个字节，因此是安... |
| 378 | git-2.49.0 | should_prune_worktree | cpp/invalid-pointer-deref | 960 | FP | FP | 切片代码显示，在写入 path[len] = '\0' 之前，存在一个 while 循环用于递减 len 以去除末尾的换行符，这确保了 len 至少为 0。当 len 为 0 时，写入操作 path[0] = '\0' 是安全的，因为... |
| 379 | git-2.46.0 | is_command | cpp/redundant-null-check-simple | 2601 | FP | FP | 告警指出的冗余空值检查是针对变量 `nick`，但切片代码显示 `nick` 是从结构体数组 `todo_command_info` 中直接读取的字符，并非指针，因此对其进行的空值检查 `nick &&` 是有效的逻辑判断，而非对解引... |
| 380 | git-2.46.0 | refname_is_safe | cpp/no-space-for-terminator | 345 | FP | FP | 函数 `xmallocz` 被调用时传递的参数是 `restlen`，而 `restlen` 是 `strlen(rest)` 的结果，不包含空终止符。但 `normalize_path_copy` 函数要求目标缓冲区足够容纳源字符串... |
| 381 | git-2.46.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 890 | FP | FP | 在第一个while循环的条件中，访问`s[off]`之前已经通过`off < len - 1`检查了偏移量`off`相对于长度`len`的范围，确保了访问的安全性。 |
| 382 | git-2.46.0 | ce_write_entry | cpp/offset-use-before-range-check | 2685 | FP | FP | 变量'common'在for循环条件中已通过'common < previous_name->len'进行了范围检查，确保其不会超过previous_name的长度，后续使用'ce->name + common'和'previous_... |
| 383 | git-2.46.0 | setup_scoreboard | cpp/inconsistent-null-check | 2857 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，该条件已确保 `sb->final` 非空且其 OID 为空。函数 `get_blame_suspects` 的定义显示它可能返... |
| 384 | git-2.46.0 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的函数 branch_get 在切片中明确显示，对于任何有效的输入（包括空指针或空字符串），它都会返回一个有效的 struct branch 指针（要么是 current_branch，要么是 make_branch 的结果），... |
| 386 | git-2.46.0 | update_head | cpp/inconsistent-null-check | 684 | FP | FP | 切片代码显示，当 `lookup_commit_reference` 返回的 `c` 为 NULL 时，后续的 `refs_update_ref` 调用会使用 `&c->object.oid`，这会导致空指针解引用。然而，该调用设置了... |
| 388 | git-2.46.0 | do_fetch | cpp/inconsistent-null-check | 1626 | FP | FP | 切片代码中，在调用 branch_get(NULL) 后，其返回值 'branch' 被直接用于条件判断 'branch_has_merge_config(branch)'。被调用的函数 'branch_has_merge_confi... |
| 389 | git-2.46.0 | get_ref_map | cpp/inconsistent-null-check | 551 | FP | FP | 切片代码显示，在调用 branch_get(NULL) 后，其返回值 'branch' 被直接传递给 branch_has_merge_config 函数，而该函数内部已包含对 NULL 指针的检查（`return branch &&... |
| 390 | git-2.46.0 | refspec_append_mapped | cpp/inconsistent-null-check | 88 | FP | FP | 被调用的函数 branch_get 在切片中明确显示，对于任何有效的分支名称（包括空名或'HEAD'），它都会返回一个有效的 struct branch 指针（例如 the_repository->remote_state->curr... |
| 391 | git-2.46.0 | do_create_stash | cpp/inconsistent-null-check | 1388 | FP | FP | 切片代码显示，`head_commit` 变量在后续被 `repo_find_unique_abbrev` 和 `pp_commit_easy` 等函数直接解引用，这表明 `lookup_commit` 的返回值预期为非空。结合上下文... |
| 392 | git-2.46.0 | reset_tree | cpp/inconsistent-null-check | 283 | FP | FP | 切片代码显示，`parse_tree_indirect`的返回值`tree`在下一行立即被传递给`parse_tree`函数进行校验，如果为NULL，`parse_tree`会返回错误（通过`parse_tree_gently`），导... |
| 394 | git-2.46.0 | write_bundle_refs | cpp/inconsistent-null-check | 430 | FP | FP | 在切片代码中，`lookup_commit_reference` 返回的指针 `one` 在解引用前（`one->object`）受到 `if (e->item == &(one->object))` 的保护，该条件仅在 `one` ... |
| 395 | git-2.46.0 | update_one | cpp/inconsistent-null-check | 327 | FP | FP | find_subtree函数在create参数为1时保证返回非空指针（通过FLEX_ALLOC_MEM分配内存），切片中调用时create=1，因此返回值无需空检查。 |
| 396 | git-2.46.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2774 | FP | FP | 切片代码显示，`lookup_commit` 的返回值 `graph_commit` 在后续被直接用于 `parse_commit_in_graph_one` 和 `get_commit_tree_in_graph_one` 等函数调... |
| 397 | git-2.46.0 | ahead_behind | cpp/inconsistent-null-check | 1069 | FP | FP | 切片代码显示，在调用 `prio_queue_get` 的循环前，函数 `queue_has_nonstale` 已确保队列中存在非过时提交，且 `prio_queue_get` 函数内部在队列为空时会返回 NULL，但此处循环条件保... |
| 398 | git-2.46.0 | paint_down_to_common | cpp/inconsistent-null-check | 81 | FP | FP | 切片代码显示，调用 `prio_queue_get` 的循环条件 `queue_has_nonstale(&queue)` 确保了队列非空，且 `prio_queue_get` 函数内部在 `queue->nr` 为0时会返回 NUL... |
| 399 | git-2.46.0 | unparse_commit | cpp/inconsistent-null-check | 182 | FP | FP | 切片代码显示，在调用`lookup_commit`后，代码立即访问`c->object.parsed`，这表明`c`被假定为非空。结合`lookup_commit`的函数定义，当`lookup_object`返回NULL时，它会调用`... |
| 401 | git-2.46.0 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 143 | FP | FP | 在调用 parse_object 后，代码立即访问了 tag->tagged，这隐含了对 tag 指针非空的检查，因为如果 tag 为 NULL，解引用 tag->tagged 会导致未定义行为。切片代码的逻辑表明开发者假设 pars... |
| 402 | git-2.46.0 | find_merge_parents | cpp/inconsistent-null-check | 616 | FP | FP | 切片代码显示，parse_object 返回的 obj 指针在后续代码中仅用于调用 add_merge_parent 函数，而该函数仅使用 obj->oid 字段，该字段在有效的 object 结构体中始终有效。即使 obj 为 NU... |
| 404 | git-2.46.0 | get_parent | cpp/inconsistent-null-check | 1098 | FP | FP | 切片代码中，`lookup_commit_reference` 的返回值 `commit` 被立即传递给 `repo_parse_commit` 进行校验，如果 `commit` 为 NULL，`repo_parse_commit` ... |
| 405 | git-2.46.0 | show_ambiguous_object | cpp/inconsistent-null-check | 436 | FP | FP | 切片代码中，在调用 `lookup_tag` 后，立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析和错误检查。`parse_tag` 函数内部会处理对象不存在或类型错误的情况并返回错误，因此存在对返回值的... |
| 407 | git-2.46.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3339 | FP | FP | 函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到项（`!ref->base`）的情况进行了处理并返回 NULL，调用方 `leave_one_treesame_to_parent` 虽未显... |
| 408 | git-2.46.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 690 | FP | FP | 切片代码显示，lookup_commit函数内部已处理了空对象指针的情况（若obj为空则创建新对象），因此调用处不检查null是安全的，符合函数的设计逻辑。 |
| 409 | git-2.46.0 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 切片代码显示，在调用lookup_commit后，其返回值`c`被直接用于访问`c->date`和`c->parents`，这表明代码逻辑假设调用总是成功。结合该函数是测试函数`test_parse_commit_in_graph`，... |
| 421 | git-2.46.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1649 | FP | FP | 切片代码显示，`buffer` 是通过 `xmallocz_gently(size)` 分配的，该函数分配 `size + 1` 字节的内存，而 `buffer[size] = '\0';` 写入的是该分配内存的最后一个字节，因此是安... |
| 422 | git-2.46.0 | should_prune_worktree | cpp/invalid-pointer-deref | 788 | FP | FP | 切片代码显示，在写入 `path[len] = '\0';` 之前，`len` 变量已通过 `while` 循环递减，确保 `len` 至少为0，因此写入位置 `path[len]` 不会超出 `xmallocz(len)` 分配的缓... |
| 423 | git-2.44.0 | is_command | cpp/redundant-null-check-simple | 2522 | FP | FP | 告警指出的冗余空值检查是针对变量 `nick`，该变量是从静态数组 `todo_command_info` 中获取的字符，其值在编译时已知，不可能为空。切片代码中的逻辑也表明 `nick` 被用作布尔条件，其空值检查是安全的编程习惯，... |
| 424 | git-2.44.0 | refname_is_safe | cpp/no-space-for-terminator | 342 | FP | FP | 函数 `xmallocz` 被调用时传入的参数是 `restlen`，而 `restlen` 是 `strlen(rest)` 的结果，不包含终止符的长度。`xmallocz` 函数内部（通过 `do_xmallocz`）通常会为终止... |
| 425 | git-2.44.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 869 | FP | FP | 切片代码显示，在第一个while循环的条件中，对`s[off] == '\r'`的访问已通过`off < len - 1`进行了范围检查，确保了off不会越界访问数组s。 |
| 426 | git-2.44.0 | ce_write_entry | cpp/offset-use-before-range-check | 2713 | FP | FP | 切片代码显示，变量'common'在for循环条件中已通过'common < previous_name->len'进行了范围检查，确保其不会超过previous_name的长度，因此后续使用'ce->name + common'是安全的。 |
| 427 | git-2.44.0 | setup_scoreboard | cpp/inconsistent-null-check | 2855 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 为真的分支内，此时 `sb->final` 是一个由 `fake_working_tree_commit` 函数创建的伪造提交，其 `blame_... |
| 428 | git-2.44.0 | inherit_tracking | cpp/inconsistent-null-check | 224 | FP | FP | 切片代码显示，`branch_get`函数内部对`name`参数进行了空指针和空字符串检查，并返回一个有效的`struct branch`指针（可能是`current_branch`或新创建的分支）。调用后立即访问`branch->r... |
| 429 | git-2.44.0 | bisect_successful | cpp/inconsistent-null-check | 640 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `read_ref(bad_ref, &oid)` 读取了引用，这确保了 `bad_ref` 是一个有效的引用名，因此 `lookup_co... |
| 432 | git-2.44.0 | do_fetch | cpp/inconsistent-null-check | 1611 | FP | FP | 切片代码显示，在调用 branch_get(NULL) 后，其返回值 'branch' 被立即用于条件判断 'branch_has_merge_config(branch)'，而 branch_has_merge_config 函数内... |
| 433 | git-2.44.0 | get_ref_map | cpp/inconsistent-null-check | 550 | FP | FP | 切片代码显示，branch_get(NULL)的返回值在后续的branch_has_merge_config函数中被显式检查是否为NULL，且该检查逻辑在切片中可见，因此不存在空指针解引用风险。 |
| 434 | git-2.44.0 | cmd_merge | cpp/inconsistent-null-check | 1638 | FP | FP | 切片代码显示，在调用 `repo_get_merge_bases` 后，其返回值 `common_one` 被直接用于访问 `common_one->item`，但在此之前，代码逻辑（如 `if (!remoteheads->next... |
| 435 | git-2.44.0 | refspec_append_mapped | cpp/inconsistent-null-check | 88 | FP | FP | 切片代码显示，`branch_get`函数内部对输入`name`进行了空指针和空字符串检查，并返回一个有效的`struct branch`指针（例如`current_branch`或`make_branch`的结果）。在调用点，`br... |
| 436 | git-2.44.0 | do_create_stash | cpp/inconsistent-null-check | 1378 | FP | FP | 切片代码显示，lookup_commit函数内部已处理空对象情况，若未找到对象会创建新对象并返回，因此调用结果不会为NULL。该告警是基于统计模式而非实际代码逻辑的误报。 |
| 437 | git-2.44.0 | reset_tree | cpp/inconsistent-null-check | 283 | FP | FP | 切片代码显示，在调用 `parse_tree_indirect` 后，其返回值 `tree` 被立即传递给 `parse_tree` 函数进行校验。`parse_tree` 函数内部会调用 `parse_tree_gently`，如果... |
| 439 | git-2.44.0 | write_bundle_refs | cpp/inconsistent-null-check | 428 | FP | FP | 在切片代码中，`lookup_commit_reference` 返回的指针 `one` 在解引用前（`one->object`）已通过 `if (e->item == &(one->object))` 的条件判断进行使用，这隐含了对... |
| 440 | git-2.44.0 | update_one | cpp/inconsistent-null-check | 325 | FP | FP | find_subtree函数在create参数为1时保证返回非空指针（通过ALLOC_GROW和FLEX_ALLOC_MEM分配内存），切片中调用时create=1，因此返回值不需要空检查。 |
| 441 | git-2.44.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2722 | FP | FP | 切片代码显示，lookup_commit 的返回值 graph_commit 在后续被直接用于 parse_commit_in_graph_one 和 get_commit_tree_in_graph_one 等函数，这些函数内部已对... |
| 442 | git-2.44.0 | ahead_behind | cpp/inconsistent-null-check | 1010 | FP | FP | 告警点位于while循环条件`queue_has_nonstale(&queue)`内部，该条件已确保队列中存在非STALE的提交对象，因此`prio_queue_get`调用时队列非空，返回NULL的可能性已被排除。切片代码的逻辑保... |
| 443 | git-2.44.0 | paint_down_to_common | cpp/inconsistent-null-check | 78 | FP | FP | 切片代码显示，调用 `prio_queue_get` 的循环条件 `queue_has_nonstale(&queue)` 保证了队列中至少有一个非 STALE 的提交，且 `prio_queue_get` 函数内部在 `queue-... |
| 444 | git-2.44.0 | unparse_commit | cpp/inconsistent-null-check | 179 | FP | FP | 切片代码显示，函数`lookup_commit`在内部已处理了`lookup_object`返回NULL的情况，会调用`create_object`创建新对象并返回，因此其返回值不会为NULL。后续对`c->object.parsed... |
| 445 | git-2.44.0 | clear_common_flag | cpp/inconsistent-null-check | 2124 | FP | FP | 切片代码显示，`lookup_object` 的调用位于 `while ((oid = oidset_iter_next(&iter)))` 循环内，该循环仅在 `oid` 非空时执行。`oid` 来自 `oidset_iter_ne... |
| 446 | git-2.44.0 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 141 | FP | FP | 在切片代码中，parse_object的返回值被立即赋值给一个struct tag指针，并随后通过`if (!tag->tagged)`进行了访问。这表明代码假设parse_object返回了有效的非空对象，且后续的tag->tagg... |
| 447 | git-2.44.0 | find_merge_parents | cpp/inconsistent-null-check | 614 | FP | FP | 切片代码显示，`parse_object` 返回的 `obj` 指针在下一行立即作为参数传递给 `repo_peel_to_type`，而 `repo_peel_to_type` 函数内部会检查传入的对象是否为 NULL 或解析失败，... |
| 448 | git-2.44.0 | get_rev | cpp/inconsistent-null-check | 187 | FP | FP | 切片代码显示，在调用 prio_queue_get 之前，已经检查了 data->rev_list.nr 是否为0，这确保了队列不为空时才会调用该函数。此外，prio_queue_get 函数内部也有对 queue->nr 的检查，并... |
| 449 | git-2.44.0 | get_parent | cpp/inconsistent-null-check | 1063 | FP | FP | 切片代码显示，`lookup_commit_reference` 的返回值 `commit` 被立即传递给 `repo_parse_commit` 进行解析，如果 `commit` 为 NULL，`repo_parse_commit`... |
| 450 | git-2.44.0 | show_ambiguous_object | cpp/inconsistent-null-check | 422 | FP | FP | 切片代码显示，在调用 `lookup_tag` 后，其返回值 `tag` 被直接传递给 `parse_tag` 函数进行解析检查。`parse_tag` 函数内部会处理对象不存在或类型错误的情况并返回错误，且后续代码逻辑（`if (!... |
| 451 | git-2.44.0 | fill_bitmap_commit | cpp/inconsistent-null-check | 416 | FP | FP | 切片代码显示，调用 `prio_queue_get` 的循环条件是 `while (queue->nr)`，而 `prio_queue_get` 函数定义明确指出，当 `queue->nr` 为 0 时会返回 NULL。由于循环条件确... |
| 452 | git-2.44.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3256 | FP | FP | 切片代码显示，在调用lookup_decoration后，变量`ts`未被直接解引用或用于可能导致空指针解引用的操作。函数`leave_one_treesame_to_parent`的后续逻辑仅遍历父提交，未使用`ts`，因此该未检查... |
| 453 | git-2.44.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 686 | FP | FP | 切片代码显示，lookup_commit函数内部已处理了空对象情况（若obj为空则创建新对象），因此调用处不检查null是安全的，属于工具误报。 |
| 454 | git-2.44.0 | <global> | cpp/inconsistent-null-check | 27 | FP | FP | 切片代码显示，在调用 `lookup_commit` 后，其返回值 `c` 被直接用于访问 `c->date` 和 `c->parents`，这表明代码逻辑假设调用总是成功。结合 `lookup_commit` 的函数定义，它在对象不... |
| 455 | git-2.44.0 | test_ctype_isxdigit | cpp/overflow-buffer | 59 | FP | FP | 切片代码显示，循环索引 i 的范围是 0 到 255，且函数 func 被调用时参数为 i 或 EOF。对 func(EOF) 的调用是显式检查，并非通过数组索引访问，因此告警所指的负索引访问在此上下文中是误报。 |
| 456 | git-2.44.0 | test_ctype_ispunct | cpp/overflow-buffer | 58 | FP | FP | 切片代码显示，循环变量 i 的范围是 0 到 255，且对 EOF 的调用有单独的条件检查，不会在数组索引操作中访问负索引 -1。 |
| 457 | git-2.44.0 | test_ctype_iscntrl | cpp/overflow-buffer | 57 | FP | FP | 切片代码显示循环索引 i 的范围是 0 到 255，且对 EOF 的调用是独立的检查，不会导致数组访问负索引 -1。 |
| 458 | git-2.44.0 | test_ctype_is_pathspec_magic | cpp/overflow-buffer | 53 | FP | FP | 切片代码显示，告警所在的宏 TEST_CTYPE_FUNC 内部循环索引 i 的范围是 0 到 255，且对 EOF 的调用是显式检查，不会导致对数组的负索引访问。 |
| 459 | git-2.44.0 | test_ctype_is_regex_special | cpp/overflow-buffer | 52 | FP | FP | 切片代码显示，宏 `TEST_CTYPE_FUNC` 中的循环索引 `i` 范围是 0 到 255，且对 `EOF` 的调用是显式检查 `func(EOF)`，并非通过数组索引访问。告警所指的负索引访问在切片逻辑中不存在。 |
| 460 | git-2.44.0 | test_ctype_is_glob_special | cpp/overflow-buffer | 51 | FP | FP | 切片代码显示，宏 `TEST_CTYPE_FUNC` 中的循环索引 `i` 范围是 0 到 255，并且对 `EOF` 的调用是显式检查，不会导致对数组的负索引访问。告警点 `TEST_CTYPE_FUNC(is_glob_speci... |
| 461 | git-2.44.0 | test_ctype_isalnum | cpp/overflow-buffer | 50 | FP | FP | 切片代码显示，循环索引 i 的范围是 0 到 255，且对 EOF 的调用是 `func(EOF)` 而非数组索引。宏定义中不存在对数组的负索引访问，告警可能是工具对宏展开的误解析。 |
| 462 | git-2.44.0 | test_ctype_isalpha | cpp/overflow-buffer | 49 | FP | FP | 切片代码显示，循环变量 i 的范围是 0 到 255，且对 EOF 的调用是独立的检查，不会导致数组以负索引访问。告警可能是工具对宏展开的误解析。 |
| 463 | git-2.44.0 | test_ctype_isspace | cpp/overflow-buffer | 48 | FP | FP | 切片代码显示，宏 TEST_CTYPE_FUNC 中的循环索引 i 范围是 0 到 255，不会产生负索引。对 func(EOF) 的调用是检查 EOF 常量（通常为 -1）作为函数参数，这是对函数功能的合法测试，并非对数组的负索引访问。 |
| 464 | git-2.44.0 | test_ctype_isdigit | cpp/overflow-buffer | 47 | FP | FP | 切片代码显示循环索引 i 的范围是 0 到 255，且对 EOF 的调用是 `func(EOF)` 而非数组索引。告警所指的负索引 -1 可能源于宏展开或工具对 EOF 值的误解，但在可见的切片逻辑中，不会发生对数组的负索引访问。 |
| 466 | git-2.44.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1647 | FP | FP | 切片代码显示，`buffer` 是通过 `xmallocz_gently(size)` 分配的，该函数分配 `size + 1` 字节的内存，而 `buffer[size] = '\0'` 写入的是该分配内存的最后一个字节，因此是安全... |
| 467 | git-2.44.0 | should_prune_worktree | cpp/invalid-pointer-deref | 791 | FP | FP | 切片代码显示，在写入 `path[len] = '\0';` 之前，存在一个 while 循环，当 `len` 大于 0 且末尾字符为换行符时会递减 `len`。这确保了写入位置 `len` 在循环后一定小于原始分配的缓冲区大小，因此... |
| 468 | curl-8_13_0 | <global> | cpp/invalid-pointer-deref | 89 | FP | FP | 切片代码显示，在写入 `newname[len]` 之前，已通过 `newlen = len + 13` 为 `newname` 分配了足够的内存，且 `newlen` 已进行溢出检查，确保 `len + 1` 在分配范围内，因此该写... |
| 469 | curl-8_15_0 | <global> | cpp/invalid-pointer-deref | 85 | FP | FP | 切片代码显示，在写入 `newname[len]` 之前，已经通过 `newlen = len + 13` 为 `newname` 分配了足够的空间（包括末尾的 '.' 和后续的数字），并且有 `newlen < len` 的溢出检查... |
| 471 | curl-8_9_1 | <global> | cpp/invalid-pointer-deref | 96 | FP | FP | 切片代码显示，在写入 `newname[len]` 之前，已经通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen = len + 13`，并且 `len` 是原始文件名长度，因此 `newname[len]... |
| 472 | curl-8_7_1 | Curl_splayremove | cpp/inconsistent-null-check | 270 | FP | FP | 在切片代码中，对 `Curl_splay` 的调用结果直接赋值给了变量 `x`，并且后续立即使用了 `x->larger`。然而，根据被调用函数 `Curl_splay` 的定义，当输入参数 `t` 不为空时，它保证返回一个非空指针（... |
| 473 | curl-8_7_1 | <global> | cpp/invalid-pointer-deref | 96 | FP | FP | 切片代码显示，在写入 `newname[len]` 之前，已通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen = len + 13`，且 `len` 为原始文件名长度，因此 `newname[len]` ... |
| 474 | curl-8_11_1 | <global> | cpp/invalid-pointer-deref | 91 | FP | FP | 切片代码显示，在写入 `newname[len]` 之前，已经通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen = len + 13`，确保了 `len` 索引处是分配缓冲区内的有效位置，不会发生越界写入。 |
| 475 | nginx-1.27.2 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 切片代码中包含明确的注释和上下文，表明数组已预分配了4个空元素，且当前nelts为0，因此ngx_array_push调用不会失败，无需进行空值检查。 |
| 476 | nginx-1.29.0 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3565 | FP | FP | 切片代码中包含明确的注释说明该数组有4个预分配的空元素，因此push操作不会失败，且后续代码逻辑不依赖该返回值进行空指针检查，符合上下文的安全保证。 |
| 477 | nginx-1.27.4 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3521 | FP | FP | 切片代码中包含明确的注释说明该数组有4个预分配的空元素，因此push操作不会失败，且后续代码逻辑不依赖该返回值进行空指针检查，符合上下文安全保证。 |
| 478 | nginx-1.25.4 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 切片代码中的注释明确指出数组有4个预分配的空元素，因此push操作不会失败，且后续代码逻辑不依赖该push的返回值进行空指针检查，这是设计上的保证而非疏忽。 |
| 479 | nginx-1.27.0 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 切片代码中包含明确的注释说明该数组有4个预分配的空元素，因此push操作不会失败，且后续代码逻辑不依赖该返回值进行空指针检查，符合上下文的安全保证。 |
| 480 | vim-9.1.0550 | <global> | cpp/redundant-null-check-simple | 3494 | FP | FP | 告警指向的代码行 `if (inc_opt != NULL && strstr((char *)inc_opt, "\\zs") != NULL)` 中，对 `inc_opt` 的判空检查是必要的，因为 `inc_opt` 可能来自 ... |
| 481 | vim-9.1.0550 | <global> | cpp/redundant-null-check-simple | 3576 | FP | FP | 切片代码中未显示存在冗余的空指针检查。告警消息指向的代码行（3576）不在提供的切片范围内，且切片内可见的逻辑（如对`regmatch.regprog`等指针的检查）是必要的，用于防止空指针解引用。 |
| 482 | vim-9.1.0550 | findmatchlimit | cpp/offset-use-before-range-check | 2522 | FP | FP | 切片代码显示变量'col'在循环条件`check_prevcol(linep, col, '\\', &col)`中被使用，但该函数内部会先对`col`执行减一操作并进行边界检查（`col >= 0`），因此'col'的使用发生在有效... |
| 483 | vim-9.1.0550 | common_function | cpp/inconsistent-null-check | 4856 | FP | FP | 切片代码显示，在调用vim_strsave后，变量'name'被传递给func_ref或vim_free，这些函数内部会处理NULL指针（如func_ref检查NULL，vim_free检查NULL）。因此，即使vim_strsave... |
| 485 | vim-9.1.0550 | get_isolated_shell_name | cpp/inconsistent-null-check | 2695 | FP | FP | 函数 `gettail` 已对空指针输入进行了检查并返回空字符串，因此传递给 `vim_strsave` 的参数不会是 NULL。`vim_strsave` 内部也检查了 `alloc` 的返回值，并在分配失败时返回 NULL，但调用... |
| 487 | vim-9.1.0550 | did_set_cryptmethod | cpp/inconsistent-null-check | 1766 | FP | FP | 切片代码显示，vim_strsave 的返回值被赋值给全局变量 p_cm，而 p_cm 是一个字符串选项指针。在后续代码中，p_cm 被用于 STRCMP 比较，如果其为 NULL，STRCMP 将导致崩溃。然而，在调用 vim_st... |
| 488 | vim-9.1.0550 | did_set_background | cpp/inconsistent-null-check | 1079 | FP | FP | 切片代码显示，vim_strsave的返回值被赋值给p_bg，而p_bg随后立即被传递给check_string_option函数。该函数明确检查指针是否为NULL，并在为NULL时将其设置为empty_option，这构成了有效的空... |
| 489 | vim-9.1.0550 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 切片代码显示，在调用 find_win_by_nr_or_id 后，立即使用 win_valid_any_tab 函数检查了返回的窗口指针的有效性，如果无效则回退到 curwin。这表明代码已包含对空指针的防护，因此告警为误报。 |
| 490 | vim-9.1.0550 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 告警指出的`regnext`调用未检查null，但切片代码显示`next`变量在后续使用前，其值`scan`已在循环开始处被检查是否为NULL（`if (got_int ｜｜ scan == NULL)`），且`regnext`函数内... |
| 491 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 切片代码显示，在调用regnode后，其返回值被立即用于条件判断（如`if (ret == NULL)`）或赋值，这表明代码逻辑已处理了潜在的NULL返回值。此外，告警点所在的循环内，后续代码会检查`reg_toolong`标志并在为... |
| 492 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 切片代码显示，对 `regnode` 的调用位于 `if (ret != JUST_CALC_SIZE)` 条件块内，而 `JUST_CALC_SIZE` 是一个特殊的哨兵值，用于指示仅计算大小而不实际分配节点。在此模式下，`regn... |
| 493 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在切片代码中，`regnext`的返回值被赋值给循环变量`br`，并在循环条件`br != lastnode`中使用。该条件隐含了对非空值的检查，因为`regnext`可能返回NULL，而NULL与`lastnode`的比较是有效的，... |
| 494 | vim-9.1.0550 | win_redr_custom | cpp/inconsistent-null-check | 1115 | FP | FP | 切片代码显示在调用vim_strsave后，其返回值被立即传递给build_stl_str_hl函数使用，随后通过vim_free(stl)释放，这表明代码逻辑正确处理了内存分配和释放，没有出现空指针解引用等安全问题。 |
| 495 | vim-9.1.0550 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 切片代码显示，在调用getroom后，函数get_wordnode的返回值n在#ifdef SPELL_PRINTTREE块中被检查是否为NULL，这表明代码对潜在的NULL返回值有处理逻辑。此外，getroom函数在内存分配失败时会... |
| 496 | vim-9.1.0550 | do_tag | cpp/inconsistent-null-check | 639 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续被立即赋值给 `tofree` 变量，而 `tofree` 在函数末尾通过 `vim_free(tofree)` 被安全释放。这表明代码逻辑已妥善处理了内存，不存... |
| 497 | vim-9.1.0550 | define_function | cpp/inconsistent-null-check | 5306 | FP | FP | 切片代码中，vim_strchr的返回值被用于条件判断（如if (vim_strchr(p, '(') != NULL)），这表明返回值被隐式检查是否为NULL（非NULL表示找到字符）。该用法符合上下文逻辑，并非未检查返回值。 |
| 498 | vim-9.1.0550 | is_duplicate_variable | cpp/inconsistent-null-check | 909 | FP | FP | 提供的切片代码中，函数 `is_duplicate_variable` 的函数体为空，未包含对 `vim_strnsave` 的调用。因此，告警所提及的未检查 `vim_strnsave` 返回值的代码不存在于当前上下文中，属于误报。 |
| 499 | vim-9.1.0550 | exec_instructions | cpp/inconsistent-null-check | 3257 | FP | FP | alloc_clear 返回的指针被直接赋值给 tv->vval.v_object，但切片代码中后续立即对该对象进行了初始化（设置 obj_class、递增引用计数、调用 object_created 等），这表明代码逻辑假设分配成功... |
| 500 | vim-9.1.0550 | barline_parse | cpp/inconsistent-null-check | 1122 | FP | FP | 切片代码显示，调用 `vim_strsave(s)` 的结果被直接赋值给 `value->bv_string`，但该值仅在 `value->bv_allocated` 为真时才会被后续释放，而此处 `bv_allocated` 被设置... |
| 501 | vim-9.1.0550 | ex_history | cpp/unsafe-strcat | 780 | FP | FP | 切片代码显示，在使用STRCAT前，已通过条件`vim_strsize(hist[i].hisstr) > (int)Columns - 10`检查了源字符串长度，若过长则调用trunc_string进行截断，否则才使用STRCAT。... |
| 502 | vim-9.1.0550 | helptags_one | cpp/unsafe-strcat | 971 | FP | FP | 切片代码中，STRCAT宏用于拼接已知的常量字符串“/**/*”和参数ext，其中ext是函数参数，其长度在调用上下文中是可控且有限的（如“.txt”等固定后缀）。NameBuff缓冲区大小未在切片中明确显示，但根据其在整个函数中的使... |
| 503 | vim-9.1.0550 | netbeans_keyname | cpp/unsafe-strcat | 2444 | FP | FP | 切片代码显示，`name` 指针要么指向静态字符串字面量（长度固定且已知），要么指向大小为2的本地数组 `namebuf`（已确保以NUL结尾）。`buf` 在首次使用前被初始化为空字符串，且所有 `strcat` 操作拼接的字符串长... |
| 504 | vim-9.1.0550 | set_init_default_backupskip | cpp/unsafe-strcat | 178 | FP | FP | 切片代码显示，在调用STRCAT前，已通过ga_grow(&ga, len) == OK检查并确保目标缓冲区有足够空间，且分配的item长度已包含NUL和分隔符，因此不存在缓冲区溢出风险。 |
| 505 | vim-9.1.0550 | do_put | cpp/unsafe-strcat | 2095 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息提示检查源缓冲区大小，但相关代码行（STRCAT宏）的上下文显示其目标缓冲区是通过alloc分配的新内存，大小计算（ml_get_len(lnum) - col + totlen + ... |
| 506 | vim-9.1.0550 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 切片代码显示，在调用STRCAT宏（即strcat）之前，目标缓冲区newword已通过vim_strncpy(newword, ae->ae_add, MAXWLEN - 1)或vim_strncpy(newword, word, ... |
| 514 | vim-9.1.0550 | buf_write | cpp/unbounded-write | 1208 | FP | FP | 切片代码中，STRCPY(IObuff, fname) 的目标缓冲区 IObuff 是一个固定大小的数组（由宏定义推断其大小为 IOSIZE），且 fname 是函数参数，其长度在调用前已通过路径处理逻辑得到控制。在切片可见的上下文中... |
| 515 | vim-9.1.0550 | buf_write | cpp/unbounded-write | 2566 | FP | FP | 切片代码中未发现对strcat的调用，告警提及的'call to strcat'在提供的上下文中不存在。该告警可能是基于不完整或错误的代码分析，因此判定为误报。 |
| 516 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2138 | FP | FP | 切片代码中未发现对 `STRCAT` 宏的直接调用，告警信息中提到的多个 `strcat` 调用在切片中不可见。切片中仅定义了 `STRCAT` 宏，但未显示其使用，因此无法确认存在缓冲区溢出风险。 |
| 518 | vim-9.1.0550 | globpath | cpp/unbounded-write | 3783 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已经通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度不会超过MAX... |
| 520 | vim-9.1.0550 | win_redr_status_matches | cpp/unbounded-write | 653 | FP | FP | 切片代码显示目标缓冲区 `buf` 的大小已根据 `Columns` 和 `MB_MAXBYTES` 安全分配，且循环条件 `(long)(clen + status_match_len(xp, SHOW_MATCH(i)) + 2)... |
| 530 | vim-9.1.0550 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过alloc(len)为目标缓冲区buf分配了精确计算的长度len，该长度已考虑了所有待拼接字符串（cmd, itmp, otmp等）的总长并预留了终止符空间。因此，strc... |
| 547 | vim-9.1.0550 | vim_rename | cpp/unbounded-write | 3839 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串长度，确保不会超过目标缓冲区`tempname`（大小为MAXPATHL + 1）的容量... |
| 552 | vim-9.1.0550 | concat_fnames | cpp/unbounded-write | 3126 | FP | FP | 切片代码显示，目标缓冲区 `dest` 的大小是通过 `alloc(STRLEN(fname1) + STRLEN(fname2) + 3)` 精确分配的，足以容纳两个源字符串、一个可选的分隔符以及终止符，因此 `STRCAT` 调用... |
| 553 | vim-9.1.0550 | uniquefy_paths | cpp/unbounded-write | 2362 | FP | FP | 切片代码显示，`file_pattern` 缓冲区的大小为 `len + 2`，其中 `len` 是输入 `pattern` 的长度。`STRCAT` 操作是在 `file_pattern[0]` 被设置为 `'*'` 后，将 `pa... |
| 558 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 801 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，明确进行了长度检查（STRLEN(search_ctx->ffsc_start_dir) + 1 < MAXPATHL），确保目标缓冲区file_path（大小为MAXPATHL）... |
| 559 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 815 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，存在明确的大小检查（STRLEN(file_path) + STRLEN(stackp->ffs_fix_path) + 1 < MAXPATHL），确保目标缓冲区不会溢出。 |
| 560 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 936 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，存在明确的长度检查（STRLEN(...) + 1 < MAXPATHL），确保目标缓冲区file_path（大小为MAXPATHL）不会溢出。因此，该告警是误报。 |
| 561 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 938 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区不会溢出。因此，该告警为误报。 |
| 562 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 1104 | FP | FP | 切片代码中所有STRCPY调用前都使用STRLEN进行了长度检查，确保目标缓冲区大小（MAXPATHL）足够，因此不存在缓冲区溢出风险。 |
| 563 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 1106 | FP | FP | 切片代码中，在调用STRCAT（即strcat）前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区不会溢出。因此，该告警为误报。 |
| 566 | vim-9.1.0550 | <global> | cpp/unbounded-write | 544 | FP | FP | 切片代码显示，STRCAT宏的目标缓冲区ff_expand_buffer是通过alloc(MAXPATHL)分配的，其大小固定为MAXPATHL。在调用STRCAT之前，代码通过STRCPY和add_pathsep操作，并计算了当前长... |
| 573 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2901 | FP | FP | 切片代码显示，`res_prolog->title` 和 `res_prolog->version` 是从受控的PostScript资源文件中解析出的固定字段，其长度在`prt_open_resource`函数中通过`vim_strn... |
| 576 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 切片代码显示 `res_cmap->title` 是从受控的 PostScript 资源文件中解析出的固定元数据，其长度在 `prt_open_resource` 函数中已被限制为不超过缓冲区大小，且没有外部输入直接写入该字段，因此 ... |
| 577 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 切片代码显示`res_cmap->title`和`res_cmap->version`是从受控的PostScript资源文件中解析出的固定字段，其长度在`prt_open_resource`函数中通过`vim_strncpy`进行了限... |
| 579 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2922 | FP | FP | 切片代码显示，`buffer` 数组大小为256字节，而 `res_encoding->title` 和 `res_encoding->version` 是从受控的PostScript资源文件中解析出的短字符串，其长度在解析时被限制（... |
| 583 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 987 | FP | FP | 目标缓冲区 `NameBuff` 在代码切片中未显示其大小，但根据其在整个项目中的典型用法（如 `MAXPATHL` 定义）和上下文（用于构建文件路径），它很可能是一个大小固定的缓冲区。告警点 `STRCAT(NameBuff, ta... |
| 585 | vim-9.1.0550 | highlight_set_startstop_termcode | cpp/unbounded-write | 1477 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，存在明确的长度检查 `if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`，确保拼接后的字符串不会超过目标缓冲区buf（大小为100）的容量，因此该... |
| 588 | vim-9.1.0550 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 切片代码显示，在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...）并分配了相应大小的内存（buf = alloc(amt)），确保了目标缓冲区足以容纳格式化后的字符串，因此不存在缓冲区... |
| 589 | vim-9.1.0550 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了足够的内存，因此不会发生缓冲区溢出。 |
| 593 | vim-9.1.0550 | ins_compl_infercase_gettext | cpp/unbounded-write | 658 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过条件`(p - IObuff) + 6 >= IOSIZE`检查了目标缓冲区IObuff的剩余空间，并且当空间不足时，会切换到使用动态增长的数组（gap），从而防止了缓冲... |
| 595 | vim-9.1.0550 | findswapname | cpp/unbounded-write | 4967 | FP | FP | STRCPY 的目标缓冲区 fname2 是通过 alloc(n + 2) 分配的，其中 n 是源字符串 fname 的长度。分配的大小比源字符串长度多 2，足以容纳源字符串和额外的字符修改，因此不会发生缓冲区溢出。 |
| 596 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2157 | FP | FP | 切片代码显示，目标缓冲区`s`的大小通过`alloc(STRLEN(f) + 1)`分配，其大小精确等于源字符串`f`的长度加1，因此`STRCPY(s, f)`不会发生缓冲区溢出。 |
| 608 | vim-9.1.0550 | add_to_showcmd | cpp/unbounded-write | 1760 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已计算了目标缓冲区showcmd_buf的当前长度和待追加字符串p的长度，并检查了溢出（overflow）。如果溢出大于0，会通过mch_memmove移动缓冲区内容以腾出空间，... |
| 615 | vim-9.1.0550 | option_value2string | cpp/unbounded-write | 8157 | FP | FP | 切片代码显示告警点位于`STRCPY(NameBuff, transchar((int)wc));`，但`NameBuff`是一个全局缓冲区，其大小未在切片中明确给出，且`transchar`函数返回的字符串长度有限（通常为可打印字符... |
| 624 | vim-9.1.0550 | regtilde | cpp/unbounded-write | 1925 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`tmpsublen > MAXCOL`对目标缓冲区大小`tmpsublen`进行了检查，并在超出限制时报错退出，这构成了有效的边界防护，防止了缓冲区溢出。 |
| 630 | vim-9.1.0550 | op_yank | cpp/unbounded-write | 1279 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过alloc函数为目标缓冲区pnew分配了足够的空间，其大小为两个源字符串长度之和加1，这确保了缓冲区不会溢出。 |
| 641 | vim-9.1.0550 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过动态内存分配确保目标缓冲区`buf`的大小（`buflen`）大于等于源字符串长度（`len`）加上`MAXWLEN + 2`，这提供了足够的空间，防止了缓冲区溢出。 |
| 642 | vim-9.1.0550 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过getroom函数为目标缓冲区sc分配了精确的长度（STRLEN(s) + 1），确保了目标缓冲区大小足以容纳源字符串s及其终止符，因此不会发生缓冲区溢出。 |
| 644 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 切片代码中，STRCAT操作的目标缓冲区p是通过getroom()分配的，其大小已根据items[0]和items[1]的长度精确计算并预留了额外空间，因此不会发生缓冲区溢出。 |
| 646 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 切片代码中，STRCAT的目标缓冲区p是通过getroom(spin, l, FALSE)动态分配的，其大小l已计算为所需字符串的总长度加分隔符，因此不会发生缓冲区溢出。 |
| 647 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 切片代码显示strcpy的目标缓冲区是动态分配的，其大小通过STRLEN(items[1]) + 2计算，确保有足够空间容纳源字符串和额外字符，因此不会发生缓冲区溢出。 |
| 649 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2748 | FP | FP | 切片代码中，sprintf的目标缓冲区`buf`大小为`MAXLINELEN`（定义为256），而源字符串`items[4]`来自受控的affix文件行解析，其长度受`MAXLINELEN`限制且已通过`vim_fgets`安全读取。... |
| 650 | vim-9.1.0550 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | 切片代码显示，STRCPY的目标缓冲区`sft->sft_word`是通过`alloc(offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1)`分配的，其大小精确等于源字符串`goo... |
| 651 | vim-9.1.0550 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY宏的目标缓冲区fword被定义为固定大小的数组char_u fword[MAXWLEN]，且切片代码中可见后续操作（如spell_casefold）会检查目标缓冲区长度，确保不会发生缓冲区溢出。 |
| 652 | vim-9.1.0550 | concat_str | cpp/unbounded-write | 768 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc为目标缓冲区分配了精确的足够空间（str1和str2的长度之和加1），因此不会发生缓冲区溢出。这是一个安全的字符串拼接实现。 |
| 665 | vim-9.1.0550 | exec_instructions | cpp/unbounded-write | 3487 | FP | FP | 切片代码中未发现任何对strcpy的调用，告警中提到的所有strcpy调用在提供的切片中均不存在。切片代码主要处理Vim脚本指令执行，未包含告警所指向的缓冲区溢出风险代码。 |
| 672 | vim-9.1.0550 | update_snapshot | cpp/invalid-pointer-deref | 2068 | FP | FP | 切片代码显示，在访问 p[pos.col + 1] 之前，存在对 width == 2 的条件检查，并且 len 是列数，pos.col 在循环中递增 width，确保了 pos.col + 1 不会超过 len-1 的边界。因此，该... |
| 695 | vim-9.1.1591 | netbeans_keyname | cpp/unsafe-strcat | 2449 | FP | FP | 切片代码显示，`name` 指针指向的字符串长度是已知且有限的（如 "F1"、"X" 或单个字符的 `namebuf`），且 `buf` 在首次使用前被初始化为空字符串。虽然未明确检查 `buf` 的大小，但根据上下文，拼接的字符串总... |
| 765 | vim-9.1.1591 | cs_make_vim_style_matches | cpp/unbounded-write | 1639 | FP | FP | 切片代码显示，在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了该大小的内存（buf = alloc(amt)），因此写入不会溢出目标缓冲区。 |
| 766 | vim-9.1.1591 | cs_make_vim_style_matches | cpp/unbounded-write | 1647 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了该大小的内存（buf = alloc(amt)），确保了目标缓冲区足以容纳格式化后的字符串，因此不存在缓冲区溢出风险。 |
| 846 | vim-9.1.1040 | <global> | cpp/redundant-null-check-simple | 3502 | FP | FP | 告警指出对 `inc_opt` 的空指针检查是冗余的，因为该变量在检查前已被解引用。切片代码显示 `inc_opt` 在检查前通过条件赋值被初始化，且赋值来源（`curbuf->b_p_inc` 或 `p_inc`）在切片中未显示为空... |
| 847 | vim-9.1.1040 | <global> | cpp/redundant-null-check-simple | 3584 | FP | FP | 告警指出空指针检查是冗余的，因为该值在任何情况下都会被解引用。但在切片代码中，指针 `inc_opt` 在解引用前已通过 `if (*inc_opt != NUL)` 进行了非空检查，且 `inc_opt` 被赋值为 `(*curbu... |
| 848 | vim-9.1.1040 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | FP | FP | 切片代码显示，在警告点使用 `pos.col` 之前，存在对 `pos.col` 值的显式检查和调整（例如 `if (pos.col > 0)`），并且 `pos.col` 的修改逻辑（如 `--pos.col` 或 `pos.col... |
| 849 | vim-9.1.1040 | common_function | cpp/inconsistent-null-check | 5061 | FP | FP | 切片代码显示，在调用 `vim_strsave` 后，`name` 变量被传递给 `func_ref` 或 `vim_free` 等函数，这些函数内部会处理 NULL 指针（如 `func_ref` 会检查 `name == NULL... |
| 851 | vim-9.1.1040 | get_isolated_shell_name | cpp/inconsistent-null-check | 2710 | FP | FP | 函数 `vim_strsave` 内部已对 `alloc` 的返回值进行了检查，若分配失败则返回 NULL，调用者 `get_isolated_shell_name` 直接返回该指针，由上层调用者负责处理 NULL 情况，这符合 Vi... |
| 853 | vim-9.1.1040 | did_set_cryptmethod | cpp/inconsistent-null-check | 1832 | FP | FP | 切片代码显示，vim_strsave的返回值被直接赋值给全局变量p_cm，而p_cm是一个字符串选项指针，后续使用前会通过free_string_option或empty_option等机制处理，且该函数在内存分配失败时返回NULL，... |
| 854 | vim-9.1.1040 | did_set_background | cpp/inconsistent-null-check | 1083 | FP | FP | 切片代码显示，在调用 vim_strsave 后，其返回值 p_bg 立即被传递给 check_string_option 函数，该函数会检查指针是否为 NULL 并将其设置为空字符串常量 empty_option，从而防止了空指针解引用。 |
| 855 | vim-9.1.1040 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 切片代码显示，在调用 `find_win_by_nr_or_id` 后，其返回值 `wp->w_popup_prop_win` 立即被 `win_valid_any_tab` 函数检查。如果检查失败，该值会被重置为 `curwin`，... |
| 856 | vim-9.1.1040 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 告警指出对regnext的调用结果未检查null，但切片代码显示该结果被赋值给局部变量'next'，并在后续循环中作为'scan'使用，而'scan'在循环开始处有明确的'if (got_int ｜｜ scan == NULL)'空值... |
| 857 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 切片代码显示，对 `regnode` 的调用结果 `br` 被立即用于条件判断 `if (ret == NULL)` 和后续的 `regtail` 操作，这些操作在 `br` 为 NULL 时不会导致解引用空指针。代码逻辑在切片可见范... |
| 858 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 切片代码显示，`regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `JUST_CALC_SIZE`，而在告警点 `br = regnode(NOTHING);` 后... |
| 859 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 切片代码显示，在调用`regnext(br)`之前，已经检查了`reg_toolong`标志，并且`regnext`函数内部也会检查`reg_toolong`并返回NULL。这表明代码逻辑已通过全局标志处理了错误情况，无需额外的空指针检查。 |
| 860 | vim-9.1.1040 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 切片代码显示，在调用getroom后，函数get_wordnode的返回值n在#ifdef SPELL_PRINTTREE块中被检查是否为NULL，这表明代码对可能的空指针进行了处理。此外，getroom函数在内存分配失败时会返回NU... |
| 861 | vim-9.1.1040 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续被赋值给 `tofree`，而 `tofree` 在函数末尾通过 `vim_free(tofree)` 被释放。这表明代码逻辑已处理了内存分配失败的情况，通过 `... |
| 862 | vim-9.1.1040 | define_function | cpp/inconsistent-null-check | 5403 | FP | FP | 切片代码中，对 `vim_strchr` 的调用结果被用于条件判断（`vim_strchr(p, '(') != NULL`），这等同于检查了返回值是否为 null，因此该告警是误报。 |
| 863 | vim-9.1.1040 | is_duplicate_variable | cpp/inconsistent-null-check | 991 | FP | FP | 提供的切片代码中，函数 `is_duplicate_variable` 的函数体为空，未包含对 `vim_strnsave` 的调用，因此无法确认存在未检查返回值的缺陷。基于切片信息，告警不成立。 |
| 864 | vim-9.1.1040 | exec_instructions | cpp/inconsistent-null-check | 3383 | FP | FP | alloc_clear() 返回的指针被直接赋值给 tv->vval.v_object，后续代码立即访问该对象的成员（如 obj_class、obj_refcount），这隐含了指针非空的假设。切片中未显示对 alloc_clear(... |
| 865 | vim-9.1.1040 | barline_parse | cpp/inconsistent-null-check | 1153 | FP | FP | 切片代码显示，调用 vim_strnsave 的结果直接赋值给局部变量 s，而 s 随后被赋值给 value->bv_string。该赋值操作发生在条件分支内，且 value->bv_allocated 被设置为 allocated ... |
| 866 | vim-9.1.1040 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | STRCAT 宏直接包装了不安全的 strcat，但切片代码显示目标缓冲区 NameBuff 在拼接前已通过 STRCPY 复制了已知长度的目录路径，且拼接的字符串是固定模式（"/**/*" 和文件扩展名），这些字符串长度固定且可控，... |
| 867 | vim-9.1.1040 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 切片代码显示，`name` 指针指向的字符串长度最大为3（如"F12"）或来自固定字符数组 `namebuf`（长度为2），且 `buf` 在每次 `strcat` 前已初始化为空字符串。虽然未明确检查 `buf` 的大小，但拼接的源... |
| 868 | vim-9.1.1040 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 切片代码显示，在调用STRCAT宏（即strcat）之前，目标缓冲区newword已通过vim_strncpy(newword, ae->ae_add, MAXWLEN - 1)进行初始化，该函数确保写入不超过MAXWLEN-1个字符... |
| 876 | vim-9.1.1040 | buf_write | cpp/unbounded-write | 2566 | FP | FP | 切片代码中未发现对strcat的直接调用，告警提及的'call to strcat'在提供的切片上下文中不可见。该告警可能基于不完整或过时的分析，或者指向的代码行不在切片范围内。基于切片内可见的证据，无法确认存在缓冲区溢出漏洞。 |
| 879 | vim-9.1.1040 | globpath | cpp/unbounded-write | 3809 | FP | FP | 切片代码显示在调用STRCAT前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区`buf`的剩余空间，确保拼接后不会超过最大长度MAXPATHL，因此不存在缓... |
| 884 | vim-9.1.1040 | ex_diffpatch | cpp/unbounded-write | 1363 | FP | FP | 告警针对的 STRCPY 调用目标缓冲区 'buf' 已通过 alloc(buflen) 分配，且 buflen 已根据源字符串长度计算并预留了额外空间，确保不会发生缓冲区溢出。 |
| 886 | vim-9.1.1040 | set_var_const | cpp/unbounded-write | 4184 | FP | FP | STRCPY宏的目标缓冲区di->di_key的大小是动态分配的，大小为STRLEN(varname) + 1，与源字符串长度完全匹配，因此不会发生缓冲区溢出。 |
| 888 | vim-9.1.1040 | ex_substitute | cpp/unbounded-write | 4883 | FP | FP | 切片代码中未发现对strcat的直接调用，告警提及的strcat可能由宏STRCAT实现，但切片内STRCAT的使用（如STRCAT(new_start, sub_firstline + copycol)）其目标缓冲区new_star... |
| 890 | vim-9.1.1040 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过alloc(len)为目标缓冲区buf分配了精确计算的长度len，且后续的vim_snprintf和STRCAT操作均在分配的缓冲区长度len范围内进行，因此不存在缓冲区溢... |
| 905 | vim-9.1.1040 | vim_rename | cpp/unbounded-write | 3858 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串`from`的长度，确保其不会超过目标缓冲区`tempname`（大小为MAXPATH... |
| 909 | vim-9.1.1040 | concat_fnames | cpp/unbounded-write | 3127 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，这确保了缓冲区大小足以容纳复制的内容，防止了缓冲区溢出。 |
| 910 | vim-9.1.1040 | concat_fnames | cpp/unbounded-write | 3130 | FP | FP | 切片代码显示，目标缓冲区 `dest` 的大小是通过 `alloc(STRLEN(fname1) + STRLEN(fname2) + 3)` 精确分配的，足以容纳两个源字符串、一个可选的分隔符以及终止空字符。因此，后续的 `STRC... |
| 916 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 805 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，均存在明确的长度检查（如`STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区`file_path`（大小为MAXPATHL）不会溢出。因此，该告警是误报。 |
| 917 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 819 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，明确进行了长度检查（STRLEN(file_path) + STRLEN(stackp->ffs_fix_path) + 1 < MAXPATHL），确保目标缓冲区不会溢出。 |
| 918 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 940 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，存在明确的大小检查（STRLEN(...) + 1 < MAXPATHL），确保目标缓冲区不会溢出。因此，该告警是误报。 |
| 919 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 942 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区不会溢出。因此，该告警是误报。 |
| 920 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 1110 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，均使用STRLEN对源字符串和目标缓冲区大小（MAXPATHL）进行了明确的长度检查，确保不会发生缓冲区溢出。 |
| 921 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 1112 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，均存在明确的长度检查（例如使用STRLEN计算并比较MAXPATHL），确保目标缓冲区不会溢出。这些防护机制使得告警的缓冲区溢出风险在实际执行路径中不会发生。 |
| 935 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 切片代码显示`buffer`是大小为256的局部数组，而`STRCAT`操作拼接的是已知的、从资源文件解析出的`title`和`version`字符串，这些字符串长度在`prt_open_resource`中通过`vim_strncp... |
| 940 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 975 | FP | FP | 切片代码中，STRCAT 宏操作的目标缓冲区 NameBuff 在之前的代码中已通过 STRCPY 被初始化为 dir 参数，其大小未明确限制。然而，dir 和 ext 参数是函数内部可控的常量字符串（如 ".txt"），并非来自不可... |
| 941 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 991 | FP | FP | STRCAT 宏用于拼接目录路径和文件名，目标缓冲区 NameBuff 在代码中未显示其大小，但根据上下文（如 MAXPATHL 的使用）和 Vim 的编码规范，它很可能是一个足够大的固定大小缓冲区（如 MAXPATHL），用于存储文... |
| 943 | vim-9.1.1040 | highlight_set_startstop_termcode | cpp/unbounded-write | 1481 | FP | FP | 切片代码中，在调用STRCAT（即strcat）前，已通过条件`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了目标缓冲区buf（大小为100字节）的剩余空间，确保拼接后不会发生溢出。该防护机... |
| 946 | vim-9.1.1040 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 切片代码中，`amt` 已通过精确计算所有输入字符串的长度总和并加上固定分隔符的长度来分配缓冲区，`sprintf` 写入的格式化字符串长度与计算值完全匹配，不存在缓冲区溢出的风险。 |
| 953 | vim-9.1.1040 | findswapname | cpp/unbounded-write | 4967 | FP | FP | STRCPY的目标缓冲区fname2是通过alloc(n + 2)分配的，其中n是源字符串fname的长度，分配的大小比源字符串长度多2个字节，确保了足够的空间，因此不会发生缓冲区溢出。 |
| 958 | vim-9.1.1040 | str2specialbuf | cpp/unbounded-write | 2017 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保拼接后不会超过其长度`len`，因此不存在... |
| 962 | vim-9.1.1040 | call_shell | cpp/unbounded-write | 1877 | FP | FP | 切片代码显示，目标缓冲区 `ncmd` 的大小通过 `alloc(STRLEN(ecmd) + STRLEN(p_sxq) * 2 + 1)` 精确计算并分配，足以容纳后续 `STRCAT` 操作拼接的字符串，因此不存在缓冲区溢出的风险。 |
| 966 | vim-9.1.1040 | add_to_showcmd | cpp/unbounded-write | 1763 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已计算了目标缓冲区showcmd_buf的当前长度和待追加字符串p的长度，并检查了溢出（overflow）。如果溢出，会通过mch_memmove移动缓冲区内容以腾出空间，从而防... |
| 973 | vim-9.1.1040 | option_value2string | cpp/unbounded-write | 8326 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区NameBuff是一个全局缓冲区，其大小未在切片中明确给出，但调用get_special_key_name和transchar等函数返回的字符串长度是受控的（如MAX_KEY_NAME_LEN），... |
| 999 | vim-9.1.1040 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已为目标缓冲区`buf`分配了足够的内存（`buflen = len + MAXWLEN + 2`），且分配大小基于源字符串`line`的长度计算，确保了缓冲区大小足以容纳源字符... |
| 1000 | vim-9.1.1040 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 切片代码显示，目标缓冲区 `sc` 的大小通过 `getroom(spin, STRLEN(s) + 1, FALSE)` 精确分配，其长度等于源字符串 `s` 的长度加 1，因此 `strcpy` 操作不会导致缓冲区溢出。 |
| 1001 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 切片代码显示，`STRCAT` 的目标缓冲区 `p` 是通过 `getroom` 函数分配的，其大小已根据源字符串长度精确计算并预留了足够空间，因此不存在缓冲区溢出的风险。 |
| 1002 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 切片代码显示告警点位于处理拼写信息（如NAME、VERSION等）的代码块中，其中STRCAT操作的目标缓冲区p是通过getroom()分配的内存，其大小已根据源字符串长度精确计算（spin->si_info长度 + items[0]... |
| 1004 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 切片代码中，STRCAT的目标缓冲区p是通过getroom(spin, l, FALSE)动态分配的，其大小l已计算为所需字符串的总长度加分隔符，因此不会发生缓冲区溢出。 |
| 1008 | vim-9.1.1040 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | STRCPY的目标缓冲区sft->sft_word是通过alloc动态分配的，其大小为offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1，与源字符串goodword的长度完全匹配，... |
| 1010 | vim-9.1.1040 | concat_str | cpp/unbounded-write | 811 | FP | FP | 切片代码显示，目标缓冲区 `dest` 的大小是通过 `alloc(l + ... + 1)` 精确计算的，其中长度 `l` 和 `str2` 的长度均使用 `STRLEN`（即 `strlen`）获取，并预留了终止符空间。`STRC... |
| 1015 | vim-9.1.1040 | show_one_termcode | cpp/unbounded-write | 7059 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，目标缓冲区IObuff的大小为5，源字符串p来自get_special_key_name函数，该函数内部使用固定大小的静态缓冲区string（MAX_KEY_NAME_LEN +... |
| 1023 | vim-9.1.1040 | exec_instructions | cpp/unbounded-write | 3613 | FP | FP | 切片代码中未发现任何对strcpy的调用，告警中提到的所有strcpy调用在切片中均不可见。切片主要展示的是exec_instructions函数中的指令分发逻辑，没有直接使用strcpy。因此，基于切片内可见的证据，该告警为误报。 |
| 1029 | vim-9.1.1040 | ExpandBufnames | cpp/invalid-pointer-deref | 2939 | FP | FP | 切片代码显示，在告警行 `(*file)[count++] = p;` 执行前，`*file` 已在循环第一轮通过 `*file = ALLOC_MULT(char_u *, count);` 分配了足够空间，且 `count` 在循... |
| 1030 | vim-9.1.1040 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | FP | 切片代码显示，在访问 `p[pos.col + 1]` 之前，存在 `if (width == 2)` 的条件检查，并且 `width` 的值来源于 `cell.width`，该值由 `vterm_screen_get_cell` 函... |
| 1031 | vim-9.1.1330 | <global> | cpp/redundant-null-check-simple | 3508 | FP | FP | 告警指出的空指针检查冗余，但切片代码显示在检查前，`inc_opt` 指针已通过条件 `if (*inc_opt != NUL)` 确保其指向的字符串非空，因此 `strstr` 调用是安全的，空指针检查是防御性编程而非逻辑错误。 |
| 1032 | vim-9.1.1330 | <global> | cpp/redundant-null-check-simple | 3590 | FP | FP | 切片代码中未显示存在对空指针的解引用，告警指出的冗余空检查在切片上下文中不可见。该告警可能是基于工具对代码模式的误判，切片内没有证据表明存在解引用空指针的风险。 |
| 1033 | vim-9.1.1330 | findmatchlimit | cpp/offset-use-before-range-check | 2529 | FP | FP | 切片代码显示变量'col'在循环条件`check_prevcol(linep, col, '\\', &col)`中被使用，但该函数内部会先对`col`执行`--col;`操作并进行边界检查（`col >= 0`），因此'col'的使... |
| 1034 | vim-9.1.1330 | common_function | cpp/inconsistent-null-check | 5228 | FP | FP | 切片代码显示，在调用 vim_strsave(s) 后，返回的指针 'name' 在后续代码中被传递给 vim_free(name) 或 func_ref(name) 等函数，这些函数内部会处理 NULL 指针（如 vim_free ... |
| 1036 | vim-9.1.1330 | get_isolated_shell_name | cpp/inconsistent-null-check | 2710 | FP | FP | 函数 `vim_strsave` 内部已对 `alloc` 的返回值进行了检查，若分配失败则返回 NULL，调用方 `get_isolated_shell_name` 直接返回该指针，由上层调用者负责处理 NULL 情况，切片中未见必... |
| 1038 | vim-9.1.1330 | did_set_cryptmethod | cpp/inconsistent-null-check | 1894 | FP | FP | 切片代码显示，`vim_strsave` 的返回值被赋值给全局变量 `p_cm`，该变量后续在 `ml_set_crypt_key` 等函数中被使用，但未直接解引用。结合 `vim_strsave` 内部已调用 `alloc` 并检查... |
| 1039 | vim-9.1.1330 | did_set_background | cpp/inconsistent-null-check | 1086 | FP | FP | 切片代码显示，在调用vim_strsave后，其返回值p_bg立即被传递给check_string_option函数，该函数会检查指针是否为NULL并将其设置为空字符串常量empty_option，这提供了对空指针的防护。 |
| 1040 | vim-9.1.1330 | apply_move_options | cpp/inconsistent-null-check | 531 | FP | FP | 切片代码显示，在调用 `find_win_by_nr_or_id` 后，其返回值 `wp->w_popup_prop_win` 立即被 `win_valid_any_tab` 函数检查。如果检查失败，该值会被重置为 `curwin`，... |
| 1041 | vim-9.1.1330 | <global> | cpp/inconsistent-null-check | 3339 | FP | FP | 切片代码显示`regnext`函数内部已包含对NULL返回值的检查（`if (offset == 0) return NULL;`），且调用点`next = regnext(scan);`的结果`next`在后续循环中作为`scan`... |
| 1042 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 切片代码显示，对 regnode 的调用结果（br）被立即用于条件判断（if (ret == NULL)），其值被直接赋值给 ret 或传递给 regtail，并未被解引用或用于可能导致空指针解引用的操作。在给定的上下文中，未检查返回... |
| 1043 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 切片代码显示，对 `regnode` 的调用位于 `if (ret != JUST_CALC_SIZE)` 条件块内，该条件块仅在非计算模式下执行。在计算模式下（`ret == JUST_CALC_SIZE`），`regnode` 函... |
| 1044 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 切片代码显示，在调用 `regnext(br)` 的循环中，`br` 变量来自 `ret` 或 `OPERAND(br)`，这些值均来自 `regnode` 函数，该函数在非 `JUST_CALC_SIZE` 模式下返回非空指针。此外... |
| 1045 | vim-9.1.1330 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 切片代码显示，在调用 getroom 后，函数返回的指针 n 在宏 SPELL_PRINTTREE 下被检查是否为 NULL，并且函数最终返回 n。更重要的是，被调用的 getroom 函数在内存分配失败时会返回 NULL，而调用者 ... |
| 1046 | vim-9.1.1330 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续被 `vim_free(tofree)` 释放，而 `tofree` 被赋值为 `name`，这表明代码已通过 `vim_free` 处理了可能的空指针，符合 V... |
| 1047 | vim-9.1.1330 | define_function | cpp/inconsistent-null-check | 5486 | FP | FP | 切片代码中，对 vim_strchr 的调用结果用于条件判断（如 `if (vim_strchr(p, '(') != NULL)`），虽然没有显式地将返回值赋给变量再检查是否为 NULL，但直接与 NULL 比较的用法在逻辑上等同于... |
| 1048 | vim-9.1.1330 | is_duplicate_variable | cpp/inconsistent-null-check | 1011 | FP | FP | 切片代码中函数 `is_duplicate_variable` 为空实现，未调用 `vim_strnsave` 或任何可能返回空指针的函数，因此不存在未检查空指针的问题。告警基于统计模式，但当前切片中无相关代码。 |
| 1049 | vim-9.1.1330 | exec_instructions | cpp/inconsistent-null-check | 3666 | FP | FP | 代码中alloc_clear的返回值被直接赋值给tv->vval.v_object->obj_class，但切片中可见后续立即对obj_class进行了递增引用计数操作，且存在object_created等初始化函数，表明对象创建流程... |
| 1050 | vim-9.1.1330 | barline_parse | cpp/inconsistent-null-check | 1153 | FP | FP | 切片代码显示，调用 vim_strnsave 的结果被赋值给局部变量 s，而 s 随后被赋值给 value->bv_string。该赋值操作发生在条件分支内，该分支仅在字符串未分配且已分配标志为真且未转换时才执行。该分支的逻辑表明，即... |
| 1051 | vim-9.1.1330 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | STRCAT宏被用于拼接已知的、受控的字符串常量（'/**/*'和ext参数），ext参数来自函数调用者，在切片中未见其被外部输入污染。拼接的目标缓冲区NameBuff在切片中未显示其大小，但根据上下文（用于构建文件路径）和后续安全使... |
| 1052 | vim-9.1.1330 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 切片代码显示，`name` 指针指向的字符串长度是严格受限的（如 "F1"、"X" 或单字符数组 `namebuf`），且 `buf` 初始化为空字符串，多次 `strcat` 拼接的字符串总长度很短，缓冲区溢出的风险极低。 |
| 1053 | vim-9.1.1330 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 切片代码显示，在使用STRCAT拼接前，目标缓冲区newword已通过vim_strncpy(newword, ae->ae_add, MAXWLEN - 1)或vim_strncpy(newword, word, MAXWLEN -... |
| 1059 | vim-9.1.1330 | maketitle | cpp/unbounded-write | 4230 | FP | FP | 切片代码显示STRCPY宏的目标缓冲区`buf`大小为IOSIZE，而源字符串`name`在复制前经过了长度检查（`namelen > 100`时被截断），且后续的`trans_characters`函数会确保缓冲区不溢出，因此该st... |
| 1061 | vim-9.1.1330 | buf_write | cpp/unbounded-write | 2568 | FP | FP | 切片代码中未发现对strcat函数的直接调用，告警提及的'call to strcat'在提供的代码片段中不可见，因此无法确认存在缓冲区溢出漏洞。 |
| 1062 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2144 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中不可见。切片主要展示的是open_line函数中的字符串处理和内存管理逻辑，没有证据表明存在缓冲区溢出漏洞。 |
| 1064 | vim-9.1.1330 | globpath | cpp/unbounded-write | 3864 | FP | FP | 切片代码中，在调用STRCAT(buf, file)之前，存在明确的缓冲区长度检查`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`，这确保了拼接后的字符串不会超过目标缓冲区`buf`的大... |
| 1069 | vim-9.1.1330 | ex_diffpatch | cpp/unbounded-write | 1390 | FP | FP | 告警针对的STRCPY操作目标缓冲区'buf'已通过alloc(buflen)分配了足够大小，其中buflen由STRLEN(tmp_orig) + STRLEN(esc_name) + STRLEN(tmp_new) + 16计算得... |
| 1073 | vim-9.1.1330 | ex_substitute | cpp/unbounded-write | 4883 | FP | FP | 切片代码中未发现对strcat函数的直接调用，告警中提到的多个strcat调用在提供的代码片段中不可见。切片主要展示的是ex_substitute函数的逻辑，涉及字符串处理和正则表达式替换，但没有显示可能导致缓冲区溢出的不安全strc... |
| 1074 | vim-9.1.1330 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区分配了精确计算的长度len，该长度足以容纳源字符串cmd及其所需的额外字符和终止符，因此不会发生缓冲区溢出。 |
| 1075 | vim-9.1.1330 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过alloc(len)分配了缓冲区，且len的计算考虑了所有待拼接字符串的长度和终止符，缓冲区大小足够，因此不会发生溢出。 |
| 1083 | vim-9.1.1330 | discard_exception | cpp/unbounded-write | 646 | FP | FP | 切片代码显示，目标缓冲区IObuff是全局缓冲区，其大小在别处定义，但源字符串saved_IObuff是之前通过vim_strsave(IObuff)保存的副本，长度与原始IObuff相同。因此，STRCPY(IObuff, save... |
| 1090 | vim-9.1.1330 | vim_rename | cpp/unbounded-write | 3861 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串`from`的长度，确保其不会导致目标缓冲区`tempname`（大小为MAXPATH... |
| 1093 | vim-9.1.1330 | concat_fnames | cpp/unbounded-write | 3134 | FP | FP | 切片代码显示，目标缓冲区 `dest` 的大小通过 `alloc(STRLEN(fname1) + STRLEN(fname2) + 3)` 精确分配，足以容纳源字符串 `fname1` 和 `fname2` 以及额外的分隔符和终止符... |
| 1094 | vim-9.1.1330 | concat_fnames | cpp/unbounded-write | 3137 | FP | FP | 切片代码显示，目标缓冲区 `dest` 的大小通过 `alloc(STRLEN(fname1) + STRLEN(fname2) + 3)` 精确分配，足以容纳两个源字符串、一个可能的路径分隔符以及终止符，因此 `STRCAT` 调用... |
| 1104 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 切片代码显示`res_cidfont->title`和`res_cidfont->version`来自受控的PostScript资源文件，其内容在`prt_open_resource`中经过严格解析和长度限制，缓冲区`buffer`大... |
| 1107 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2920 | FP | FP | 告警点 STRCPY(buffer, res_encoding->title) 的目标缓冲区 buffer 在函数开头已定义为 char buffer[256]，而源数据 res_encoding->title 来自受控的资源文件，其... |
| 1110 | vim-9.1.1330 | do_helptags | cpp/unbounded-write | 1210 | FP | FP | 告警指向的 STRCPY 宏用于复制已知的目录路径参数 `dirname`，该参数来自函数内部调用，并非直接来自不可信的外部输入。在切片代码中，`dirname` 在后续使用前经过了 `add_pathsep` 处理，但未发现其长度超... |
| 1111 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 975 | FP | FP | 切片代码显示，STRCAT 宏操作的目标缓冲区 NameBuff 在多次拼接前已通过 STRCPY 初始化，且其大小 MAXPATHL 在上下文中被用于格式化输出，表明它是一个具有固定大小的缓冲区。告警点拼接的字符串由固定字符串和参数... |
| 1112 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 991 | FP | FP | 切片代码显示目标缓冲区 `NameBuff` 在拼接前已通过 `STRCPY(NameBuff, dir); add_pathsep(NameBuff);` 初始化，且 `dir` 和 `tagfname` 均为函数参数，其长度在切片... |
| 1114 | vim-9.1.1330 | highlight_set_startstop_termcode | cpp/unbounded-write | 1485 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，存在明确的长度检查 `if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`，确保拼接后的字符串不会超过目标缓冲区buf（大小为100）的容量，因此该... |
| 1122 | vim-9.1.1330 | ins_compl_infercase_gettext | cpp/unbounded-write | 688 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过条件`(p - IObuff) + 6 >= IOSIZE`确保了目标缓冲区`IObuff`有足够的剩余空间（至少6字节），并且紧接着的`*p = NUL;`操作表明源字... |
| 1124 | vim-9.1.1330 | findswapname | cpp/unbounded-write | 4967 | FP | FP | 切片代码显示，STRCPY的目标缓冲区fname2是通过alloc(n + 2)分配的，其中n是源字符串fname的长度，分配的大小比源字符串长度多2，确保了足够的空间。因此，该strcpy调用不会导致缓冲区溢出。 |
| 1128 | vim-9.1.1330 | msg_show_console_dialog | cpp/unbounded-write | 4502 | FP | FP | 切片代码显示，目标缓冲区 `confirm_msg` 的长度 `len` 已通过计算 `STRLEN(message)`、`STRLEN(buttons)` 等字符串长度并加上固定开销来精确分配，`STRCPY` 操作的目标缓冲区大小... |
| 1131 | vim-9.1.1330 | may_trigger_modechanged | cpp/unbounded-write | 2836 | FP | FP | STRCPY的目标缓冲区last_mode和源缓冲区curr_mode大小均为MODE_MAX_LENGTH，且get_mode函数确保curr_mode不会溢出其缓冲区，因此该复制操作是安全的。 |
| 1136 | vim-9.1.1330 | add_to_showcmd | cpp/unbounded-write | 1764 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已计算了现有缓冲区长度和待追加字符串长度，并检查了溢出情况（overflow > 0）。当检测到溢出时，会通过mch_memmove移动缓冲区内容以腾出空间，从而防止缓冲区溢出。 |
| 1142 | vim-9.1.1330 | option_value2string | cpp/unbounded-write | 8372 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区NameBuff是一个全局缓冲区，其大小未在切片中明确给出，但调用get_special_key_name返回的字符串来自内部静态缓冲区string，其大小被定义为MAX_KEY_NAME_LE... |
| 1143 | vim-9.1.1330 | option_value2string | cpp/unbounded-write | 8374 | FP | FP | 切片代码显示，告警点所在的 `STRCPY` 宏调用位于 `option_value2string` 函数中，其源数据 `transchar((int)wc)` 或 `get_special_key_name((int)wc, 0)`... |
| 1147 | vim-9.1.1330 | qf_store_title | cpp/unbounded-write | 1940 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已使用STRLEN计算了源字符串长度，并分配了长度+2的内存空间，确保了目标缓冲区足够大，因此不存在缓冲区溢出风险。 |
| 1162 | vim-9.1.1330 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，数据流经过了allcap_copy或onecap_copy函数处理，这些函数内部包含对目标缓冲区wcopy（即cword）的边界检查（如与MAXWLEN比较），确保不会发生溢出。... |
| 1167 | vim-9.1.1330 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过`buflen < len + MAXWLEN + 2`的判断为`buf`分配了足够大的内存（`buflen = len + MAXWLEN + 2`），且`buf`的大小... |
| 1168 | vim-9.1.1330 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过getroom函数为目标缓冲区sc分配了精确的长度（STRLEN(s) + 1），确保了缓冲区大小足以容纳源字符串s及其终止符，因此不存在缓冲区溢出的风险。 |
| 1169 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 切片代码显示告警点位于处理拼写信息（如NAME、VERSION等）的代码块中，其中STRCAT操作的目标缓冲区p是通过getroom()分配的内存，其大小已根据源字符串长度精确计算（spin->si_info长度 + items[0]... |
| 1170 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 切片代码显示，strcat操作的目标缓冲区p是通过getroom函数分配的，其大小已根据源字符串长度计算并预留了足够空间（包括分隔符和空字符），因此不会发生缓冲区溢出。 |
| 1172 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 切片代码显示，`STRCAT` 的目标缓冲区 `p` 是通过 `getroom(spin, l, FALSE)` 动态分配的，其大小 `l` 已计算为 `compflags` 和 `items[1]` 的长度之和加分隔符，因此缓冲区大... |
| 1173 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 切片代码显示，strcpy的目标缓冲区`p`是通过`getroom(spin, STRLEN(items[1]) + 2, FALSE)`动态分配的，其大小等于源字符串长度加2，足以容纳源字符串和追加的'+'字符，因此不会发生缓冲区溢出。 |
| 1176 | vim-9.1.1330 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | 切片代码中，STRCPY的目标缓冲区`sft->sft_word`的大小通过`alloc(offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1)`动态分配，其大小精确等于源字符串`g... |
| 1177 | vim-9.1.1330 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY宏的目标缓冲区fword大小为MAXWLEN，源字符串su->su_fbadword是内部生成的拼写建议候选词，其长度受相同MAXWLEN常量限制，且在切片中未见外部未受控输入直接复制到该缓冲区，因此不存在缓冲区溢出风险。 |
| 1178 | vim-9.1.1330 | concat_str | cpp/unbounded-write | 792 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc为目标缓冲区分配了精确的、足以容纳源字符串（str1和str2）的长度加1的空间，因此不会发生缓冲区溢出。 |
| 1179 | vim-9.1.1330 | concat_str | cpp/unbounded-write | 794 | FP | FP | 切片代码显示，函数通过alloc为目标缓冲区分配了精确的、基于输入字符串长度计算的大小，并在调用STRCPY（即strcpy）前进行了空指针检查。目标缓冲区大小足以容纳源字符串和空终止符，因此不存在缓冲区溢出的风险。 |
| 1180 | vim-9.1.1330 | expand_tag_fname | cpp/unbounded-write | 4129 | FP | FP | 切片代码显示目标缓冲区 retval 通过 alloc(MAXPATHL) 分配了固定大小 MAXPATHL，且后续的 vim_strncpy 调用明确限制了拷贝长度（MAXPATHL - (p - tag_fname) - 1），因... |
| 1184 | vim-9.1.1330 | show_one_termcode | cpp/unbounded-write | 7050 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，目标缓冲区IObuff的大小未知，但源字符串p来自get_special_key_name函数，该函数内部使用静态缓冲区string，其大小被定义为MAX_KEY_NAME_LE... |
| 1187 | vim-9.1.1330 | fname_trans_sid | cpp/unbounded-write | 2259 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`fnamelen < FLEN_FIXED`进行了长度检查，确保目标缓冲区`fname_buf`有足够空间，因此不会发生缓冲区溢出。 |
| 1189 | vim-9.1.1330 | exec_instructions | cpp/unbounded-write | 3896 | FP | FP | 切片代码中未发现任何对strcpy的调用，告警所引用的行号（3896）在切片中对应的是STRCPY宏定义，而该宏在切片中被定义为strcpy的包装。切片内没有实际使用STRCPY的代码片段，因此无法确认存在缓冲区溢出风险。 |
| 1195 | vim-9.1.1330 | ExpandBufnames | cpp/invalid-pointer-deref | 2971 | FP | FP | 切片代码显示，在写入 `(*file)[count++] = p` 之前，`*file` 指针已在循环第一轮通过 `*file = ALLOC_MULT(char_u *, count)` 分配了足够的内存，且 `count` 变量受... |
| 1196 | vim-9.1.1330 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | FP | 切片代码显示，在访问 p[pos.col + 1] 之前，存在对 width == 2 的条件检查，且 pos.col 的循环上限为 len，而 p 被分配了 len 个元素。当 width 为 2 时，pos.col + 1 的最大... |
| 1197 | vim-9.1.0790 | <global> | cpp/redundant-null-check-simple | 3502 | FP | FP | 切片代码中，在检查 `inc_opt != NULL` 之前，`inc_opt` 已被明确赋值（`inc_opt = (*curbuf->b_p_inc == NUL) ? p_inc : curbuf->b_p_inc;`），因此该... |
| 1198 | vim-9.1.0790 | <global> | cpp/redundant-null-check-simple | 3584 | FP | FP | 切片代码中未发现对空指针的冗余检查，告警信息指向的代码行（3584）不在切片内，无法确认存在冗余的空指针解引用。基于切片内可见的证据，该告警为误报。 |
| 1199 | vim-9.1.0790 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | FP | FP | 切片代码显示变量'col'在循环条件`check_prevcol(linep, col, '\\', &col)`中被使用，但该函数内部会先对`col`执行`--col`并进行边界检查（`col >= 0`），因此'col'的使用在有... |
| 1200 | vim-9.1.0790 | common_function | cpp/inconsistent-null-check | 4876 | FP | FP | 切片代码显示，在调用 `vim_strsave` 后，`name` 变量被传递给 `func_ref` 或 `vim_free` 等函数，这些函数内部会处理 NULL 指针（例如 `func_ref` 在开头检查 `name == N... |
| 1202 | vim-9.1.0790 | get_isolated_shell_name | cpp/inconsistent-null-check | 2695 | FP | FP | 切片代码显示，函数`gettail`在输入为NULL时会返回空字符串，而非NULL，因此`vim_strsave`的输入不会是NULL，其返回值`p`在后续被直接返回，调用者`get_isolated_shell_name`的返回值可... |
| 1203 | vim-9.1.0790 | get_isolated_shell_name | cpp/inconsistent-null-check | 2706 | FP | FP | 函数`vim_strnsave`的返回值`p`被直接返回给调用者，调用者`get_isolated_shell_name`的返回值在切片代码的调用上下文中可能被检查。告警仅基于统计模式（87%的调用检查null），但切片内未显示此特定... |
| 1204 | vim-9.1.0790 | did_set_cryptmethod | cpp/inconsistent-null-check | 1821 | FP | FP | 切片代码显示，vim_strsave 的参数是字符串字面量 "zip"，而非动态或可能失败的内存分配来源，因此该调用不会返回 NULL，无需检查。 |
| 1205 | vim-9.1.0790 | did_set_background | cpp/inconsistent-null-check | 1082 | FP | FP | 切片代码显示，在调用vim_strsave后，其返回值p_bg立即被传递给check_string_option函数，该函数会检查指针是否为NULL并将其设置为empty_option，这提供了对空指针的防护。 |
| 1206 | vim-9.1.0790 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 切片代码显示，在调用 `find_win_by_nr_or_id` 后，其返回值 `wp->w_popup_prop_win` 立即被 `win_valid_any_tab` 函数检查。如果检查失败，该值会被重置为 `curwin`，... |
| 1207 | vim-9.1.0790 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 告警指出对regnext的调用结果未检查null，但切片代码显示在调用regnext后，变量'next'被直接使用而未进行空值检查。然而，在切片中可见的regnext函数定义（第1042-1058行）表明，当输入指针p为NULL或re... |
| 1208 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 切片代码显示，在调用regnode后，其返回值被立即用于赋值或条件判断（如`if (ret == NULL)`），且后续逻辑（如`regtail`）会检查`reg_toolong`标志并在出错时返回NULL，这表明代码路径已包含错误处... |
| 1209 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 切片代码显示，在调用 `regnode(NOTHING)` 后，其返回值 `br` 被立即用于后续的 `regtail` 操作，但该操作仅在 `ret != JUST_CALC_SIZE` 的条件下执行。`regnode` 函数内部处... |
| 1210 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 切片代码显示，在调用`regnext(br)`之前，已经检查了`reg_toolong`标志，并且`regnext`函数内部也会检查`reg_toolong`并返回NULL。此外，`br`变量来自`ret`或`OPERAND(br)`... |
| 1211 | vim-9.1.0790 | win_redr_custom | cpp/inconsistent-null-check | 1115 | FP | FP | 切片代码显示在调用 vim_strsave 后，其返回值 stl 被传递给 build_stl_str_hl 函数使用，随后立即通过 vim_free(stl) 释放，这表明代码正确处理了内存管理，且没有可见的后续空指针解引用风险。 |
| 1212 | vim-9.1.0790 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 切片代码显示，在调用getroom后，函数返回的指针'n'在后续的#ifdef SPELL_PRINTTREE代码块中被检查是否为NULL，这表明代码逻辑已包含对潜在空指针的考虑。此外，getroom函数内部在内存分配失败时会返回NU... |
| 1213 | vim-9.1.0790 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续被赋值给 `tofree`，而 `tofree` 在函数末尾通过 `vim_free(tofree)` 被释放。这表明代码逻辑已处理了内存管理，且 `name` ... |
| 1214 | vim-9.1.0790 | define_function | cpp/inconsistent-null-check | 5356 | FP | FP | 切片代码中，vim_strchr的返回值在多个地方被检查是否为NULL（例如在条件判断中直接使用），并且告警所指的调用点（第5356行）在切片中未出现，无法确认该特定调用点是否存在未检查NULL的问题。基于切片内可见的典型使用模式（检... |
| 1215 | vim-9.1.0790 | is_duplicate_variable | cpp/inconsistent-null-check | 909 | FP | FP | 切片代码中函数 `is_duplicate_variable` 为空实现，未调用 `vim_strnsave` 或任何可能返回空指针的函数，因此工具报告的未检查空指针问题在当前上下文中不存在。 |
| 1216 | vim-9.1.0790 | exec_instructions | cpp/inconsistent-null-check | 3266 | FP | FP | alloc_clear 返回的指针被直接赋值给 tv->vval.v_object，后续代码立即访问其成员（如 obj_class），这暗示调用者期望分配成功。切片中未显示对 alloc_clear 返回值的显式 NULL 检查，但代... |
| 1217 | vim-9.1.0790 | barline_parse | cpp/inconsistent-null-check | 1122 | FP | FP | 切片代码显示，在调用vim_strsave(s)之前，变量s可能指向已分配的缓冲区buf（当s == buf时），或者指向已转换的字符串sconv（当converted为TRUE时）。在这两种情况下，字符串已存在于分配的内存中，且后续... |
| 1218 | vim-9.1.0790 | ex_history | cpp/unsafe-strcat | 780 | FP | FP | 切片代码显示，在使用STRCAT前，已通过条件`vim_strsize(hist[i].hisstr) > (int)Columns - 10`检查了源字符串长度，若过长则调用trunc_string进行截断，否则才使用STRCAT。... |
| 1219 | vim-9.1.0790 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | STRCAT 宏是对标准 strcat 的简单包装，但切片代码显示其目标缓冲区 NameBuff 是一个全局或静态缓冲区（如 MAXPATHL 大小），且其使用模式（拼接固定字符串）在切片可见范围内不会导致缓冲区溢出。 |
| 1220 | vim-9.1.0790 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 切片代码显示，`name` 指针指向的字符串来源是有限的常量字符串或一个固定大小的本地数组 `namebuf`，其最大长度为3（包括空字符）。虽然未显式检查目标缓冲区 `buf` 的大小，但根据上下文，该函数用于生成键盘按键名称，`b... |
| 1222 | vim-9.1.0790 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 切片代码显示，在调用STRCAT宏（即strcat）之前，目标缓冲区newword已通过vim_strncpy(newword, ae->ae_add, MAXWLEN - 1)或vim_strncpy(newword, word, ... |
| 1230 | vim-9.1.0790 | buf_write | cpp/unbounded-write | 2566 | FP | FP | 切片代码中未发现对strcat函数的直接调用，告警提及的'call to strcat'在提供的代码片段中不可见。基于可见的切片代码，无法确认存在缓冲区溢出漏洞，因此判定为误报。 |
| 1231 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2138 | FP | FP | 切片代码中未发现对strcat的直接调用，告警提及的strcat可能来自宏定义STRCAT，但切片内未显示其使用存在缓冲区溢出风险的具体证据。基于切片信息，无法确认存在可触发的缓冲区溢出漏洞。 |
| 1233 | vim-9.1.0790 | globpath | cpp/unbounded-write | 3795 | FP | FP | 切片代码中在调用STRCAT前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度不会超过`MAXPATHL`，因此不存在... |
| 1235 | vim-9.1.0790 | win_redr_status_matches | cpp/unbounded-write | 658 | FP | FP | 切片代码显示，目标缓冲区 `buf` 的大小已根据 `Columns` 和 `MB_MAXBYTES` 通过 `alloc` 安全分配，且循环条件 `(long)(clen + status_match_len(xp, SHOW_MA... |
| 1243 | vim-9.1.0790 | ex_substitute | cpp/unbounded-write | 4883 | FP | FP | 切片代码中未发现对strcat的直接调用，告警引用的行号（4883）在切片中对应的是STRCAT宏的使用，但该宏用于拼接已知长度的字符串片段，且上下文显示new_start缓冲区大小已通过new_start_len管理，存在边界检查机制。 |
| 1244 | vim-9.1.0790 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区分配了精确计算的长度，且该长度足以容纳源字符串cmd（通过STRLEN(cmd)计算并加上额外字符）。因此，缓冲区大小是充足的，不存在溢出风险。 |
| 1245 | vim-9.1.0790 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，已通过alloc(len)分配了缓冲区，且len的计算包含了所有待拼接字符串的长度和终止符，缓冲区大小足够，不存在溢出风险。 |
| 1253 | vim-9.1.0790 | discard_exception | cpp/unbounded-write | 642 | FP | FP | 切片代码显示，目标缓冲区IObuff是全局缓冲区，其大小未在切片中明确，但源字符串saved_IObuff是之前通过vim_strsave(IObuff)保存的副本，长度与原始IObuff相同。因此，将saved_IObuff复制回I... |
| 1262 | vim-9.1.0790 | vim_rename | cpp/unbounded-write | 3839 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。 |
| 1266 | vim-9.1.0790 | concat_fnames | cpp/unbounded-write | 3123 | FP | FP | 切片代码显示，目标缓冲区 `dest` 的大小通过 `alloc(STRLEN(fname1) + STRLEN(fname2) + 3)` 精确分配，足以容纳源字符串 `fname1` 和 `fname2` 以及额外的分隔符和终止符... |
| 1267 | vim-9.1.0790 | concat_fnames | cpp/unbounded-write | 3126 | FP | FP | 切片代码显示，目标缓冲区 `dest` 的大小通过 `alloc(STRLEN(fname1) + STRLEN(fname2) + 3)` 精确分配，足以容纳两个源字符串、一个可选的分隔符以及终止符，因此 `strcat` 操作不会... |
| 1268 | vim-9.1.0790 | uniquefy_paths | cpp/unbounded-write | 2364 | FP | FP | 切片代码显示，`file_pattern` 缓冲区的大小是 `alloc(len + 2)`，其中 `len` 是输入 `pattern` 的长度。`STRCAT` 操作是将 `pattern` 追加到已包含 `"*"` 和空字符的缓... |
| 1273 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 805 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，明确使用STRLEN检查了源字符串长度与目标缓冲区大小（MAXPATHL），并确保有足够的空间，从而防止了缓冲区溢出。 |
| 1274 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 819 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，明确进行了长度检查（STRLEN(file_path) + STRLEN(stackp->ffs_fix_path) + 1 < MAXPATHL），确保目标缓冲区不会溢出。 |
| 1275 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 940 | FP | FP | 切片代码中所有STRCPY调用前都进行了明确的长度检查（STRLEN(...) + ... < MAXPATHL），确保目标缓冲区不会溢出，因此告警是误报。 |
| 1276 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 942 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，均存在明确的长度检查（例如使用STRLEN计算并比较MAXPATHL），确保目标缓冲区不会溢出。这些防护机制使得告警指出的缓冲区溢出风险在实际执行路径中不会发生。 |
| 1277 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 1110 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，存在明确的长度检查（STRLEN(...) + 1 < MAXPATHL），确保目标缓冲区file_path（大小为MAXPATHL）不会溢出。因此，该告警是误报。 |
| 1278 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 1112 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区不会溢出。因此，该告警为误报。 |
| 1290 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 告警点位于对已知资源文件元数据的字符串拼接，`res_cidfont->title` 和 `res_cidfont->version` 来自受控的PostScript资源文件头，其长度在 `prt_open_resource` 函数中... |
| 1291 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 切片代码显示，`res_cmap->title` 和 `res_cmap->version` 是从受控的 PostScript 资源文件中解析出来的，其长度在 `prt_open_resource` 函数中通过 `vim_strncp... |
| 1292 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 切片代码显示，`res_cmap->title` 和 `res_cmap->version` 是从受控的PostScript资源文件中解析出的固定字段，其长度在解析时已被限制（如 `vim_strncpy` 的使用），且缓冲区 `bu... |
| 1295 | vim-9.1.0790 | prt_resource_name | cpp/unbounded-write | 1659 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已使用STRLEN检查了源字符串长度，确保其小于MAXPATHL，从而防止了缓冲区溢出。 |
| 1297 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 975 | FP | FP | NameBuff 缓冲区大小在切片中未明确显示，但根据其在整个代码库中的典型用法（如与 MAXPATHL 一起使用）以及告警点之前的 STRCPY 和 STRCAT 操作是针对已知的、受控的目录路径和文件扩展名，这些输入的长度是有限且... |
| 1298 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 991 | FP | FP | 目标缓冲区 `NameBuff` 的大小未在切片中明确给出，但根据其在整个代码库中的典型用法（如 `MAXPATHL` 常量）和上下文（用于构建文件路径），它很可能是一个足够大的固定大小缓冲区。此外，`tagfname` 参数是调用者... |
| 1300 | vim-9.1.0790 | highlight_set_startstop_termcode | cpp/unbounded-write | 1477 | FP | FP | 切片代码在调用STRCAT（即strcat）前，明确检查了目标缓冲区buf（大小为100字节）的剩余空间，确保STRLEN(buf) + STRLEN(p) < 99，从而防止了缓冲区溢出。 |
| 1303 | vim-9.1.0790 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 切片代码中，`amt` 变量已通过精确计算所有输入字符串的长度总和并加上固定分隔符的长度来分配缓冲区，`sprintf` 写入的格式化字符串长度与预先计算的 `amt` 完全匹配，不存在缓冲区溢出的风险。 |
| 1304 | vim-9.1.0790 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了该大小的内存（buf = alloc(amt)），确保了目标缓冲区足以容纳格式化后的字符串，因此不存在缓冲区溢出风险。 |
| 1308 | vim-9.1.0790 | ins_compl_infercase_gettext | cpp/unbounded-write | 653 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过条件`(p - IObuff) + 6 >= IOSIZE`确保了目标缓冲区`gap.ga_data`有足够的空间（通过`ga_grow(&gap, IOSIZE)`分配... |
| 1310 | vim-9.1.0790 | findswapname | cpp/unbounded-write | 4967 | FP | FP | 切片代码显示，STRCPY的目标缓冲区fname2是通过alloc(n + 2)分配的，其大小比源字符串fname的长度n多2个字节，确保了足够的空间。STRCPY操作在分配后立即执行，不会发生缓冲区溢出。 |
| 1315 | vim-9.1.0790 | str2specialbuf | cpp/unbounded-write | 1919 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度小于给定的`len`参数，从... |
| 1318 | vim-9.1.0790 | expand_env_esc | cpp/unbounded-write | 1632 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，存在明确的长度检查 `(STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen)`，确保目标缓冲区有足够空间，因此不会发生缓冲区溢出。 |
| 1319 | vim-9.1.0790 | call_shell | cpp/unbounded-write | 1877 | FP | FP | 切片代码显示，在调用STRCAT前，已通过alloc为ncmd分配了足够的内存，其大小为STRLEN(ecmd) + STRLEN(p_sxq) * 2 + 1，这包含了源字符串ecmd和两个p_sxq以及终止符的空间，因此缓冲区大小... |
| 1323 | vim-9.1.0790 | add_to_showcmd | cpp/unbounded-write | 1760 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已计算了目标缓冲区showcmd_buf的当前长度和待追加字符串p的长度，并检查了溢出（overflow）。如果溢出大于0，会通过mch_memmove移动缓冲区内容以腾出空间，... |
| 1329 | vim-9.1.0790 | option_value2string | cpp/unbounded-write | 8213 | FP | FP | 切片代码显示STRCPY宏的目标缓冲区NameBuff未明确其大小，但告警点位于处理特殊键名的分支，其源字符串来自get_special_key_name函数，该函数内部使用固定大小的本地缓冲区string[MAX_KEY_NAME_... |
| 1330 | vim-9.1.0790 | option_value2string | cpp/unbounded-write | 8215 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，函数get_special_key_name内部使用固定大小的缓冲区string[MAX_KEY_NAME_LEN + 1]并进行了边界检查（如len + idx + 2 <= ... |
| 1338 | vim-9.1.0790 | regtilde | cpp/unbounded-write | 1959 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`tmpsublen > MAXCOL`检查了目标缓冲区大小，并在超出时提前报错退出，且tmpsub缓冲区大小通过`alloc(tmpsublen + 1)`精确分配，... |
| 1342 | vim-9.1.0790 | do_put | cpp/unbounded-write | 2095 | FP | FP | 切片代码中未发现对strcat的直接调用，告警提及的多个strcat调用在切片中不可见。切片内可见的内存操作（如mch_memmove）均使用了显式计算的长度，且存在分配检查（alloc），未发现明显的缓冲区溢出证据。 |
| 1350 | vim-9.1.0790 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 告警点位于`make_case_word`函数中，该函数仅在特定标志下使用`STRCPY`（即`strcpy`）。切片代码显示，调用该函数的两个分支`allcap_copy`和`onecap_copy`均包含明确的边界检查（如`MAX... |
| 1356 | vim-9.1.0790 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过getroom函数为目标缓冲区sc分配了精确的长度（STRLEN(s) + 1），确保了缓冲区大小足以容纳源字符串s及其终止符，因此不存在缓冲区溢出的风险。 |
| 1357 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 切片代码显示告警点位于处理拼写信息（如NAME、VERSION等）的代码块中，这些信息来自受控的affix文件，并非不可信的用户输入。代码通过getroom分配了足够的内存，且拼接前已计算了总长度，因此不存在缓冲区溢出的实际风险。 |
| 1358 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 切片代码显示告警点位于处理拼写信息（如NAME、AUTHOR等）的代码块中，这些信息来自受控的.aff文件，并非不可信的用户输入。代码通过getroom分配了足够的内存来拼接字符串，且拼接前已计算了总长度，因此不存在缓冲区溢出的实际风险。 |
| 1361 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 切片代码显示，strcpy的目标缓冲区`cur_aff->ah_key`的大小为`AH_KEY_LEN`，而源字符串`items[1]`在复制前已通过`STRLEN(items[1]) >= AH_KEY_LEN`检查，确保不会溢出。 |
| 1364 | vim-9.1.0790 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | 切片代码显示，STRCPY的目标缓冲区`sft->sft_word`的大小是通过`offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1`动态分配的，其大小精确匹配源字符串`goodw... |
| 1365 | vim-9.1.0790 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | 目标缓冲区 fword 的大小为 MAXWLEN，而源字符串 su->su_fbadword 是同一函数内生成的拼写建议候选词，其长度在之前的逻辑中已被确保不超过 MAXWLEN。切片代码中未见外部未受控数据直接复制到 fword，因... |
| 1366 | vim-9.1.0790 | concat_str | cpp/unbounded-write | 795 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc为目标缓冲区分配了精确的、足以容纳源字符串（str1和str2）的长度（包括空终止符），因此不会发生缓冲区溢出。 |
| 1367 | vim-9.1.0790 | concat_str | cpp/unbounded-write | 797 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加1，因此不会发生缓冲区溢出。 |
| 1371 | vim-9.1.0790 | show_one_termcode | cpp/unbounded-write | 7058 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区IObuff足够大（在调用前已初始化并填充了多个字节），且源字符串p来自get_special_key_name函数，该函数内部使用固定大小的静态缓冲区string并确保以NUL结尾，因此不存在... |
| 1374 | vim-9.1.0790 | get_scriptlocal_funcname | cpp/unbounded-write | 4658 | FP | FP | 切片代码显示，目标缓冲区 `newname` 的大小是精确计算的（`alloc(STRLEN(sid_buf) + STRLEN(p + off) + 1)`），然后使用 `STRCPY` 和 `STRCAT` 进行复制和拼接，不会发... |
| 1379 | vim-9.1.0790 | exec_instructions | cpp/unbounded-write | 3496 | FP | FP | 切片代码中未发现任何对strcpy的调用，告警消息中提到的所有strcpy调用在提供的切片中均不可见。因此，基于切片内可见的证据，该告警是误报。 |
| 1385 | vim-9.1.0790 | ExpandBufnames | cpp/invalid-pointer-deref | 2937 | FP | FP | 切片代码显示，在写入 `(*file)[count++] = p` 之前，`*file` 已在循环第一轮通过 `*file = alloc(...)` 分配了足够的内存（`count` 个元素），且 `count` 作为索引在分配的内... |
| 1386 | vim-9.1.0790 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | FP | 切片代码显示，在访问 p[pos.col + 1] 之前，存在对 width == 2 的条件检查，并且 len 是列数，pos.col 在循环中严格小于 len，当 width 为 2 时，pos.col + 1 的最大值等于 le... |
| 1387 | musl-1.2.3 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 切片代码显示，分配的内存大小 `sizeof *f + UNGET + BUFSIZ` 是用于一个 `FILE` 结构体及其内部缓冲区的复合结构，这是标准的内存布局模式，并非可疑的分配大小计算错误。 |
| 1388 | musl-1.2.3 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat之前，切片代码显示buf数组的大小为256字节，并且通过inet_ntop等函数写入的内容长度有限，同时存在对nodelen的边界检查（strlen(buf) >= nodelen时返回EAI_OVERFLOW），这... |
| 1389 | musl-1.2.3 | load_library | cpp/unbounded-write | 1162 | FP | FP | 切片代码显示，`strcpy`的目标缓冲区`p->name`是`p->buf`的别名，而`p`是通过`calloc(1, alloc_size)`分配的，其中`alloc_size = sizeof *p + strlen(pathn... |
| 1390 | musl-1.2.3 | <global> | cpp/unbounded-write | 67 | FP | FP | 切片代码显示，在调用strcpy之前，已通过strlen(canon)计算了所需缓冲区大小，并与传入的buflen进行了比较（need > buflen），若空间不足会提前返回ERANGE。因此，在strcpy执行时，目标缓冲区h->... |
| 1391 | musl-1.2.3 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 切片代码中，在调用strcpy(node, buf)之前，有明确的长度检查'if (strlen(buf) >= nodelen) return EAI_OVERFLOW;'，这确保了目标缓冲区node不会溢出。因此该告警是误报。 |
| 1392 | musl-1.2.3 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码显示，在调用strcpy之前，已通过`if (strlen(logname) >= size) return ERANGE;`检查了源字符串长度是否小于目标缓冲区大小，防止了缓冲区溢出。 |
| 1393 | musl-1.2.2 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 切片代码显示，分配的内存大小是 `sizeof *f + UNGET + BUFSIZ`，这是一个为 `FILE` 结构体及其额外缓冲区预留的典型模式，并非错误的大小计算。代码逻辑正确，分配的内存用于结构体和缓冲区，因此是误报。 |
| 1394 | musl-1.2.2 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 切片代码显示，在调用strcat之前，buf数组的大小为256字节，且通过inet_ntop等函数写入的内容长度有限，同时存在对最终字符串长度的检查（strlen(buf) >= nodelen），这防止了缓冲区溢出。 |
| 1395 | musl-1.2.2 | load_library | cpp/unbounded-write | 1161 | FP | FP | 切片代码显示，`pathname` 的来源（`buf` 或 `name`）在写入 `p->name` 前已通过 `snprintf` 或 `strlen` 进行了长度限制或检查，且 `buf` 的大小为 `2*NAME_MAX+2`，... |
| 1396 | musl-1.2.2 | <global> | cpp/unbounded-write | 67 | FP | FP | 切片代码显示，在调用strcpy之前，已经通过strlen(canon)计算了所需缓冲区大小，并与传入的buflen进行了比较（need > buflen），若空间不足则提前返回ERANGE。这确保了目标缓冲区buf有足够的空间容纳c... |
| 1397 | musl-1.2.2 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 切片代码中，在调用strcpy(node, buf)之前，明确进行了长度检查'if (strlen(buf) >= nodelen) return EAI_OVERFLOW;'，这确保了目标缓冲区node不会溢出。因此该告警是误报。 |
| 1398 | musl-1.2.2 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码显示，在调用strcpy之前，已通过`if (strlen(logname) >= size) return ERANGE;`检查了目标缓冲区大小，防止了缓冲区溢出。 |
| 1399 | musl-1.2.1 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 分配的内存大小（sizeof *f + UNGET + BUFSIZ）是用于结构体FILE、反推缓冲区UNGET和标准缓冲区BUFSIZ的组合，其对齐和布局由实现逻辑决定，并非错误。代码逻辑正确，分配的内存足以容纳所需数据，没有内存访... |
| 1400 | musl-1.2.1 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 切片代码显示，在调用strcat之前，已经通过inet_ntop将地址写入buf，且buf的大小为256字节，而p指向的字符串长度有限（来自itoa或if_indextoname），并且后续有strlen(buf) >= nodele... |
| 1401 | musl-1.2.1 | load_library | cpp/unbounded-write | 1138 | FP | FP | 切片代码显示，在调用strcpy之前，pathname的来源（buf或name）已通过路径搜索和构建过程得到控制，且buf的大小（2*NAME_MAX+2）在相关函数（如path_open）中被谨慎使用，没有证据表明环境变量会导致超出... |
| 1402 | musl-1.2.1 | <global> | cpp/unbounded-write | 67 | FP | FP | 切片代码显示，在调用strcpy之前，已经通过strlen(canon)计算了所需缓冲区大小，并与传入的buflen进行了比较（need > buflen），若空间不足则提前返回ERANGE。因此，当strcpy执行时，缓冲区大小已得... |
| 1403 | musl-1.2.1 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 切片代码中，在调用strcpy(node, buf)之前，明确进行了长度检查'if (strlen(buf) >= nodelen) return EAI_OVERFLOW;'，该防护机制确保了目标缓冲区不会溢出。 |
| 1404 | musl-1.2.1 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码显示，在调用strcpy之前，已通过`if (strlen(logname) >= size) return ERANGE;`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1405 | musl-1.1.24 | getname | cpp/offset-use-before-range-check | 89 | FP | FP | 切片代码显示，在for循环条件中，对变量'i'的访问与范围检查'i<TZNAME_MAX'是同时进行的，这确保了在访问(*p)[i]之前，i的值已经过范围检查，因此不存在先于范围检查使用偏移量的风险。 |
| 1406 | musl-1.1.24 | getname | cpp/offset-use-before-range-check | 93 | FP | FP | 切片代码显示，在for循环的条件部分，变量'i'的使用已通过'i<TZNAME_MAX'进行了前置范围检查，确保了数组访问的安全性，因此告警为误报。 |
| 1407 | musl-1.1.24 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 切片代码显示分配的内存大小 `sizeof *f + UNGET + BUFSIZ` 是用于 `FILE` 结构体及其内部缓冲区的总大小，这是标准的内存布局模式，并非可疑的分配大小不匹配。 |
| 1408 | musl-1.1.24 | getnameinfo | cpp/unsafe-strcat | 178 | FP | FP | 切片代码显示，在调用strcat之前，buf数组的大小为256字节，并且通过inet_ntop和手动构建的字符串p（来自itoa或if_indextoname）的长度是有限且可控的。此外，在strcat之后，代码立即检查strlen(... |
| 1409 | musl-1.1.24 | load_library | cpp/unbounded-write | 1133 | FP | FP | 切片代码显示，在调用strcpy之前，pathname的来源（buf数组）大小已通过path_open等函数调用得到控制，且对name的长度进行了检查（strlen(name) > NAME_MAX），缓冲区溢出风险已被缓解。 |
| 1410 | musl-1.1.24 | <global> | cpp/unbounded-write | 67 | FP | FP | 切片代码显示，在调用strcpy之前，已经通过strlen(canon)计算了所需缓冲区大小，并与传入的buflen进行了比较（need > buflen），确保缓冲区足够。canon数组大小为256字节，且__lookup_name... |
| 1411 | musl-1.1.24 | getnameinfo | cpp/unbounded-write | 182 | FP | FP | 切片代码中，在调用strcpy(node, buf)之前，有明确的长度检查'if (strlen(buf) >= nodelen) return EAI_OVERFLOW;'，这确保了目标缓冲区node不会溢出。因此该告警是误报。 |
| 1412 | musl-1.1.24 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码中，在调用strcpy之前，已通过`if (strlen(logname) >= size) return ERANGE;`检查了源字符串长度是否小于目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1413 | musl-1.2.4 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 切片代码显示分配的内存大小是 `sizeof *f + UNGET + BUFSIZ`，这是一个结构体大小加上两个常量的总和，是经过设计的有效内存布局，用于为FILE结构体和额外的缓冲区预留空间，并非错误的分配大小。 |
| 1414 | musl-1.2.4 | getnameinfo | cpp/unsafe-strcat | 180 | FP | FP | 切片代码显示，在调用strcat之前，buf数组的大小为256字节，且通过inet_ntop写入的IPv6地址字符串长度有限，加上scopeid转换后的字符串（由itoa或if_indextoname生成）长度也有限，组合后不太可能超... |
| 1415 | musl-1.2.4 | load_library | cpp/unbounded-write | 1224 | FP | FP | 切片代码显示，在调用strcpy之前，pathname的来源（buf数组）的大小为2*NAME_MAX+2，并且通过path_open等函数的使用确保了写入buf的路径名长度受到buf_size（即sizeof buf）的限制，因此不... |
| 1416 | musl-1.2.4 | <global> | cpp/unbounded-write | 69 | FP | FP | 切片代码显示，`canon` 缓冲区在 `__lookup_name` 函数中已通过 `strnlen(name, 255)` 和 `l-1 >= 254` 检查确保长度不超过255字节，且 `canon` 数组大小为256，因此 `... |
| 1417 | musl-1.2.4 | getnameinfo | cpp/unbounded-write | 184 | FP | FP | 在调用strcpy之前，代码已通过'if (strlen(buf) >= nodelen) return EAI_OVERFLOW;'进行了明确的长度检查，确保目标缓冲区node有足够空间，因此不会发生缓冲区溢出。 |
| 1418 | musl-1.2.4 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码显示，在调用strcpy之前，已通过`if (strlen(logname) >= size) return ERANGE;`对目标缓冲区大小进行了检查，确保了不会发生缓冲区溢出。 |
| 1419 | tmux-3.4 | <global> | cpp/overflow-buffer | 67 | FP | FP | 切片代码显示，在访问 `place[1]` 之前，已经通过 `*(place = nargv[BSDoptind]) != '-'` 和 `place[1] && *++place == '-'` 等条件确保了 `place` 指向一... |
| 1420 | tmux-3.4 | <global> | cpp/overflow-buffer | 68 | FP | FP | 切片代码显示，在访问 `place[1]` 之前，已经通过 `if (place[1] && *++place == '-')` 检查了 `place[1]` 不为空，因此后续的 `if (place[1])` 访问是安全的，不会发生... |
| 1421 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 700 | FP | FP | 切片代码显示，在调用cliConcatArguments函数前，已通过assert语句确保args->type为REDIS_REPLY_ARRAY，且args是specs->element[j+1]的有效指针，这防止了空指针解引用。 |
| 1422 | redis-7.0.11 | breakstat | Dereference of null pointer | 986 | FP | FP | 切片代码显示，在调用 `luaK_codeABC` 函数前，`bl` 指针已在 `while` 循环中被更新，且循环条件 `while (bl && !bl->isbreakable)` 确保了只有当 `bl` 非空时才会进入循环体。... |
| 1423 | redis-7.0.11 | xgroupCommand | Dereference of null pointer | 2700 | FP | FP | 在SETID子命令分支中，cg指针的赋值依赖于前面的代码逻辑，但切片中未显示cg在进入该分支前被初始化的路径。然而，该分支的条件检查确保了cg在解引用前（cg->last_id = id）必然存在，因为该分支仅在流和消费者组已存在时执... |
| 1424 | redis-7.0.11 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1626 | FP | FP | 切片代码显示，在调用`sdsfree(state->lines[linenum])`之前，`linenum`变量未定义或初始化，这很可能是一个逻辑错误，但`sdsfree`函数内部已包含对NULL指针的检查（`if (s == NUL... |
| 1425 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在访问 `specs->element[j]->str` 之前，已经通过 `assert(specs->element[j]->type == REDIS_REPLY_STRING)` 确保了元素类型为字符串，这保证了指... |
| 1427 | redis-7.0.11 | dictGetRandomKey | Dereference of null pointer | 682 | FP | FP | 切片代码显示，在获取`he`指针的循环中，`do...while(he == NULL)`保证了`he`不为空，且后续的`while(he)`循环也确保了`listlen`大于0，因此`he = he->next`不会对空指针解引用。 |
| 1428 | redis-7.0.11 | cliConcatArguments | Dereference of null pointer | 542 | FP | FP | 切片代码显示，在访问 `arguments->elements` 之前，函数 `cliAddArgument` 已通过类型检查确保 `argMap` 是有效的 MAP 或 ARRAY 类型，并且 `arguments` 变量是从 `a... |
| 1429 | redis-7.0.11 | rewriteConfigRewriteLine | Dereference of null pointer | 1236 | FP | FP | 在调用`sdsfree(state->lines[linenum])`之前，代码已通过`if (l)`检查确保`l`非空，并通过`listFirst(l)`获取了`ln`，且`linenum`是从`ln->value`转换而来。切片中... |
| 1430 | redis-7.0.11 | sdscat_orempty | Dereference of null pointer | 532 | FP | FP | 切片代码显示函数参数 `value` 在解引用前没有进行空指针检查，但调用函数 `sdscat` 内部会调用 `strlen(t)`，如果 `value` 为 NULL，`strlen` 会先于 `value[0]` 的解引用导致崩溃... |
| 1432 | redis-7.0.11 | cliInitGroupHelpEntries | Dereference of null pointer | 771 | FP | FP | 切片代码显示，`helpEntries` 数组的索引 `pos` 由静态变量 `helpEntriesLen` 初始化，并在循环中递增。未发现对 `helpEntries` 数组边界或空指针的检查，但告警点 `helpEntries[... |
| 1433 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 688 | FP | FP | 切片代码中，在访问 `reply->str` 之前，已通过 `assert(reply->type == REDIS_REPLY_STRING)` 确保 `reply` 是字符串类型，且 `sdsnew` 函数内部会处理 `NULL`... |
| 1435 | redis-7.0.11 | _quicklistListpackMerge | Dereference of null pointer | 813 | FP | FP | 切片代码显示，在访问 `keep->count` 和 `keep->entry` 之前，逻辑已确保 `keep` 指针不为空（`keep = a` 或 `keep = b`），且 `a` 和 `b` 是函数参数，调用方非空。因此，对 ... |
| 1436 | redis-7.0.11 | xgroupCommand | Dereference of null pointer | 2696 | FP | FP | 在SETID子命令中，当参数为'$'时，代码`s->last_id`的访问发生在`s`指针非空的条件下。切片显示`s`在`o = lookupKeyWrite(c->db,c->argv[2]);`中赋值，且当`o`存在且类型正确时`... |
| 1437 | redis-7.0.11 | cliOldInitHelp | Dereference of null pointer | 455 | FP | FP | 切片代码显示 `zmalloc` 在分配失败时会调用 `zmalloc_oom_handler` 处理，不会返回空指针给 `tmp.argv`；且 `sdscatprintf` 和 `sdsempty` 的调用链未显示会返回空指针，因... |
| 1438 | redis-7.0.11 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 切片代码中，在告警行（assert语句）之前存在条件判断 `if (quicklist->len == 0) return;`，这保证了当链表为空时函数会提前返回，因此后续对 `quicklist->head` 和 `quicklis... |
| 1439 | redis-7.0.11 | getKeySizes | Dereference of null pointer | 8193 | FP | FP | 切片代码显示，在警告行 `if(!types[i] ｜｜ (!types[i]->sizecmd && !memkeys))` 中，对 `types[i]` 进行了空指针检查，只有非空时才会解引用 `types[i]->sizecmd... |
| 1440 | redis-7.0.11 | json_next_token | Dereference of null pointer | 1022 | FP | FP | 切片代码显示，在访问 `ch2token` 数组前，`json->cfg` 指针的有效性已在函数外部或调用链中得到保证，且告警行 `token->type = ch2token[ch];` 中的数组索引 `ch` 是 `unsigne... |
| 1441 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 684 | FP | FP | 切片代码显示，在访问 `help->org.summary` 之前，`help` 指针已在函数开头通过 `help = next++` 被正确初始化，且 `next` 作为参数传入，不存在空指针解引用。告警点位于已初始化的结构体成员赋值处。 |
| 1442 | redis-7.0.11 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 切片代码显示，在访问 `forward->next` 之前，`forward` 指针已通过 `quicklist->head` 初始化，且循环条件 `depth++ < quicklist->compress` 和 `forward ... |
| 1443 | redis-7.0.11 | _quicklistListpackMerge | Dereference of null pointer | 820 | FP | FP | 在切片代码中，`keep`指针的赋值逻辑确保了它不会为NULL。`keep`被赋值为`a`或`b`，而这两个节点作为函数参数传入，且在调用`lpMerge`之前已对它们进行了解压缩操作，表明它们是有效的节点。因此，对`keep->en... |
| 1444 | redis-7.0.11 | moduleFreeContext | Dereference of null pointer | 748 | FP | FP | 切片代码显示，在调用 `zfree(ctx->postponed_arrays)` 之前，已通过 `if (ctx->postponed_arrays)` 检查指针非空，因此不会发生空指针解引用。 |
| 1445 | redis-7.0.11 | extent_try_coalesce_impl | Dereference of null pointer | 1666 | FP | FP | 切片代码显示，在解引用指针 `extent` 之前，函数 `extent_lock_from_addr` 的返回值 `prev` 和 `next` 都经过了 `NULL` 检查，并且 `extent_unlock` 函数内部有 `as... |
| 1446 | redis-7.0.11 | streamPropagateXCLAIM | Dereference of null pointer | 1564 | FP | FP | 切片代码显示告警行访问了 `nack->consumer->name`，但该指针在调用 `createStringObject` 和 `sdslen` 前未被检查。然而，`sdslen` 函数内部通过 `s[-1]` 访问内存，若 `... |
| 1447 | redis-7.0.11 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 切片代码显示，在警告行（h->size == 0）之前，h 指针已通过多次赋值（如 h = child; h = newh;）和函数调用（如 raxAddChild, raxCompressNode）被更新，这些函数均返回有效的节点指... |
| 1448 | redis-7.0.11 | extent_try_coalesce_impl | Dereference of null pointer | 1636 | FP | FP | 切片代码显示，在解引用指针 `coalesced` 之前，存在对 `extents` 指针的访问（`extents->delay_coalesce`），而 `extents` 是函数参数，不可能为 NULL。此外，`coalesced... |
| 1449 | redis-7.0.11 | clusterManagerAddSlots | Dereference of null pointer | 3898 | FP | FP | 切片代码显示，在调用`clusterManagerCheckRedisReply`函数前，`err`指针已被显式初始化为NULL，且该函数内部对`err`参数进行了非空检查（`if (err != NULL)`），因此不会发生空指针解引用。 |
| 1450 | redis-7.0.11 | min_expand | Dereference of null pointer | 322 | FP | FP | 在切片代码中，对指针 `s` 的解引用发生在条件 `s<ms->src_end` 之后，该条件确保了 `s` 指向有效内存范围，因此不会发生空指针解引用。 |
| 1451 | redis-7.0.11 | strbuf_init | Dereference of null pointer | 53 | FP | FP | 切片代码显示，函数仅将结构体成员`s->buf`初始化为NULL，并未对其进行解引用操作。告警所提示的'解引用空指针'逻辑错误在当前切片中并未发生。 |
| 1452 | redis-7.0.11 | strbuf_ensure_null | Dereference of null pointer | 142 | FP | FP | 切片代码显示函数为内联静态函数，其参数`s`在调用前通常已由调用者确保非空且`buf`和`length`有效；直接对数组`s->buf`进行索引赋值是安全的操作模式，未见明显的空指针解引用逻辑错误。 |
| 1453 | redis-7.0.11 | checkMultiPartAof | Dereference of null pointer | 474 | FP | FP | 切片代码中，在访问 `am->incr_aof_list` 之前，`am` 指针已通过 `aofLoadManifestFromFile` 函数调用获取，虽然未显式检查其是否为 NULL，但该函数在切片中未定义其失败行为。更重要的是，... |
| 1454 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2541 | FP | FP | 切片代码显示 `dstzset->dict` 在调用 `dictPauseAutoResize` 前已被有效初始化（通过 `dictAdd` 调用），且该指针在循环中持续使用，没有可见的使其变为 null 的路径。告警点是对一个已知非... |
| 1455 | redis-7.4.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2891 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，`dstkey` 和 `dstobj` 已被使用，且 `dstzset` 是 `dstobj->ptr` 的一部分。告警行位于 `if (dstkey)` 条件... |
| 1456 | redis-7.4.2 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 切片代码显示，函数`strbuf_init`仅对结构体成员`s->buf`进行初始化赋值为NULL，并未对其进行解引用操作。告警信息描述的'解引用空指针'逻辑错误在提供的代码片段中并未发生。 |
| 1457 | redis-7.4.2 | breakstat | Dereference of null pointer | 986 | FP | FP | 切片代码显示，在访问 `bl->nactvar` 之前，`bl` 指针已在 while 循环中被更新，且循环条件 `while (bl && !bl->isbreakable)` 确保了 `bl` 非空时才进入循环体。因此，当循环退出... |
| 1458 | redis-7.4.2 | xgroupCommand | Dereference of null pointer | 2711 | FP | FP | 在SETID子命令分支中，cg指针的赋值依赖于前面的代码路径。切片显示，当执行到'cg->last_id = id;'这一行时，cg可能为NULL的情况已被前面的条件分支（如CREATE子命令）处理或排除。工具可能未能完全理解控制流，... |
| 1459 | redis-7.4.2 | dictGenericDelete | Dereference of null pointer | 628 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，已经通过 `dictSize(d) == 0` 检查了字典非空，并且在循环中通过 `while(he)` 确保了指针 `he` 非空时才进行解引用，因此不... |
| 1460 | redis-7.4.2 | zdiffAlgorithm1 | Dereference of null pointer | 2497 | FP | FP | 切片代码显示，在调用zslInsert之前，tmp变量由zuiNewSdsFromValue函数返回，该函数总是返回一个有效的sds字符串（通过sdsdup、sdsnewlen或sdsfromlonglong），因此tmp不可能为NU... |
| 1461 | redis-7.4.2 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1634 | FP | FP | 切片代码显示，在调用`sdsfree(state->lines[linenum])`之前，`linenum`变量未定义，这很可能是一个编译或静态分析工具未能正确解析的上下文。更重要的是，`sdsfree`函数内部已包含对NULL指针的... |
| 1462 | redis-7.4.2 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 切片代码中，告警行`*coalesced = false;`是对指针`coalesced`的写入操作，而非解引用空指针。`coalesced`作为函数参数传入，在函数内部多处被安全赋值，切片内未见其被赋值为NULL或存在空指针解引用路径。 |
| 1463 | redis-7.4.2 | clusterSendPing | Dereference of null pointer | 3650 | FP | FP | 告警点位于条件语句 `if (!link->inbound && type == CLUSTERMSG_TYPE_PING)` 内部，该条件已确保 `link->node` 在解引用前不为空，因为外层存在 `if (link->nod... |
| 1464 | redis-7.4.2 | rb_gen | Dereference of null pointer | 88 | FP | FP | 切片代码仅显示一个宏或函数调用（rb_gen），用于生成数据结构，没有可见的指针解引用操作或空指针变量，因此告警很可能是工具对宏展开的误判。 |
| 1465 | redis-7.4.2 | dictGetVal | Dereference of null pointer | 887 | FP | FP | 函数 `dictGetVal` 接收一个指向 `dictEntry` 的指针 `de`，并直接返回其成员 `v.val`。该函数本身不包含空指针检查，但这是一个简单的访问器函数，其安全性依赖于调用者传入非空指针。在切片代码中，没有证据... |
| 1466 | redis-7.4.2 | dictFind | Dereference of null pointer | 762 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，已经通过 `dictSize(d) == 0` 和 `!dictIsRehashing(d)` 等条件检查了字典状态，并且在循环中 `he` 被赋值后立即... |
| 1467 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12395 | FP | FP | 切片代码显示，在访问 `module->usedby` 等指针成员之前，已经通过 `if (module == NULL)` 检查了指针 `module` 是否为 NULL。只有当 `module` 非 NULL 时，才会执行后续的指... |
| 1468 | redis-7.4.2 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 切片代码中，对指针`next`和`prev`在解引用前都进行了明确的非空检查（`if (next != NULL)`和`if (prev != NULL)`），且告警点位于`*coalesced = true;`，该语句是对`coal... |
| 1469 | redis-7.4.2 | <global> | Dereference of null pointer | 122 | FP | FP | 提供的切片代码仅为函数名或符号，不包含任何实际的指针解引用操作或数据流上下文，无法支持存在空指针解引用逻辑错误的结论。 |
| 1470 | redis-7.4.2 | RM_ListInsert | Dereference of null pointer | 4665 | FP | FP | 切片代码显示，在调用 `listTypeTryConversionAppend` 前，`key` 指针已在 `moduleListIteratorSeek` 函数中进行了有效性检查（`if (!key)`），且告警行本身是函数调用，并... |
| 1471 | redis-7.4.2 | cliInitGroupHelpEntries | Dereference of null pointer | 728 | FP | FP | 切片代码显示 `helpEntries` 数组通过 `pos` 变量索引，该变量初始化为 `helpEntriesLen`，并在循环中递增。切片中未显示 `helpEntries` 的声明或大小，但告警点 `helpEntries[p... |
| 1472 | redis-7.4.2 | cliFillInCommandHelpEntry | Dereference of null pointer | 588 | FP | FP | 切片代码显示，`help->argc` 被赋值为 1 或 2，`zmalloc` 函数在分配失败时会调用 `zmalloc_oom_handler` 处理，不会返回空指针给 `help->argv` 赋值，因此不存在对空指针的解引用。 |
| 1473 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12388 | FP | FP | 切片代码显示，在解引用指针 `*errmsg` 之前，已经对指针 `module` 是否为 NULL 进行了检查。当 `module` 为 NULL 时，代码直接返回错误，不会执行后续可能解引用空指针的代码路径。因此，该告警是误报。 |
| 1474 | redis-7.4.2 | <global> | Dereference of null pointer | 103 | FP | FP | 提供的切片代码仅为变量名，不包含任何指针解引用操作或数据流上下文，无法支持空指针解引用这一逻辑错误的判定，因此视为误报。 |
| 1475 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2559 | FP | FP | 切片代码显示，在调用 dictShrinkIfNeeded 之前，dstzset->dict 已在多个代码路径中被使用（如 dictAdd 和 zsetRemoveFromSkiplist），这表明字典指针已被初始化且有效。此外，函数... |
| 1476 | redis-7.4.2 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查oldp和oldlenp是否为NULL，告警点位于该宏内部，但宏的逻辑确保了不会发生空指针解引用。 |
| 1477 | redis-7.4.2 | xgroupCommand | Dereference of null pointer | 2707 | FP | FP | 在SETID子命令中，当参数为'$'时，代码`id = s->last_id;`仅在`s`不为NULL时执行。切片显示`s`在之前的逻辑中（如CREATE子命令）可能为NULL，但此时会触发`mkstream`选项或返回错误，且SET... |
| 1478 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12391 | FP | FP | 切片代码显示，在访问 `module->types` 之前，已经对指针 `module` 进行了 `NULL` 检查，并且当其为 `NULL` 时，函数会提前设置错误信息并继续执行（未返回）。因此，在后续的 `else if` 分支中... |
| 1479 | redis-7.4.2 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 切片代码显示，在告警行（assert语句）之前，函数已通过条件`if (quicklist->len == 0) return;`确保quicklist非空，因此quicklist->head和quicklist->tail不会为NU... |
| 1480 | redis-7.4.2 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 切片代码显示，在调用 VERIFY_READ 宏之前，并未对 `oldp` 或 `oldlenp` 进行解引用操作。该宏本身包含对指针是否为空的检查，并在条件不满足时跳转返回，因此不会发生空指针解引用。 |
| 1481 | redis-7.4.2 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 切片代码显示，在访问 `ch2token` 数组前，`json->cfg` 指针已在函数开头被解引用并赋值给局部变量 `ch2token`，这表明 `json->cfg` 在进入该函数时已被假定为非空。告警点 `ch2token[ch... |
| 1482 | redis-7.4.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2874 | FP | FP | 切片代码显示，在调用dictExpand(dstzset->dict,...)之前，dstzset已通过dstobj = createZsetObject()被正确初始化，其dict成员由createZsetObject()中的dic... |
| 1483 | redis-7.4.2 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 切片代码显示，在访问 `forward->next` 之前，`forward` 变量在循环中从 `quicklist->head` 开始，并且循环条件 `depth++ < quicklist->compress` 确保了 `forw... |
| 1484 | redis-7.4.2 | _quicklistListpackMerge | Dereference of null pointer | 882 | FP | FP | 切片代码逻辑表明，在调用 `keep->count = lpLength(keep->entry);` 之前，`keep` 指针已被明确赋值（为 `a` 或 `b`），且 `keep->entry` 在 `lpMerge` 成功且 `... |
| 1485 | redis-7.4.2 | moduleFreeContext | Dereference of null pointer | 815 | FP | FP | 切片代码显示，在调用 `zfree(ctx->postponed_arrays)` 之前，已通过 `if (ctx->postponed_arrays)` 检查指针非空，且 `zfree` 函数内部也有 `if (ptr == NUL... |
| 1486 | redis-7.4.2 | rewriteConfigRewriteLine | Dereference of null pointer | 1243 | FP | FP | 在调用`sdsfree(state->lines[linenum])`之前，代码已通过`if (l)`检查确保`l`非空，并通过`listFirst(l)`获取`ln`，且`linenum`来自`ln->value`。切片中`list... |
| 1487 | redis-7.4.2 | raxGenericInsert | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在访问 h->size 之前，h 已被赋值为 child 或 newh，这些值来自 raxAddChild 或 raxCompressNode 等函数，这些函数在失败时返回 NULL 并跳转到 oom 标签，但成功时返回... |
| 1488 | redis-7.4.2 | clusterManagerAddSlots | Dereference of null pointer | 4762 | FP | FP | 切片代码显示，在调用 `freeReplyObject(reply)` 之前，已通过 `if (reply != NULL)` 进行了空指针检查，确保了不会对空指针进行解引用。 |
| 1489 | redis-7.4.2 | min_expand | Dereference of null pointer | 322 | FP | FP | 切片代码显示，在解引用指针 `*s` 之前，已通过条件 `s<ms->src_end` 检查了指针 `s` 的有效性，确保其未越界。该检查逻辑上防止了对空指针或无效地址的解引用，因此告警为误报。 |
| 1490 | redis-7.4.2 | usUntilEarliestTimer | Dereference of null pointer | 257 | FP | FP | 切片代码显示，函数在循环前已检查 `eventLoop->timeEventHead` 是否为 NULL，若为 NULL 则直接返回 -1。循环条件 `while (te)` 保证了只有当链表非空时才会进入循环并寻找 `earlies... |
| 1491 | redis-7.4.2 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | FP | 切片代码显示函数为内联静态函数，其参数`s`在调用前可能已通过其他函数（如`strbuf_init`）确保其`buf`成员非空且长度有效。直接对`s->buf`的索引赋值是此类缓冲区管理函数的常见模式，假定调用者已维护了不变式，因此单... |
| 1492 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12399 | FP | FP | 切片代码显示，在访问 `module->blocked_clients` 之前，已经对指针 `module` 进行了非空检查（`if (module == NULL)`），并且后续的 `else if` 分支仅在 `module` 不... |
| 1493 | redis-7.4.2 | checkMultiPartAof | Dereference of null pointer | 488 | FP | FP | 切片代码显示，在访问 `am->incr_aof_list` 之前，`am` 指针已通过 `aofLoadManifestFromFile` 函数调用返回，且后续代码正常使用了 `am` 并调用了 `aofManifestFree(a... |
| 1494 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12403 | FP | FP | 切片代码显示，在调用 `moduleHoldsTimer(module)` 之前，已经对 `module` 指针进行了非空检查（`if (module == NULL)`），并且后续所有条件判断都位于 `else` 分支中，因此 `m... |
| 1495 | redis-7.4.2 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | 切片代码显示，在调用 `VERIFY_READ(unsigned)` 宏之前，`oldp` 和 `oldlenp` 指针作为函数参数传入，宏内部已对它们是否为 NULL 进行了检查。如果 `oldp` 或 `oldlenp` 为 NU... |
| 1496 | redis-7.4.2 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | 切片代码显示，在调用 VERIFY_READ 宏时，如果 oldp 或 oldlenp 为 NULL，宏内会设置错误码并跳转到 label_return 返回，不会发生空指针解引用。告警点位于宏展开后的条件检查处，该逻辑是安全的。 |
| 1497 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2537 | FP | FP | 切片代码显示，在调用 zslInsert 之前，dstzset 及其成员 zsl 和 dict 已在函数参数中传入，且函数逻辑依赖于它们有效。告警行位于 j == 0 的分支，该分支仅在 dstzset 非空时执行插入操作，且后续的 ... |
| 1498 | redis-7.4.2 | connClose | Dereference of null pointer | 229 | FP | FP | 切片代码显示 `conn` 指针被直接解引用，但这是一个静态内联函数，其调用者应确保传入有效的 `connection` 对象。在典型的连接关闭上下文中，调用此函数前会进行状态检查，且 `conn->type` 在连接建立时已被正确初... |
| 1500 | redis-7.2.1 | zunionInterDiffGenericCommand | Dereference of null pointer | 2818 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，`dstkey` 参数已通过函数签名传入，且 `dstzset` 应来源于 `dstobj`（由 `dstkey` 查找或创建）。告警行位于 `if (dstk... |
| 1501 | redis-7.2.1 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 切片代码显示，函数仅将结构体成员`s->buf`初始化为NULL，这是合法的初始化操作，并未发生对空指针的解引用。告警是对代码意图的误判。 |
| 1502 | redis-7.2.1 | breakstat | Dereference of null pointer | 986 | FP | FP | 切片代码显示，在访问 `bl->nactvar` 之前，`bl` 指针已在 `while` 循环中被更新，且循环条件 `while (bl && !bl->isbreakable)` 确保了只有当 `bl` 非空时才会进入循环体。因此... |
| 1503 | redis-7.2.1 | xgroupCommand | Dereference of null pointer | 2697 | FP | FP | 在SETID子命令分支中，cg指针的使用前有明确的流查找和消费者组查找逻辑，切片中未显示cg可能为NULL的路径。告警点'cg->last_id = id;'前，代码已通过streamCreateCG或查找确保了cg的有效性，因此解引... |
| 1504 | redis-7.2.1 | zdiffAlgorithm1 | Dereference of null pointer | 2432 | FP | FP | 切片代码显示，在调用zslInsert之前，tmp变量由zuiNewSdsFromValue函数返回，该函数总是返回一个有效的sds字符串或新分配的sds，不会返回NULL。因此，传递给zslInsert的ele参数不会是空指针，不存... |
| 1505 | redis-7.2.1 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1643 | FP | FP | 切片代码显示，在调用`sdsfree(state->lines[linenum])`之前，`state->lines`数组的访问依赖于`linenum`变量，但该变量在切片中未定义或初始化，这很可能是静态分析工具未能正确追踪变量来源导... |
| 1506 | redis-7.2.1 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 切片代码显示告警行是对布尔变量`*coalesced`的赋值操作，`coalesced`是一个传入的非空指针参数，不存在解引用空指针的逻辑。告警点之前的循环和条件判断中也未对`coalesced`进行可能使其为空的修改。 |
| 1507 | redis-7.2.1 | rb_gen | Dereference of null pointer | 88 | FP | FP | 切片代码仅显示一个宏或函数调用，用于生成红黑树结构，没有可见的指针解引用操作。该告警可能源于静态分析工具对宏展开或内部实现的误判，在提供的切片上下文中不存在明确的空指针解引用逻辑错误。 |
| 1508 | redis-7.2.1 | dictGetVal | Dereference of null pointer | 805 | FP | FP | 函数 `dictGetVal` 的参数 `de` 是一个指向 `dictEntry` 的指针，但切片代码中未提供其调用上下文。该函数本身只是解引用指针成员，假设调用者会传入有效的指针。在没有证据表明调用者会传入 NULL 的情况下，这... |
| 1509 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12227 | FP | FP | 告警指向的代码行是字符串字面量赋值给指针，并非解引用空指针。切片代码显示，在解引用 `errmsg` 指针之前，函数已通过多个条件检查确保 `module` 指针非空，且 `errmsg` 是函数的输入参数，其有效性由调用者保证。 |
| 1510 | redis-7.2.1 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 切片代码中，对指针`next`和`prev`在解引用前都进行了明确的非空检查（`if (next != NULL)`和`if (prev != NULL)`），逻辑上避免了空指针解引用。告警点所在行（`*coalesced = tru... |
| 1511 | redis-7.2.1 | <global> | Dereference of null pointer | 122 | FP | FP | 提供的切片代码仅为函数名或符号，不包含任何实际的指针解引用操作或数据流上下文，无法支持存在空指针解引用逻辑错误的结论。 |
| 1512 | redis-7.2.1 | RM_ListInsert | Dereference of null pointer | 4585 | FP | FP | 切片代码显示，在调用 `listTypeTryConversionAppend` 之前，`key` 指针已在 `moduleListIteratorSeek` 函数中进行了有效性检查（`if (!key)` 和 `if (!key->... |
| 1513 | redis-7.2.1 | cliInitGroupHelpEntries | Dereference of null pointer | 724 | FP | FP | 切片代码显示，`helpEntries` 数组的索引 `pos` 从静态变量 `helpEntriesLen` 初始化，并在循环中递增。虽然切片未显示 `helpEntries` 的声明和大小，但告警行是向数组赋值，而非解引用指针。工... |
| 1514 | redis-7.2.1 | cliFillInCommandHelpEntry | Dereference of null pointer | 584 | FP | FP | 切片代码显示，`help->argc` 被赋值为 1 或 2，`zmalloc` 函数在分配失败时会调用 `zmalloc_oom_handler` 处理，不会返回空指针给 `help->argv` 赋值，因此不存在对空指针的解引用。 |
| 1515 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12220 | FP | FP | 切片代码显示，在解引用指针 `errmsg` 之前，函数 `moduleUnload` 已通过 `if (module == NULL)` 检查了指针 `module` 是否为 NULL，并仅在 `module` 不为 NULL 时才... |
| 1516 | redis-7.2.1 | <global> | Dereference of null pointer | 103 | FP | FP | 提供的切片代码仅为变量名 `prof_gctx_comp)`，不包含任何指针解引用操作或相关数据流，无法支持存在空指针解引用逻辑错误的结论。 |
| 1517 | redis-7.2.1 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | 告警指向的 `VERIFY_READ` 宏在解引用 `oldlenp` 前已检查其是否为 NULL，且 `READONLY` 宏确保了 `newp` 和 `newlen` 的合法性，切片代码中未见空指针解引用路径。 |
| 1518 | redis-7.2.1 | xgroupCommand | Dereference of null pointer | 2693 | FP | FP | 在SETID子命令中，当参数为'$'时，代码`id = s->last_id;`仅在`s`不为NULL时执行。切片显示`s`在之前的逻辑中可能为NULL，但该分支仅在`!strcasecmp(opt,"SETID") && (c->a... |
| 1519 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12223 | FP | FP | 切片代码显示，在访问 `module->types` 之前，已经对指针 `module` 进行了 `NULL` 检查。只有当 `module` 不为 `NULL` 时，才会执行后续的 `listLength(module->types... |
| 1520 | redis-7.2.1 | __quicklistCompress | Dereference of null pointer | 313 | FP | FP | 切片代码显示，在调用assert语句前，函数已通过`if (quicklist->len == 0) return;`确保quicklist非空，且assert语句本身用于验证内部状态，其条件失败将导致程序终止而非空指针解引用。因此，... |
| 1521 | redis-7.2.1 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 切片代码显示，在调用 VERIFY_READ 宏之前，告警点所在的函数参数 `oldp` 和 `oldlenp` 并未被解引用。VERIFY_READ 宏本身会检查这些指针是否为 NULL，并在为 NULL 时设置错误码并跳转返回，因... |
| 1522 | redis-7.2.1 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 切片代码显示，在访问 `ch2token` 数组前，`json->cfg` 指针的合法性已在函数外部或调用上下文中得到保证，且告警行 `token->type = ch2token[ch];` 中的数组索引 `ch` 是经过类型转换的... |
| 1523 | redis-7.2.1 | zunionInterDiffGenericCommand | Dereference of null pointer | 2801 | FP | FP | 切片代码显示，在调用dictExpand(dstzset->dict,...)之前，dstzset已通过createZsetObject()初始化，其dict成员由dictCreate(&zsetDictType)创建，因此dstzs... |
| 1524 | redis-7.2.1 | __quicklistCompress | Dereference of null pointer | 366 | FP | FP | 切片代码显示，在访问`forward->next`和`reverse->prev`的循环之前，`forward`和`reverse`指针分别被初始化为`quicklist->head`和`quicklist->tail`，并且函数开头... |
| 1525 | redis-7.2.1 | _quicklistListpackMerge | Dereference of null pointer | 827 | FP | FP | 切片代码逻辑表明，在调用 `keep->count = lpLength(keep->entry);` 之前，`keep` 指针被赋值为 `a` 或 `b`，而 `a` 和 `b` 的 `entry` 字段在 `lpMerge` 调用... |
| 1526 | redis-7.2.1 | moduleFreeContext | Dereference of null pointer | 816 | FP | FP | 切片代码显示，在调用 `zfree(ctx->postponed_arrays)` 之前，已通过 `if (ctx->postponed_arrays)` 检查指针非空，因此不会发生空指针解引用。 |
| 1527 | redis-7.2.1 | rewriteConfigRewriteLine | Dereference of null pointer | 1252 | FP | FP | 切片代码显示，在调用 `sdsfree(state->lines[linenum])` 之前，已经通过 `if (l)` 检查了指针 `l` 非空，并且 `ln` 是通过 `listFirst(l)` 从非空列表 `l` 中获取的，因... |
| 1528 | redis-7.2.1 | zsetRemoveFromSkiplist | Dereference of null pointer | 1502 | FP | FP | 切片代码显示，在调用 dictGetVal(de) 之前，已经通过 'if (de != NULL)' 检查了指针 de 不为空，因此不会发生空指针解引用。 |
| 1529 | redis-7.2.1 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 切片代码显示，在警告行（h->size == 0）之前，h 指针已在循环中通过 `h = child;` 赋值，且 `child` 由 `raxAddChild` 或 `raxCompressNode` 返回，这些函数在失败时返回 N... |
| 1530 | redis-7.2.1 | clusterManagerAddSlots | Dereference of null pointer | 4641 | FP | FP | 切片代码显示，在调用 `freeReplyObject(reply)` 之前，已通过 `if (reply != NULL)` 进行了空指针检查，确保了不会对空指针进行解引用。 |
| 1531 | redis-7.2.1 | min_expand | Dereference of null pointer | 322 | FP | FP | 在切片代码中，对指针 `s` 的解引用发生在条件 `s<ms->src_end` 之后，该条件已确保 `s` 指向有效内存范围，因此不会发生空指针解引用。 |
| 1532 | redis-7.2.1 | usUntilEarliestTimer | Dereference of null pointer | 276 | FP | FP | 切片代码显示，函数在进入循环前已检查 `eventLoop->timeEventHead` 是否为 NULL，若为 NULL 则直接返回 -1。循环条件 `while (te)` 保证了 `earliest` 指针在循环中被赋值后才可... |
| 1533 | redis-7.2.1 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | FP | 切片代码显示函数为内联静态函数，其参数`s`在调用前可能已通过其他函数（如`strbuf_init`）确保其`buf`成员非空且`length`有效。直接对`s->buf`进行索引赋值是安全的常见模式，未见明显的空指针解引用逻辑错误。 |
| 1534 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12231 | FP | FP | 切片代码显示，在访问 `module->blocked_clients` 之前，已经通过 `if (module == NULL)` 检查了指针 `module` 是否为 NULL，并且在该检查失败后直接返回了错误信息。因此，当执行到... |
| 1535 | redis-7.2.1 | checkMultiPartAof | Dereference of null pointer | 478 | FP | FP | 切片代码显示，在访问 `am->incr_aof_list` 之前，函数 `aofLoadManifestFromFile` 已被调用并返回 `am` 指针，且后续代码正常使用了 `am` 并调用了 `aofManifestFree(... |
| 1536 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12235 | FP | FP | 切片代码显示，在调用 `moduleHoldsTimer(module)` 之前，已经对指针 `module` 进行了非空检查，并且所有返回路径都确保了 `module` 不为空。因此，在告警点解引用 `module` 时，它不可能为... |
| 1537 | redis-7.2.1 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | 切片代码显示，在调用 `VERIFY_READ(unsigned)` 宏之前，`oldp` 和 `oldlenp` 指针作为函数参数传入，宏内部已对它们进行了空指针检查。如果 `oldp` 或 `oldlenp` 为 NULL，宏会设... |
| 1538 | redis-7.2.1 | zdiffAlgorithm2 | Dereference of null pointer | 2492 | FP | FP | 切片代码显示，在调用 `htNeedsResize(dstzset->dict)` 之前，`dstzset` 及其 `dict` 字段已在函数中被正确初始化和使用（例如通过 `dictAdd` 和 `zsetRemoveFromSki... |
| 1539 | redis-7.2.1 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | 切片代码显示，在调用 `VERIFY_READ(unsigned)` 宏之前，`oldp` 和 `oldlenp` 指针已在函数参数中传入，宏内部会检查它们是否为 NULL 或长度不匹配，并在条件不满足时通过 `goto label_... |
| 1540 | redis-7.2.1 | zdiffAlgorithm2 | Dereference of null pointer | 2472 | FP | FP | 切片代码显示，在调用 zslInsert 之前，zuiNext 函数会检查迭代器状态并返回 0 表示结束，且 zuiInitIterator 会处理空 subject 的情况，这确保了传入 zslInsert 的参数是有效的。此外，d... |
| 1542 | redis-7.2.5 | zunionInterDiffGenericCommand | Dereference of null pointer | 2819 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，`dstkey` 和 `dstzset` 的初始化及有效性检查逻辑未包含在切片中，但告警行位于 `if (dstkey)` 条件块内，且 `dstzset` 应... |
| 1543 | redis-7.2.5 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 切片代码显示，函数`strbuf_init`仅将结构体成员`s->buf`初始化为NULL，这是对指针变量的合法赋值操作，并非对空指针的解引用。告警是对代码逻辑的误判。 |
| 1544 | redis-7.2.5 | breakstat | Dereference of null pointer | 986 | FP | FP | 切片代码显示，在访问 `bl->nactvar` 之前，`bl` 指针已在 `while` 循环中被更新，且循环条件 `while (bl && !bl->isbreakable)` 确保了只有当 `bl` 非空时才会进入循环体。因此... |
| 1545 | redis-7.2.5 | xgroupCommand | Dereference of null pointer | 2697 | FP | FP | 在SETID子命令分支中，cg指针的使用位于`s`指针非空的条件下（`id = s->last_id;`），且该分支仅在`s`非空时才会执行，切片中未见cg在解引用前可能为空的明确路径。 |
| 1546 | redis-7.2.5 | zdiffAlgorithm1 | Dereference of null pointer | 2433 | FP | FP | 切片代码显示，在调用 `zslInsert` 前，`tmp` 变量由 `zuiNewSdsFromValue` 返回，该函数保证返回一个有效的 sds 字符串或新分配的 sds，不会返回 NULL。因此，传递给 `zslInsert`... |
| 1547 | redis-7.2.5 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1643 | FP | FP | 切片代码显示，在调用 `sdsfree(state->lines[linenum])` 之前，`state->lines[linenum]` 已通过 `listFirst(l)` 和 `dictGetVal(de)` 等操作获取，这些... |
| 1548 | redis-7.2.5 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用指针 `coalesced` 之前，函数已通过 `assert` 确保 `edata` 非守卫状态，且 `coalesced` 是传入的布尔指针参数，其有效性由调用者保证。在告警行 `*coalesced = f... |
| 1549 | redis-7.2.5 | rb_gen | Dereference of null pointer | 88 | FP | FP | 切片代码显示该行是宏定义或函数声明，并未包含任何实际的指针解引用操作，因此不存在空指针解引用的逻辑错误。 |
| 1550 | redis-7.2.5 | dictGetVal | Dereference of null pointer | 805 | FP | FP | 函数 `dictGetVal` 接收一个指向 `dictEntry` 的指针 `de`，并直接返回其成员 `v.val`。该函数本身不包含空指针检查，但这是一个简单的访问器函数，其安全性依赖于调用者传入非空指针。切片代码中未显示调用上... |
| 1551 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12235 | FP | FP | 切片代码显示，在访问 `module->usedby` 等指针成员之前，已经通过 `if (module == NULL)` 检查了指针 `module` 是否为 NULL，并设置了错误消息。因此，后续的指针解引用是在确认指针非空后进... |
| 1552 | redis-7.2.5 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 切片代码中，对指针`next`和`prev`在解引用前都进行了明确的非空检查（`if (next != NULL)`和`if (prev != NULL)`），逻辑上避免了空指针解引用。告警点位于`*coalesced = true;... |
| 1553 | redis-7.2.5 | <global> | Dereference of null pointer | 122 | FP | FP | 提供的切片代码仅为函数名 `prof_tdata_comp`，不包含任何指针解引用操作或相关数据流，无法支持存在空指针解引用错误的结论。 |
| 1554 | redis-7.2.5 | RM_ListInsert | Dereference of null pointer | 4585 | FP | FP | 切片代码显示，在调用 `listTypeTryConversionAppend` 前，`key` 指针已在 `moduleListIteratorSeek` 函数中进行了有效性检查（`if (!key)`），且该函数在调用前被检查了返... |
| 1555 | redis-7.2.5 | cliInitGroupHelpEntries | Dereference of null pointer | 724 | FP | FP | 切片代码显示 `helpEntries` 数组通过 `pos` 变量索引，该变量初始化为 `helpEntriesLen`，并在循环中递增。虽然未直接显示 `helpEntries` 的声明和大小，但告警行 `helpEntries[... |
| 1556 | redis-7.2.5 | cliFillInCommandHelpEntry | Dereference of null pointer | 584 | FP | FP | 切片代码显示，在解引用指针 `help` 之前，函数 `cliFillInCommandHelpEntry` 的调用上下文未提供，无法确认 `help` 是否为 null。该告警点是对 `help->argc` 的赋值，但 `help... |
| 1557 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12228 | FP | FP | 切片代码显示，在解引用指针 `errmsg` 之前，已经通过 `if (module == NULL)` 检查了 `module` 指针。当 `module` 为 NULL 时，代码直接返回错误，不会执行后续可能解引用 `module... |
| 1558 | redis-7.2.5 | <global> | Dereference of null pointer | 103 | FP | FP | 提供的切片代码仅为变量名或函数名片段，不包含任何可分析的赋值、条件判断或解引用操作，无法支持空指针解引用的告警。基于可见信息，该告警无效。 |
| 1559 | redis-7.2.5 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | 切片代码显示，在调用 `tcaches_create` 函数前，`VERIFY_READ` 宏已对 `oldp` 和 `oldlenp` 指针进行了非空验证，若为空则直接返回错误，因此不会发生空指针解引用。 |
| 1560 | redis-7.2.5 | xgroupCommand | Dereference of null pointer | 2693 | FP | FP | 在SETID子命令分支中，对`s`指针的访问发生在`s`被赋值的代码块之后，且切片代码显示`s`可能为NULL的情况已在CREATE子命令分支中通过`mkstream`选项和`serverAssert`进行了处理，因此`s`在访问时不... |
| 1561 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12231 | FP | FP | 切片代码显示，在访问 `module->types` 之前，已经通过 `if (module == NULL)` 检查了指针 `module` 是否为空。如果为空，函数会提前设置错误信息并继续执行，但后续的 `else if` 条件仅... |
| 1562 | redis-7.2.5 | __quicklistCompress | Dereference of null pointer | 316 | FP | FP | 切片代码显示，在调用assert语句前，函数已通过条件`if (quicklist->len == 0) return;`确保quicklist非空，且assert语句本身用于验证内部不变条件，其失败将导致程序终止而非空指针解引用。因... |
| 1563 | redis-7.2.5 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警指向的 `VERIFY_READ` 宏在 `oldp` 或 `oldlenp` 为空时会设置错误码并跳转返回，不会发生空指针解引用。切片代码中的控制流逻辑确保了安全性。 |
| 1564 | redis-7.2.5 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 切片代码显示，在访问 `ch2token` 数组前，`json->cfg` 指针的合法性已在函数外部或调用路径中得到保证，且 `ch2token` 是 `json->cfg` 的一个固定成员数组，其访问索引 `ch` 是经过类型转换的... |
| 1565 | redis-7.2.5 | zunionInterDiffGenericCommand | Dereference of null pointer | 2802 | FP | FP | 切片代码显示，在调用 dictExpand(dstzset->dict, dictSize(accumulator)) 之前，dstzset 已在条件分支 `if (!cardinality_only)` 中通过 `dstobj = ... |
| 1566 | redis-7.2.5 | __quicklistCompress | Dereference of null pointer | 369 | FP | FP | 切片代码显示，在访问 `forward->next` 之前，`forward` 指针已通过 `quicklist->head` 初始化，且函数开头有 `assert` 确保 `quicklist->head` 和 `quicklist... |
| 1567 | redis-7.2.5 | _quicklistListpackMerge | Dereference of null pointer | 869 | FP | FP | 切片代码逻辑表明，在调用 `keep->count = lpLength(keep->entry);` 之前，`keep` 指针的赋值经过了条件判断，确保它指向 `a` 或 `b` 中 `entry` 不为空的那个节点，因此 `kee... |
| 1568 | redis-7.2.5 | moduleFreeContext | Dereference of null pointer | 816 | FP | FP | 切片代码显示，在调用 `zfree(ctx->postponed_arrays)` 之前，已通过 `if (ctx->postponed_arrays)` 检查了指针非空，因此不会发生空指针解引用。 |
| 1569 | redis-7.2.5 | rewriteConfigRewriteLine | Dereference of null pointer | 1252 | FP | FP | 在调用 `sdsfree(state->lines[linenum])` 之前，代码已通过 `if (l)` 检查确保 `l` 非空，并通过 `listFirst(l)` 获取 `ln`，且 `linenum` 是从 `ln->val... |
| 1570 | redis-7.2.5 | zsetRemoveFromSkiplist | Dereference of null pointer | 1503 | FP | FP | 切片代码显示，在调用 dictGetVal(de) 之前，已经通过 'if (de != NULL)' 检查了指针 de 不为空，因此不会发生空指针解引用。 |
| 1571 | redis-7.2.5 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 切片代码显示，在警告行（h->size == 0）之前，h 已通过 child = raxNewNode(0,0) 分配并赋值给 h，且未在切片中看到任何将 h 置为 NULL 的路径。因此，h 不可能为 NULL，解引用是安全的。 |
| 1572 | redis-7.2.5 | clusterManagerAddSlots | Dereference of null pointer | 4642 | FP | FP | 切片代码显示，在调用 `freeReplyObject(reply)` 之前，已通过 `if (reply != NULL)` 进行了空指针检查，确保了不会对空指针进行解引用。 |
| 1573 | redis-7.2.5 | min_expand | Dereference of null pointer | 322 | FP | FP | 切片代码显示，在解引用指针 `*s` 之前，已通过条件 `s<ms->src_end` 检查了指针 `s` 的有效性，确保其未越界。该检查逻辑上防止了对空指针或无效地址的解引用，因此告警为误报。 |
| 1574 | redis-7.2.5 | usUntilEarliestTimer | Dereference of null pointer | 276 | FP | FP | 切片代码显示，函数在遍历链表前已检查 `eventLoop->timeEventHead` 是否为 NULL，若为 NULL 则直接返回 -1。后续循环中 `earliest` 指针仅在满足条件（`te->id != AE_DELET... |
| 1575 | redis-7.2.5 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | FP | 切片代码显示函数为内联静态函数，仅对结构体指针`s`进行操作。在调用此函数前，调用方必须确保`s`和`s->buf`已正确分配且`s->length`在有效范围内，否则程序已处于未定义状态。该告警是对一个封装好的、假设前置条件已满足的... |
| 1576 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12239 | FP | FP | 切片代码显示，在访问 `module->blocked_clients` 之前，已经通过 `if (module == NULL)` 检查了指针 `module` 是否为 NULL。如果 `module` 为 NULL，函数会提前设置... |
| 1577 | redis-7.2.5 | checkMultiPartAof | Dereference of null pointer | 486 | FP | FP | 切片代码显示，在访问 `am->incr_aof_list` 之前，函数 `aofLoadManifestFromFile` 已被调用并返回 `am`，且没有对 `am` 进行空指针检查。然而，在告警行 `if (listLength... |
| 1578 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12243 | FP | FP | 切片代码显示，在调用 `moduleHoldsTimer(module)` 之前，已经对指针 `module` 进行了非空检查，并且所有 `else if` 分支都依赖于 `module` 不为 NULL 的前提，因此不会发生空指针解引用。 |
| 1579 | redis-7.2.5 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | 切片代码显示，在调用VERIFY_READ宏时，若oldp或oldlenp为NULL，宏内会设置错误码并跳转到label_return，从而避免了空指针解引用。告警点位于宏展开后的条件检查处，该逻辑是安全的。 |
| 1580 | redis-7.2.5 | zdiffAlgorithm2 | Dereference of null pointer | 2493 | FP | FP | 切片代码显示，在调用 `htNeedsResize(dstzset->dict)` 之前，`dstzset` 及其 `dict` 字段已在函数中被初始化和使用（例如通过 `dictAdd` 和 `zsetRemoveFromSkipl... |
| 1581 | redis-7.2.5 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | 切片代码显示，在告警行`VERIFY_READ(unsigned);`之前，`oldlenp`指针已在宏定义中被解引用，但该宏包含前置检查`if (oldp == NULL ｜｜ oldlenp == NULL ｜｜ *oldlenp... |
| 1582 | redis-7.2.5 | zdiffAlgorithm2 | Dereference of null pointer | 2473 | FP | FP | 切片代码显示，在调用 zslInsert 之前，dstzset 指针及其成员 zsl 和 dict 已在函数参数中传入，且后续操作（如 dictAdd、zsetRemoveFromSkiplist）均直接使用这些指针，表明它们已被正确... |
| 1584 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12586 | FP | FP | 切片代码显示，在访问 `module->loadmod->path` 之前，已经检查了 `module` 指针不为 NULL。`sdslen` 函数内部对 `s` 参数的访问是安全的，因为 `module->loadmod->path... |
| 1585 | redis-8.0.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2871 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，`dstkey` 参数已通过 `if (dstkey)` 进行了非空检查，确保了 `dstzset` 指针的有效性，因此不会发生空指针解引用。 |
| 1588 | redis-8.0.2 | xgroupCommand | Dereference of null pointer | 2730 | FP | FP | 在SETID子命令分支中，cg指针仅在s（stream）不为NULL时才会被赋值（通过streamCreateCG函数），而该分支的代码逻辑表明，当执行到cg->last_id = id;时，cg必然已被成功创建或查找，不会为NULL... |
| 1589 | redis-8.0.2 | exprTokenToNum | Dereference of null pointer | 688 | FP | FP | 切片代码显示，在访问指针 t 的成员 token_type 之前，函数已通过参数接收指针，但函数内部没有对 t 进行空指针检查。然而，该告警点位于条件判断 `if (t->token_type == ...)` 中，这本身是安全的，因... |
| 1590 | redis-8.0.2 | dictGenericDelete | Dereference of null pointer | 661 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，函数已通过 `dictSize(d) == 0` 检查确保字典非空，并通过 `_dictRehashStepIfNeeded` 处理了可能的rehash状... |
| 1591 | redis-8.0.2 | zdiffAlgorithm1 | Dereference of null pointer | 2494 | FP | FP | 切片代码显示，在调用 zslInsert 前，tmp 变量由 zuiNewSdsFromValue 返回，该函数总是返回一个有效的 sds 字符串或新分配的 sds，不会返回 NULL。因此，传递给 zslInsert 的 ele 参... |
| 1592 | redis-8.0.2 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1645 | FP | FP | 切片代码显示，在调用`sdsfree(state->lines[linenum])`之前，`state->lines`数组的访问依赖于`linenum`变量，但该变量在切片中未定义或初始化，这很可能是一个局部变量或参数，其值在切片外被... |
| 1593 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12578 | FP | FP | 切片代码显示，在访问 `module->loadmod->path` 之前，已经对指针 `module` 进行了空值检查（`if (module == NULL)`），并且当其为空时，函数已通过设置错误信息并继续执行（未返回）来处理。... |
| 1595 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12571 | FP | FP | 在切片代码中，对指针 `module` 的访问（如 `module->loadmod->path`）都位于 `if (module == NULL)` 检查之后，并且仅在 `module` 不为 NULL 的分支中执行。因此，不存在对... |
| 1596 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12568 | FP | FP | 切片代码显示，在解引用 `module->loadmod->path` 之前，已经通过 `if (module == NULL)` 检查了指针 `module` 不为空。只有当 `module` 非空时，才会执行到解引用 `modul... |
| 1597 | redis-8.0.2 | clusterSendPing | Dereference of null pointer | 3670 | FP | FP | 切片代码显示，在访问 `link->node->ping_sent` 之前，存在条件 `if (!link->inbound && type == CLUSTERMSG_TYPE_PING)`，这确保了 `link->node` 在解... |
| 1599 | redis-8.0.2 | dictGetVal | Dereference of null pointer | 937 | FP | FP | 函数`dictGetVal`接收一个指向`dictEntry`的指针`de`，并直接返回其成员`v.val`。该函数本身不包含空指针检查，但这是一个简单的访问器函数，其安全性依赖于调用者传入非空指针。在切片代码中，没有证据表明`de`... |
| 1600 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12582 | FP | FP | 切片代码显示，在访问 `module->loadmod->path` 之前，已对指针 `module` 进行了空值检查（`if (module == NULL)`），并且该访问位于 `else if` 分支中，仅在 `module` ... |
| 1603 | redis-8.0.2 | RM_ListInsert | Dereference of null pointer | 4704 | FP | FP | 切片代码显示，在调用 `listTypeTryConversionAppend` 前，`key->value` 的访问发生在 `moduleListIteratorSeek` 函数内部，该函数已对 `key` 和 `key->valu... |
| 1604 | redis-8.0.2 | cliInitGroupHelpEntries | Dereference of null pointer | 729 | FP | FP | 切片代码显示 `helpEntries` 数组通过 `pos` 变量进行索引，该变量初始化为 `helpEntriesLen` 并随循环递增。未发现对 `helpEntries` 数组边界或空指针的检查，但告警点 `helpEntri... |
| 1605 | redis-8.0.2 | cliFillInCommandHelpEntry | Dereference of null pointer | 589 | FP | FP | 切片代码显示，`help->argc` 被赋值为1或2，然后作为参数传递给 `zmalloc`。`zmalloc` 函数内部有内存分配失败的处理（调用 `zmalloc_oom_handler`），并且会返回一个指针。在切片可见范围内... |
| 1607 | redis-8.0.2 | zdiffAlgorithm2 | Dereference of null pointer | 2556 | FP | FP | 切片代码显示，在调用 dictShrinkIfNeeded 之前，dstzset->dict 已在多个路径中被使用（如 dictAdd 和 zsetRemoveFromSkiplist），表明该指针已被正确初始化且非空。工具可能因无法... |
| 1609 | redis-8.0.2 | xgroupCommand | Dereference of null pointer | 2726 | FP | FP | 在SETID子命令中，当argv[4]为'$'时，访问s->last_id。切片显示，当s为NULL时，仅当mkstream为1且命令为CREATE时才会创建流对象。对于SETID命令，s可能为NULL，但切片中未显示在访问s->la... |
| 1610 | redis-8.0.2 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 切片代码显示，在调用`assert`之前，函数已通过`if (quicklist->len == 0) return;`确保链表非空，因此`quicklist->head`和`quicklist->tail`不应为空指针。该断言是对已... |
| 1611 | redis-8.0.2 | exprTokensEqual | Dereference of null pointer | 717 | FP | FP | 函数 `exprTokensEqual` 在访问指针 `a` 和 `b` 的成员 `token_type` 之前，没有对指针本身进行空值检查。然而，根据切片代码中 `exprTokenToNum` 函数的实现，该函数同样直接访问了指针... |
| 1614 | redis-8.0.2 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 切片代码显示，在访问 `forward->next` 之前，`forward` 指针已通过 `quicklistDecompressNode` 宏进行检查，该宏包含 `if ((_node) && ...)` 的非空判断，且循环条件 ... |
| 1615 | redis-8.0.2 | _quicklistListpackMerge | Dereference of null pointer | 882 | FP | FP | 切片代码逻辑表明，在调用 `keep->count = lpLength(keep->entry);` 之前，`keep` 指针被赋值为 `a` 或 `b`，而 `a` 和 `b` 是函数参数，非空。同时，`keep` 的赋值条件 `... |
| 1616 | redis-8.0.2 | moduleFreeContext | Dereference of null pointer | 827 | FP | FP | 切片代码显示，在调用 `zfree(ctx->postponed_arrays)` 之前，已通过 `if (ctx->postponed_arrays)` 检查指针非空，且 `zfree` 函数内部也有 `if (ptr == NUL... |
| 1617 | redis-8.0.2 | rewriteConfigRewriteLine | Dereference of null pointer | 1251 | FP | FP | 切片代码显示，在调用 `sdsfree(state->lines[linenum])` 之前，`linenum` 是从 `ln->value` 获取的，而 `ln` 是 `listFirst(l)` 的返回值，仅在 `l` 非空时执行... |
| 1618 | redis-8.0.2 | raxGenericInsert | Dereference of null pointer | 870 | FP | FP | 切片代码显示，在警告行（h->size == 0）之前，h 已被赋值为 child 指针，且 child 在 raxAddChild 或 raxCompressNode 中已分配并检查了空指针。因此，h 不可能为空，解引用是安全的。 |
| 1619 | redis-8.0.2 | clusterManagerAddSlots | Dereference of null pointer | 4769 | FP | FP | 切片代码显示，在调用 `clusterManagerCheckRedisReply` 函数前，`err` 指针已被显式初始化为 `NULL`。该函数内部对 `err` 参数进行了 `NULL` 检查，仅在 `err != NULL` ... |
| 1621 | redis-8.0.2 | usUntilEarliestTimer | Dereference of null pointer | 275 | FP | FP | 切片代码显示，函数入口处已检查 `eventLoop->timeEventHead` 是否为 NULL，并在为 NULL 时直接返回 -1。后续循环中，`earliest` 指针仅在 `te->id != AE_DELETED_EVE... |
| 1623 | redis-8.0.2 | checkMultiPartAof | Dereference of null pointer | 488 | FP | FP | 切片代码显示，在访问 `am->incr_aof_list` 之前，`am` 指针已通过 `aofLoadManifestFromFile` 函数调用返回，且后续代码未对其进行空值检查。然而，该函数调用后没有立即检查 `am` 是否为... |
| 1624 | redis-8.0.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2813 | FP | FP | 切片代码显示，在调用 dictExpand(dstzset->dict, ...) 之前，存在条件判断 `if (!cardinality_only)` 和 `if (setnum)`，并且 `dstzset` 在 `!cardina... |
| 1627 | redis-8.0.2 | zdiffAlgorithm2 | Dereference of null pointer | 2534 | FP | FP | 切片代码显示，在调用 `zslInsert` 前，`dstzset->zsl` 和 `dstzset->dict` 作为参数传入函数，其有效性由调用者保证。在 `zslInsert` 函数内部，`zsl->header` 被直接解引用... |
| 1628 | redis-8.0.2 | exprTokenToBool | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `t->token_type` 之前，函数 `exprTokenToBool` 没有对指针 `t` 进行空值检查。然而，该函数是一个内部辅助函数，其调用上下文（未在切片中显示）很可能保证了传入的指针非空。直接判定... |
| 1629 | redis-8.0.2 | connClose | Dereference of null pointer | 235 | FP | FP | 切片代码显示 `conn` 指针被直接解引用，但这是一个静态内联函数，其调用上下文（如对 `conn` 是否为空的检查）未包含在切片内。基于常见编程实践，此类连接关闭函数通常在被调用前已对指针有效性进行了检查，因此倾向于判定为误报。 |
| 1631 | ffmpeg-7.1.1 | show_bits | Dereference of null pointer | 376 | FP | FP | 切片代码仅展示了宏定义和函数框架，未显示对指针's'进行解引用的具体操作或明确的空指针传递路径。告警指向的宏UPDATE_CACHE在定义中未直接解引用参数，且缺乏上下文证明's'为null，因此判定为工具误报。 |
| 1632 | ffmpeg-7.1.1 | finalize_packet | Dereference of null pointer | 678 | FP | FP | 切片代码中，在告警行`s->st->time_base.den`被访问前，已存在对`s->st`的间接访问`s->st->time_base.num`，且`s->st`作为结构体指针在函数上下文中被使用，表明其已被初始化且非空。工具可... |
| 1633 | ffmpeg-7.1.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 413 | FP | FP | 切片代码显示，在访问 `ctx->buffers[buf.index]` 之前，`buf.index` 的值来自 `ioctl` 系统调用 `VIDIOC_DQBUF` 的成功返回，该操作由驱动管理，应保证索引在有效范围内。同时，`c... |
| 1634 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 299 | FP | FP | 切片代码显示，在调用 `encode_line` 函数前，`src` 指针作为参数传入，并在循环中被用于计算地址和读取数据，没有证据表明 `src` 为 NULL。告警点 `((uint16_t*)(src + stride*y))[... |
| 1635 | ffmpeg-7.1.1 | roq_dpcm_encode_frame | Dereference of null pointer | 180 | FP | FP | 在告警行访问 `frame->pts` 之前，切片代码已通过 `if (!in && context->input_frames >= 8)` 和 `if (in && context->input_frames < 8)` 等条件确... |
| 1636 | ffmpeg-7.1.1 | ebml_read_binary | Dereference of null pointer | 1095 | FP | FP | 切片代码显示，在调用`memset`之前，`av_buffer_realloc`函数已被调用并成功返回（`ret < 0`时函数已提前返回），这确保了`bin->buf`及其`data`字段不为空，因此对`bin->buf->data... |
| 1637 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 209 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回 `AVERROR(ENOMEM)`，因此 `ptr2` 在解引用时不为空。 |
| 1638 | ffmpeg-7.1.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | FP | 切片代码显示，指针 `dc_val` 作为参数传递给函数 `ff_vc1_pred_dc`，该函数预期会将其设置为一个有效的地址。在调用后立即进行解引用赋值 `*dc_val = dcdiff;`，这表明在正常的程序流程中，`dc_v... |
| 1639 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 切片代码显示，在访问 `in->data[plane]` 之前，`in` 帧作为函数参数传入且未被修改，其有效性由调用者保证。此外，`out` 帧在可能为 NULL 时通过 `ff_get_video_buffer` 分配，后续对 `... |
| 1640 | ffmpeg-7.1.1 | unsharp_slice_16 | Dereference of null pointer | 172 | FP | FP | 切片代码中，宏定义 `DEF_UNSHARP_SLICE_FUNC` 展开后，告警点 `{ NULL }` 是函数体的一部分，但该函数体在宏展开后已被完整的代码逻辑所替代，不存在空指针解引用。告警可能是工具对宏展开的误解析。 |
| 1641 | ffmpeg-7.1.1 | ebml_parse | Dereference of null pointer | 1363 | FP | FP | 切片代码中，在访问 `level->length` 之前，已通过 `if (matroska->num_levels > 0)` 检查确保 `level` 指针非空。因此，在告警行 `level->length != EBML_UNK... |
| 1642 | ffmpeg-7.1.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码中，宏 `BITS_AVAILABLE` 被定义为常量 1，这导致 `while (ret<0x8000000U && BITS_AVAILABLE(re, gb))` 循环条件恒真，但宏定义表明这是工具已知的常量，不会导致空... |
| 1643 | ffmpeg-7.1.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 切片代码中，在解引用 `s->bit_buf` 之前，函数参数 `s` 已作为指针传入，但切片内未显示对 `s` 进行空值检查。然而，函数名为 `put_bits_no_assert`，暗示其设计为内部辅助函数，调用方应确保传入非空指... |
| 1644 | ffmpeg-7.1.1 | rtp_set_prft | Dereference of null pointer | 646 | FP | FP | 切片代码显示，在调用av_rescale_q之前，已检查了指针prft是否为NULL，若为NULL则函数已提前返回，因此后续对prft->wallclock的赋值不会发生空指针解引用。 |
| 1645 | ffmpeg-7.1.1 | ebml_read_sint | Dereference of null pointer | 1022 | FP | FP | 切片代码显示，在调用`avio_r8`函数读取数据前，函数内部已包含对缓冲区指针的边界检查（`s->buf_ptr >= s->buf_end`），并会在缓冲区耗尽时调用`fill_buffer`进行填充，这提供了防护机制，使得对`a... |
| 1646 | ffmpeg-7.1.1 | safe_filename | Dereference of null pointer | 98 | FP | FP | 切片代码显示，在for循环条件`*f`中解引用指针`f`之前，函数已接收参数`f`，且循环仅在`*f`非零时执行。没有证据表明传入的`f`是空指针，且函数逻辑旨在检查字符串内容，解引用发生在有效的循环条件检查中，属于正常的安全检查逻辑... |
| 1647 | ffmpeg-7.1.1 | try_push_frame | Dereference of null pointer | 512 | FP | FP | 切片代码显示，在访问 s->input_frames[0] 之前，已经通过循环检查了所有 input_frames 元素，并且当 nb_samples 为 0 时会跳转到 eof 标签，从而避免了后续对空指针的访问。因此，在告警行执行... |
| 1648 | ffmpeg-7.1.1 | dump_stream_group | Dereference of null pointer | 788 | FP | FP | 切片代码显示告警行 `printed[st->index] = 1;` 位于 `for` 循环内，循环条件 `i < stg->nb_streams` 确保 `stg` 非空且 `stg->streams[i]` 有效。`stg` 来... |
| 1649 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，在访问 `in->linesize[plane]` 之前，存在条件 `s->planeheight[plane] > 1` 进行保护。当条件不满足时，`linesize` 被赋值为 0，避免了空指针解引用。因此，该告警是误报。 |
| 1650 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 236 | FP | FP | 切片代码显示，在访问 `frame->format` 等字段前，存在 `av_assert0(frame ｜｜ (enc->type != AVMEDIA_TYPE_VIDEO && enc->type != AVMEDIA_TYPE... |
| 1651 | ffmpeg-7.1.1 | ff_encode_encode_cb | Dereference of null pointer | 275 | FP | FP | 切片代码显示，在访问 `frame->duration` 之前，已经存在条件 `if (frame && (codec->caps_internal & FF_CODEC_CAP_EOF_FLUSH))` 或 `if (frame)`... |
| 1652 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 219 | FP | FP | 告警指向的代码行位于一个av_assert0宏断言内部，该宏在条件不满足时会调用abort()终止程序。切片代码显示，该断言仅在编码器类型为音频且frame指针非空时才会执行，且断言检查的是frame结构体内部字段的有效性，而非对空指... |
| 1653 | ffmpeg-7.1.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 切片代码显示告警位于宏 UPDATE_CACHE 的调用处，该宏展开为 UPDATE_CACHE_LE，其定义未在切片中提供。切片中未显示任何对指针 's' 的直接解引用操作，且函数 get_sbits 是 FFmpeg 中广泛使用的... |
| 1654 | ffmpeg-7.1.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码中，变量 `dpd` 在条件判断 `if (dpd[pos])` 中被解引用，但 `dpd` 在切片中未定义或初始化，无法确认其为空指针。告警基于不完整的上下文，且切片内未见明确的空指针赋值或传递路径，倾向于判定为工具误报。 |
| 1656 | ffmpeg-7.1.1 | hls_append_segment | Dereference of null pointer | 1185 | FP | FP | 在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 之前，代码已通过 `en = vs->segments;` 将 `e... |
| 1657 | ffmpeg-7.1.1 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 切片代码显示，在DIR_DURATION指令处理前，DIR_FILE指令已通过add_file函数初始化了file指针，且该指令执行失败会通过goto fail跳转，因此执行到file->user_duration赋值时file指针不... |
| 1658 | ffmpeg-7.1.1 | dump_argument | Dereference of null pointer | 516 | FP | FP | 切片代码显示函数参数 `a` 在循环条件 `for (p = a; *p; p++)` 中被直接解引用，这仅在 `a` 为 `NULL` 时会导致空指针解引用。然而，函数签名 `dump_argument(FILE *report_f... |
| 1659 | ffmpeg-7.1.1 | kalman_smoothen | Dereference of null pointer | 585 | FP | FP | 切片代码显示，在解引用 `best_hist_ptr` 之前，存在条件 `if (optimal_gain <= 0) return -1;` 和 `if (dot <= 0) return -1;` 确保 `best_hist_pt... |
| 1660 | ffmpeg-7.1.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在访问 `dp1[pos]` 和 `dp2[pos]` 之前，存在条件 `if (dpd[pos])` 进行保护，这确保了指针 `dp1` 和 `dp2` 仅在 `dpd[pos]` 非零时被解引用。结合上下文，`dpd... |
| 1661 | ffmpeg-7.1.1 | id3v2_parse | Dereference of null pointer | 1055 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 获取的，该函数仅在找到匹配的标签时才返回非空指针。告警点位于 `else` 分支，该分支仅... |
| 1662 | ffmpeg-7.1.1 | set_bframe_chain_length | Dereference of null pointer | 1596 | FP | FP | 在告警行`s->input_picture[i - 1]->f->data[0]`处，切片代码显示其位于`s->b_frame_strategy == 1`的条件分支内，且该行执行前有明确的`if (s->input_picture[... |
| 1663 | ffmpeg-7.1.1 | split_commandline | Dereference of null pointer | 809 | FP | FP | 切片代码显示，在警告行 `if (opt[0] == '-' && opt[1] == '-' && !opt[2])` 之前，`opt` 变量已通过 `const char *opt = argv[optindex++];` 被赋值... |
| 1664 | ffmpeg-7.1.1 | ebml_read_ascii | Dereference of null pointer | 1077 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，不会实际解引用任何指针，因此不存在空指针解引用问题。 |
| 1665 | ffmpeg-7.1.1 | output_packet | Dereference of null pointer | 1103 | FP | FP | 切片代码显示，在访问 `timestamp_packet->unwritten_size` 之前，`timestamp_packet` 被赋值为 `stream->premux_packet`，而 `stream->premux_pa... |
| 1666 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 286 | FP | FP | 切片代码中，在访问 `ost->ist->par` 之前，`ost` 和 `ost->ist` 的有效性已在函数入口处通过 `av_assert0` 宏间接保证，且该宏在条件失败时会中止程序，因此空指针解引用在实际执行中不会发生。 |
| 1667 | ffmpeg-7.1.1 | ebml_read_uint | Dereference of null pointer | 1002 | FP | FP | 切片代码显示指针 `num` 在函数入口处被直接解引用赋值（`*num = 0;`），但该指针是函数参数，调用者必须提供有效地址。在典型的C语言函数调用约定中，调用方有责任确保传入的指针非空，且切片中未见有对 `num` 进行空指针检... |
| 1668 | ffmpeg-7.1.1 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 切片代码显示，在DIR_INPOINT指令执行前，必须通过DIR_FILE指令成功创建file对象，且add_file函数会初始化file->inpoint为AV_NOPTS_VALUE。此外，代码逻辑确保file指针在赋值前已被有效... |
| 1669 | ffmpeg-7.1.1 | sb_decode | Dereference of null pointer | 1348 | FP | FP | 切片代码显示，在访问 `innov_save` 指针前，已通过 `if (st->innov_save)` 检查其非空，并且仅在条件成立时才执行 `innov_save[2 * i] = exc[i];` 这一行。因此，不会发生空指针... |
| 1670 | ffmpeg-7.1.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 切片代码显示，在访问 `(*child)->state` 之前，`t->state` 非零且 `(*child)` 指针来自 `&t->child[i]`，而 `t` 在函数入口已通过 `if (t)` 确保非空，且 `child` ... |
| 1671 | ffmpeg-7.1.1 | check_header_mismatch | Dereference of null pointer | 519 | FP | FP | 切片代码中，在警告行`curr = curr->next;`之前，循环条件`for (i = 0; i < FLAC_MAX_SEQUENTIAL_HEADERS && curr != child; i++)`确保了`curr`在解引... |
| 1672 | ffmpeg-7.1.1 | get_pict_type | Dereference of null pointer | 136 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，`unit->content` 被赋值给 `slice` 指针，但 `unit->content` 的来源和空值检查在切片中不可见。然而，根据函数... |
| 1673 | ffmpeg-7.1.1 | ogg_write_header | Dereference of null pointer | 629 | FP | FP | 切片代码显示告警行是对结构体成员的直接赋值，并未发生对空指针的解引用操作。代码逻辑在切片可见范围内是安全的，工具报告的逻辑错误不成立。 |
| 1674 | ffmpeg-7.1.1 | mpegts_open_filter | Dereference of null pointer | 495 | FP | FP | 切片代码中，`av_log` 宏被定义为 `while(0)`，这意味着该函数调用在编译后为空操作，不会对指针 `ts->stream` 进行解引用。因此，不存在对空指针的解引用逻辑错误。 |
| 1675 | ffmpeg-7.1.1 | guess_mv | Dereference of null pointer | 432 | FP | FP | 切片代码中，在警告行（第432行）使用`s->last_pic.f->data[0]`之前，存在明确的条件检查`if (s->last_pic.f && s->last_pic.f->data[0])`，这确保了指针不为空。因此，该行... |
| 1676 | ffmpeg-7.1.1 | build_table | Dereference of null pointer | 204 | FP | FP | 切片代码显示告警行`table[j].len = -subtable_bits;`中的`table`指针在`alloc_table`成功且`table_index >= 0`时被正确赋值，且`j`的计算基于`code_prefix`和... |
| 1677 | ffmpeg-7.1.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `chapters[i]` 之前，外层存在条件判断 `if (chapters && nb_chapters)` 和 `if (m)`，并且内部循环 `for (int i = 0; i < nb_chapter... |
| 1678 | ffmpeg-7.1.1 | locate_option | Dereference of null pointer | 495 | FP | FP | 切片代码显示，在调用 `po->name` 之前，`po` 指针来自 `find_option` 函数的返回值，该函数在循环中返回一个指向 `OptionDef` 结构体的指针。虽然 `find_option` 可能返回一个 `nam... |
| 1679 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 78 | FP | FP | 切片代码显示，UPDATE_CACHE是一个宏，其展开不涉及对指针gb的直接解引用；告警点位于宏定义行，实际解引用操作发生在宏展开的内部逻辑中，且上下文未显示gb为null。 |
| 1680 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 切片代码显示，在警告行`uint16_t *val = (uint16_t *)in->data[plane];`之前，`in`指针作为函数参数传入，且后续被直接使用，表明其非空。此外，代码逻辑中`in`被用于多个数据访问操作，未见任... |
| 1681 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 333 | FP | FP | 切片代码显示，在访问outlink指针之前，已通过条件`s->do_video`进行保护。当`s->do_video`为假时，outlink被初始化为NULL，但后续使用outlink的代码块（如`av_rescale_q`）都位于`... |
| 1682 | ffmpeg-7.1.1 | av_dump_format | Dereference of null pointer | 898 | FP | FP | 切片代码显示，在访问 printed 数组之前，已通过条件 'if (ic->nb_streams && !printed) return;' 确保 printed 不为 NULL 或 nb_streams 为 0，且后续访问 pri... |
| 1683 | ffmpeg-7.1.1 | check_header_mismatch | Dereference of null pointer | 475 | FP | FP | 切片代码中，在访问 `curr->link_penalty[i]` 之前，`curr` 指针通过 `curr = curr->next;` 在循环中更新，但循环条件 `curr != child` 确保了 `curr` 在遍历链表时不... |
| 1684 | ffmpeg-7.1.1 | update_context_from_thread | Dereference of null pointer | 438 | FP | FP | 切片代码中，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 条件确保 `hwaccel` 指针有... |
| 1685 | ffmpeg-7.1.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 切片代码显示，在调用UPDATE_CACHE_32之前，函数get_bits_long已通过宏av_assert2对参数n进行了断言检查，并且其内部调用的get_bits函数也包含类似的断言。这些断言在调试构建中会检查指针和参数的有效... |
| 1686 | ffmpeg-7.1.1 | activate | Dereference of null pointer | 186 | FP | FP | 切片代码显示，在访问frame->pts之前，frame指针在`s->stop_mode == MODE_ADD`或`MODE_CLONE`分支中已被分配（通过ff_get_video_buffer或av_frame_clone），并... |
| 1687 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 200 | FP | FP | 切片代码显示，在访问ptr2[x]之前，ptr2已通过av_malloc_array分配内存，且分配失败时函数会提前返回，因此ptr2不为NULL。此外，访问发生在条件`if (depth == 1)`或`else`分支内，这些分支仅... |
| 1688 | ffmpeg-7.1.1 | check_available | Dereference of null pointer | 616 | FP | FP | 切片代码显示，在访问 `TAB_MVF(n->x, n->y).pred_flag` 之前，已通过 `is_available(fc, n->x, n->y)` 检查了坐标的有效性，这很可能确保了 `tab_mvf` 数组访问不会导致... |
| 1689 | ffmpeg-7.1.1 | ff_encode_encode_cb | Dereference of null pointer | 272 | FP | FP | 切片代码显示，在访问 `frame->pts` 之前，已经存在条件 `if (!ret && *got_packet)` 和 `if (avpkt->pts == AV_NOPTS_VALUE)`，并且 `frame` 参数在函数入口... |
| 1690 | ffmpeg-7.1.1 | rtp_parse_one_packet | Dereference of null pointer | 888 | FP | FP | 切片代码显示，在告警行访问`buf[0]`之前，函数开头已对`buf`指针进行了检查。当`buf`为NULL时，函数会提前返回`rtp_parse_queued_packet`或进行其他处理，不会执行到解引用操作。因此，该空指针解引用... |
| 1691 | ffmpeg-7.1.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，`dpd` 指针已通过三元条件运算符从 `out->data` 数组安全赋值，且 `out` 指针作为函数参数非空，因此 `dpd` 为 null 的可能性极低。告警为逻辑误判。 |
| 1692 | ffmpeg-7.1.1 | ost_add | Dereference of null pointer | 1541 | FP | FP | 切片代码显示，在访问 `ist->st->duration` 之前，存在条件 `if (ost->ist && ost->ist->st->duration > 0)` 检查 `ost->ist` 和 `ost->ist->st` 是... |
| 1693 | ffmpeg-7.1.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1420 | FP | FP | 切片代码显示`scale_matrix`在解引用前已通过条件`sps->scaling_list_enabled && !(transform_skip_flag && log2_trafo_size > 2)`进行保护，且存在默认值... |
| 1694 | ffmpeg-7.1.1 | nal_parse_units | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `list->nalus` 之前，已通过 `if (!tmp)` 检查了 `av_fast_realloc` 的返回值，确保指针非空后才进行赋值和使用，因此不存在空指针解引用。 |
| 1695 | ffmpeg-7.1.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1513 | FP | FP | 切片代码显示，在调用 `ff_get_audio_buffer` 之前，`frame` 指针已通过 `AVFrame *frame = *rframe;` 获取，并在 `av_frame_is_writable(frame)` 中被直... |
| 1696 | ffmpeg-7.1.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 切片代码显示`s->buffer`是一个数组访问，`s`指针本身在函数调用时已通过上下文确保非空，且数组索引`index >> 3`的计算在切片内未见越界或空指针解引用风险。告警可能源于工具对指针别名或数组边界的不精确分析。 |
| 1697 | ffmpeg-7.1.1 | asf_parse_packet | Dereference of null pointer | 1307 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data[i]` 之前，已通过 `av_new_packet` 或 `av_packet_unref` 等函数确保 `asf_st->pkt.data` 被正确分配或置空，且循环前有 `a... |
| 1698 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 146 | FP | FP | 切片代码显示，在解引用alpMmxFilter指针之前，已通过条件`(CONFIG_SWSCALE_ALPHA && hasAlpha)`检查alpSrcPtr是否为NULL，并且alpMmxFilter仅在alpSrcPtr非空时被... |
| 1699 | ffmpeg-7.1.1 | choose_rct_params | Dereference of null pointer | 1008 | FP | FP | 切片代码显示告警行位于条件分支 `else if (f->use32bit ｜｜ transparency)` 内部，该分支仅在 `transparency` 为真或 `f->use32bit` 为真时执行。变量 `transpare... |
| 1700 | ffmpeg-7.1.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在访问 `dp1[pos]` 和 `dp2[pos]` 之前，已通过 `if (dpd[pos])` 条件进行了检查，这确保了指针 `dpd` 在解引用前不为空，因此不存在空指针解引用逻辑错误。 |
| 1701 | ffmpeg-7.1.1 | unsharp_slice_8 | Dereference of null pointer | 173 | FP | FP | 切片代码中，宏定义 `DEF_UNSHARP_SLICE_FUNC` 展开的函数体开头对指针 `sc` 和 `sr` 的访问是安全的，它们来自结构体成员 `fp->sc` 和 `fp->sr`，且告警点 `{ NULL }` 是宏定义... |
| 1702 | ffmpeg-7.1.1 | mov_write_trak_tag | Dereference of null pointer | 4191 | FP | FP | 切片代码中，变量 `st` 作为函数参数传入，在告警行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 之前，`st` 已在多处被直接使用（如 `mov_... |
| 1703 | ffmpeg-7.1.1 | ebml_parse | Dereference of null pointer | 1380 | FP | FP | 切片代码中，在告警行（1380行）之前，变量`level`已通过条件`matroska->num_levels > 0`进行检查，确保其不为NULL。告警行位于`else if (level->length != EBML_UNKNO... |
| 1704 | ffmpeg-7.1.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码中，`dpd` 指针来源于 `out->data[s->pd]` 或 `out->data[0]`，这些是 AVFrame 结构体的有效数据指针，在正常上下文中不应为 NULL。告警点 `dpd[pos]` 的访问发生在对 `... |
| 1705 | ffmpeg-7.1.1 | get_bits_le | Dereference of null pointer | 361 | FP | FP | 切片代码仅展示了宏定义和函数框架，未显示对指针's'进行显式解引用或任何可能导致空指针解引用的具体操作。告警可能源于工具对宏展开的误判，在切片可见范围内没有证据表明存在空指针解引用。 |
| 1706 | ffmpeg-7.1.1 | ac3_apply_rematrixing | Dereference of null pointer | 598 | FP | FP | 切片代码中，`flags` 变量未定义，其来源和初始化不可见，无法确认其为空指针。基于告警为逻辑错误的描述和常见编码模式，`flags` 很可能是一个有效的数组指针，工具可能误判了其可能的空值状态。 |
| 1707 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 683 | FP | FP | 切片代码显示，在调用FFSWAP宏之前，已通过条件`if (js_databuf == q->decoded_bytes_buffer)`确保`ptr1`和`ptr2`指针均指向有效缓冲区，不会发生空指针解引用。 |
| 1708 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 303 | FP | FP | 切片代码显示告警行是对一个指针进行类型转换和位移操作，该指针 `src` 是函数参数且已在循环中被使用，没有证据表明它是空指针。代码逻辑在切片可见范围内是安全的，工具可能误判了指针解引用。 |
| 1709 | ffmpeg-7.1.1 | ff_rdt_parse_header | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在告警行（while循环条件）中，对`buf`的访问前已通过`len >= 5`确保了缓冲区长度，且`buf`作为函数参数传入，在切片内未见其被赋值为空。因此，对`buf[1]`的解引用是安全的，属于静态分析工具的逻辑误报。 |
| 1710 | ffmpeg-7.1.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 切片代码显示，在访问 `info->key_ids[i]` 之前，函数已通过 `if (info)` 检查确保 `info` 指针非空，并且 `info->key_ids` 的访问发生在该保护条件内，因此不会发生空指针解引用。 |
| 1712 | ffmpeg-7.1.1 | build_table | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `alloc_table` 分配内存并检查了 `table_index` 的有效性，且 `j` 的值由 `code` 移位计算得出，其范围受 `table_... |
| 1713 | ffmpeg-7.1.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用memcpy访问info->key_ids[j]之前，已通过av_encryption_init_info_alloc函数为每个key_ids[i]分配了内存，并且该函数在分配失败时会返回NULL，导致外层函数提前... |
| 1714 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 293 | FP | FP | 切片代码显示，在调用 `encode_line` 函数前，`sample[0]` 指针已通过 `sample[i] = sc->sample_buffer + ...` 被正确初始化并指向有效的缓冲区，不存在空指针解引用。 |
| 1715 | ffmpeg-7.1.1 | dump_stream_group | Dereference of null pointer | 715 | FP | FP | 切片代码中，告警行访问的 `st` 指针来源于未在切片中定义的循环变量 `k` 和数组 `stg->streams`，其有效性无法从当前切片中确认。但告警点位于一个受 `channel_count > 0` 和 `k < stg->n... |
| 1716 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 166 | FP | FP | 切片代码显示，在访问`alpSrcPtr`指针前，已通过条件`(CONFIG_SWSCALE_ALPHA && hasAlpha)`进行检查，当条件不满足时`alpSrcPtr`被初始化为NULL，而在后续使用该指针的代码块（告警行）... |
| 1717 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向的UPDATE_CACHE是一个宏，其展开后是对结构体指针gb的操作。切片代码显示gb是函数参数，在调用前已传入，且宏内部没有对gb进行空指针解引用。在切片可见范围内，没有证据表明gb为NULL，因此判定为误报。 |
| 1718 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在告警行使用`in->linesize[plane]`之前，`in`指针已作为参数传入且未在切片内被置空。告警行位于`s->planeheight[plane] > 1`的条件判断之后，当条件不满足时`linesize`... |
| 1719 | ffmpeg-7.1.1 | set_bframe_chain_length | Dereference of null pointer | 1611 | FP | FP | 切片代码显示，在访问 `s->input_picture[i]` 之前，循环条件 `i < b_frames + 1` 中的 `b_frames` 由 `FFMAX(0, i - 1)` 计算得出，且前面的逻辑已确保 `i` 的取值使... |
| 1720 | ffmpeg-7.1.1 | mov_write_trak_tag | Dereference of null pointer | 4196 | FP | FP | 切片代码中，在调用 `is_clcp_track(track)` 之前，`track` 指针作为函数参数传入，并在多处被安全使用（如 `track->mode`、`track->tag`），没有证据表明它在此处可能为空。告警点位于条件... |
| 1721 | ffmpeg-7.1.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后不涉及直接的指针解引用操作。函数 get_bits 是 FFmpeg 中经过充分验证的位读取工具函数，其内部宏和断言机制确保了操作的鲁棒性，未见明显的空指针解引用逻辑。 |
| 1722 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 472 | FP | FP | 切片代码中，`DECODE_CODEWORD` 宏内部调用了 `UPDATE_CACHE` 和 `GET_CACHE` 宏，这些宏负责从比特流读取数据并更新上下文，`gb` 指针在宏展开的上下文中被使用。告警点位于宏调用处，但切片未显... |
| 1723 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 687 | FP | FP | 切片代码显示，在警告行`q->decoded_bytes_buffer[i] = *ptr2--;`之前，`q->decoded_bytes_buffer`已在函数开头通过`ATRAC3Context *q = avctx->priv... |
| 1724 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确初始化为 `q->decoded_bytes_buffer`，这是一个有效的数组指针，因此不会发生空... |
| 1725 | ffmpeg-7.0.1 | show_bits | Dereference of null pointer | 376 | FP | FP | 切片代码仅展示了宏定义和函数框架，未显示对指针's'进行解引用的具体操作或明确的空指针传递路径。告警指向的宏UPDATE_CACHE在切片中未展开，无法确认存在必然的空指针解引用逻辑错误。 |
| 1726 | ffmpeg-7.0.1 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 切片代码显示，在访问 `s->st->time_base.den` 之前，存在条件 `s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->ic->nb_streams > 1` 和 `s->la... |
| 1727 | ffmpeg-7.0.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 412 | FP | FP | 切片代码显示，在访问 `ctx->buffers[buf.index]` 之前，`buf.index` 来自 `ioctl` 系统调用 `VIDIOC_DQBUF` 的返回结果，该操作由驱动管理，应保证索引在有效范围内。同时，`ctx... |
| 1728 | ffmpeg-7.0.1 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | FP | 切片代码显示，在访问 `frame->pts` 的代码行之前，存在 `if (!in && context->input_frames >= 8) return 0;` 的逻辑。当 `in` 为 NULL（即 `frame` 为 NU... |
| 1729 | ffmpeg-7.0.1 | ebml_read_binary | Dereference of null pointer | 1088 | FP | FP | 切片代码显示，在调用`memset`之前，`av_buffer_realloc`函数已被调用并成功返回（`ret < 0`时函数已提前返回），这确保了`bin->buf`和`bin->buf->data`是有效的非空指针。因此，对`b... |
| 1730 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码中，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回，因此 `ptr2` 不为空。告警点 `ptr[2*x] = ptr2[x] >> 4;` 处... |
| 1732 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 切片代码显示，在访问 `in->data[plane]` 之前，`in` 帧作为函数参数传入且未被修改，其指针不可能为空。此外，代码逻辑仅在 `s->filter` 为真时才可能使用 `dst` 指针，而 `dst` 的空值检查也已存... |
| 1733 | ffmpeg-7.0.1 | unsharp_slice_16 | Dereference of null pointer | 141 | FP | FP | 切片代码显示，在宏展开的函数定义中，`src2` 变量被初始化为 NULL，但在后续可见的代码中并未被解引用。告警点位于宏定义行，该行本身不执行解引用操作，因此是工具对代码结构的误判。 |
| 1734 | ffmpeg-7.0.1 | ebml_parse | Dereference of null pointer | 1354 | FP | FP | 切片代码显示，在告警行访问`level->length`之前，已通过`if (matroska->num_levels > 0)`检查确保`level`指针非空，且`level`是从`matroska->levels`数组中有效获取的... |
| 1735 | ffmpeg-7.0.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码中，`UPDATE_CACHE` 是一个宏，其展开不涉及对指针 `gb` 的解引用。告警点所在的宏调用本身不会导致空指针解引用，且切片内没有证据表明 `gb` 在调用前被赋值为空。 |
| 1736 | ffmpeg-7.0.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 切片代码中，在访问 `s->bit_buf` 之前，函数参数 `s` 的来源和有效性未知，但函数内部逻辑是完整的赋值和位操作，没有明显的空指针解引用路径。告警点 `bit_buf = s->bit_buf;` 是结构体成员访问，其安全... |
| 1737 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码中，`src` 作为函数参数传入，在循环内被用作指针偏移计算的基础，但并未直接解引用空指针。告警指向的代码行 `sample[0][x] = ((uint16_t*)(src + stride*y))[x] >> (16 - ... |
| 1738 | ffmpeg-7.0.1 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 切片代码显示，在调用av_rescale_q之前，已对av_packet_new_side_data的返回值prft进行了空指针检查，若为空则直接返回错误，因此后续对s->st的访问不会在prft为空时发生。 |
| 1739 | ffmpeg-7.0.1 | ebml_read_sint | Dereference of null pointer | 1015 | FP | FP | 切片代码显示，在调用avio_r8函数时，其内部已包含对AVIOContext指针s的边界检查（s->buf_ptr >= s->buf_end），且当缓冲区耗尽时会调用fill_buffer(s)并最终返回0，这确保了函数不会对空指... |
| 1740 | ffmpeg-7.0.1 | safe_filename | Dereference of null pointer | 97 | FP | FP | 切片代码显示，在for循环条件 `*f` 中解引用指针 `f` 之前，该指针已作为函数参数传入，且循环内对 `f` 的递增操作始终在检查 `*f` 非空之后进行，不存在解引用空指针的逻辑路径。 |
| 1741 | ffmpeg-7.0.1 | try_push_frame | Dereference of null pointer | 511 | FP | FP | 切片代码显示，在访问 `s->input_frames[0]` 之前，已经通过 `if (!nb_samples) goto eof;` 确保了至少有一个输入帧存在（`nb_samples > 0`），这隐含了 `s->input_f... |
| 1742 | ffmpeg-7.0.1 | dump_stream_group | Dereference of null pointer | 751 | FP | FP | 切片代码显示，在访问 `stg->streams[i]` 之前，存在对 `stg->nb_streams` 的检查（`stg->nb_streams &&`），这确保了循环仅在流数量大于0时执行，且 `stg` 本身在函数开头已从有效... |
| 1743 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，在访问 `in->linesize[plane]` 之前，存在条件 `s->planeheight[plane] > 1` 的保护。当 `planeheight` 不大于1时，`linesize` 被赋值为0，从而避免了... |
| 1744 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 225 | FP | FP | 切片代码显示，在访问frame->format之前，存在av_assert0断言检查frame是否为NULL，且该断言在条件不满足时会调用abort()终止程序，因此不会发生空指针解引用。 |
| 1745 | ffmpeg-7.0.1 | ff_encode_encode_cb | Dereference of null pointer | 274 | FP | FP | 切片代码显示，在访问 `frame->duration` 之前，外层条件 `if (!ret && *got_packet)` 已经成立，并且内部存在 `if (frame)` 的条件检查（第274行），但更关键的是，在告警所在行（`... |
| 1746 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问 `frame->format` 等字段之前，存在 `av_assert0(frame ｜｜ (enc->type != AVMEDIA_TYPE_VIDEO && enc->type != AVMEDIA_TYP... |
| 1747 | ffmpeg-7.0.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后仅进行位操作，并未直接解引用指针。函数 get_sbits 的参数 s 在切片中未显示为空，且其作为 GetBitContext 指针在常规使用场景下由调用者保证... |
| 1748 | ffmpeg-7.0.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码中，变量 `dpd` 在条件判断 `if (dpd[pos])` 中被解引用，但 `dpd` 未在切片中定义或初始化，无法确认其为空指针。告警基于不完整的上下文，且切片内未见明确的空指针赋值或传递，倾向于判定为工具误报。 |
| 1751 | ffmpeg-7.0.1 | hls_append_segment | Dereference of null pointer | 1171 | FP | FP | 切片代码显示，在警告行`if (!en->next->discont_program_date_time && !en->discont_program_date_time)`之前，`en`被赋值为`vs->segments`，而`v... |
| 1752 | ffmpeg-7.0.1 | concat_parse_script | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `file->user_duration` 之前，`file` 指针已在 `DIR_FILE` 分支通过 `add_file` 函数成功初始化并赋值，且该分支执行失败时会通过 `goto fail` 跳转，不会执... |
| 1753 | ffmpeg-7.0.1 | dump_argument | Dereference of null pointer | 507 | FP | FP | 切片代码显示函数参数 `a` 在循环条件 `for (p = a; *p; p++)` 中被直接解引用，这暗示调用者必须传递一个有效的非空字符串指针。函数是静态工具函数，其内部逻辑依赖于 `a` 不为空，且切片中未见对 `a` 的显式... |
| 1754 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 297 | FP | FP | 切片代码显示，在调用 `encode_line` 函数前，`sample[0]` 指针已在循环中被明确赋值，且其指向的缓冲区 `s->sample_buffer` 已通过 `memset` 初始化，不存在空指针解引用。告警点 `((u... |
| 1755 | ffmpeg-7.0.1 | kalman_smoothen | Dereference of null pointer | 584 | FP | FP | 切片代码显示，在解引用 `best_hist_ptr` 之前，存在条件判断 `if (optimal_gain <= 0) return -1;` 和 `if (dot <= 0) return -1;`，这确保了只有当 `best_... |
| 1756 | ffmpeg-7.0.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在访问dp1和dp2指针前，存在条件判断`if (dpd[pos])`，这确保了只有在dpd[pos]非零时才进行解引用。虽然dp1和dp2的定义未在切片中明确显示，但根据上下文逻辑，它们很可能与dpd类似，是有效的数组... |
| 1757 | ffmpeg-7.0.1 | id3v2_parse | Dereference of null pointer | 1054 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 获取的，该函数仅在找到匹配的标签时才返回非空指针。告警点位于 `else` 分支，该分支仅... |
| 1758 | ffmpeg-7.0.1 | choose_rct_params | Dereference of null pointer | 983 | FP | FP | 切片代码中，src数组的索引访问（src[0]、src[1]、src[2]）发生在循环内部，且索引值（0,1,2）是固定的，没有证据表明src数组本身或其元素为NULL。告警点（src[1]）的访问模式与src[0]和src[2]一致... |
| 1759 | ffmpeg-7.0.1 | split_commandline | Dereference of null pointer | 800 | FP | FP | 切片代码显示，在警告行 `if (opt[0] == '-' && opt[1] == '-' && !opt[2])` 之前，`opt` 被赋值为 `argv[optindex++]`，而 `argv` 来自命令行参数，在正常执行流... |
| 1760 | ffmpeg-7.0.1 | ebml_read_ascii | Dereference of null pointer | 1070 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 1761 | ffmpeg-7.0.1 | output_packet | Dereference of null pointer | 1102 | FP | FP | 切片代码显示，在访问 `timestamp_packet->unwritten_size` 之前，`timestamp_packet` 被赋值为 `stream->premux_packet`，而 `stream->premux_pa... |
| 1762 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 293 | FP | FP | 切片代码中，在访问 `ost->ist->par->width` 之前，`ost` 和 `ost->ist` 的有效性已在函数调用路径中得到保证，且 `set_encoder_id` 函数成功执行并返回 0，表明 `ost->enc_... |
| 1763 | ffmpeg-7.0.1 | ebml_read_uint | Dereference of null pointer | 995 | FP | FP | 切片代码显示，在指针`num`被解引用之前，函数入口处没有可见的NULL检查，但告警行`*num = 0;`是赋值操作，其解引用行为本身不依赖于`num`是否为NULL。结合函数签名和上下文，`num`作为输出参数，其有效性应由调用者... |
| 1764 | ffmpeg-7.0.1 | concat_parse_script | Dereference of null pointer | 561 | FP | FP | 切片代码显示，在DIR_INPOINT指令执行前，必须通过DIR_FILE指令成功创建文件对象（file = add_file(...)），且该指令会检查NEEDS_FILE标志，确保cat->nb_files > 0。因此，当执行到... |
| 1766 | ffmpeg-7.0.1 | ost_add | Dereference of null pointer | 1428 | FP | FP | 切片代码中，在访问 `ist->st->duration` 之前，存在条件 `if (ost->ist && ost->ist->st->duration > 0)`，该条件已经检查了 `ost->ist` 和 `ost->ist->... |
| 1767 | ffmpeg-7.0.1 | sb_decode | Dereference of null pointer | 1347 | FP | FP | 切片代码显示，在访问 `innov_save` 指针前，已通过 `if (st->innov_save)` 检查其是否为空，并且 `innov_save` 被赋值为 `st->innov_save + 2 * offset`，该赋值仅... |
| 1768 | ffmpeg-7.0.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 切片代码显示，在访问 `(*child)->state` 之前，`t->state` 已通过 `t->state += 2 * i - 1;` 更新，且外层条件 `if (t->state)` 确保 `t->state` 非零，结合 ... |
| 1769 | ffmpeg-7.0.1 | check_header_mismatch | Dereference of null pointer | 520 | FP | FP | 切片代码显示，在访问 `header->link_penalty[i]` 之前，循环 `for (i = 0; i < FLAC_MAX_SEQUENTIAL_HEADERS && curr != child; i++)` 确保了 `... |
| 1770 | ffmpeg-7.0.1 | get_pict_type | Dereference of null pointer | 135 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效范围，这确保了 `unit->conte... |
| 1771 | ffmpeg-7.0.1 | ogg_write_header | Dereference of null pointer | 628 | FP | FP | 切片代码显示对指针 `oggstream` 进行了成员访问，但未提供其定义或初始化上下文，无法确认其为空指针。在典型的代码上下文中，此类结构体指针通常在函数入口处已进行有效性检查或初始化，告警很可能是工具对代码路径的误判。 |
| 1772 | ffmpeg-7.0.1 | mpegts_open_filter | Dereference of null pointer | 497 | FP | FP | 切片代码显示，在调用av_log时，其参数ts->stream被使用，但ts作为函数参数传入，其有效性由调用者保证。更重要的是，av_log宏被定义为空操作（while(0)），因此该行代码不会实际执行任何解引用操作，不存在空指针解引... |
| 1773 | ffmpeg-7.0.1 | guess_mv | Dereference of null pointer | 428 | FP | FP | 切片代码显示，在告警行访问 `s->last_pic.f->data[0]` 之前，存在条件 `if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])` 进行非空检查，因此不会发... |
| 1774 | ffmpeg-7.0.1 | build_table | Dereference of null pointer | 204 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `alloc_table` 成功分配内存并赋值，且 `j` 的计算基于输入参数，其范围受 `table_size`（即 `1 << table_nb_bit... |
| 1775 | ffmpeg-7.0.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `chapters[i]` 之前，存在条件 `if (chapters && nb_chapters)` 和 `for (int i = 0; i < nb_chapters; i++)`，这确保了当 `chap... |
| 1776 | ffmpeg-7.0.1 | locate_option | Dereference of null pointer | 486 | FP | FP | 在切片代码中，`po` 指针由 `find_option` 函数返回，该函数在循环中返回指向 `OptionDef` 结构数组的指针，即使未找到匹配项，也返回一个指向数组末尾（`name` 字段为 NULL）的有效指针，而非空指针。因... |
| 1777 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 切片代码显示，在告警行`uint16_t *val = (uint16_t *)in->data[plane];`之前，`in`作为函数参数传入，且后续代码中`in->data[plane]`被直接使用，表明`in`指针非空。告警点是... |
| 1778 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 332 | FP | FP | 告警行位于条件语句 `if (s->do_video)` 内部，该条件确保 `outlink` 不为 NULL（因为 `outlink` 在函数开头被赋值为 `s->do_video ? ctx->outputs[1] : NULL`... |
| 1779 | ffmpeg-7.0.1 | av_dump_format | Dereference of null pointer | 834 | FP | FP | 切片代码显示，在访问 `printed` 数组前，已通过 `if (ic->nb_streams && !printed) return;` 确保 `printed` 在 `ic->nb_streams > 0` 时非空，且后续访问 ... |
| 1780 | ffmpeg-7.0.1 | check_header_mismatch | Dereference of null pointer | 476 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 之前，`curr` 指针通过 `curr = curr->next;` 在循环中更新，但循环条件 `while (curr != child)` 确保了 `curr... |
| 1781 | ffmpeg-7.0.1 | update_context_from_thread | Dereference of null pointer | 360 | FP | FP | 切片代码中，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 条件进行了保护，并且 `hwacce... |
| 1782 | ffmpeg-7.0.1 | choose_rct_params | Dereference of null pointer | 984 | FP | FP | 切片代码显示告警行访问的 src[2] 指针在 else 分支中，该分支仅在 lbd 为假时执行。切片中未提供 src[2] 为空的证据，且函数参数 src[3] 表明它是一个指针数组，调用者应保证其有效性。基于切片可见的上下文，没有... |
| 1783 | ffmpeg-7.0.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 切片代码显示，在调用UPDATE_CACHE_32宏之前，函数已通过OPEN_READER宏初始化读取器，并且参数`s`在调用路径中已被使用，没有证据表明它是空指针。此外，该函数是内联工具函数，其调用上下文（未在切片中显示）很可能已确... |
| 1784 | ffmpeg-7.0.1 | activate | Dereference of null pointer | 186 | FP | FP | 切片代码显示，在访问frame->pts之前，frame指针要么通过ff_get_video_buffer分配（已检查NULL），要么通过av_frame_clone复制（已检查NULL），或者来自ff_inlink_consume_... |
| 1785 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 199 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回错误，因此 `ptr2` 不为空。告警点位于 `if (depth == 1)` 分支内，该... |
| 1786 | ffmpeg-7.0.1 | ff_encode_encode_cb | Dereference of null pointer | 271 | FP | FP | 切片代码显示，在访问 `frame->pts` 之前，存在条件 `if (frame && (codec->caps_internal & FF_CODEC_CAP_EOF_FLUSH))` 或 `if (frame)` 的检查，并且... |
| 1787 | ffmpeg-7.0.1 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 切片代码显示，在告警行访问`buf[0]`之前，存在对`buf`指针的明确空值检查（`if (!buf)`）和长度检查（`if (len < 12)`），且当`buf`为空时，函数会提前返回或调用其他路径，不会执行到解引用操作。因此，... |
| 1788 | ffmpeg-7.0.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已经通过条件 `if (dpd[pos])` 进行了非空检查，确保了指针的有效性。此外，`dpd` 指向 `out->data` 数组的某个元素，该数组在有效的 `AVFrame` 结... |
| 1789 | ffmpeg-7.0.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1507 | FP | FP | 切片代码显示，在调用 `ff_get_audio_buffer` 使用 `frame->nb_samples` 之前，`frame` 指针已通过 `AVFrame *frame = *rframe;` 获取，并且已作为参数传递给 `a... |
| 1790 | ffmpeg-7.0.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 切片代码显示`s->buffer`在解引用前未进行空指针检查，但`get_bits1`是一个内联辅助函数，其调用者`GetBitContext *s`的初始化及`buffer`的有效性应在外部保证。在典型的比特流读取上下文中，`s`和... |
| 1791 | ffmpeg-7.0.1 | asf_parse_packet | Dereference of null pointer | 1306 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data[i]` 之前，已通过 `av_assert0(asf_st)` 确保 `asf_st` 非空，且 `asf_st->pkt.data` 在循环前已通过 `av_new_packe... |
| 1792 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 148 | FP | FP | 切片代码显示，在解引用alpSrcPtr指针之前，已通过条件`(CONFIG_SWSCALE_ALPHA && hasAlpha)`进行检查，仅当条件为真时alpSrcPtr才为非NULL。告警行位于该条件保护的代码块内，因此不会发生... |
| 1793 | ffmpeg-7.0.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，对指针 `dpd` 的访问 `if (dpd[pos])` 发生在对 `dst[3]` 的非空检查 `if (dst[3])` 之后，且 `dpd` 很可能指向 `dst[3]` 的数据，这表明存在前置的指针有效性防护，... |
| 1795 | ffmpeg-7.0.1 | unsharp_slice_8 | Dereference of null pointer | 142 | FP | FP | 切片代码显示，在宏展开的函数定义中，`sc` 和 `sr` 等指针是从传入的 `ThreadData *td` 和 `UnsharpFilterParam *fp` 结构体中获取的，其有效性依赖于调用者。告警点位于宏定义展开的起始行，... |
| 1796 | ffmpeg-7.0.1 | mov_write_trak_tag | Dereference of null pointer | 3899 | FP | FP | 切片代码中，`st->sample_aspect_ratio` 在解引用前已通过 `st->sample_aspect_ratio.num` 进行了检查，且 `st` 指针在函数入口处作为参数传入，其有效性由调用者保证。告警点 `av... |
| 1797 | ffmpeg-7.0.1 | ebml_parse | Dereference of null pointer | 1371 | FP | FP | 切片代码中，变量 `level` 在访问前已通过 `matroska->num_levels > 0` 条件进行保护，且告警行位于 `else if (level->length != EBML_UNKNOWN_LENGTH)` 分支... |
| 1798 | ffmpeg-7.0.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码中，`dpd` 指针来源于 `out->data[s->pd]` 或 `out->data[0]`，而 `out` 是函数参数，在切片可见范围内没有证据表明 `out` 或其 `data` 字段为 NULL。告警点是对 `dp... |
| 1799 | ffmpeg-7.0.1 | get_bits_le | Dereference of null pointer | 361 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE_LE 的调用处，该宏及其相关宏（如 OPEN_READER）的操作对象是结构体指针 's' 的成员。切片中未提供 's' 的来源或对其为空的检查，但根据函数上下文和宏定义，这是一个内... |
| 1800 | ffmpeg-7.0.1 | ac3_apply_rematrixing | Dereference of null pointer | 387 | FP | FP | 切片代码中，`flags` 变量未定义，其来源和初始化状态不可见。告警点 `if (flags[bnd])` 假设 `flags` 为 null 指针，但根据上下文，`flags` 很可能是一个有效的数组指针（例如，可能是 `bloc... |
| 1801 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 682 | FP | FP | 切片代码显示，在调用FFSWAP宏之前，已经通过条件`if (js_databuf == q->decoded_bytes_buffer)`确保了`ptr1`和`ptr2`指针都指向有效的缓冲区（`q->decoded_bytes_b... |
| 1802 | ffmpeg-7.0.1 | ff_rdt_parse_header | Dereference of null pointer | 201 | FP | FP | 切片代码中，在告警行（while循环条件）访问buf[1]之前，函数参数buf作为指针传入，但未在切片内显示其来源。然而，告警行访问的是buf[1]而非buf[0]，且while循环条件已包含对len >= 5的检查，确保buf指向的... |
| 1803 | ffmpeg-7.0.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 切片代码显示，在访问 `info->key_ids[i]` 之前，函数入口处已通过 `if (info)` 检查了指针 `info` 非空，因此不会发生对空指针 `info` 的解引用。 |
| 1805 | ffmpeg-7.0.1 | build_table | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 1806 | ffmpeg-7.0.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用memcpy访问info->key_ids[j]之前，av_encryption_init_info_alloc函数已为每个key_ids[i]分配了内存，并且分配失败时函数会提前返回NULL。因此，当程序执行到告... |
| 1807 | ffmpeg-7.0.1 | dump_stream_group | Dereference of null pointer | 678 | FP | FP | 切片代码中，告警行 `printed[st->index] = 1;` 使用的指针 `st` 未在切片内定义或初始化，但该行位于一个条件循环 `for (int k = 0; channel_count > 0 && k < stg-... |
| 1808 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 168 | FP | FP | 切片代码显示，在解引用alpSrcPtr之前，已通过条件`(CONFIG_SWSCALE_ALPHA && hasAlpha)`进行检查，当条件不满足时alpSrcPtr被初始化为NULL，而告警所在行位于同一条件块内，因此不会发生空... |
| 1809 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 658 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE 的调用处，该宏最终展开为 UPDATE_CACHE_LE，但切片中未提供其定义。由于缺乏对宏展开后具体空指针解引用操作的可见证据，且该函数是FFmpeg中广泛使用的、经过验证的位读取... |
| 1810 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在警告行（linesize 计算）之前，已通过条件 `s->planeheight[plane] > 1` 进行保护。当 planeheight 不大于 1 时，linesize 被赋值为 0，避免了除以零或空指针解引用... |
| 1811 | ffmpeg-7.0.1 | mov_write_trak_tag | Dereference of null pointer | 3904 | FP | FP | 切片代码中，在调用 `is_clcp_track(track)` 之前，`track` 指针作为函数参数传入，且在整个函数中都被直接使用，没有可见的空指针解引用操作。告警点所在行 `is_clcp_track(track) && st... |
| 1812 | ffmpeg-7.0.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后不涉及直接的指针解引用操作。函数 get_bits 是 FFmpeg 中经过充分验证的位读取工具函数，其内部宏和逻辑旨在安全地操作 GetBitContext 结... |
| 1814 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 291 | FP | FP | 切片代码显示告警点 `src[x * pixel_stride + stride * y]` 是对传入的 `src` 指针进行数组索引访问，该指针是函数参数，在切片范围内没有证据表明它可能为空。函数逻辑是常规的图像像素遍历，属于正常的... |
| 1815 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 686 | FP | FP | 切片代码显示，在警告行（`q->decoded_bytes_buffer[i] = *ptr2--;`）之前，`q->decoded_bytes_buffer` 已在 `else` 分支的父级 `if` 条件（`js_databuf ... |
| 1816 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 691 | FP | FP | 切片代码显示，在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确初始化为 `q->decoded_bytes_buffer`，这是一个有效的数组指针，不可能为 NU... |
| 1817 | ffmpeg-6.1.1 | show_bits | Dereference of null pointer | 376 | FP | FP | 切片代码仅展示了宏定义和函数框架，未显示对指针's'进行解引用的具体操作或明确的空指针传递路径。告警指向的宏UPDATE_CACHE在切片中未展开其可能导致空指针解引用的实现，缺乏判定为真实空指针解引用的直接证据。 |
| 1818 | ffmpeg-6.1.1 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 切片代码显示，在告警行`s->st->time_base.den`被访问前，已存在条件`s->st->time_base.den`的检查`s->ic->nb_streams > 1`，且`s->st`在函数上下文中应为有效指针；更重要... |
| 1819 | ffmpeg-6.1.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 412 | FP | FP | 切片代码显示，在访问 `ctx->buffers[buf.index]` 之前，`buf.index` 来自 `ioctl` 系统调用 `VIDIOC_DQBUF` 的返回结果，该操作由内核驱动填充，且 `ctx->buffers` ... |
| 1820 | ffmpeg-6.1.1 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | FP | 切片代码显示，在访问 `frame->pts` 之前，存在 `if (!in && context->input_frames >= 8) return 0;` 和 `if (in && context->input_frames <... |
| 1821 | ffmpeg-6.1.1 | ebml_read_binary | Dereference of null pointer | 1087 | FP | FP | 切片代码显示，在调用`memset`之前，`av_buffer_realloc`函数已被调用并成功返回（`ret < 0`为假），这确保了`bin->buf`和`bin->buf->data`是有效的非空指针，因此不会发生空指针解引用。 |
| 1822 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问 `ptr[2*x]` 和 `ptr[2*x+1]` 之前，`ptr` 指向 `p->data[0]`，该指针由 `ff_get_buffer` 分配并成功返回，且循环条件 `x < (w + 7 >> 3) * ... |
| 1823 | ffmpeg-6.1.1 | vc1_decode_intra_block | Dereference of null pointer | 964 | FP | FP | 切片代码显示，在调用 `ff_vc1_pred_dc` 函数时，`dc_val` 指针作为参数 `dc_val_ptr` 被传入，该函数内部将 `*dc_val_ptr` 设置为 `&dc_val[0]`（即一个有效的非空地址）。因此... |
| 1824 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 切片代码显示，在访问 `in->data[plane]` 之前，`in` 指针作为函数参数传入且未被修改，并且在 `s->depth <= 8` 和 `else` 分支中，`in` 都被直接使用，表明其非空。此外，`out` 指针在可... |
| 1825 | ffmpeg-6.1.1 | unsharp_slice_16 | Dereference of null pointer | 141 | FP | FP | 切片代码显示，在宏展开的函数定义中，`sc` 和 `sr` 等指针在解引用前已从 `fp` 结构体中获取，且存在对 `amount` 的检查，逻辑上确保了指针的有效性。告警点位于宏定义行，是对宏展开后代码的误判，切片内未见实际的空指针... |
| 1826 | ffmpeg-6.1.1 | enc_open | Dereference of null pointer | 271 | FP | FP | 切片代码显示，在访问 `ost->ist->par->width` 和 `ost->ist->par->height` 之前，已通过 `if (!enc_ctx->width)` 进行条件判断，且告警点位于 `switch (enc_... |
| 1827 | ffmpeg-6.1.1 | ebml_parse | Dereference of null pointer | 1353 | FP | FP | 切片代码中，在警告行访问`level->length`之前，已通过条件`matroska->num_levels > 0`确保`level`指针非空，且`level`是从`matroska->levels`数组中有效获取的，因此不会发... |
| 1828 | ffmpeg-6.1.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码中，`UPDATE_CACHE` 是一个宏，其展开不涉及对指针 `gb` 的直接解引用；且宏 `BITS_AVAILABLE` 被定义为常量 1，表明循环条件可控，未提供 `gb` 为空的证据。基于切片可见的逻辑，该告警为误报。 |
| 1829 | ffmpeg-6.1.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 切片代码中，对指针 `s` 的访问发生在函数参数接收之后，且函数内部逻辑是常规的位操作，没有证据表明传入的 `s` 指针为 NULL。告警点 `s->bit_buf` 是访问结构体成员，这本身不构成空指针解引用，除非调用者传入 NUL... |
| 1830 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码显示告警行是对一个指针进行解引用和移位操作，该指针 `src` 是函数参数，其有效性由调用者保证。在切片可见的上下文和 `encode_line` 函数中，没有证据表明 `src` 为 NULL 或会导致空指针解引用。 |
| 1831 | ffmpeg-6.1.1 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 切片代码显示，在调用`av_rescale_q`之前，已对`av_packet_new_side_data`的返回值`prft`进行了空指针检查，若为空则提前返回错误，因此后续对`s->st`的访问不会在`prft`为空时发生。 |
| 1832 | ffmpeg-6.1.1 | ebml_read_sint | Dereference of null pointer | 1014 | FP | FP | 切片代码显示，在调用avio_r8函数时，其内部有明确的边界检查（`s->buf_ptr >= s->buf_end`）和缓冲区填充逻辑，这确保了函数返回一个有效值（或0），不会返回空指针。因此，对avio_r8返回值的解引用是安全的... |
| 1833 | ffmpeg-6.1.1 | safe_filename | Dereference of null pointer | 97 | FP | FP | 在循环条件 `for (; *f; f++)` 中，对指针 `f` 的解引用 `*f` 发生在检查 `*f` 是否为真（即不为空字符 `'\0'`）之后，这是安全的。该告警是对空指针解引用的逻辑误判，实际代码逻辑确保了指针在解引用前已... |
| 1834 | ffmpeg-6.1.1 | try_push_frame | Dereference of null pointer | 538 | FP | FP | 切片代码显示，在访问`s->input_frames[0]`之前，已经通过`if (!nb_samples) goto eof;`检查，其中`nb_samples`的计算依赖于`s->input_frames[i]`的有效性。当`nb... |
| 1835 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，在访问 `in->linesize[plane]` 之前，`in` 指针仅在 `s->filter` 为假时可能为 NULL，但此时 `out` 被赋值为 `in`，后续的 `if (!out)` 分支会为 `out` ... |
| 1836 | ffmpeg-6.1.1 | ff_encode_encode_cb | Dereference of null pointer | 285 | FP | FP | 切片代码显示，在访问 `frame->duration` 之前，已经通过 `if (frame && (codec->caps_internal & FF_CODEC_CAP_EOF_FLUSH))` 条件以及外层 `if (!ret... |
| 1837 | ffmpeg-6.1.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 切片代码仅展示了宏定义和内联函数的展开，没有提供任何关于指针`s`来源、初始化或可能为空的上下文。在缺乏具体证据表明`s`为null的情况下，无法确认存在空指针解引用，因此判定为误报。 |
| 1838 | ffmpeg-6.1.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码中，变量 `dpd` 在条件判断 `if (dpd[pos])` 中被直接使用，但其来源和初始化在切片中不可见。由于切片是判断告警的核心依据，且未提供 `dpd` 可能为空的证据，无法确认存在空指针解引用。基于切片内可见信息，... |
| 1839 | ffmpeg-6.1.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1476 | FP | FP | 切片代码显示`scale_matrix`在访问前已通过条件`s->ps.sps->scaling_list_enable_flag && !(transform_skip_flag && log2_trafo_size > 2)`进行... |
| 1841 | ffmpeg-6.1.1 | hls_read_header | Dereference of null pointer | 2123 | FP | FP | 切片代码显示在访问 `in_fmt->name` 之前，`in_fmt` 已通过 `av_demuxer_iterate` 或 `av_probe_input_buffer` 被正确赋值，且存在空指针检查。告警点位于条件分支 `if ... |
| 1842 | ffmpeg-6.1.1 | hls_append_segment | Dereference of null pointer | 1173 | FP | FP | 切片代码显示，在警告行`if (!en->next->discont_program_date_time && !en->discont_program_date_time)`之前，`en`被赋值为`vs->segments`，而`v... |
| 1843 | ffmpeg-6.1.1 | concat_parse_script | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `file->user_duration` 之前，`file` 指针已在 `DIR_FILE` 分支中通过 `add_file` 函数成功初始化并赋值。该函数确保 `file` 指向有效内存，且 `DIR_DUR... |
| 1844 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 297 | FP | FP | 切片代码显示，在解引用 `src` 指针之前，函数 `encode_plane` 的调用者已传入有效的 `src` 参数，且切片内没有证据表明 `src` 可能为空。告警点 `((uint16_t*)(src + stride*y))... |
| 1845 | ffmpeg-6.1.1 | kalman_smoothen | Dereference of null pointer | 584 | FP | FP | 切片代码显示，在解引用 `best_hist_ptr` 之前，存在条件判断 `if (optimal_gain <= 0) return -1;`，这确保了只有当 `optimal_gain > 0` 时才会继续执行，而 `optim... |
| 1846 | ffmpeg-6.1.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在访问dp1和dp2指针前，存在条件判断`if (dpd[pos])`，这确保了只有在`dpd[pos]`非零时才进行解引用。虽然dp1和dp2的定义未在切片中明确，但根据上下文模式，它们很可能与dpd类似，是已初始化的... |
| 1847 | ffmpeg-6.1.1 | id3v2_parse | Dereference of null pointer | 1054 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 获取的，该函数仅在找到匹配的标签时才返回非空指针。调用点位于 `extra_func &&... |
| 1848 | ffmpeg-6.1.1 | choose_rct_params | Dereference of null pointer | 983 | FP | FP | 切片代码显示告警行访问的 src[1] 和 src[2] 是函数参数，在切片内没有证据表明它们可能为 NULL。函数逻辑在循环内正常使用这些指针，且告警点位于 else 分支，该分支仅在 lbd 为假时执行，切片未显示 lbd 状态与... |
| 1849 | ffmpeg-6.1.1 | split_commandline | Dereference of null pointer | 731 | FP | FP | 切片代码显示，在访问 `opt[0]` 和 `opt[1]` 之前，变量 `opt` 被赋值为 `argv[optindex++]`，而 `argv` 是命令行参数数组，在循环条件 `optindex < argc` 的保护下，`ar... |
| 1850 | ffmpeg-6.1.1 | ebml_read_ascii | Dereference of null pointer | 1069 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，不会实际解引用任何指针，因此不存在解引用空指针的逻辑错误。 |
| 1851 | ffmpeg-6.1.1 | output_packet | Dereference of null pointer | 1102 | FP | FP | 切片代码显示，在访问 `timestamp_packet->unwritten_size` 之前，`timestamp_packet` 被赋值为 `stream->premux_packet`，而 `stream` 来自 `ctx->... |
| 1853 | ffmpeg-6.1.1 | concat_parse_script | Dereference of null pointer | 561 | FP | FP | 切片代码显示，在访问`file->inpoint`之前，`file`指针已在`DIR_FILE`指令分支中通过`add_file`函数成功初始化并赋值。此外，`DIR_INPOINT`指令的执行受`NEEDS_FILE`标志保护，确保... |
| 1854 | ffmpeg-6.1.1 | ost_add | Dereference of null pointer | 1456 | FP | FP | 切片代码中，在访问 `ist->st->duration` 之前，存在条件 `if (ost->ist && ost->ist->st->duration > 0)` 对 `ist` 指针进行了非空检查，并且检查了其成员 `st` 的... |
| 1855 | ffmpeg-6.1.1 | sb_decode | Dereference of null pointer | 1346 | FP | FP | 切片代码显示，在访问 `innov_save` 指针前，已通过 `if (st->innov_save)` 检查其是否为空，并且仅在非空时才会执行 `innov_save[2 * i] = exc[i];` 这行告警代码，因此不会发生... |
| 1856 | ffmpeg-6.1.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警指向的代码行位于条件分支 `if ((*child)->state * 2 == -t->state)` 内部，该分支仅在 `t->state` 非零且 `t->state` 为偶数时才会进入。切片代码显示，在进入此分支前，`*c... |
| 1857 | ffmpeg-6.1.1 | check_header_mismatch | Dereference of null pointer | 520 | FP | FP | 切片代码显示，在访问 `header->link_penalty[i]` 之前，`i` 的值由 `for` 循环控制，且循环条件 `i < FLAC_MAX_SEQUENTIAL_HEADERS && curr != child` 确... |
| 1858 | ffmpeg-6.1.1 | get_pict_type | Dereference of null pointer | 135 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，`slice` 指针来源于 `unit->content`，而 `unit` 是 `pu->units[i]` 的地址，其有效性由循环条件 `i ... |
| 1859 | ffmpeg-6.1.1 | ogg_write_header | Dereference of null pointer | 628 | FP | FP | 切片代码显示告警行仅是对结构体成员进行赋值，并未发生对空指针的解引用操作。工具报告的'空指针解引用'逻辑错误在提供的代码上下文中不成立。 |
| 1860 | ffmpeg-6.1.1 | mpegts_open_filter | Dereference of null pointer | 493 | FP | FP | 切片代码显示，在调用av_log时，其第一个参数`ts->stream`可能为NULL，但av_log宏被定义为`while(0)`，这意味着该调用在编译后不会生成任何实际代码，因此不会发生空指针解引用。 |
| 1861 | ffmpeg-6.1.1 | guess_mv | Dereference of null pointer | 428 | FP | FP | 切片代码中，在警告行（else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])）访问 s->last_pic.f->data[0] 之前，已经存在前置条件检查（if (s... |
| 1862 | ffmpeg-6.1.1 | fg_output_frame | Dereference of null pointer | 2111 | FP | FP | 切片代码显示，在告警行使用`frame->pts`之前，函数`video_sync_process`已被调用，该函数内部包含对`frame`指针的显式空值检查（`if (!frame) { ... }`），这表明在后续逻辑中`fram... |
| 1863 | ffmpeg-6.1.1 | build_table | Dereference of null pointer | 204 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 1864 | ffmpeg-6.1.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `chapters[i]` 之前，存在条件判断 `if (chapters && nb_chapters)` 和 `for (int i = 0; i < nb_chapters; i++)`，这确保了当 `ch... |
| 1865 | ffmpeg-6.1.1 | locate_option | Dereference of null pointer | 424 | FP | FP | 在切片代码中，`po` 指针仅在 `find_option` 函数返回后使用，而 `find_option` 函数保证返回一个指向 `OptionDef` 结构体的指针（即使未找到匹配项，也会返回指向数组末尾的指针，该指针的 `nam... |
| 1866 | ffmpeg-6.1.1 | guess_status_pts | Dereference of null pointer | 462 | FP | FP | 切片代码显示，在访问 `ctx->inputs[i]` 指针前，循环条件 `i < ctx->nb_inputs` 确保了 `i` 在有效范围内，但未直接验证 `ctx->inputs[i]` 本身是否为 NULL。然而，在典型的FF... |
| 1867 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 切片代码显示，在指针解引用之前，存在对指针 `in` 的明确赋值（`out = s->filter ? NULL : in;`）和条件判断（`if (!out)`），并且 `in` 是函数参数，在切片可见范围内没有证据表明其为空。宏 ... |
| 1868 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 332 | FP | FP | 切片代码显示，在告警行使用outlink之前，存在条件判断`s->do_video`，且当`s->do_video`为真时，outlink在函数开头被赋值为`ctx->outputs[1]`，不为NULL。因此，在访问outlink-... |
| 1869 | ffmpeg-6.1.1 | av_dump_format | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `printed` 数组前，已通过条件 `if (ic->nb_streams && !printed) return;` 确保当 `ic->nb_streams` 非零时 `printed` 不为空。告警点 `... |
| 1870 | ffmpeg-6.1.1 | check_header_mismatch | Dereference of null pointer | 476 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 的循环中，`curr` 指针通过 `curr = curr->next;` 遍历链表，且循环条件 `while (curr != child)` 确保了 `curr... |
| 1871 | ffmpeg-6.1.1 | update_context_from_thread | Dereference of null pointer | 366 | FP | FP | 切片代码中，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 进行了条件检查，并且 `hwacce... |
| 1872 | ffmpeg-6.1.1 | choose_rct_params | Dereference of null pointer | 984 | FP | FP | 切片代码显示，在解引用 `src[2]` 指针之前，函数已通过 `for (p = 0; p < 3; p++)` 循环和 `lbd` 条件分支对数据访问路径进行了控制，且 `src` 数组作为参数传入，在切片可见上下文中没有证据表明... |
| 1873 | ffmpeg-6.1.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 切片代码显示，在调用UPDATE_CACHE_32宏之前，函数已通过av_assert2宏对输入参数n进行了断言检查，并且宏展开后涉及对指针gb的访问，但该指针s作为函数参数，其有效性由调用者保证且在切片内未见明确的空指针解引用证据。... |
| 1874 | ffmpeg-6.1.1 | activate | Dereference of null pointer | 186 | FP | FP | 切片代码显示，在访问frame->pts之前，frame指针要么通过ff_get_video_buffer分配（已检查NULL），要么通过av_frame_clone分配（已检查NULL），或者frame来自ff_inlink_con... |
| 1875 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 199 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被分配内存（`ptr2 = av_malloc_array(...)`），且后续循环 `for ... |
| 1876 | ffmpeg-6.1.1 | h264_field_start | Dereference of null pointer | 1426 | FP | FP | 切片代码显示，在访问 `sps->log2_max_frame_num` 之前，`sps` 指针已通过 `h264_init_ps` 函数成功初始化并赋值，且该函数在成功时返回 `ret >= 0` 才会继续执行。因此，`sps` 指... |
| 1877 | ffmpeg-6.1.1 | ff_encode_encode_cb | Dereference of null pointer | 282 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，该行访问 `frame->pts`。切片代码显示，在进入此条件分支前，外层存在 `if (!ret && *got_packet)` 和... |
| 1878 | ffmpeg-6.1.1 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 切片代码显示，在告警行 `buf[0] & 0xc0` 之前，函数开头已对 `buf` 指针进行了空值检查（`if (!buf) { ... }`），并且当 `len < 12` 时函数会提前返回，确保了后续访问 `buf` 时其不为... |
| 1879 | ffmpeg-6.1.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，`dpd` 指针已通过三元条件运算符从 `out->data` 数组的已知有效索引（`s->pd` 或 0）中赋值，且 `out` 指针已在函数参数中传入，因此 `dpd` 为 nul... |
| 1880 | ffmpeg-6.1.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1442 | FP | FP | 切片代码显示，在调用 `ff_get_audio_buffer` 前已对 `frame` 指针进行了非空检查（通过 `av_frame_is_writable` 调用），且 `ff_get_audio_buffer` 内部有安全处理，... |
| 1881 | ffmpeg-6.1.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 切片代码显示`s->buffer`是一个数组访问，`index >> 3`计算字节偏移，这是典型的位读取操作。在函数上下文中，`s`和`s->buffer`的有效性应由调用者保证，且该行代码本身不构成对空指针的解引用。告警很可能是工具... |
| 1882 | ffmpeg-6.1.1 | asf_parse_packet | Dereference of null pointer | 1306 | FP | FP | 切片代码中，在警告行（for循环条件检查）之前，已经通过`av_new_packet`为`asf_st->pkt.data`分配了内存，并且有检查`asf_st->pkt.data`是否为NULL的逻辑。循环条件是检查数据是否为零，而... |
| 1883 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 148 | FP | FP | 切片代码显示，在访问alpSrcPtr指针前，已通过条件`(CONFIG_SWSCALE_ALPHA && hasAlpha)`进行检查，仅当条件为真时alpSrcPtr才被赋值非NULL值，否则为NULL。在告警行使用该指针时，外层... |
| 1884 | ffmpeg-6.1.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在告警行`dp1[pos] = s->tint[0];`之前，存在条件判断`if (dpd[pos])`，这表明对指针`dp1`的访问受限于`dpd[pos]`为真，且`dpd`在切片中未显示为空。代码逻辑表明存在前置检... |
| 1885 | ffmpeg-6.1.1 | avc_parse_nal_units | Dereference of null pointer | 92 | FP | FP | 切片代码显示，在警告行（`list->nb_nalus >= nalu_limit`）中，`list` 指针仅在 `pb` 为 `NULL` 时才会被解引用，而 `list` 作为函数参数，其有效性由调用者保证。警告行之前的 `if ... |
| 1886 | ffmpeg-6.1.1 | unsharp_slice_8 | Dereference of null pointer | 142 | FP | FP | 切片代码显示，在宏展开的函数中，指针 `sc` 在 `memset` 调用前已从 `fp->sc` 获取，且 `sc` 被用于数组索引 `sc[sc_offset + y]`，这表明 `sc` 本身非空。告警点 `{ NULL }` ... |
| 1887 | ffmpeg-6.1.1 | mov_write_trak_tag | Dereference of null pointer | 3818 | FP | FP | 切片代码中，告警行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 在访问 `st->sample_aspect_ratio` 前，已通过条件 `if (... |
| 1888 | ffmpeg-6.1.1 | ebml_parse | Dereference of null pointer | 1370 | FP | FP | 切片代码显示，在告警行（line 1370）访问`level`指针前，已通过`if (matroska->num_levels > 0)`检查确保`level`有效，且该行位于`else if (level->length != EB... |
| 1889 | ffmpeg-6.1.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码中，`dpd` 指针来源于 `out->data[s->pd]` 或 `out->data[0]`，这些是 AVFrame 结构体的有效数据指针，在正常上下文中不应为空。告警点 `dpd[pos]` 的访问发生在指针已明确指向... |
| 1890 | ffmpeg-6.1.1 | get_bits_le | Dereference of null pointer | 361 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE_LE 的调用处，该宏展开后对参数 gb 的访问是间接的。在函数入口处，参数 s 未进行空指针检查，但根据函数 get_bits_le 的上下文和FFmpeg编码惯例，调用者应确保传入... |
| 1891 | ffmpeg-6.1.1 | ac3_apply_rematrixing | Dereference of null pointer | 411 | FP | FP | 切片代码中未定义变量 `flags`，无法确认其来源或是否为空。告警点 `if (flags[bnd])` 的 `flags` 可能是一个有效的数组指针，因为其后续被用于索引访问，且切片中未见其被赋值为空或存在空指针检查。基于切片内可... |
| 1892 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 682 | FP | FP | 切片代码显示，在调用FFSWAP宏之前，已经通过条件`if (js_databuf == q->decoded_bytes_buffer)`确保了`ptr1`和`ptr2`都指向有效的缓冲区，不会发生空指针解引用。 |
| 1893 | ffmpeg-6.1.1 | ff_rdt_parse_header | Dereference of null pointer | 200 | FP | FP | 切片代码中，在警告行（while循环条件）访问`buf[1]`之前，函数参数`buf`和`len`已作为非空指针传入，且`init_get_bits`函数内部有对`buffer`为空的检查。在切片可见的上下文中，没有证据表明`buf`... |
| 1894 | ffmpeg-6.1.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 切片代码显示，在访问 `info->key_ids[i]` 之前，函数已通过 `if (info)` 检查确保 `info` 指针非空，并且 `info->key_ids` 的访问发生在该保护条件内，因此不会发生空指针解引用。 |
| 1895 | ffmpeg-6.1.1 | shift_frame | Dereference of null pointer | 153 | FP | FP | 切片代码显示，`av_log` 被宏定义为 `while(0)`，这意味着该函数调用在编译后为空操作，不会发生对 `frame` 指针的解引用，因此不存在空指针解引用风险。 |
| 1896 | ffmpeg-6.1.1 | build_table | Dereference of null pointer | 170 | FP | FP | 切片代码显示告警行`int bits = table[j].len;`中的`table`指针在`alloc_table`调用成功且`table_index >= 0`后已通过`table = &vlc->table[table_ind... |
| 1897 | ffmpeg-6.1.1 | ff_inlink_evaluate_timeline_at_frame | Dereference of null pointer | 1485 | FP | FP | 切片代码显示，告警行`int64_t pts = frame->pts;`中的指针`frame`是函数参数，在调用前已由调用者确保非空，且告警规则`Dereference of null pointer`针对的是逻辑错误而非空指针解引... |
| 1898 | ffmpeg-6.1.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], side_data, key_id_size)` 之前，`info->key_ids` 数组及其每个元素已通过 `av_encryption_init_info... |
| 1899 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 168 | FP | FP | 切片代码显示，在解引用alpMmxFilter指针前，已通过条件`(CONFIG_SWSCALE_ALPHA && hasAlpha)`检查alpSrcPtr是否为NULL，告警行位于该条件保护块内，因此不会发生空指针解引用。 |
| 1900 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 658 | FP | FP | 切片代码显示 `UPDATE_CACHE` 是一个宏定义，其展开为 `UPDATE_CACHE_LE`，告警点位于宏调用处，并未直接解引用指针。在 `get_vlc2` 函数中，`s` 和 `table` 作为参数传入，但切片中未提供... |
| 1901 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在深度大于8的分支中，变量 `linesize` 的计算包含条件判断 `s->planeheight[plane] > 1`，当条件不满足时 `linesize` 被赋值为0，这可能导致后续指针运算 `val[(x) +... |
| 1902 | ffmpeg-6.1.1 | mov_write_trak_tag | Dereference of null pointer | 3823 | FP | FP | 切片代码中，在调用 `is_clcp_track(track)` 之前，已经通过 `if (track->mode == MODE_MOV)` 进行了条件检查，并且 `is_clcp_track` 函数内部仅访问 `track->ta... |
| 1903 | ffmpeg-6.1.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后仅涉及位读取操作，且传入的指针 's' 在函数入口处未进行空指针检查。然而，该函数为内联辅助函数，其调用上下文（未在切片中提供）很可能已确保指针非空。基于静态分析... |
| 1904 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 471 | FP | FP | 切片代码中，DECODE_CODEWORD 是一个宏，其内部包含 GET_CACHE 等操作，但未展示可能导致空指针解引用的具体赋值或调用路径。告警点 `DECODE_CODEWORD(code, FIRST_DC_CB, LAST_... |
| 1905 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 291 | FP | FP | 切片代码显示告警点位于一个数组索引赋值操作（sample[0][x] = src[x * pixel_stride + stride * y]），该操作在循环边界内，且src指针作为函数参数传入，其有效性应在调用前确保。切片中未显示s... |
| 1906 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 686 | FP | FP | 切片代码显示，在警告行（`q->decoded_bytes_buffer[i] = *ptr2--;`）之前，`js_databuf` 被检查是否等于 `q->decoded_bytes_buffer`，如果不等，`ptr2` 被赋值... |
| 1907 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 691 | FP | FP | 切片代码显示，在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确初始化为 `q->decoded_bytes_buffer`，这是一个有效的缓冲区指针。循环内还有边... |
| 1908 | ffmpeg-7.1 | show_bits | Dereference of null pointer | 376 | FP | FP | 切片代码仅展示了宏定义和函数框架，未显示对指针's'进行解引用的具体操作或明确的空指针传递路径。告警指向的宏UPDATE_CACHE在定义中未直接解引用指针，且缺乏上下文证明's'为null，因此判定为误报。 |
| 1909 | ffmpeg-7.1 | finalize_packet | Dereference of null pointer | 678 | FP | FP | 切片代码显示，在告警行`s->st->time_base.den`被访问前，存在条件`s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->ic->nb_streams > 1`，且`s->st`... |
| 1910 | ffmpeg-7.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 413 | FP | FP | 切片代码显示，在访问 `ctx->buffers` 数组前，存在对 `ctx->buffers` 是否为空的检查（`if (!ctx->buffers) break;`），并且 `avbuf = &ctx->buffers[buf.i... |
| 1911 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 299 | FP | FP | 切片代码显示，在调用 `encode_line` 函数前，`src` 指针作为参数传入，并在循环中用于计算地址和读取数据，没有证据表明 `src` 为 NULL。告警点 `((uint16_t*)(src + stride*y))[x... |
| 1912 | ffmpeg-7.1 | roq_dpcm_encode_frame | Dereference of null pointer | 180 | FP | FP | 在告警行`avpkt->pts = context->input_frames <= 7 ? context->first_pts : frame->pts;`中，只有当`context->input_frames > 7`时才会解引... |
| 1913 | ffmpeg-7.1 | ebml_read_binary | Dereference of null pointer | 1095 | FP | FP | 切片代码显示，在调用 `memset` 之前，`av_buffer_realloc` 函数已被调用并成功返回（`ret < 0` 的检查已通过），这确保了 `bin->buf` 及其 `data` 字段已被正确分配且非空。因此，对 `... |
| 1914 | ffmpeg-7.1 | <global> | Dereference of null pointer | 209 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被 `av_malloc_array` 分配内存，且分配失败时函数会提前返回 `AVERROR(... |
| 1916 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 切片代码显示，在告警行`uint8_t *val = in->data[plane];`之前，`in`指针作为函数参数传入，且后续被直接使用，表明其非空。此外，在`s->filter`为假时`out`被赋值为`in`，进一步确认`in... |
| 1917 | ffmpeg-7.1 | unsharp_slice_16 | Dereference of null pointer | 172 | FP | FP | 切片代码中，宏定义 `DEF_UNSHARP_SLICE_FUNC` 展开后，告警行 `{ NULL }` 是函数体的一部分，但该函数体在宏展开后已被完整的实现代码所替代，不存在空指针解引用。工具可能误报了宏定义处的语法结构。 |
| 1918 | ffmpeg-7.1 | ebml_parse | Dereference of null pointer | 1363 | FP | FP | 切片代码中，在访问 `level->length` 之前，存在条件 `if (matroska->num_levels > 0)` 确保 `level` 指针不为 NULL，因为 `level` 是从 `matroska->level... |
| 1919 | ffmpeg-7.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码中，`UPDATE_CACHE` 是一个宏，其展开不涉及对 `gb` 指针的直接解引用；告警点所在的宏调用本身不构成空指针解引用。代码逻辑在切片可见范围内是安全的，工具可能误报了宏展开的逻辑。 |
| 1920 | ffmpeg-7.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 切片代码中，对指针`s`的访问发生在函数参数接收之后，且函数内部逻辑未显示`s`可能为空。告警点`s->bit_buf`的访问是安全的，因为`s`作为函数参数传入，在调用上下文中应已被检查。 |
| 1921 | ffmpeg-7.1 | rtp_set_prft | Dereference of null pointer | 646 | FP | FP | 切片代码显示，在调用`av_rescale_q`之前，已对`av_packet_new_side_data`的返回值`prft`进行了空指针检查，若为空则直接返回错误。因此，在后续使用`s->st`时，`s`和`s->st`在切片内未... |
| 1922 | ffmpeg-7.1 | ebml_read_sint | Dereference of null pointer | 1022 | FP | FP | 切片代码显示，avio_r8函数内部有缓冲区边界检查，当缓冲区耗尽时会调用fill_buffer或返回0，不会直接导致空指针解引用。告警点`*num = sign_extend(avio_r8(pb), 8)`中的avio_r8返回值... |
| 1923 | ffmpeg-7.1 | safe_filename | Dereference of null pointer | 98 | FP | FP | 切片代码显示，在for循环条件`*f`中解引用指针`f`之前，已通过函数参数`const char *f`传入，且循环条件`*f`本身是检查指针是否指向字符串结束符，这是安全的空值检查方式。代码逻辑是遍历字符串直到结束，不存在解引用空... |
| 1925 | ffmpeg-7.1 | dump_stream_group | Dereference of null pointer | 788 | FP | FP | 切片代码显示，在访问 `stg->streams[i]` 之前，存在对 `stg->nb_streams` 的检查（`stg->nb_streams &&`），这确保了循环仅在流数量大于0时执行，且 `stg` 本身在 `switch... |
| 1926 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，在访问 `in->linesize[plane]` 之前，存在条件 `s->planeheight[plane] > 1` 作为保护。当 `planeheight` 不大于1时，`linesize` 被赋值为0，从而避免... |
| 1927 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 236 | FP | FP | 切片代码显示，在访问 `frame->format` 之前，存在 `av_assert0(frame ｜｜ (enc->type != AVMEDIA_TYPE_VIDEO && enc->type != AVMEDIA_TYPE_A... |
| 1928 | ffmpeg-7.1 | ff_encode_encode_cb | Dereference of null pointer | 275 | FP | FP | 切片代码显示，在访问 `frame->duration` 之前，外层条件 `if (!ret && *got_packet)` 已确保 `ret` 为0且 `*got_packet` 为真，并且 `if (frame && ...)`... |
| 1929 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 219 | FP | FP | 告警指向的代码行位于一个av_assert0宏调用内部，该宏在条件不满足时会调用abort()终止程序。切片代码显示，该断言仅在编码器类型为音频且frame指针非空时才会执行，且该断言检查的是frame结构体内部字段的有效性，而非指针... |
| 1930 | ffmpeg-7.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后是对结构体指针 `s` 的操作。函数 `get_sbits` 的参数 `s` 在切片中未显示其来源，但作为内联函数，其调用者应保证传入有效的指针。此外，该函数是F... |
| 1931 | ffmpeg-7.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码中，变量 `dpd` 在条件判断 `if (dpd[pos])` 中被直接使用，但其来源和初始化在切片中不可见。由于切片是判断告警的核心依据，且未提供 `dpd` 可能为空的证据，无法确认存在空指针解引用。基于切片内可见信息，... |
| 1932 | ffmpeg-7.1 | try_push_frame | Dereference of null pointer | 241 | FP | FP | 切片代码显示，在访问 `inbuf[0]->pts` 之前，`inbuf` 数组已通过 `ff_inlink_consume_samples` 调用进行填充，该函数在成功时会设置 `*rframe`（即 `inbuf[i]`）为非空指... |
| 1933 | ffmpeg-7.1 | hls_append_segment | Dereference of null pointer | 1183 | FP | FP | 在警告行`if (!en->next->discont_program_date_time && !en->discont_program_date_time)`之前，代码已通过`en = vs->segments;`将`en`指向链... |
| 1934 | ffmpeg-7.1 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 切片代码显示，在访问 `file->user_duration` 之前，`file` 指针已在 `DIR_FILE` 分支通过 `add_file` 函数成功初始化并赋值，且存在 `if (!file)` 的全局性空指针检查。因此，在... |
| 1935 | ffmpeg-7.1 | dump_argument | Dereference of null pointer | 516 | FP | FP | 切片代码显示函数参数 `a` 在循环条件 `for (p = a; *p; p++)` 中被直接解引用，这要求 `a` 不能为 NULL。该函数是静态的，其调用上下文未知，但根据常见的编码模式，此类打印参数的函数通常由调用者确保传入有... |
| 1936 | ffmpeg-7.1 | kalman_smoothen | Dereference of null pointer | 585 | FP | FP | 在切片代码中，`best_hist_ptr` 在循环中被赋值，且仅在 `optimal_gain > 0` 和 `dot > 0` 的条件下才会被后续使用。如果 `optimal_gain <= 0` 或 `dot <= 0`，函数会... |
| 1937 | ffmpeg-7.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在访问dp1和dp2之前，存在条件判断`if (dpd[pos])`，这确保了dpd[pos]不为零，从而间接表明dp1和dp2指向的内存位置是有效的，因为它们在同一个循环和上下文中被使用。没有直接证据表明dp1或dp2... |
| 1938 | ffmpeg-7.1 | id3v2_parse | Dereference of null pointer | 1055 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 获取的，该函数仅在找到匹配的标签时才返回非空指针。告警点位于 `else` 分支，该分支仅... |
| 1939 | ffmpeg-7.1 | set_bframe_chain_length | Dereference of null pointer | 1590 | FP | FP | 在告警行`s->input_picture[i - 1]->f->data[0]`处，切片代码显示其位于`s->b_frame_strategy == 1`的条件分支内，且外层有`if (s->input_picture[i] && ... |
| 1940 | ffmpeg-7.1 | split_commandline | Dereference of null pointer | 809 | FP | FP | 切片代码显示，在访问 `opt[1]` 之前，存在对 `opt[0]` 和 `opt[1]` 的明确检查（`if (opt[0] == '-' && opt[1] == '-' && !opt[2])`），并且 `opt` 是来自 `... |
| 1941 | ffmpeg-7.1 | ebml_read_ascii | Dereference of null pointer | 1077 | FP | FP | 切片代码显示 `av_free` 被定义为 `while(0)` 宏，这是一个空操作，不会发生空指针解引用。同时，`av_malloc` 被定义为 `NULL`，但告警点 `av_free(*str)` 的解引用发生在宏展开之前，且宏... |
| 1942 | ffmpeg-7.1 | output_packet | Dereference of null pointer | 1103 | FP | FP | 切片代码显示，在访问 `timestamp_packet` 指针之前，`best_i` 已通过循环被赋值为一个非负整数，确保了 `ctx->streams[best_i]` 和后续的 `stream->premux_packet` 访... |
| 1943 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 286 | FP | FP | 切片代码中，在访问 `ost->ist->par` 之前，`ost` 和 `ost->ist` 的有效性已在函数入口处通过 `av_assert0` 宏间接保证（该宏在条件失败时会中止程序），且告警行位于 `enc_ctx->code... |
| 1944 | ffmpeg-7.1 | ebml_read_uint | Dereference of null pointer | 1002 | FP | FP | 切片代码显示指针 `num` 在解引用前已被赋值（`*num = 0;`），且函数入口处有对 `num` 的赋值操作，表明指针已被使用，逻辑上不会出现空指针解引用。 |
| 1945 | ffmpeg-7.1 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 切片代码显示，在DIR_INPOINT指令执行前，必须通过DIR_FILE指令成功调用add_file函数来初始化file指针。DIR_FILE指令执行失败会通过FAIL宏跳转到fail标签，因此当执行到`file->inpoint ... |
| 1946 | ffmpeg-7.1 | sb_decode | Dereference of null pointer | 1348 | FP | FP | 切片代码显示，在访问 `innov_save` 指针前，已通过 `if (st->innov_save)` 检查其是否为空，并且当条件成立时，`innov_save` 被赋值为 `st->innov_save + 2 * offset... |
| 1947 | ffmpeg-7.1 | choose_rct_params | Dereference of null pointer | 990 | FP | FP | 切片代码中，`src[1]` 和 `src[2]` 作为函数参数传入，在 `lbd` 为假的分支中被直接解引用。告警点位于对 `src[1]` 的访问。由于函数签名显示 `src` 是一个指向 `const uint8_t*` 数组的... |
| 1948 | ffmpeg-7.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 切片代码显示，在警告行`if ((*child)->state * 2 == -t->state)`之前，`child`指针被赋值为`&t->child[i]`，而`t`在函数入口已确认非空。进入该条件分支的前提是`t->state`... |
| 1949 | ffmpeg-7.1 | check_header_mismatch | Dereference of null pointer | 519 | FP | FP | 切片代码中，在警告行`curr = curr->next;`之前，循环条件`curr != child`和`i < FLAC_MAX_SEQUENTIAL_HEADERS`确保了`curr`不会为NULL。此外，紧随其后的`av_as... |
| 1950 | ffmpeg-7.1 | get_pict_type | Dereference of null pointer | 136 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，`slice` 指针来源于 `unit->content`，而 `unit` 是 `pu->units[i]` 的地址，其有效性由循环条件 `i ... |
| 1951 | ffmpeg-7.1 | ogg_write_header | Dereference of null pointer | 629 | FP | FP | 切片代码显示对指针 `oggstream` 进行了成员访问，但未提供其定义或初始化上下文。在典型的代码模式中，此处的 `oggstream` 很可能是一个已分配的结构体指针，否则函数无法正常工作。基于常见实践和切片中缺乏明确的空指针证... |
| 1952 | ffmpeg-7.1 | mpegts_open_filter | Dereference of null pointer | 495 | FP | FP | 切片代码显示，在调用av_log时，其参数ts->stream是作为第一个参数传入的，而ts是函数的输入参数，其有效性由调用者保证。更重要的是，av_log宏被定义为空操作（while(0)），因此该行代码不会对任何指针进行解引用，不... |
| 1953 | ffmpeg-7.1 | guess_mv | Dereference of null pointer | 432 | FP | FP | 切片代码显示，在访问 `s->last_pic.f->data[0]` 之前，存在条件检查 `if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])`，这确保了指针不为空。因此，... |
| 1954 | ffmpeg-7.1 | build_table | Dereference of null pointer | 204 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 1955 | ffmpeg-7.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `chapters[i]` 之前，存在条件判断 `if (chapters && nb_chapters)` 和 `if (m)`，并且 `chapters[i]` 仅在 `for (int i = 0; i <... |
| 1957 | ffmpeg-7.1 | <global> | Dereference of null pointer | 78 | FP | FP | 切片代码显示，UPDATE_CACHE是一个宏，其展开不涉及直接的指针解引用，且告警点所在的代码路径（#else分支）在调用UPDATE_CACHE前已通过OPEN_READER宏初始化了读取器，没有证据表明传入的gb指针为null或... |
| 1958 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 切片代码显示，在深度大于8的分支中，`val` 指针被赋值为 `(uint16_t *)in->data[plane]`，而 `in` 是函数参数，在调用前已存在且非空，因此 `val` 不会是空指针。告警点是对 `val` 的赋值而... |
| 1959 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 333 | FP | FP | 切片代码显示，在访问 `outlink` 指针的 `time_base` 成员之前，存在 `if (s->do_video)` 条件保护。当 `s->do_video` 为假时，`outlink` 被初始化为 NULL，但该代码路径不... |
| 1960 | ffmpeg-7.1 | av_dump_format | Dereference of null pointer | 898 | FP | FP | 切片代码显示，在访问`printed`数组前，存在条件`if (ic->nb_streams && !printed) return;`，当`printed`为NULL时会提前返回，避免了空指针解引用。后续使用`printed`的循环... |
| 1961 | ffmpeg-7.1 | check_header_mismatch | Dereference of null pointer | 475 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 之前，`curr` 指针通过 `curr = curr->next;` 在 while 循环中遍历，且循环条件 `curr != child` 确保了 `curr`... |
| 1962 | ffmpeg-7.1 | update_context_from_thread | Dereference of null pointer | 438 | FP | FP | 切片代码中，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 进行了条件检查，并且 `hwacce... |
| 1963 | ffmpeg-7.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 切片代码显示，在调用UPDATE_CACHE_32宏之前，函数已通过OPEN_READER宏初始化读取器，并且告警点位于一个已进行参数有效性断言（av_assert2）的函数内。宏展开后，对指针‘gb’（即参数‘s’）的访问是受保护的... |
| 1964 | ffmpeg-7.1 | activate | Dereference of null pointer | 186 | FP | FP | 切片代码显示，在访问`frame->pts`之前，`frame`变量要么通过`ff_get_video_buffer`分配（已检查非空），要么通过`av_frame_clone`分配（已检查非空），或者来自`ff_inlink_con... |
| 1965 | ffmpeg-7.1 | <global> | Dereference of null pointer | 200 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回 `AVERROR(ENOMEM)`，因此 `ptr2` 不可能为 NULL。 |
| 1966 | ffmpeg-7.1 | check_available | Dereference of null pointer | 616 | FP | FP | 切片代码中，`cu` 指针在函数开头从 `lc->cu` 获取，`lc` 作为参数传入且未被修改，因此 `cu` 在后续使用前不太可能为 NULL。告警行对 `cu->pred_mode` 的访问发生在 `cu` 被解引用之后，且没有... |
| 1967 | ffmpeg-7.1 | ff_encode_encode_cb | Dereference of null pointer | 272 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，该行代码 `avpkt->pts = frame->pts;` 仅在 `frame` 指针非空时才会执行。切片代码显示，包含该行的整个代... |
| 1968 | ffmpeg-7.1 | rtp_parse_one_packet | Dereference of null pointer | 888 | FP | FP | 切片代码显示，在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，函数开头已对 `buf` 指针进行了空值检查（`if (!buf) { ... }`），并且当 `len < 12... |
| 1969 | ffmpeg-7.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，`dpd` 指针已通过三元条件运算符从 `out->data` 数组的有效成员中赋值，且 `out` 指针作为函数参数传入，在切片上下文中未见其为空的证据。因此，对 `dpd` 的访问... |
| 1971 | ffmpeg-7.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1420 | FP | FP | 切片代码显示`scale_matrix`在解引用前已通过条件`sps->scaling_list_enabled && !(transform_skip_flag && log2_trafo_size > 2)`进行保护，并且当该条件... |
| 1972 | ffmpeg-7.1 | nal_parse_units | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `list->nalus` 之前，已通过 `if (!tmp)` 检查了 `av_fast_realloc` 的返回值，若分配失败则直接返回错误，因此不会发生空指针解引用。 |
| 1973 | ffmpeg-7.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1513 | FP | FP | 切片代码显示，在调用 `ff_get_audio_buffer` 之前，`frame` 指针已通过 `AVFrame *frame = *rframe;` 获取，并作为参数传递给 `av_frame_is_writable(frame... |
| 1974 | ffmpeg-7.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 切片代码显示`s->buffer`被直接索引访问，但函数`get_bits1`是内联辅助函数，其调用者应确保`GetBitContext *s`及其`buffer`成员有效。在典型的比特流读取上下文中，缓冲区会在高级函数中预先分配和验... |
| 1975 | ffmpeg-7.1 | asf_parse_packet | Dereference of null pointer | 1307 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data[i]` 之前，已通过 `av_new_packet` 或 `av_packet_new_side_data` 等函数为 `asf_st->pkt.data` 分配了内存，并且有 ... |
| 1976 | ffmpeg-7.1 | <global> | Dereference of null pointer | 146 | FP | FP | 切片代码显示，在解引用alpSrcPtr指针之前，已通过条件`(CONFIG_SWSCALE_ALPHA && hasAlpha)`进行检查，仅当条件为真时alpSrcPtr才为非NULL。告警行位于该条件为真的代码块内，因此不会发生... |
| 1977 | ffmpeg-7.1 | choose_rct_params | Dereference of null pointer | 991 | FP | FP | 切片代码显示告警行位于 `lbd` 为 false 的 else 分支中，该分支访问 `src[1]` 和 `src[2]`。虽然切片未直接展示 `src` 数组的初始化，但函数签名和上下文表明 `src` 是调用者传入的指针数组，且... |
| 1978 | ffmpeg-7.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，对指针 `dpd` 的访问 `if (dpd[pos])` 发生在对 `dst[3]` 的非空检查 `if (dst[3])` 之后，且 `dpd` 很可能指向 `dst[3]` 的数据，这表明存在前置的指针有效性防护，... |
| 1979 | ffmpeg-7.1 | unsharp_slice_8 | Dereference of null pointer | 173 | FP | FP | 切片代码显示，在宏展开的函数定义中，对指针 `sc` 的访问 `sc[sc_offset + y]` 发生在对其有效性进行明确检查（`if (!amount)`）和初始化（`memset`）之后，且 `sc` 来自结构体成员 `fp-... |
| 1980 | ffmpeg-7.1 | mov_write_trak_tag | Dereference of null pointer | 4187 | FP | FP | 切片代码中，在告警行访问 `st->sample_aspect_ratio` 之前，函数参数 `st` 已在多处被直接使用（如 `mov_write_tkhd_tag` 调用），且未进行空指针检查，这表明调用者保证 `st` 非空。告... |
| 1981 | ffmpeg-7.1 | ebml_parse | Dereference of null pointer | 1380 | FP | FP | 切片代码中，在访问 `level->length` 之前，存在条件 `if (level && level->length == EBML_UNKNOWN_LENGTH)` 和 `if (matroska->num_levels > ... |
| 1982 | ffmpeg-7.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码中，`dpd`指针指向`out->data`数组的有效元素，且循环边界由`out->width`和`out->height`控制，数组访问`dpd[pos]`、`dpd[pos-1]`等均在有效索引范围内，未发现空指针解引用。... |
| 1983 | ffmpeg-7.1 | get_bits_le | Dereference of null pointer | 361 | FP | FP | 切片代码仅展示了宏定义和函数框架，未显示`s`指针的获取或校验逻辑。在典型的FFmpeg代码中，`GetBitContext`指针通常由调用者保证非空，且宏展开本身不直接解引用空指针。基于切片内缺乏明确的空指针解引用证据，倾向于判定为误报。 |
| 1984 | ffmpeg-7.1 | ac3_apply_rematrixing | Dereference of null pointer | 598 | FP | FP | 切片代码中，`flags` 变量未定义，其来源和初始化在切片中不可见。告警基于假设 `flags` 可能为空指针，但切片内没有证据表明 `flags` 在解引用前未被正确初始化或分配。基于切片可见的上下文，无法确认存在空指针解引用，因... |
| 1985 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 683 | FP | FP | 切片代码显示，在调用FFSWAP宏之前，`ptr1`和`ptr2`都已被正确初始化并指向有效的缓冲区（`q->decoded_bytes_buffer`或其偏移位置），不存在空指针解引用。 |
| 1986 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 303 | FP | FP | 切片代码显示，在调用 `encode_line` 函数前，`sample` 数组已通过 `sc->sample_buffer` 正确初始化并分配了内存，且 `sample[0]` 指向有效的缓冲区地址。告警点 `sample[0][x... |
| 1987 | ffmpeg-7.1 | ff_rdt_parse_header | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在告警行（while循环条件）访问buf[1]之前，函数参数buf作为指针被传入，但未在切片内看到其被赋值为NULL的路径。同时，调用init_get_bits函数时内部有对buffer参数的NULL检查，这间接表明调用... |
| 1988 | ffmpeg-7.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 切片代码显示，在访问 `info->key_ids[i]` 之前，函数已通过 `if (info)` 检查确保 `info` 指针非空，并且 `info->key_ids` 的访问发生在该保护条件内，因此不存在对空指针的解引用。 |
| 1989 | ffmpeg-7.1 | shift_frame | Dereference of null pointer | 152 | FP | FP | 切片代码显示，在引用`frame->pts`的同一行，`av_log`被宏定义为`while(0)`，这意味着该行代码实际上不会被执行，因此不可能发生空指针解引用。 |
| 1990 | ffmpeg-7.1 | build_table | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功（返... |
| 1991 | ffmpeg-7.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用memcpy访问info->key_ids[j]之前，已通过av_encryption_init_info_alloc函数分配了内存，并且该函数内部对key_id_size为0或分配失败的情况进行了检查和处理，确保... |
| 1992 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 293 | FP | FP | 切片代码显示，在调用encode_line函数前，sample[0]数组已通过sample[i] = sc->sample_buffer + ...进行初始化，指向有效的缓冲区，不存在空指针解引用。告警点处的sample[0][x]赋... |
| 1993 | ffmpeg-7.1 | dump_stream_group | Dereference of null pointer | 715 | FP | FP | 切片代码中，告警行 `printed[st->index] = 1;` 使用的指针 `st` 未在切片内定义或初始化，但该行位于 `for (int k = 0; channel_count > 0 && k < stg->nb_st... |
| 1994 | ffmpeg-7.1 | <global> | Dereference of null pointer | 166 | FP | FP | 切片代码显示，在解引用alpMmxFilter指针之前，已通过条件`(CONFIG_SWSCALE_ALPHA && hasAlpha)`检查alpSrcPtr是否为NULL，并且alpMmxFilter仅在alpSrcPtr非空时被... |
| 1995 | ffmpeg-7.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的调用，但切片代码显示该宏最终展开为 UPDATE_CACHE_LE，其具体实现未在切片中提供。由于缺乏宏展开后的具体指针操作代码，无法确认存在空指针解引用。基于切片内可见信息，没有证据表明传入的... |
| 1996 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在计算 `linesize` 时存在条件判断 `s->planeheight[plane] > 1`，当条件不满足时 `linesize` 被赋值为 0，这避免了除以零或无效指针访问。后续使用 `linesize` 的宏... |
| 1997 | ffmpeg-7.1 | set_bframe_chain_length | Dereference of null pointer | 1605 | FP | FP | 切片代码显示，在访问`s->input_picture[i]`的`b_frame_score`成员之前，存在条件`if (s->input_picture[i] && s->input_picture[i]->b_frame_scor... |
| 1998 | ffmpeg-7.1 | mov_write_trak_tag | Dereference of null pointer | 4192 | FP | FP | 切片代码中，在调用 `is_clcp_track(track)` 之前，`track` 指针作为函数参数传入，且函数内多处已直接使用 `track->` 成员，表明 `track` 非空。告警点 `st->sample_aspect_... |
| 1999 | ffmpeg-7.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后不直接涉及指针解引用。函数 get_bits 的参数 s 在切片中未显示为空指针的来源，且函数内部包含断言宏 av_assert2，表明存在运行时检查。基于切片可... |
| 2000 | ffmpeg-7.1 | <global> | Dereference of null pointer | 472 | FP | FP | 切片代码中未显示对指针`gb`或`out`进行空指针解引用。告警点位于宏`DECODE_CODEWORD`的调用处，该宏内部操作的是位缓存，不直接解引用传入的指针参数。代码逻辑在切片可见范围内是安全的。 |
| 2001 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 687 | FP | FP | 切片代码中，在警告行（`q->decoded_bytes_buffer[i] = *ptr2--;`）之前，`q->decoded_bytes_buffer` 已在 `else` 分支的上下文（`js_databuf != q->de... |
| 2002 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在解引用指针 `ptr1` 的循环前，`ptr1` 被明确初始化为指向 `q->decoded_bytes_buffer`，这是一个有效的缓冲区。此外，循环内部有边界检查（`i >= js_block_align`），确... |
| 2003 | ffmpeg-6.0 | show_bits | Dereference of null pointer | 366 | FP | FP | 切片代码仅展示了宏定义和函数框架，未显示对指针's'进行解引用的具体操作或任何可能导致空指针的赋值逻辑。告警点位于宏UPDATE_CACHE的调用处，但该宏及其相关宏的定义中并未直接解引用传入的指针，因此缺乏证据表明存在空指针解引用。 |
| 2004 | ffmpeg-6.0 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 切片代码显示，在访问 `s->st->time_base.den` 和 `s->st->time_base.num` 之前，已经存在条件 `s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->i... |
| 2005 | ffmpeg-6.0 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 408 | FP | FP | 切片代码显示，在访问 `ctx->buffers[buf.index]` 之前，`buf.index` 来自 `ioctl(VIDIOC_DQBUF)` 系统调用，该调用成功返回后应保证索引有效。此外，`ctx->buffers` 数... |
| 2006 | ffmpeg-6.0 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | FP | 在告警行`avpkt->pts = context->input_frames <= 7 ? context->first_pts : frame->pts;`中，只有当`context->input_frames <= 7`为假时才... |
| 2007 | ffmpeg-6.0 | ebml_read_binary | Dereference of null pointer | 1073 | FP | FP | 切片代码显示，在调用 `memset` 之前，`av_buffer_realloc` 函数已被调用并成功返回（`ret < 0` 的检查已通过），这确保了 `bin->buf` 及其 `data` 字段已被正确分配且非空。因此，对 `... |
| 2008 | ffmpeg-6.0 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回，因此不会发生空指针解引用。 |
| 2009 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 119 | FP | FP | 切片代码显示，在访问 `in->data[plane]` 之前，`in` 帧作为参数传入且未被置空，且函数逻辑中 `out` 帧可能为 `in` 帧或新分配，但 `in` 本身在切片中始终有效。告警点 `uint8_t *val = ... |
| 2010 | ffmpeg-6.0 | unsharp_slice_16 | Dereference of null pointer | 142 | FP | FP | 切片代码显示，在宏展开的函数定义中，`sc` 和 `sr` 等指针在解引用前已从 `fp` 结构体获取，且存在 `if (!amount)` 的早期返回路径，这降低了空指针解引用的可能性。告警点位于宏定义行，该行本身不包含解引用操作，... |
| 2011 | ffmpeg-6.0 | ebml_parse | Dereference of null pointer | 1339 | FP | FP | 切片代码中，在警告行（第1339行）使用`level`指针前，已通过条件`matroska->num_levels > 0`进行了检查，确保了`level`不为NULL。因此，对`level->length`的访问是安全的，不存在空指... |
| 2012 | ffmpeg-6.0 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码中，`UPDATE_CACHE` 是一个宏，其展开不涉及对指针 `gb` 的直接解引用。告警点所在的代码行是宏调用，且切片内未提供该宏展开后会导致空指针解引用的证据。结合提供的宏定义，该行代码本身不构成空指针解引用。 |
| 2013 | ffmpeg-6.0 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 切片代码中，在访问 `s->bit_buf` 之前，函数参数 `PutBitContext *s` 并未被检查是否为 NULL，但该函数为 `static inline` 辅助函数，其调用上下文不可见。然而，告警点 `bit_buf ... |
| 2014 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码中，`src` 作为函数参数传入，在循环内被用作指针偏移和类型转换的基础地址，但并未直接解引用 `src` 本身。告警指向的代码行是对 `((uint16_t*)(src + stride*y))[x]` 进行右移操作，这本质... |
| 2015 | ffmpeg-6.0 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 332 | FP | FP | 切片代码显示，在访问 `ctx->buffers[i]` 之前，存在 `if (!ctx->buffers)` 的检查，这可以防止对空指针的解引用。因此，在切片可见的上下文中，该空指针解引用警告是误报。 |
| 2016 | ffmpeg-6.0 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 切片代码显示，在调用`av_rescale_q`之前，已对`av_packet_new_side_data`的返回值`prft`进行了空指针检查，若为空则提前返回错误。因此，在后续使用`s->st`时，`s`和`s->st`在切片内已... |
| 2017 | ffmpeg-6.0 | ebml_read_sint | Dereference of null pointer | 1000 | FP | FP | 切片代码显示，在调用`avio_r8`函数读取数据前，函数内部已包含对缓冲区指针`buf_ptr`的边界检查，当指针越界时会调用`fill_buffer`或返回0，这提供了防护机制，避免了直接解引用空指针或无效指针。 |
| 2018 | ffmpeg-6.0 | safe_filename | Dereference of null pointer | 97 | FP | FP | 切片代码显示，在解引用指针 `f` 之前，`for` 循环的条件 `*f` 已确保 `f` 不为空指针，因此不会发生空指针解引用。 |
| 2019 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 117 | FP | FP | 切片代码显示，在访问 `in->linesize[plane]` 之前，存在条件 `s->planeheight[plane] > 1` 进行保护。当条件不满足时，`linesize` 被赋值为 0，避免了空指针解引用。因此，该告警是误报。 |
| 2020 | ffmpeg-6.0 | of_open | Dereference of null pointer | 2303 | FP | FP | 切片代码显示，在访问 `ost->enc_ctx->codec` 之前，存在 `if (ost->filter)` 条件判断，这表明 `ost` 指针可能已被检查或初始化，且告警行位于该条件块内，降低了空指针解引用的风险。此外，`os... |
| 2021 | ffmpeg-6.0 | ff_encode_encode_cb | Dereference of null pointer | 244 | FP | FP | 在切片代码中，访问 `frame->duration` 的代码行位于 `if (frame)` 条件检查之后，并且该行所在的代码块由 `if (frame && ...)` 条件保护。因此，当执行到该行时，`frame` 指针不可能为... |
| 2022 | ffmpeg-6.0 | get_sbits | Dereference of null pointer | 315 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE 的调用处，该宏展开为 UPDATE_CACHE_LE，仅涉及位读取操作。函数 get_sbits 的参数 s 在切片中未见为空指针的传入证据，且该函数是内联工具函数，通常由调用者保证... |
| 2023 | ffmpeg-6.0 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码中，变量 `dpd` 在条件判断 `if (dpd[pos])` 中被解引用，但 `dpd` 未在切片中定义或初始化，无法确认其为空指针。基于切片可见信息，无法断定存在空指针解引用，倾向于判定为工具误报。 |
| 2024 | ffmpeg-6.0 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1476 | FP | FP | 切片代码显示，在访问 scale_matrix[pos] 之前，存在条件检查 `if (s->ps.sps->scaling_list_enable_flag && !(transform_skip_flag && log2_traf... |
| 2026 | ffmpeg-6.0 | hls_read_header | Dereference of null pointer | 2131 | FP | FP | 切片代码显示，在解引用 `in_fmt` 指针之前，`in_fmt` 已在 `av_demuxer_iterate` 循环或 `av_probe_input_buffer` 调用中被赋值，且存在对 `seg` 和 `in_fmt->n... |
| 2027 | ffmpeg-6.0 | hls_append_segment | Dereference of null pointer | 1180 | FP | FP | 切片代码显示，在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 之前，`en` 被赋值为 `vs->segments`... |
| 2028 | ffmpeg-6.0 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 切片代码显示，在访问 `file->user_duration` 之前，`DIR_DURATION` 指令的执行受到 `(dir->flags & NEEDS_FILE) && !cat->nb_files` 的条件保护。只有当 `c... |
| 2029 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 297 | FP | FP | 切片代码显示，在指针解引用前，`src` 作为函数参数传入，其值在切片内未显示为空。告警点 `((uint16_t*)(src + stride*y))[x]` 的访问基于循环变量 `x` 和 `y`，这些变量受 `w` 和 `h` ... |
| 2030 | ffmpeg-6.0 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在访问 `dp1[pos]` 和 `dp2[pos]` 之前，存在条件 `if (dpd[pos])` 进行保护，这确保了指针解引用仅在 `dpd[pos]` 非零时发生，从而避免了空指针解引用。 |
| 2031 | ffmpeg-6.0 | id3v2_parse | Dereference of null pointer | 1051 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 函数获取的，该函数仅在找到匹配的标签时才返回非空指针。告警点位于 `else` 分支，该分... |
| 2032 | ffmpeg-6.0 | choose_rct_params | Dereference of null pointer | 979 | FP | FP | 切片代码显示告警行访问 src[1] 和 src[2] 发生在 lbd 为 false 的 else 分支中，但未提供 src 数组初始化的上下文。然而，函数参数 src 被声明为 const uint8_t *src[3]，表明它是... |
| 2033 | ffmpeg-6.0 | split_commandline | Dereference of null pointer | 713 | FP | FP | 切片代码显示，在访问 `opt[1]` 之前，已经存在条件 `if (opt[0] == '-' && opt[1] == '-' && !opt[2])` 检查了 `opt[1]`，这表明 `opt` 字符串长度至少为2，且告警行（... |
| 2034 | ffmpeg-6.0 | ebml_read_ascii | Dereference of null pointer | 1055 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 2035 | ffmpeg-6.0 | output_packet | Dereference of null pointer | 1092 | FP | FP | 切片代码显示，在访问 `timestamp_packet->unwritten_size` 之前，`timestamp_packet` 被赋值为 `stream->premux_packet`，而 `stream->premux_pa... |
| 2036 | ffmpeg-6.0 | ebml_read_uint | Dereference of null pointer | 980 | FP | FP | 切片代码显示，在告警行`*num = 0;`之前，函数已通过`if (size == 0)`分支对`num`指针进行了明确的解引用赋值`*num = default_value;`，这确保了`num`指针在该执行路径下是有效的，因此告... |
| 2037 | ffmpeg-6.0 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 切片代码显示，在访问 `file->inpoint` 之前，`file` 指针已在 `DIR_FILE` 分支通过 `add_file` 函数被正确初始化并赋值。此外，`DIR_INPOINT` 指令仅在 `(dir->flags &... |
| 2038 | ffmpeg-6.0 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警指向的代码行位于条件 `if ((*child)->state * 2 == -t->state)` 内部，该条件仅在 `t->state` 非零且 `t->state` 为偶数时才会进入。在切片代码中，`child` 指针来自 ... |
| 2039 | ffmpeg-6.0 | ogg_write_header | Dereference of null pointer | 628 | FP | FP | 切片代码显示对指针`oggstream`的直接解引用，但未提供其定义或初始化上下文。在典型的FFmpeg代码模式中，此类结构体指针通常由上层函数传入并已校验。基于切片内缺乏明确的空指针证据，倾向于判定为工具误报。 |
| 2040 | ffmpeg-6.0 | init_output_stream_encode | Dereference of null pointer | 3153 | FP | FP | 切片代码显示，对 `ost->ist->par` 的访问发生在 `enc_ctx->codec_type` 为 `AVMEDIA_TYPE_SUBTITLE` 且 `enc_ctx->width` 为 0 的条件下，但切片中未提供 `... |
| 2041 | ffmpeg-6.0 | guess_mv | Dereference of null pointer | 428 | FP | FP | 切片代码中，在告警行（else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])）访问 s->last_pic.f 之前，已经存在前置条件检查（if (s->last_pi... |
| 2042 | ffmpeg-6.0 | build_table | Dereference of null pointer | 203 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `alloc_table` 成功分配内存并赋值，且 `j` 的值由 `code_prefix` 计算而来，其范围受 `table_nb_bits` 限制，确... |
| 2043 | ffmpeg-6.0 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `chapters[i]` 之前，外层存在条件判断 `if (chapters && nb_chapters)` 和 `if (m)`，并且内部循环 `for (int i = 0; i < nb_chapter... |
| 2045 | ffmpeg-6.0 | guess_status_pts | Dereference of null pointer | 446 | FP | FP | 切片代码显示，在访问 `ctx->inputs[i]` 指针前，循环条件 `i < ctx->nb_inputs` 确保了 `i` 在有效索引范围内，且 `ctx->inputs` 数组的有效性由调用上下文保证。没有证据表明 `ctx... |
| 2046 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 148 | FP | FP | 切片代码显示，在警告行`uint16_t *val = (uint16_t *)in->data[plane];`之前，`in`帧作为参数传入且未在切片内被置空，因此`in->data[plane]`解引用是安全的。告警点不存在对空指... |
| 2047 | ffmpeg-6.0 | av_dump_format | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `printed` 数组前，存在条件 `if (ic->nb_streams && !printed) return;`，这确保了当 `ic->nb_streams` 非零且 `printed` 为 NULL 时... |
| 2048 | ffmpeg-6.0 | choose_rct_params | Dereference of null pointer | 980 | FP | FP | 切片代码显示，在访问 src[2] 之前，函数已通过循环条件 `for (p = 0; p < 3; p++)` 和 `lbd` 分支判断了数据流，且 src 数组作为参数传入，在切片可见上下文中没有证据表明 src[2] 为 NUL... |
| 2049 | ffmpeg-6.0 | activate | Dereference of null pointer | 168 | FP | FP | 切片代码显示，在访问`frame->pts`的代码路径中，`frame`变量要么通过`ff_get_video_buffer`分配（已检查非空），要么通过`av_frame_clone`从`s->cache_stop`克隆（也已检查非... |
| 2050 | ffmpeg-6.0 | <global> | Dereference of null pointer | 199 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被 `av_malloc_array` 分配内存或保持为 `NULL`，并在后续使用前被检查。在... |
| 2051 | ffmpeg-6.0 | ff_encode_encode_cb | Dereference of null pointer | 241 | FP | FP | 切片代码显示，在解引用 `frame->pts` 之前，存在条件 `if (frame && (codec->caps_internal & FF_CODEC_CAP_EOF_FLUSH))` 或 `if (frame)` 的检查，并... |
| 2052 | ffmpeg-6.0 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 切片代码显示，在解引用buf指针之前，函数开头已通过条件判断确保buf不为NULL（buf = bufptr ? *bufptr : NULL;），并且当buf为NULL时，函数会提前返回rtp_parse_queued_packet... |
| 2053 | ffmpeg-6.0 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，`dpd` 指针已通过三元条件运算符从 `out->data` 数组的已知有效索引（`s->pd` 或 0）中赋值，且 `out` 指针已在函数参数中传入，未发现其为空的证据。因此，该... |
| 2054 | ffmpeg-6.0 | ff_inlink_make_frame_writable | Dereference of null pointer | 1423 | FP | FP | 告警点位于`ff_get_audio_buffer(link, frame->nb_samples)`，但切片代码显示在调用前已通过`av_frame_is_writable(frame)`检查，且`frame`是函数参数`*rfra... |
| 2055 | ffmpeg-6.0 | get_bits1 | Dereference of null pointer | 381 | FP | FP | 切片代码显示`s->buffer`是一个数组访问，其指针`s`在函数调用时通常由调用者保证非空，且函数内部没有对`s`进行空指针解引用。告警针对的是数组元素访问，而非指针`s`本身，因此是误报。 |
| 2056 | ffmpeg-6.0 | asf_parse_packet | Dereference of null pointer | 1302 | FP | FP | 切片代码中，在警告行（for循环条件检查）之前，已经通过`av_new_packet`为`asf_st->pkt.data`分配了内存，并且有`av_assert0(asf_st)`确保`asf_st`非空。循环条件是检查数据包数据是... |
| 2057 | ffmpeg-6.0 | <global> | Dereference of null pointer | 148 | FP | FP | 切片代码显示，在访问 `alpSrcPtr` 指针前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，当条件不满足时 `alpSrcPtr` 被设为 `NULL`，而后续使用该指针时均受... |
| 2058 | ffmpeg-6.0 | add_interval | Dereference of null pointer | 1035 | FP | FP | 在切片代码中，对指针`ri`的访问仅在`ref >= 0`的条件分支内，此时`ri`被明确赋值为`&inter->inter[ref]`，该地址来自有效的数组索引，因此不会发生空指针解引用。 |
| 2059 | ffmpeg-6.0 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在访问 dp1[pos] 和 dp2[pos] 之前，存在条件判断 `if (dpd[pos])`，这确保了指针 `dpd` 在解引用前已被检查，因此不会发生空指针解引用。 |
| 2060 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 335 | FP | FP | 切片代码显示，在访问 `s->out->pts` 和 `s->out->duration` 的代码块之前，存在条件 `if (s->do_video)` 保护。当 `s->do_video` 为真时，前面的逻辑（`if (s->do_... |
| 2061 | ffmpeg-6.0 | unsharp_slice_8 | Dereference of null pointer | 143 | FP | FP | 切片代码中，宏定义 `DEF_UNSHARP_SLICE_FUNC` 展开的函数体开头对指针 `sc` 和 `sr` 的访问是安全的，因为它们是从传入的 `ThreadData *td` 结构体中正确获取的。告警点 `{ NULL }... |
| 2062 | ffmpeg-6.0 | ebml_parse | Dereference of null pointer | 1356 | FP | FP | 切片代码中，在警告行（line 1356）访问 `level` 指针前，已通过 `if (matroska->num_levels > 0)` 条件确保 `level` 不为 NULL，因此不会发生空指针解引用。 |
| 2063 | ffmpeg-6.0 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码中，对数组`dpd`的访问均在有效的边界检查（如`!j`、`j == (out->width - 1)`、`!i`、`i == (out->height - 1)`）保护下进行，不会发生越界访问。指针`dpd`指向有效的帧数据... |
| 2064 | ffmpeg-6.0 | get_bits_le | Dereference of null pointer | 351 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE_LE 内部，该宏对指针 `(gb)->buffer` 进行解引用。然而，函数 `get_bits_le` 的参数 `GetBitContext *s` 在切片中未显示其来源或空值检查... |
| 2065 | ffmpeg-6.0 | ac3_apply_rematrixing | Dereference of null pointer | 410 | FP | FP | 切片代码中，`flags` 变量未定义且来源未知，无法确认其为空指针。告警基于对未定义变量的假设，在切片可见范围内没有证据表明 `flags` 是空指针或会导致解引用错误。 |
| 2066 | ffmpeg-6.0 | av_encryption_init_info_free | Dereference of null pointer | 219 | FP | FP | 切片代码显示，在访问 `info->key_ids[i]` 之前，函数已通过 `if (info)` 检查确保 `info` 指针非空，并且 `info->key_ids` 的访问发生在该保护条件内，因此不存在对空指针的解引用。 |
| 2068 | ffmpeg-6.0 | build_table | Dereference of null pointer | 169 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 2069 | ffmpeg-6.0 | ff_inlink_evaluate_timeline_at_frame | Dereference of null pointer | 1466 | FP | FP | 切片代码显示，在解引用 `frame->pts` 之前，函数参数 `frame` 已通过调用链传入，且函数内部没有对其进行空指针检查。然而，该告警为逻辑错误，提示解引用空指针。考虑到 `ff_inlink_evaluate_timel... |
| 2070 | ffmpeg-6.0 | av_encryption_init_info_get_side_data | Dereference of null pointer | 278 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], side_data, key_id_size)` 之前，`av_encryption_init_info_alloc` 函数已为 `info->key_ids`... |
| 2071 | ffmpeg-6.0 | <global> | Dereference of null pointer | 168 | FP | FP | 切片代码显示，在解引用 `alpSrcPtr` 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，当条件不满足时 `alpSrcPtr` 被设为 `NULL`，而解引用操作仅在条件为... |
| 2072 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 146 | FP | FP | 切片代码显示，在计算 `linesize` 时存在条件判断 `s->planeheight[plane] > 1`，当条件不满足时 `linesize` 被赋值为 0，这避免了除以零或无效指针访问。后续使用 `linesize` 的宏... |
| 2073 | ffmpeg-6.0 | get_bits | Dereference of null pointer | 330 | FP | FP | 切片代码中未显示对指针's'进行空值检查，但该函数为内联辅助函数，其调用上下文（未在切片中提供）很可能已确保指针非空。此外，宏展开后对'gb'的访问是间接的，工具可能误判了宏的语义。基于常见编码模式，这更可能是误报。 |
| 2074 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 291 | FP | FP | 切片代码显示 `src` 作为函数参数传入，并在循环中被直接用于指针运算和数组索引，没有显式的空指针检查。然而，该告警点位于对 `src` 的索引访问处，而 `src` 在函数入口处并未被验证。但根据函数逻辑和FFmpeg编码器的典型... |
| 2075 | ffmpeg-6.0 | bits_priv_refill_32_be | Dereference of null pointer | 85 | FP | FP | 切片代码显示，在调用AV_RB32(bc->ptr)之前，存在条件判断`if (bc->ptr >= bc->buffer_end) return -1;`，这确保了bc->ptr不会越界访问无效内存，从而避免了空指针解引用。 |
| 2076 | git-2.46.0 | add_parents_only | Dereference of null pointer | 1929 | FP | FP | 在调用 `it->type` 之前，切片代码显示 `it` 可能为 NULL 的情况已被检查和处理（`if (!it && revs->ignore_missing) return 0;`），且 `get_reference` 函数在... |
| 2077 | git-2.46.0 | get_mode | Dereference of null pointer | 63 | FP | FP | 切片代码显示，在解引用 `special` 指针之前，函数已通过 `if (special && ...)` 检查其是否为非空，因此不会发生空指针解引用。 |
| 2079 | git-2.46.0 | crlf_to_git | Dereference of null pointer | 573 | FP | FP | 在告警行`unsigned char c = *src++;`之前，切片代码已包含条件`if (!buf && !src) return 1;`，当`src`为NULL时函数会提前返回，不会执行到解引用指针的循环。因此，在切片可见的上... |
| 2080 | git-2.46.0 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码显示，在警告行 `d = delta[c = (end += d)[-1]];` 之前，变量 `d` 已在循环条件 `while (lim - end >= d)` 中被使用，表明 `d` 在进入循环时已被初始化，且警告行是 ... |
| 2081 | git-2.46.0 | diffcore_merge_broken | Dereference of null pointer | 295 | FP | FP | 切片代码显示，在内层循环访问 `pp` 之前，外层循环已通过 `if (!p) continue;` 确保 `q->queue[i]` 非空，且内层循环从 `i+1` 开始，`pp` 来自同一队列 `q->queue[j]`。虽然未直... |
| 2082 | git-2.46.0 | parse_options_step | Dereference of null pointer | 900 | FP | FP | 切片代码显示，在访问 `ctx->opt` 之前（例如 `if (ctx->opt)` 和 `if (internal_help && *ctx->opt == 'h')`），`ctx->opt` 已被明确赋值为 `arg + 1` ... |
| 2083 | git-2.46.0 | rstrip_ref_components | Dereference of null pointer | 2117 | FP | FP | 切片代码中，在警告行 `for (i = 0; p[i]; p[i] == '/' ? i++ : *p++)` 处，`p` 被初始化为 `refname`，而 `refname` 是函数参数，由调用者传入。虽然 `refname` ... |
| 2084 | git-2.46.0 | parse_options | Dereference of null pointer | 1046 | FP | FP | 切片代码显示，在访问 `*ctx.opt` 之前，`ctx.opt` 已在 `parse_options_step` 函数中被显式初始化为 `NULL`，并且在 `PARSE_OPT_UNKNOWN` 分支中，`ctx.opt` 仅在... |
| 2085 | git-2.46.0 | process_entry | Dereference of null pointer | 3413 | FP | FP | 切片代码显示告警行位于RENAME_ONE_FILE_TO_TWO分支内，该分支仅在ci->ren2非空时执行，而前面的条件判断if (ci->ren2)确保了ci->ren2的有效性，因此b->path的赋值不会发生空指针解引用。 |
| 2086 | git-2.46.0 | verify_absent | Dereference of null pointer | 2526 | FP | FP | 告警点位于条件判断语句中，用于检查指针`o`和`ce`的成员，并非解引用空指针。切片代码显示`verify_absent_1`函数内部对`ce->name`等成员的访问均有前置条件保护（如`o->index_only ｜｜ !o->u... |
| 2087 | git-2.46.0 | show_pack_info | Dereference of null pointer | 1688 | FP | FP | 切片代码显示，指针 `chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，而在使用该指针的循环内部，访问 `chain_histogram` 的条件 `i... |
| 2088 | git-2.46.0 | output | Dereference of null pointer | 548 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 仅在 `j < b->nr` 的条件下被赋值，且 `b_util->matching` 在 `while (j < b-... |
| 2089 | git-2.46.0 | limit_list | Dereference of null pointer | 1492 | FP | FP | 切片代码显示，在标记的告警行（if (obj->flags & UNINTERESTING)）之前，obj 被明确赋值为 &commit->object，而 commit 是从 original_list 中通过 pop_commit... |
| 2090 | git-2.46.0 | add_lines_to_move_detection | Dereference of null pointer | 1055 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行动态扩容和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，确保了数... |
| 2091 | git-2.46.0 | limit_list | Dereference of null pointer | 1488 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量是从 `pop_commit` 函数返回的，该函数在栈非空时返回有效指针，在栈为空时返回 NULL。告警所在行的 `commit` 是在 `while (... |
| 2092 | git-2.46.0 | lstrip_ref_components | Dereference of null pointer | 2079 | FP | FP | 切片代码中，在警告行 `p[i]` 被访问前，循环条件 `p[i]` 已确保指针 `p` 指向的字符不为空（非 '\0'），因此不会发生对空指针的解引用。该警告是静态分析工具的逻辑误判。 |
| 2093 | git-2.46.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 切片代码显示，在指针`result`为空时，函数直接返回`map->default_value`，并未对空指针进行解引用操作。告警所指向的行是返回语句，而非解引用。 |
| 2094 | git-2.46.0 | coalesce_lines | Dereference of null pointer | 264 | FP | FP | 在告警行`newend = newend->prev;`之前，`newend`指针已在循环条件`if (directions[i][j] == MATCH)`的保护下，且`directions`数组已通过`CALLOC_ARRAY`正... |
| 2095 | git-2.46.0 | merge_ort_internal | Dereference of null pointer | 5217 | FP | FP | 切片代码显示，在警告行`opt->priv->call_depth--;`之前，存在对应的`opt->priv->call_depth++;`操作，且该操作位于循环内，每次迭代都会成对增减。切片中未见`opt->priv`为空的证据，... |
| 2096 | git-2.46.0 | process_parents | Dereference of null pointer | 1175 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，并且 `repo_parse_commit_gently` 调用失败时会 `continue`，这降低了 `p` 为无效的可能性。切片代码... |
| 2097 | git-2.46.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1364 | FP | FP | 切片代码显示告警行调用 `write_message` 时传递的 `msg->buf` 和 `msg->len` 来自参数 `msg`，该参数是一个指向 `struct strbuf` 的指针，在调用前未显式置空。告警假设 `msg`... |
| 2098 | git-2.46.0 | gather_stats | Dereference of null pointer | 51 | FP | FP | 切片代码显示函数入口处有明确的空指针检查 `if (!buf ｜｜ !size ｜｜ !stats) return;`，这确保了在访问 `buf` 之前指针的有效性，因此告警的潜在空指针解引用在实际执行路径中不会发生。 |
| 2099 | git-2.46.0 | append_strategy | Dereference of null pointer | 229 | FP | FP | 切片代码显示函数仅将指针存入数组，未对指针`s`进行解引用操作。告警消息描述的'解引用空指针'逻辑错误在提供的代码片段中并未发生。 |
| 2100 | git-2.46.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码中，函数参数 `array` 和 `value` 的来源未知，但函数内部逻辑是常规的数组赋值操作，没有直接的指针解引用空值证据。告警点 `array->v[array->nr++] = value;` 本身不构成对空指针的解引... |
| 2101 | git-2.46.0 | add_lines_to_move_detection | Dereference of null pointer | 1058 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行动态增长和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，确保了数... |
| 2102 | git-2.46.0 | coalesce_lines | Dereference of null pointer | 272 | FP | FP | 切片代码显示，在访问 `lline->prev` 之前，`lline` 被赋值为 `newend`，而 `newend` 在循环中通过 `newend = newend->prev;` 更新，其值来自链表遍历，不太可能为 NULL。更... |
| 2103 | git-2.46.0 | apply_one_fragment | Dereference of null pointer | 3025 | FP | FP | 切片代码显示，在访问 `postimage.line_allocated[postimage.nr - 1]` 之前，`postimage.nr` 已通过 `add_line_info` 函数递增，确保了数组索引有效。此外，访问操作位... |
| 2104 | git-2.46.0 | try_to_commit | Dereference of null pointer | 1698 | FP | FP | 切片代码显示，在调用 `commit_tree_extended` 函数前，`parents` 变量可能为 NULL，但该函数内部（切片中已包含）通过 `commit_list_count(parents)` 和循环处理 NULL 列... |
| 2105 | git-2.46.0 | prepare_attr_stack | Dereference of null pointer | 1013 | FP | FP | 切片代码显示，在警告行`*stack = info->prev;`之前，`info`被赋值为`*stack`，而`*stack`由`bootstrap_attr_stack`函数初始化确保非空。此外，后续循环`while ((*sta... |
| 2106 | git-2.46.0 | split_graph_merge_strategy | Dereference of null pointer | 2269 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，变量 `g` 已在 `while (g && ...)` 循环中被赋值或更新，且循环后的 `if (ctx->num_commit_graphs_a... |
| 2107 | git-2.46.0 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 切片代码显示，函数在`line == 0`时直接返回`data`，否则才进行指针运算。`ends`数组的访问依赖于参数`line`，但切片中未提供`ends`的来源或`line`的范围，无法确认`ends[line]`是否会导致空指针... |
| 2108 | git-2.46.0 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数体为空，没有实际的指针解引用操作，因此工具报告的'空指针解引用'逻辑错误不成立。 |
| 2109 | git-2.46.0 | find_bisection | Dereference of null pointer | 439 | FP | FP | 切片代码显示，在访问 `list->item` 之前，`list` 被赋值为 `last`，而 `last` 在循环中被确保为非空（因为循环条件 `p` 非空且 `last = p`）。此外，`best` 仅在 `do_find_bi... |
| 2110 | git-2.46.0 | verify_absent_1 | Dereference of null pointer | 2485 | FP | FP | 切片代码显示，在调用 `check_leading_path` 之前，函数已通过条件 `if (o->index_only ｜｜ !o->update)` 提前返回，确保了 `ce` 指针在后续使用前不会被解引用。此外，`ce` 作为... |
| 2111 | git-2.46.0 | merge_ref_iterator_advance | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 仅在 `selection & ITER_YIELD_CURRENT` 为真时被使用，而 `ITER_YIELD_CURRENT` 的选择... |
| 2112 | git-2.46.0 | try_to_commit | Dereference of null pointer | 1582 | FP | FP | 切片代码显示，在调用 `copy_commit_list(current_head->parents)` 之前，`current_head` 已通过 `parse_head` 函数成功获取，且当 `flags & AMEND_MSG`... |
| 2113 | git-2.46.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数`ce_path_match`的参数`ce`被直接用于宏`ce_namelen(ce)`和访问`ce->name`、`ce->ce_mode`。由于`ce`是函数参数，调用者必须提供有效的指针，且切片中未见任何对`c... |
| 2114 | git-2.46.0 | cmp_local_packs | Dereference of null pointer | 481 | FP | FP | 切片代码显示，函数`cmp_local_packs`仅在`local_packs`非空时被调用，且`pl`被初始化为`local_packs`，但`local_packs`是一个全局变量，其初始化状态在切片中不可见。然而，在函数入口处... |
| 2115 | git-2.46.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 677 | FP | FP | 切片代码显示，在解引用指针 `n`（即 `tws->next`）之前，已通过 `if (n)` 进行了明确的非空检查，确保了后续的 `n->buf.buf` 等访问是安全的，因此该空指针解引用告警是误报。 |
| 2116 | git-2.46.0 | unload_one_branch | Dereference of null pointer | 2049 | FP | FP | 切片代码显示，在访问 `e->active_next_branch` 之前，`e` 被赋值为 `active_branches`，而 `active_branches` 仅在 `cur_active_branches` 非零且满足循环... |
| 2117 | git-2.46.0 | process_entries | Dereference of null pointer | 4451 | FP | FP | 切片代码显示，对`dir_metadata.offsets.items[0].util`的访问发生在条件`dir_metadata.offsets.nr != 1`检查之后，该条件确保了数组至少有一个元素，因此不会发生空指针解引用。 |
| 2118 | git-2.46.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过 `string_list_append` 或 `string_list_app... |
| 2119 | git-2.46.0 | kwsprep | Dereference of null pointer | 502 | FP | FP | 切片代码显示，在访问 `curr->parent->maxshift` 之前，`curr` 是从 `kwset->trie->next` 开始遍历的，而 `kwset->trie` 在之前的逻辑中已被确保非空（例如在 `enqueue... |
| 2120 | git-2.46.0 | cmd_merge | Dereference of null pointer | 1529 | FP | FP | 切片代码显示告警行 `use_strategies[i]->attr` 在循环前已通过 `for (i = 0; i < use_strategies_nr; i++)` 确保 `i` 在有效范围内，且 `use_strategies... |
| 2121 | git-2.46.0 | get_ref_map | Dereference of null pointer | 545 | FP | FP | 切片代码显示，在警告所在行（for循环）使用`fetch_refspec`之前，已经通过条件判断（`if (refmap.nr)`）对其进行了赋值，确保它指向一个有效的结构体（`&refmap`或`&remote->fetch`）。`... |
| 2122 | git-2.46.0 | setup_scoreboard | Dereference of null pointer | 2841 | FP | FP | 切片代码显示，在访问 `c->parents` 之前，while 循环条件 `c->parents && ...` 已经对 `c->parents` 进行了非空检查，因此不会发生空指针解引用。 |
| 2123 | git-2.46.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在解引用 `sb->buf` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 检查其是否指向特殊缓冲区。当条件为真时，`sb->buf` 不为空，解引用是安全的；当条件为假时，执行的是... |
| 2125 | git-2.46.0 | assert_sane_strbuf | Dereference of null pointer | 36 | FP | FP | 切片代码显示，在解引用 `buf->buf` 之前，已通过 `check(!!buf->buf)` 宏对指针 `buf->buf` 进行了非空检查，这确保了后续的 `buf->buf[buf->len]` 访问不会解引用空指针。 |
| 2126 | git-2.46.0 | show_pack_info | Dereference of null pointer | 1710 | FP | FP | 切片代码显示，在访问 `chain_histogram[i]` 之前，`chain_histogram` 已通过 `CALLOC_ARRAY` 宏（即 `xcalloc`）分配了内存，该函数会返回已初始化为零的内存或失败退出。因此，`... |
| 2127 | git-2.49.0 | image_remove_last_line | Dereference of null pointer | 363 | FP | FP | 切片代码显示，在访问 `img->line[img->line_nr - 1]` 之前，函数 `image_remove_last_line` 的调用上下文未提供，无法确认 `img->line` 或 `img->line_nr` 是... |
| 2128 | git-2.49.0 | add_parents_only | Dereference of null pointer | 1941 | FP | FP | 在调用 `it->type` 之前，切片代码显示 `get_reference` 函数可能返回 NULL，但紧接着有 `if (!it && revs->ignore_missing) return 0;` 检查。当 `it` 为 N... |
| 2129 | git-2.49.0 | get_mode | Dereference of null pointer | 65 | FP | FP | 切片代码显示，在*special = SPECIAL_STDIN;赋值之前，path已与file_from_standard_input进行相等性比较，确认path非空且指向有效字符串常量，因此不会发生空指针解引用。 |
| 2131 | git-2.49.0 | <global> | Dereference of null pointer | 88 | FP | FP | 切片代码显示告警位于单元测试函数中，对指针'out'的访问前有明确的'check(out != NULL)'非空检查，确保了指针的有效性。该告警是静态分析工具对测试代码中安全访问模式的误判。 |
| 2132 | git-2.49.0 | crlf_to_git | Dereference of null pointer | 583 | FP | FP | 切片代码显示，在警告行（`unsigned char c = *src++;`）之前，函数已通过条件 `if (src && !len)` 和 `if (!buf && !src)` 对 `src` 指针进行了检查，确保在 `src`... |
| 2133 | git-2.49.0 | cwexec | Dereference of null pointer | 675 | FP | FP | 切片代码显示，在警告行 `d = delta[c = (end += d)[-1]];` 之前，变量 `d` 已在循环条件 `while (lim - end >= d)` 中被使用，表明 `d` 在进入循环时已被初始化且不为零，因此... |
| 2134 | git-2.49.0 | diffcore_merge_broken | Dereference of null pointer | 291 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环已确保 `pp` 是从 `q->queue[j]` 获取的，而外层循环已对 `q->queue[i]` 进行了空指针检查，且 `q->queue` 数组在初始化后未被整体置空，... |
| 2135 | git-2.49.0 | parse_options_step | Dereference of null pointer | 906 | FP | FP | 切片代码显示，在访问 `ctx->opt` 之前，存在 `if (ctx->opt)` 的条件检查，这防止了对空指针的解引用。告警点位于 `if (internal_help && *ctx->opt == 'h')`，但该行仅在 `... |
| 2136 | git-2.49.0 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | FP | 切片代码中，`p` 指针在 for 循环条件 `p[i]` 处被解引用，但 `p` 被初始化为非空的 `refname` 参数，且 `xstrdup` 函数确保了 `refname` 的有效性，因此 `p` 不可能为 null，不存在... |
| 2137 | git-2.49.0 | clar_summary_init | Dereference of null pointer | 76 | FP | FP | 切片代码显示，在解引用 `summary` 指针之前，`fopen` 调用失败时会通过 `clar_abort` 函数退出程序，因此 `summary` 指针不可能为 NULL 时执行到解引用行。 |
| 2138 | git-2.49.0 | parse_options | Dereference of null pointer | 1052 | FP | FP | 告警点位于检查 `isascii(*ctx.opt)` 处，但切片代码显示 `ctx->opt` 在 `parse_options_step` 函数开头被显式重置为 `NULL`，且后续赋值逻辑表明只有当解析到短选项（`arg[1] ... |
| 2139 | git-2.49.0 | <global> | Dereference of null pointer | 82 | FP | FP | 切片代码显示告警点位于单元测试中，`check(out != NULL)` 已确保 `out` 非空后才访问 `out[0]`，且 `parse_names` 函数在成功时返回非空指针，失败时返回 NULL 并提前退出测试。因此不存在... |
| 2141 | git-2.49.0 | verify_absent | Dereference of null pointer | 2537 | FP | FP | 切片代码显示，在告警行访问 `ce->ce_flags` 之前，函数 `verify_absent` 的调用者必须已经提供了有效的 `ce` 指针，且函数内部逻辑表明 `ce` 被直接传递给 `verify_absent_1` 并多次... |
| 2142 | git-2.49.0 | show_pack_info | Dereference of null pointer | 1776 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，随后在循环中访问该数组。访问发生在 `if (is_delta_type(obj->t... |
| 2143 | git-2.49.0 | output | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，存在条件 `if (j < b->nr)` 和 `if (i < a->nr && a_util->matching < 0)` 等逻辑，... |
| 2145 | git-2.49.0 | limit_list | Dereference of null pointer | 1499 | FP | FP | 切片代码显示告警行 `if (obj->flags & UNINTERESTING)` 中的 `obj` 指针来自 `&commit->object`，而 `commit` 指针在循环中由 `pop_commit` 返回，该函数在栈为... |
| 2146 | git-2.49.0 | add_lines_to_move_detection | Dereference of null pointer | 1060 | FP | FP | 切片代码显示，在访问 entry_list[l->id] 之前，l->id 的值由条件分支确定，并且当 l->id 等于 id 时，会调用 ALLOC_GROW_BY 来确保 entry_list 数组有足够的空间。ALLOC_GRO... |
| 2147 | git-2.49.0 | limit_list | Dereference of null pointer | 1495 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量来自 `pop_commit` 函数，该函数在栈非空时返回有效指针，在栈为空时返回 NULL。但在 `while (original_list)` 循环中... |
| 2148 | git-2.49.0 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | FP | 切片代码中，在警告行 `for (i = 0; p[i]; p[i] == '/' ? i++ : *p++)` 处，`p` 被初始化为 `refname`，而 `refname` 是函数参数，不可能为 NULL，因此对 `p[i]`... |
| 2149 | git-2.49.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 切片代码显示，在指针`result`为空时，函数直接返回`map->default_value`，并未对空指针进行解引用操作。告警的逻辑错误不成立。 |
| 2150 | git-2.49.0 | coalesce_lines | Dereference of null pointer | 251 | FP | FP | 在告警行 `newend = newend->prev;` 之前，`newend` 仅在 `directions[i][j] == MATCH` 分支中被赋值，而该分支仅在 `match_string_spaces` 返回真时进入，这... |
| 2151 | git-2.49.0 | merge_ort_internal | Dereference of null pointer | 5219 | FP | FP | 切片代码显示，在警告行（opt->priv->call_depth--;）之前，opt->priv->call_depth 已通过 opt->priv->call_depth++ 进行了递增，确保了指针 opt->priv 在递减前已... |
| 2152 | git-2.49.0 | assert_sane_strbuf | Dereference of null pointer | 35 | FP | FP | 切片代码显示，cl_assert 是一个单元测试宏，用于在测试失败时触发断言，并非在生产代码中无条件解引用空指针。该告警是针对测试框架逻辑的误报。 |
| 2153 | git-2.49.0 | process_parents | Dereference of null pointer | 1182 | FP | FP | 在切片代码中，对指针 `p` 的访问（`p->parents`）位于 `if (p)` 条件检查之后，该检查确保了 `p` 不为空。因此，在访问 `p->parents` 时，`p` 不可能为空指针，该告警为误报。 |
| 2154 | git-2.49.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1366 | FP | FP | 切片代码显示告警行调用的是 `write_message` 函数，该函数内部已对 `filename` 参数（即 `name`）进行了空指针检查（通过 `hold_lock_file_for_update` 和 `error_errn... |
| 2155 | git-2.49.0 | gather_stats | Dereference of null pointer | 52 | FP | FP | 切片代码显示函数入口处有`size`参数，循环条件`i < size`确保访问`buf[i]`时`i`在有效范围内，且`buf`作为参数传入，在切片可见上下文中没有证据表明`buf`为NULL或`size`无效，因此不存在空指针解引用。 |
| 2156 | git-2.49.0 | clar_parse_args | Dereference of null pointer | 496 | FP | FP | 切片代码显示，在访问 `argument[1]` 之前，外层循环 `for (i = 1; i < argc; ++i)` 确保了 `argv[i]` 不为空，且 `argument` 被赋值为 `argv[i]`。因此，`argum... |
| 2157 | git-2.49.0 | append_strategy | Dereference of null pointer | 234 | FP | FP | 切片代码显示函数接收一个指向结构体`strategy`的指针`s`，并将其存入数组。函数内部没有对`s`进行解引用操作，仅存储其地址。告警所指的行是数组赋值，并非解引用空指针。 |
| 2158 | git-2.49.0 | merge_ref_iterator_advance | Dereference of null pointer | 205 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 仅在 `ITER_YIELD_CURRENT` 分支中被使用，而该分支仅在 `iter->select` 函数返回特定标志时进入。虽然切片... |
| 2159 | git-2.49.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码中未显示对指针`array`或`array->v`的显式空值检查，但函数`strvec_push_nodup`的语义暗示调用者应确保传入有效的`struct strvec`。在典型的C语言库设计中，此类内部函数通常由已进行前置... |
| 2160 | git-2.49.0 | add_lines_to_move_detection | Dereference of null pointer | 1063 | FP | FP | 切片代码显示，在访问 entry_list[l->id] 之前，l->id 的值由条件分支确定，并且当 l->id 被赋值为 id 时，会调用 ALLOC_GROW_BY 来确保 entry_list 数组有足够的容量。ALLOC_G... |
| 2161 | git-2.49.0 | image_remove_first_line | Dereference of null pointer | 355 | FP | FP | 切片代码显示告警点是对 `strbuf_remove` 函数的调用，该函数内部仅调用 `strbuf_splice` 并传入空字符串和长度0。函数定义清晰，没有对空指针 `img` 或 `img->buf` 进行解引用操作，因此工具报... |
| 2162 | git-2.49.0 | coalesce_lines | Dereference of null pointer | 259 | FP | FP | 在告警行`if (lline->prev)`之前，`lline`被赋值为`newend`，而`newend`在循环中通过`newend = newend->prev;`更新，该赋值仅在`directions[i][j] == MATC... |
| 2163 | git-2.49.0 | write_table | Dereference of null pointer | 65 | FP | FP | 切片代码显示 `(*names)[i]` 的赋值来自 `xstrfmt` 的返回值，该函数返回有效字符串指针，不会为 NULL。同时，`refs` 和 `logs` 数组通过 `REFTABLE_CALLOC_ARRAY` 分配，确保... |
| 2164 | git-2.49.0 | strvec_splice | Dereference of null pointer | 69 | FP | FP | 切片代码显示，在告警行之前调用了ALLOC_GROW宏，该宏会确保array->v有足够的分配内存，因此对array->v的索引访问是安全的，不会解引用空指针。 |
| 2165 | git-2.49.0 | <global> | Dereference of null pointer | 30 | FP | FP | 切片代码仅显示一个空函数定义，没有指针解引用操作，因此工具报告的'空指针解引用'逻辑错误不成立。 |
| 2166 | git-2.49.0 | try_to_commit | Dereference of null pointer | 1700 | FP | FP | 切片代码显示告警行（commit_tree_extended调用）的参数均经过前置逻辑检查或赋值，未发现明显的空指针解引用路径。特别是parents、author、committer等指针在调用前已被合理初始化或由安全函数（如fmt_... |
| 2167 | git-2.49.0 | prepare_attr_stack | Dereference of null pointer | 978 | FP | FP | 切片代码显示，在解引用 `*stack` 之前，`bootstrap_attr_stack` 函数确保 `*stack` 不为空，且后续循环 `while ((*stack)->origin)` 和 `assert((*stack)-... |
| 2168 | git-2.49.0 | split_graph_merge_strategy | Dereference of null pointer | 2281 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，代码路径 `if (ctx->num_commit_graphs_after == 2)` 表明 `g` 变量可能为空，但切片代码显示，进入该分支的... |
| 2169 | git-2.49.0 | get_nth_line | Dereference of null pointer | 879 | FP | FP | 切片代码显示，当`line`为0时，函数直接返回`data`，避免了`ends[line]`的访问。只有当`line`不为0时才会访问`ends`数组，但此时`ends`指针是否为空取决于调用者传入的参数。在切片提供的有限上下文中，没... |
| 2170 | git-2.49.0 | <global> | Dereference of null pointer | 15 | FP | FP | 切片代码仅显示一个空函数定义，没有对指针进行解引用的操作，因此工具报告的'空指针解引用'逻辑错误在当前切片中不存在。 |
| 2171 | git-2.49.0 | find_bisection | Dereference of null pointer | 440 | FP | FP | 切片代码显示，在警告行`list->item = best->item;`之前，`best`指针已通过`do_find_bisection`函数返回，且该函数在`if (best)`条件内执行，确保了`best`非空。因此，对`bes... |
| 2172 | git-2.49.0 | <global> | Dereference of null pointer | 1541 | FP | FP | 切片代码显示，在访问 `use_strategies[i]->attr` 之前，`use_strategies` 数组已通过 `add_strategies` 函数初始化，且循环条件 `i < use_strategies_nr` 确... |
| 2173 | git-2.49.0 | verify_absent_1 | Dereference of null pointer | 2496 | FP | FP | 切片代码显示，在调用 `check_leading_path` 函数前，已通过条件 `if (o->index_only ｜｜ !o->update)` 进行了检查，若条件为真则直接返回0，不会执行到告警行。告警行处的 `ce` 指针... |
| 2174 | git-2.49.0 | <global> | Dereference of null pointer | 182 | FP | FP | 切片代码显示，在访问 `arr[0] = 42;` 之前，已经通过 `REFTABLE_ALLOC_GROW_OR_NULL` 宏进行了内存分配，并且紧随其后有 `check(arr != NULL);` 断言来确保指针非空。这表明代... |
| 2175 | git-2.49.0 | try_to_commit | Dereference of null pointer | 1584 | FP | FP | 切片代码显示，在告警行 `parents = copy_commit_list(current_head->parents);` 之前，`current_head` 已通过 `parse_head` 函数成功获取，且当 `flags ... |
| 2176 | git-2.49.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数`ce_path_match`的参数`ce`被直接用于宏`ce_namelen(ce)`和访问`ce->name`、`ce->ce_mode`。调用该函数的上下文未在切片中给出，但函数本身未对`ce`进行空值检查。然... |
| 2177 | git-2.49.0 | cmp_local_packs | Dereference of null pointer | 509 | FP | FP | 切片代码显示，函数cmp_local_packs被调用时，静态变量local_packs可能为NULL，但函数入口处将pl初始化为local_packs后，立即在if条件中解引用pl->next。然而，该函数是静态的，且local_p... |
| 2178 | git-2.49.0 | t_log_write_read | Dereference of null pointer | 224 | FP | FP | 切片代码中，`names[i] = xstrdup(name);` 调用的 `xstrdup` 函数内部已包含内存分配失败处理（`die`），因此 `names[i]` 不会为 NULL 指针。后续使用 `names[i]` 的代码（... |
| 2179 | git-2.49.0 | reftable_stack_reload_once | Dereference of null pointer | 351 | FP | FP | 切片代码显示，在告警行`new_readers[new_readers_len] = rd;`之前，`new_readers`已通过`reftable_calloc`分配了内存，且分配大小`names_len`与后续循环访问的边界一致... |
| 2180 | git-2.49.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 678 | FP | FP | 切片代码显示，在解引用指针 `n` 之前（例如 `n->buf.buf`），已经通过 `if (n)` 检查了其非空性，因此不会发生空指针解引用。 |
| 2181 | git-2.49.0 | unload_one_branch | Dereference of null pointer | 2065 | FP | FP | 切片代码显示，在解引用 `e->active_next_branch` 之前，`e` 被赋值为 `active_branches`，而 `active_branches` 仅在 `cur_active_branches && cur_... |
| 2182 | git-2.49.0 | cmd_add | Dereference of null pointer | 431 | FP | FP | 切片代码显示告警行是对结构体成员的直接赋值，而非解引用空指针。函数参数 `repo` 在切片中作为非空指针传入，且赋值操作本身不会导致空指针解引用。 |
| 2183 | git-2.49.0 | apply_one_fragment | Dereference of null pointer | 2991 | FP | FP | 切片代码中，在警告行（postimage.line[postimage.line_nr - 1].len--）之前，存在对 `postimage.line_nr` 的严格检查（`newlines.len > 0`），确保了数组访问不会... |
| 2184 | git-2.49.0 | process_entries | Dereference of null pointer | 4453 | FP | FP | 告警点位于一个BUG断言检查的printf语句中，该代码路径仅在内部一致性检查失败时执行，随后会调用BUG()宏终止程序。这属于防御性编程的错误处理逻辑，而非对正常运行时空指针的解引用。 |
| 2185 | git-2.49.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过 `string_list_append` 或 `string_list_app... |
| 2186 | git-2.49.0 | clar_run_suite | Dereference of null pointer | 399 | FP | FP | 切片代码显示，在报告行`report->suite = _clar.active_suite;`之前，`report`指针已通过`calloc`分配内存，且分配失败时会调用`clar_abort`退出程序，因此`report`不可能为... |
| 2187 | git-2.49.0 | kwsprep | Dereference of null pointer | 504 | FP | FP | 切片代码显示，在警告行`for (curr = kwset->trie->next; curr; curr = curr->next)`之前，`kwset->trie`已在多个循环中被访问且未发生空指针解引用，表明其已被正确初始化且非... |
| 2188 | git-2.49.0 | <global> | Dereference of null pointer | 188 | FP | FP | 切片代码显示告警行位于单元测试中，该行访问 `arr[alloc - 1]` 前已通过 `check(arr != NULL)` 和 `check_uint(alloc, >, old_alloc)` 确保了数组指针非空且索引有效，因... |
| 2189 | git-2.49.0 | get_ref_map | Dereference of null pointer | 545 | FP | FP | 切片代码显示，在警告行（for循环）之前，存在对`remote`指针的明确非空检查（`if (remote)`），并且`fetch_refspec`的赋值逻辑确保了它要么指向非空的`&refmap`，要么指向`remote->fetc... |
| 2190 | git-2.49.0 | setup_scoreboard | Dereference of null pointer | 2842 | FP | FP | 切片代码显示，在访问 `c->parents` 之前，`c` 被赋值为 `final_commit`，而 `final_commit` 仅在 `sb->reverse && sb->revs->first_parent_only` 条... |
| 2191 | git-2.49.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `sb->buf[len]` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 确保 `sb->buf` 不是指向只读缓冲区 `strbuf_slopbuf` 的指针，从而避免了... |
| 2192 | git-2.49.0 | t_table_refs_for | Dereference of null pointer | 577 | FP | FP | 切片代码显示 `want_names` 数组在循环中被 `xstrdup` 返回的指针填充，`xstrdup` 函数在内存分配失败时会调用 `die` 终止程序，因此 `want_names` 元素不会为 NULL。在循环结束后，`f... |
| 2194 | git-2.49.0 | show_pack_info | Dereference of null pointer | 1798 | FP | FP | 切片代码显示，在for循环访问chain_histogram[i]之前，存在条件判断`if (deepest_delta)`，当该条件为真时，会通过CALLOC_ARRAY宏（即xcalloc）为指针分配内存，该函数保证返回已初始化的... |
| 2195 | git-2.44.0 | add_parents_only | Dereference of null pointer | 1898 | FP | FP | 在调用 `it->type` 之前，切片代码显示 `it` 指针在 `if (!it && revs->ignore_missing)` 条件中已被检查，当 `it` 为 NULL 且 `revs->ignore_missing` 为... |
| 2196 | git-2.44.0 | table_iter_next_block | Dereference of null pointer | 327 | FP | FP | 切片代码显示，在计算 `next_block_off` 时，`src->bi.br` 可能为空，但该值仅用于计算偏移量，并未立即解引用。后续的 `reader_init_block_reader` 函数在 `next_off >= r... |
| 2197 | git-2.44.0 | get_mode | Dereference of null pointer | 63 | FP | FP | 切片代码显示，在解引用指针 `special` 之前，已通过条件 `path == file_from_standard_input` 确保 `special` 参数非空，因为该条件分支内直接对 `*special` 进行了赋值，表明... |
| 2199 | git-2.44.0 | crlf_to_git | Dereference of null pointer | 569 | FP | FP | 切片代码显示，在解引用 `src` 指针的循环之前，函数已通过 `if (src && !len)` 和 `if (!buf && !src)` 等条件对 `src` 进行了检查，并且 `gather_stats(src, len, ... |
| 2200 | git-2.44.0 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码中，变量 `next` 在函数开头被赋值为 `kwset->next`，而 `kwset` 在函数开头被赋值为 `(struct kwset *) kws`，表明 `next` 是一个有效的指针数组。在告警行 `trie = ... |
| 2201 | git-2.44.0 | diffcore_merge_broken | Dereference of null pointer | 292 | FP | FP | 切片代码显示，在内层循环访问 `pp` 之前，外层循环已通过 `if (!p) continue;` 确保 `p` 非空，且 `pp` 是从同一队列 `q->queue[j]` 中获取，该队列在初始化后未显示有显式的空值插入。虽然工具... |
| 2202 | git-2.44.0 | parse_options_step | Dereference of null pointer | 891 | FP | FP | 切片代码显示，在访问 `ctx->opt` 之前，`ctx->opt` 被明确赋值为 `arg + 1`（第45行），因此当执行到告警行（第55行）时，`ctx->opt` 不可能为 NULL。该告警是静态分析工具的逻辑误判。 |
| 2203 | git-2.44.0 | rstrip_ref_components | Dereference of null pointer | 2113 | FP | FP | 切片代码中，在循环条件 `for (i = 0; p[i]; p[i] == '/' ? i++ : *p++)` 中，`p` 指向 `refname` 且 `refname` 来自函数参数，不会为 NULL。指针 `p` 在循环中被... |
| 2204 | git-2.44.0 | parse_options | Dereference of null pointer | 1037 | FP | FP | 切片代码显示，在告警行 `isascii(*ctx.opt)` 之前，`ctx.opt` 已在 `parse_options_step` 函数中被显式初始化为 `NULL`，并且在 `PARSE_OPT_UNKNOWN` 分支中，`c... |
| 2205 | git-2.44.0 | process_entry | Dereference of null pointer | 3357 | FP | FP | 切片代码显示告警行位于 `RENAME_ONE_FILE_TO_TWO` 分支内，该分支仅在 `ci->ren2` 非空时才会执行，而前面的 `if (ci->ren2)` 断言确保了 `ci->ren2` 的有效性，因此不会发生空指... |
| 2206 | git-2.44.0 | verify_absent | Dereference of null pointer | 2523 | FP | FP | 切片代码显示，在告警行 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))` 中，对指针 `o` 和 `ce` 的访问是安全的，因为它们作为函... |
| 2207 | git-2.44.0 | show_pack_info | Dereference of null pointer | 1698 | FP | FP | 切片代码显示，指针`chain_histogram`仅在`deepest_delta`为真（非零）时通过`CALLOC_ARRAY`分配内存，随后在循环中访问该数组前，通过`if (is_delta_type(obj->type))`... |
| 2208 | git-2.44.0 | output | Dereference of null pointer | 546 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 仅在 `j < b->nr` 的条件下被赋值，且 `b_util->matching` 在 `while (j < b-... |
| 2209 | git-2.44.0 | limit_list | Dereference of null pointer | 1460 | FP | FP | 切片代码显示，在标记的警告行（obj->flags & UNINTERESTING）之前，obj 被赋值为 &commit->object，而 commit 是从 original_list 中通过 pop_commit 弹出的，该函... |
| 2210 | git-2.44.0 | add_lines_to_move_detection | Dereference of null pointer | 1034 | FP | FP | 切片代码显示，`entry_list` 通过 `ALLOC_GROW_BY` 宏进行动态增长，该宏会分配内存并初始化为零。在访问 `entry_list[l->id]` 之前，`l->id` 的值被正确设置，且数组已通过 `ALLOC... |
| 2211 | git-2.44.0 | limit_list | Dereference of null pointer | 1456 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量来自 `pop_commit` 函数，该函数在栈非空时返回有效指针，在循环条件 `while (original_list)` 的保护下，`commit`... |
| 2212 | git-2.44.0 | lstrip_ref_components | Dereference of null pointer | 2075 | FP | FP | 切片代码中，指针 `p` 在循环条件 `p[i]` 中被解引用前，已通过函数参数 `refname` 初始化，而 `refname` 来自 `xstrdup` 的返回值，该函数保证返回非空指针或终止程序，因此 `p` 不可能为 NULL。 |
| 2213 | git-2.44.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 切片代码显示，在指针`result`被解引用之前，已经通过`if (!result)`进行了空指针检查，并直接返回了默认值，因此不会发生空指针解引用。 |
| 2214 | git-2.44.0 | coalesce_lines | Dereference of null pointer | 262 | FP | FP | 在告警行`newend = newend->prev;`之前，`newend`指针已在循环`for (j = 1, newend = newline; j < lennew + 1; j++)`中被初始化为`newline`，且切片中... |
| 2215 | git-2.44.0 | process_parents | Dereference of null pointer | 1143 | FP | FP | 在调用 `p->parents` 之前，切片代码中已存在 `if (p)` 的显式空指针检查，确保了 `p` 不为空。因此，对 `p->parents` 的访问是安全的，不会发生空指针解引用。 |
| 2216 | git-2.44.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1282 | FP | FP | 切片代码显示告警行调用的是 `write_message` 函数，该函数内部对 `filename` 参数进行了空指针检查（通过 `hold_lock_file_for_update` 和 `error_errno` 处理），且 `n... |
| 2217 | git-2.44.0 | gather_stats | Dereference of null pointer | 49 | FP | FP | 切片代码显示函数入口处有明确的空指针检查（`if (!buf ｜｜ !size)`），确保了后续对`buf`数组的访问是安全的，因此不存在空指针解引用问题。 |
| 2218 | git-2.44.0 | append_strategy | Dereference of null pointer | 227 | FP | FP | 切片代码显示函数仅将指针参数 `s` 存入数组，未对其进行解引用操作。告警消息描述的'解引用空指针'逻辑错误在提供的代码片段中并未发生。 |
| 2219 | git-2.44.0 | add_lines_to_move_detection | Dereference of null pointer | 1037 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行动态增长和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，确保了数... |
| 2220 | git-2.44.0 | coalesce_lines | Dereference of null pointer | 270 | FP | FP | 在告警行`lline->prev->next = lline->next;`之前，切片代码已通过`if (lline->prev)`进行了明确的空指针检查，确保了`lline->prev`不为空时才进行解引用，因此该解引用是安全的，属... |
| 2221 | git-2.44.0 | apply_one_fragment | Dereference of null pointer | 2990 | FP | FP | 切片代码中，`postimage.line_allocated` 在 `add_line_info` 函数中被分配和初始化，且 `postimage.nr` 在递减前被检查（`inaccurate_eof` 条件确保 `newline... |
| 2222 | git-2.44.0 | try_to_commit | Dereference of null pointer | 1615 | FP | FP | 切片代码显示，在调用 `commit_tree_extended` 函数时，其 `parents` 参数可能为 NULL，但该函数内部（已提供定义）包含 `while (parents)` 循环，能正确处理 NULL 值，不会导致空指... |
| 2223 | git-2.44.0 | prepare_attr_stack | Dereference of null pointer | 1011 | FP | FP | 切片代码显示，在警告行`*stack = info->prev;`之前，`info`被赋值为`*stack`，而`*stack`由`bootstrap_attr_stack`函数初始化，该函数确保`*stack`不为空（若为空则进行初... |
| 2224 | git-2.44.0 | split_graph_merge_strategy | Dereference of null pointer | 2239 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，代码逻辑确保了 `g` 不为空。具体来说，只有当 `ctx->num_commit_graphs_after == 2` 时才会执行该行，而此条件仅... |
| 2225 | git-2.44.0 | read_cached_dir | Dereference of null pointer | 2515 | FP | FP | 切片代码显示，在访问 `cdir->untracked` 之前，函数 `read_cached_dir` 已被调用，这表明 `cdir` 指针本身非空。此外，该函数是静态辅助函数，其调用者应确保 `cdir->untracked` 的... |
| 2226 | git-2.44.0 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 切片代码显示，函数在访问 `ends[line]` 前，`data` 参数被直接使用或返回，但未显示 `ends` 指针的来源。然而，函数逻辑表明 `ends` 是一个数组，且 `line` 参数在访问前经过了 `if (line =... |
| 2227 | git-2.44.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码显示函数`strvec_push_nodup`仅执行数组赋值操作，未包含任何指针解引用前的空值检查或分配逻辑。该告警点`array->v[array->nr++] = value;`本身不涉及对`array`或`array->... |
| 2228 | git-2.44.0 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数体为空，没有实际的指针解引用操作，因此工具报告的'空指针解引用'逻辑错误不成立。 |
| 2229 | git-2.44.0 | find_bisection | Dereference of null pointer | 437 | FP | FP | 切片代码显示，在警告行`list->item = best->item;`之前，`best`指针已通过`do_find_bisection`函数调用被赋值，且该函数在切片中明确包含返回`NULL`或有效指针的逻辑。当`best`为`N... |
| 2230 | git-2.44.0 | verify_absent_1 | Dereference of null pointer | 2482 | FP | FP | 切片代码显示，在调用 `check_leading_path(ce->name, ce_namelen(ce), 0)` 之前，函数已通过条件 `if (o->index_only ｜｜ !o->update)` 提前返回，确保了 `... |
| 2231 | git-2.44.0 | merge_ref_iterator_advance | Dereference of null pointer | 161 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 仅在 `ITER_YIELD_CURRENT` 分支中被使用，而该分支仅在 `selection` 包含 `ITER_YIELD_CURR... |
| 2232 | git-2.44.0 | try_to_commit | Dereference of null pointer | 1499 | FP | FP | 切片代码显示，在调用 `parents = copy_commit_list(current_head->parents);` 之前，`current_head` 已通过 `parse_head` 函数成功获取或设置为 NULL，并且... |
| 2233 | git-2.44.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数 `ce_path_match` 的参数 `ce` 被直接用于宏 `ce_namelen(ce)` 和访问 `ce->name`、`ce->ce_mode`。调用者 `match_pathspec` 的参数 `nam... |
| 2234 | git-2.44.0 | cmp_local_packs | Dereference of null pointer | 479 | FP | FP | 告警点位于函数入口处对指针 `pl` 的检查 `if (!pl->next)`，但 `pl` 被初始化为全局变量 `local_packs`，其初始值为 `NULL`。在切片代码中，没有证据表明 `local_packs` 在函数调用... |
| 2235 | git-2.44.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 673 | FP | FP | 切片代码显示，在解引用指针 `n` 之前，已通过 `if (n)` 检查其非空，因此不会发生空指针解引用。该告警是静态分析工具的逻辑误判。 |
| 2236 | git-2.44.0 | unload_one_branch | Dereference of null pointer | 2052 | FP | FP | 切片代码显示，在解引用 `e->active_next_branch` 之前，`e` 被赋值为 `active_branches`，而 `active_branches` 仅在 `cur_active_branches` 为真且满足循... |
| 2237 | git-2.44.0 | process_entries | Dereference of null pointer | 4329 | FP | FP | 切片代码显示，在访问 `dir_metadata.offsets.items[0].util` 之前，已通过 `if` 条件检查了 `dir_metadata.offsets.nr == 1`，并且该条件为真时才会执行访问。告警行位于... |
| 2238 | git-2.44.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 169 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过 `string_list_append` 或 `string_list_app... |
| 2239 | git-2.44.0 | merge_ort_internal | Dereference of null pointer | 5056 | FP | FP | 切片代码显示，在警告行（opt->priv->call_depth--）之前，opt->priv->call_depth 已通过 opt->priv->call_depth++ 进行了递增，且 opt->priv 在函数调用路径中未被... |
| 2240 | git-2.44.0 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警指向的代码行 `curr = kwset->trie->next` 位于一个循环中，该循环的遍历条件是 `curr` 不为空。切片代码显示，`curr` 的初始值 `kwset->trie->next` 是由 `enqueue` ... |
| 2241 | git-2.44.0 | cmd_merge | Dereference of null pointer | 1509 | FP | FP | 切片代码显示，在告警行（use_strategies[i]->attr）被访问前，变量use_strategies已通过循环条件（i < use_strategies_nr）确保访问在有效范围内，且切片中未见其被赋值为空。因此，该指针... |
| 2242 | git-2.44.0 | get_ref_map | Dereference of null pointer | 544 | FP | FP | 切片代码显示，在访问 `remote->fetch` 之前，存在 `if (remote)` 的条件检查，这防止了对空指针的解引用。告警点位于 `for (i = 0; i < fetch_refspec->nr; i++)` 循环，... |
| 2243 | git-2.44.0 | setup_scoreboard | Dereference of null pointer | 2839 | FP | FP | 切片代码显示，在访问 `c->parents` 之前，`c` 被赋值为 `final_commit`，而 `final_commit` 仅在 `sb->reverse && sb->revs->first_parent_only` 条... |
| 2244 | git-2.44.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在解引用指针 `sb->buf[len]` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 确保 `sb->buf` 不是指向静态缓冲区 `strbuf_slopbuf` 的指针，这通... |
| 2245 | git-2.44.0 | prepare_attr_stack | Dereference of null pointer | 1019 | FP | FP | 切片代码显示，在进入警告所在的while循环`while ((*stack)->origin)`之前，`*stack`已被赋值为`info->prev`，而`info`来自`*stack`的初始值。虽然存在`*stack`可能为NUL... |
| 2246 | git-2.44.0 | assert_sane_strbuf | Dereference of null pointer | 34 | FP | FP | 切片代码显示，在解引用 `buf->buf` 之前，已通过 `check(!!buf->buf)` 宏对指针 `buf->buf` 进行了非空检查，这构成了有效的防护机制，因此该空指针解引用告警是误报。 |
| 2247 | git-2.44.0 | show_pack_info | Dereference of null pointer | 1720 | FP | FP | 切片代码显示，在for循环访问`chain_histogram[i]`之前，已通过条件`if (deepest_delta)`判断，若条件为真则调用`CALLOC_ARRAY`为指针分配内存，否则指针保持为NULL。循环仅在`deep... |
| 2248 | git-2.50.1 | image_remove_last_line | Dereference of null pointer | 363 | FP | FP | 切片代码显示，在访问 `img->line[img->line_nr - 1]` 之前，没有对 `img->line` 或 `img->line_nr` 进行空指针或越界检查。然而，该函数是静态的，且调用上下文未知。在缺乏前置条件验证... |
| 2249 | git-2.50.1 | add_parents_only | Dereference of null pointer | 1933 | FP | FP | 在调用 `it->type` 之前，切片代码显示 `get_reference` 函数可能返回 NULL，但紧接着有 `if (!it && revs->ignore_missing) return 0;` 检查。当 `it` 为 N... |
| 2250 | git-2.50.1 | reftable_stack_reload_once | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在告警行`new_tables[new_tables_len] = table;`之前，`new_tables`已通过`reftable_calloc`分配了大小为`names_len`的内存，且`new_tables_... |
| 2251 | git-2.50.1 | get_mode | Dereference of null pointer | 65 | FP | FP | 告警点位于对指针 `special` 的赋值语句，但在切片代码中，该指针作为函数参数传入，并在赋值前已通过 `if (special && ...)` 进行了非空检查，因此不会发生空指针解引用。 |
| 2254 | git-2.50.1 | crlf_to_git | Dereference of null pointer | 583 | FP | FP | 切片代码显示，在解引用src指针之前，函数开头已通过条件`if (src && !len)`和`if (!buf && !src)`对src指针进行了检查，确保在后续使用src时它不为空或已提前返回。告警点位于循环内部，但循环执行的条... |
| 2255 | git-2.50.1 | cwexec | Dereference of null pointer | 679 | FP | FP | 切片代码显示，在访问 `trie->accepting` 和 `trie->shift` 之前，`trie` 变量是通过 `next[c]` 赋值的，而 `next` 指向 `kwset->next`，这是一个在函数开头初始化的有效数... |
| 2256 | git-2.50.1 | diffcore_merge_broken | Dereference of null pointer | 291 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环的 `pp` 是从 `q->queue[j]` 直接赋值的，而 `q->queue` 是一个指针数组，其元素可能为 NULL（如第291行所示，`q->queue[j]` 可能... |
| 2257 | git-2.50.1 | parse_options_step | Dereference of null pointer | 958 | FP | FP | 切片代码显示，在访问 `ctx->opt` 之前，存在 `if (ctx->opt)` 的条件检查，这防止了对空指针的解引用。告警点位于 `if (internal_help && *ctx->opt == 'h')`，但该行仅在 `... |
| 2258 | git-2.50.1 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | FP | 切片代码中，for循环的条件表达式 `p[i] == '/' ? i++ : *p++` 存在逻辑错误，但该表达式不会导致空指针解引用，因为 `p` 指向 `refname`（由 `xstrdup` 保证非空），且循环条件 `p[i]... |
| 2259 | git-2.50.1 | clar_summary_init | Dereference of null pointer | 76 | FP | FP | 切片代码显示，在解引用 `summary` 指针之前，`fopen` 调用失败会触发 `clar_abort` 函数，该函数会调用 `exit(-1)` 终止程序。因此，程序不会执行到解引用 `summary` 的代码行，该空指针解引... |
| 2260 | git-2.50.1 | parse_options | Dereference of null pointer | 1104 | FP | FP | 切片代码显示，在访问 `*ctx.opt` 之前，`ctx.opt` 已在 `parse_options_step` 函数中被显式初始化为 `NULL`，并且在 `PARSE_OPT_UNKNOWN` 分支中，`ctx.opt` 仅在... |
| 2261 | git-2.50.1 | allocate_snapshot_buffer | Dereference of null pointer | 533 | FP | FP | 告警点位于die_errno函数调用处，该函数用于处理错误并终止程序，并非对空指针的解引用。切片代码显示snapshot->buf由xmalloc分配，若分配失败会调用die终止程序，因此不会出现对空指针的读写操作。 |
| 2263 | git-2.50.1 | verify_absent | Dereference of null pointer | 2537 | FP | FP | 告警指向的代码行 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))` 中，`ce` 和 `o` 均为函数入参，在切片代码中未见其被赋值为 N... |
| 2264 | git-2.50.1 | show_pack_info | Dereference of null pointer | 1784 | FP | FP | 切片代码显示，指针`chain_histogram`仅在`deepest_delta`为真（非零）时通过`CALLOC_ARRAY`分配内存，否则为NULL。在解引用`chain_histogram`的代码行前，存在条件`if (is... |
| 2265 | git-2.50.1 | output | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 仅在 `j < b->nr` 的条件下被赋值，且 `b_util->matching` 在 `while (j < b-... |
| 2267 | git-2.50.1 | limit_list | Dereference of null pointer | 1491 | FP | FP | 切片代码中，在告警行（obj->flags & UNINTERESTING）之前，obj 被赋值为 &commit->object，而 commit 来自 pop_commit 且被检查非空，因此 obj 不可能为空指针。 |
| 2268 | git-2.50.1 | add_lines_to_move_detection | Dereference of null pointer | 1060 | FP | FP | 切片代码显示，在访问 entry_list[l->id] 之前，已经通过 ALLOC_GROW_BY 宏确保了 entry_list 数组会根据 id 进行增长和初始化，因此不会出现空指针解引用。 |
| 2269 | git-2.50.1 | limit_list | Dereference of null pointer | 1487 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量来自 `pop_commit` 函数，该函数在栈非空时返回有效指针，在栈为空时返回 NULL。然而，告警所在行的 `if` 条件检查了 `revs->ma... |
| 2270 | git-2.50.1 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | FP | 切片代码中，在警告行 `for (i = 0; p[i]; p[i] == '/' ? i++ : *p++)` 处，循环条件 `p[i]` 确保了在访问 `p[i]` 之前指针 `p` 不为空，因为 `refname` 参数已通过 ... |
| 2271 | git-2.50.1 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 切片代码显示，在指针`result`被解引用前，已通过`if (!result)`进行了空指针检查，并直接返回默认值，因此不会发生空指针解引用。 |
| 2272 | git-2.50.1 | coalesce_lines | Dereference of null pointer | 251 | FP | FP | 在切片代码中，对`newend`的访问（如`newend->prev`）发生在`directions[i][j] == MATCH`分支内，该分支仅在`i`和`j`不为零时进入，且`newend`在循环前已通过`newend = ne... |
| 2273 | git-2.50.1 | merge_ort_internal | Dereference of null pointer | 5277 | FP | FP | 切片代码显示，在警告行（opt->priv->call_depth--;）之前，opt->priv->call_depth 已通过 opt->priv->call_depth++ 进行了递增，确保了指针 opt->priv 在递减前非... |
| 2274 | git-2.50.1 | assert_sane_strbuf | Dereference of null pointer | 35 | FP | FP | 切片代码显示，`cl_assert` 是一个单元测试断言宏，用于在测试失败时触发错误，并非生产代码中的空指针解引用。该告警是针对测试框架的误报，不构成实际的安全风险。 |
| 2275 | git-2.50.1 | process_parents | Dereference of null pointer | 1174 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，并且 `repo_parse_commit_gently` 函数调用后 `p` 的状态未改变，因此对 `p->parents` 的访问是安... |
| 2276 | git-2.50.1 | run_prepare_commit_msg_hook | Dereference of null pointer | 1352 | FP | FP | 切片代码显示告警行 `write_message(msg->buf, msg->len, name, 0)` 中，`msg` 是函数参数且未在切片内被赋值为 NULL，调用 `write_message` 前也无空指针检查缺失的逻辑。... |
| 2277 | git-2.50.1 | gather_stats | Dereference of null pointer | 52 | FP | FP | 切片代码显示函数入口处有`size`参数，循环条件`i < size`确保了对`buf`数组的访问在边界内，且告警行`unsigned char c = buf[i];`之前没有对`buf`进行空指针解引用。函数逻辑是遍历缓冲区统计字... |
| 2278 | git-2.50.1 | clar_parse_args | Dereference of null pointer | 496 | FP | FP | 切片代码显示，在访问 `argument[1]` 之前，`argument` 被赋值为 `argv[i]`，而 `argv` 是函数参数，其元素在标准C程序中不应为NULL。此外，代码逻辑表明 `argument` 用于命令行参数解析... |
| 2279 | git-2.50.1 | append_strategy | Dereference of null pointer | 233 | FP | FP | 切片代码显示，函数`append_strategy`仅将指针`s`存入数组，并未对`s`进行解引用操作。告警信息描述的'解引用空指针'逻辑错误在提供的代码片段中并未发生。 |
| 2280 | git-2.50.1 | merge_ref_iterator_advance | Dereference of null pointer | 214 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 仅在 `ITER_YIELD_CURRENT` 分支中被使用，而该分支仅在 `iter->select` 函数返回特定标志时进入。虽然切片... |
| 2281 | git-2.50.1 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码中，`array` 指针在函数参数中未进行空值检查，但函数 `strvec_push_nodup` 是一个内部辅助函数，其调用者应确保传入的 `array` 指针有效。在切片可见范围内，没有直接证据表明 `array` 一定为... |
| 2282 | git-2.50.1 | add_lines_to_move_detection | Dereference of null pointer | 1063 | FP | FP | 切片代码显示，在访问 entry_list[l->id] 之前，已经通过 ALLOC_GROW_BY 宏确保了 entry_list 数组的大小至少为 id+1，并且该宏会将新分配的内存清零，因此 entry_list 指针不会为 N... |
| 2283 | git-2.50.1 | image_remove_first_line | Dereference of null pointer | 355 | FP | FP | 切片代码显示告警点是对 `strbuf_remove` 函数的调用，该函数内部实现安全，且切片中未提供 `img` 或 `img->line` 为空的证据。该告警很可能是工具对指针状态的不确定分析导致的误报。 |
| 2284 | git-2.50.1 | coalesce_lines | Dereference of null pointer | 259 | FP | FP | 切片代码显示，在访问 `lline->prev` 之前，`lline` 被赋值为 `newend`，而 `newend` 在循环中通过 `newend = newend->prev;` 更新，这确保了 `newend` 及其 `pre... |
| 2286 | git-2.50.1 | strvec_splice | Dereference of null pointer | 69 | FP | FP | 切片代码显示，在告警行之前，如果 `array->v == empty_strvec`，会将其设置为 NULL，但随后立即调用了 `ALLOC_GROW` 宏，该宏会通过 `REALLOC_ARRAY` 对 `array->v` 进行... |
| 2287 | git-2.50.1 | <global> | Dereference of null pointer | 30 | FP | FP | 切片代码显示函数 `is_absolute_path` 为空实现，没有对指针 `path` 进行解引用操作，因此不存在空指针解引用问题，属于工具误报。 |
| 2288 | git-2.50.1 | prepare_attr_stack | Dereference of null pointer | 978 | FP | FP | 切片代码显示，在警告行`*stack = info->prev;`之前，`info`被赋值为`*stack`，而`*stack`由`bootstrap_attr_stack`函数初始化。`bootstrap_attr_stack`仅在... |
| 2289 | git-2.50.1 | split_graph_merge_strategy | Dereference of null pointer | 2284 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，`g` 指针在 `while (g) {...}` 循环中被赋值和使用，且循环条件 `while (g)` 确保了 `g` 不为空。因此，在进入 `... |
| 2290 | git-2.50.1 | get_nth_line | Dereference of null pointer | 879 | FP | FP | 切片代码显示，函数在访问 `ends[line]` 前，`data` 参数被直接使用或返回，但 `ends` 指针的来源和有效性在切片中未体现。然而，`line` 为 0 时直接返回 `data`，`line` 非零时进行指针运算，这... |
| 2291 | git-2.50.1 | <global> | Dereference of null pointer | 15 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对指针 `ref_iterator` 进行解引用操作，因此不存在空指针解引用问题。 |
| 2292 | git-2.50.1 | find_bisection | Dereference of null pointer | 440 | FP | FP | 切片代码显示，在告警行`list->item = best->item;`之前，`best`指针已在`if (best)`条件中进行了非空检查，确保了其不为空。因此，对`best->item`的访问是安全的，不存在空指针解引用。 |
| 2293 | git-2.50.1 | try_to_commit | Dereference of null pointer | 1570 | FP | FP | 切片代码显示，在调用 `current_head->parents` 之前，`current_head` 已通过 `parse_head` 函数获取，且当其为 NULL 时函数会提前返回错误。在告警所在行，`current_head`... |
| 2294 | git-2.50.1 | <global> | Dereference of null pointer | 1546 | FP | FP | 切片代码显示告警点位于条件判断 `if (use_strategies[i]->attr & NO_FAST_FORWARD)`，其中 `use_strategies` 是一个数组，`i` 在循环 `for (i = 0; i < u... |
| 2295 | git-2.50.1 | verify_absent_1 | Dereference of null pointer | 2496 | FP | FP | 切片代码显示，在调用 `check_leading_path` 函数前，已通过条件 `if (o->index_only ｜｜ !o->update)` 进行了保护，若条件为真则函数直接返回0，不会执行到告警行。因此，在切片可见的上下... |
| 2296 | git-2.50.1 | try_to_commit | Dereference of null pointer | 1686 | FP | FP | 切片代码显示告警行（commit_tree_extended调用）的参数均来自函数内部变量或经过验证的输入，没有明显的空指针解引用路径。函数逻辑在切片内是完整的，且告警点之前的代码路径（如parse_head）已处理了可能的错误情况。 |
| 2298 | git-2.50.1 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数`ce_path_match`的参数`ce`被直接用于宏`ce_namelen(ce)`和访问`ce->name`、`ce->ce_mode`。调用该函数的上下文未在切片中给出，但函数内部逻辑没有对`ce`进行空值检... |
| 2299 | git-2.50.1 | cmp_local_packs | Dereference of null pointer | 509 | FP | FP | 切片代码显示函数入口处`pl`被赋值为全局变量`local_packs`，该变量初始化为NULL，但函数`cmp_local_packs`被调用前，`local_packs`很可能已被正确初始化，否则程序逻辑无法进行。告警点`if (... |
| 2301 | git-2.50.1 | tree_write_stack_finish_subtree | Dereference of null pointer | 679 | FP | FP | 切片代码显示，在解引用指针 `n`（即 `tws->next`）之前，已通过 `if (n)` 进行了明确的非空检查，因此不会发生空指针解引用。 |
| 2302 | git-2.50.1 | unload_one_branch | Dereference of null pointer | 2066 | FP | FP | 切片代码显示，在解引用 `e->active_next_branch` 之前，`e` 被赋值为 `active_branches`，而 `active_branches` 仅在 `cur_active_branches` 为真时才会进... |
| 2303 | git-2.50.1 | apply_one_fragment | Dereference of null pointer | 2991 | FP | FP | 切片代码中，在警告行（postimage.line[postimage.line_nr - 1].len--）之前，已通过条件 `newlines.len > 0` 和 `newlines.buf[newlines.len - 1] ... |
| 2304 | git-2.50.1 | process_entries | Dereference of null pointer | 4486 | FP | FP | 切片代码显示，对`dir_metadata.offsets.items[0].util`的访问发生在条件检查`dir_metadata.offsets.nr != 1`之后，该检查确保了数组至少有一个元素。此外，该代码路径仅在调试断言... |
| 2305 | git-2.50.1 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已在循环中被填充，且 `remotes->nr == 1` 的条件确保了列表至少有一个... |
| 2306 | git-2.50.1 | clar_run_suite | Dereference of null pointer | 399 | FP | FP | 切片代码显示，在报告行`report->suite = _clar.active_suite;`之前，`report`指针已通过`calloc`分配内存，且分配失败时会调用`clar_abort`退出程序，因此`report`不可能为... |
| 2307 | git-2.50.1 | kwsprep | Dereference of null pointer | 507 | FP | FP | 切片代码显示，在警告行`for (curr = kwset->trie->next; curr; curr = curr->next)`之前，`kwset->trie`已在多个循环中被访问且未发生空指针解引用，且`kwset->tri... |
| 2309 | git-2.50.1 | get_ref_map | Dereference of null pointer | 544 | FP | FP | 切片代码显示在访问 `remote->fetch` 前已通过 `if (remote)` 进行了空指针检查，且告警行位于 `if (rs->nr)` 分支内，该分支内 `remote` 变量可能已通过前置逻辑确保非空或访问受控，未发现... |
| 2310 | git-2.50.1 | setup_scoreboard | Dereference of null pointer | 2842 | FP | FP | 切片代码显示，在访问 `c->parents` 之前，`c` 被赋值为 `final_commit`，而 `final_commit` 仅在特定条件（`sb->reverse && sb->revs->first_parent_onl... |
| 2311 | git-2.50.1 | clear_snapshot_buffer | Dereference of null pointer | 185 | FP | FP | 切片代码显示，在调用die_errno函数前，已通过if语句检查了snapshot->mmapped为非零值，并且munmap的返回值作为条件，这表明对snapshot->buf的访问发生在有效的内存映射上下文中，不存在对空指针的解引... |
| 2312 | git-2.50.1 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在解引用 `sb->buf` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 检查其是否指向特殊缓冲区 `strbuf_slopbuf`。当不相等时，`sb->buf` 应为有效指针，... |
| 2315 | git-2.50.1 | show_pack_info | Dereference of null pointer | 1806 | FP | FP | 切片代码显示，在访问`chain_histogram[i]`的循环之前，存在条件`if (deepest_delta)`，当条件为真时，会通过`CALLOC_ARRAY`为`chain_histogram`分配内存。循环边界`deep... |
| 2316 | git-2.47.1 | image_remove_last_line | Dereference of null pointer | 362 | FP | FP | 切片代码显示，在访问 `img->line[img->line_nr - 1]` 之前，函数 `image_remove_last_line` 的调用者应已确保 `img->line_nr > 0` 且 `img->line` 非空，... |
| 2317 | git-2.47.1 | add_parents_only | Dereference of null pointer | 1934 | FP | FP | 在调用 `it->type` 之前，切片代码显示 `it` 可能为 NULL 的情况已被检查和处理（`if (!it && revs->ignore_missing) return 0;`），因此当程序执行到告警行时，`it` 已被确... |
| 2318 | git-2.47.1 | get_mode | Dereference of null pointer | 63 | FP | FP | 切片代码显示，在告警行 `*special = SPECIAL_STDIN;` 之前，`special` 指针作为函数参数传入，其有效性由调用者保证。告警点位于 `path == file_from_standard_input` 的... |
| 2320 | git-2.47.1 | crlf_to_git | Dereference of null pointer | 582 | FP | FP | 切片代码显示，在解引用 `src` 指针的循环之前，函数已通过 `if (src && !len)` 和 `if (!buf && !src)` 等条件对 `src` 进行了检查，并且 `gather_stats(src, len, ... |
| 2321 | git-2.47.1 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码中，变量 `trie` 在 `if (!(trie = next[c]))` 条件分支中可能为 NULL，但随后的 `if (trie->accepting && beg <= mch)` 访问 `trie->acceptin... |
| 2322 | git-2.47.1 | diffcore_merge_broken | Dereference of null pointer | 295 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环的 `pp` 是从 `q->queue[j]` 直接赋值的，而 `q->queue` 是一个指针数组，其元素可能为 NULL（如第 `q->queue[j] = NULL;` ... |
| 2323 | git-2.47.1 | parse_options_step | Dereference of null pointer | 906 | FP | FP | 切片代码显示，在访问 `ctx->opt` 之前，`ctx->opt` 被明确赋值为 `arg + 1`（第38行），因此它不可能为空。告警点（第40行）的 `if (internal_help && *ctx->opt == 'h'... |
| 2324 | git-2.47.1 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | FP | 切片代码中，在警告行 `p[i]` 被访问前，`p` 被赋值为 `refname`，而 `refname` 是函数的非空参数，因此 `p` 不为空。循环条件 `p[i]` 检查的是字符是否为 `'\0'`，而非解引用空指针。 |
| 2325 | git-2.47.1 | parse_options | Dereference of null pointer | 1052 | FP | FP | 切片代码显示，在调用 `isascii(*ctx.opt)` 之前，`ctx->opt` 已在 `parse_options_step` 函数中被显式初始化为 `NULL`，并且在 `PARSE_OPT_UNKNOWN` 分支中，`c... |
| 2326 | git-2.47.1 | process_entry | Dereference of null pointer | 3413 | FP | FP | 切片代码显示，在访问 ci->ren2 之前，存在条件判断 `if (ci->ren2)` 和 `assert` 语句，表明代码逻辑已考虑空指针情况。此外，告警行位于 `RENAME_ONE_FILE_TO_TWO` 分支内，该分支仅... |
| 2327 | git-2.47.1 | verify_absent | Dereference of null pointer | 2534 | FP | FP | 切片代码显示，在告警行访问 `ce->ce_flags` 之前，函数 `verify_absent` 的调用者必须传入有效的 `ce` 指针，且函数内部逻辑（如调用 `verify_absent_1` 时也直接使用了 `ce`）表明该... |
| 2328 | git-2.47.1 | show_pack_info | Dereference of null pointer | 1689 | FP | FP | 切片代码显示，指针`chain_histogram`仅在`deepest_delta`为真（非零）时通过`CALLOC_ARRAY`分配内存，而在后续的循环访问`chain_histogram[obj_stat[i].delta_de... |
| 2329 | git-2.47.1 | output | Dereference of null pointer | 550 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 仅在 `j < b->nr` 的条件下被赋值，且 `b_util->matching` 在 `while (j < b-... |
| 2330 | git-2.47.1 | limit_list | Dereference of null pointer | 1497 | FP | FP | 切片代码中，在警告行（obj->flags & UNINTERESTING）之前，obj 被明确赋值为 &commit->object，而 commit 是从 original_list 中通过 pop_commit 弹出的，该函数在... |
| 2331 | git-2.47.1 | add_lines_to_move_detection | Dereference of null pointer | 1059 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`l->id` 的值被明确赋值为 `id` 变量，而 `id` 变量在循环中通过 `ALLOC_GROW_BY` 宏与 `entry_list` 数组同步增长，确保了... |
| 2332 | git-2.47.1 | limit_list | Dereference of null pointer | 1493 | FP | FP | 切片代码显示，在访问 `obj->flags` 之前，`obj` 被赋值为 `&commit->object`，而 `commit` 是从 `pop_commit` 返回的，该函数在输入非空时保证返回非空指针。因此，`obj` 不可能... |
| 2333 | git-2.47.1 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | FP | 切片代码中，`p` 被初始化为 `refname`（非空指针），在 for 循环条件 `p[i]` 中，`p` 作为基地址被使用，但并未被解引用为指针值。循环体为空，且 `p` 在循环中未被赋值修改，因此不存在对空指针的解引用。该告警... |
| 2334 | git-2.47.1 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 切片代码显示，在指针`result`被解引用前，已通过`if (!result)`进行了空指针检查，并直接返回默认值，因此不会发生空指针解引用。 |
| 2335 | git-2.47.1 | coalesce_lines | Dereference of null pointer | 264 | FP | FP | 在告警行`newend = newend->prev;`之前，`newend`指针已在循环条件`while (i != 0 ｜｜ j != 0)`和内部`if (directions[i][j] == MATCH)`分支中被保护，且`... |
| 2336 | git-2.47.1 | merge_ort_internal | Dereference of null pointer | 5218 | FP | FP | 切片代码显示告警行 `opt->priv->call_depth--;` 位于一个递归调用 `merge_ort_internal` 之后，该递归调用前有对应的 `opt->priv->call_depth++;` 操作，且递归调用后... |
| 2337 | git-2.47.1 | process_parents | Dereference of null pointer | 1180 | FP | FP | 在调用 `p->parents` 之前，切片代码已通过 `if (p)` 检查了指针 `p` 非空，并且 `repo_parse_commit_gently` 的调用也暗示了 `p` 的有效性。因此，对 `p->parents` 的访... |
| 2338 | git-2.47.1 | run_prepare_commit_msg_hook | Dereference of null pointer | 1365 | FP | FP | 切片代码显示告警行 `write_message(msg->buf, msg->len, name, 0)` 中，`msg` 是函数参数且类型为 `struct strbuf *`，调用前未显式检查其是否为 NULL。但 `strbu... |
| 2339 | git-2.47.1 | gather_stats | Dereference of null pointer | 51 | FP | FP | 切片代码显示函数入口处有`size`参数，循环条件`i < size`确保了对`buf`数组的访问在边界内。告警点`buf[i]`的访问受`size`控制，且函数内部有`size >= 1`的检查，表明指针`buf`在有效范围内使用，... |
| 2340 | git-2.47.1 | append_strategy | Dereference of null pointer | 231 | FP | FP | 切片代码显示函数仅将指针存入数组，未对指针`s`进行解引用操作。告警消息描述的'解引用空指针'逻辑错误在提供的代码片段中并未发生。 |
| 2341 | git-2.47.1 | merge_ref_iterator_advance | Dereference of null pointer | 203 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 仅在 `ITER_YIELD_CURRENT` 分支中被使用，而该分支仅在 `iter->select` 函数返回包含 `ITER_YIE... |
| 2342 | git-2.47.1 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码中未提供对输入参数 `array` 或 `array->v` 的校验，但函数 `strvec_push_nodup` 是一个内部辅助函数，其调用者应确保传入有效的 `struct strvec` 指针和已分配的内存。仅基于此切... |
| 2343 | git-2.47.1 | add_lines_to_move_detection | Dereference of null pointer | 1062 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，并与数组大小... |
| 2344 | git-2.47.1 | image_remove_first_line | Dereference of null pointer | 354 | FP | FP | 切片代码显示，传递给 `strbuf_remove` 的 `img->line[0].len` 是作为长度参数使用，而非被解引用的指针。告警所指的 `img->line[0].len` 访问发生在 `image_remove_firs... |
| 2345 | git-2.47.1 | coalesce_lines | Dereference of null pointer | 272 | FP | FP | 在告警行`if (lline->prev)`之前，`lline`被赋值为`newend`，而`newend`在循环中通过`newend = newend->prev;`更新，这确保了`newend`（以及`lline`）是链表中的一个... |
| 2346 | git-2.47.1 | try_to_commit | Dereference of null pointer | 1699 | FP | FP | 切片代码显示，在调用 commit_tree_extended 函数前，对 parents 参数进行了明确的空值检查和处理，确保其不会为 NULL 指针。具体逻辑中，parents 要么通过 copy_commit_list 从 cu... |
| 2347 | git-2.47.1 | prepare_attr_stack | Dereference of null pointer | 1013 | FP | FP | 切片代码显示，在警告行`*stack = info->prev;`之前，`info`被赋值为`*stack`，而`*stack`由`bootstrap_attr_stack`函数初始化，该函数确保在`*stack`为空时会进行分配，因... |
| 2348 | git-2.47.1 | split_graph_merge_strategy | Dereference of null pointer | 2269 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，`g` 的赋值和检查逻辑确保了它不为 NULL。`g` 在 while 循环中被更新，但循环条件 `while (g && ...)` 保证了只有当... |
| 2349 | git-2.47.1 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 切片代码显示，当line为0时直接返回data，否则通过ends数组偏移计算返回地址。ends指针作为参数传入，其有效性应在调用者处保证。在切片可见范围内，没有对ends进行解引用前检查其是否为空的直接证据，但函数逻辑本身不包含对en... |
| 2350 | git-2.47.1 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数体为空，没有实际的指针解引用操作，因此工具报告的‘空指针解引用’逻辑错误在当前切片上下文中不成立。 |
| 2351 | git-2.47.1 | find_bisection | Dereference of null pointer | 439 | FP | FP | 切片代码显示，在警告行`list->item = best->item;`之前，`best`指针已通过`do_find_bisection`函数返回，且该函数在多种条件下（如`approx_halfway`或`best_bisecti... |
| 2352 | git-2.47.1 | <global> | Dereference of null pointer | 1537 | FP | FP | 切片代码显示告警点位于条件判断语句 `if (use_strategies[i]->attr & NO_FAST_FORWARD)`，其中 `use_strategies` 是一个数组，其元素在 `add_strategies` 函数... |
| 2353 | git-2.47.1 | verify_absent_1 | Dereference of null pointer | 2493 | FP | FP | 切片代码显示，在调用 `check_leading_path` 函数前，函数参数 `ce` 已被用于条件判断 `if (o->index_only ｜｜ !o->update)`，且 `ce` 作为参数传入函数本身，表明其指针在调用点... |
| 2354 | git-2.47.1 | try_to_commit | Dereference of null pointer | 1583 | FP | FP | 切片代码显示，在调用 `current_head->parents` 之前，`current_head` 已通过 `parse_head` 函数获取，且当 `current_head` 为 NULL 时，函数会提前返回错误。在告警所在... |
| 2355 | git-2.47.1 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数`ce_path_match`的参数`ce`被直接用于宏`ce_namelen(ce)`和访问`ce->name`、`ce->ce_mode`。调用该函数的上下文未在切片中提供，但函数内部没有对`ce`进行空指针检查... |
| 2356 | git-2.47.1 | cmp_local_packs | Dereference of null pointer | 482 | FP | FP | 切片代码显示函数入口处 `pl` 被赋值为全局变量 `local_packs`，该变量初始化为 NULL。在未检查 `pl` 是否为 NULL 的情况下，代码直接访问 `pl->next`，这确实是一个空指针解引用风险。然而，该函数被... |
| 2357 | git-2.47.1 | tree_write_stack_finish_subtree | Dereference of null pointer | 677 | FP | FP | 在切片代码中，对指针 `tws->next` 的访问 `n = tws->next` 后，立即通过 `if (n)` 进行了空指针检查，后续所有对 `n` 的访问（如 `n->buf`）都位于该条件保护块内，因此不会发生空指针解引用。 |
| 2358 | git-2.47.1 | unload_one_branch | Dereference of null pointer | 2049 | FP | FP | 切片代码显示在解引用 `e->active_next_branch` 之前，`e` 被赋值为 `active_branches`，而 `active_branches` 仅在 `cur_active_branches && cur_a... |
| 2359 | git-2.47.1 | apply_one_fragment | Dereference of null pointer | 2987 | FP | FP | 切片代码中未发现对空指针的直接解引用。告警行（postimage.line[postimage.line_nr - 1].len--）操作前，postimage.line_nr 已在循环中递增，且存在前置条件检查（newlines.l... |
| 2360 | git-2.47.1 | process_entries | Dereference of null pointer | 4452 | FP | FP | 切片代码显示，在访问 `dir_metadata.offsets.items[0].util` 之前，已通过条件 `if (dir_metadata.offsets.nr != 1 ｜｜ (uintptr_t)dir_metadata... |
| 2361 | git-2.47.1 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过循环被填充，且 `remotes->nr == 1` 的条件确保了列表至少有一个... |
| 2362 | git-2.47.1 | kwsprep | Dereference of null pointer | 502 | FP | FP | 切片代码显示，在访问 `curr->parent` 之前，`curr` 变量是通过 `kwset->trie->next` 遍历获得的，而 `kwset->trie` 在函数逻辑中已被初始化和使用，`curr` 的父节点 `paren... |
| 2363 | git-2.47.1 | get_ref_map | Dereference of null pointer | 546 | FP | FP | 切片代码显示，在警告行（`for (i = 0; i < fetch_refspec->nr; i++)`）之前，`fetch_refspec` 被明确赋值为 `&refmap` 或 `&remote->fetch`，两者均非空。`r... |
| 2364 | git-2.47.1 | setup_scoreboard | Dereference of null pointer | 2841 | FP | FP | 切片代码显示，在访问 `c->parents` 的 `while` 循环条件之前，`final_commit` 变量是通过 `find_single_final(sb->revs, NULL)` 赋值的，该函数在切片中定义，当找不到符... |
| 2365 | git-2.47.1 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `sb->buf[len]` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 确保 `sb->buf` 不是指向静态缓冲区 `strbuf_slopbuf` 的指针。该条件逻辑... |
| 2366 | git-2.47.1 | prepare_attr_stack | Dereference of null pointer | 1021 | FP | FP | 切片代码显示，在进入while循环前，*stack指针已通过`*stack = info->prev;`被更新，且info来自`info = *stack;`，表明stack指针链存在有效的遍历逻辑。循环条件`(*stack)->or... |
| 2368 | git-2.47.1 | show_pack_info | Dereference of null pointer | 1711 | FP | FP | 切片代码显示，在访问`chain_histogram[i]`之前，已通过`if (deepest_delta)`条件检查并调用了`CALLOC_ARRAY`进行分配，且循环边界为`deepest_delta`，因此指针不会为NULL。 |
| 2369 | musl-1.2.1 | iconv | Dereference of null pointer | 373 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为偶数时 `scd` 才被赋值为非空指针。对于 `IS... |
| 2370 | musl-1.2.1 | load_direct_deps | Dereference of null pointer | 1194 | FP | FP | 切片代码显示，在警告行访问 `p->deps` 之前，存在条件 `if (!p->deps)` 并在其为空时调用 `error` 并可能 `longjmp` 退出，这阻止了对空指针的解引用。警告行位于 `if (p==head)` 条... |
| 2371 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 切片代码显示，在访问 `pmatch[bt].rm_so` 之前，`pmatch` 指针已通过 `xmalloc` 分配内存，且 `bt` 是 `trans_i->u.backref`，其值受限于 `tnfa->num_submatc... |
| 2372 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在解引用指针 `next_tags` 之前，存在条件判断 `if (next_tags)`，这确保了指针非空时才进行解引用操作。因此，该告警是误报。 |
| 2373 | musl-1.2.1 | do_relocs | Dereference of null pointer | 435 | FP | FP | 在REL_COPY分支中，memcpy的目标地址reloc_addr由laddr函数计算得到，该函数在切片中可见，当p->loadmap为空时返回p->base + v，这是一个有效的非空地址；源地址sym_val由laddr(def... |
| 2374 | musl-1.2.1 | iconv | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，`scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。在 `case ISO2022_JP:` 分支中，`scd->state` ... |
| 2375 | musl-1.2.1 | iconv | Dereference of null pointer | 372 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为奇数（表示无状态转换）时 `scd` 保持为 N... |
| 2377 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用next_tags指针前，存在明确的空指针检查（if (next_tags)），并且该指针仅在非空时才会被使用。因此，该告警是误报。 |
| 2378 | musl-1.2.1 | iconv | Dereference of null pointer | 374 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，函数已通过条件 `if (!((size_t)cd & 1))` 检查 `cd` 指针，并仅在条件为真时将 `scd` 赋值为非空指针。在 `ISO2022_JP` 处理分支中，访... |
| 2379 | musl-1.2.1 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码中，`tags` 指针作为函数参数传入，其值在切片内未显示为空。告警行访问 `tags[...]` 前，代码逻辑已通过 `if (match_eo >= 0 && !(cflags & REG_NOSUB))` 确保进入分支，... |
| 2380 | musl-1.2.1 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，变量 `max` 已在 `else if` 分支中被赋值为 `-1`，这发生在 `IS_TAG(lit) && (flags & COPY_MAXIMIZE_FI... |
| 2381 | musl-1.2.1 | iconv | Dereference of null pointer | 375 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，已通过条件 `if (!((size_t)cd & 1))` 检查了 `cd` 的有效性，并仅在条件为真时将 `scd` 指向非空地址。对于 `ISO2022_JP` 等需要 `s... |
| 2382 | musl-1.2.1 | iconv | Dereference of null pointer | 300 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，`scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。告警点位于 `case UCS2:` 和 `case UTF_16:` 分支... |
| 2383 | musl-1.2.1 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，已通过 `while (i < tnfa->num_submatches && i < nmatch)` 循环条件确保索引在有效范围内，且 `... |
| 2384 | musl-1.2.1 | queue_ctors | Dereference of null pointer | 1452 | FP | FP | 切片代码显示，在访问 `p->deps[p->next_dep]` 之前，`p` 来自 `stack`，而 `stack` 被初始化为 `queue`，`queue` 中的元素是 `dso` 及其依赖项，这些对象在入队前已通过 `p-... |
| 2385 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，存在 `if (stack->prev)` 的条件检查，确保 `stack` 不为空，且 `stack->item.state` 的访... |
| 2386 | musl-1.2.1 | iconv | Dereference of null pointer | 376 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，当 `cd` 的最低有效位为1时，`scd` 保持为0（NULL）。在告... |
| 2387 | musl-1.2.1 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 切片代码显示，在告警行（xmalloc调用）之前，函数开头已对参数tnfa进行了空指针检查（first_pass = (mem == NULL ｜｜ tnfa == NULL)），且后续使用tnfa->num_submatches时，... |
| 2388 | musl-1.2.4 | iconv | Dereference of null pointer | 373 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，函数已通过条件 `if (!((size_t)cd & 1))` 检查 `cd` 指针，并仅在条件为真时将 `scd` 赋值为非空指针。对于 `ISO2022_JP` 等需要 `s... |
| 2390 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 切片代码显示，在访问pmatch[bt]之前，pmatch已通过条件检查tnfa->num_submatches并调用xmalloc分配了内存，且tre_fill_pmatch函数内部有逻辑确保pmatch数组索引的有效性。因此，在正... |
| 2391 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在解引用指针 `next_tags` 之前，存在条件判断 `if (next_tags)`，这确保了指针非空。因此，该行代码不会发生空指针解引用，属于静态分析工具的误报。 |
| 2392 | musl-1.2.4 | do_relocs | Dereference of null pointer | 484 | FP | FP | 在REL_COPY分支中，memcpy调用前已通过条件判断确保def.sym和sym_val有效，且sym->st_size的访问受sym_index非零及def.sym存在保护，切片中未见明显的空指针解引用路径。 |
| 2393 | musl-1.2.4 | iconv | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，函数已通过条件 `if (!((size_t)cd & 1))` 检查 `cd` 的有效性，并仅在条件为真时将 `scd` 指向 `cd`。对于 `ISO2022_JP` 编码，`... |
| 2394 | musl-1.2.4 | iconv | Dereference of null pointer | 372 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，函数已通过条件 `if (!((size_t)cd & 1))` 检查 `cd` 指针，并仅在条件为真时将 `scd` 指向非空地址。对于 `ISO2022_JP` 等需要 `sc... |
| 2395 | musl-1.2.4 | do_relocs | Dereference of null pointer | 519 | FP | FP | 切片代码显示，在调用 malloc 分配内存后，立即检查了返回值 `if (!new)`，并在分配失败时通过 error 和 longjmp 处理错误，因此不会发生对 null 指针的解引用。 |
| 2396 | musl-1.2.4 | do_relocs | Dereference of null pointer | 458 | FP | FP | 切片代码显示，在警告行（第458行）对`def.dso->tls_id`进行解引用之前，已经存在对`def.sym`的检查（第437行），并且`def.dso`在`def.sym`为0时被明确赋值为`dso`（第434行），这确保了`... |
| 2397 | musl-1.2.4 | load_direct_deps | Dereference of null pointer | 1292 | FP | FP | 切片代码显示在访问 `p->deps[cnt]` 之前，已通过 `if (p->deps) return;` 检查了指针 `p->deps` 是否为 null，若为 null 则函数直接返回，因此不会发生空指针解引用。 |
| 2398 | musl-1.2.4 | do_relocs | Dereference of null pointer | 500 | FP | FP | 在切片代码中，`def.dso` 在 `sym_index` 为0的分支中被明确赋值为 `dso`，而在 `sym_index` 非零的分支中，`def` 也通过 `find_sym` 或 `get_lfs64` 被赋值，因此 `de... |
| 2399 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，存在 `if (next_tags)` 的条件检查，确保指针非空。因此，该解引用操作是安全的，属于静态分析工具的误报。 |
| 2400 | musl-1.2.4 | iconv | Dereference of null pointer | 374 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }` 对 `scd` 指针进行初始化。当 `cd` 为奇数时，`scd` 保持为0... |
| 2401 | musl-1.2.4 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `while (i < tnfa->num_submatches && i < nmatch)` 循环条件确保索引 `i` 在有效范围内，且 `submatch_data[i].so... |
| 2402 | musl-1.2.4 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，对数组`tag_directions`的访问发生在条件`IS_TAG(lit) && (flags & COPY_MAXIMIZE_FIRST_TAG) && first_tag`为真时，且索引`max`的值在之前的代码... |
| 2403 | musl-1.2.4 | iconv | Dereference of null pointer | 375 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为奇数（表示无状态转换）时 `scd` 保持为 N... |
| 2404 | musl-1.2.4 | iconv | Dereference of null pointer | 300 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1))`，当条件为真时 `scd` 被赋值为非空指针。告警点位于 `case UCS2:` 和 `case UTF_16:` ... |
| 2405 | musl-1.2.4 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，已通过 `while (i < tnfa->num_submatches && i < nmatch)` 循环条件确保索引在有效范围内，且 `... |
| 2406 | musl-1.2.4 | queue_ctors | Dereference of null pointer | 1553 | FP | FP | 切片代码显示，在访问 `p->deps[p->next_dep]` 之前，`p` 来自 `stack` 数组，而 `stack` 数组的元素是 `dso` 及其依赖项，这些对象在之前的逻辑中已被标记或管理，且循环条件 `p->next... |
| 2407 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，存在 `if (stack->prev)` 的条件检查，确保 `stack` 不为空；同时，`stack` 在函数入口处已通过 `tr... |
| 2408 | musl-1.2.4 | iconv | Dereference of null pointer | 376 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为奇数（表示无状态转换）时 `scd` 为 NULL，... |
| 2409 | musl-1.2.4 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 切片代码显示，在告警行（xmalloc调用）之前，函数参数tnfa已通过条件`first_pass = (mem == NULL ｜｜ tnfa == NULL)`进行检查，但该检查仅用于设置标志，并未阻止后续对tnfa->num_s... |
| 2410 | musl-1.1.24 | iconv | Dereference of null pointer | 373 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1))`，当 `cd` 为奇数时 `scd` 保持为 0，但后续仅在 `type` 为 `UCS2`、`UTF_16` 或 `... |
| 2411 | musl-1.1.24 | load_direct_deps | Dereference of null pointer | 1189 | FP | FP | 切片代码显示，在访问 `p->deps[cnt++]` 之前，`p->deps` 已被分配（`p->deps = (p==head && cnt<2) ? builtin_deps : ...`），且紧接着有 `if (!p->dep... |
| 2412 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 切片代码显示，在访问 `pmatch[bt].rm_so` 之前，`pmatch` 指针已通过 `xmalloc` 分配了内存，且 `bt` 是 `trans_i->u.backref`，其值受限于 `tnfa->num_submat... |
| 2413 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，存在 `if (next_tags)` 的条件检查，这确保了指针非空时才进行解引用操作，因此不会发生空指针解引用。 |
| 2414 | musl-1.1.24 | do_relocs | Dereference of null pointer | 430 | FP | FP | 在REL_COPY分支中，memcpy的目标地址reloc_addr由laddr函数计算返回，该函数逻辑确保返回有效地址或基址偏移，不会返回空指针；且sym_val由def.sym和def.dso计算，当def.sym存在时sym_v... |
| 2415 | musl-1.1.24 | iconv | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1))` 将 `scd` 初始化为非空指针。当 `cd` 为偶数时 `scd` 才被赋值，此时 `scd` 非空，其 `sta... |
| 2416 | musl-1.1.24 | iconv | Dereference of null pointer | 372 | FP | FP | 切片代码显示，在ISO2022_JP编码处理分支中，对变量`scd`的访问（`scd->state`）位于条件`if (!((size_t)cd & 1)) { scd = (void *)cd; }`之后。当`cd`为奇数时，`sc... |
| 2418 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，存在 `if (next_tags)` 的条件检查，这确保了指针不为空时才进行解引用操作，因此不会发生空指针解引用。 |
| 2419 | musl-1.1.24 | iconv | Dereference of null pointer | 374 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为状态转换描述符时 `scd` 才被赋值。在 `I... |
| 2420 | musl-1.1.24 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `while (i < tnfa->num_submatches && i < nmatch)` 循环条件确保索引 `i` 在有效范围内，且 `submatch_data[i].so... |
| 2421 | musl-1.1.24 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，变量 `max` 已被赋值为 -1（当 `(flags & COPY_REMOVE_TAGS)` 为真时）。由于 `tag_directions` 是一个数组指针... |
| 2422 | musl-1.1.24 | iconv | Dereference of null pointer | 375 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为奇数（表示无状态转换）时 `scd` 保持为 NUL... |
| 2423 | musl-1.1.24 | iconv | Dereference of null pointer | 300 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1))` 用于初始化 `scd` 指针。当 `cd` 为奇数时，`scd` 保持为 0，但此时代码逻辑不会进入 `case UCS... |
| 2424 | musl-1.1.24 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，`submatch_data` 指针已从 `tnfa->submatch_data` 获取，且 `tnfa` 指针作为函数参数传入，其有效性应... |
| 2425 | musl-1.1.24 | queue_ctors | Dereference of null pointer | 1447 | FP | FP | 在切片代码中，对指针 `p->deps[p->next_dep]` 进行解引用前，已通过 `while (p->next_dep < p->ndeps_direct)` 条件确保索引 `p->next_dep` 在有效范围内，且 `p... |
| 2426 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，存在 `if (stack->prev)` 的条件检查，确保 `stack` 不为空，且 `stack->item.state` 的访... |
| 2427 | musl-1.1.24 | iconv | Dereference of null pointer | 376 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为奇数时 `scd` 保持为 NULL。在 `ISO2... |
| 2428 | musl-1.1.24 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 切片代码显示，在告警行`regset = xmalloc(...)`之前，`tnfa`指针已在条件`first_pass = (mem == NULL ｜｜ tnfa == NULL)`中被检查，且后续对`tnfa->num_subm... |
| 2429 | musl-1.2.3 | iconv | Dereference of null pointer | 373 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1))` 来确保 `scd` 仅在 `cd` 为偶数（即非状态转换描述符）时才被赋值为非空指针。对于状态转换编码（如 ISO2... |
| 2431 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 切片代码显示，在访问 `pmatch[bt].rm_so` 之前，`pmatch` 指针已通过 `xmalloc` 分配内存，且 `bt` 是 `trans_i->u.backref`，其值受限于 `tnfa->num_submatc... |
| 2432 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在警告行（tags[*next_tags] = pos;）之前，next_tags指针已通过条件`if (next_tags)`进行了非空检查，并且其解引用操作`*next_tags >= 0`位于for循环条件中，该条... |
| 2433 | musl-1.2.3 | do_relocs | Dereference of null pointer | 440 | FP | FP | 在REL_COPY分支中，memcpy的目标地址reloc_addr由laddr函数计算得到，该函数保证返回非空指针；源地址sym_val由def.sym存在性保护，且sym->st_size的使用受sym_index非零和def.s... |
| 2434 | musl-1.2.3 | iconv | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `scd` 被使用时，它已被正确初始化（非空）。此外，在 `IS... |
| 2435 | musl-1.2.3 | iconv | Dereference of null pointer | 372 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，已通过条件 `if (!((size_t)cd & 1))` 检查 `cd` 指针，并仅在条件为真时将 `scd` 指向 `cd`。对于 `ISO2022_JP` 等需要 `scd... |
| 2437 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，存在 `if (next_tags)` 的条件检查，确保指针非空后才进入循环进行解引用操作，因此不会发生空指针解引用。 |
| 2438 | musl-1.2.3 | iconv | Dereference of null pointer | 374 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为奇数（表示无状态转换）时 `scd` 保持为 NUL... |
| 2439 | musl-1.2.3 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags` 数组前，`submatch_data[i].so_tag` 和 `submatch_data[i].eo_tag` 的值已与 `tnfa->end_tag` 进行了比较，若相等则不会使用 `tags... |
| 2440 | musl-1.2.3 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，变量 `max` 已被赋值为 -1（当 `(flags & COPY_REMOVE_TAGS)` 为真时），且 `tag_directions` 是一个数组指针。... |
| 2441 | musl-1.2.3 | iconv | Dereference of null pointer | 375 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为状态转换描述符时 `scd` 被正确赋值。在 `IS... |
| 2442 | musl-1.2.3 | iconv | Dereference of null pointer | 300 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1))` 用于初始化 `scd` 指针。当 `cd` 为奇数时，`scd` 保持为 0，但代码中 `type` 为 `UCS2` ... |
| 2443 | musl-1.2.3 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `while (i < tnfa->num_submatches && i < nmatch)` 循环条件确保索引 `i` 在有效范围内，且 `submatch_data[i].eo... |
| 2444 | musl-1.2.3 | queue_ctors | Dereference of null pointer | 1487 | FP | FP | 切片代码显示，在访问 `p->deps[p->next_dep]` 之前，`p` 来自 `stack`，而 `stack` 初始化为 `queue`，`queue` 要么是静态数组 `builtin_ctor_queue`，要么是 `... |
| 2445 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，存在 `if (stack->prev)` 的条件检查，确保 `stack` 不为空；同时，`stack` 在初始化时被分配了内存，且... |
| 2446 | musl-1.2.3 | iconv | Dereference of null pointer | 376 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为状态转换描述符时 `scd` 才被赋值，否则 `sc... |
| 2447 | musl-1.2.3 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 切片代码中，在告警行（xmalloc调用）之前，对函数参数`tnfa`进行了空指针检查（`first_pass = (mem == NULL ｜｜ tnfa == NULL)`），并且后续对`tnfa->num_submatches`... |
| 2448 | musl-1.2.2 | iconv | Dereference of null pointer | 373 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1))` 来初始化 `scd` 指针。对于 `ISO2022_JP` 编码处理，`scd` 仅在 `cd` 为偶数时被赋值，否... |
| 2450 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 切片代码显示，在访问 `pmatch[bt].rm_so` 之前，`pmatch` 已通过 `xmalloc` 分配了内存，且 `bt` 是来自状态机的 `trans_i->u.backref`，其值在 `tre_fill_pmatc... |
| 2451 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在警告行（tags[*next_tags] = pos;）之前，next_tags指针已通过条件'if (next_tags)'进行检查，确保其非空。此外，tags数组在循环中通过'for (; *next_tags >... |
| 2452 | musl-1.2.2 | do_relocs | Dereference of null pointer | 440 | FP | FP | 在REL_COPY分支中，memcpy的目标地址reloc_addr由laddr函数计算得到，该函数保证返回非空指针（返回p->base + v或经过计算的地址），且源地址sym_val由def.sym和def.dso保证有效，切片中... |
| 2453 | musl-1.2.2 | iconv | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，函数已通过条件 `if (!((size_t)cd & 1))` 检查 `cd` 的有效性，并仅在条件为真时将 `scd` 指向非空地址。对于 `ISO2022_JP` 等需要 `... |
| 2454 | musl-1.2.2 | iconv | Dereference of null pointer | 372 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这表明 `scd` 仅在 `cd` 为偶数（非状态转换描述符）时才被赋值。对... |
| 2456 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，存在 `if (next_tags)` 的条件检查，确保指针非空。因此，该解引用操作是安全的，属于静态分析工具的误报。 |
| 2457 | musl-1.2.2 | iconv | Dereference of null pointer | 374 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，这确保了当 `cd` 为偶数时 `scd` 才被赋值为非空指针。对于 `IS... |
| 2458 | musl-1.2.2 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码中，`tags` 数组的访问索引 `submatch_data[i].so_tag` 和 `submatch_data[i].eo_tag` 受 `i < tnfa->num_submatches` 循环条件约束，且 `tag... |
| 2459 | musl-1.2.2 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，变量 `max` 已被赋值为 -1（当 `(flags & COPY_REMOVE_TAGS)` 为真时），这可能导致数组索引越界或使用负索引。然而，该行位于 `... |
| 2460 | musl-1.2.2 | iconv | Dereference of null pointer | 375 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，已通过条件 `if (!((size_t)cd & 1))` 检查 `cd` 指针，并仅在条件为真时将 `scd` 赋值为非空指针。在 `ISO2022_JP` 分支中，访问 `s... |
| 2461 | musl-1.2.2 | iconv | Dereference of null pointer | 300 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，函数开头已通过条件 `if (!((size_t)cd & 1))` 检查了 `cd` 参数，若为偶数则将其转换为 `struct stateful_cd *` 指针并赋值给 `s... |
| 2462 | musl-1.2.2 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，已通过 `while (i < tnfa->num_submatches && i < nmatch)` 循环条件确保索引 `i` 在有效范围... |
| 2463 | musl-1.2.2 | queue_ctors | Dereference of null pointer | 1486 | FP | FP | 切片代码显示，在访问 `p->deps[p->next_dep]` 之前，`p` 来自 `stack`，而 `stack` 初始化为 `queue`，`queue` 已通过 `calloc` 分配并检查了非空，且 `p` 是 `dso... |
| 2464 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，存在条件 `if (stack->prev)` 检查，确保 `stack` 不为空且 `stack->prev` 存在，这防止了对空指... |
| 2465 | musl-1.2.2 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于switch-case语句中，该行仅是对scd->state进行赋值，而scd指针在函数入口处已通过条件判断确保非空（当cd为偶数时scd被赋值为(void*)cd，否则为0）。在ISO2022_JP编码处理路径中... |
| 2466 | musl-1.2.2 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 切片代码显示，在告警行`regset = xmalloc(...)`之前，函数开头已通过`first_pass = (mem == NULL ｜｜ tnfa == NULL)`检查了`tnfa`参数，但`tnfa`仅在`first_p... |
| 2467 | tmux-3.3 | recalculate_sizes_now | Dereference of null pointer | 458 | FP | FP | 在告警行访问 s->statuslines 之前，代码通过 TAILQ_FOREACH 遍历 clients，并且对每个 client c，调用了 ignore_client_size(c)。ignore_client_size 函数... |
| 2468 | tmux-3.3 | mode_tree_draw | Dereference of null pointer | 750 | FP | FP | 切片代码显示，在调用 xasprintf 函数前，已通过条件判断确保 mti 指针非空（mti = line->item），且 mti->name 的访问在多个路径中已被安全使用。xasprintf 函数内部会处理内存分配失败，不会导... |
| 2469 | tmux-3.3 | window_copy_search | Dereference of null pointer | 3674 | FP | FP | 切片代码显示，在访问 `data->searchmark[at]` 之前，已通过 `window_copy_search_mark_at(data, fx, fy, &at) == 0` 检查了 `at` 的有效性，并且 `at > ... |
| 2470 | tmux-3.3 | grid_string_cells | Dereference of null pointer | 1013 | FP | FP | 切片代码显示，在调用 `grid_string_cells_code(*lastgc, ...)` 之前，存在条件判断 `if (lastgc != NULL && *lastgc == NULL)`，该条件会初始化 `*lastgc... |
| 2471 | tmux-3.3 | mode_tree_draw | Dereference of null pointer | 754 | FP | FP | 切片代码显示，在告警行`xasprintf(&text, " %s", mti->name);`之前，`mti`指针已通过`mti = line->item;`或`mti = mti->parent;`赋值，且`line`来自`mtd... |
| 2472 | tmux-3.3 | grid_reflow_join | Dereference of null pointer | 1212 | FP | FP | 切片代码显示，在访问`from`指针前，`from`已在循环中被赋值为`&gd->linedata[line]`，且循环条件`if (lines == 0) return;`确保了`from`不为空。因此，`left = from->... |
| 2473 | tmux-3.3 | spawn_window | Dereference of null pointer | 180 | FP | FP | 告警点位于 `free(w->name);`，但切片代码显示，在 `if (~sc->flags & SPAWN_RESPAWN)` 分支中，`w` 被显式赋值为 `NULL`，因此当执行到该分支时，`w` 为 NULL，不会调用 `... |
| 2474 | tmux-3.3 | server_client_reset_state | Dereference of null pointer | 2340 | FP | FP | 切片代码显示，在访问 `s->cx` 和 `s->cy` 之前，变量 `s` 已被正确赋值：要么通过 `c->overlay_mode` 调用，要么赋值为 `wp->screen`。`wp` 来自 `server_client_get... |
| 2475 | tmux-3.3 | input_parse | Dereference of null pointer | 907 | FP | FP | 切片代码显示，在访问 `ictx->state->transitions` 之前，`ictx->state` 已在循环中被使用且未发生改变，表明其不为空；且若 `transitions` 指针为空，后续循环条件 `itr->first... |
| 2476 | tmux-3.2 | recalculate_sizes_now | Dereference of null pointer | 367 | FP | FP | 在访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已检查 `c->session` 是否为 NULL，若为 NULL 则提前返回，确保了后续 `s = c->session` 中的 `... |
| 2477 | tmux-3.2 | mode_tree_draw | Dereference of null pointer | 753 | FP | FP | 切片代码显示，在告警行使用 `mti->name` 之前，`mti` 指针已通过 `line->item` 赋值，且 `line` 来自 `mtd->line_list` 数组，该数组在循环中被安全访问。没有证据表明 `mti` 可能为空。 |
| 2478 | tmux-3.2 | window_copy_search | Dereference of null pointer | 3183 | FP | FP | 在访问 `data->searchmark[at]` 之前，代码通过 `window_copy_search_mark_at(data, fx, fy, &at) == 0` 检查了 `at` 的有效性，并且 `at > 0` 确保了... |
| 2479 | tmux-3.2 | spawn_window | Dereference of null pointer | 181 | FP | FP | 切片代码中，在告警行（w->name = format_single(...)）之前，变量 `w` 已在多个分支中被明确赋值（例如 `w = sc->wl->window` 或 `w = sc->wl->window`），且没有证据表... |
| 2480 | tmux-3.2 | grid_string_cells | Dereference of null pointer | 983 | FP | FP | 切片代码显示，在调用 `grid_string_cells_code(*lastgc, ...)` 之前，存在条件判断 `if (lastgc != NULL && *lastgc == NULL)`，该条件会初始化 `*lastgc... |
| 2481 | tmux-3.2 | mode_tree_draw | Dereference of null pointer | 757 | FP | FP | 切片代码显示，在调用xasprintf之前，mti指针已通过`mti = line->item;`赋值，且line来自`mtd->line_list[mtd->current]`，该数组在循环中已被安全访问。切片中未见mti可能为NU... |
| 2482 | tmux-3.2 | spawn_window | Dereference of null pointer | 185 | FP | FP | 告警指向 `w->name = default_window_name(w);` 行，但切片代码显示，在调用 `default_window_name(w)` 之前，变量 `w` 已在多个分支中被明确赋值（例如 `w = sc->wl... |
| 2483 | tmux-3.2 | grid_reflow_join | Dereference of null pointer | 1182 | FP | FP | 切片代码显示，在访问`from`指针前，`from = &gd->linedata[line];`已对其进行了赋值，且`line`变量在循环中受`gd->linedata[line].flags`和`gd->linedata[line... |
| 2484 | tmux-3.2 | server_client_reset_state | Dereference of null pointer | 1672 | FP | FP | 切片代码显示，在访问 `s->cx` 和 `s->cy` 之前，`s` 指针已在条件分支中被明确赋值（要么来自 `c->overlay_mode` 的调用结果，要么指向 `wp->screen`），且 `wp` 来自 `server_... |
| 2485 | tmux-3.2 | input_parse | Dereference of null pointer | 902 | FP | FP | 切片代码显示，在访问 `ictx->state->transitions` 之前，`ictx->state` 已在循环中被使用且未发生改变，表明其不为空；同时，`itr` 指针在循环中被递增前已通过 `while (itr->firs... |
| 2486 | tmux-3.1 | spawn_window | Dereference of null pointer | 185 | FP | FP | 切片代码中，在调用 format_single 函数前，已通过条件判断 sc->name != NULL 确保指针非空，因此不会发生空指针解引用。 |
| 2487 | tmux-3.1 | grid_string_cells | Dereference of null pointer | 927 | FP | FP | 切片代码显示，在调用 `grid_string_cells_code(*lastgc, ...)` 之前，函数开头已通过条件判断 `if (lastgc != NULL && *lastgc == NULL)` 将 `*lastgc`... |
| 2489 | tmux-3.1 | grid_reflow_join | Dereference of null pointer | 1126 | FP | FP | 切片代码显示，在访问 `from` 指针前，存在 `if (lines == 0) return;` 的检查，确保 `from` 在后续使用前已在循环中被赋值（`from = &gd->linedata[line];`）。当 `lin... |
| 2491 | tmux-3.1 | spawn_window | Dereference of null pointer | 189 | FP | FP | 切片代码显示，在调用 xstrdup(default_window_name(w)) 之前，变量 w 已在多个分支中被赋值或检查，包括在条件 (~sc->flags & SPAWN_RESPAWN) 分支中明确将 w 设置为 NULL... |
| 2492 | tmux-3.1 | cmdq_get_command | Dereference of null pointer | 248 | FP | FP | 切片代码显示，在`shared`被解引用之前，`TAILQ_FOREACH`循环内存在条件分支`if (cmd->group != group)`，当条件为真时会调用`xcalloc`为`shared`分配内存。`xcalloc`函数... |
| 2493 | tmux-3.1 | recalculate_sizes | Dereference of null pointer | 387 | FP | FP | 在告警行访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已对 `c->session` 进行了空指针检查，若为空则直接返回，确保了后续访问 `s`（即 `c->session`）时不为... |
| 2494 | tmux-3.0 | grid_string_cells | Dereference of null pointer | 918 | FP | FP | 切片代码显示，在调用 `grid_string_cells_code(*lastgc, ...)` 之前，存在条件判断 `if (lastgc != NULL && *lastgc == NULL)`，该条件会初始化 `*lastgc... |
| 2495 | tmux-3.0 | spawn_window | Dereference of null pointer | 183 | FP | FP | 切片代码中，在告警行 `w->name = xstrdup(sc->name);` 之前，已通过条件 `if (sc->name != NULL)` 对指针 `sc->name` 进行了非空检查，确保了不会对空指针进行解引用。 |
| 2496 | tmux-3.0 | grid_reflow_join | Dereference of null pointer | 1117 | FP | FP | 切片代码显示，在访问 `from` 指针前，`from` 已在循环中被赋值（`from = &gd->linedata[line];`），且后续的 `if (left != 0)` 条件检查确保了 `from` 非空时才使用。因此，该... |
| 2498 | tmux-3.0 | spawn_window | Dereference of null pointer | 186 | FP | FP | 告警点位于 `w->name = xstrdup(default_window_name(w));`，其中 `w` 在切片代码的 `else` 分支中被赋值为 `NULL`，但该赋值仅发生在 `(~sc->flags & SPAWN_... |
| 2499 | tmux-3.0 | cmdq_get_command | Dereference of null pointer | 233 | FP | FP | 切片代码显示，在首次进入循环或组号改变时，`shared` 会通过 `xcalloc` 分配内存，该函数保证返回非空指针（否则调用 `fatalx` 终止程序），因此 `shared` 在解引用前不可能为 NULL。 |
| 2500 | tmux-3.0 | options_array_set | Dereference of null pointer | 368 | FP | FP | 切片代码显示，在解引用 `cause` 指针（`*cause = xstrdup(...)`）之前，已经通过 `if (cause != NULL)` 进行了空指针检查，确保了 `cause` 非空时才解引用，因此不存在空指针解引用逻... |
| 2501 | tmux-3.4 | recalculate_sizes_now | Dereference of null pointer | 458 | FP | FP | 在告警行访问 s->statuslines 之前，TAILQ_FOREACH 循环内的 ignore_client_size(c) 函数已对 c->session 进行了 NULL 检查，若为 NULL 则跳过当前迭代，因此 s（即 ... |
| 2502 | tmux-3.4 | mode_tree_draw | Dereference of null pointer | 750 | FP | FP | 切片代码中，在调用xasprintf函数前，已通过条件判断确保mti指针非空（mti = line->item），且后续使用mti->name等成员时未进行空指针检查，但告警点位于xasprintf调用处，该函数内部会处理内存分配失败... |
| 2503 | tmux-3.4 | mode_tree_get_tag | Dereference of null pointer | 309 | FP | FP | 切片代码显示，在访问 `mtd->line_list[i].item->tag` 之前，循环条件 `i < mtd->line_size` 确保了索引 `i` 在 `line_list` 的有效范围内。虽然未直接检查 `item` 是... |
| 2504 | tmux-3.4 | mode_tree_draw | Dereference of null pointer | 754 | FP | FP | 切片代码中，在告警行 `xasprintf(&text, " %s", mti->name);` 之前，`mti` 已通过 `mti = line->item;` 和 `if (mti->draw_as_parent) mti = m... |
| 2505 | tmux-3.4 | grid_reflow_join | Dereference of null pointer | 1286 | FP | FP | 切片代码显示，在访问 `from` 指针前，`from` 已在循环中被赋值为 `&gd->linedata[line]`，且该循环在 `lines == 0` 时提前返回，确保了 `from` 不为空。因此，在警告行 `left = ... |
| 2506 | tmux-3.4 | spawn_window | Dereference of null pointer | 181 | FP | FP | 切片代码显示，在调用 free(w->name) 之前，变量 w 已在条件分支中被赋值为 NULL，因此该行代码仅在 w 不为 NULL 时才会执行，不会发生空指针解引用。 |
| 2507 | tmux-3.4 | grid_string_cells | Dereference of null pointer | 1073 | FP | FP | 切片代码显示，在调用grid_string_cells_code函数前，已通过条件判断确保lastgc指针不为NULL，且当*lastgc为NULL时已将其初始化为指向lastgc1的地址，因此解引用*lastgc是安全的。 |
| 2508 | tmux-3.4 | server_client_reset_state | Dereference of null pointer | 2394 | FP | FP | 切片代码显示，在访问 `s->cx` 和 `s->cy` 之前，变量 `s` 已在条件分支中被正确赋值（要么来自 `c->overlay_mode` 的调用结果，要么指向 `wp->screen`），且 `wp` 的获取函数 `ser... |
| 2509 | tmux-3.4 | window_copy_move_after_search_mark | Dereference of null pointer | 3691 | FP | FP | 在调用 `data->searchmark[start]` 之前，`window_copy_search_mark_at` 函数已返回0，这表明 `start` 索引已通过边界检查，且 `data->searchmark` 数组的访问... |
| 2510 | tmux-3.4 | input_parse | Dereference of null pointer | 912 | FP | FP | 切片代码显示，在访问 `ictx->state->transitions` 之前，`ictx->state` 已在循环中被使用且未发生改变，表明其不为空；同时，`fatalx` 函数会在 `itr` 查找失败时终止程序，防止了后续对无... |

### 5.3 不一致：算法=TP，LLM=FP（共 113 条）

> 算法认为是真实漏洞（TP），但 LLM 认为是误报（FP）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 276 | git-2.47.1 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含了 `ARRAY_SIZE(string) - 1`，但 `string` 是字符串字面量 `DIGIT "abcdefABCDEF"`，其大小固定且大于... |
| 277 | git-2.47.1 | test_ctype__ispunct | cpp/overflow-buffer | 91 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含了 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数 `PUNCT`，其具体内容在切片中不可见。然而，宏内使用了 `BUI... |
| 278 | git-2.47.1 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string) > 0` 的编译时断言通过时才会执行，这保证了数组大小至少为1，因此索引 `-... |
| 279 | git-2.47.1 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中 `ARRAY_SIZE(string) - 1` 的减1操作是在 `ARRAY_SIZE(string) > 0` 的编译时断言保护下执行的，确保了数组大小至少为1，因此不会出... |
| 280 | git-2.47.1 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | TP | FP | 告警指出的负索引访问发生在宏 `ARRAY_SIZE(string) - 1` 中，但切片代码显示 `string` 是一个字符串字面量 `"$()*+.?[\\^{｜"`，其 `ARRAY_SIZE` 肯定大于0，因此 `ARRAY... |
| 281 | git-2.47.1 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中用于计算 `len` 的表达式 `ARRAY_SIZE(string) - 1` 是安全的，因为 `ARRAY_SIZE(string)` 对于字符串字面量 `"*?[\\"` ... |
| 282 | git-2.47.1 | test_ctype__isalnum | cpp/overflow-buffer | 51 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数，在调用处为 `LOWER UPPER DIGIT`，这是一个字符串字面... |
| 283 | git-2.47.1 | test_ctype__isalpha | cpp/overflow-buffer | 46 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含了 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数 `LOWER UPPER`，其 `ARRAY_SIZE` 结果大于0... |
| 284 | git-2.47.1 | test_ctype__isdigit | cpp/overflow-buffer | 41 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string) > 0` 时才会执行，且 `BUILD_ASSERT_OR_ZERO` 宏在数... |
| 285 | git-2.47.1 | <global> | cpp/overflow-buffer | 36 | TP | FP | 切片代码显示函数体为空，不存在任何数组索引操作，因此工具报告的访问负索引-1的告警在可见上下文中不成立。 |
| 403 | git-2.46.0 | get_rev | cpp/inconsistent-null-check | 189 | TP | FP | 切片代码显示，在调用 `prio_queue_get` 后，代码立即通过 `entry->commit` 访问其成员，这隐含了对 `entry` 非空的假设。更重要的是，在调用 `prio_queue_get` 之前，函数已检查 `d... |
| 406 | git-2.46.0 | fill_bitmap_commit | cpp/inconsistent-null-check | 493 | TP | FP | 切片代码显示，在调用 `prio_queue_get` 的循环条件 `while (queue->nr)` 中，已确保队列非空，因此 `prio_queue_get` 不会返回 NULL。该前置条件检查使告警无效。 |
| 410 | git-2.46.0 | <global> | cpp/overflow-buffer | 37 | TP | FP | 切片代码中仅显示函数定义，未包含任何数组索引操作，因此工具报告的负索引访问在可见上下文中不存在，属于误报。 |
| 411 | git-2.46.0 | <global> | cpp/overflow-buffer | 38 | TP | FP | 切片代码中仅显示空的函数定义，没有数组访问操作，因此工具报告的负索引访问问题在可见上下文中不存在。 |
| 412 | git-2.46.0 | <global> | cpp/overflow-buffer | 39 | TP | FP | 切片代码仅显示函数空定义，未包含任何数组访问操作，无法支持工具报告的负索引访问告警。 |
| 413 | git-2.46.0 | <global> | cpp/overflow-buffer | 40 | TP | FP | 切片代码显示，宏`TEST_CHAR_CLASS`中的`ARRAY_SIZE(string) - 1`操作仅在`ARRAY_SIZE(string) > 0`时执行，且该条件由`BUILD_ASSERT_OR_ZERO`宏保证，因此不... |
| 414 | git-2.46.0 | <global> | cpp/overflow-buffer | 41 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 操作仅在数组大小大于0时执行，且存在 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > ... |
| 415 | git-2.46.0 | <global> | cpp/overflow-buffer | 42 | TP | FP | 切片代码显示，宏`TEST_CHAR_CLASS`内部循环索引`i`的范围是0到255，用于测试字符分类函数。告警所指的负索引-1（`string[-1]`）仅出现在宏定义中`ARRAY_SIZE(string) - 1`的计算部分，... |
| 416 | git-2.46.0 | <global> | cpp/overflow-buffer | 43 | TP | FP | 切片代码显示，宏`TEST_CHAR_CLASS`中的`ARRAY_SIZE(string) - 1`操作仅在数组大小大于0时执行，且存在`BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)`断言... |
| 417 | git-2.46.0 | <global> | cpp/overflow-buffer | 47 | TP | FP | 切片代码显示，宏`TEST_CHAR_CLASS`中的循环索引`i`范围固定为0到255，用于测试字符分类函数，不会产生负索引。告警提及的索引-1可能源于宏内`ARRAY_SIZE(string) - 1`的计算，但`string`是... |
| 418 | git-2.46.0 | <global> | cpp/overflow-buffer | 48 | TP | FP | 切片代码显示，`TEST_CHAR_CLASS` 宏中的 `ARRAY_SIZE(string) - 1` 操作仅在 `ARRAY_SIZE(string) > 0` 的编译时断言通过时才会执行，这确保了数组大小至少为1，因此索引 `... |
| 419 | git-2.46.0 | <global> | cpp/overflow-buffer | 49 | TP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 操作仅在 `ARRAY_SIZE(string) > 0` 的编译时断言通过时执行，确保了数组大小至少为1，因此索引 `-1... |
| 470 | curl-8_9_1 | Curl_splayremove | cpp/inconsistent-null-check | 270 | TP | FP | 在切片代码中，调用 `Curl_splay` 后，其返回值被直接赋值给变量 `x` 并随后被使用，但此处的逻辑是移除根节点时对子树进行展开，`t->smaller` 在调用前已被检查为非空，且 `Curl_splay` 函数内部对空输... |
| 673 | vim-9.1.1591 | <global> | cpp/redundant-null-check-simple | 3506 | TP | FP | 告警指出空指针检查是冗余的，因为该值在任何情况下都会被解引用。但在切片代码中，对 `inc_opt` 的检查 `if (inc_opt != NULL && ...)` 是合理的，因为 `inc_opt` 可能来自 `curbuf->... |
| 674 | vim-9.1.1591 | <global> | cpp/redundant-null-check-simple | 3588 | TP | FP | 告警指出的空指针检查冗余，但切片代码显示在检查前已通过`alloc`函数分配内存，且`alloc`失败时已通过`goto fpip_end`跳转，因此该检查是必要的防御性编程，并非冗余。 |
| 675 | vim-9.1.1591 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | TP | FP | 切片代码中，变量'col'在for循环初始化时被赋值为pos.col，随后在循环条件`check_prevcol(linep, col, '\\', &col)`中被使用，但该函数内部会对col进行递减和边界检查（col >= 0），... |
| 676 | vim-9.1.1591 | common_function | cpp/inconsistent-null-check | 5253 | TP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续代码中被 `vim_free(name)` 安全地释放，且没有在释放前进行解引用等危险操作。该告警是基于统计模式（88%的调用检查了null），但当前上下文中未检... |
| 677 | vim-9.1.1591 | common_function | cpp/inconsistent-null-check | 5366 | TP | FP | 告警点位于条件分支 `else if (is_funcref)` 内部，该分支仅在 `trans_name != NULL` 且 `find_func(trans_name, is_global) == NULL` 时才会执行。切片代... |
| 679 | vim-9.1.1591 | get_isolated_shell_name | cpp/inconsistent-null-check | 2743 | TP | FP | 切片代码显示，函数 `gettail` 在输入为 NULL 时会返回空字符串而非 NULL，这保证了 `vim_strsave` 的参数 `string` 非空。`vim_strsave` 内部已对 `alloc` 的返回值进行了 N... |
| 681 | vim-9.1.1591 | did_set_cryptmethod | cpp/inconsistent-null-check | 1923 | TP | FP | 切片代码显示，vim_strsave的返回值被赋值给全局变量p_cm，而p_cm是一个字符串选项指针，后续使用前会通过free_string_option处理，且该函数内部会检查指针是否为empty_option（一个特殊的空字符串常... |
| 682 | vim-9.1.1591 | did_set_background | cpp/inconsistent-null-check | 1098 | TP | FP | 切片代码显示，在调用`vim_strsave`后，其返回值`p_bg`立即被传递给`check_string_option`函数，该函数会检查指针是否为NULL并将其设置为安全值`empty_option`，因此即使内存分配失败，后续... |
| 683 | vim-9.1.1591 | apply_move_options | cpp/inconsistent-null-check | 531 | TP | FP | 切片代码显示，在调用 `find_win_by_nr_or_id` 后，其返回值 `wp->w_popup_prop_win` 立即被 `win_valid_any_tab` 函数检查，如果无效则会被重置为 `curwin`。这表明代... |
| 684 | vim-9.1.1591 | <global> | cpp/inconsistent-null-check | 3339 | TP | FP | 告警指出对regnext的调用结果未检查NULL，但切片代码显示在regnext函数内部已对NULL进行了处理（当p为JUST_CALC_SIZE或reg_toolong时返回NULL，且offset为0时也返回NULL），且调用点后... |
| 685 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1541 | TP | FP | 切片代码显示，在调用regnode后，其返回值br被立即用于条件判断（if (ret == NULL) ret = br;），这表明代码逻辑依赖于regnode的成功执行，而非其返回值是否为NULL。此外，regnode函数内部在re... |
| 686 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1562 | TP | FP | 切片代码显示，在调用regnode后，其返回值br被直接用于regtail等操作，但上下文表明regnode函数在regcode为JUST_CALC_SIZE时仅增加regsize而不返回NULL，且调用点前有对ret == JUST... |
| 687 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1579 | TP | FP | 切片代码显示，在调用`regnext(br)`的循环中，`br`变量来自`OPERAND(br)`或前一次迭代的`regnext`结果，而`regnext`函数内部已对`JUST_CALC_SIZE`和`reg_toolong`状态进... |
| 688 | vim-9.1.1591 | get_wordnode | cpp/inconsistent-null-check | 4636 | TP | FP | 切片代码显示，在调用getroom后，函数get_wordnode的返回值n在#ifdef SPELL_PRINTTREE块中被检查是否为NULL（`if (n != NULL)`），这表明代码已考虑并处理了潜在的NULL返回值情况。... |
| 689 | vim-9.1.1591 | do_tag | cpp/inconsistent-null-check | 638 | TP | FP | 切片代码显示，vim_strsave的返回值被立即赋值给变量'name'，随后在同一代码块中，'name'被重新赋值给'tag'，且原始指针'tofree'被释放。这表明代码逻辑旨在管理内存，且存在对分配内存的清理路径（vim_fre... |
| 690 | vim-9.1.1591 | is_duplicate_variable | cpp/inconsistent-null-check | 1044 | TP | FP | 切片代码仅显示函数定义，未包含对 `vim_strnsave` 的实际调用，无法确认存在未检查返回值的具体代码，因此判定为误报。 |
| 691 | vim-9.1.1591 | exec_instructions | cpp/inconsistent-null-check | 3699 | TP | FP | 切片代码中，alloc_clear的返回值被直接赋值给tv->vval.v_object，后续代码立即访问了该对象的成员（如obj_class、obj_refcount），这表明代码假设alloc_clear成功返回了非空指针。在切片... |
| 692 | vim-9.1.1591 | barline_parse | cpp/inconsistent-null-check | 1158 | TP | FP | 切片代码显示，调用 vim_strnsave 的结果被赋值给局部变量 s，而 s 随后被赋值给 value->bv_string，但 value->bv_allocated 被设置为 TRUE 或 converted 状态，表明内存管... |
| 693 | vim-9.1.1591 | common_function | cpp/unsafe-strcat | 5401 | TP | FP | 切片代码中，STRCAT宏被用于拼接已知大小的缓冲区IObuff和字符串start_bracket，且IObuff在STRCPY后已包含确定长度的字符串name，没有证据表明拼接会导致缓冲区溢出。 |
| 694 | vim-9.1.1591 | helptags_one | cpp/unsafe-strcat | 975 | TP | FP | STRCAT 宏用于拼接固定字符串 "/**/*" 和参数 ext，ext 是函数参数，在切片中未见其来源，但拼接的目标缓冲区 NameBuff 在代码中广泛使用且未显示其大小，但告警点拼接的字符串长度是固定且有限的，且该函数是内部工... |
| 696 | vim-9.1.1591 | store_aff_word | cpp/unsafe-strcat | 3915 | TP | FP | 切片代码显示，在调用STRCAT(newword, p)之前，newword数组已通过vim_strncpy(newword, ae->ae_add, MAXWLEN - 1)初始化，且目标缓冲区大小MAXWLEN已明确限定。此外，对... |
| 704 | vim-9.1.1591 | buf_write | cpp/unbounded-write | 2568 | TP | FP | 切片代码中未发现对strcat函数的直接调用，告警提及的'call to strcat'在提供的代码片段中不可见。基于切片内可见信息，无法确认存在缓冲区溢出风险，因此判定为误报。 |
| 705 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2150 | TP | FP | 切片代码中使用了宏STRCAT，其定义为strcat，但目标缓冲区'leader'的大小是动态计算的（lead_len + lead_repl_len + extra_space + extra_len + ... + 1），并且通过... |
| 709 | vim-9.1.1591 | win_redr_status_matches | cpp/unbounded-write | 698 | TP | FP | 切片代码显示，目标缓冲区 `buf` 的大小是根据 `Columns` 变量动态分配的（`alloc(Columns + 1)` 或 `alloc(Columns * MB_MAXBYTES + 1)`），并且在 `STRCPY` 调... |
| 710 | vim-9.1.1591 | win_redr_status_matches | cpp/unbounded-write | 717 | TP | FP | 切片代码显示，目标缓冲区 `buf` 的大小已根据 `Columns` 和 `MB_MAXBYTES` 通过 `alloc` 安全分配，且循环中的 `STRCPY` 操作目标为 `buf + len`，其写入长度受限于 `transc... |
| 717 | vim-9.1.1591 | ex_substitute | cpp/unbounded-write | 5115 | TP | FP | 切片代码中使用了宏STRCAT，其定义为strcat，但目标缓冲区new_start是动态分配的，其大小new_start_len在分配时考虑了所需长度并留有额外空间，且每次追加前都会检查缓冲区大小并进行扩容，因此不存在缓冲区溢出的风险。 |
| 718 | vim-9.1.1591 | make_filter_cmd | cpp/unbounded-write | 1854 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)分配了足够大小的缓冲区，且len的计算包含了源字符串cmd的长度和必要的额外字符及终止符，确保了目标缓冲区大小足以容纳源字符串，因此不存在缓冲区溢出风险。 |
| 719 | vim-9.1.1591 | make_filter_cmd | cpp/unbounded-write | 1858 | TP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过alloc(len)分配了缓冲区，且len的计算考虑了所有待拼接字符串的长度和终止符，缓冲区大小足够。因此，不存在缓冲区溢出的风险。 |
| 730 | vim-9.1.1591 | discard_exception | cpp/unbounded-write | 646 | TP | FP | 切片代码显示，目标缓冲区 IOBuff 的源数据 saved_IObuff 来自 vim_strsave(IObuff)，这是对 IOBuff 内容的复制，其长度在复制时已确定。STRCPY 宏展开为 strcpy，但源和目标缓冲区大... |
| 737 | vim-9.1.1591 | vim_rename | cpp/unbounded-write | 3865 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过`if (STRLEN(from) >= MAXPATHL - 5)`对源字符串`from`的长度进行了检查，确保其长度小于`MAXPATHL - 5`，而目标缓冲区`t... |
| 740 | vim-9.1.1591 | concat_fnames | cpp/unbounded-write | 3134 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc为目标缓冲区分配了足够的内存，其大小为两个源字符串长度之和加3，这确保了缓冲区大小足以容纳复制的内容，防止了缓冲区溢出。 |
| 755 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2920 | TP | FP | 切片代码显示告警点 `STRCPY(buffer, res_encoding->title);` 中的 `res_encoding->title` 来自受控的资源文件解析，其长度在 `prt_open_resource` 函数中通过 ... |
| 757 | vim-9.1.1591 | prt_resource_name | cpp/unbounded-write | 1659 | TP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，存在明确的前置长度检查（STRLEN(filename) >= MAXPATHL），当源字符串长度超过目标缓冲区容量（MAXPATHL）时，会通过将目标字符串首字符置为NUL来避免... |
| 760 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 991 | TP | FP | 切片代码显示NameBuff缓冲区在多次STRCAT操作前已通过STRCPY和add_pathsep进行路径构建，且告警点STRCAT的目标是tagfname参数，该参数来自函数调用者，在切片内未见其长度不受控的证据。结合上下文，缓冲... |
| 762 | vim-9.1.1591 | highlight_set_startstop_termcode | cpp/unbounded-write | 1488 | TP | FP | 切片代码中，在调用STRCAT（即strcat）之前，存在明确的长度检查 `if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`，确保拼接后的字符串不会超过目标缓冲区buf（大小为100）的容量，因此该... |
| 772 | vim-9.1.1591 | findswapname | cpp/unbounded-write | 4967 | TP | FP | 切片代码显示，STRCPY的目标缓冲区fname2是通过alloc(n + 2)分配的，其中n是源字符串fname的长度。目标缓冲区大小比源字符串长度多2，足以容纳源字符串和NUL终止符，因此不会发生缓冲区溢出。 |
| 773 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2157 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，目标缓冲区`s`是通过`alloc(STRLEN(f) + 1)`分配的，其大小精确等于源字符串`f`的长度加1，因此不会发生缓冲区溢出。 |
| 777 | vim-9.1.1591 | str2specialbuf | cpp/unbounded-write | 2015 | TP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度小于传入的长度参数`len... |
| 779 | vim-9.1.1591 | may_trigger_modechanged | cpp/unbounded-write | 2869 | TP | FP | 切片代码显示，STRCPY的目标缓冲区`last_mode`和源缓冲区`curr_mode`都是大小为`MODE_MAX_LENGTH`的字符数组，且`curr_mode`由`get_mode`函数填充，该函数内部逻辑确保写入的字符数... |
| 780 | vim-9.1.1591 | expand_env_esc | cpp/unbounded-write | 1678 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`c + STRLEN(tail) + 1 < (unsigned)dstlen`检查了目标缓冲区`dst`的剩余空间`dstlen`是否足以容纳源字符串`var`和后... |
| 784 | vim-9.1.1591 | add_to_showcmd | cpp/unbounded-write | 1764 | TP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已计算了目标缓冲区showcmd_buf的当前长度和待追加字符串p的长度，并检查了溢出（overflow）。如果溢出大于0，会通过mch_memmove移动缓冲区内容以腾出空间，... |
| 788 | vim-9.1.1591 | op_delete | cpp/unbounded-write | 962 | TP | FP | 切片代码中，STRCPY宏的目标缓冲区newp是通过alloc(ml_get_len(lnum) + 1 - n)分配的，其大小精确计算为原行长度减去删除字符数再加1，确保了目标缓冲区足够容纳源字符串oldp + bd.textcol... |
| 790 | vim-9.1.1591 | option_value2string | cpp/unbounded-write | 8459 | TP | FP | 切片代码显示，STRCPY宏的目标缓冲区NameBuff是一个全局数组，其大小未在切片中明确给出，但调用get_special_key_name返回的字符串长度受MAX_KEY_NAME_LEN常量限制，且该函数内部对数组边界有检查（... |
| 803 | vim-9.1.1591 | op_yank | cpp/unbounded-write | 1318 | TP | FP | 切片代码显示，STRCPY宏用于拼接两个已知长度的字符串，且目标缓冲区大小已通过alloc函数精确分配为两个源字符串长度之和加1，不存在缓冲区溢出的风险。 |
| 810 | vim-9.1.1591 | make_case_word | cpp/unbounded-write | 3140 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，函数allcap_copy和onecap_copy中均包含对目标缓冲区wcopy/cword的边界检查（如`d - wcopy >= MAXWLEN - 1`），且最终会写入终止... |
| 815 | vim-9.1.1591 | spell_move_to | cpp/unbounded-write | 1420 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过动态内存分配确保目标缓冲区`buf`的大小（`buflen`）大于等于源字符串长度（`len`）加上`MAXWLEN + 2`，这提供了足够的空间来容纳源字符串，从而防止了... |
| 816 | vim-9.1.1591 | getroom_save | cpp/unbounded-write | 4341 | TP | FP | 切片代码显示，目标缓冲区 `sc` 的大小是通过 `getroom(spin, STRLEN(s) + 1, FALSE)` 分配的，其长度精确等于源字符串 `s` 的长度加1，因此 `STRCPY`（即 `strcpy`）操作不会导... |
| 818 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2371 | TP | FP | 切片代码显示告警点位于处理拼写信息（如NAME、VERSION等）的代码块中，其中STRCAT操作的目标缓冲区p是通过getroom()分配的内存，其大小已根据源字符串长度精确计算（包括分隔符和空字符），因此不存在缓冲区溢出的风险。 |
| 824 | vim-9.1.1591 | add_sound_suggest | cpp/unbounded-write | 3243 | TP | FP | 切片代码显示，STRCPY的目标缓冲区`sft->sft_word`是通过`alloc(offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1)`分配的，其大小精确等于源字符串`goo... |
| 825 | vim-9.1.1591 | suggest_try_change | cpp/unbounded-write | 1199 | TP | FP | STRCPY宏的目标缓冲区fword被定义为固定大小的数组char_u fword[MAXWLEN]，且源字符串su->su_fbadword是内部拼写检查数据结构，其长度受MAXWLEN限制。切片代码显示在复制前有明确的长度检查（如... |
| 826 | vim-9.1.1591 | concat_str | cpp/unbounded-write | 792 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc函数为目标缓冲区分配了精确的、足以容纳源字符串（str1和str2）及其空终止符的内存大小，因此不存在缓冲区溢出的风险。 |
| 828 | vim-9.1.1591 | strlow_save | cpp/unbounded-write | 463 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，目标缓冲区`s`的大小是通过`alloc(STRLEN(res) + 1 + newl - l)`精确分配的，其长度足以容纳源字符串`p + l`（即`res`的剩余部分）。目标... |
| 833 | vim-9.1.1591 | show_one_termcode | cpp/unbounded-write | 7054 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，目标缓冲区IObuff的大小未知，但源字符串p来自get_special_key_name函数，该函数内部使用固定大小的静态缓冲区string[MAX_KEY_NAME_LEN ... |
| 836 | vim-9.1.1591 | fname_trans_sid | cpp/unbounded-write | 2278 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`fnamelen < FLEN_FIXED`确保目标缓冲区`fname_buf`有足够空间（FLEN_FIXED是固定大小），且`fnamelen`已计算了源字符串长... |
| 837 | vim-9.1.1591 | alloc_ufunc | cpp/unbounded-write | 728 | TP | FP | 切片代码显示，目标缓冲区 `fp->uf_name` 的大小是动态计算的 `len = offsetof(ufunc_T, uf_name) + namelen + 1`，并且分配的内存大小确保能容纳源字符串 `name` 及其空终止... |
| 838 | vim-9.1.1591 | exec_instructions | cpp/unbounded-write | 3929 | TP | FP | 切片代码中 STRCPY 宏的使用位于 ISN_EXECCONCAT 指令中，其中 cmd 缓冲区已通过 alloc(len + 1) 分配了足够长度（len 已预先计算所有字符串长度之和），且 STRCPY 前有 if (pass ... |
| 842 | vim-9.1.1591 | find_exported | cpp/unbounded-write | 763 | TP | FP | 切片代码显示，在调用sprintf前已通过动态分配确保目标缓冲区大小足够（len < sizeof(buffer)时使用栈缓冲区，否则分配len大小的堆缓冲区），因此不会发生缓冲区溢出。 |
| 844 | vim-9.1.1591 | ExpandBufnames | cpp/invalid-pointer-deref | 2980 | TP | FP | 切片代码显示，在写入 `(*file)[count++] = p` 之前，`*file` 已在循环第一轮通过 `*file = ALLOC_MULT(char_u *, count)` 分配了足够的内存，且 `count` 在写入时不... |
| 845 | vim-9.1.1591 | update_snapshot | cpp/invalid-pointer-deref | 2075 | TP | FP | 切片代码显示，在访问 `p[pos.col + 1]` 之前，已通过 `if (width == 2)` 条件确保 `pos.col + 1` 在分配的 `len` 范围内，且 `len` 由 `pos.col` 循环确定，`p` 分... |
| 1426 | redis-7.0.11 | rb_gen | Dereference of null pointer | 273 | TP | FP | 切片代码仅显示一个宏或函数定义（rb_gen），没有具体的指针解引用操作或数据流上下文，无法确认存在空指针解引用。告警可能源于静态分析工具对宏展开或复杂数据结构的误判。 |
| 1431 | redis-7.0.11 | <global> | Dereference of null pointer | 307 | TP | FP | 提供的切片代码仅为函数名或符号，不包含任何实际的指针解引用操作或数据流上下文，无法支持存在空指针解引用逻辑错误的结论。 |
| 1434 | redis-7.0.11 | <global> | Dereference of null pointer | 288 | TP | FP | 提供的切片代码仅为变量名'prof_gctx_comp'，不包含任何指针解引用操作或相关上下文，无法支持空指针解引用这一逻辑错误的判定，因此视为误报。 |
| 1586 | redis-8.0.2 | strbuf_init | Dereference of null pointer | 55 | TP | FP | 切片代码显示，函数 `strbuf_init` 仅将结构体成员 `s->buf` 初始化为 NULL，这是合法的初始化操作，并未发生对空指针的解引用。告警是对代码逻辑的误判。 |
| 1587 | redis-8.0.2 | breakstat | Dereference of null pointer | 986 | TP | FP | 切片代码显示，在访问 `bl->nactvar` 之前，`bl` 指针已在 `while` 循环中被更新，且循环条件 `while (bl && !bl->isbreakable)` 确保了只有当 `bl` 非空时才访问其成员。因此，... |
| 1594 | redis-8.0.2 | extent_try_coalesce_impl | Dereference of null pointer | 869 | TP | FP | 切片代码显示告警行是对布尔变量`*coalesced`的赋值操作，不存在指针解引用。`coalesced`是传入函数的指针参数，在函数入口处已通过`assert`确保`edata`非空，且告警行本身不涉及对空指针的访问。 |
| 1598 | redis-8.0.2 | rb_gen | Dereference of null pointer | 88 | TP | FP | 切片代码显示该行是宏定义或函数声明，并未包含任何实际的指针解引用操作。告警点本身不构成可执行的解引用逻辑，因此属于工具误报。 |
| 1601 | redis-8.0.2 | extent_try_coalesce_impl | Dereference of null pointer | 844 | TP | FP | 切片代码显示，在解引用指针 `coalesced` 之前，函数逻辑已确保其不为空。该指针是函数参数，在调用点被传入，且在告警行 `*coalesced = true;` 之前，代码路径已通过条件检查 `if (ecache->dela... |
| 1602 | redis-8.0.2 | <global> | Dereference of null pointer | 122 | TP | FP | 提供的切片代码仅为一行函数名声明，不包含任何实际的指针解引用操作，无法支持存在空指针解引用逻辑错误的结论。 |
| 1606 | redis-8.0.2 | <global> | Dereference of null pointer | 103 | TP | FP | 提供的切片代码仅为变量名'prof_gctx_comp'，不包含任何指针解引用操作或相关上下文，无法支持存在空指针解引用逻辑错误的结论。 |
| 1608 | redis-8.0.2 | tcache_create_ctl | Dereference of null pointer | 2467 | TP | FP | 切片代码显示，在调用 `tcaches_create` 函数前，`VERIFY_READ` 宏会检查 `oldp` 和 `oldlenp` 指针的有效性，若为 NULL 则提前返回错误，因此不会发生对空指针的解引用。 |
| 1612 | redis-8.0.2 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | TP | FP | 切片代码显示，在调用 `batch_alloc` 函数前，`batch_alloc_packet` 结构体已通过 `ASSURED_WRITE` 宏从 `newp` 安全写入，且 `VERIFY_READ` 宏会检查 `oldp` 和... |
| 1613 | redis-8.0.2 | json_next_token | Dereference of null pointer | 1024 | TP | FP | 切片代码显示，在访问 `ch2token[ch]` 之前，`ch` 的值来自 `*(json->ptr)`，而 `json->ptr` 在循环中会递增，但始终指向 `json->data` 缓冲区内的位置。`json->cfg` 和 ... |
| 1620 | redis-8.0.2 | min_expand | Dereference of null pointer | 322 | TP | FP | 在切片代码中，对指针 `ms` 的访问发生在条件 `s<ms->src_end` 之后，该条件已隐含了对 `ms` 非空的检查，因为如果 `ms` 为 NULL，则 `ms->src_end` 的解引用会导致更早的崩溃，而告警行处的 ... |
| 1622 | redis-8.0.2 | strbuf_ensure_null | Dereference of null pointer | 134 | TP | FP | 切片代码显示`s->buf`和`s->length`是结构体成员，但未提供其初始化或赋值上下文。函数名为`ensure_null`，其目的可能是确保缓冲区以空字符结尾，这是一种常见的防御性编程模式。在没有证据表明`s->buf`为NU... |
| 1625 | redis-8.0.2 | arenas_create_ctl | Dereference of null pointer | 3101 | TP | FP | 切片代码显示，在调用 `VERIFY_READ(unsigned)` 宏之前，`oldp` 和 `oldlenp` 指针可能为空，但该宏内部已包含对 `oldp` 和 `oldlenp` 是否为空的检查。如果它们为空，宏会设置错误码并... |
| 1626 | redis-8.0.2 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | TP | FP | 切片代码显示，在调用 `VERIFY_READ(unsigned)` 宏之前，`oldp` 和 `oldlenp` 指针可能为空，但该宏内部已包含对 `oldp` 和 `oldlenp` 是否为空的检查，若为空则直接设置错误码并跳转返... |
| 1749 | ffmpeg-7.0.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1428 | TP | FP | 切片代码显示`scale_matrix`在解引用前已通过条件`s->ps.sps->scaling_list_enable_flag && !(transform_skip_flag && log2_trafo_size > 2)`进... |
| 1765 | ffmpeg-7.0.1 | check_available | Dereference of null pointer | 608 | TP | FP | 切片代码显示，在访问 `TAB_MVF(n->x, n->y).pred_flag` 之前，`n->available` 的计算已包含对 `sps->r` 指针的访问，且该指针在函数开头已从 `fc->ps.sps` 安全获取。这表明... |
| 1794 | ffmpeg-7.0.1 | avc_parse_nal_units | Dereference of null pointer | 92 | TP | FP | 切片代码显示，在访问 `list->nalus` 之前，已经通过 `if (pb)` 和 `else if (list->nb_nalus >= nalu_limit)` 进行了条件判断。当 `pb` 为空且 `list` 非空时，才... |
| 1813 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 471 | TP | FP | 切片代码中，`DECODE_CODEWORD` 是一个宏，其内部会调用 `UPDATE_CACHE` 和 `GET_CACHE` 来操作 `GetBitContext *gb`，但未显示 `gb` 为空。告警点 `DECODE_COD... |
| 2140 | git-2.49.0 | process_entry | Dereference of null pointer | 3413 | TP | FP | 切片代码显示，在访问 `ci->ren2->pair->two->path` 之前，已通过 `if (ci->ren2)` 语句对 `ci->ren2` 进行了检查，确保其非空。该告警点位于 `RENAME_ONE_FILE_TO_T... |
| 2253 | git-2.50.1 | <global> | Dereference of null pointer | 88 | TP | FP | 切片代码显示告警位于单元测试的检查语句 `check_str(out[0], "a");`，该语句在 `out = parse_names(...);` 和 `check(out != NULL);` 之后。前置的 `check(ou... |
| 2262 | git-2.50.1 | <global> | Dereference of null pointer | 82 | TP | FP | 切片代码显示在访问 out[0] 之前已通过 check(out != NULL) 进行了空指针检查，且 parse_names 函数在成功时返回非空指针，失败时返回 NULL。告警点 check_str(out[0], "line"... |
| 2285 | git-2.50.1 | write_table | Dereference of null pointer | 65 | TP | FP | 切片代码显示，`(*names)[i]` 被赋值为 `xstrfmt` 的返回值，这是一个分配内存并返回有效指针的函数，不会返回空指针。同时，`refs` 和 `logs` 数组通过 `REFTABLE_CALLOC_ARRAY` 分... |
| 2297 | git-2.50.1 | <global> | Dereference of null pointer | 200 | TP | FP | 切片代码显示告警行位于单元测试中，且紧邻对指针arr的显式非空检查（check(arr != NULL)），这表明在解引用前已确保指针有效。该代码是测试逻辑的一部分，旨在验证分配成功，因此解引用是安全的。 |
| 2300 | git-2.50.1 | t_log_write_read | Dereference of null pointer | 224 | TP | FP | 切片代码中，`names[i] = xstrdup(name);` 处的 `name` 是局部数组 `char name[256]` 通过 `snprintf` 安全生成的字符串，`xstrdup` 内部会检查 `strdup` 的返... |
| 2308 | git-2.50.1 | <global> | Dereference of null pointer | 206 | TP | FP | 切片代码显示告警行位于单元测试中，且该行之前有明确的空指针检查（check(arr != NULL)），访问arr[alloc - 1]是在确认arr非空后进行的，因此不会发生空指针解引用。 |
| 2313 | git-2.50.1 | t_table_refs_for | Dereference of null pointer | 577 | TP | FP | 切片代码显示 `want_names` 数组在循环中被 `xstrdup` 返回的指针填充，`xstrdup` 函数在内存分配失败时会调用 `die` 终止程序，因此 `want_names` 元素不会为 NULL。随后 `free_... |
| 2367 | git-2.47.1 | assert_sane_strbuf | Dereference of null pointer | 36 | TP | FP | 切片代码显示，在解引用 `buf->buf` 之前，已通过 `check(!!buf->buf)` 宏对指针进行了非空检查，因此后续的 `buf->buf[buf->len]` 访问是受保护的，不会发生空指针解引用。 |
| 2488 | tmux-3.1 | <global> | Dereference of null pointer | 74 | TP | FP | 切片代码显示，在调用 `window_pane_key` 函数前，已对 `wme` 和 `wme->mode->key_table` 进行了空指针检查，且告警行位于检查通过后的安全分支内，不会发生空指针解引用。 |

### 5.4 不一致：算法=FP，LLM=TP（共 565 条）

> 算法认为是误报（FP），但 LLM 认为是真实漏洞（TP）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 10 | ffmpeg-6.1.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回了 `av_mallocz` 的调用结果，切片代码中未见对返回指针进行空值检查。调用者可能直接使用该指针，导致空指针解引用风险。 |
| 13 | ffmpeg-6.1.1 | get_frag_time | cpp/inconsistent-null-check | 1383 | FP | TP | 函数get_frag_stream_info可能返回NULL，但调用后未检查返回值就直接解引用其成员sidx_pts，存在空指针解引用风险。切片中未见任何防护机制。 |
| 15 | ffmpeg-6.1.1 | url_alloc_for_protocol | cpp/unbounded-write | 101 | FP | TP | 代码使用strcpy将filename复制到新分配的内存中，虽然分配大小为strlen(filename)+1，但filename可能来自外部输入（如环境变量），若在分配后、复制前被修改或存在并发问题，可能导致缓冲区溢出。切片中未见对... |
| 25 | ffmpeg-7.1.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回 `av_mallocz` 的调用结果，未对返回值进行空指针检查。切片代码中未见任何防护机制，若内存分配失败返回 NULL，后续使用可能导致程序崩溃。 |
| 31 | ffmpeg-7.1.1 | url_alloc_for_protocol | cpp/unbounded-write | 146 | FP | TP | 代码使用strcpy将filename复制到新分配的内存中，虽然分配的大小为strlen(filename)+1，但filename是外部传入的参数，若在分配后、复制前被修改或存在并发问题，可能导致缓冲区溢出。切片中未见对filena... |
| 40 | ffmpeg-7.0.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回了 `av_mallocz` 的调用结果，切片代码中未见对返回指针进行空值检查。根据告警信息，绝大多数调用都会检查空值，此处缺失检查可能导致后续对空指针的解引用风险。 |
| 44 | ffmpeg-7.0.1 | get_frag_time | cpp/inconsistent-null-check | 1541 | FP | TP | 函数 get_frag_stream_info 可能返回 NULL，但调用后未检查返回值就直接解引用访问其成员（如 sidx_pts），存在空指针解引用风险。切片中未见对该指针的有效防护。 |
| 46 | ffmpeg-7.0.1 | url_alloc_for_protocol | cpp/unbounded-write | 145 | FP | TP | 代码使用strcpy将filename复制到新分配的内存中，虽然分配的大小为strlen(filename)+1，但filename可能来自不受信任的命令行参数或环境变量，且切片中未见对filename长度进行前置校验或使用安全复制函... |
| 52 | ffmpeg-7.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 148 | FP | TP | 在while循环条件中，先访问`entries[m].flags`，然后才检查`m < b && m < nb_entries - 1`，存在数组越界访问的风险。切片代码中未见前置的索引范围校验来确保`m`在访问`entries`数组... |
| 56 | ffmpeg-7.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回 `av_mallocz` 的调用结果，切片代码中未见对返回指针进行空值检查。调用者可能直接使用该指针，存在空指针解引用的风险。 |
| 60 | ffmpeg-7.1 | get_frag_time | cpp/inconsistent-null-check | 1630 | FP | TP | 函数get_frag_stream_info在参数无效时会返回NULL，但调用后未检查返回值就直接解引用访问其成员sidx_pts，存在空指针解引用风险。切片中未见任何防护机制。 |
| 62 | ffmpeg-7.1 | cmp_dm_level0 | cpp/overflow-buffer | 294 | FP | TP | memcmp调用试图访问从结构体成员signal_eotf到结构体末尾的整个区域（大小为sizeof(AVDOVIColorMetadata) - offsetof(...)），这很可能超过该成员及其后续成员的实际大小，导致缓冲区溢出... |
| 63 | ffmpeg-7.1 | url_alloc_for_protocol | cpp/unbounded-write | 146 | FP | TP | 代码使用strcpy将filename复制到新分配的内存中，虽然分配的大小为strlen(filename)+1，但filename可能来自不受信任的命令行参数、环境变量或文件读取，且切片中未见对filename长度的前置验证或使用安... |
| 70 | ffmpeg-6.0 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 203 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回了 `av_mallocz` 的调用结果，切片代码中未见对返回指针进行空值检查。根据告警信息，绝大多数调用都会检查空值，此处的缺失可能导致后续对空指针的解引用风险。 |
| 73 | ffmpeg-6.0 | get_frag_time | cpp/inconsistent-null-check | 1286 | FP | TP | 函数get_frag_stream_info在索引无效或未找到匹配id时返回NULL，但调用后未检查返回值就直接解引用访问其成员，存在空指针解引用风险。 |
| 82 | openssl-openssl-3.5.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1729 | FP | TP | 切片代码显示，在调用 `memcmp` 比较 `s->session->ext.alpn_selected` 和 `s->s3.alpn_selected` 时，`s->s3.alpn_selected` 可能为 NULL（如果之前的... |
| 89 | openssl-openssl-3.5.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 在特定条件下（如 `enc_level` 越界或 `require_prov` 为真且状态不满足）会返回 NULL，但调用者 `ossl_qrl_enc_level_se... |
| 95 | openssl-openssl-3.5.1 | main | cpp/unbounded-write | 82 | FP | TP | 代码使用`strcpy`将命令行参数`argv[n]`复制到固定大小的缓冲区`pathname`（大小为`PATH_MAX`），若参数长度超过`PATH_MAX`将导致缓冲区溢出。切片中未见对`argv[n]`长度的前置校验，存在安全风险。 |
| 121 | openssl-openssl-3.3.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 在特定条件下（如 `enc_level` 越界或 `require_prov` 为真且状态不满足）会返回 NULL，但调用方 `ossl_qrl_enc_level_se... |
| 124 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 2582 | FP | TP | sprintf 使用来自命令行参数或环境变量的字符串 evp_mac_mdname 作为格式化参数，目标缓冲区 evp_hmac_name 的大小为固定字符串 "hmac()" 加上该变量长度，但若变量长度过长，拼接后的总长度可能超过... |
| 163 | openssl-openssl-3.4.1 | main | cpp/unbounded-write | 82 | FP | TP | 代码使用`strcpy`将命令行参数`argv[n]`复制到固定大小的缓冲区`pathname`（大小为`PATH_MAX`），但未检查`argv[n]`的长度是否小于`PATH_MAX`，存在缓冲区溢出风险。切片中未见对输入长度的前... |
| 188 | openssl-openssl-3.2.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 在特定条件下（如 `enc_level` 越界或 `require_prov` 为真且状态不满足）会返回 NULL，但调用方 `ossl_qrl_enc_level_se... |
| 190 | openssl-openssl-3.2.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | TP | 代码使用strcat向固定大小的缓冲区failure_text追加字符串，但未检查源字符串长度或目标缓冲区剩余空间，存在缓冲区溢出的风险。切片中未见任何长度校验或安全防护机制。 |
| 191 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 2530 | FP | TP | sprintf 使用来自命令行参数或环境变量的字符串 evp_mac_mdname 作为格式化参数，未进行长度检查，可能导致目标缓冲区 evp_hmac_name 溢出。切片中未见对 evp_mac_mdname 长度的限制或防护。 |
| 196 | openssl-openssl-3.2.1 | main | cpp/unbounded-write | 82 | FP | TP | 代码使用strcpy将命令行参数argv[n]复制到固定大小（PATH_MAX）的缓冲区pathname中，未检查源字符串长度，存在缓冲区溢出风险。切片中未见对argv[n]长度的前置校验。 |
| 224 | openssl-openssl-3.4.0 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 在特定条件下（如 `enc_level` 越界或 `require_prov` 为真且状态不满足）会返回 NULL，但调用者 `ossl_qrl_enc_level_se... |
| 226 | openssl-openssl-3.4.0 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | TP | 代码使用strcat向固定大小的缓冲区failure_text追加字符串，但切片中未显示对源字符串ts_failure_info[i].text的长度检查，也未显示对failure_text缓冲区剩余空间的检查，存在缓冲区溢出的风险。 |
| 230 | openssl-openssl-3.4.0 | main | cpp/unbounded-write | 82 | FP | TP | 代码使用`strcpy`将命令行参数`argv[n]`复制到固定大小的缓冲区`pathname`（大小为`PATH_MAX`），但未检查`argv[n]`的长度是否小于`PATH_MAX`，存在缓冲区溢出风险。切片中未见对输入长度的前... |
| 255 | git-2.47.1 | bisect_successful | cpp/inconsistent-null-check | 646 | FP | TP | 代码直接使用 lookup_commit_reference_by_name 的返回值 commit，未检查其是否为 NULL，随后在 oid_to_hex(&commit->object.oid) 中解引用 commit->obje... |
| 257 | git-2.47.1 | describe_commit | cpp/inconsistent-null-check | 324 | FP | TP | 函数 `lookup_commit_reference` 可能返回 NULL，但切片代码中未检查其返回值，后续代码直接解引用 `cmit->object.oid`，存在空指针解引用风险。 |
| 263 | git-2.47.1 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1924 | FP | TP | 切片代码中，函数submodule_from_path的返回值'sub'被直接解引用（sub->name），未进行空指针检查。根据告警信息，该函数95%的调用会检查空值，此处缺失检查可能导致空指针解引用崩溃。 |
| 268 | git-2.47.1 | clear_common_flag | cpp/inconsistent-null-check | 2132 | FP | TP | 代码在调用lookup_object后未检查返回的指针是否为NULL，便直接解引用（obj->flags），这可能导致空指针解引用崩溃。切片中未见任何防护逻辑确保obj非空。 |
| 286 | git-2.47.1 | add_patterns | cpp/invalid-pointer-deref | 1151 | FP | TP | 代码在分配大小为size的缓冲区后，执行了`buf[size++] = '\n';`，这明显是对缓冲区末尾之后一个字节的越界写入。切片中未见任何防护或校验来阻止此操作，因此存在内存损坏风险。 |
| 298 | git-2.50.1 | describe_commit | cpp/inconsistent-null-check | 326 | FP | TP | 代码在调用lookup_commit_reference后未检查返回值是否为NULL，随后直接解引用cmit（如cmit->object.oid），存在空指针解引用风险。切片中未见对该指针的有效防护或前置校验。 |
| 304 | git-2.50.1 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1932 | FP | TP | 切片代码中，`submodule_from_path` 的返回值 `sub` 被直接解引用（`sub->name`），未进行空指针检查。函数 `submodule_from_path` 可能返回 NULL，直接解引用会导致未定义行为或崩溃。 |
| 308 | git-2.50.1 | clear_common_flag | cpp/inconsistent-null-check | 2146 | FP | TP | 代码在调用 lookup_object 后未检查返回的指针是否为 NULL，便直接解引用访问 obj->flags，存在空指针解引用风险。切片中未见任何防护机制确保 obj 非空。 |
| 329 | git-2.50.1 | add_patterns | cpp/invalid-pointer-deref | 1152 | FP | TP | 代码在分配大小为 `size` 的缓冲区 `buf` 后，执行了 `buf[size++] = '\n';`，这明显是在缓冲区末尾之后的一个字节进行写入，属于越界写入。切片中未见任何防护或逻辑表明该写入是安全的。 |
| 343 | git-2.49.0 | bisect_successful | cpp/inconsistent-null-check | 648 | FP | TP | 函数 `lookup_commit_reference_by_name` 的返回值 `commit` 在后续 `repo_format_commit_message` 和 `oid_to_hex(&commit->object.oid... |
| 344 | git-2.49.0 | describe_commit | cpp/inconsistent-null-check | 326 | FP | TP | 函数 `lookup_commit_reference` 返回的指针 `cmit` 在未进行空值检查的情况下，立即被解引用（`cmit->object.oid`），这可能导致空指针解引用崩溃。切片代码中未见任何防护机制来确保该指针非空。 |
| 351 | git-2.49.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1932 | FP | TP | 切片代码中，`submodule_from_path`的返回值`sub`被直接解引用（`sub->name`），未进行空指针检查。根据告警信息，该函数95%的调用处都进行了空值检查，此处缺失检查可能导致解引用空指针，存在程序崩溃风险。 |
| 355 | git-2.49.0 | clear_common_flag | cpp/inconsistent-null-check | 2147 | FP | TP | 代码在调用`lookup_object`后未检查返回的`obj`指针是否为NULL，便直接解引用进行`obj->flags`操作，存在空指针解引用风险。切片中未见任何防护机制确保指针非空。 |
| 376 | git-2.49.0 | add_patterns | cpp/invalid-pointer-deref | 1152 | FP | TP | 代码在分配大小为 `size` 的缓冲区 `buf` 后，执行了 `buf[size++] = '\n';` 写入操作。`xmallocz` 分配了 `size` 字节，有效索引范围为 `0` 到 `size-1`，因此写入 `buf... |
| 385 | git-2.46.0 | bisect_successful | cpp/inconsistent-null-check | 644 | FP | TP | 函数 lookup_commit_reference_by_name 可能返回 NULL，但调用后未检查返回值，直接传递给 repo_format_commit_message 使用，存在空指针解引用风险。切片中未见任何防护机制。 |
| 387 | git-2.46.0 | describe_commit | cpp/inconsistent-null-check | 323 | FP | TP | 函数 `lookup_commit_reference` 的返回值 `cmit` 被直接解引用（`cmit->object.oid`），但切片代码中未见对该返回值进行空指针检查。根据规则描述，该函数可能返回 NULL，直接解引用存在空... |
| 393 | git-2.46.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1900 | FP | TP | 切片代码中，调用submodule_from_path返回的指针'sub'被直接解引用（sub->name），未进行空指针检查。根据告警信息，该函数95%的调用都检查了空值，此处缺失检查可能导致空指针解引用崩溃。 |
| 400 | git-2.46.0 | clear_common_flag | cpp/inconsistent-null-check | 2130 | FP | TP | 代码在调用`lookup_object`后未检查返回的`obj`指针是否为NULL，便直接解引用进行`obj->flags`操作，存在空指针解引用风险。切片中未见任何防护机制确保指针非空。 |
| 420 | git-2.46.0 | add_patterns | cpp/invalid-pointer-deref | 1150 | FP | TP | 代码在分配大小为 `size` 的缓冲区后，执行了 `buf[size++] = '\n';` 写入操作，这超出了 `xmallocz(size)` 分配的原始缓冲区边界一个字节，存在越界写入风险。切片中未见任何防护措施来防止此操作。 |
| 430 | git-2.44.0 | update_head | cpp/inconsistent-null-check | 648 | FP | TP | 代码直接使用 `lookup_commit_reference` 的返回值 `c` 访问其成员 `c->object.oid`，未检查返回值是否为 NULL。根据规则描述，该函数可能返回 NULL，且切片中未见任何前置校验或错误处理，... |
| 431 | git-2.44.0 | describe_commit | cpp/inconsistent-null-check | 320 | FP | TP | 函数 `lookup_commit_reference` 可能返回 NULL，但调用后未检查返回值，切片中后续代码直接解引用 `cmit->object.oid`，存在空指针解引用风险。 |
| 438 | git-2.44.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1838 | FP | TP | 切片代码中，`submodule_from_path`的返回值`sub`被直接解引用（`sub->name`），未进行空指针检查。根据告警信息，该函数95%的调用点都进行了空值检查，此处缺失检查可能导致空指针解引用，构成真实缺陷。 |
| 465 | git-2.44.0 | add_patterns | cpp/invalid-pointer-deref | 1117 | FP | TP | 代码在分配大小为 `size` 的缓冲区后，执行了 `buf[size++] = '\n';` 操作，这明显是在缓冲区末尾之后的一个字节进行写入，属于越界写。切片中未见任何防护或逻辑表明该写入是安全的。 |
| 484 | vim-9.1.0550 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数getcell可能返回NULL，但调用后未检查返回值就直接解引用cell->chars[0]，存在空指针解引用风险。切片代码中未见任何防护机制。 |
| 486 | vim-9.1.0550 | get_isolated_shell_name | cpp/inconsistent-null-check | 2706 | FP | TP | 函数 `vim_strnsave` 的返回值 `p` 被直接返回给调用者，切片代码中未检查其是否为 NULL，可能导致后续代码对空指针进行解引用。 |
| 507 | vim-9.1.0550 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 "%6ld" 写入最多6位数字加符号和终止符，可能超过20字节的目标缓冲区 tbuf，存在缓冲区溢出风险。切片中未见对输入 lnum 的范围校验或使用更安全的函数。 |
| 508 | vim-9.1.0550 | highlight_color | cpp/overrunning-write | 3254 | FP | TP | sprintf 目标缓冲区 'buf' 大小为10字节，但格式化字符串 '#%02x%02x%02x' 加上终止符需要至少10字节，在特定输入下（如 rgb 值全为0）恰好填满，但若 rgb 值产生非零高位字节，可能导致缓冲区溢出。切... |
| 509 | vim-9.1.0550 | msg_outnum | cpp/overrunning-write | 1555 | FP | TP | sprintf 的目标缓冲区 buf 大小为 20 字节，但格式化长整型数 "%ld" 最多可能需要 21 字节（包括负号和终止符），存在缓冲区溢出的风险。 |
| 510 | vim-9.1.0550 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf函数将格式化的字符串写入大小为32字节的reply数组，当cmdno和result的值组合超过31个字符（加上空终止符）时，会导致缓冲区溢出。切片代码中没有对输入参数进行长度检查或使用安全函数，存在明显的缓冲区溢出风险。 |
| 511 | vim-9.1.0550 | uc_check_code | cpp/overrunning-write | 1764 | FP | TP | sprintf 的目标缓冲区 num_buf 大小为 20 字节，但格式化长整型（%ld）的最大长度可能超过 20 字节（如 -9223372036854775808），导致缓冲区溢出。切片中未见对输入值 'num' 的范围校验，存在... |
| 512 | vim-9.1.0550 | ga_concat_strings | cpp/unbounded-write | 788 | FP | TP | 代码使用不安全的strcpy宏将动态长度的字符串复制到固定大小的缓冲区，且切片中未见对源字符串长度的检查或对目标缓冲区边界的防护，存在缓冲区溢出的风险。 |
| 513 | vim-9.1.0550 | maketitle | cpp/unbounded-write | 4112 | FP | TP | 代码使用STRCPY宏（即strcpy）将字符串p复制到icon_str，而p来自gettail函数处理的缓冲区文件名，其长度未经验证。icon_str指向大小为IOSIZE的缓冲区buf，但p的长度可能超过IOSIZE，导致缓冲区溢... |
| 517 | vim-9.1.0550 | transstr | cpp/unbounded-write | 366 | FP | TP | 代码使用STRCAT宏（即strcat）向动态分配的缓冲区res追加内容，但切片中未显示对res缓冲区剩余空间的检查。transstr函数根据输入字符串s计算长度并分配内存，但在循环中多次追加，存在缓冲区溢出的风险。 |
| 519 | vim-9.1.0550 | win_redr_status_matches | cpp/unbounded-write | 634 | FP | TP | 代码使用STRCPY宏（即strcpy）将可变长度字符串复制到固定大小的缓冲区中，缓冲区大小基于Columns计算，但源字符串长度未经验证，存在缓冲区溢出风险。切片中未见对源字符串长度的前置检查或安全限制。 |
| 521 | vim-9.1.0550 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码使用STRCPY（即strcpy）将fname复制到新分配的缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对fname长度的校验或使用安全函数。 |
| 522 | vim-9.1.0550 | has_profiling | cpp/unbounded-write | 973 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的源字符串fname复制到固定大小的目标缓冲区pe->pen_name，而目标缓冲区的大小仅通过STRLEN(fname)+1分配，这无法防止strcpy因源字符串未正确终止而导致的... |
| 523 | vim-9.1.0550 | do_string_sub | cpp/unbounded-write | 7697 | FP | TP | 切片代码中，STRCPY宏被直接用于将`tail`复制到`ga.ga_data`缓冲区，而`ga.ga_data`的大小由`ga_grow`调用保证，但`ga_grow`仅确保有足够空间容纳`(end - tail) + sublen... |
| 524 | vim-9.1.0550 | make_expanded_name | cpp/unbounded-write | 6918 | FP | TP | 代码使用STRCPY（即strcpy）将in_start复制到新分配的缓冲区retval，但未检查in_start的长度是否超过retval的大小。虽然retval的大小是根据表达式计算结果动态计算的，但in_start是外部输入的一... |
| 525 | vim-9.1.0550 | make_expanded_name | cpp/unbounded-write | 6920 | FP | TP | 代码使用STRCAT宏（即strcat）拼接字符串，目标缓冲区retval的大小由alloc分配，其长度计算为各部分长度之和加1，但STRCPY和STRCAT操作未在切片中显示有边界检查，存在缓冲区溢出的风险。 |
| 526 | vim-9.1.0550 | set_var_const | cpp/unbounded-write | 4183 | FP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname长度未经验证，可能导致目标缓冲区溢出。切片中未见对varname长度的限制或防护。 |
| 527 | vim-9.1.0550 | cat_prefix_varname | cpp/unbounded-write | 2504 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串复制到目标缓冲区，虽然目标缓冲区大小已根据源字符串长度动态分配，但分配后立即使用strcpy，未检查源字符串在分配后是否被修改或是否包含空终止符，存在缓冲区溢出的潜在风险。 |
| 528 | vim-9.1.0550 | ex_substitute | cpp/unbounded-write | 4862 | FP | TP | 切片代码中直接使用了未进行边界检查的STRCAT宏（即strcat），将sub_firstline + copycol的内容追加到new_start缓冲区，存在缓冲区溢出风险。切片内未见任何对目标缓冲区new_start长度的校验或防... |
| 529 | vim-9.1.0550 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | TP | 切片代码中直接使用STRCPY（即strcpy）将外部命令字符串cmd复制到固定大小的缓冲区buf中，未对cmd的长度进行校验，存在缓冲区溢出风险。 |
| 531 | vim-9.1.0550 | ex_sort | cpp/unbounded-write | 605 | FP | TP | 代码使用STRCPY宏（即strcpy）将行内容复制到固定大小的缓冲区sortbuf1，而sortbuf1的大小基于之前计算的最大行长maxlen分配。如果后续行的长度超过maxlen，strcpy将导致缓冲区溢出。切片中未见对复制前... |
| 532 | vim-9.1.0550 | expand_sfile | cpp/unbounded-write | 9823 | FP | TP | 代码使用STRCPY（即strcpy）将可变长度的字符串repl复制到固定大小的缓冲区newres中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对repl长度的限制或边界检查。 |
| 533 | vim-9.1.0550 | repl_cmdline | cpp/unbounded-write | 5332 | FP | TP | 切片代码中 STRCPY 宏直接展开为 strcpy，目标缓冲区 new_cmdline 的大小 i 由计算得出，但未对源字符串 src + srclen 的长度进行校验，存在缓冲区溢出的风险。 |
| 534 | vim-9.1.0550 | repl_cmdline | cpp/unbounded-write | 5338 | FP | TP | 代码使用不安全的STRCPY（即strcpy）宏将eap->nextcmd复制到固定大小的缓冲区new_cmdline中，而eap->nextcmd是外部输入，其长度未在切片内进行验证或限制，存在缓冲区溢出风险。 |
| 535 | vim-9.1.0550 | replace_makeprg | cpp/unbounded-write | 5039 | FP | TP | 代码使用STRCPY（即strcpy）宏将未经验证的用户输入（`p`）复制到固定大小的缓冲区（`ptr`指向的目标），且切片中未见对输入长度`len`的边界检查，存在缓冲区溢出的风险。 |
| 536 | vim-9.1.0550 | replace_makeprg | cpp/unbounded-write | 5054 | FP | TP | 代码使用STRCPY宏（即strcpy）将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区，未在切片中看到对源字符串长度的检查或使用安全函数，存在缓冲区溢出风险。 |
| 537 | vim-9.1.0550 | do_one_cmd | cpp/unbounded-write | 2677 | FP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将未知长度的字符串复制到固定大小的IObuff缓冲区，存在缓冲区溢出风险。切片中未见对源字符串长度的检查或使用安全函数。 |
| 538 | vim-9.1.0550 | discard_exception | cpp/unbounded-write | 642 | FP | TP | 代码使用不安全的STRCPY（即strcpy）宏将saved_IObuff复制回IObuff，而saved_IObuff是之前通过vim_strsave保存的IObuff副本，其长度可能超过IObuff的目标缓冲区大小，存在缓冲区溢出... |
| 539 | vim-9.1.0550 | get_exception_string | cpp/unbounded-write | 473 | FP | TP | 切片代码中，`val`指向的缓冲区大小由`vim_strnsave`分配，其大小计算包含了`mesg`的长度，但后续循环中`STRCAT(val, mesg)`或`STRCAT(val, p)`的调用，其源字符串`mesg`或`p`可... |
| 540 | vim-9.1.0550 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 切片代码中`sprintf`使用未限制长度的源字符串`&mesg[1]`作为格式化参数，目标缓冲区`val`的大小由之前的`vim_strnsave`分配，但未检查`&mesg[1]`的长度是否会导致溢出，存在缓冲区溢出风险。 |
| 541 | vim-9.1.0550 | escape_fname | cpp/unbounded-write | 4072 | FP | TP | 代码使用strcpy将源字符串复制到新分配的缓冲区，虽然缓冲区大小根据源字符串长度计算（STRLEN(*pp) + 2），但strcpy本身不检查边界，若源字符串未以空字符结尾或计算长度有误，仍可能导致缓冲区溢出。切片中未见对输入字符... |
| 542 | vim-9.1.0550 | cmdline_browse_history | cpp/unbounded-write | 1484 | FP | TP | 代码使用STRCPY宏（即strcpy）将历史条目字符串p复制到ccline.cmdbuff，目标缓冲区大小由alloc_cmdbuff根据p的长度分配，但分配后未检查p的长度是否超过缓冲区大小，且strcpy本身不限制复制长度，若p... |
| 543 | vim-9.1.0550 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 861 | FP | TP | 代码使用STRCPY（即strcpy）将动态长度的字符串p复制到固定缓冲区ccline.cmdbuff，虽然之前调用了realloc_cmdbuff，但该函数仅确保缓冲区长度不小于len，并未检查目标缓冲区大小是否严格匹配，strcp... |
| 544 | vim-9.1.0550 | <global> | cpp/unbounded-write | 5375 | FP | TP | 切片代码中`sprintf`使用未限制长度的`vim_tempdir`和递增的`temp_count`拼接字符串，目标缓冲区`itmp`大小固定为`TEMPNAMELEN`，存在缓冲区溢出风险。 |
| 545 | vim-9.1.0550 | vim_settempdir | cpp/unbounded-write | 5235 | FP | TP | 切片代码显示，当`vim_FullName`调用失败时，程序使用`STRCPY`（即`strcpy`）将未知长度的`tempdir`参数复制到固定大小的缓冲区`buf`中，而`buf`的大小为`MAXPATHL + 2`。`tempd... |
| 546 | vim-9.1.0550 | <global> | cpp/unbounded-write | 4352 | FP | TP | 代码使用`sprintf`将用户控制的`mesg`和`path`变量格式化到固定大小的缓冲区`tbuf`中，而`tbuf`的大小仅基于`path`、`mesg`和`mesg2`的长度之和分配，未考虑`sprintf`格式化扩展带来的额... |
| 548 | vim-9.1.0550 | buf_modname | cpp/unbounded-write | 3620 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证的外部输入（fname）复制到固定大小的缓冲区（retval），且切片中未见对fname长度的前置检查，存在缓冲区溢出风险。 |
| 549 | vim-9.1.0550 | addfile | cpp/unbounded-write | 4196 | FP | TP | 代码使用STRCPY（即strcpy）将参数f复制到新分配的内存p中，虽然p的大小根据f的长度（STRLEN(f) + 1 + isdir）分配，但f作为函数参数（文件名）可能来自不可信的外部输入（如环境变量、文件读取等），且切片中未... |
| 550 | vim-9.1.0550 | unix_expandpath | cpp/unbounded-write | 3833 | FP | TP | 切片代码中 STRCPY 宏直接展开为 strcpy，将源字符串复制到目标缓冲区，未检查目标缓冲区大小。目标缓冲区 `buf` 的大小为 `buflen`，但源字符串 `path_end + 1` 的长度可能超过剩余空间，存在缓冲区溢... |
| 551 | vim-9.1.0550 | concat_fnames | cpp/unbounded-write | 3123 | FP | TP | 代码使用STRCPY（即strcpy）将fname1复制到新分配的缓冲区dest，虽然缓冲区大小通过STRLEN(fname1) + STRLEN(fname2) + 3计算，但切片中未显示对fname1或fname2的来源进行任何验... |
| 554 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1720 | FP | TP | 切片代码中直接使用STRCPY（即strcpy）宏将rel_fname或*file_to_find复制到NameBuff缓冲区，未检查目标缓冲区大小（MAXPATHL）与源字符串长度的关系，存在缓冲区溢出风险。 |
| 555 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1721 | FP | TP | 切片代码中直接使用STRCPY（即strcpy）将可能较长的字符串复制到固定大小的缓冲区NameBuff（大小为MAXPATHL），且未在复制前检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 556 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1726 | FP | TP | 代码使用STRCPY（即strcpy）将*file_to_find复制到NameBuff中，而NameBuff的大小为MAXPATHL，但*file_to_find可能来自未经验证的环境变量或用户输入，其长度可能超过MAXPATHL，... |
| 557 | vim-9.1.0550 | ff_check_visited | cpp/unbounded-write | 1364 | FP | TP | 代码使用STRCPY（即strcpy）将ff_expand_buffer复制到vp->ffv_fname，目标缓冲区大小由分配时STRLEN(ff_expand_buffer)+1决定，但源缓冲区ff_expand_buffer可能通... |
| 564 | vim-9.1.0550 | <global> | cpp/unbounded-write | 533 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将未知长度的字符串复制到固定大小的缓冲区ff_expand_buffer，而该缓冲区的大小为MAXPATHL。切片中未显示对源字符串长度的检查或限制，存在缓冲区溢出的风险。 |
| 565 | vim-9.1.0550 | <global> | cpp/unbounded-write | 541 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的字符串复制到固定大小的缓冲区（如ff_expand_buffer），且未在切片内看到对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 567 | vim-9.1.0550 | <global> | cpp/unbounded-write | 586 | FP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将未知长度的字符串复制到固定大小的缓冲区，且未在切片内看到对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 568 | vim-9.1.0550 | <global> | cpp/unbounded-write | 587 | FP | TP | 切片代码中，`STRCAT(temp, search_ctx->ffsc_wc_path)` 使用了不安全的 `strcat` 函数，且 `temp` 缓冲区的大小为 `STRLEN(search_ctx->ffsc_wc_path)... |
| 569 | vim-9.1.0550 | <global> | cpp/unbounded-write | 3793 | FP | TP | 代码使用strcat将未经验证长度的字符串`s`追加到缓冲区`r`中，而`r`的分配大小仅考虑了`s`的初始长度，未考虑`s`可能被后续的`foldtext_cleanup`函数修改而变长，存在缓冲区溢出风险。 |
| 570 | vim-9.1.0550 | foldDelMarker | cpp/unbounded-write | 1892 | FP | TP | 代码使用STRCPY宏（即strcpy）将源字符串`p + len`复制到目标缓冲区`newline + (p - line)`，目标缓冲区大小由`alloc(ml_get_len(lnum) - len + 1)`分配，但未验证源字... |
| 571 | vim-9.1.0550 | foldAddMarker | cpp/unbounded-write | 1810 | FP | TP | 代码使用STRCPY（即strcpy）宏将line复制到newline，而newline的大小为line_len + markerlen + STRLEN(cms) + 1，虽然分配了足够空间，但strcpy本身不检查目标缓冲区大小，... |
| 572 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2899 | FP | TP | 代码使用STRCPY（即strcpy）将res_prolog->title复制到固定大小的buffer[256]中，而title的来源是外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 574 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2905 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而title的来源是外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 575 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2907 | FP | TP | 代码使用STRCAT宏（即strcat）将res_cidfont->version拼接到固定大小的buffer中，而version是从外部资源文件读取的，切片中未见对其长度的校验，存在缓冲区溢出风险。 |
| 578 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2920 | FP | TP | STRCPY宏直接展开为strcpy，将res_encoding->title复制到固定大小的buffer[256]中，切片内未见对title长度的校验，存在缓冲区溢出风险。 |
| 580 | vim-9.1.0550 | prt_resource_name | cpp/unbounded-write | 1659 | FP | TP | 代码使用strcpy复制字符串，虽然存在长度检查，但检查条件为`STRLEN(filename) >= MAXPATHL`时清空目标，否则执行复制。这未能防止源字符串长度恰好等于目标缓冲区大小（MAXPATHL）时导致的缓冲区溢出，因... |
| 581 | vim-9.1.0550 | do_helptags | cpp/unbounded-write | 1206 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的dirname复制到固定大小的NameBuff缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对dirname长度的校验或使用安全函数。 |
| 582 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 971 | FP | TP | 代码使用STRCAT宏（即strcat）向NameBuff缓冲区拼接字符串，但切片中未显示对NameBuff大小（MAXPATHL）的检查，也未限制输入字符串（dir, ext）的长度，存在缓冲区溢出的风险。 |
| 584 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 1108 | FP | TP | 代码使用sprintf将动态内容（p1和fname）写入固定大小的缓冲区s，而s的大小计算为(p2 - p1 + STRLEN(fname) + 2)，未考虑sprintf格式字符串本身可能导致的缓冲区溢出风险，存在潜在的安全问题。 |
| 586 | vim-9.1.0550 | load_colors | cpp/unbounded-write | 602 | FP | TP | sprintf 使用未经验证的用户输入 `name` 构造路径，目标缓冲区 `buf` 的大小为 `STRLEN(name) + 12`，但格式化字符串 "colors/%s.vim" 在 `name` 长度不变时总长度恰好为 `st... |
| 587 | vim-9.1.0550 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | sprintf 使用未经验证的字符串拼接，目标缓冲区 `fullname` 的大小 `len` 可能不足以容纳拼接后的完整路径，存在缓冲区溢出风险。切片中未见对最终字符串长度的安全计算或边界检查。 |
| 590 | vim-9.1.0550 | <global> | cpp/unbounded-write | 1456 | FP | TP | strcpy 的目标缓冲区 csinfo[i].fname 大小由 alloc(strlen(fname)+1) 分配，与源字符串 fname 长度相同，但 strcpy 不检查边界，若 fname 在分配后、复制前被修改或未正确终止... |
| 591 | vim-9.1.0550 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，未检查源字符串长度是否超过目标缓冲区大小。虽然目标缓冲区大小是根据strlen(fname)+1分配的，但若fname在分配与复制之间被并发修改，仍可能导致溢出。切片中未见任何锁或... |
| 592 | vim-9.1.0550 | cs_add_common | cpp/unbounded-write | 604 | FP | TP | 代码使用sprintf拼接路径和文件名，未对目标缓冲区大小进行限制，且拼接的源字符串长度可能超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 594 | vim-9.1.0550 | <global> | cpp/unbounded-write | 3097 | FP | TP | 代码使用sprintf将transchar(from)的返回值格式化到固定大小的缓冲区args->os_errbuf中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对目标缓冲区大小的限制或使用安全函数（如snprintf）的防护。 |
| 597 | vim-9.1.0550 | <global> | cpp/unbounded-write | 811 | FP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将call_data复制到新分配的缓冲区，未检查源字符串长度是否小于目标缓冲区大小。分配的缓冲区大小为STRLEN(call_data) + 5，但strcpy会复制整个源字符串直到空... |
| 598 | vim-9.1.0550 | <global> | cpp/unbounded-write | 815 | FP | TP | 代码在多个位置使用STRCPY宏（即strcpy）将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区，且切片中未见对源字符串长度进行校验或使用安全函数，存在缓冲区溢出风险。 |
| 599 | vim-9.1.0550 | msg_show_console_dialog | cpp/unbounded-write | 4387 | FP | TP | 代码使用STRCPY（即strcpy）将message复制到confirm_msg缓冲区，其大小由alloc(len)分配，而len的计算包含了STRLEN(message)，但未考虑目标缓冲区confirm_msg + 1的偏移，可... |
| 600 | vim-9.1.0550 | str2specialbuf | cpp/unbounded-write | 1919 | FP | TP | 切片代码显示，在调用STRCAT（即strcat）前，仅检查了源字符串s和目标缓冲区buf的当前长度之和是否小于len，但未检查拼接后是否会超出buf的原始总容量。如果buf在进入循环前已包含内容或len参数大于buf的实际大小，仍可... |
| 601 | vim-9.1.0550 | get_emsg_source | cpp/unbounded-write | 484 | FP | TP | sprintf 使用未限制长度的外部字符串 sname 作为格式化参数，且分配的目标缓冲区大小仅基于 sname 和 p 的当前长度计算，若 sname 在分配后被修改或包含额外格式化字符，可能导致缓冲区溢出。切片中未见对 sname... |
| 602 | vim-9.1.0550 | may_trigger_modechanged | cpp/unbounded-write | 2821 | FP | TP | 代码使用STRCPY（即strcpy）将curr_mode复制到last_mode，而curr_mode来自get_mode函数，其长度可能达到MODE_MAX_LENGTH。切片中未显示对last_mode目标缓冲区大小的检查或限制... |
| 603 | vim-9.1.0550 | expand_env_esc | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）将环境变量内容复制到目标缓冲区，虽然前面有长度检查（STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen），但该检查依赖于STRLEN(var)的结果... |
| 604 | vim-9.1.0550 | call_shell | cpp/unbounded-write | 1877 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区ncmd追加内容，而ncmd的大小仅基于ecmd和p_sxq的长度计算，未考虑追加的第三个字符串的长度，存在缓冲区溢出风险。 |
| 605 | vim-9.1.0550 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 切片代码中多次使用STRCAT宏（即strcat），将外部输入（如环境变量、文件读取数据）拼接到缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 606 | vim-9.1.0550 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | 代码使用sprintf将外部输入result和cmdno写入固定大小的缓冲区reply，而reply的大小仅基于result的长度计算，未考虑格式化字符串本身（'%d %s\n'）的额外长度，存在缓冲区溢出风险。 |
| 607 | vim-9.1.0550 | push_showcmd | cpp/unbounded-write | 1805 | FP | TP | 切片代码显示直接使用不安全的strcpy宏，将showcmd_buf复制到old_showcmd_buf，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 609 | vim-9.1.0550 | op_change | cpp/unbounded-write | 1866 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将源字符串复制到新分配的缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何边界检查或安全防护机制。 |
| 610 | vim-9.1.0550 | op_replace | cpp/unbounded-write | 1162 | FP | TP | 切片代码中 STRCPY 宏展开为 strcpy，目标缓冲区 newp 的大小为 oldlen + 1 + n，源字符串来自 oldp + bd.textcol + bd.textlen，其长度未在切片内进行验证或限制，存在缓冲区溢出... |
| 611 | vim-9.1.0550 | op_replace | cpp/unbounded-write | 1171 | FP | TP | 切片代码中直接使用STRCPY（即strcpy）宏，将未知长度的源字符串（`oldp + bd.textcol + bd.textlen`）复制到固定大小的目标缓冲区（`after_p`），未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 612 | vim-9.1.0550 | op_delete | cpp/unbounded-write | 825 | FP | TP | 切片代码中 STRCPY 宏展开为 strcpy，且目标缓冲区 newp 的大小为 `ml_get_len(lnum) + 1 - n`，而源字符串 `oldp + bd.textcol + bd.textlen` 可能超出该缓冲区长... |
| 613 | vim-9.1.0550 | block_insert | cpp/unbounded-write | 607 | FP | TP | 切片代码中，STRCPY宏被用于将`oldp`字符串复制到`newp + offset`位置，而`oldp`来自`ml_get`函数获取的行内容，其长度不受控制。目标缓冲区`newp`的大小由`alloc`分配，但复制前未检查`old... |
| 614 | vim-9.1.0550 | option_value2string | cpp/unbounded-write | 8155 | FP | TP | 代码使用不安全的STRCPY（即strcpy）宏将get_special_key_name函数的返回值复制到NameBuff缓冲区，但切片中未显示对源字符串长度的检查或对目标缓冲区大小的限制，存在缓冲区溢出风险。 |
| 616 | vim-9.1.0550 | stropt_expand_envvar | cpp/unbounded-write | 1757 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串`s`复制到新分配的目标缓冲区`newval`，但未检查源字符串长度是否超过目标缓冲区大小。虽然`newval`的大小是根据`STRLEN(s)`计算并分配的，但`s`来自`option... |
| 617 | vim-9.1.0550 | set_init_default_backupskip | cpp/unbounded-write | 169 | FP | TP | 代码使用STRCPY（即strcpy）将环境变量值复制到固定大小的缓冲区（item），而item的大小仅基于环境变量字符串长度加3分配，未考虑add_pathsep和STRCAT操作可能增加的字符，存在缓冲区溢出风险。 |
| 618 | vim-9.1.0550 | mch_expand_wildcards | cpp/unbounded-write | 6931 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区`command`追加内容，而`command`的大小由`alloc(len)`分配，`len`的计算依赖于多个外部输入（如环境变量、文件内容、命令行参数），若这些输入的总长度... |
| 619 | vim-9.1.0550 | mch_expand_wildcards | cpp/unbounded-write | 7277 | FP | TP | 切片代码中，`STRCPY(p, (*file)[i]);` 宏展开为 `strcpy`，目标缓冲区 `p` 的大小为 `STRLEN((*file)[i]) + 1 + dir`，而源字符串 `(*file)[i]` 的长度可能超过... |
| 620 | vim-9.1.0550 | mch_FullName | cpp/unbounded-write | 2816 | FP | TP | 切片代码显示在调用STRCAT(buf, fname)前，仅通过条件`(int)(STRLEN(buf) + STRLEN(fname)) >= len`检查了总长度，但未验证目标缓冲区`buf`在执行strcat前的剩余空间是否足以... |
| 621 | vim-9.1.0550 | qf_store_title | cpp/unbounded-write | 1932 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的title字符串复制到新分配的缓冲区p中，虽然p的大小根据STRLEN(title)+2分配，但若title字符串在分配后、复制前被并发修改变长，或存在未显示的缓冲区溢出风险，strc... |
| 622 | vim-9.1.0550 | reg_submatch | cpp/unbounded-write | 2689 | FP | TP | 切片代码中直接使用STRCPY（即strcpy）宏将未知长度的字符串复制到固定大小的缓冲区retval中，而retval的大小仅由alloc(len)分配，未对源字符串长度进行验证，存在缓冲区溢出风险。 |
| 623 | vim-9.1.0550 | reg_submatch | cpp/unbounded-write | 2698 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，将长度未知的源字符串（来自reg_getline_submatch）复制到固定大小的目标缓冲区retval中，而retval的大小仅由len变量决定，但len的计算基于匹配位置，未验证... |
| 625 | vim-9.1.0550 | match_with_backref | cpp/unbounded-write | 1600 | FP | TP | 代码使用STRCPY（即strcpy）将rex.line复制到reg_tofree，而reg_tofree的分配大小基于STRLEN(rex.line) + 50，但若rex.line在分配后、复制前被其他代码修改而变长，则可能发生缓... |
| 626 | vim-9.1.0550 | get_reg_contents | cpp/unbounded-write | 2668 | FP | TP | 代码使用STRCPY（即strcpy）将y_current->y_array[i]的内容复制到retval缓冲区，而目标缓冲区retval的大小是根据字符串长度总和预先计算的。虽然计算了总长度，但STRCPY调用本身不检查单个源字符串... |
| 627 | vim-9.1.0550 | do_put | cpp/unbounded-write | 2094 | FP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将y_array[y_size - 1]复制到固定大小的缓冲区newp中，而y_array的内容来自外部输入（如环境变量、文件读取等），未进行长度检查，存在缓冲区溢出风险。 |
| 628 | vim-9.1.0550 | do_put | cpp/unbounded-write | 2095 | FP | TP | 切片代码中直接使用了不安全的 `STRCAT` 宏（即 `strcat`），将 `y_array[y_size - 1]` 的内容拼接到未检查目标缓冲区大小的 `newp` 中，存在缓冲区溢出风险。 |
| 629 | vim-9.1.0550 | op_yank | cpp/unbounded-write | 1278 | FP | TP | 代码使用STRCPY宏（即strcpy）将两个字符串拼接，目标缓冲区大小通过alloc动态分配，但分配的大小基于两个源字符串的长度之和，未考虑strcpy的NUL终止符，存在缓冲区溢出的风险。 |
| 631 | vim-9.1.0550 | stuff_yank | cpp/unbounded-write | 452 | FP | TP | 代码使用STRCPY（即strcpy）将字符串从*pp复制到新分配的内存lp，但lp的大小是基于STRLEN(*pp) + STRLEN(p) + 1计算的，这确保了目标缓冲区足够大，不会发生溢出。然而，告警指出strcpy的输入可能... |
| 632 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2755 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区scriptname追加内容，该缓冲区大小仅基于输入name的长度分配，未考虑已存在的'autoload/'前缀长度，存在缓冲区溢出的风险。 |
| 633 | vim-9.1.0550 | ExpandPackAddDir | cpp/unbounded-write | 1226 | FP | TP | sprintf 使用未经验证的用户输入 `pat` 作为格式化字符串的一部分，目标缓冲区 `s` 的大小为 `pat_len + 26`，但格式化字符串 `"pack/*/opt/%s*"` 的长度加上 `pat` 的长度可能超过该缓... |
| 634 | vim-9.1.0550 | sign_jump | cpp/unbounded-write | 1324 | FP | TP | sprintf 使用未限制长度的缓冲区 buf->b_fname 作为输入，目标缓冲区 cmd 的大小仅基于 buf->b_fname 的当前长度计算，若 buf->b_fname 在分配后被修改或包含格式化字符，可能导致缓冲区溢出。... |
| 635 | vim-9.1.0550 | dump_word | cpp/unbounded-write | 4187 | FP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向未经验证的用户输入（如word或cword），存在缓冲区溢出风险。切片中未见对源字符串长度的检查或限制。 |
| 636 | vim-9.1.0550 | make_case_word | cpp/unbounded-write | 3140 | FP | TP | 切片代码中，当flags不满足WF_ALLCAP或WF_ONECAP时，直接使用STRCPY宏（即strcpy）将fword复制到cword，未对源字符串fword的长度进行任何检查，存在缓冲区溢出的风险。 |
| 637 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2998 | FP | TP | 代码使用STRCPY宏（即strcpy）将repl_to复制到新分配的缓冲区p中，未检查repl_to的长度是否超过目标缓冲区剩余空间，存在缓冲区溢出风险。切片中未见任何长度校验或安全防护。 |
| 638 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2999 | FP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p中，但p的大小是基于ml_get_curline_len() + addlen + 1分配的，未考虑拼接后总长度可能超过分配大小，存在缓冲区溢出风险。切片中未见长度检... |
| 639 | vim-9.1.0550 | count_common_word | cpp/unbounded-write | 1919 | FP | TP | 代码使用STRCPY宏（即strcpy）将字符串p复制到新分配的内存wc->wc_word中，而p的来源可能是外部输入（如环境变量、文件读取等），且切片中未见对p的长度进行校验以确保其不超过目标缓冲区大小的防护措施，存在缓冲区溢出风险。 |
| 640 | vim-9.1.0550 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）宏将参数lang直接复制到固定大小的数组sl.sl_lang中，切片未显示对lang的长度进行任何验证或限制，存在缓冲区溢出风险。 |
| 643 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2369 | FP | TP | 代码使用STRCAT宏（即strcat）将items[0]和items[1]拼接到缓冲区p中，而p的大小仅根据spin->si_info、items[0]和items[1]的长度计算，未检查目标缓冲区p的剩余容量，存在缓冲区溢出的风险。 |
| 645 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2464 | FP | TP | 切片代码中，STRCPY(p, items[1]) 直接将 items[1] 复制到 p，而 p 的大小为 STRLEN(items[1]) + 2，仅比源字符串多两个字节，若 items[1] 长度接近或等于缓冲区大小，可能导致缓冲... |
| 648 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2746 | FP | TP | 切片代码中第2746行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，未检查长度，可能导致缓冲区溢出。 |
| 653 | vim-9.1.0550 | concat_str | cpp/unbounded-write | 770 | FP | TP | 函数内部使用STRCPY（即strcpy）进行字符串复制，未对源字符串长度进行限制，而目标缓冲区大小仅由alloc根据两个源字符串长度之和分配。虽然分配大小正确，但strcpy本身不检查边界，若传入的str1或str2不是以空字符结尾... |
| 654 | vim-9.1.0550 | expand_tag_fname | cpp/unbounded-write | 4121 | FP | TP | 代码使用不安全的STRCPY（即strcpy）将tag_fname复制到固定大小的缓冲区retval，而tag_fname是外部输入（如环境变量、文件读取等），其长度未经验证，可能导致缓冲区溢出。切片中未见对tag_fname长度的前... |
| 655 | vim-9.1.0550 | findtags_add_match | cpp/unbounded-write | 2624 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区中，且未见对源字符串长度的检查或目标缓冲区大小的验证，存在缓冲区溢出的风险。 |
| 656 | vim-9.1.0550 | findtags_add_match | cpp/unbounded-write | 2703 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串（如st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区mfp中，而mfp的大小由alloc(len+1)分配，未对源字符串长... |
| 657 | vim-9.1.0550 | show_one_termcode | cpp/unbounded-write | 7058 | FP | TP | 切片代码显示STRCPY宏直接展开为strcpy，将get_special_key_name返回的字符串复制到IObuff+5位置，而IObuff的大小未知且未在切片内进行边界检查，存在缓冲区溢出风险。 |
| 658 | vim-9.1.0550 | current_tagblock | cpp/unbounded-write | 1386 | FP | TP | sprintf 使用未限制长度的用户输入（p 和 len）作为格式化字符串的一部分，且目标缓冲区 spat 和 epat 的大小仅基于 len 计算，未考虑格式化字符串本身的固定长度开销，存在缓冲区溢出风险。 |
| 659 | vim-9.1.0550 | uc_check_code | cpp/unbounded-write | 1691 | FP | TP | 切片代码中多处使用STRCPY（即strcpy）宏将外部输入（如eap->arg、*split_buf）复制到固定大小的缓冲区buf中，未对源字符串长度进行校验，存在缓冲区溢出风险。 |
| 660 | vim-9.1.0550 | get_scriptlocal_funcname | cpp/unbounded-write | 4608 | FP | TP | 代码使用STRCAT宏（即strcat）将未知长度的字符串拼接到固定大小的缓冲区newname中，newname的大小由alloc分配，但分配前未检查拼接后的总长度是否超过分配的大小，存在缓冲区溢出风险。 |
| 661 | vim-9.1.0550 | trans_function_name_ext | cpp/unbounded-write | 4521 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将内容复制到固定大小的sid_buf缓冲区，而源字符串sid_buf的内容来自格式化输出，其长度未在切片内进行限制，存在缓冲区溢出风险。 |
| 662 | vim-9.1.0550 | fname_trans_sid | cpp/unbounded-write | 2115 | FP | TP | 切片代码中，STRCPY宏直接展开为不安全的strcpy，且其目标缓冲区fname_buf的大小为FLEN_FIXED。虽然存在长度检查`i + STRLEN(name + llen) < FLEN_FIXED`，但该检查仅确保拼接后... |
| 663 | vim-9.1.0550 | fname_trans_sid | cpp/unbounded-write | 2127 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区fname的大小由alloc(i + STRLEN(name + llen) + 1)动态分配，但源字符串name + llen来自外部输入，其长度未在切片内进行验证或限制... |
| 664 | vim-9.1.0550 | set_ufunc_name | cpp/unbounded-write | 663 | FP | TP | 代码使用不安全的strcpy函数，将外部传入的字符串name复制到固定大小的缓冲区fp->uf_name中，切片中未见对name长度的校验或使用安全函数，存在缓冲区溢出风险。 |
| 666 | vim-9.1.0550 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到固定大小的缓冲区`funcname`中，而`funcname`的大小仅为`STRLEN(name) + 3`，未对源字符串长度进行限制，存在缓冲区溢出风险。切片中未见任... |
| 667 | vim-9.1.0550 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | TP | 代码使用STRCPY（即strcpy）将变量`name`复制到新分配的内存`newsav->sav_key`中，目标缓冲区大小仅为`STRLEN(name) + 1`，与源字符串长度相同，没有额外缓冲区来防止溢出。若`name`在复制... |
| 668 | vim-9.1.0550 | find_exported | cpp/unbounded-write | 756 | FP | TP | 代码使用`sprintf`将外部可控的`script->sn_autoload_prefix`和`name`拼接到固定大小的缓冲区`funcname`中，而`funcname`可能是指向栈上小数组`buffer[200]`的指针，且拼... |
| 669 | vim-9.1.0550 | find_exported | cpp/unbounded-write | 763 | FP | TP | sprintf 使用未限制长度的外部输入（sid 和 name）写入固定大小的缓冲区，存在缓冲区溢出风险。切片代码中未见对输入长度进行验证或使用安全函数（如 snprintf）的防护措施。 |
| 670 | vim-9.1.0550 | xxdline | cpp/unbounded-write | 533 | FP | TP | strcpy 的目标缓冲区 z 是固定大小的静态数组，而源 l 是外部输入，切片中未见对 l 长度的校验或限制，存在缓冲区溢出风险。 |
| 671 | vim-9.1.0550 | ExpandBufnames | cpp/invalid-pointer-deref | 2904 | FP | TP | 切片代码显示，在`(*file)[count++] = p;`行，`*file`指针可能为NULL（由`*file = NULL;`初始化），且当`*file == NULL`时，后续循环会直接返回FAIL，但若`*file`未被重新... |
| 700 | vim-9.1.1591 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 写入的格式化字符串长度可能超过目标缓冲区 reply 的 32 字节大小，切片中未见任何长度检查或使用安全函数，存在缓冲区溢出风险。 |
| 764 | vim-9.1.1591 | cs_resolve_file | cpp/unbounded-write | 2438 | FP | TP | sprintf 使用用户控制的 `name` 和 `csinfo[i].ppath` 拼接字符串，目标缓冲区 `fullname` 的大小 `len` 计算基于 `strlen(name) + 2` 加上可能的路径长度，但未考虑格式化... |
| 767 | vim-9.1.1591 | <global> | cpp/unbounded-write | 1454 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，但未检查fname的长度是否超过分配的大小（strlen(fname)+1），存在缓冲区溢出风险。切片中未见对fname长度的前置校验或使用安全复制函数。 |
| 768 | vim-9.1.1591 | <global> | cpp/unbounded-write | 1463 | FP | TP | 代码使用strcpy将fname复制到新分配的内存，但未检查fname的长度是否超过分配的大小，存在缓冲区溢出风险。切片中未见对源字符串长度的验证或使用安全函数。 |
| 769 | vim-9.1.1591 | cs_add_common | cpp/unbounded-write | 603 | FP | TP | sprintf 使用未限制长度的字符串拼接，目标缓冲区 fname2 的大小为 strlen(CSCOPE_DBFILE) + strlen(fname) + 2，但拼接后的字符串长度可能超过该值，存在缓冲区溢出风险。 |
| 781 | vim-9.1.1591 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 切片代码中多次使用STRCAT宏（即strcat），将外部输入（如环境变量、文件读取数据）拼接到固定大小的缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 782 | vim-9.1.1591 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf函数使用外部输入`result`和`cmdno`格式化字符串，目标缓冲区`reply`的大小为`STRLEN(result) + 32`，但sprintf的格式化输出长度可能超过此大小，导致缓冲区溢出。切片中未见对`re... |
| 850 | vim-9.1.1040 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数getcell在特定条件下（如行列越界或缓冲区为空）会返回NULL，但调用者vterm_screen_is_eol未对返回值进行空指针检查，直接解引用cell->chars，可能导致空指针解引用崩溃。切片中未见任何防护机制。 |
| 852 | vim-9.1.1040 | get_isolated_shell_name | cpp/inconsistent-null-check | 2721 | FP | TP | 函数 `vim_strnsave` 返回的指针 `p` 未进行空指针检查，而该函数在内存分配失败时会返回 NULL。调用者 `get_isolated_shell_name` 直接将 `p` 返回给上层，可能导致后续代码对空指针进行解... |
| 869 | vim-9.1.1040 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 "%6ld" 向大小为 20 字节的 tbuf 数组写入，当 lnum 为 6 位数字时，格式化后的字符串（包括结尾空字符）需要 7 字节，未超过缓冲区大小。但告警提示需要 21 字节，这表明工具可能认... |
| 870 | vim-9.1.1040 | highlight_color | cpp/overrunning-write | 3259 | FP | TP | sprintf 目标缓冲区 'buf' 大小为 10 字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少 8 个字符（# + 6个十六进制数字 + '\0'），计算为 8 字节，未超过 10 字节。然而，告警指出... |
| 871 | vim-9.1.1040 | msg_outnum | cpp/overrunning-write | 1653 | FP | TP | sprintf 的目标缓冲区 buf 大小为 20 字节，但格式化长整数（%ld）最多可能产生 21 个字符（包括负号和终止符），存在缓冲区溢出的风险。 |
| 872 | vim-9.1.1040 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf函数将格式化的字符串写入大小为32字节的固定缓冲区reply，当cmdno和result的值组合超过31个字符（加上空终止符）时，会导致缓冲区溢出。切片代码中未见任何对输入长度的校验或使用安全函数（如snprintf）的... |
| 873 | vim-9.1.1040 | ga_concat_strings | cpp/unbounded-write | 788 | FP | TP | 代码使用不安全的strcpy宏将动态长度的字符串复制到固定大小的缓冲区中，且切片内未见对目标缓冲区大小的检查或对源字符串长度的限制，存在缓冲区溢出风险。 |
| 874 | vim-9.1.1040 | maketitle | cpp/unbounded-write | 4147 | FP | TP | 代码使用STRCPY宏（即strcpy）将指针p的内容复制到icon_str缓冲区，而p指向的文件名长度可能超过目标缓冲区大小（IOSIZE），切片中未见对源字符串长度的限制性检查，存在缓冲区溢出风险。 |
| 875 | vim-9.1.1040 | buf_write | cpp/unbounded-write | 1208 | FP | TP | 代码使用STRCPY（即strcpy）将fname复制到固定大小的IObuff缓冲区，未检查fname长度，存在缓冲区溢出风险。切片中未见对fname长度的验证或使用安全函数。 |
| 877 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2138 | FP | TP | 代码中直接使用STRCAT宏（即strcat）将p_extra拼接到leader缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何边界检查或防护机制。 |
| 878 | vim-9.1.1040 | transstr | cpp/unbounded-write | 400 | FP | TP | 切片代码显示使用STRCAT宏（即strcat）向动态分配的缓冲区res追加内容，但未检查目标缓冲区剩余空间，存在缓冲区溢出的风险。 |
| 880 | vim-9.1.1040 | win_redr_status_matches | cpp/unbounded-write | 640 | FP | TP | 代码使用STRCPY宏（即strcpy）将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区中，未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。切片中未见对输入长度的验证或使用安全函数。 |
| 881 | vim-9.1.1040 | win_redr_status_matches | cpp/unbounded-write | 659 | FP | TP | 切片代码中，STRCPY宏被用于将transchar_byte(*s)的结果复制到buf+len位置，而buf的大小基于Columns计算，但transchar_byte的返回值长度未经验证，可能导致目标缓冲区溢出。 |
| 882 | vim-9.1.1040 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码使用STRCPY（即strcpy）宏将fname复制到新分配的缓冲区name中，未检查源字符串长度是否小于目标缓冲区大小。name的分配大小基于STRLEN(fname) + 3，但strcpy操作可能溢出目标缓冲区name + ... |
| 883 | vim-9.1.1040 | has_profiling | cpp/unbounded-write | 973 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的fname复制到固定大小的缓冲区pe->pen_name，而fname是外部传入的字符串，可能导致缓冲区溢出。切片中未见对fname长度的检查或使用安全函数。 |
| 885 | vim-9.1.1040 | do_string_sub | cpp/unbounded-write | 7726 | FP | TP | 切片代码中，STRCPY宏被用于将`tail`指向的字符串复制到动态分配的缓冲区`ga.ga_data`的末尾，但未检查目标缓冲区剩余空间是否足够容纳源字符串，存在缓冲区溢出风险。 |
| 887 | vim-9.1.1040 | cat_prefix_varname | cpp/unbounded-write | 2505 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到缓冲区`varnamebuf+2`，虽然缓冲区大小`varnamebuflen`根据`STRLEN(name)+3`计算并分配，但未对`name`的长度进行限制，且`n... |
| 889 | vim-9.1.1040 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | TP | 代码在多个分支中直接使用STRCPY（即strcpy）将外部输入（如cmd、itmp）复制到固定大小的缓冲区buf中，而buf的大小len是基于输入字符串长度计算的，但strcpy本身不检查目标缓冲区大小，若输入字符串长度计算有误或缓... |
| 891 | vim-9.1.1040 | ex_sort | cpp/unbounded-write | 605 | FP | TP | 代码使用STRCPY宏（即strcpy）将未知长度的源字符串`s`复制到固定大小的缓冲区`sortbuf1`中，而`sortbuf1`的大小仅基于`maxlen`分配，未考虑源字符串长度可能超过`maxlen`的情况，存在缓冲区溢出风险。 |
| 892 | vim-9.1.1040 | expand_sfile | cpp/unbounded-write | 10068 | FP | TP | 代码使用STRCPY宏（即strcpy）将可变长度的字符串repl复制到固定大小的缓冲区newres中，而newres的大小仅通过resultlen + 1计算，未检查repllen是否超过目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 893 | vim-9.1.1040 | repl_cmdline | cpp/unbounded-write | 5307 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，目标缓冲区new_cmdline的大小i由计算得出，但未对源字符串src + srclen的长度进行校验，存在缓冲区溢出的风险。 |
| 894 | vim-9.1.1040 | repl_cmdline | cpp/unbounded-write | 5313 | FP | TP | 切片代码中 STRCPY 宏直接展开为不安全的 strcpy 函数，目标缓冲区 new_cmdline 的大小 i 由多个长度计算而来，但未对源字符串 eap->nextcmd 的长度进行校验，存在缓冲区溢出风险。 |
| 895 | vim-9.1.1040 | replace_makeprg | cpp/unbounded-write | 5014 | FP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串p复制到目标缓冲区ptr，而p是用户输入的命令行参数，其长度可能超过目标缓冲区剩余空间，存在缓冲区溢出风险。切片中未见对p长度的检查或使用安全复制函数。 |
| 896 | vim-9.1.1040 | replace_makeprg | cpp/unbounded-write | 5029 | FP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串p复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小是基于program和p的长度计算分配的，但STRCPY本身不检查边界，若计算的长度不足或存... |
| 897 | vim-9.1.1040 | do_one_cmd | cpp/unbounded-write | 2678 | FP | TP | 切片代码中直接使用了不安全的 STRCPY 宏（即 strcpy），将未知长度的字符串（如错误消息）复制到固定大小的 IObuff 缓冲区，存在缓冲区溢出风险，且未见任何长度检查或防护机制。 |
| 898 | vim-9.1.1040 | discard_exception | cpp/unbounded-write | 646 | FP | TP | 代码使用不安全的STRCPY（即strcpy）宏将`saved_IObuff`复制回`IObuff`，而`saved_IObuff`是`vim_strsave(IObuff)`的副本，其长度与原始`IObuff`相同。由于`IObuf... |
| 899 | vim-9.1.1040 | get_exception_string | cpp/unbounded-write | 473 | FP | TP | 切片代码显示，`val`指向的缓冲区大小由`vim_strnsave`分配，其大小基于`cmdlen`和`STRLEN(mesg)`计算，但后续`STRCAT(val, mesg)`或`STRCAT(val, p)`操作中，`mesg... |
| 900 | vim-9.1.1040 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 切片代码中，sprintf 使用未受控的字符串 `&mesg[1]` 作为格式化参数，该字符串来自外部输入（异常消息），且未进行长度检查或使用安全函数，存在缓冲区溢出风险。 |
| 901 | vim-9.1.1040 | escape_fname | cpp/unbounded-write | 4105 | FP | TP | 代码使用strcpy将源字符串(*pp)复制到目标缓冲区(p+1)，目标缓冲区大小仅为源字符串长度加2（STRLEN(*pp)+2），但strcpy会复制包括空终止符在内的所有字符，若源字符串长度恰好等于分配大小减1，则复制空终止符时... |
| 902 | vim-9.1.1040 | cmdline_browse_history | cpp/unbounded-write | 1494 | FP | TP | 切片代码显示 STRCPY 宏直接调用了不安全的 strcpy 函数，将源字符串 p 复制到目标缓冲区 ccline.cmdbuff，而目标缓冲区的大小由 alloc_cmdbuff 分配，其长度仅基于源字符串长度 plen 加上少量... |
| 903 | vim-9.1.1040 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 860 | FP | TP | 代码使用不安全的STRCPY（即strcpy）将动态长度的字符串p复制到固定缓冲区ccline.cmdbuff，虽然前面调用了realloc_cmdbuff(len + 1)来调整缓冲区大小，但该函数内部使用alloc_cmdbuff... |
| 904 | vim-9.1.1040 | vim_settempdir | cpp/unbounded-write | 5286 | FP | TP | 代码使用不安全的STRCPY（即strcpy）将未知长度的tempdir复制到固定大小的buf中，虽然buf大小为MAXPATHL+2，但tempdir作为参数来源未在切片中显示有长度限制或验证，存在缓冲区溢出风险。 |
| 906 | vim-9.1.1040 | buf_modname | cpp/unbounded-write | 3636 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的fname复制到新分配的缓冲区retval中，虽然retval的大小基于fnamelen计算，但fname是外部输入（如环境变量、文件读取等），其长度可能超过目标缓冲区大小，存在缓... |
| 907 | vim-9.1.1040 | addfile | cpp/unbounded-write | 4202 | FP | TP | 代码使用STRCPY（即strcpy）将输入字符串f复制到新分配的内存p中，虽然p的大小根据STRLEN(f)+1分配，但若f在分配后、复制前被其他线程修改或存在并发问题，可能导致缓冲区溢出。切片中未见对f的锁定或长度再校验，存在潜在风险。 |
| 908 | vim-9.1.1040 | unix_expandpath | cpp/unbounded-write | 3837 | FP | TP | 切片代码中 STRCPY(s, path_end + 1) 宏展开为 strcpy，目标缓冲区 's' 指向栈分配的 'buf' 内部，源 'path_end + 1' 来自外部输入且长度未知，未在切片内看到对源字符串长度的检查或对目... |
| 911 | vim-9.1.1040 | uniquefy_paths | cpp/unbounded-write | 2364 | FP | TP | 代码使用STRCAT宏（即strcat）将可变长度的pattern字符串追加到新分配的file_pattern缓冲区，该缓冲区仅分配了len+2字节，但pattern可能包含任意长度，存在缓冲区溢出风险。切片中未见对pattern长度... |
| 912 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1718 | FP | TP | 切片代码中直接使用STRCPY（即strcpy）将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区NameBuff，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 913 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1719 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串复制到固定大小的缓冲区NameBuff中，存在缓冲区溢出风险。切片中未显示对源字符串长度的前置检查或使用安全函数。 |
| 914 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1724 | FP | TP | 代码使用STRCPY宏（即strcpy）将用户控制的`*file_to_find`复制到固定大小的`NameBuff`缓冲区，且切片中未见对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 915 | vim-9.1.1040 | ff_check_visited | cpp/unbounded-write | 1370 | FP | TP | 切片代码显示，STRCPY宏被用于将ff_expand_buffer复制到新分配的内存vp->ffv_fname中，而STRCPY被定义为strcpy。虽然分配的内存大小考虑了源字符串长度（STRLEN(ff_expand_buffe... |
| 922 | vim-9.1.1040 | <global> | cpp/unbounded-write | 537 | FP | TP | 切片代码中多次使用不安全的STRCPY宏（即strcpy），将长度未知的源字符串复制到固定大小的缓冲区ff_expand_buffer中，该缓冲区大小为MAXPATHL，但源字符串（如search_ctx->ffsc_start_di... |
| 923 | vim-9.1.1040 | <global> | cpp/unbounded-write | 545 | FP | TP | 切片代码中多次使用不安全的STRCPY宏（即strcpy），将未知长度的源字符串复制到固定大小的缓冲区（如ff_expand_buffer），且未在切片内看到对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 924 | vim-9.1.1040 | <global> | cpp/unbounded-write | 548 | FP | TP | 切片代码中，`STRCAT` 宏直接展开为 `strcat`，目标缓冲区 `ff_expand_buffer` 的大小为 `MAXPATHL`，但源字符串 `search_ctx->ffsc_fix_path` 的长度未经验证，存在缓... |
| 925 | vim-9.1.1040 | <global> | cpp/unbounded-write | 590 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy），将来源未知或长度未经验证的字符串（如环境变量、文件读取内容）复制到固定大小的缓冲区中，存在缓冲区溢出风险。切片内未见对源字符串长度的检查或使用安全函数。 |
| 926 | vim-9.1.1040 | <global> | cpp/unbounded-write | 591 | FP | TP | 切片代码中，`STRCAT(temp, search_ctx->ffsc_wc_path)` 使用了不安全的 `strcat` 函数，且 `temp` 缓冲区的大小为 `STRLEN(search_ctx->ffsc_wc_path)... |
| 927 | vim-9.1.1040 | <global> | cpp/unbounded-write | 3798 | FP | TP | 代码使用strcat将未经验证的外部输入（s，来自文件行内容）追加到固定大小的缓冲区r中，而r的分配大小计算可能未充分考虑s的长度，存在缓冲区溢出风险。切片中未见对s长度的校验或防护。 |
| 928 | vim-9.1.1040 | foldDelMarker | cpp/unbounded-write | 1897 | FP | TP | 代码使用STRCPY宏（即strcpy）将源字符串复制到新分配的缓冲区，未检查源字符串长度是否小于目标缓冲区大小。目标缓冲区大小由`ml_get_len(lnum) - len + 1`计算，但源字符串`p + len`的长度可能超过... |
| 929 | vim-9.1.1040 | foldAddMarker | cpp/unbounded-write | 1815 | FP | TP | 代码使用STRCPY（即strcpy）宏将line复制到newline，而newline的分配大小基于line_len、markerlen和STRLEN(cms)计算，但未检查line的实际长度是否超过line_len，存在缓冲区溢出... |
| 930 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2899 | FP | TP | 代码使用STRCPY（即strcpy）将res_prolog->title复制到固定大小的buffer[256]中，但切片内未显示对res_prolog->title长度的验证，存在缓冲区溢出风险。 |
| 931 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2901 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的字符串（res_prolog->title和res_prolog->version）长度在切片内未经验证，存在缓冲区溢出的风险。 |
| 932 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2905 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而title的来源是外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 933 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2907 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的字符串（res_cidfont->title和res_cidfont->version）长度在切片内未经验证，存在缓冲区溢出的风险。 |
| 934 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2912 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cmap->title复制到固定大小的buffer[256]中，而res_cmap->title是外部资源文件读取的字符串，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 936 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2920 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_encoding->title复制到固定大小的buffer（256字节）中，未检查源字符串长度，存在缓冲区溢出风险。切片中未见对res_encoding->title长度的验证或防护。 |
| 937 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2922 | FP | TP | 代码使用STRCAT宏（即strcat）将资源标题和版本号拼接到固定大小的缓冲区buffer（256字节）中，未检查缓冲区边界，存在缓冲区溢出风险。切片中未见对res_encoding->title或version长度的校验。 |
| 938 | vim-9.1.1040 | prt_resource_name | cpp/unbounded-write | 1659 | FP | TP | 切片代码显示，在调用STRCPY（即strcpy）前，仅检查了源字符串长度是否大于等于MAXPATHL，但未检查目标缓冲区resource_filename的大小。若目标缓冲区小于MAXPATHL，即使源字符串长度小于MAXPATHL... |
| 939 | vim-9.1.1040 | do_helptags | cpp/unbounded-write | 1210 | FP | TP | 代码使用STRCPY（即strcpy）将参数dirname复制到固定大小的NameBuff缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对dirname长度的验证或使用安全函数。 |
| 942 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 1112 | FP | TP | sprintf 使用未经验证的外部输入（p1 和 fname）作为格式化字符串的参数，且目标缓冲区 s 的大小仅根据 p2-p1 和 fname 的长度计算，未考虑 sprintf 格式化本身可能导致的缓冲区溢出风险。 |
| 944 | vim-9.1.1040 | load_colors | cpp/unbounded-write | 602 | FP | TP | sprintf 使用未经验证的输入 'name' 直接格式化字符串到固定大小的缓冲区 'buf'，而 'buf' 的大小仅基于 STRLEN(name) + 12 分配，无法防止 'name' 中包含格式化字符（如 %s）导致缓冲区溢... |
| 945 | vim-9.1.1040 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | sprintf 使用用户控制的 `name` 和 `csinfo[i].ppath` 拼接字符串，目标缓冲区 `fullname` 的大小 `len` 基于这两个字符串的长度计算，但未考虑格式化字符串 `"%s/%s"` 中额外的 '... |
| 947 | vim-9.1.1040 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | TP | 代码使用`sprintf`将多个字符串拼接至固定大小的缓冲区`buf`，缓冲区大小`amt`的计算已包含所有源字符串的长度，因此不会发生缓冲区溢出。该告警为误报，因为切片代码中已通过精确计算确保了目标缓冲区足够大。 |
| 948 | vim-9.1.1040 | <global> | cpp/unbounded-write | 1456 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，未检查fname长度是否超过分配的大小（strlen(fname)+1），存在缓冲区溢出风险。切片中未见任何长度校验或使用安全函数。 |
| 949 | vim-9.1.1040 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，未对源字符串长度进行任何检查。虽然目标缓冲区大小通过alloc(strlen(fname)+1)分配，但strcpy本身不检查边界，若fname在分配后、复制前被恶意修改（如并发环... |
| 950 | vim-9.1.1040 | cs_add_common | cpp/unbounded-write | 604 | FP | TP | sprintf函数使用未限制长度的字符串fname和常量CSCOPE_DBFILE拼接，目标缓冲区fname2的大小仅基于这两个字符串的长度计算，若fname长度被恶意控制，可能导致缓冲区溢出。切片中未见对fname长度的前置校验。 |
| 951 | vim-9.1.1040 | ins_compl_infercase_gettext | cpp/unbounded-write | 653 | FP | TP | 切片代码显示使用STRCPY宏（即strcpy）将IObuff复制到gap.ga_data，IObuff是一个固定大小的缓冲区（IOSIZE），而目标缓冲区gap.ga_data的大小未在切片中验证，存在缓冲区溢出风险。 |
| 952 | vim-9.1.1040 | <global> | cpp/unbounded-write | 3129 | FP | TP | 代码使用sprintf将格式化字符串和用户输入（来自transchar函数）写入固定大小的缓冲区args->os_errbuf，未进行长度检查，存在缓冲区溢出风险。切片中未见对目标缓冲区大小的限制或使用安全函数。 |
| 954 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2157 | FP | TP | 代码使用STRCPY（即strcpy）将fix_fname返回的字符串复制到新分配的缓冲区s中，虽然s的大小是根据源字符串长度分配的，但fix_fname函数可能返回一个更长的规范化路径，导致源字符串长度超过目标缓冲区大小，存在缓冲区... |
| 955 | vim-9.1.1040 | <global> | cpp/unbounded-write | 811 | FP | TP | 代码使用STRCPY宏（即strcpy）将call_data复制到新分配的缓冲区，未检查目标缓冲区大小，且call_data是外部输入，存在缓冲区溢出风险。切片中未见对call_data长度的验证或使用安全复制函数。 |
| 956 | vim-9.1.1040 | <global> | cpp/unbounded-write | 815 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将call_data复制到固定大小的缓冲区menu->strings[i]中，而call_data是外部输入，切片中未见对call_data长度的检查或对目标缓冲区大小的限制，存在缓冲区溢... |
| 957 | vim-9.1.1040 | msg_show_console_dialog | cpp/unbounded-write | 4502 | FP | TP | 代码使用STRCPY宏（即strcpy）将未经验证长度的message字符串复制到固定大小的confirm_msg缓冲区，且切片中未见对message长度的前置校验，存在缓冲区溢出风险。 |
| 959 | vim-9.1.1040 | get_emsg_source | cpp/unbounded-write | 502 | FP | TP | sprintf 使用未限制长度的源字符串 sname 和格式字符串 p 进行格式化，目标缓冲区 Buf 的大小为 STRLEN(sname) + STRLEN(p)，这仅能容纳两个字符串的连接，但 sprintf 会额外写入格式字符 ... |
| 960 | vim-9.1.1040 | may_trigger_modechanged | cpp/unbounded-write | 2836 | FP | TP | 代码使用STRCPY（即strcpy）将curr_mode复制到last_mode，而last_mode的大小未知，curr_mode来自get_mode函数，其最大长度为MODE_MAX_LENGTH，但切片中未见对last_mod... |
| 961 | vim-9.1.1040 | expand_env_esc | cpp/unbounded-write | 1647 | FP | TP | 代码在调用STRCPY（即strcpy）前，仅通过`STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen`检查了目标缓冲区大小，但未验证源字符串`var`的长度是否小于目标缓冲区`dst`... |
| 963 | vim-9.1.1040 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 切片代码中多次使用STRCAT宏（即strcat），将外部输入（如环境变量、文件读取内容）拼接到固定大小的缓冲区，没有可见的边界检查，存在缓冲区溢出风险。 |
| 964 | vim-9.1.1040 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf 使用未受控的输入 result 和 cmdno 写入固定大小的缓冲区 reply，而 reply 的大小仅基于 result 的长度计算，未考虑格式化字符串本身（如 cmdno 和空格、换行符）的额外长度，存在缓冲区溢... |
| 965 | vim-9.1.1040 | push_showcmd | cpp/unbounded-write | 1808 | FP | TP | 代码使用不安全的strcpy函数，将源缓冲区showcmd_buf的内容复制到目标缓冲区old_showcmd_buf，切片中未显示对源字符串长度的检查或对目标缓冲区大小的保护，存在缓冲区溢出风险。 |
| 967 | vim-9.1.1040 | op_change | cpp/unbounded-write | 2003 | FP | TP | 切片代码中 STRCPY 宏被直接用于将源字符串复制到目标缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 968 | vim-9.1.1040 | op_replace | cpp/unbounded-write | 1299 | FP | TP | 切片代码中 STRCPY 宏被直接展开为 strcpy，且目标缓冲区 newp 的大小为 oldlen + 1 + n，源字符串来自 oldp + bd.textcol + bd.textlen，其长度未在切片内进行验证或限制，存在缓... |
| 969 | vim-9.1.1040 | op_replace | cpp/unbounded-write | 1308 | FP | TP | 切片代码中直接使用STRCPY（即strcpy）宏，将源字符串复制到固定大小的目标缓冲区，且未见对源字符串长度的检查或对目标缓冲区边界的防护，存在缓冲区溢出的风险。 |
| 970 | vim-9.1.1040 | op_delete | cpp/unbounded-write | 962 | FP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将源字符串复制到目标缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 971 | vim-9.1.1040 | block_insert | cpp/unbounded-write | 743 | FP | TP | 代码使用STRCPY（即strcpy）将oldp复制到newp + offset，未检查目标缓冲区newp的大小，且oldp是来自ml_get的任意行内容，其长度可能超过剩余缓冲区空间，存在缓冲区溢出风险。 |
| 972 | vim-9.1.1040 | option_value2string | cpp/unbounded-write | 8324 | FP | TP | 代码使用STRCPY（即strcpy）宏将get_special_key_name函数的返回值复制到NameBuff，但切片中未显示NameBuff的大小，也未对源字符串长度进行限制，存在缓冲区溢出风险。 |
| 974 | vim-9.1.1040 | stropt_expand_envvar | cpp/unbounded-write | 1803 | FP | TP | 切片代码显示，STRCPY宏直接展开为strcpy，目标缓冲区newval的大小newlen基于源字符串s的长度计算，但未检查s的长度是否超过newval的分配大小。由于s来自外部环境变量或文件读取（如option_expand调用e... |
| 975 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 6989 | FP | TP | 切片代码中多次使用STRCAT宏（即strcat）向固定大小的缓冲区`command`追加内容，而`command`的大小由`alloc(len)`分配，`len`的计算依赖于多个外部输入（如环境变量、文件内容、用户模式等），未在切片... |
| 976 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 7029 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区`command`追加内容，而`command`的大小`len`是根据多个变量（如`tempname`长度、模式字符串长度等）动态计算的，但追加的`tempname`和模式字符... |
| 977 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 7335 | FP | TP | 切片代码中，`STRCPY(p, (*file)[i]);` 宏展开为 `strcpy`，目标缓冲区 `p` 的大小为 `STRLEN((*file)[i]) + 1 + dir`，而源字符串 `(*file)[i]` 来自外部文件内... |
| 978 | vim-9.1.1040 | mch_FullName | cpp/unbounded-write | 2819 | FP | TP | 代码在调用STRCAT（即strcat）前，仅检查了目标缓冲区buf和源字符串fname的总长度是否小于len，但未检查buf的剩余空间是否足以容纳fname。strcat要求目标缓冲区有足够空间，否则会导致缓冲区溢出。切片中未见任何... |
| 979 | vim-9.1.1040 | qf_store_title | cpp/unbounded-write | 1934 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的title字符串复制到新分配的内存中，虽然分配的大小为STRLEN(title)+2，但strcpy本身不检查目标缓冲区大小，若title在分配后被修改或存在并发问题，仍可能导致溢出。... |
| 980 | vim-9.1.1040 | reg_submatch | cpp/unbounded-write | 2723 | FP | TP | 切片代码中 STRCPY 宏直接展开为 strcpy，且目标缓冲区 retval 的大小 len 是根据匹配的文本位置动态计算的，但 strcpy 调用时未检查目标缓冲区是否足以容纳源字符串 s，存在缓冲区溢出风险。 |
| 981 | vim-9.1.1040 | reg_submatch | cpp/unbounded-write | 2732 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区retval的大小len由动态计算得出，而源字符串s来自reg_getline_submatch，其长度可能超过len，存在缓冲区溢出风险。切片内未见对源字符串长度的前置校... |
| 982 | vim-9.1.1040 | regtilde | cpp/unbounded-write | 1959 | FP | TP | 切片代码中，STRCPY宏展开为strcpy，目标缓冲区tmpsub的大小为tmpsublen+1，源字符串postfix的长度未经验证，存在缓冲区溢出的可能性。虽然前面有tmpsublen > MAXCOL的检查，但未对postfi... |
| 983 | vim-9.1.1040 | match_with_backref | cpp/unbounded-write | 1600 | FP | TP | 切片代码中，STRCPY宏展开为strcpy，目标缓冲区reg_tofree的大小为len（由STRLEN(rex.line)计算并加50），但源字符串rex.line的长度可能超过len，导致缓冲区溢出。代码中未见对源字符串长度进行... |
| 984 | vim-9.1.1040 | get_reg_contents | cpp/unbounded-write | 2733 | FP | TP | 代码使用STRCPY（即strcpy）将y_current->y_array[i].string复制到目标缓冲区，未检查源字符串长度是否超过目标缓冲区剩余空间。目标缓冲区retval的大小由alloc(len+1)分配，但STRCPY... |
| 985 | vim-9.1.1040 | do_put | cpp/unbounded-write | 2159 | FP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将y_array[y_size - 1].string复制到缓冲区newp，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 986 | vim-9.1.1040 | do_put | cpp/unbounded-write | 2160 | FP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将y_array[i].string等源字符串复制到固定大小的缓冲区newp中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 987 | vim-9.1.1040 | op_yank | cpp/unbounded-write | 1315 | FP | TP | 代码使用STRCPY宏（即strcpy）拼接两个字符串，目标缓冲区pnew的大小是两段字符串长度之和加1，但strcpy不检查边界，若源字符串未以空字符结尾或长度计算有误，可能导致缓冲区溢出。切片中未见对源字符串长度或内容的边界检查。 |
| 988 | vim-9.1.1040 | op_yank | cpp/unbounded-write | 1316 | FP | TP | 代码使用STRCPY宏（即strcpy）拼接两个字符串，目标缓冲区pnew的大小是两者长度之和加1，但strcpy不检查边界，若源字符串长度计算错误或未以空字符结尾，可能导致缓冲区溢出。切片中未见对源字符串长度或内容的边界检查。 |
| 989 | vim-9.1.1040 | stuff_yank | cpp/unbounded-write | 470 | FP | TP | 代码使用STRCPY（即strcpy）将pp->string复制到新分配的缓冲区tmp，但tmp的大小tmplen+1是基于pp->length + plen + 1计算的，而STRCPY的目标缓冲区tmp的大小是tmplen+1，源... |
| 990 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2838 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区scriptname追加内容，该缓冲区大小仅基于输入字符串name的长度计算，未考虑已存在的'autoload/'前缀长度，存在缓冲区溢出的风险。 |
| 991 | vim-9.1.1040 | ExpandPackAddDir | cpp/unbounded-write | 1309 | FP | TP | sprintf 使用未经验证的用户输入 `pat` 构造目标字符串，目标缓冲区 `s` 的大小为 `pat_len + 26`，而格式化字符串 `"pack/*/opt/%s*"` 的长度加上 `pat` 的长度可能超过该缓冲区大小，... |
| 992 | vim-9.1.1040 | sign_jump | cpp/unbounded-write | 1313 | FP | TP | sprintf 使用未受控的缓冲区名称和行号构造命令字符串，目标缓冲区大小仅基于文件名长度计算，未考虑格式化后字符串的总长度，存在缓冲区溢出风险。 |
| 993 | vim-9.1.1040 | dump_word | cpp/unbounded-write | 4187 | FP | TP | 代码使用STRCPY宏（即strcpy）将变量p复制到固定大小的数组badword中，而p可能指向用户输入或外部数据（如cword或word），切片中未见对p长度的校验，存在缓冲区溢出风险。 |
| 994 | vim-9.1.1040 | make_case_word | cpp/unbounded-write | 3140 | FP | TP | 代码直接使用不安全的STRCPY（即strcpy）宏复制字符串，未检查目标缓冲区cword的大小，且切片中未显示对源字符串fword的长度有任何限制或验证，存在缓冲区溢出的风险。 |
| 995 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2998 | FP | TP | 代码使用STRCPY宏（即strcpy）将repl_to复制到新分配的缓冲区p中，未检查repl_to的长度是否超过目标缓冲区剩余空间，存在缓冲区溢出风险。切片中未见任何长度校验或安全防护。 |
| 996 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2999 | FP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p中，但p的大小是基于ml_get_curline_len() + addlen + 1分配的，而addlen可能为负数（当repl_to_len < repl_fro... |
| 997 | vim-9.1.1040 | count_common_word | cpp/unbounded-write | 1919 | FP | TP | 代码使用STRCPY（即strcpy）将未知长度的字符串p复制到固定大小的缓冲区wc->wc_word中，而p可能来自未经验证的外部输入（如环境变量、文件读取等），存在缓冲区溢出风险。切片中未见对p长度的检查或使用安全复制函数。 |
| 998 | vim-9.1.1040 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY宏（即strcpy）将参数lang直接复制到固定大小的数组sl.sl_lang中，切片中未见对lang长度的校验或限制，存在缓冲区溢出风险。 |
| 1003 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2464 | FP | TP | 代码使用STRCPY宏（即strcpy）将items[1]复制到缓冲区p，而items[1]来自外部文件行，其长度可能超过p的分配大小（STRLEN(items[1]) + 2），存在缓冲区溢出风险。切片中未见对items[1]长度的校验。 |
| 1005 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2644 | FP | TP | 切片代码中，`STRCPY(p, spin->si_info);` 和 `STRCAT(p, items[0]);` 等宏展开为 `strcpy` 和 `strcat`，它们的目标缓冲区 `p` 是通过 `getroom` 分配的内存... |
| 1006 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2746 | FP | TP | 切片代码中第2746行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，未检查长度，可能导致缓冲区溢出。 |
| 1007 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2748 | FP | TP | 切片代码中第2748行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，长度未经验证，可能导致缓冲区溢出。 |
| 1009 | vim-9.1.1040 | suggest_try_change | cpp/unbounded-write | 1199 | FP | TP | 代码使用STRCPY宏（即strcpy）将su->su_fbadword复制到固定大小的缓冲区fword中，未检查源字符串长度是否超过目标缓冲区大小MAXWLEN，存在缓冲区溢出风险。 |
| 1011 | vim-9.1.1040 | concat_str | cpp/unbounded-write | 813 | FP | TP | 函数使用STRCPY（即strcpy）进行字符串复制，其目标缓冲区dest的大小由alloc分配，但分配大小基于STRLEN（即strlen）计算输入字符串的长度。若str1或str2不是以空字符结尾的字符串，STRLEN将导致未定义... |
| 1012 | vim-9.1.1040 | expand_tag_fname | cpp/unbounded-write | 4125 | FP | TP | 代码使用不安全的STRCPY（即strcpy）宏将tag_fname复制到固定大小的缓冲区retval中，未检查源字符串长度是否超过目标缓冲区大小MAXPATHL，存在缓冲区溢出风险。 |
| 1013 | vim-9.1.1040 | findtags_add_match | cpp/unbounded-write | 2623 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区中，且未见对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 1014 | vim-9.1.1040 | findtags_add_match | cpp/unbounded-write | 2702 | FP | TP | 切片代码中多次使用STRCPY（即strcpy）宏，将长度未知的源字符串（如st->tag_fname、st->ebuf、st->lbuf）复制到固定大小的缓冲区，未进行边界检查，存在缓冲区溢出风险。 |
| 1016 | vim-9.1.1040 | current_tagblock | cpp/unbounded-write | 1386 | FP | TP | sprintf使用未限制长度的用户输入（p和len）作为格式化字符串的一部分，目标缓冲区spat和epat的大小仅基于len计算，未考虑格式化字符串本身的固定长度，存在缓冲区溢出风险。 |
| 1017 | vim-9.1.1040 | uc_check_code | cpp/unbounded-write | 1782 | FP | TP | 切片代码中多次使用STRCPY（即strcpy）将外部输入（如eap->arg）复制到缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1018 | vim-9.1.1040 | get_scriptlocal_funcname | cpp/unbounded-write | 4705 | FP | TP | 代码使用STRCAT宏（即strcat）将未知长度的字符串拼接到固定大小的缓冲区newname中，newname的大小仅根据sid_buf和p+off的长度计算分配，但未检查拼接后的总长度是否超过分配的内存，存在缓冲区溢出的风险。 |
| 1019 | vim-9.1.1040 | trans_function_name_ext | cpp/unbounded-write | 4618 | FP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将sid_buf内容复制到目标缓冲区，而sid_buf的大小为20字节，但复制源sid_buf可能包含格式化后的字符串，若长度超过目标缓冲区剩余空间则会导致缓冲区溢出。切片内未见对目标... |
| 1020 | vim-9.1.1040 | fname_trans_sid | cpp/unbounded-write | 2212 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区fname_buf的大小FLEN_FIXED未知，虽然存在长度检查`i + STRLEN(name + llen) < FLEN_FIXED`，但未明确FLEN_FIXED... |
| 1021 | vim-9.1.1040 | fname_trans_sid | cpp/unbounded-write | 2224 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区fname的大小由alloc(i + STRLEN(name + llen) + 1)动态分配，但源字符串name + llen来自外部输入，其长度未在切片内进行验证或限制... |
| 1022 | vim-9.1.1040 | set_ufunc_name | cpp/unbounded-write | 664 | FP | TP | 代码使用不安全的strcpy函数将外部输入（name）复制到固定大小的缓冲区（fp->uf_name），未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何长度校验或安全复制机制。 |
| 1024 | vim-9.1.1040 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到固定大小的缓冲区`funcname`中，而`funcname`的大小仅为`STRLEN(name) + 3`，未对源字符串长度进行限制，存在缓冲区溢出风险。切片中未见任... |
| 1025 | vim-9.1.1040 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | TP | 代码使用STRCPY（即strcpy）将变量`name`复制到新分配的内存`newsav->sav_key`中，而`name`是函数参数，其来源在切片中未经验证或限制长度，存在缓冲区溢出风险。 |
| 1026 | vim-9.1.1040 | find_exported | cpp/unbounded-write | 756 | FP | TP | 代码使用`sprintf`将外部输入（如环境变量、文件读取内容）直接写入固定大小的缓冲区，未对输入长度进行限制，存在缓冲区溢出风险。切片中未见对输入长度的前置校验或使用安全函数（如`snprintf`）进行防护。 |
| 1027 | vim-9.1.1040 | find_exported | cpp/unbounded-write | 763 | FP | TP | 代码使用sprintf将外部提供的脚本ID和名称格式化到缓冲区，缓冲区大小基于对名称长度的计算动态分配，但sprintf本身不检查边界，若计算的长度len小于实际所需，则会导致缓冲区溢出。切片中未见对格式化后字符串长度的边界检查。 |
| 1028 | vim-9.1.1040 | xxdline | cpp/unbounded-write | 537 | FP | TP | 代码使用strcpy将外部输入'l'复制到固定大小的缓冲区'z'，未检查'l'的长度，存在缓冲区溢出风险。切片中未见对'l'的长度进行验证或使用安全函数的防护措施。 |
| 1035 | vim-9.1.1330 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数getcell在越界或缓冲区为空时返回NULL，但调用者vterm_screen_is_eol未检查返回值，直接解引用cell->chars，可能导致空指针解引用。切片中未见任何防护机制。 |
| 1037 | vim-9.1.1330 | get_isolated_shell_name | cpp/inconsistent-null-check | 2721 | FP | TP | 函数`vim_strnsave`可能返回NULL，但调用后未检查返回值，直接赋值给指针`p`并在函数末尾返回，存在空指针解引用风险。切片中未见任何针对该返回值的空值检查或防护机制。 |
| 1054 | vim-9.1.1330 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 "%6ld" 写入一个长整数，在最坏情况下（如 lnum 为负数）需要至少 7 个字符（包括符号和空格填充），加上字符串终止符 '\0' 共 8 字节，但目标缓冲区 tbuf 仅 20 字节，足够容纳。... |
| 1055 | vim-9.1.1330 | highlight_color | cpp/overrunning-write | 3275 | FP | TP | sprintf 目标缓冲区 'buf' 大小为10字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少10字节，当三个颜色分量均为最大值（0xff）时，生成的字符串 "#ffffffff" 恰好为9个字符加上终止符... |
| 1056 | vim-9.1.1330 | msg_outnum | cpp/overrunning-write | 1653 | FP | TP | 目标缓冲区`buf`大小为20字节，但`sprintf`写入长整数`n`时，当`n`为负10位数（如-1000000000）时，格式化字符串'%ld'将产生21字节（包括负号和终止空字符），导致缓冲区溢出。切片中未见任何对`n`的范围... |
| 1057 | vim-9.1.1330 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 的目标缓冲区 'reply' 大小为 32 字节，但格式化字符串 "%d %ld\n" 在极端情况下（如 cmdno 为多位数，result 为长整型最小值）可能超过 32 字节，导致缓冲区溢出。切片代码中未见任何长度... |
| 1058 | vim-9.1.1330 | ga_concat_strings | cpp/unbounded-write | 788 | FP | TP | 代码使用STRCPY（即strcpy）将未知长度的字符串复制到固定大小的缓冲区中，且切片内未见对源字符串长度的检查或目标缓冲区大小的验证，存在缓冲区溢出风险。 |
| 1060 | vim-9.1.1330 | buf_write | cpp/unbounded-write | 1208 | FP | TP | 代码中使用STRCPY宏（即strcpy）将fname复制到IObuff缓冲区，但未检查fname长度是否超过IObuff大小，存在缓冲区溢出风险。切片中未见对源字符串长度的限制或验证。 |
| 1063 | vim-9.1.1330 | transstr | cpp/unbounded-write | 400 | FP | TP | 切片代码显示，`res` 缓冲区的大小由 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 分配，但后续循环中多次使用 `STRCAT(res, transchar_byte(*p++))`... |
| 1065 | vim-9.1.1330 | win_redr_status_matches | cpp/unbounded-write | 663 | FP | TP | 代码使用STRCPY（即strcpy）宏将可变长度字符串复制到固定大小的缓冲区buf中，而buf的大小基于Columns计算，但源字符串s（来自matches数组）的长度未经验证，存在缓冲区溢出的风险。 |
| 1066 | vim-9.1.1330 | win_redr_status_matches | cpp/unbounded-write | 682 | FP | TP | 切片代码中，STRCPY宏被用于将transchar_byte(*s)的结果复制到buf+len指向的缓冲区，而buf的大小分配基于Columns，但transchar_byte返回的字符串长度未经验证，可能导致缓冲区溢出。 |
| 1067 | vim-9.1.1330 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码使用STRCPY宏（即strcpy）将fname复制到新分配的缓冲区name中，未检查源字符串长度是否超过目标缓冲区大小。name的分配大小基于STRLEN(fname) + 3，但STRCPY的目标地址是name + 5，存在缓... |
| 1068 | vim-9.1.1330 | has_profiling | cpp/unbounded-write | 973 | FP | TP | 代码使用STRCPY宏（即strcpy）将fname复制到新分配的缓冲区pe->pen_name，而fname是外部传入的字符串参数，其长度未在切片内进行验证。虽然缓冲区大小通过STRLEN(fname)+1计算后分配，但strcpy... |
| 1070 | vim-9.1.1330 | do_string_sub | cpp/unbounded-write | 8014 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，将tail指向的字符串复制到ga.ga_data缓冲区中，但未检查目标缓冲区剩余空间是否足够容纳tail字符串，存在缓冲区溢出风险。 |
| 1071 | vim-9.1.1330 | set_var_const | cpp/unbounded-write | 4271 | FP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname长度未经验证，可能导致目标缓冲区溢出。切片中未见对varname长度的检查或使用安全函数。 |
| 1072 | vim-9.1.1330 | cat_prefix_varname | cpp/unbounded-write | 2576 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到缓冲区`varnamebuf + 2`，虽然缓冲区大小`varnamebuflen`根据`STRLEN(name) + 3`动态分配，但分配后未检查`name`是否在分... |
| 1076 | vim-9.1.1330 | ex_sort | cpp/unbounded-write | 605 | FP | TP | 代码使用STRCPY宏（即strcpy）将未知长度的字符串`s`复制到固定大小的缓冲区`sortbuf1`中，而`sortbuf1`的大小基于之前计算的最大行长度`maxlen`分配。如果后续行的长度超过之前记录的`maxlen`，将... |
| 1077 | vim-9.1.1330 | expand_sfile | cpp/unbounded-write | 10101 | FP | TP | 代码使用STRCPY（即strcpy）将可变长度的字符串repl复制到固定大小的缓冲区newres中，而newres的大小仅通过resultlen + 1分配，未检查repllen是否超过目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 1078 | vim-9.1.1330 | repl_cmdline | cpp/unbounded-write | 5311 | FP | TP | 代码使用不安全的STRCPY（即strcpy）宏向固定大小的缓冲区new_cmdline写入数据，而目标缓冲区的大小'i'是基于多个字符串长度计算得来，但写入的源字符串'src + srclen'和'eap->nextcmd'长度未在... |
| 1079 | vim-9.1.1330 | repl_cmdline | cpp/unbounded-write | 5317 | FP | TP | 代码使用STRCPY（即strcpy）将eap->nextcmd复制到缓冲区new_cmdline中，而eap->nextcmd是外部输入，其长度未在切片内进行验证。目标缓冲区new_cmdline的大小i虽经计算，但计算过程未考虑e... |
| 1080 | vim-9.1.1330 | replace_makeprg | cpp/unbounded-write | 5018 | FP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串p复制到固定大小的缓冲区ptr中，而p来自用户输入或外部数据，切片中未见长度检查或边界防护，存在缓冲区溢出风险。 |
| 1081 | vim-9.1.1330 | replace_makeprg | cpp/unbounded-write | 5033 | FP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串（如程序变量和参数）复制到固定大小的缓冲区，存在缓冲区溢出的风险。切片中未见对源字符串长度的检查或使用安全函数。 |
| 1082 | vim-9.1.1330 | do_one_cmd | cpp/unbounded-write | 2678 | FP | TP | 切片代码中直接使用了不安全的 STRCPY 宏（即 strcpy），将未知长度的字符串（如错误消息）复制到固定大小的 IObuff 缓冲区，存在缓冲区溢出风险，且未见对目标缓冲区大小的检查或限制。 |
| 1084 | vim-9.1.1330 | get_exception_string | cpp/unbounded-write | 473 | FP | TP | 切片代码显示，`val` 缓冲区的大小由 `vim_strnsave` 分配，其大小计算依赖于 `mesg` 的长度，但在循环中 `STRCAT(val, mesg)` 或 `STRCAT(val, p)` 被多次调用，且 `mesg... |
| 1085 | vim-9.1.1330 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 切片代码中，sprintf 的目标缓冲区 `val` 的大小由 `vim_strnsave` 分配，其长度计算涉及 `STRLEN(p)` 和 `STRLEN(mesg)`，但 `p` 是 `mesg` 的子字符串指针，其长度未经验证... |
| 1086 | vim-9.1.1330 | escape_fname | cpp/unbounded-write | 4116 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串(*pp)复制到目标缓冲区(p+1)，目标缓冲区大小仅为源字符串长度加2（alloc(STRLEN(*pp) + 2)），但复制时目标起始位置为p+1，未考虑源字符串末尾的'\0'，可能... |
| 1087 | vim-9.1.1330 | cmdline_browse_history | cpp/unbounded-write | 1498 | FP | TP | 切片代码显示 STRCPY 宏直接调用了 strcpy，将源字符串 p 复制到目标缓冲区 ccline.cmdbuff，而目标缓冲区的大小由 alloc_cmdbuff 分配，但未在切片中看到对源字符串长度 plen 与目标缓冲区大小... |
| 1088 | vim-9.1.1330 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 860 | FP | TP | 代码使用STRCPY（即strcpy）将动态获取的表达式结果字符串p复制到固定大小的缓冲区ccline.cmdbuff中，虽然之前调用了realloc_cmdbuff(len + 1)来确保缓冲区大小足够，但该函数仅当len小于当前缓... |
| 1089 | vim-9.1.1330 | vim_settempdir | cpp/unbounded-write | 5289 | FP | TP | 切片代码显示，当vim_FullName调用失败时，STRCPY宏（即strcpy）被直接用于将未知长度的tempdir复制到固定大小的buf中，而buf的大小为MAXPATHL+2。由于tempdir是外部输入且未在切片内进行长度校... |
| 1091 | vim-9.1.1330 | buf_modname | cpp/unbounded-write | 3639 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的fname复制到新分配的缓冲区retval，未对源字符串长度进行校验，而目标缓冲区大小仅基于fnamelen + extlen + 3分配，若fname长度超过分配大小或未以空字符结尾... |
| 1092 | vim-9.1.1330 | addfile | cpp/unbounded-write | 4219 | FP | TP | 代码使用STRCPY（即strcpy）将参数f复制到新分配的内存p中，虽然p的大小根据f的长度（STRLEN(f) + 1 + isdir）分配，但f是函数参数，其来源在切片中未显示任何验证或边界检查，因此存在缓冲区溢出的潜在风险。 |
| 1095 | vim-9.1.1330 | uniquefy_paths | cpp/unbounded-write | 2569 | FP | TP | 代码使用STRCPY（即strcpy）将用户提供的`pattern`字符串复制到新分配的缓冲区`file_pattern`中，目标缓冲区大小仅比源字符串长度多2，若`pattern`长度接近或等于缓冲区大小，strcpy可能因未检查边... |
| 1096 | vim-9.1.1330 | find_file_in_path_option | cpp/unbounded-write | 1912 | FP | TP | 代码使用STRCPY宏（即strcpy）将外部输入（*file_to_find）复制到固定大小的缓冲区NameBuff（大小为MAXPATHL），未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 1097 | vim-9.1.1330 | ff_check_visited | cpp/unbounded-write | 1537 | FP | TP | 代码使用STRCPY（即strcpy）将ff_expand_buffer.string复制到vp->ffv_fname，而目标缓冲区vp->ffv_fname的大小为ff_expand_buffer.length + 1，但源字符串f... |
| 1098 | vim-9.1.1330 | <global> | cpp/unbounded-write | 3794 | FP | TP | 代码使用strcat将未经验证长度的字符串`s`追加到缓冲区`r`中，而`r`的分配大小计算包含了`s`的长度，但`s`来自文件内容且后续可能被`foldtext_cleanup`修改，存在缓冲区溢出风险。 |
| 1099 | vim-9.1.1330 | foldDelMarker | cpp/unbounded-write | 1897 | FP | TP | 代码使用STRCPY宏（即strcpy）将源字符串复制到目标缓冲区，目标缓冲区大小由`ml_get_len(lnum) - len + 1`计算，但未检查源字符串`p + len`的长度是否小于该缓冲区大小，存在缓冲区溢出的风险。 |
| 1100 | vim-9.1.1330 | foldAddMarker | cpp/unbounded-write | 1815 | FP | TP | 代码使用STRCPY（即strcpy）宏将`line`和`cms`等字符串复制到固定大小的缓冲区`newline`中，而`newline`的大小是基于`line_len`、`markerlen`和`STRLEN(cms)`计算分配的，... |
| 1101 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2899 | FP | TP | 代码使用STRCPY宏（即strcpy）将长度未知的字符串（res_prolog->title）复制到固定大小的缓冲区（buffer[256]）中，存在缓冲区溢出的风险。切片中未见对源字符串长度的检查或限制。 |
| 1102 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2901 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer追加内容，而buffer的大小为256字节。切片中未显示对res_prolog->title和res_prolog->version的长度进行任何检查或限制，存在缓... |
| 1103 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2905 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而title来自外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 1105 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2912 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cmap->title复制到固定大小的buffer[256]中，而title的来源是外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 1106 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2914 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的源字符串（如res_cmap->title和res_cmap->version）长度在切片内未经验证，存在缓冲区溢出的风险。 |
| 1108 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2922 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer追加内容，而buffer的大小为256字节。切片中未显示对res_encoding->title和res_encoding->version的长度进行任何检查或限制... |
| 1109 | vim-9.1.1330 | prt_resource_name | cpp/unbounded-write | 1659 | FP | TP | 切片代码显示，在调用STRCPY（即strcpy）前，仅检查了源字符串长度是否大于等于MAXPATHL，但未检查目标缓冲区resource_filename的大小。若目标缓冲区小于MAXPATHL，复制较长的合法文件名仍可能导致缓冲区溢出。 |
| 1113 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 1112 | FP | TP | 代码使用sprintf将动态内容(p1, fname)写入固定大小的缓冲区s，而s的大小仅根据p2-p1和fname长度计算，未考虑sprintf格式字符串本身占用的两个字符（'\t'和字符串结束符），存在缓冲区溢出风险。 |
| 1115 | vim-9.1.1330 | load_colors | cpp/unbounded-write | 606 | FP | TP | 代码使用sprintf将外部输入`name`拼接到固定大小的缓冲区`buf`中，而`buf`的大小仅通过`STRLEN(name) + 12`分配，未对`name`的长度进行限制，存在缓冲区溢出风险。 |
| 1116 | vim-9.1.1330 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | sprintf 使用用户控制的 `name` 和 `csinfo[i].ppath` 拼接字符串，目标缓冲区 `fullname` 的大小 `len` 计算正确，但 `sprintf` 本身不检查边界，存在缓冲区溢出风险。切片中未见对... |
| 1117 | vim-9.1.1330 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | TP | 代码使用`sprintf`将多个字符串拼接写入固定大小的缓冲区`buf`，缓冲区大小`amt`的计算基于`strlen`结果，虽然计算了总长度并分配了内存，但`sprintf`的格式字符串中包含额外的制表符、分号和引号等固定字符，其数... |
| 1118 | vim-9.1.1330 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | TP | 代码使用sprintf将多个字符串拼接至固定大小的缓冲区，缓冲区大小由各输入字符串长度计算得出，但计算时未考虑sprintf格式字符串中额外的转义字符和空终止符，可能导致缓冲区溢出。 |
| 1119 | vim-9.1.1330 | <global> | cpp/unbounded-write | 1456 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，未检查源字符串长度是否超过目标缓冲区大小。虽然目标缓冲区大小是根据strlen(fname)+1分配的，但strcpy本身存在缓冲区溢出的固有风险，且切片中未见任何边界检查或使用安... |
| 1120 | vim-9.1.1330 | <global> | cpp/unbounded-write | 1465 | FP | TP | 切片代码显示使用strcpy将fname复制到新分配的内存，但未检查分配的缓冲区大小是否足够。fname是外部传入的文件名，其长度可能超过目标缓冲区，导致缓冲区溢出。 |
| 1121 | vim-9.1.1330 | cs_add_common | cpp/unbounded-write | 604 | FP | TP | 代码使用sprintf拼接路径和文件名，未对目标缓冲区大小进行限制，且输入参数fname来自用户可控的环境变量，存在缓冲区溢出风险。 |
| 1123 | vim-9.1.1330 | <global> | cpp/unbounded-write | 3129 | FP | TP | 切片代码中`sprintf`直接使用未经验证的用户输入（`transchar(from)`）作为格式化字符串参数，且目标缓冲区`args->os_errbuf`的大小未知，存在缓冲区溢出风险。切片内未见对缓冲区大小或输入长度的校验。 |
| 1125 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2157 | FP | TP | 代码使用STRCPY（即strcpy）将fix_fname返回的字符串复制到新分配的缓冲区s中，虽然s的大小是根据源字符串f的长度分配的，但fix_fname函数可能返回一个更长的路径（例如，通过符号链接扩展或规范化），导致源字符串长... |
| 1126 | vim-9.1.1330 | <global> | cpp/unbounded-write | 811 | FP | TP | 代码使用STRCPY宏（即strcpy）将call_data复制到新分配的缓冲区，未检查源字符串长度是否小于目标缓冲区大小。切片中未见对call_data长度的校验或使用安全函数，存在缓冲区溢出风险。 |
| 1127 | vim-9.1.1330 | <global> | cpp/unbounded-write | 815 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将call_data复制到新分配的缓冲区，未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。切片中未见对call_data长度的前置校验。 |
| 1129 | vim-9.1.1330 | str2specialbuf | cpp/unbounded-write | 2017 | FP | TP | 切片代码中，str2specialbuf函数使用strcat前仅检查了当前拼接后的总长度是否小于len，但未检查目标缓冲区buf的原始大小，且str2special返回的字符串长度可能超过剩余缓冲区容量，存在缓冲区溢出风险。 |
| 1130 | vim-9.1.1330 | get_emsg_source | cpp/unbounded-write | 502 | FP | TP | sprintf 使用未受控的源文件名 sname 和格式字符串 p 进行格式化，虽然分配了 Buf = alloc(STRLEN(sname) + STRLEN(p))，但 sprintf 的格式字符串包含一个 %s 占位符，而分配的... |
| 1132 | vim-9.1.1330 | expand_env_esc | cpp/unbounded-write | 1647 | FP | TP | 代码使用STRCPY（即strcpy）将环境变量内容复制到目标缓冲区，虽然复制前检查了目标缓冲区长度，但该检查使用了STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen，其中dstlen是... |
| 1133 | vim-9.1.1330 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 切片代码中多次使用STRCAT宏（即strcat）将可变长度的字符串（如用户输入、环境变量、文件读取内容）拼接到固定大小的缓冲区上，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1134 | vim-9.1.1330 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf 使用未受控的 `result` 和 `cmdno` 作为输入写入固定大小的缓冲区 `reply`，而 `reply` 的大小仅基于 `result` 的长度计算，未考虑格式化字符串 `"%d %s\n"` 引入的额外字... |
| 1135 | vim-9.1.1330 | push_showcmd | cpp/unbounded-write | 1809 | FP | TP | 代码使用不安全的strcpy函数，将showcmd_buf的内容复制到old_showcmd_buf，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何边界检查或安全防护机制。 |
| 1137 | vim-9.1.1330 | op_change | cpp/unbounded-write | 2003 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将源字符串复制到新分配的目标缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何边界检查或安全防护机制。 |
| 1138 | vim-9.1.1330 | op_replace | cpp/unbounded-write | 1299 | FP | TP | 切片代码中 STRCPY 宏展开为 strcpy，目标缓冲区 newp 的大小为 oldlen + 1 + n，源字符串来自 oldp + bd.textcol + bd.textlen，其长度未在切片内进行验证，存在缓冲区溢出的风险。 |
| 1139 | vim-9.1.1330 | op_replace | cpp/unbounded-write | 1308 | FP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的目标缓冲区，未进行边界检查，存在缓冲区溢出风险。 |
| 1140 | vim-9.1.1330 | op_delete | cpp/unbounded-write | 962 | FP | TP | 切片代码中 STRCPY 宏被定义为 strcpy，且目标缓冲区 newp 的大小为 (ml_get_len(lnum) + 1 - n)，而源字符串 oldp + bd.textcol + bd.textlen 的长度未经验证，存在... |
| 1141 | vim-9.1.1330 | block_insert | cpp/unbounded-write | 743 | FP | TP | 切片代码中 STRCPY 宏展开为 strcpy，目标缓冲区 newp 的大小由 alloc 分配，其大小计算涉及多个变量，但未对源字符串 oldp 的长度进行校验，存在缓冲区溢出的风险。 |
| 1144 | vim-9.1.1330 | stropt_expand_envvar | cpp/unbounded-write | 1803 | FP | TP | 切片代码显示STRCPY宏直接展开为strcpy，目标缓冲区newval由alloc(newlen)分配，其大小newlen基于STRLEN(s)计算，但未检查s（来自option_expand）的长度是否超过newlen，存在缓冲区... |
| 1145 | vim-9.1.1330 | mch_expand_wildcards | cpp/unbounded-write | 7371 | FP | TP | 切片代码中，STRCPY宏被定义为strcpy，在多个位置（如复制文件名时）直接使用，未检查目标缓冲区大小。告警指出数据源来自外部（如环境变量、文件读取），存在缓冲区溢出风险，且切片内未见边界检查。 |
| 1146 | vim-9.1.1330 | mch_FullName | cpp/unbounded-write | 2829 | FP | TP | 切片代码中，STRCPY宏被直接展开为strcpy，且目标缓冲区大小（len）和源字符串长度（STRLEN(fname)）在调用前已进行校验，但校验条件为`(int)(buflen + STRLEN(fname)) >= len`，这... |
| 1148 | vim-9.1.1330 | reg_submatch | cpp/unbounded-write | 2723 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，将来自reg_getline_submatch的未知长度字符串复制到固定大小的缓冲区retval中，而retval的大小由alloc(len)分配，len的计算依赖于外部输入（如匹配位... |
| 1149 | vim-9.1.1330 | reg_submatch | cpp/unbounded-write | 2732 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区retval的大小len由外部输入（如匹配位置）动态计算，未在切片中看到对源字符串s长度的校验或对目标缓冲区retval的边界保护，存在缓冲区溢出的风险。 |
| 1150 | vim-9.1.1330 | regtilde | cpp/unbounded-write | 1959 | FP | TP | STRCPY宏展开为strcpy，目标缓冲区tmpsub的大小为tmpsublen+1，源字符串postfix的长度未经验证，存在缓冲区溢出的可能性。切片中未见对postfix长度的前置校验，仅通过tmpsublen > MAXCOL... |
| 1151 | vim-9.1.1330 | match_with_backref | cpp/unbounded-write | 1600 | FP | TP | 代码使用STRCPY（即strcpy）将长度未知的rex.line复制到固定大小的缓冲区reg_tofree中，而reg_tofree的大小仅基于rex.line的长度加上固定余量分配，未对源字符串长度进行边界检查，存在缓冲区溢出风险。 |
| 1152 | vim-9.1.1330 | get_reg_contents | cpp/unbounded-write | 2741 | FP | TP | 代码使用STRCPY（即strcpy）将y_current->y_array[i].string复制到目标缓冲区，未检查源字符串长度是否超过目标缓冲区剩余空间。目标缓冲区retval的大小由alloc(len + 1)分配，但STRC... |
| 1153 | vim-9.1.1330 | do_put | cpp/unbounded-write | 2164 | FP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将y_array[y_size - 1].string复制到缓冲区newp，未检查目标缓冲区大小，且源字符串长度来自外部输入（如环境变量、文件读取等），存在缓冲区溢出风险。 |
| 1154 | vim-9.1.1330 | do_put | cpp/unbounded-write | 2165 | FP | TP | 切片代码中直接使用了不安全的 STRCPY 宏（即 strcpy），将 y_array[i].string 复制到固定大小的缓冲区 newp 中，而源字符串长度未经验证，存在缓冲区溢出风险。 |
| 1155 | vim-9.1.1330 | op_yank | cpp/unbounded-write | 1317 | FP | TP | 代码使用STRCPY宏（即strcpy）拼接两个字符串，目标缓冲区大小由两个源字符串长度之和加1计算得出，但未考虑strcpy在复制第二个字符串时可能因源字符串未以空字符结尾而越界读取，导致缓冲区溢出风险。切片中未见对源字符串内容或长... |
| 1156 | vim-9.1.1330 | op_yank | cpp/unbounded-write | 1318 | FP | TP | 代码使用STRCPY宏（即strcpy）进行字符串拼接，目标缓冲区大小由alloc分配，其大小基于两个源字符串长度的和。切片中未显示对源字符串长度进行任何验证或限制，存在缓冲区溢出的风险。 |
| 1157 | vim-9.1.1330 | stuff_yank | cpp/unbounded-write | 470 | FP | TP | 代码使用STRCPY（即strcpy）宏将源字符串复制到目标缓冲区，目标缓冲区大小由tmplen+1分配，但源字符串pp->string的长度未知，可能超过分配的大小，存在缓冲区溢出风险。切片中未见对源字符串长度的校验。 |
| 1158 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2838 | FP | TP | 代码使用`strcat`拼接字符串，目标缓冲区`scriptname`的大小仅根据输入`name`的长度分配，未考虑已拷贝的固定前缀"autoload/"的长度，存在缓冲区溢出的风险。 |
| 1159 | vim-9.1.1330 | ExpandPackAddDir | cpp/unbounded-write | 1309 | FP | TP | sprintf 使用未经验证的用户输入 `pat` 构造目标字符串，目标缓冲区 `s` 的大小为 `pat_len + 26`，但格式化字符串 `"pack/*/opt/%s*"` 的长度加上 `pat` 的长度可能超过该缓冲区大小，... |
| 1160 | vim-9.1.1330 | sign_jump | cpp/unbounded-write | 1313 | FP | TP | sprintf 使用未限制长度的缓冲区 buf->b_fname 作为输入，而该缓冲区内容来自外部文件路径，可能导致目标缓冲区 cmd 溢出，切片中未见对 buf->b_fname 长度的前置校验。 |
| 1161 | vim-9.1.1330 | dump_word | cpp/unbounded-write | 4187 | FP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或外部数据（如word或cword），且切片中未见对p长度的前置校验，存在缓冲区溢出风险。 |
| 1163 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2998 | FP | TP | 代码使用STRCPY宏（即strcpy）将repl_to复制到新分配的缓冲区p中，未检查目标缓冲区大小，且repl_to是外部输入（来自全局变量），存在缓冲区溢出风险。切片中未见对repl_to长度的验证或使用安全复制函数。 |
| 1164 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2999 | FP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p，但p的大小是基于ml_get_curline_len() + addlen + 1分配的，而addlen可能为负数（当repl_to_len < repl_from... |
| 1165 | vim-9.1.1330 | count_common_word | cpp/unbounded-write | 1919 | FP | TP | 代码使用STRCPY宏（即strcpy）将未知长度的字符串p复制到新分配的内存wc->wc_word中，而分配的大小基于STRLEN(p) + 1，这确保了目标缓冲区足够大，不会溢出。然而，告警指出strcpy的输入可能来自多个外部源... |
| 1166 | vim-9.1.1330 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的`lang`参数复制到固定大小的结构体成员`sl.sl_lang`中，切片中未见对`lang`长度的校验或限制，存在缓冲区溢出风险。 |
| 1171 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2464 | FP | TP | 代码中使用STRCPY宏（即strcpy）将items[1]复制到缓冲区p，而p的大小仅为STRLEN(items[1]) + 2，但items[1]来自外部文件行，其长度可能超过p的分配大小，导致缓冲区溢出。切片中未见对items[... |
| 1174 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2746 | FP | TP | 切片代码中第2746行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，未检查长度，可能导致缓冲区溢出。 |
| 1175 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2748 | FP | TP | 切片代码中第2748行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，未检查长度，可能导致缓冲区溢出。 |
| 1181 | vim-9.1.1330 | get_tagfname | cpp/unbounded-write | 3435 | FP | TP | 代码在行'STRCPY(buf, fname);'处使用strcpy宏，将fname复制到buf中，而fname来自vim_findfile函数，其长度可能超过buf的大小（MAXPATHL）。切片中未见对fname长度的检查或限制，... |
| 1182 | vim-9.1.1330 | findtags_add_match | cpp/unbounded-write | 2624 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区中，且未在切片内看到对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 1183 | vim-9.1.1330 | findtags_add_match | cpp/unbounded-write | 2703 | FP | TP | 切片代码中多次使用STRCPY（即strcpy）宏，将来源如st->tag_fname、st->ebuf、st->lbuf等字符串复制到固定大小的缓冲区mfp中，而mfp的大小通过alloc分配，但未检查源字符串长度是否超过目标缓冲区... |
| 1185 | vim-9.1.1330 | current_tagblock | cpp/unbounded-write | 1392 | FP | TP | sprintf使用未限制长度的用户输入（p）作为格式化字符串的一部分，且目标缓冲区（spat/epat）的大小仅基于len计算，未考虑格式化字符串本身的额外长度，存在缓冲区溢出风险。 |
| 1186 | vim-9.1.1330 | uc_check_code | cpp/unbounded-write | 1782 | FP | TP | 切片代码中直接使用STRCPY（即strcpy）将外部输入（如eap->arg）复制到缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1188 | vim-9.1.1330 | alloc_ufunc | cpp/unbounded-write | 728 | FP | TP | 代码使用不安全的strcpy函数，将外部传入的name字符串复制到固定大小的缓冲区fp->uf_name中，且切片中未见对namelen与目标缓冲区大小的边界检查，存在缓冲区溢出风险。 |
| 1190 | vim-9.1.1330 | generate_PUSHFUNC | cpp/unbounded-write | 1041 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到固定大小的缓冲区`funcname`中，而`funcname`的大小仅为`STRLEN(name) + 3`，未对源字符串长度进行限制，存在缓冲区溢出风险。 |
| 1191 | vim-9.1.1330 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | TP | 代码使用STRCPY（即strcpy）将变量name复制到newsav->sav_key，目标缓冲区大小仅为STRLEN(name)+1，与源长度相同，没有额外空间，若name未以空字符结尾或计算有误，可能导致缓冲区溢出。切片中未见对... |
| 1192 | vim-9.1.1330 | find_exported | cpp/unbounded-write | 756 | FP | TP | 代码使用sprintf将外部可控的`script->sn_autoload_prefix`和`name`拼接到固定大小的缓冲区`buffer`或动态分配的`funcname`中，但动态分配的大小`len`仅基于这两个字符串的长度计算，... |
| 1193 | vim-9.1.1330 | find_exported | cpp/unbounded-write | 763 | FP | TP | sprintf 使用外部输入的 name 和 sid 拼接字符串，目标缓冲区 funcname 的大小由 len 计算决定，但 len 的计算可能超过缓冲区大小，且切片中未见对最终拼接字符串长度的边界检查，存在缓冲区溢出风险。 |
| 1194 | vim-9.1.1330 | xxdline | cpp/unbounded-write | 537 | FP | TP | 代码使用strcpy将外部输入'l'复制到固定大小的缓冲区'z'，未检查输入长度，存在缓冲区溢出风险。切片中未见对'l'长度的前置校验或使用安全函数。 |
| 1201 | vim-9.1.0790 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数getcell在越界或buffer为空时返回NULL，但调用者vterm_screen_is_eol未检查返回值，直接解引用cell->chars，存在空指针解引用风险。 |
| 1221 | vim-9.1.0790 | do_put | cpp/unsafe-strcat | 2095 | FP | TP | 切片代码中直接使用了不安全的STRCAT宏（即strcat），将y_array[y_size - 1]的内容追加到newp缓冲区，未检查目标缓冲区newp的大小是否足以容纳源字符串，存在缓冲区溢出的风险。 |
| 1223 | vim-9.1.0790 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 "%6ld" 写入最多6位数字加符号和终止符，可能超过20字节的目标缓冲区 tbuf，存在缓冲区溢出风险。切片中未见对 lnum 值的范围校验或使用更安全的函数。 |
| 1224 | vim-9.1.0790 | highlight_color | cpp/overrunning-write | 3254 | FP | TP | sprintf 目标缓冲区 'buf' 大小为10字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少10字节，当RGB值均为两位数时恰好填满，但若值小于16（如0x0f）则格式化为一位数，导致字符串长度变为8字节... |
| 1225 | vim-9.1.0790 | msg_outnum | cpp/overrunning-write | 1555 | FP | TP | sprintf 的目标缓冲区 buf 大小为 20 字节，但格式化长整型数 '%ld' 最多可能需要 21 字节（包括负号和终止符），存在缓冲区溢出的风险。 |
| 1226 | vim-9.1.0790 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf函数将格式化的字符串写入大小为32字节的固定缓冲区reply，当cmdno和result的值组合超过31个字符（加上空终止符）时，会发生缓冲区溢出。切片代码中未见任何对输入值的范围校验或使用更安全的函数（如snprint... |
| 1227 | vim-9.1.0790 | ga_concat_strings | cpp/unbounded-write | 788 | FP | TP | 代码使用STRCPY（即strcpy）将未知长度的字符串复制到固定大小的缓冲区中，且切片内未见对源字符串长度的校验或对目标缓冲区边界的防护，存在缓冲区溢出风险。 |
| 1228 | vim-9.1.0790 | maketitle | cpp/unbounded-write | 4145 | FP | TP | 代码使用STRCPY（即strcpy）将指针p的内容复制到icon_str缓冲区，而p指向的文件名长度可能超过目标缓冲区大小（IOSIZE），且切片中未见对源字符串长度的限制或检查，存在缓冲区溢出风险。 |
| 1229 | vim-9.1.0790 | buf_write | cpp/unbounded-write | 1208 | FP | TP | 代码使用STRCPY（即strcpy）将fname复制到固定大小的IObuff缓冲区，未检查fname长度是否超过IObuff大小，存在缓冲区溢出风险。切片中未见对fname长度的前置校验。 |
| 1232 | vim-9.1.0790 | transstr | cpp/unbounded-write | 366 | FP | TP | 切片代码显示，`res` 缓冲区的大小由 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 分配，但后续循环中多次使用 `STRCAT`（即 `strcat`）向其追加内容。`strcat`... |
| 1234 | vim-9.1.0790 | win_redr_status_matches | cpp/unbounded-write | 639 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将可变长度字符串复制到固定大小的缓冲区buf中，而buf的大小基于Columns计算，但源字符串长度未经验证，存在缓冲区溢出风险。 |
| 1236 | vim-9.1.0790 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码使用STRCPY（即strcpy）将fname复制到新分配的缓冲区name中，未检查fname的长度是否超过目标缓冲区大小。虽然name的分配大小基于STRLEN(fname) + 3，但后续的STRCPY操作目标地址为name ... |
| 1237 | vim-9.1.0790 | has_profiling | cpp/unbounded-write | 973 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的源字符串fname复制到固定大小的目标缓冲区pe->pen_name，而目标缓冲区的大小仅通过STRLEN(fname)+1分配，没有对源字符串长度进行限制，存在缓冲区溢出风险。 |
| 1238 | vim-9.1.0790 | do_string_sub | cpp/unbounded-write | 7697 | FP | TP | 切片代码中，STRCPY宏被用于将`tail`字符串复制到动态数组`ga`的剩余空间中，但未检查`tail`的长度是否超过目标缓冲区`(char *)ga.ga_data + ga.ga_len`的剩余容量。虽然前面有`ga_grow... |
| 1239 | vim-9.1.0790 | make_expanded_name | cpp/unbounded-write | 6918 | FP | TP | 代码使用STRCPY（即strcpy）将eval_to_string返回的字符串复制到新分配的内存中，虽然分配的大小考虑了源字符串长度，但strcpy本身不检查目标缓冲区大小，若分配计算错误或temp_result被后续修改，仍可能导... |
| 1240 | vim-9.1.0790 | make_expanded_name | cpp/unbounded-write | 6920 | FP | TP | 代码使用`strcat`拼接字符串，目标缓冲区`retval`的大小通过`alloc`分配，其大小计算依赖于`temp_result`的长度，而`temp_result`来自`eval_to_string`函数对用户输入表达式的求值，... |
| 1241 | vim-9.1.0790 | set_var_const | cpp/unbounded-write | 4183 | FP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname长度由STRLEN(varname)计算，目标缓冲区大小仅为STRLEN(varname) + 1，但STRCPY未限制复制长度，若v... |
| 1242 | vim-9.1.0790 | cat_prefix_varname | cpp/unbounded-write | 2504 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到缓冲区`varnamebuf+2`，虽然缓冲区大小`len`根据`name`的长度计算并分配，但`len`的计算未包含空终止符，且分配后立即使用strcpy，存在缓冲区... |
| 1246 | vim-9.1.0790 | ex_sort | cpp/unbounded-write | 605 | FP | TP | 代码使用STRCPY宏（即strcpy）将ml_get返回的字符串复制到固定大小的缓冲区sortbuf1，而sortbuf1的大小基于之前计算的最大行长maxlen分配。如果后续行的长度超过之前计算的最大长度，strcpy将导致缓冲区... |
| 1247 | vim-9.1.0790 | expand_sfile | cpp/unbounded-write | 9801 | FP | TP | 代码使用STRCPY（即strcpy）将可变长度的字符串repl复制到固定大小的缓冲区newres中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何边界检查或安全防护机制。 |
| 1248 | vim-9.1.0790 | repl_cmdline | cpp/unbounded-write | 5302 | FP | TP | 代码使用STRCPY（即strcpy）复制未经验证长度的字符串（src + srclen），目标缓冲区new_cmdline的大小i虽经计算，但未确保src + srclen的长度小于剩余空间，存在缓冲区溢出风险。切片中未见对源字符串... |
| 1249 | vim-9.1.0790 | repl_cmdline | cpp/unbounded-write | 5308 | FP | TP | 切片代码中 STRCPY 宏直接展开为不安全的 strcpy 函数，目标缓冲区 new_cmdline 的大小 i 由动态计算得出，但未对源字符串 eap->nextcmd 的长度进行校验以确保其不超过目标缓冲区剩余空间，存在缓冲区溢... |
| 1250 | vim-9.1.0790 | replace_makeprg | cpp/unbounded-write | 5009 | FP | TP | 代码使用STRCPY（即strcpy）将用户控制的参数p复制到新分配的缓冲区，未检查p的长度是否超过目标缓冲区剩余空间，存在缓冲区溢出风险。切片中未见对p的长度进行验证或使用安全复制函数。 |
| 1251 | vim-9.1.0790 | replace_makeprg | cpp/unbounded-write | 5024 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区，且切片中未见对输入长度进行校验或使用安全复制函数，存在缓冲区溢出风险。 |
| 1252 | vim-9.1.0790 | do_one_cmd | cpp/unbounded-write | 2673 | FP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将未知长度的字符串复制到固定大小的IObuff缓冲区，且未见对源字符串长度的检查或限制，存在缓冲区溢出的真实风险。 |
| 1254 | vim-9.1.0790 | get_exception_string | cpp/unbounded-write | 473 | FP | TP | 切片代码中，`val`指向的缓冲区大小由`vim_strnsave`分配，其长度计算依赖于`STRLEN(mesg)`等变量，但后续`STRCAT(val, mesg)`或`STRCAT(val, p)`调用时，若`mesg`或`p`... |
| 1255 | vim-9.1.0790 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 切片代码中，sprintf 使用未经验证的字符串 mesg 作为格式化参数，该字符串来自外部输入（异常消息），且目标缓冲区 val 的大小未明确限制，存在缓冲区溢出风险。 |
| 1256 | vim-9.1.0790 | escape_fname | cpp/unbounded-write | 4109 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串(*pp)复制到目标缓冲区(p+1)，目标缓冲区大小仅为源字符串长度加2（alloc(STRLEN(*pp) + 2)），但strcpy会复制包括终止空字符在内的所有字符，这可能导致目标... |
| 1257 | vim-9.1.0790 | cmdline_browse_history | cpp/unbounded-write | 1498 | FP | TP | 代码使用STRCPY宏（即strcpy）将历史记录字符串p复制到ccline.cmdbuff，而p的长度plen可能超过alloc_cmdbuff分配的缓冲区大小，因为alloc_cmdbuff仅根据plen分配，未考虑strcpy的... |
| 1258 | vim-9.1.0790 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 864 | FP | TP | 代码使用STRCPY（即strcpy）将动态获取的字符串p复制到固定大小的缓冲区ccline.cmdbuff中，虽然之前调用了realloc_cmdbuff(len + 1)来调整缓冲区大小，但该函数仅确保缓冲区长度不小于len+1，... |
| 1259 | vim-9.1.0790 | <global> | cpp/unbounded-write | 5375 | FP | TP | sprintf 使用未限制长度的 vim_tempdir 和递增的 temp_count 拼接字符串，目标缓冲区 itmp 大小固定为 TEMPNAMELEN，存在缓冲区溢出风险。切片中未见对 vim_tempdir 长度或最终字符串... |
| 1260 | vim-9.1.0790 | vim_settempdir | cpp/unbounded-write | 5235 | FP | TP | 切片代码显示，当`vim_FullName`调用失败时，程序使用`STRCPY`（即`strcpy`）将未知长度的`tempdir`参数复制到固定大小的缓冲区`buf`中，而`buf`的大小为`MAXPATHL + 2`。由于`tem... |
| 1261 | vim-9.1.0790 | <global> | cpp/unbounded-write | 4352 | FP | TP | 代码使用`sprintf(tbuf, mesg, path)`，其中`tbuf`的大小基于`mesg`和`path`的长度计算，但`mesg`是格式化字符串，可能包含额外的格式说明符，导致缓冲区溢出。切片中未见对`mesg`内容的安全验证。 |
| 1263 | vim-9.1.0790 | buf_modname | cpp/unbounded-write | 3620 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证的外部输入fname复制到新分配的缓冲区retval，且切片中未见对fname长度的前置校验，存在缓冲区溢出风险。 |
| 1264 | vim-9.1.0790 | addfile | cpp/unbounded-write | 4198 | FP | TP | 代码使用STRCPY（即strcpy）将输入字符串f复制到新分配的内存p中，虽然p的大小根据f的长度（STRLEN(f) + 1 + isdir）分配，但strcpy本身不检查边界，若f在分配后被修改或存在并发问题，理论上可能导致溢出... |
| 1265 | vim-9.1.0790 | unix_expandpath | cpp/unbounded-write | 3833 | FP | TP | 切片代码中 STRCPY 宏直接展开为 strcpy，将路径字符串复制到缓冲区，但未检查源字符串长度是否超过目标缓冲区大小。缓冲区大小由 STRLEN(path) + MAXPATHL 计算，但源字符串 path_end + 1 的长... |
| 1269 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1718 | FP | TP | 切片代码中 STRCPY 宏直接展开为 strcpy，将外部输入（如环境变量、文件读取内容）复制到固定大小的 NameBuff 缓冲区，未检查源字符串长度是否超过目标缓冲区大小 MAXPATHL，存在缓冲区溢出风险。 |
| 1270 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1719 | FP | TP | 切片代码中 STRCPY 宏直接展开为 strcpy，将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区 NameBuff，且切片内未见对输入长度的校验或使用安全函数，存在缓冲区溢出风险。 |
| 1271 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1724 | FP | TP | 代码使用STRCPY（即strcpy）将*file_to_find复制到NameBuff，而*file_to_find可能来自用户输入的环境变量（通过expand_env_esc），且切片中未见对源字符串长度的检查或限制，存在缓冲区溢... |
| 1272 | vim-9.1.0790 | ff_check_visited | cpp/unbounded-write | 1370 | FP | TP | 切片代码显示，STRCPY宏被用于将ff_expand_buffer复制到新分配的内存vp->ffv_fname中，而STRCPY被定义为strcpy。虽然目标缓冲区大小是根据源字符串长度（STRLEN(ff_expand_buffe... |
| 1279 | vim-9.1.0790 | <global> | cpp/unbounded-write | 537 | FP | TP | 切片代码中多次使用不安全的STRCPY宏（即strcpy）将可变长度的字符串复制到固定大小的缓冲区ff_expand_buffer（大小为MAXPATHL），且未对源字符串长度进行校验，存在缓冲区溢出风险。 |
| 1280 | vim-9.1.0790 | <global> | cpp/unbounded-write | 545 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区（如ff_expand_buffer），且未在切片内看到对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 1281 | vim-9.1.0790 | <global> | cpp/unbounded-write | 548 | FP | TP | 代码使用STRCAT宏（即strcat）向ff_expand_buffer追加内容，但切片中未显示对目标缓冲区大小的检查或限制。ff_expand_buffer被分配为MAXPATHL大小，但源字符串长度可能超过剩余空间，导致缓冲区溢出。 |
| 1282 | vim-9.1.0790 | <global> | cpp/unbounded-write | 590 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区（如ff_expand_buffer），且未对源字符串长度进行验证。缓冲区大小由alloc(MAXPATHL)分配，但源字符串可能来自外部输入... |
| 1283 | vim-9.1.0790 | <global> | cpp/unbounded-write | 591 | FP | TP | 切片代码中，STRCAT宏直接使用strcat，将search_ctx->ffsc_wc_path拼接到temp缓冲区，而temp缓冲区的大小计算依赖于多个字符串长度，未在切片中看到对目标缓冲区大小的边界检查，存在缓冲区溢出的风险。 |
| 1284 | vim-9.1.0790 | <global> | cpp/unbounded-write | 3798 | FP | TP | 代码使用strcat将未经验证长度的字符串`s`拼接到缓冲区`r`中，而`r`的分配大小虽然考虑了`s`的长度，但`s`的内容来自文件行数据，可能被外部输入控制，且切片中未见对`s`长度的运行时校验以防止缓冲区溢出。 |
| 1285 | vim-9.1.0790 | foldDelMarker | cpp/unbounded-write | 1897 | FP | TP | 代码使用STRCPY宏（即strcpy）将源字符串`p + len`复制到目标缓冲区`newline + (p - line)`，目标缓冲区大小由`alloc(ml_get_len(lnum) - len + 1)`分配，但未检查源字... |
| 1286 | vim-9.1.0790 | foldAddMarker | cpp/unbounded-write | 1815 | FP | TP | 代码使用STRCPY（即strcpy）宏将line和cms等字符串复制到newline缓冲区，而newline的大小基于line_len、markerlen和STRLEN(cms)计算，未对源字符串长度进行限制，存在缓冲区溢出的风险。 |
| 1287 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2899 | FP | TP | 代码使用STRCPY宏（即strcpy）将长度未知的字符串（res_prolog->title）复制到固定大小的缓冲区（buffer[256]）中，存在缓冲区溢出的风险。切片中未见对源字符串长度的检查或限制。 |
| 1288 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2901 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer追加内容，而buffer的大小为256字节。切片中未显示对res_prolog->title和res_prolog->version的长度进行任何检查或限制，存在缓... |
| 1289 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2905 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而title的来源是外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 1293 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2920 | FP | TP | STRCPY宏展开为strcpy，将res_encoding->title复制到固定大小的buffer[256]中，切片内未见对title长度的校验，存在缓冲区溢出风险。 |
| 1294 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2922 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer追加内容，而buffer的大小为256字节。切片中未显示对res_encoding->title和res_encoding->version的长度进行任何检查或限制... |
| 1296 | vim-9.1.0790 | do_helptags | cpp/unbounded-write | 1210 | FP | TP | 代码使用STRCPY（即strcpy）将未知长度的参数`dirname`复制到固定大小的缓冲区`NameBuff`中，切片内未见对`dirname`长度的校验或使用安全函数，存在缓冲区溢出风险。 |
| 1299 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 1112 | FP | TP | 代码使用sprintf将动态生成的标签字符串(p1)和文件名(fname)写入固定大小的缓冲区(s)，其中p1和fname的长度在切片中未受限制，存在缓冲区溢出风险。 |
| 1301 | vim-9.1.0790 | load_colors | cpp/unbounded-write | 602 | FP | TP | sprintf 使用未经验证的输入 'name' 格式化字符串到固定大小的缓冲区 'buf'，缓冲区大小仅为 STRLEN(name) + 12，而格式化字符串 "colors/%s.vim" 的长度加上 name 的长度可能超过此分... |
| 1302 | vim-9.1.0790 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | sprintf 使用用户控制的 `name` 和 `csinfo[i].ppath` 拼接字符串，目标缓冲区 `fullname` 的大小 `len` 计算基于这两个字符串的长度，但未考虑格式化字符串 `"%s/%s"` 中额外的 '... |
| 1305 | vim-9.1.0790 | <global> | cpp/unbounded-write | 1456 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是函数参数，其长度未在切片内进行验证，而strcpy存在缓冲区溢出风险。切片中未见对fname长度的前置检查或使用安全函数。 |
| 1306 | vim-9.1.0790 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存，fname是外部传入的文件名参数，其长度未在切片内进行验证。虽然分配了strlen(fname)+1的空间，但strcpy本身对目标缓冲区无边界检查，若fname在调用后被修改或非预... |
| 1307 | vim-9.1.0790 | cs_add_common | cpp/unbounded-write | 604 | FP | TP | 代码使用sprintf拼接路径和文件名，未对目标缓冲区大小进行限制，且拼接的源字符串长度可能超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 1309 | vim-9.1.0790 | <global> | cpp/unbounded-write | 3119 | FP | TP | 代码使用sprintf将格式化字符串和transchar(from)的结果写入固定大小的缓冲区args->os_errbuf，未对transchar返回的字符串长度进行限制，存在缓冲区溢出风险。切片中未见对目标缓冲区大小的检查或使用安... |
| 1311 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2157 | FP | TP | 代码使用STRCPY（即strcpy）将fix_fname返回的字符串`s`复制到新分配的缓冲区`d`中，虽然`s`的大小是根据`f`的长度分配的，但`fix_fname`函数可能返回一个更长的路径（例如，通过符号链接解析或路径规范化... |
| 1312 | vim-9.1.0790 | <global> | cpp/unbounded-write | 811 | FP | TP | 代码使用STRCPY宏（即strcpy）将call_data复制到新分配的缓冲区，但分配的大小为STRLEN(call_data) + 5，而strcpy会复制整个源字符串（包括终止空字符），如果call_data长度恰好为STRLE... |
| 1313 | vim-9.1.0790 | <global> | cpp/unbounded-write | 815 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将可变长度的源字符串复制到固定大小的缓冲区中，例如在gui_add_tearoff函数中，未对源字符串长度进行校验，存在缓冲区溢出风险。 |
| 1314 | vim-9.1.0790 | msg_show_console_dialog | cpp/unbounded-write | 4387 | FP | TP | 代码使用STRCPY宏（即strcpy）将未经验证的'message'字符串复制到固定大小的缓冲区'confirm_msg'中，而'confirm_msg'的大小仅由'len'计算决定，未对源字符串长度进行显式限制，存在缓冲区溢出风险。 |
| 1316 | vim-9.1.0790 | get_emsg_source | cpp/unbounded-write | 484 | FP | TP | 代码使用sprintf格式化字符串，目标缓冲区大小通过STRLEN(sname) + STRLEN(p)计算，但sprintf的格式字符串包含占位符%s，其最终长度取决于sname的实际内容。若sname包含格式化指令（如%s），可能... |
| 1317 | vim-9.1.0790 | may_trigger_modechanged | cpp/unbounded-write | 2821 | FP | TP | 代码使用STRCPY（即strcpy）将curr_mode复制到last_mode，而last_mode的大小未知，curr_mode来自get_mode函数，其长度可能超过last_mode的缓冲区大小，存在缓冲区溢出风险。切片中未... |
| 1320 | vim-9.1.0790 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 切片代码中多次使用STRCAT宏（即strcat）将未经验证长度的字符串（如用户输入、环境变量、文件读取内容）拼接到固定大小的缓冲区（如newline），存在缓冲区溢出的风险，未见长度检查等防护机制。 |
| 1321 | vim-9.1.0790 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf 使用未受控的 `result` 参数作为格式化字符串的一部分，而 `result` 可能来自外部输入（如环境变量、网络读取等），且切片中未见对 `result` 长度进行校验或使用安全函数（如 snprintf），存在... |
| 1322 | vim-9.1.0790 | push_showcmd | cpp/unbounded-write | 1805 | FP | TP | 代码使用不安全的strcpy函数，将showcmd_buf的内容复制到old_showcmd_buf中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何边界检查或安全防护机制。 |
| 1324 | vim-9.1.0790 | op_change | cpp/unbounded-write | 1867 | FP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将源字符串复制到目标缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1325 | vim-9.1.0790 | op_replace | cpp/unbounded-write | 1163 | FP | TP | 切片代码中 STRCPY 宏被定义为 strcpy，且目标缓冲区 newp 的大小基于动态计算，但源字符串 oldp + bd.textcol + bd.textlen 的长度未经验证，存在缓冲区溢出的风险。 |
| 1326 | vim-9.1.0790 | op_replace | cpp/unbounded-write | 1172 | FP | TP | 代码使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的目标缓冲区，且切片中未见对源字符串长度的检查或对目标缓冲区边界的防护，存在缓冲区溢出风险。 |
| 1327 | vim-9.1.0790 | op_delete | cpp/unbounded-write | 826 | FP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将源字符串`oldp + bd.textcol + bd.textlen`复制到目标缓冲区`newp + bd.textcol + bd.startspaces + bd.... |
| 1328 | vim-9.1.0790 | block_insert | cpp/unbounded-write | 607 | FP | TP | 代码使用STRCPY（即strcpy）将字符串oldp复制到newp + offset位置，未检查目标缓冲区newp的大小，而newp是通过alloc分配的内存，其大小取决于ml_get_len(lnum)、spaces、slen等变... |
| 1331 | vim-9.1.0790 | stropt_expand_envvar | cpp/unbounded-write | 1800 | FP | TP | 代码使用strcpy复制字符串，目标缓冲区newval的大小由alloc(newlen)分配，而newlen的计算基于源字符串s的长度。虽然s来自option_expand，但切片中未显示对s的长度有明确的上限约束或验证，存在缓冲区溢... |
| 1332 | vim-9.1.0790 | mch_expand_wildcards | cpp/unbounded-write | 6937 | FP | TP | 代码使用strcat宏（即标准库strcat）向固定大小的缓冲区command追加内容，而缓冲区大小len的计算依赖于多个外部输入（如环境变量、shell路径、用户模式），若这些输入长度总和超过alloc(len)分配的大小，将导致缓... |
| 1333 | vim-9.1.0790 | mch_expand_wildcards | cpp/unbounded-write | 7283 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将可变长度的字符串复制到固定大小的缓冲区，且未对源字符串长度进行边界检查。例如，在构建shell命令时，直接将用户提供的模式字符串（pat[i]）拼接到command缓冲区中，存在缓冲... |
| 1334 | vim-9.1.0790 | mch_FullName | cpp/unbounded-write | 2819 | FP | TP | 切片代码显示，在调用STRCAT（即strcat）追加fname到buf之前，仅检查了总长度是否小于len，但未检查追加后是否会超出buf的原始分配大小（MAXPATHL）。由于fname可能来自外部输入（如环境变量、命令行参数等），... |
| 1335 | vim-9.1.0790 | qf_store_title | cpp/unbounded-write | 1934 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的title字符串复制到新分配的内存中，虽然分配的大小基于STRLEN(title)+2，但strcpy本身不检查目标缓冲区大小，若title不是以空字符结尾的字符串，strcpy将导致... |
| 1336 | vim-9.1.0790 | reg_submatch | cpp/unbounded-write | 2723 | FP | TP | 切片代码中，`STRCPY` 宏直接展开为不安全的 `strcpy`，且目标缓冲区 `retval` 的大小 `len` 是在循环中动态计算的，没有证据表明在调用 `strcpy` 前对源字符串长度进行了检查以确保不会溢出目标缓冲区。 |
| 1337 | vim-9.1.0790 | reg_submatch | cpp/unbounded-write | 2732 | FP | TP | 切片代码中，STRCPY宏直接展开为不安全的strcpy，将长度未知的源字符串`s`复制到固定大小的目标缓冲区`retval`中，而`retval`的大小`len`是在复制后递增的，存在缓冲区溢出风险。未见对源字符串长度的前置校验。 |
| 1339 | vim-9.1.0790 | match_with_backref | cpp/unbounded-write | 1600 | FP | TP | 代码使用STRCPY（即strcpy）将长度未知的rex.line复制到固定大小的reg_tofree缓冲区，虽然reg_tofree会根据rex.line的长度重新分配，但分配逻辑（len = STRLEN(rex.line) + ... |
| 1340 | vim-9.1.0790 | get_reg_contents | cpp/unbounded-write | 2668 | FP | TP | 代码使用STRCPY（即strcpy）将y_current->y_array[i]的内容复制到retval缓冲区，但目标缓冲区retval的大小是根据源字符串长度之和预先计算的，理论上不会溢出。然而，告警指出源数据可能来自外部输入（如... |
| 1341 | vim-9.1.0790 | do_put | cpp/unbounded-write | 2094 | FP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将y_array[y_size - 1]的内容复制到未进行边界检查的缓冲区newp中，存在缓冲区溢出风险。 |
| 1343 | vim-9.1.0790 | op_yank | cpp/unbounded-write | 1278 | FP | TP | 代码使用STRCPY宏（即strcpy）将两个字符串拼接，目标缓冲区大小通过alloc动态分配，但分配的大小基于两个源字符串的STRLEN之和，未考虑strcpy可能导致的缓冲区溢出风险，因为strcpy会复制终止空字符，而分配时已预... |
| 1344 | vim-9.1.0790 | op_yank | cpp/unbounded-write | 1279 | FP | TP | 代码使用`strcat`拼接两个字符串，目标缓冲区`pnew`的大小由`alloc`分配，其大小基于两个源字符串的长度之和，但未考虑`strcat`操作本身需要目标缓冲区已包含第一个字符串内容，这可能导致缓冲区溢出。切片中未见任何边界... |
| 1345 | vim-9.1.0790 | stuff_yank | cpp/unbounded-write | 452 | FP | TP | 切片代码显示STRCPY宏直接展开为strcpy，目标缓冲区lp的大小为STRLEN(*pp) + STRLEN(p) + 1，但源字符串*pp的长度未经验证，若其长度超过lp的分配大小，将导致缓冲区溢出。切片中未见对*pp长度的前置... |
| 1346 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2755 | FP | TP | 代码使用`strcat`拼接字符串，目标缓冲区`scriptname`的大小为`STRLEN(name) + 14`，但拼接的源字符串`name`或其变体长度未在切片内进行限制，可能导致缓冲区溢出。 |
| 1347 | vim-9.1.0790 | ExpandPackAddDir | cpp/unbounded-write | 1226 | FP | TP | sprintf 使用环境变量等外部输入作为格式化字符串的一部分，目标缓冲区大小仅基于 pat 的长度分配，未考虑固定字符串 'pack/*/opt/' 和通配符 '*' 的长度，存在缓冲区溢出风险。 |
| 1348 | vim-9.1.0790 | sign_jump | cpp/unbounded-write | 1324 | FP | TP | 代码使用`sprintf`将外部文件名和行号格式化到固定大小的缓冲区中，缓冲区大小仅基于文件名长度计算，未考虑格式化字符串`"e +%ld %s"`的额外开销，存在缓冲区溢出风险。 |
| 1349 | vim-9.1.0790 | dump_word | cpp/unbounded-write | 4187 | FP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或外部数据（如word或cword），切片中未见对p的长度进行校验或使用安全函数，存在缓冲区溢出风险。 |
| 1351 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2998 | FP | TP | 代码使用STRCPY宏（即strcpy）将repl_to复制到新分配的缓冲区p中，未检查目标缓冲区大小，且repl_to是外部输入（来自先前拼写替换），存在缓冲区溢出风险。切片中未见对repl_to长度的边界检查。 |
| 1352 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2999 | FP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p中，目标缓冲区p的大小为ml_get_curline_len() + addlen + 1，但拼接的源字符串长度未经验证，可能导致缓冲区溢出。切片中未见对源字符串长度... |
| 1353 | vim-9.1.0790 | count_common_word | cpp/unbounded-write | 1919 | FP | TP | 代码使用STRCPY宏（即strcpy）将未知长度的字符串p复制到新分配的内存wc->wc_word中，虽然分配的大小基于STRLEN(p)+1，但strcpy本身不检查目标缓冲区大小，若p在复制前被修改或分配计算有误，仍可能导致溢出... |
| 1354 | vim-9.1.0790 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的lang字符串复制到固定大小的sl.sl_lang数组中，切片中未显示sl.sl_lang的大小定义，也未对lang的长度进行任何校验，存在缓冲区溢出风险。 |
| 1355 | vim-9.1.0790 | spell_move_to | cpp/unbounded-write | 1420 | FP | TP | 代码使用STRCPY宏（即strcpy）将长度未知的line字符串复制到固定大小的buf缓冲区，而buf的大小仅根据len + MAXWLEN + 2分配，未对源字符串长度进行限制，存在缓冲区溢出风险。 |
| 1359 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2464 | FP | TP | 切片代码中，STRCPY(p, items[1]) 直接将 items[1] 复制到缓冲区 p，而 p 的大小为 STRLEN(items[1]) + 2，未对源字符串长度进行限制，可能导致缓冲区溢出。 |
| 1360 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2495 | FP | TP | 切片代码中，STRCAT宏直接调用strcat，且目标缓冲区p的大小由动态计算的长度l决定，但l包含了源字符串items[1]的长度，未检查是否超过p的分配大小。存在缓冲区溢出的风险。 |
| 1362 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2746 | FP | TP | 切片代码中第2746行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件读取的未经验证的数据，可能导致缓冲区溢出。 |
| 1363 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2748 | FP | TP | 切片代码中第2748行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，未检查长度，可能导致缓冲区溢出。 |
| 1368 | vim-9.1.0790 | expand_tag_fname | cpp/unbounded-write | 4125 | FP | TP | 代码使用不安全的STRCPY（即strcpy）将tag_fname复制到固定大小的缓冲区retval，而tag_fname是外部输入（如环境变量或文件读取），其长度可能超过目标缓冲区大小（MAXPATHL），存在缓冲区溢出风险。切片中... |
| 1369 | vim-9.1.0790 | findtags_add_match | cpp/unbounded-write | 2623 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将外部输入（如st->help_lang、st->tag_fname、st->lbuf）复制到固定大小的缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1370 | vim-9.1.0790 | findtags_add_match | cpp/unbounded-write | 2702 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将外部来源的字符串（如st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1372 | vim-9.1.0790 | current_tagblock | cpp/unbounded-write | 1386 | FP | TP | sprintf使用未经验证的字符串p和长度len作为输入，直接写入固定大小的缓冲区spat和epat，存在缓冲区溢出风险。切片代码中未见对p或len进行边界检查或使用安全函数（如snprintf）。 |
| 1373 | vim-9.1.0790 | uc_check_code | cpp/unbounded-write | 1778 | FP | TP | 切片代码中多次使用STRCPY（即strcpy）将外部输入（如eap->arg）复制到缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1375 | vim-9.1.0790 | trans_function_name_ext | cpp/unbounded-write | 4571 | FP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将sid_buf内容复制到目标缓冲区，而sid_buf的大小为20字节，但复制源sid_buf可能包含格式化后的字符串，若其长度超过目标缓冲区剩余空间（name+3）则会导致缓冲区溢出... |
| 1376 | vim-9.1.0790 | fname_trans_sid | cpp/unbounded-write | 2115 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区fname_buf的大小为FLEN_FIXED。虽然存在长度检查`i + STRLEN(name + llen) < FLEN_FIXED`，但该检查仅确保拼接后的总长度小... |
| 1377 | vim-9.1.0790 | fname_trans_sid | cpp/unbounded-write | 2127 | FP | TP | 切片代码中，STRCPY宏直接展开为strcpy，且目标缓冲区fname的大小由alloc(i + STRLEN(name + llen) + 1)动态分配，但源字符串name + llen来自外部输入，其长度未在切片内进行验证或限制... |
| 1378 | vim-9.1.0790 | set_ufunc_name | cpp/unbounded-write | 663 | FP | TP | 代码使用不安全的strcpy函数将外部传入的字符串name复制到固定大小的缓冲区fp->uf_name中，切片中未见对name长度的校验或使用安全函数，存在缓冲区溢出风险。 |
| 1380 | vim-9.1.0790 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到固定大小的缓冲区`funcname`，而`funcname`的大小仅为`STRLEN(name) + 3`，未预留足够的空间来容纳源字符串和额外的'g:'前缀，存在缓冲... |
| 1381 | vim-9.1.0790 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | TP | 代码使用STRCPY（即strcpy）将变量`name`复制到新分配的内存`newsav->sav_key`中，目标缓冲区大小仅为`STRLEN(name) + 1`，与源字符串长度相同，但strcpy不检查目标缓冲区大小，若`nam... |
| 1382 | vim-9.1.0790 | find_exported | cpp/unbounded-write | 756 | FP | TP | sprintf 使用外部输入（name 和 script->sn_autoload_prefix）直接格式化到缓冲区，未检查长度。虽然存在基于 len 的缓冲区大小分配逻辑，但 sprintf 调用本身未使用长度限制，存在缓冲区溢出风险。 |
| 1383 | vim-9.1.0790 | find_exported | cpp/unbounded-write | 763 | FP | TP | sprintf函数使用外部输入的`name`和`sid`拼接字符串，目标缓冲区`funcname`的大小由`len`决定，但`sprintf`未限制写入长度，存在缓冲区溢出风险。切片代码中未见对`name`长度或最终字符串长度的边界检查。 |
| 1384 | vim-9.1.0790 | xxdline | cpp/unbounded-write | 534 | FP | TP | 代码使用strcpy将外部输入'l'复制到固定大小的缓冲区'z'，未检查'l'的长度，存在缓冲区溢出风险。切片中未见对'l'的长度进行验证或使用安全函数。 |
| 1499 | redis-7.4.2 | auxHumanNodenameSetter | Dereference of null pointer | 233 | FP | TP | 在`else if (sdslen(n->human_nodename) != 0)`这一行，当`n`为`NULL`时，代码会直接解引用`n`指针以访问`n->human_nodename`，这会导致空指针解引用错误。切片代码中未见任... |
| 1541 | redis-7.2.1 | auxHumanNodenameSetter | Dereference of null pointer | 267 | FP | TP | 在 `else if (sdslen(n->human_nodename) != 0)` 这一行，当 `n` 为 `NULL` 时，代码会解引用空指针 `n` 以访问其成员 `human_nodename` 并传递给 `sdslen`... |
| 1630 | redis-8.0.2 | auxHumanNodenameSetter | Dereference of null pointer | 234 | FP | TP | 在 `if (n)` 为 false 的分支中，代码直接访问 `n->human_nodename` 并调用 `sdslen` 函数，此时 `n` 为 NULL 指针，导致空指针解引用。切片中未见任何防护机制能阻止此访问。 |
| 1655 | ffmpeg-7.1.1 | try_push_frame | Dereference of null pointer | 241 | FP | TP | 切片代码显示，在调用 `outbuf->pts = inbuf[0]->pts;` 之前，`inbuf[0]` 可能为 NULL（因为 `inbuf` 数组初始化为 NULL，且 `ff_inlink_consume_samples`... |
| 1711 | ffmpeg-7.1.1 | shift_frame | Dereference of null pointer | 152 | FP | TP | 切片代码中直接解引用了指针变量 `frame` 以访问其 `pts` 成员，但该指针的来源和空值检查在切片中不可见，且没有前置的防护逻辑，因此存在解引用空指针的逻辑错误风险。 |
| 1731 | ffmpeg-7.0.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | TP | 切片代码显示`dc_val`被初始化为NULL，随后在未进行非空检查的情况下，通过`*dc_val = dcdiff;`进行解引用赋值，存在解引用空指针的逻辑错误风险。 |
| 1750 | ffmpeg-7.0.1 | try_push_frame | Dereference of null pointer | 241 | FP | TP | 切片代码显示，在访问 `inbuf[0]->pts` 之前，`inbuf` 数组被初始化为 `{ NULL }`，且 `ff_inlink_consume_samples` 的返回值未被检查，`inbuf[0]` 可能仍为 NULL，... |
| 1804 | ffmpeg-7.0.1 | shift_frame | Dereference of null pointer | 153 | FP | TP | 切片代码中，变量 `frame` 在未经验证是否为 NULL 的情况下被直接解引用以访问其 `pts` 成员，这构成了对空指针的解引用逻辑错误。 |
| 1840 | ffmpeg-6.1.1 | try_push_frame | Dereference of null pointer | 244 | FP | TP | 切片代码显示，`inbuf[0]` 在循环中被赋值，但若 `ctx->nb_inputs` 为0，则 `inbuf[0]` 保持初始值 NULL，随后在 `outbuf->pts = inbuf[0]->pts;` 处解引用，存在解引... |
| 1852 | ffmpeg-6.1.1 | ebml_read_uint | Dereference of null pointer | 994 | FP | TP | 在切片代码中，当size为0时，函数会先执行`*num = default_value;`，然后立即被`*num = 0;`覆盖，这导致对default_value的赋值无效，是一个逻辑错误。虽然指针num本身可能不为空，但代码存在明... |
| 1915 | ffmpeg-7.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | TP | 切片代码显示`dc_val`被初始化为NULL，随后在未进行非空检查的情况下，通过`*dc_val = dcdiff;`进行解引用赋值，存在解引用空指针的逻辑错误风险。 |
| 1924 | ffmpeg-7.1 | try_push_frame | Dereference of null pointer | 512 | FP | TP | 在切片代码中，`frame->pts = s->input_frames[0]->pts;` 这一行直接解引用了 `s->input_frames[0]`。根据前面的逻辑，当 `nb_samples` 为0时会跳转到 `eof` 标签... |
| 1956 | ffmpeg-7.1 | locate_option | Dereference of null pointer | 495 | FP | TP | 在切片代码中，`po` 指针来自 `find_option` 的返回值，当 `find_option` 未找到匹配项时，会返回一个 `name` 字段为 NULL 的 `OptionDef` 结构体指针。随后代码直接访问 `po->n... |
| 1970 | ffmpeg-7.1 | ost_add | Dereference of null pointer | 1541 | FP | TP | 在切片代码的第1541行，存在对指针`ist`的成员`st`的访问（`ist->st->duration`），但该行上方的条件判断`if (ost->ist && ost->ist->st->duration > 0)`表明，只有当`... |
| 2025 | ffmpeg-6.0 | try_push_frame | Dereference of null pointer | 243 | FP | TP | 切片代码显示，`inbuf[0]` 在循环中被 `ff_inlink_consume_samples` 填充，但该函数可能返回0且不设置 `inbuf[0]`，导致其保持为NULL。随后代码直接解引用 `inbuf[0]->pts`，... |
| 2044 | ffmpeg-6.0 | locate_option | Dereference of null pointer | 424 | FP | TP | 在切片代码中，`po = find_option(options, cur_opt);` 后直接访问 `po->name`，而 `find_option` 函数在未找到匹配项时返回的 `po` 指针可能指向一个 `name` 为 NU... |
| 2067 | ffmpeg-6.0 | shift_frame | Dereference of null pointer | 150 | FP | TP | 切片代码显示在函数 shift_frame 中，直接解引用了指针变量 `frame` 的成员 `pts`，但切片中未见 `frame` 指针的初始化或空值检查，存在解引用空指针的逻辑错误风险。 |
| 2078 | git-2.46.0 | sync_submodule | Dereference of null pointer | 1273 | FP | TP | 切片代码中，变量 `sub` 由 `submodule_from_path` 函数返回，该函数可能返回 NULL，但后续代码 `sub->name` 直接解引用 `sub` 指针，未进行 NULL 检查，存在解引用空指针的风险。 |
| 2124 | git-2.46.0 | prepare_attr_stack | Dereference of null pointer | 1021 | FP | TP | 在while循环条件`(*stack)->origin`中直接解引用指针`*stack`，但循环前`*stack = info->prev;`可能使`*stack`为NULL，切片中未见对`*stack`为NULL的检查，存在空指针解... |
| 2130 | git-2.49.0 | sync_submodule | Dereference of null pointer | 1288 | FP | TP | 切片代码中，变量 `sub` 由 `submodule_from_path` 函数返回，该函数可能返回 NULL，但后续代码 `sub->name` 直接解引用 `sub` 指针，未进行空指针检查，存在空指针解引用风险。 |
| 2144 | git-2.49.0 | clar__fail | Dereference of null pointer | 698 | FP | TP | 切片代码中直接解引用了指针变量 `error`，但未显示其被初始化或进行空值检查，存在解引用空指针的逻辑错误风险。 |
| 2193 | git-2.49.0 | prepare_attr_stack | Dereference of null pointer | 986 | FP | TP | 在while循环条件`(*stack)->origin`中直接解引用指针`*stack`，但前一行`*stack = info->prev;`可能使`*stack`为NULL，切片中未见对`info->prev`或`*stack`的非... |
| 2198 | git-2.44.0 | sync_submodule | Dereference of null pointer | 1267 | FP | TP | 切片代码显示，变量 `sub` 由 `submodule_from_path` 函数返回，该函数可能返回 NULL，但后续代码直接解引用 `sub->name`，未进行空指针检查，存在空指针解引用风险。 |
| 2252 | git-2.50.1 | sync_submodule | Dereference of null pointer | 1288 | FP | TP | 切片代码显示 `sub` 指针来自 `submodule_from_path` 的返回值，该函数可能返回 NULL，但后续直接解引用 `sub->name` 而未进行空指针检查，存在解引用空指针的风险。 |
| 2266 | git-2.50.1 | clar__fail | Dereference of null pointer | 698 | FP | TP | 切片代码中直接解引用了指针变量 `error`，但未显示其被初始化或进行空值检查，存在解引用空指针的逻辑错误风险。 |
| 2314 | git-2.50.1 | prepare_attr_stack | Dereference of null pointer | 986 | FP | TP | 在while循环条件`(*stack)->origin`中直接解引用指针`*stack`，但切片代码显示`*stack`可能在上一步`*stack = info->prev;`中被赋值为NULL（因为`info->prev`可能为NU... |
| 2319 | git-2.47.1 | sync_submodule | Dereference of null pointer | 1283 | FP | TP | 切片代码显示，在调用 `submodule_from_path` 后，未检查其返回值 `sub` 是否为 NULL 就直接解引用 `sub->name`，存在对空指针解引用的逻辑错误风险。 |
| 2376 | musl-1.2.1 | load_direct_deps | Dereference of null pointer | 1206 | FP | TP | 切片代码显示，在未检查指针 `p->deps` 是否为 `NULL` 的情况下，直接将其作为数组进行下标访问 `p->deps[cnt] = 0;`，这构成了对空指针的潜在解引用，存在逻辑错误风险。 |
| 2389 | musl-1.2.4 | load_direct_deps | Dereference of null pointer | 1280 | FP | TP | 切片代码显示，在警告行使用 `p->deps` 之前，存在一个条件分支 `if (!p->deps)` 用于处理分配失败的情况，但该分支会调用 `longjmp` 退出函数。然而，警告行位于 `if (p==head)` 循环内，且 ... |
| 2417 | musl-1.1.24 | load_direct_deps | Dereference of null pointer | 1201 | FP | TP | 切片代码显示，在未检查指针 `p->deps` 是否已分配内存的情况下，直接对其进行数组下标访问和赋值，存在解引用空指针的风险。 |
| 2430 | musl-1.2.3 | load_direct_deps | Dereference of null pointer | 1218 | FP | TP | 切片代码显示，在警告行`p->deps[cnt++] = q;`之前，存在条件分支`if (!p->deps)`，若`p->deps`为空则会调用`error`并可能`longjmp`退出。然而，警告行位于`if (p==head)`... |
| 2436 | musl-1.2.3 | load_direct_deps | Dereference of null pointer | 1230 | FP | TP | 切片代码显示，在未检查指针 `p->deps` 是否为 `NULL` 的情况下，直接对其进行了数组下标访问和赋值操作，存在解引用空指针的风险。 |
| 2449 | musl-1.2.2 | load_direct_deps | Dereference of null pointer | 1217 | FP | TP | 切片代码显示，在警告行`p->deps[cnt++] = q;`之前，存在条件分支`if (!p->deps)`，若`p->deps`为NULL则会报错并跳转。然而，在`p==head && cnt<2`时，`p->deps`被赋值为... |
| 2455 | musl-1.2.2 | load_direct_deps | Dereference of null pointer | 1229 | FP | TP | 切片代码显示，在未检查指针 `p->deps` 是否为 `NULL` 的情况下，直接对其进行了数组下标访问和赋值操作，存在解引用空指针的风险。 |
| 2490 | tmux-3.1 | mode_tree_build | Dereference of null pointer | 407 | FP | TP | 在切片代码中，当 `tag == UINT64_MAX` 时，代码直接访问 `mtd->line_list[mtd->current].item->tag`，但此时 `mtd->line_list` 可能为 NULL（如函数开头检查所... |
| 2497 | tmux-3.0 | mode_tree_build | Dereference of null pointer | 407 | FP | TP | 在切片代码中，当 `tag == UINT64_MAX` 时，代码直接访问 `mtd->line_list[mtd->current].item->tag`，但此时 `mtd->line_list` 可能为 NULL（如函数开头检查所... |

### 5.5 Unknown：算法=TP，LLM=Unknown（共 0 条）

> 算法判定为 TP，LLM 无法判定。

*（无）*

### 5.6 Unknown：算法=FP，LLM=Unknown（共 0 条）

> 算法判定为 FP，LLM 无法判定。

*（无）*

## 6. 按 (tool_name, project_name_without_version, rule_id) 联合分组统计

> 共 **43** 种不同组合（种类），按条目数降序排列。

| # | tool_name | project_name_without_version | rule_id | 总计 | TP | FP | Unknown |
|---|---|---|---|---|---|---|---|
| 1 | codeql | vim | cpp/unbounded-write | 753 | 550 | 203 | 0 |
| 2 | csa | ffmpeg | Dereference of null pointer | 445 | 14 | 431 | 0 |
| 3 | csa | git | Dereference of null pointer | 293 | 10 | 283 | 0 |
| 4 | csa | redis | Dereference of null pointer | 210 | 4 | 206 | 0 |
| 5 | codeql | git | cpp/inconsistent-null-check | 129 | 18 | 111 | 0 |
| 6 | csa | musl | Dereference of null pointer | 98 | 7 | 91 | 0 |
| 7 | codeql | vim | cpp/inconsistent-null-check | 87 | 9 | 78 | 0 |
| 8 | codeql | git | cpp/overflow-buffer | 50 | 0 | 50 | 0 |
| 9 | codeql | openssl-openssl | cpp/unterminated-variadic-call | 45 | 0 | 45 | 0 |
| 10 | csa | tmux | Dereference of null pointer | 44 | 2 | 42 | 0 |
| 11 | codeql | openssl-openssl | cpp/use-after-free | 40 | 1 | 39 | 0 |
| 12 | codeql | ffmpeg | cpp/inconsistent-null-check | 35 | 9 | 26 | 0 |
| 13 | codeql | ffmpeg | cpp/offset-use-before-range-check | 33 | 1 | 32 | 0 |
| 14 | codeql | openssl-openssl | cpp/invalid-pointer-deref | 25 | 0 | 25 | 0 |
| 15 | codeql | openssl-openssl | cpp/unbounded-write | 24 | 6 | 18 | 0 |
| 16 | codeql | vim | cpp/overrunning-write | 21 | 21 | 0 | 0 |
| 17 | codeql | vim | cpp/unsafe-strcat | 21 | 1 | 20 | 0 |
| 18 | codeql | git | cpp/offset-use-before-range-check | 20 | 0 | 20 | 0 |
| 19 | codeql | musl | cpp/unbounded-write | 20 | 0 | 20 | 0 |
| 20 | codeql | openssl-openssl | cpp/inconsistent-null-check | 19 | 4 | 15 | 0 |
| 21 | codeql | git | cpp/invalid-pointer-deref | 15 | 5 | 10 | 0 |
| 22 | codeql | vim | cpp/invalid-pointer-deref | 10 | 1 | 9 | 0 |
| 23 | codeql | vim | cpp/redundant-null-check-simple | 10 | 0 | 10 | 0 |
| 24 | codeql | openssl-openssl | cpp/offset-use-before-range-check | 8 | 0 | 8 | 0 |
| 25 | codeql | ffmpeg | cpp/unbounded-write | 5 | 4 | 1 | 0 |
| 26 | codeql | git | cpp/no-space-for-terminator | 5 | 0 | 5 | 0 |
| 27 | codeql | musl | cpp/suspicious-allocation-size | 5 | 0 | 5 | 0 |
| 28 | codeql | musl | cpp/unsafe-strcat | 5 | 0 | 5 | 0 |
| 29 | codeql | nginx | cpp/inconsistent-null-check | 5 | 0 | 5 | 0 |
| 30 | codeql | openssl-openssl | cpp/unsafe-strcat | 5 | 2 | 3 | 0 |
| 31 | codeql | vim | cpp/offset-use-before-range-check | 5 | 0 | 5 | 0 |
| 32 | codeql | git | cpp/redundant-null-check-simple | 4 | 0 | 4 | 0 |
| 33 | codeql | openssl-openssl | cpp/redundant-null-check-simple | 3 | 0 | 3 | 0 |
| 34 | codeql | ffmpeg | cpp/overflow-buffer | 2 | 1 | 1 | 0 |
| 35 | codeql | musl | cpp/offset-use-before-range-check | 2 | 0 | 2 | 0 |
| 36 | codeql | tmux | cpp/overflow-buffer | 2 | 0 | 2 | 0 |
| 37 | codeql | curl-8_11 | cpp/invalid-pointer-deref | 1 | 0 | 1 | 0 |
| 38 | codeql | curl-8_13 | cpp/invalid-pointer-deref | 1 | 0 | 1 | 0 |
| 39 | codeql | curl-8_15 | cpp/invalid-pointer-deref | 1 | 0 | 1 | 0 |
| 40 | codeql | curl-8_7 | cpp/inconsistent-null-check | 1 | 0 | 1 | 0 |
| 41 | codeql | curl-8_7 | cpp/invalid-pointer-deref | 1 | 0 | 1 | 0 |
| 42 | codeql | curl-8_9 | cpp/inconsistent-null-check | 1 | 0 | 1 | 0 |
| 43 | codeql | curl-8_9 | cpp/invalid-pointer-deref | 1 | 0 | 1 | 0 |

---

*报告由 `analyze_results.py` 自动生成，生成时间：2026-03-05 23:16:33*
