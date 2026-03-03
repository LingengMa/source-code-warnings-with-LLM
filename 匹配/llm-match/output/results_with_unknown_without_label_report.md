# LLM 分类结果分析报告

- **分析文件**：`results_with_unknown_without_label.json`
- **完整路径**：`/home/lg/Documents/projects/毕设/大仓/匹配/llm-match/output/results_with_unknown_without_label.json`
- **生成时间**：2026-03-03 20:10:02

---

## 1. 数据总览

| 指标 | 数值 |
|---|---|
| 数据总条数 | 2500 |
| 有效条目数（含 label / llm_label） | 2500 |
| 跳过条目数（字段缺失或无效） | 0 |
| Unknown 条目数 | 102 |
| Unknown 比率 | 4.1% |
| 已判定条目数（非 Unknown） | 2398 |
| 判定一致数 | 1538 |
| 判定不一致数 | 860 |

## 2. 算法标注（label）分布

| label | 数量 | 占比 |
|---|---|---|
| TP | 216 | 8.6% |
| FP | 2284 | 91.4% |

## 3. label × llm_label 交叉矩阵

| label \ llm_label | TP | FP | Unknown | **合计** |
|---|---|---|---|---|
| **TP** | 133 | 71 | 12 | **216** |
| **FP** | 789 | 1405 | 90 | **2284** |
| **合计** | 922 | 1476 | 102 | **2500** |

## 4. 汇总指标

> 以下指标仅基于**已判定（非 Unknown）**条目计算。

| 指标 | 数值 |
|---|---|
| 准确率（Accuracy） | 64.1% |
| 精确率（Precision，以 TP 为正类） | 14.4% |
| 召回率（Recall，以 TP 为正类） | 65.2% |
| F1 分数（以 TP 为正类） | 23.6% |

## 5. 各分类条目详情

### 5.1 一致：算法=TP，LLM=TP（共 133 条）

> 算法与 LLM 均判定为真阳性（True Positive）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 403 | git-2.46.0 | get_rev | cpp/inconsistent-null-check | 189 | TP | TP | 代码在调用prio_queue_get后，未检查返回值是否为NULL，就直接解引用entry->commit，存在空指针解引用风险。切片中未显示任何前置检查或保证返回值非空的逻辑。 |
| 678 | vim-9.1.1591 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | TP | TP | 函数getcell在特定条件下（如行列越界或缓冲区为空）会返回NULL，但调用点vterm_screen_is_eol未对返回值进行空指针检查，直接解引用cell->chars，存在空指针解引用风险。 |
| 680 | vim-9.1.1591 | get_isolated_shell_name | cpp/inconsistent-null-check | 2754 | TP | TP | 函数`vim_strnsave`可能返回NULL，但调用结果`p`被直接返回给调用者，未进行空指针检查。这违反了代码库中85%的调用检查NULL的惯例，可能导致调用者解引用空指针。 |
| 692 | vim-9.1.1591 | barline_parse | cpp/inconsistent-null-check | 1158 | TP | TP | 代码在调用 vim_strnsave 后未检查返回值是否为 NULL，直接赋值给 bv_string 使用，存在空指针解引用风险。切片中未显示任何针对该返回值的空指针检查。 |
| 693 | vim-9.1.1591 | common_function | cpp/unsafe-strcat | 5401 | TP | TP | 代码使用宏STRCAT(IObuff, start_bracket)进行字符串拼接，该宏直接展开为strcat((char *)(d), (char *)(s))。切片中未显示对IObuff缓冲区大小的检查，也未显示对start_br... |
| 697 | vim-9.1.1591 | prt_line_number | cpp/overrunning-write | 387 | TP | TP | sprintf 使用格式字符串 '%6ld' 写入最多6位数字加符号和终止符，最多需要21字节，但目标缓冲区 tbuf 仅20字节，存在缓冲区溢出风险。 |
| 699 | vim-9.1.1591 | msg_outnum | cpp/overrunning-write | 1651 | TP | TP | 目标缓冲区 `buf` 大小为20字节，而 `sprintf` 写入 `"%ld"` 格式化的长整数在最坏情况下（如 `-9223372036854775808`）需要21字节（包括负号和终止空字符），存在缓冲区溢出风险。 |
| 698 | vim-9.1.1591 | highlight_color | cpp/overrunning-write | 3278 | TP | TP | sprintf 目标缓冲区 'buf' 大小为 10 字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少 8 个字符（# + 6 个十六进制数字 + '\0'），计算出的实际需求为 8 字节，小于缓冲区大小，因此... |
| 701 | vim-9.1.1591 | ga_concat_strings | cpp/unbounded-write | 788 | TP | TP | 代码使用不安全的strcpy函数，将动态长度的字符串复制到固定大小的缓冲区中，且切片中未显示对源字符串长度的检查或对目标缓冲区大小的验证，存在缓冲区溢出风险。 |
| 702 | vim-9.1.1591 | maketitle | cpp/unbounded-write | 4239 | TP | TP | 代码使用STRCPY（即strcpy）将变量`name`复制到固定大小的缓冲区`buf`中，而`name`可能来自不受控的文件名，且切片中未显示对`name`长度的检查或对`buf`的边界保护，存在缓冲区溢出风险。 |
| 703 | vim-9.1.1591 | buf_write | cpp/unbounded-write | 1208 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将fname复制到IObuff缓冲区，未检查fname长度是否超过IObuff大小，存在缓冲区溢出风险。切片中未显示IObuff的大小定义，但strcpy的不安全使用模式是明确的。 |
| 705 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2150 | TP | TP | 代码中直接使用STRCAT宏（即strcat）将p_extra拼接到leader缓冲区，未检查目标缓冲区leader的大小，存在缓冲区溢出风险。 |
| 706 | vim-9.1.1591 | transstr | cpp/unbounded-write | 400 | TP | TP | 代码使用STRCAT宏（即strcat）向目标缓冲区res追加内容，而res的大小由alloc(len + 1)或alloc(vim_strsize(s) + 1)分配，但后续循环中多次追加transchar_byte的返回值，其长度... |
| 707 | vim-9.1.1591 | globpath | cpp/unbounded-write | 4180 | TP | TP | 代码使用STRCPY（即strcpy）将用户控制的'file'参数复制到固定大小的缓冲区'buf'中，虽然存在长度检查（pathlen + seplen + filelen + 1 <= MAXPATHL），但该检查依赖于'filel... |
| 708 | vim-9.1.1591 | expand_shellcmd | cpp/unbounded-write | 3902 | TP | TP | 代码使用STRCPY（即strcpy）将可变长度的字符串`pat`复制到固定大小的缓冲区`buf`中，且切片内未显示对`pat`长度进行任何边界检查，存在缓冲区溢出风险。 |
| 709 | vim-9.1.1591 | win_redr_status_matches | cpp/unbounded-write | 698 | TP | TP | 代码使用STRCPY（即strcpy）宏将字符串复制到固定大小的缓冲区buf中，而buf的大小基于Columns计算，但源字符串s来自外部输入（matches数组），其长度未经验证，存在缓冲区溢出风险。 |
| 710 | vim-9.1.1591 | win_redr_status_matches | cpp/unbounded-write | 717 | TP | TP | 代码使用STRCPY（即strcpy）将transchar_byte函数的返回值复制到固定大小的缓冲区buf中，而transchar_byte返回的字符串长度未知，可能导致缓冲区溢出。切片中未显示对目标缓冲区大小的检查或限制。 |
| 711 | vim-9.1.1591 | debuggy_find | cpp/unbounded-write | 1067 | TP | TP | 代码使用STRCPY（即strcpy）宏将源字符串fname复制到新分配的内存name中，未检查目标缓冲区大小。由于fname是函数参数，其长度可能超过分配的内存（STRLEN(fname) + 3），导致缓冲区溢出。 |
| 712 | vim-9.1.1591 | has_profiling | cpp/unbounded-write | 973 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的源字符串fname复制到固定大小的目标缓冲区pe->pen_name，存在缓冲区溢出风险。切片显示目标缓冲区大小基于STRLEN(fname)+1分配，但STRCPY本身不检查边界... |
| 714 | vim-9.1.1591 | do_string_sub | cpp/unbounded-write | 8057 | TP | TP | 代码在告警行使用STRCPY（即strcpy）将'tail'指向的字符串复制到动态分配的缓冲区'ga.ga_data'中，目标缓冲区大小由'ga.ga_len'和'ga.ga_data'的分配决定，但未检查'tail'字符串的长度是否... |
| 713 | vim-9.1.1591 | ex_diffpatch | cpp/unbounded-write | 1512 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将tmp_new复制到buf，而buf的大小是根据tmp_orig、esc_name和tmp_new的长度计算分配的，但tmp_new是vim_tempname生成的临时文件名，其长度可能... |
| 715 | vim-9.1.1591 | set_var_const | cpp/unbounded-write | 4300 | TP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname的长度由STRLEN(varname)计算，但目标缓冲区di->di_key的大小仅为STRLEN(varname) + 1，没有预留... |
| 716 | vim-9.1.1591 | cat_prefix_varname | cpp/unbounded-write | 2578 | TP | TP | 代码使用strcpy将外部传入的name字符串复制到varnamebuf缓冲区，虽然根据name长度动态分配了缓冲区，但分配后立即将长度赋值给varnamebuflen，随后在STRCPY调用时未检查缓冲区大小，若name在分配后被修... |
| 718 | vim-9.1.1591 | make_filter_cmd | cpp/unbounded-write | 1854 | TP | TP | 代码在多个分支中直接使用 STRCPY（即 strcpy）将外部传入的 cmd 参数复制到固定大小的缓冲区 buf 中，而 buf 的大小仅基于 cmd 等字符串的长度计算，未考虑目标缓冲区大小限制，存在缓冲区溢出风险。 |
| 720 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 795 | TP | TP | 代码使用STRCPY（即strcpy）将长度不确定的字符串&s[start_col]复制到固定大小的缓冲区sortbuf1中，而sortbuf1的大小仅由maxlen+1决定，maxlen是之前遍历行计算出的最大长度，但&s[star... |
| 717 | vim-9.1.1591 | ex_substitute | cpp/unbounded-write | 5115 | TP | TP | 切片代码中第5115行附近存在对STRCAT宏的调用，该宏展开为strcat，将sub_firstline + copycol的内容追加到new_start指向的缓冲区。切片显示new_start缓冲区的大小通过new_start_l... |
| 721 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 815 | TP | TP | 代码使用STRCPY宏（即strcpy）将长度不确定的字符串s[start_col]复制到固定大小的缓冲区sortbuf1中，而sortbuf1的大小仅由maxlen+1决定，无法保证源字符串长度不超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 722 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 833 | TP | TP | 切片代码显示 STRCPY 宏（即 strcpy）被用于将长度不确定的字符串（来自缓冲区 s 的切片）复制到固定大小的缓冲区 sortbuf1 中，而 sortbuf1 的大小仅基于之前计算的最大行长（maxlen）分配，无法保证当前... |
| 724 | vim-9.1.1591 | expand_sfile | cpp/unbounded-write | 10143 | TP | TP | 代码使用STRCPY（即strcpy）将可变长度的字符串repl复制到固定大小的缓冲区newres中，而newres的大小仅由resultlen + 1决定，未检查repllen是否会导致目标缓冲区溢出，存在缓冲区溢出风险。 |
| 723 | vim-9.1.1591 | ex_sort | cpp/unbounded-write | 605 | TP | TP | 代码使用STRCPY宏（即strcpy）将长度未知的字符串`s`复制到固定大小的缓冲区`sortbuf1`中，而`sortbuf1`的大小仅基于`maxlen`分配，但`s`的长度可能超过`maxlen`（例如，当`s`来自后续被修改... |
| 725 | vim-9.1.1591 | repl_cmdline | cpp/unbounded-write | 5330 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串（src + srclen）复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小i是基于多个字符串长度计算分配的，但未确保目标缓冲区有足够空间容纳该... |
| 726 | vim-9.1.1591 | repl_cmdline | cpp/unbounded-write | 5336 | TP | TP | 代码使用STRCPY（即strcpy）将eap->nextcmd复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小由alloc(i)分配，i的计算包含了STRLEN(eap->nextcmd)，但复制前未检... |
| 727 | vim-9.1.1591 | replace_makeprg | cpp/unbounded-write | 5037 | TP | TP | 代码使用STRCPY（即strcpy）宏将用户控制的参数p复制到目标缓冲区ptr，目标缓冲区大小由alloc分配，但分配时仅基于program长度和p长度计算，未限制p的长度，若p长度超过分配空间将导致缓冲区溢出。 |
| 728 | vim-9.1.1591 | replace_makeprg | cpp/unbounded-write | 5052 | TP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串（`program`和`p`）复制到固定大小的缓冲区`new_cmdline`中，而`new_cmdline`的大小是通过`alloc`动态分配的，其长度计算依赖于`STR... |
| 731 | vim-9.1.1591 | get_exception_string | cpp/unbounded-write | 473 | TP | TP | 代码使用strcat向固定大小的缓冲区val追加内容，而val指向的缓冲区大小由vim_strnsave分配，其长度计算依赖于外部输入mesg和cmdname，但追加操作前未检查剩余空间，存在缓冲区溢出风险。 |
| 729 | vim-9.1.1591 | do_one_cmd | cpp/unbounded-write | 2686 | TP | TP | 切片代码中明确使用了不安全的 STRCPY 宏（即 strcpy），将未知长度的字符串（如来自环境变量、文件读取等外部输入）复制到固定大小的缓冲区 IObuff 中，存在缓冲区溢出风险。 |
| 733 | vim-9.1.1591 | escape_fname | cpp/unbounded-write | 4193 | TP | TP | 代码使用strcpy将源字符串(*pp)复制到目标缓冲区(p+1)，目标缓冲区大小仅为源字符串长度加2（alloc(STRLEN(*pp) + 2)），但strcpy会复制终止空字符，若源字符串长度恰好为STRLEN(*pp)，则复制... |
| 732 | vim-9.1.1591 | get_exception_string | cpp/unbounded-write | 484 | TP | TP | 代码使用`sprintf`将`mesg`（来自`value->throw_msg`）拼接到`val`缓冲区，而`val`缓冲区的大小由`vim_strnsave`分配，其长度计算依赖于`STRLEN(mesg)`，但`sprintf`... |
| 735 | vim-9.1.1591 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 879 | TP | TP | 代码使用不安全的strcpy函数将动态长度的字符串p复制到固定大小的缓冲区ccline.cmdbuff中，虽然调用了realloc_cmdbuff，但该函数仅在目标缓冲区长度不足时重新分配，而strcpy本身没有长度限制，存在缓冲区溢... |
| 734 | vim-9.1.1591 | cmdline_browse_history | cpp/unbounded-write | 1528 | TP | TP | 代码使用STRCPY宏（即strcpy）将历史记录字符串p复制到ccline.cmdbuff中，而ccline.cmdbuff的大小由alloc_cmdbuff根据plen分配，但分配时仅额外增加20字节，若p的长度（plen）接近或... |
| 736 | vim-9.1.1591 | vim_settempdir | cpp/unbounded-write | 5293 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的tempdir复制到固定大小的buf中，buf大小为MAXPATHL+2，而tempdir是外部传入的变量，可能超过目标缓冲区大小，导致缓冲区溢出。 |
| 738 | vim-9.1.1591 | buf_modname | cpp/unbounded-write | 3643 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的fname复制到新分配的缓冲区retval中，而retval的大小仅基于fnamelen + extlen + 3计算，未限制源字符串fname的长度，存在缓冲区溢出风险。 |
| 739 | vim-9.1.1591 | addfile | cpp/unbounded-write | 4219 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证的外部文件名`f`复制到新分配的缓冲区`p`，虽然缓冲区大小基于`STRLEN(f)+1`分配，但若`f`在分配后、复制前被并发修改，仍可能导致缓冲区溢出。切片中未显示对`f`的锁定或验... |
| 742 | vim-9.1.1591 | uniquefy_paths | cpp/unbounded-write | 2568 | TP | TP | 代码使用STRCPY（即strcpy）将用户可控的`pattern`参数复制到固定大小的缓冲区`file_pattern`中，而`file_pattern`的大小仅比`pattern`长度大2，未对源字符串长度进行限制，存在缓冲区溢出风险。 |
| 741 | vim-9.1.1591 | concat_fnames | cpp/unbounded-write | 3137 | TP | TP | 函数`concat_fnames`使用`alloc`分配缓冲区，其大小为两个输入字符串长度之和加3，随后使用`STRCPY`和`STRCAT`进行拷贝和拼接。由于`STRCAT`在拼接`fname2`时，目标缓冲区`dest`的大小已... |
| 743 | vim-9.1.1591 | uniquefy_paths | cpp/unbounded-write | 2685 | TP | TP | 代码在行号2685处使用STRCPY（即strcpy）宏将short_name复制到fnames[i]中，目标缓冲区fnames[i]的大小未知，而源short_name可能来自用户输入或环境变量，存在缓冲区溢出风险。切片中未显示对s... |
| 744 | vim-9.1.1591 | find_file_in_path_option | cpp/unbounded-write | 1911 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串*file_to_find复制到固定大小的缓冲区NameBuff（大小为MAXPATHL），存在缓冲区溢出风险。切片中未显示对*file_to_find长度的检查，且该字符串... |
| 745 | vim-9.1.1591 | ff_check_visited | cpp/unbounded-write | 1537 | TP | TP | 代码使用STRCPY（即strcpy）将ff_expand_buffer.string复制到vp->ffv_fname，目标缓冲区大小由ff_expand_buffer.length + 1决定，但源字符串长度可能等于或超过该大小，存... |
| 746 | vim-9.1.1591 | <global> | cpp/unbounded-write | 3794 | TP | TP | 代码使用strcat将未经验证长度的字符串s追加到缓冲区r，而r的大小是基于对s长度的计算（STRLEN(s)）分配的，但s来自文件内容（ml_get），其长度可能超过分配时预留的空间，导致缓冲区溢出。 |
| 747 | vim-9.1.1591 | foldDelMarker | cpp/unbounded-write | 1897 | TP | TP | 代码使用STRCPY宏（即strcpy）将源字符串p+len复制到目标缓冲区newline + (p - line)，未检查目标缓冲区大小，而目标缓冲区newline的大小为ml_get_len(lnum) - len + 1，源字符... |
| 749 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2899 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_prolog->title复制到固定大小的buffer[256]中，而title来自外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 748 | vim-9.1.1591 | foldAddMarker | cpp/unbounded-write | 1815 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串'line'复制到固定大小的缓冲区'newline'中，而'newline'的大小基于line_len、markerlen和STRLEN(cms)计算，但strcpy的源字符... |
| 751 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2905 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而res_cidfont->title是从外部资源文件读取的，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 750 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2901 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的字符串（res_prolog->title和res_prolog->version）长度未经验证，存在缓冲区溢出的风险。 |
| 752 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2907 | TP | TP | 代码使用STRCAT宏（即strcat）将res_cidfont->version拼接到固定大小的buffer数组，而version字符串长度未经验证，可能导致缓冲区溢出。切片中未显示对version长度的任何检查或限制。 |
| 753 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2912 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_cmap->title复制到固定大小的buffer[256]中，而res_cmap->title是从外部资源文件读取的，其长度未经验证，存在缓冲区溢出风险。 |
| 754 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2914 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的源字符串（如res_cmap->title和res_cmap->version）长度未经验证，存在缓冲区溢出的风险。 |
| 755 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2920 | TP | TP | 代码使用STRCPY（即strcpy）将res_encoding->title复制到固定大小的buffer[256]中，而title来源于外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 757 | vim-9.1.1591 | prt_resource_name | cpp/unbounded-write | 1659 | TP | TP | 代码使用strcpy复制字符串，虽然对源字符串长度进行了检查，但检查的目标是filename而非目标缓冲区resource_filename的大小。目标缓冲区的大小未知，若其小于MAXPATHL，仍可能发生缓冲区溢出。 |
| 756 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2922 | TP | TP | 代码使用STRCAT宏（即strcat）将资源标题和版本号拼接到固定大小的缓冲区buffer（256字节）中，未检查目标缓冲区长度，存在缓冲区溢出风险。切片中未显示对res_encoding->title或version长度的任何限制... |
| 758 | vim-9.1.1591 | do_helptags | cpp/unbounded-write | 1210 | TP | TP | 代码中直接使用STRCPY（即strcpy）将参数dirname复制到固定大小的缓冲区NameBuff中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 761 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 1112 | TP | TP | sprintf 使用未限制长度的动态字符串 p1 和 fname 作为输入，目标缓冲区 s 的大小为 (p2 - p1 + STRLEN(fname) + 2)，若拼接后字符串长度超过缓冲区大小，将导致缓冲区溢出。切片中未见任何长度检... |
| 763 | vim-9.1.1591 | load_colors | cpp/unbounded-write | 609 | TP | TP | sprintf 使用未经验证的用户输入 'name' 直接格式化字符串到固定大小的缓冲区 'buf' 中，缓冲区大小仅为 STRLEN(name) + 12，而格式化字符串 "colors/%s.vim" 会额外增加固定长度，若 na... |
| 770 | vim-9.1.1591 | ins_compl_infercase_gettext | cpp/unbounded-write | 723 | TP | TP | 代码使用STRCPY宏（即strcpy）将IObuff的内容复制到gap.ga_data中，而IObuff是一个固定大小的缓冲区（IOSIZE），但切片中未显示对IObuff的写入有明确的长度限制检查，存在缓冲区溢出的风险。 |
| 771 | vim-9.1.1591 | <global> | cpp/unbounded-write | 3140 | TP | TP | 代码直接使用sprintf将格式化字符串和用户控制的transchar(from)结果写入固定大小的缓冲区args->os_errbuf，未进行长度检查，存在缓冲区溢出风险。切片中未显示对os_errbuf大小的限制或对输入长度的验证。 |
| 774 | vim-9.1.1591 | <global> | cpp/unbounded-write | 811 | TP | TP | 代码使用宏STRCPY（即strcpy）将call_data复制到固定大小的缓冲区menu->strings[i]中，而call_data是外部传入的字符串，其长度未经验证，存在缓冲区溢出风险。 |
| 773 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2157 | TP | TP | 代码使用STRCPY（即strcpy）将fix_fname返回的字符串复制到新分配的缓冲区s中，而s的大小仅为STRLEN(f) + 1，与源字符串长度相同。若fix_fname函数未保证返回的字符串以空字符结尾，或在其内部处理中产生... |
| 772 | vim-9.1.1591 | findswapname | cpp/unbounded-write | 4967 | TP | TP | 代码使用STRCPY（即strcpy）将fname复制到新分配的fname2缓冲区，fname2的大小为n+2，而fname的长度为n，存在一个字节的冗余。虽然缓冲区大小看似足够，但STRCPY不检查目标缓冲区大小，且fname的来源... |
| 775 | vim-9.1.1591 | <global> | cpp/unbounded-write | 815 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将call_data字符串复制到固定大小的缓冲区menu->strings[i]中，而menu->strings[i]的大小仅通过alloc(STRLEN(call_data) + 5)分... |
| 776 | vim-9.1.1591 | msg_show_console_dialog | cpp/unbounded-write | 4505 | TP | TP | 代码使用STRCPY（即strcpy）将message字符串复制到confirm_msg缓冲区，其长度由alloc(len)分配，而len的计算包含了STRLEN(message)，但未预留额外的空间给源字符串的终止空字符，且strc... |
| 778 | vim-9.1.1591 | get_emsg_source | cpp/unbounded-write | 500 | TP | TP | 代码使用`sprintf`将`sname`格式化写入固定大小的缓冲区`Buf`，而`Buf`的大小仅为`STRLEN(sname) + STRLEN(p)`，未考虑`sprintf`添加的格式化字符和终止符，存在缓冲区溢出风险。 |
| 777 | vim-9.1.1591 | str2specialbuf | cpp/unbounded-write | 2015 | TP | TP | 切片代码显示，在调用STRCAT（即strcat）前，仅检查了源字符串s和目标缓冲区buf的当前长度之和是否小于len，但未检查拼接后总长度是否超过缓冲区buf的原始容量。如果buf在进入函数时已非空，或len参数大于buf的实际大小... |
| 780 | vim-9.1.1591 | expand_env_esc | cpp/unbounded-write | 1678 | TP | TP | 代码使用strcpy复制环境变量内容到目标缓冲区，仅通过比较源字符串长度与剩余缓冲区长度（dstlen）来判断，但未检查目标缓冲区dst的原始大小，存在缓冲区溢出风险。 |
| 783 | vim-9.1.1591 | push_showcmd | cpp/unbounded-write | 1809 | TP | TP | 代码使用不安全的strcpy函数，将源缓冲区showcmd_buf的内容复制到目标缓冲区old_showcmd_buf，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 786 | vim-9.1.1591 | op_replace | cpp/unbounded-write | 1299 | TP | TP | 代码中直接使用STRCPY（即strcpy）宏，将源字符串复制到目标缓冲区，未检查目标缓冲区大小。切片显示目标缓冲区newp通过alloc(oldlen + 1 + n)分配，但源字符串oldp + bd.textcol + bd.t... |
| 787 | vim-9.1.1591 | op_replace | cpp/unbounded-write | 1308 | TP | TP | 代码中直接使用STRCPY（即strcpy）将源字符串复制到目标缓冲区，未检查目标缓冲区大小，且源字符串长度可能超过目标缓冲区分配的大小（oldlen + 1 + n），存在缓冲区溢出风险。 |
| 788 | vim-9.1.1591 | op_delete | cpp/unbounded-write | 962 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将源字符串复制到新分配的目标缓冲区，未检查源字符串长度是否小于目标缓冲区大小，存在缓冲区溢出风险。 |
| 785 | vim-9.1.1591 | op_change | cpp/unbounded-write | 2003 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将源字符串复制到新分配的缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中可见newp缓冲区大小基于ml_get_len(linenr) + vpos.coladd + ins_le... |
| 790 | vim-9.1.1591 | option_value2string | cpp/unbounded-write | 8459 | TP | TP | 代码中直接使用不安全的strcpy宏（STRCPY）将get_special_key_name等函数的返回值复制到固定大小的缓冲区NameBuff，未检查源字符串长度，存在缓冲区溢出风险。 |
| 789 | vim-9.1.1591 | block_insert | cpp/unbounded-write | 743 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串oldp复制到固定缓冲区newp的偏移位置，存在缓冲区溢出的风险。切片中未显示对oldp长度的检查或对目标缓冲区剩余空间的验证。 |
| 791 | vim-9.1.1591 | option_value2string | cpp/unbounded-write | 8461 | TP | TP | 代码在多个分支中直接使用不安全的STRCPY（即strcpy）将数据复制到固定大小的NameBuff缓冲区，且切片中未显示对源字符串长度进行任何边界检查，存在缓冲区溢出风险。 |
| 792 | vim-9.1.1591 | stropt_expand_envvar | cpp/unbounded-write | 1803 | TP | TP | 代码使用strcpy将长度不确定的字符串s复制到newval缓冲区，而newval的大小仅根据s和origval的长度计算，未考虑strcpy不检查目标缓冲区大小的固有风险，存在缓冲区溢出的可能性。 |
| 794 | vim-9.1.1591 | mch_FullName | cpp/unbounded-write | 2846 | TP | TP | 代码使用STRCPY（即strcpy）将fname复制到缓冲区buf中，未检查fname的长度是否超过目标缓冲区剩余空间（len - buflen），存在缓冲区溢出风险。切片中未显示对fname长度的前置校验。 |
| 796 | vim-9.1.1591 | reg_submatch | cpp/unbounded-write | 2723 | TP | TP | 代码在多个位置使用STRCPY（即strcpy）宏，将长度未知的源字符串（如来自reg_getline_submatch的返回值）复制到固定大小的缓冲区retval中，而retval的大小仅由alloc(len)分配，但复制前未确保目... |
| 795 | vim-9.1.1591 | qf_store_title | cpp/unbounded-write | 1940 | TP | TP | 代码使用strcpy将外部传入的title字符串复制到新分配的内存中，虽然分配的大小为STRLEN(title)+2，但strcpy本身不检查目标缓冲区大小，若title字符串未以空字符结尾或分配函数alloc_id失败返回NULL，... |
| 793 | vim-9.1.1591 | mch_expand_wildcards | cpp/unbounded-write | 7445 | TP | TP | 代码在行 `STRCPY(p, (*file)[i]);` 处使用 `strcpy` 将文件路径复制到新分配的缓冲区 `p` 中。`p` 的大小为 `STRLEN((*file)[i]) + 1 + dir`，而源字符串 `(*fil... |
| 797 | vim-9.1.1591 | reg_submatch | cpp/unbounded-write | 2732 | TP | TP | 代码在多个位置使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区retval中，而retval的大小仅由alloc(len)分配，len的计算依赖于外部输入（如匹配位置），无法保证目标缓冲区足够大以容纳源字... |
| 798 | vim-9.1.1591 | regtilde | cpp/unbounded-write | 1959 | TP | TP | 代码使用STRCPY（即strcpy）将postfix复制到tmpsub缓冲区，其目标缓冲区大小tmpsublen+1由alloc分配，但postfix长度postfixlen未在切片中显示受控，且STRCPY调用未使用长度限制，存在... |
| 800 | vim-9.1.1591 | get_reg_contents | cpp/unbounded-write | 2743 | TP | TP | 代码使用STRCPY宏（即strcpy）将y_current->y_array[i].string复制到目标缓冲区retval + len，但目标缓冲区大小由alloc(len + 1)分配，而源字符串长度来自y_current->y... |
| 799 | vim-9.1.1591 | match_with_backref | cpp/unbounded-write | 1600 | TP | TP | 代码使用STRCPY（即strcpy）将rex.line复制到reg_tofree，而reg_tofree的大小基于STRLEN(rex.line) + 50分配。若rex.line在分配后、复制前被其他代码修改并增长，或存在并发修改... |
| 801 | vim-9.1.1591 | do_put | cpp/unbounded-write | 2166 | TP | TP | 切片代码中直接使用STRCPY宏（即strcpy）将y_array[y_size - 1].string复制到缓冲区newp，未检查目标缓冲区大小，且源字符串长度来自用户可控的yank寄存器，存在缓冲区溢出风险。 |
| 803 | vim-9.1.1591 | op_yank | cpp/unbounded-write | 1318 | TP | TP | 代码使用STRCPY（即strcpy）宏进行字符串拼接，未检查目标缓冲区大小，且源字符串长度来自动态分配的字符串，存在缓冲区溢出风险。 |
| 804 | vim-9.1.1591 | op_yank | cpp/unbounded-write | 1319 | TP | TP | 代码使用STRCPY宏（即strcpy）拼接两个字符串，目标缓冲区pnew的大小为两个源字符串长度之和加1，但strcpy不检查边界，若任一源字符串未正确以空字符结尾，将导致缓冲区溢出。切片中未显示对源字符串内容的验证。 |
| 802 | vim-9.1.1591 | do_put | cpp/unbounded-write | 2167 | TP | TP | 切片代码中直接使用了不安全的 STRCPY 宏（即 strcpy），将 y_array[i].string 复制到固定大小的缓冲区 newp 中，而 y_array[i].string 的长度 yanklen 可能超过目标缓冲区剩余空... |
| 805 | vim-9.1.1591 | stuff_yank | cpp/unbounded-write | 471 | TP | TP | 代码使用STRCPY（即strcpy）将源字符串复制到固定大小的缓冲区tmp中，而tmp的大小由tmplen+1决定，但源字符串pp->string的长度未知且未在切片中显示有边界检查，存在缓冲区溢出风险。 |
| 806 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2850 | TP | TP | 代码使用strcat拼接字符串，目标缓冲区scriptname的大小为STRLEN(name)+14，但拼接的源字符串长度可能超过此大小，导致缓冲区溢出。切片中未显示对name长度的前置校验或安全防护。 |
| 807 | vim-9.1.1591 | ExpandPackAddDir | cpp/unbounded-write | 1321 | TP | TP | sprintf 使用未经验证的用户输入 `pat` 作为格式化字符串的一部分，目标缓冲区 `s` 的大小为 `pat_len + 26`，但格式化后的字符串长度可能超过此大小，存在缓冲区溢出风险。 |
| 808 | vim-9.1.1591 | sign_jump | cpp/unbounded-write | 1313 | TP | TP | sprintf 使用未限制长度的缓冲区 buf->b_fname 作为输入，且目标缓冲区 cmd 的大小仅基于该输入的长度计算，未考虑格式化字符串 'e +%ld ' 的额外长度，存在缓冲区溢出风险。 |
| 809 | vim-9.1.1591 | dump_word | cpp/unbounded-write | 4187 | TP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或外部数据（如环境变量、文件读取内容），且切片中未显示对p的长度进行任何校验，存在缓冲区溢出风险。 |
| 810 | vim-9.1.1591 | make_case_word | cpp/unbounded-write | 3140 | TP | TP | 切片代码显示，当 flags 不满足 WF_ALLCAP 或 WF_ONECAP 时，直接使用 STRCPY（即 strcpy）将 fword 复制到 cword，未对源字符串长度和目标缓冲区大小进行任何检查。cword 缓冲区大小未... |
| 811 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2998 | TP | TP | 代码使用STRCPY宏（即strcpy）将repl_to字符串复制到新分配的内存p中，未检查目标缓冲区大小。p的大小基于ml_get_curline_len() + addlen + 1计算，但repl_to的长度可能超过为它分配的空... |
| 812 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2999 | TP | TP | 代码使用 STRCAT（即 strcat）将源字符串拼接到目标缓冲区 p 中，但 p 的大小是基于 ml_get_curline_len() + addlen + 1 分配的，而 STRCAT 的源字符串长度未经验证，可能导致缓冲区溢... |
| 814 | vim-9.1.1591 | spell_load_lang | cpp/unbounded-write | 1632 | TP | TP | 代码使用STRCPY（即strcpy）将参数lang复制到固定大小的数组sl.sl_lang中，但切片未显示对lang长度的任何检查或限制，存在缓冲区溢出风险。 |
| 813 | vim-9.1.1591 | count_common_word | cpp/unbounded-write | 1919 | TP | TP | 代码使用STRCPY（即strcpy）将长度未知的字符串p复制到新分配的内存wc->wc_word中，分配的大小基于STRLEN(p)，但strcpy在遇到源字符串中的空字符前会持续复制，若p未正确以空字符结尾，将导致缓冲区溢出。切片... |
| 815 | vim-9.1.1591 | spell_move_to | cpp/unbounded-write | 1420 | TP | TP | 代码使用 STRCPY（即 strcpy）将 `line` 复制到 `buf`，而 `buf` 的大小基于 `len + MAXWLEN + 2` 分配。由于 `line` 来自缓冲区内容，其长度 `len` 可能超过 `buf` 的... |
| 817 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2369 | TP | TP | 代码使用STRCAT宏（即strcat）将items[0]和items[1]拼接到缓冲区p中，而p的大小仅根据spin->si_info、items[0]和items[1]的长度计算，未考虑strcat可能导致的缓冲区溢出风险。 |
| 818 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2371 | TP | TP | 代码使用STRCAT宏（即strcat）将items[1]拼接到指针p指向的缓冲区，而p的缓冲区大小是通过动态计算分配，但未检查拼接后总长度是否超过分配的大小，存在缓冲区溢出的风险。 |
| 819 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2464 | TP | TP | 代码中直接使用STRCPY(p, items[1])将fgets读取的字符串复制到缓冲区，未检查items[1]的长度是否超过目标缓冲区p的大小，存在缓冲区溢出风险。 |
| 820 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2495 | TP | TP | 代码在拼接字符串时使用STRCAT宏（即strcat），目标缓冲区大小未知，且输入来自外部文件读取（fgets），存在缓冲区溢出风险。 |
| 822 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2746 | TP | TP | 代码中使用 sprintf 将用户控制的 items[4] 拼接到固定大小的缓冲区 buf 中，未检查长度，存在缓冲区溢出风险。 |
| 821 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2644 | TP | TP | 代码使用STRCPY宏（即strcpy）将items[1]复制到p指向的缓冲区，而p指向的缓冲区大小仅为STRLEN(items[1]) + 2，未对源字符串长度进行限制。由于items[1]来自外部文件读取的未经验证的行，可能导致目... |
| 823 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2748 | TP | TP | 代码中使用 sprintf 将 items[4] 直接格式化到固定大小的缓冲区 buf 中，而 items[4] 来源于外部文件读取的未经验证的行数据，可能导致缓冲区溢出。 |
| 824 | vim-9.1.1591 | add_sound_suggest | cpp/unbounded-write | 3243 | TP | TP | 代码使用STRCPY（即strcpy）将goodword复制到新分配的内存中，但分配大小仅基于goodword的长度（STRLEN(goodword) + 1），未检查目标缓冲区sft->sft_word的大小，若goodword长度... |
| 825 | vim-9.1.1591 | suggest_try_change | cpp/unbounded-write | 1199 | TP | TP | 代码使用STRCPY宏（即strcpy）将su->su_fbadword复制到固定大小的缓冲区fword[MAXWLEN]中，未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 827 | vim-9.1.1591 | concat_str | cpp/unbounded-write | 794 | TP | TP | 函数`concat_str`使用`strcpy`复制未知长度的源字符串（`str1`和`str2`）到新分配的内存中。虽然目标缓冲区大小是根据源字符串长度计算分配的，但`strcpy`本身不检查边界，若传入的字符串未以空字符结尾（不符... |
| 829 | vim-9.1.1591 | expand_tag_fname | cpp/unbounded-write | 4141 | TP | TP | 代码使用不安全的STRCPY（即strcpy）将tag_fname复制到固定大小的缓冲区retval（大小为MAXPATHL），而tag_fname的来源包括环境变量、文件读取等外部输入，未进行长度检查，存在缓冲区溢出风险。 |
| 832 | vim-9.1.1591 | findtags_add_match | cpp/unbounded-write | 2704 | TP | TP | 切片代码中多次使用STRCPY（即strcpy）宏，将长度未知的源字符串（如st->tag_fname、st->ebuf、st->lbuf）复制到固定大小的缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 830 | vim-9.1.1591 | get_tagfname | cpp/unbounded-write | 3436 | TP | TP | 代码在行 'STRCPY(buf, fname);' 处使用 strcpy 宏（即标准库 strcpy）将 vim_findfile 返回的字符串 fname 复制到缓冲区 buf 中，而 buf 的大小为 MAXPATHL。虽然 v... |
| 831 | vim-9.1.1591 | findtags_add_match | cpp/unbounded-write | 2625 | TP | TP | 代码使用STRCPY宏（即strcpy）将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未显示对源字符串长度的验证或安全复制机制。 |
| 833 | vim-9.1.1591 | show_one_termcode | cpp/unbounded-write | 7054 | TP | TP | 代码使用不安全的strcpy函数将get_special_key_name返回的字符串复制到固定大小的IObuff缓冲区中，且切片中未显示对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 835 | vim-9.1.1591 | uc_check_code | cpp/unbounded-write | 1810 | TP | TP | 代码在多个分支中直接使用STRCPY（即strcpy）将外部输入（如eap->arg、*split_buf）复制到固定大小的缓冲区buf中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 837 | vim-9.1.1591 | alloc_ufunc | cpp/unbounded-write | 728 | TP | TP | 代码使用不安全的strcpy函数，将长度不确定的源字符串'name'复制到固定大小的目标缓冲区fp->uf_name中，存在缓冲区溢出风险。切片显示目标缓冲区大小由namelen计算，但未对源字符串长度进行验证或限制。 |
| 834 | vim-9.1.1591 | current_tagblock | cpp/unbounded-write | 1392 | TP | TP | 代码使用`sprintf`将用户控制的字符串`p`（来自缓冲区）和长度`len`写入固定大小的缓冲区`spat`和`epat`，而缓冲区大小仅基于`len`计算，未限制`len`的最大值，存在缓冲区溢出风险。 |
| 836 | vim-9.1.1591 | fname_trans_sid | cpp/unbounded-write | 2278 | TP | TP | 代码在条件`fnamelen < FLEN_FIXED`下，使用STRCPY（即strcpy）将`script_name`复制到`fname_buf + fname_buflen`处，但目标缓冲区`fname_buf`的大小为`FLE... |
| 839 | vim-9.1.1591 | generate_PUSHFUNC | cpp/unbounded-write | 1042 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证的字符串name复制到固定大小的缓冲区funcname中，而funcname的大小仅基于STRLEN(name)+3分配，未对源字符串长度进行限制，存在缓冲区溢出风险。 |
| 840 | vim-9.1.1591 | update_vim9_script_var | cpp/unbounded-write | 947 | TP | TP | 代码使用STRCPY（即strcpy）将变量`name`复制到新分配的内存`newsav->sav_key`中，而`name`是函数参数，其来源在切片中未显示任何验证或长度限制。目标缓冲区大小仅为`STRLEN(name) + 1`，... |
| 841 | vim-9.1.1591 | find_exported | cpp/unbounded-write | 756 | TP | TP | 代码使用`sprintf`将外部可控的`script->sn_autoload_prefix`和`name`拼接到固定大小的缓冲区`funcname`中，而`funcname`可能是指向栈上小数组`buffer[200]`的指针，当拼... |
| 842 | vim-9.1.1591 | find_exported | cpp/unbounded-write | 763 | TP | TP | 代码使用`sprintf`将外部输入（`sid`和`name`）写入固定大小的缓冲区`funcname`，而`funcname`可能是指向栈上小数组`buffer`的指针，当拼接后的字符串长度超过目标缓冲区大小时会导致缓冲区溢出。切片... |
| 843 | vim-9.1.1591 | xxdline | cpp/unbounded-write | 600 | TP | TP | 函数`xxdline`中的`strcpy(z, l)`调用，目标缓冲区`z`是固定大小的静态数组`z[LLEN_NO_COLOR+1]`，而源字符串`l`是函数参数，其内容未在切片代码中进行任何长度校验或限制。根据告警信息，`l`可能... |
| 844 | vim-9.1.1591 | ExpandBufnames | cpp/invalid-pointer-deref | 2980 | TP | TP | 在切片代码中，`(*file)[count++] = p;` 这一行存在越界写入风险。`*file` 指针在循环第一轮（round == 1）时可能为 NULL，且仅在 `round == 1` 且 `!fuzzy` 时才会分配内存。... |
| 838 | vim-9.1.1591 | exec_instructions | cpp/unbounded-write | 3929 | TP | TP | 代码在 ISN_EXECCONCAT 指令中使用 STRCPY 宏（即 strcpy）将多个字符串拼接，目标缓冲区 cmd 的长度通过累加源字符串长度计算后分配，但若累加长度计算错误或源字符串长度在两次循环间发生变化，可能导致缓冲区溢... |
| 845 | vim-9.1.1591 | update_snapshot | cpp/invalid-pointer-deref | 2075 | TP | TP | 当 width 为 2 时，代码执行 p[pos.col + 1] = p[pos.col]; 但 p 是通过 ALLOC_MULT(cellattr_T, len) 分配的，长度为 len。若 pos.col 等于 len-1，则 ... |
| 1583 | redis-7.2.5 | auxHumanNodenameSetter | Dereference of null pointer | 281 | TP | TP | 当指针 n 为 NULL 时，代码在 else if 条件中直接调用 sdslen(n->human_nodename)，这会导致对空指针 n 进行解引用，属于明确的空指针解引用逻辑错误。 |

### 5.2 一致：算法=FP，LLM=FP（共 1405 条）

> 算法与 LLM 均判定为假阳性（False Positive）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 2 | ffmpeg-6.1.1 | capture_screen | cpp/offset-use-before-range-check | 479 | FP | FP | 告警所在行的while循环条件已包含'j < tab'的范围检查，确保j不会越界访问数组。切片代码显示j的初始化和递增逻辑安全，不存在越界风险。 |
| 3 | ffmpeg-6.1.1 | capture_screen | cpp/offset-use-before-range-check | 479 | FP | FP | 在while循环条件中，对变量j的访问已包含边界检查'j < tab'，且tab的值由前一个循环计算得出，确保j在访问数组前不会越界。 |
| 4 | ffmpeg-6.1.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码显示，在警告所在行 `for(; (((x86_reg)&dst[i]) & 0x1F) && i<w_r; i++){` 中，对索引 `i` 的使用（`dst[i]`）之前已经通过 `i<w_r` 条件进行了范围检查，确保了... |
| 5 | ffmpeg-6.1.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警行使用变量 `i` 之前，循环条件 `i<w_r` 已经对其进行了范围检查，确保了 `i` 在有效范围内，因此不存在越界访问风险。 |
| 7 | ffmpeg-6.1.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 215 | FP | FP | 切片代码显示，在循环条件 `i < q->nb_subs` 的保护下，对 `q->subs[i]` 和 `q->subs[i + 1]` 的访问是安全的。条件 `i < q->nb_subs - 1` 进一步确保了 `i + 1` 不... |
| 9 | ffmpeg-6.1.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部实现仅跳过空格字符，不会返回NULL，因此调用后无需检查NULL。告警是基于统计模式而非实际代码语义的误报。 |
| 8 | ffmpeg-6.1.1 | choose_out_timebase | cpp/inconsistent-null-check | 1850 | FP | FP | 函数 frame_data 在传入的 frame->opaque_ref 为空时会分配内存并返回指针，仅在分配失败时返回 NULL。切片代码中，frame 作为参数传入，其 opaque_ref 可能已由上游调用者初始化，且后续代码直... |
| 11 | ffmpeg-6.1.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1392 | FP | FP | 函数 `ff_framequeue_peek` 内部已通过 `av_assert1(idx < fq->queued)` 确保索引有效，且调用前 `ff_inlink_check_available_frame` 已确认队列非空，因此... |
| 14 | ffmpeg-6.1.1 | init_muxer | cpp/inconsistent-null-check | 189 | FP | FP | ffofmt 是一个简单的内联转换函数，仅执行指针类型转换，不会返回空指针。因此，调用结果不需要进行空指针检查，告警属于误报。 |
| 16 | ffmpeg-7.1.1 | upcase_string | cpp/offset-use-before-range-check | 1109 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了在访问 `src[i]` 和 `dst[i]` 之前，`i` 已通过 `i < dst_size-1` 进行了范围检查，因此不存在偏移量在范围检查前使用的问题。 |
| 17 | ffmpeg-7.1.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在循环条件 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 中，对变量 `j` 的访问已通过 `j < tab` 进行了范围检查，确保了... |
| 18 | ffmpeg-7.1.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警行 'while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)' 中，变量 'j' 在循环条件中已与 'tab' 进行了范围检查，且 'tab'... |
| 12 | ffmpeg-6.1.1 | intercept_id3 | cpp/inconsistent-null-check | 1185 | FP | FP | 函数 `current_segment` 在切片中被调用后，其返回值 `seg` 被直接传递给 `read_from_url` 等函数使用，但后续代码在使用 `seg->size` 前未检查 `seg` 是否为 NULL。然而，`re... |
| 19 | ffmpeg-7.1.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码显示，在告警所在的for循环条件中，变量'i'的使用（`i<w_r`）与对其地址的对齐检查（`((x86_reg)&dst[i]) & 0x1F`）是同时进行的，这构成了一个隐式的范围检查，确保了在访问`dst[i]`之前'i... |
| 20 | ffmpeg-7.1.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警行使用变量 `i` 的循环条件 `i<w_r` 中，`i` 的初始值为0，且 `w_r` 在函数开头定义为 `w2 - 1`，这是一个非负的确定值。循环条件 `i<w_r` 本身就是一个范围检查，确保了 `i` 在... |
| 22 | ffmpeg-7.1.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 223 | FP | FP | 切片代码显示，在循环条件 `i < q->nb_subs` 的保护下，对 `q->subs[i]` 和 `q->subs[i + 1]` 的访问是安全的。`i + 1` 的访问仅在 `i < q->nb_subs - 1` 的条件下进... |
| 24 | ffmpeg-7.1.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部没有失败路径，它只是跳过空格并返回移动后的指针，不会返回NULL。因此，调用后无需检查NULL，告警是误报。 |
| 26 | ffmpeg-7.1.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1461 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 29 | ffmpeg-7.1.1 | init_muxer | cpp/inconsistent-null-check | 190 | FP | FP | ffofmt 是一个简单的内联类型转换函数，它直接返回转换后的指针，不会返回 NULL。因此，调用 ffofmt 的结果不需要进行空指针检查，告警属于误报。 |
| 27 | ffmpeg-7.1.1 | hls_read_header | cpp/inconsistent-null-check | 2158 | FP | FP | 切片代码显示，`in_fmt` 变量在后续的 `avformat_open_input` 调用中被直接使用，但该调用会检查返回值，且 `in_fmt` 为 NULL 时 `avformat_open_input` 本身能处理。此外，`... |
| 28 | ffmpeg-7.1.1 | intercept_id3 | cpp/inconsistent-null-check | 1240 | FP | FP | 函数 `current_segment` 在切片中已定义，其返回值仅在 `seg->size` 处被解引用。该解引用操作位于 `seg->size >= 0` 的条件判断中，即使 `seg` 为 NULL，`seg->size` 的访... |
| 33 | ffmpeg-7.0.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警所在行的while循环条件中，已经明确包含了'j < tab'的范围检查，确保j不会超出tab的值。切片代码显示tab的值由前一个循环计算得出，且j的初始化和递增逻辑均在受控范围内，因此不存在越界访问风险。 |
| 35 | ffmpeg-7.0.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码显示，在告警行使用变量 `i` 之前，循环条件 `i<w_r` 已经对其进行了范围检查，确保了 `i` 在访问数组 `dst` 时是安全的。 |
| 34 | ffmpeg-7.0.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在`while`循环条件`j < tab`中，变量`j`在循环体中被使用前已经与`tab`进行了范围比较，确保了`j`不会超过`tab`。切片代码显示`tab`的值由第一个循环计算得出，且`j`的初始值为0并在循环中递增，因此不存在越... |
| 36 | ffmpeg-7.0.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警所在的for循环条件中，变量'i'的使用（`i<w_r`）与范围检查（`i<w_r`）是同时进行的，且循环体内部没有对'i'进行可能导致越界的修改。因此，'i'的使用是在有效的范围检查保护之下的，不存在先于范围检查... |
| 39 | ffmpeg-7.0.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部没有返回NULL的路径，它仅跳过空格并返回一个指针，因此调用后无需检查NULL。告警是基于统计模式而非实际代码逻辑。 |
| 38 | ffmpeg-7.0.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 215 | FP | FP | 切片代码显示，在循环条件 `i < q->nb_subs` 的保护下，访问 `q->subs[i]` 和 `q->subs[i + 1]` 是安全的。对于 `q->subs[i + 1]` 的访问，存在显式的范围检查 `i < q->... |
| 41 | ffmpeg-7.0.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1455 | FP | FP | 函数 `ff_framequeue_peek` 内部包含 `av_assert1(idx < fq->queued);` 断言，确保索引有效且返回的帧指针非空。调用前 `ff_inlink_check_available_frame`... |
| 43 | ffmpeg-7.0.1 | intercept_id3 | cpp/inconsistent-null-check | 1190 | FP | FP | 函数 `current_segment` 的返回值 `seg` 在后续代码中仅作为参数传递给 `read_from_url`，而 `read_from_url` 内部对 `seg->size` 的访问已通过 `if (seg->siz... |
| 42 | ffmpeg-7.0.1 | hls_read_header | cpp/inconsistent-null-check | 2107 | FP | FP | 切片代码显示，`in_fmt` 变量在后续的 `avformat_open_input` 调用中被直接使用，但该函数本身接受 `NULL` 作为有效的输入格式参数。规则检测的是对 `av_find_input_format` 返回值的... |
| 45 | ffmpeg-7.0.1 | init_muxer | cpp/inconsistent-null-check | 189 | FP | FP | ffofmt 是一个简单的内联类型转换函数，它只是将 AVOutputFormat 指针转换为 FFOutputFormat 指针，不会返回 NULL。因此，对它的返回值进行空指针检查是多余的，工具报告的告警是误报。 |
| 49 | ffmpeg-7.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在while循环条件中，变量j的使用已包含范围检查'j < tab'，确保j不会超过tab的值，因此不存在越界访问风险。 |
| 48 | ffmpeg-7.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在while循环条件中，变量j的使用已通过'j < tab'进行了范围检查，确保了j不会超出tab的界限，因此不存在越界访问的风险。 |
| 51 | ffmpeg-7.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警所在的循环条件 `i<w_r` 中，变量 `i` 已通过前置的 `for` 循环条件 `i<w_r` 进行了范围检查，确保了循环内对 `temp[i]` 的访问是安全的。 |
| 50 | ffmpeg-7.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码显示，在循环条件 `(((x86_reg)&dst[i]) & 0x1F) && i<w_r` 中，对索引 `i` 的使用（`&dst[i]`）与范围检查 `i<w_r` 位于同一条件表达式中，且逻辑与运算符 `&&` 确保了... |
| 53 | ffmpeg-7.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 223 | FP | FP | 在for循环条件`i < q->nb_subs`的保护下，循环体内对`q->subs[i]`和`q->subs[i + 1]`的访问是安全的。条件`i < q->nb_subs - 1`确保了`i + 1`不会越界，因此不存在偏移量在... |
| 55 | ffmpeg-7.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部没有返回空指针的路径，它只是移动指针并返回一个非空指针（即使输入为空字符串，也返回指向字符串终止符的指针）。因此，检查其返回值是否为NULL是多余的，工具报告的“未检查null”是误报。 |
| 54 | ffmpeg-7.1 | enc_open | cpp/inconsistent-null-check | 189 | FP | FP | 告警点对av_frame_side_data_desc的返回值进行了间接检查。代码在访问desc->props前，先检查了desc->props & AV_SIDE_DATA_PROP_GLOBAL，这隐含了desc不为NULL的前提... |
| 57 | ffmpeg-7.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1461 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有 `av_assert1(idx ... |
| 61 | ffmpeg-7.1 | init_muxer | cpp/inconsistent-null-check | 190 | FP | FP | ffofmt 是一个简单的内联类型转换函数，它只是将 AVOutputFormat 指针转换为 FFOutputFormat 指针，不会返回 NULL。因此，对它的返回值进行空值检查是多余的，工具报告的告警是误报。 |
| 58 | ffmpeg-7.1 | hls_read_header | cpp/inconsistent-null-check | 2109 | FP | FP | 切片代码显示，`in_fmt` 变量在后续的 `avformat_open_input` 调用中仅作为参数传递，该函数内部会处理 NULL 输入格式的情况。此外，`in_fmt` 的赋值来源是 `av_find_input_forma... |
| 65 | ffmpeg-6.0 | capture_screen | cpp/offset-use-before-range-check | 485 | FP | FP | 在while循环条件中，变量j的使用已通过'j < tab'进行了范围检查，确保j不会超出tab的边界，因此不存在越界访问的风险。 |
| 66 | ffmpeg-6.0 | capture_screen | cpp/offset-use-before-range-check | 485 | FP | FP | 在告警行 'while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)' 中，变量 'j' 在循环条件中已与 'tab' 进行了范围检查，确保了 'j ... |
| 69 | ffmpeg-6.0 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部没有返回NULL的路径，它只是跳过空格并返回一个指针，因此调用后无需检查NULL。告警是基于统计模式而非实际代码逻辑。 |
| 68 | ffmpeg-6.0 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 207 | FP | FP | 切片代码显示，在循环条件 `i < q->nb_subs` 的保护下，对 `q->subs[i]` 和 `q->subs[i + 1]` 的访问是安全的。`i + 1` 的访问仅在 `i < q->nb_subs - 1` 的条件下进... |
| 71 | ffmpeg-6.0 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1373 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有 `av_assert1(idx ... |
| 74 | ffmpeg-6.0 | init_muxer | cpp/inconsistent-null-check | 185 | FP | FP | ffofmt 是一个简单的内联转换函数，仅执行指针类型转换，不会返回空指针。因此，调用结果不需要进行空值检查，告警属于误报。 |
| 75 | ffmpeg-6.0 | url_alloc_for_protocol | cpp/unbounded-write | 102 | FP | FP | 目标缓冲区 `uc->filename` 的大小通过 `strlen(filename) + 1` 精确分配，`strcpy` 操作不会导致缓冲区溢出。 |
| 76 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1194 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后检查新分配的内存是否为 NULL，若不为空才进行解引用和赋值操作... |
| 78 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1196 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，并且新分配的内存地址已正确赋值给sc->ext.session_ticket->data，不存在对已释放内存的访问。 |
| 72 | ffmpeg-6.0 | intercept_id3 | cpp/inconsistent-null-check | 1184 | FP | FP | 函数 `current_segment` 的返回值 `seg` 在后续代码中仅作为参数传递给 `read_from_url`，而 `read_from_url` 内部对 `seg` 的使用是安全的（通过 `FFMIN` 进行边界检查，... |
| 79 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1196 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且新分配的内存地址已赋值给sc->ext.session_ticket->data，不存在对已释放内存的访问。 |
| 77 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1195 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后，`sc->ext.session_ticket` 被重新分配了... |
| 80 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1198 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后对新分配的内存进行条件检查，只有在分配成功后才进行后续操作，不存... |
| 81 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1199 | FP | FP | 切片代码显示，在将`sc->ext.session_ticket->data`赋值为NULL之前，已经通过`OPENSSL_free`释放了旧指针并分配了新内存，新分配的内存指针被赋值给`sc->ext.session_ticket`... |
| 82 | openssl-openssl-3.5.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1729 | FP | FP | 切片代码显示，在调用memcmp比较s->session->ext.alpn_selected和s->s3.alpn_selected之前，s->s3.alpn_selected已通过OPENSSL_malloc分配了内存，并且没有在... |
| 84 | openssl-openssl-3.5.1 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 告警指出的空指针检查是必要的，因为`keySpec`指针在函数中可能被重新赋值（例如在循环中分配内存），后续的`sk_OSSL_CMP_ATAV_pop_free`调用会释放该内存并将其置为NULL，因此最后的`if (keySpec... |
| 85 | openssl-openssl-3.5.1 | <global> | cpp/offset-use-before-range-check | 266 | FP | FP | 循环条件 `src[i] != '\0' && i < len` 已确保索引 `i` 在访问 `src[i]` 和 `tgt[i]` 前会先检查 `i < len`，且 `src` 为 NULL 时函数已提前返回，因此不存在越界访问风险。 |
| 87 | openssl-openssl-3.5.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 345 | FP | FP | 切片代码中，在调用 CRYPTO_THREAD_get_local 后，立即使用 `assert(data != NULL);` 对返回值进行了非空断言，这确保了后续代码路径中 data 不为空，因此该告警为误报。 |
| 86 | openssl-openssl-3.5.1 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 切片代码显示，变量'i'在for循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'中被使用，但该使用点本身包含了范围检查'i < (maskedDBLen - 1)'，确保了'i'在访问DB数组时不会越... |
| 92 | openssl-openssl-3.5.1 | <global> | cpp/unbounded-write | 30 | FP | FP | 函数CRYPTO_strdup在调用strcpy前，已通过CRYPTO_malloc分配了strlen(str) + 1大小的内存，目标缓冲区大小与源字符串长度精确匹配，不存在缓冲区溢出的风险。 |
| 90 | openssl-openssl-3.5.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 获取 `f` 后，代码立即在 `if (start <= f->range.start && end >= z->range.end)` 中解引用 `f->range.... |
| 93 | openssl-openssl-3.5.1 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码显示，在调用strcpy之前，函数已通过`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 94 | openssl-openssl-3.5.1 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码中，在调用strcpy之前，已通过条件`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 96 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3468 | FP | FP | 告警提示的宏 QUIC_RAISE_NON_NORMAL_ERROR 在切片中已明确定义，其参数列表以 `(msg)` 结尾，没有使用可变参数，因此不存在未终止的可变参数调用问题。这是工具对宏展开的误判。 |
| 97 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3477 | FP | FP | 告警指出的调用是宏 `QUIC_RAISE_NON_NORMAL_ERROR` 的展开，该宏已正确提供了 `reason` 和 `msg` 两个参数，符合其定义。切片中未显示该宏或底层函数 `quic_raise_non_normal... |
| 98 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3487 | FP | FP | 告警指出的QUIC_RAISE_NON_NORMAL_ERROR宏调用已正确传递了三个参数（ctx, reason, msg），符合其定义。切片中未发现可变参数（variadic）调用的错误终止符问题，该告警是基于统计模式（112次调... |
| 100 | openssl-openssl-3.5.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3409 | FP | FP | 告警指出的宏 `QUIC_RAISE_NON_NORMAL_ERROR` 调用已正确使用了终止符 `0`。该宏展开为 `quic_raise_non_normal_error` 函数调用，其参数列表在切片中已完整给出，最后一个参数是字... |
| 99 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3493 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数（ctx, reason, msg），与宏定义匹配，不存在未终止的可变参数问题。代码逻辑正确，工具报告是基于统计模式（112次调用中有1... |
| 101 | openssl-openssl-3.5.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3421 | FP | FP | 告警指出的调用是宏 QUIC_RAISE_NON_NORMAL_ERROR 的展开，该宏已固定传递了5个参数给 quic_raise_non_normal_error，符合其函数签名要求，不存在未终止的可变参数问题。 |
| 102 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1846 | FP | FP | 告警指出的宏 QUIC_RAISE_NON_NORMAL_ERROR 在切片代码中被正确使用，其展开为对 quic_raise_non_normal_error 的调用，且提供了所有必需的参数（包括文件、行号、函数名、原因和消息）。切... |
| 103 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1853 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数，与宏定义 `(ctx, reason, msg)` 的参数数量一致，不存在未终止的可变参数调用问题。切片代码显示该宏调用是安全的。 |
| 104 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1861 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确传递了三个参数（ctx, reason, msg），与宏定义 `quic_raise_non_normal_error` 的参数列表匹配。切片中未显示... |
| 105 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 代码使用恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来安全地处理边界条件，确保指针访问不会越界。循环中的 `flen` 递减和 `from` 指针移动... |
| 107 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用恒定时间操作（constant_time_*函数）和掩码（mask）来安全地处理边界条件，循环中的指针运算 `*--em = *from & mask;` 在 `flen` 为0时会被掩码保护，不会发生越界读取。 |
| 106 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中的 `em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，且后续循环 `for (from ... |
| 108 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 `em[0]` 的访问是安全的，因为 `em` 指针指向 `OPENSSL_malloc(num)` 分配的内存块，且循环 `for (from += flen, em += num, i = 0; i < num; i++)... |
| 109 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警指向的数组访问 `em[1]` 是安全的，因为 `em` 指向大小为 `num` 的动态分配内存，且循环 `for (i = 0; i < num; i++)` 确保 `num >= 1`，因此索引 1 在边界内。代码使用常数时间... |
| 110 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1171 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，随后立即分配新内存并检查其是否为 NULL。在 `ext_data != NULL` 的分支中，... |
| 111 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1172 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，随后立即检查了新分配的内存是否为 NULL。警告所指的 `sc->ext.session_tic... |
| 112 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1173 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且已为新分配的sc->ext.session_ticket分配了足够的内存（sizeof(TLS_SESSION_TICKET_EXT) + ext... |
| 113 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1173 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保sc->ext.session_ticket不为NULL，并且分配了足够的内存（sizeof(TLS_SESSION_TICKET_EXT) + ext_len）。因此，对已分配... |
| 114 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1175 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后对新分配的内存进行访问，不存在对已释放内存的访问。告警点位于对新分... |
| 115 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1176 | FP | FP | 切片代码显示，在将 `sc->ext.session_ticket->data` 赋值为 NULL 之前，已经通过 `OPENSSL_malloc` 为新结构体分配了内存，并检查了分配结果。对 `data` 字段的赋值是结构体初始化的... |
| 116 | openssl-openssl-3.3.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1626 | FP | FP | 切片代码显示，在调用memcmp比较`s->session->ext.alpn_selected`和`s->s3.alpn_selected`之前，已通过`OPENSSL_free`释放了`s->s3.alpn_selected`的原... |
| 119 | openssl-openssl-3.3.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 447 | FP | FP | 提供的切片代码显示函数 `ossl_rcu_read_unlock` 为空实现，未调用 `CRYPTO_THREAD_get_local`，因此工具报告的未检查空值的问题在可见代码中不存在，属于误报。 |
| 118 | openssl-openssl-3.3.1 | RSA_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 109 | FP | FP | 切片代码显示，变量'i'在for循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'中被使用，但其值在循环前已通过'for (i = 0; i < maskedDBLen; i++) DB[i] ^= E... |
| 120 | openssl-openssl-3.3.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 无效时返回 NULL，而调用前 `enc_level` 由调用者传入，切片中无证据表明其为... |
| 122 | openssl-openssl-3.3.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 获取 `f` 后，代码立即在 `if (start <= f->range.start ...)` 中解引用 `f->range.start`，这表明代码逻辑假设 `f... |
| 126 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 29 | FP | FP | 函数CRYPTO_strdup在调用strcpy前，已通过CRYPTO_malloc分配了strlen(str) + 1字节的内存，目标缓冲区大小与源字符串长度精确匹配，不存在缓冲区溢出的风险。 |
| 127 | openssl-openssl-3.3.1 | RAND_file_name | cpp/unbounded-write | 309 | FP | FP | 切片代码中，在调用strcpy之前，已通过`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`对目标缓冲区大小进行了严格检查，确保了不会发生缓冲区溢出。 |
| 128 | openssl-openssl-3.3.1 | RAND_file_name | cpp/unbounded-write | 313 | FP | FP | 切片代码显示，在调用strcpy之前，函数已通过`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 130 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3131 | FP | FP | 告警指出的宏调用 QUIC_RAISE_NON_NORMAL_ERROR 已正确使用了 NULL 作为可变参数的终止符，符合规则要求。切片代码显示该调用格式正确，不存在未终止的可变参数调用问题。 |
| 133 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3156 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数（ctx, reason, msg），其中最后一个参数 `msg` 是一个字符串字面量，符合宏定义的要求。切片代码中未发现未终止的可变参... |
| 134 | openssl-openssl-3.3.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3072 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数（reason 和 msg），切片中未发现其作为可变参数函数被错误终止的用法，且该宏展开后调用 `quic_raise_non_norm... |
| 132 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3150 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_INTERNAL_ERROR, "ref")` 提供了三个参数，与宏定义 `(ctx, reason, msg)` 完全匹配，不存在未... |
| 131 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3140 | FP | FP | 告警指出的调用点 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_SHOULD_NOT_HAVE_BEEN_CALLED, "connection already has a default stre... |
| 137 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1551 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数，与宏定义 `(ctx, reason, msg)` 的参数数量一致，不存在未终止的可变参数调用问题。代码片段中所有对该宏的调用都是安全的。 |
| 136 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1544 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了 `0` 作为终止符，因为其展开后的函数 `quic_raise_non_normal_error` 是一个固定参数函数，而非可变参数函数。切片... |
| 138 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1561 | FP | FP | 告警指出的宏调用 QUIC_RAISE_NON_NORMAL_ERROR 已提供了三个参数（ctx, reason, msg），符合其定义。切片中未发现任何可变参数列表（variadic arguments）的使用，因此不存在未终止的... |
| 135 | openssl-openssl-3.3.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3084 | FP | FP | 告警指出的宏 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中被调用时，其参数列表是完整的，并以字符串字面量结尾，这符合C语言可变参数函数的调用规范。切片中未发现该调用缺少必需的终止符（如0）的证据，且该宏展开... |
| 139 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 221 | FP | FP | 切片代码显示，循环访问指针前使用了`mask`变量和`constant_time_is_zero`函数进行边界检查，`flen`的递减和指针`from`的移动受`mask`控制，确保了不会发生越界读取。代码采用了常数时间安全编程模式来... |
| 141 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 切片代码显示，循环访问指针 'from' 和 'em' 时使用了掩码 'mask' 进行条件控制，该掩码由 constant_time_is_zero(flen) 计算得出，确保在 flen 耗尽后不会进行越界读取。代码采用了常数时间... |
| 140 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 229 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 处的指针 `em` 已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，且后续循环 `for (from ... |
| 142 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 'em[0]' 的访问是安全的，因为 'em' 指针指向由 'OPENSSL_malloc(num)' 分配的内存块起始位置，且循环 'for (i = 0; i < num; i++)' 确保 'em' 在访问前已通过 'e... |
| 146 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保sc->ext.session_ticket不为NULL，且对ext_data进行了非空检查。代码逻辑正确，不存在对已释放内存的访问。 |
| 143 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的。`em` 指向大小为 `num` 的已分配内存，且循环 `for (from += flen, em += num, i = 0; i < num; i++)` 已将 `em` 递减回指向分配区... |
| 144 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1182 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后对新分配的内存进行了空指针检查，访问 `sc->ext.sess... |
| 145 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1183 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，随后立即检查新分配的内存是否为 NULL。`sc->ext.session_ticket->da... |
| 147 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保sc->ext.session_ticket不为NULL，并且分配了内存。告警所指的释放操作是针对旧指针，且在新内存分配成功后才会使用新指针，不存在use-after-free。 |
| 148 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1186 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后对新分配的内存进行访问（如设置 length 和 data），不存... |
| 149 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1187 | FP | FP | 告警指向的代码行 `sc->ext.session_ticket->data = NULL;` 是对新分配内存结构体成员的初始化，并非对已释放内存的再次使用。切片代码显示，在分配 `sc->ext.session_ticket` 后，... |
| 151 | openssl-openssl-3.4.1 | tls_parse_stoc_npn | cpp/use-after-free | 1620 | FP | FP | 切片代码显示，在调用memcpy之前，已通过OPENSSL_free释放了s->ext.npn，并立即通过OPENSSL_malloc重新分配了内存。对同一指针的释放和重新分配是连续且受控的操作，不存在访问已释放内存的风险。 |
| 153 | openssl-openssl-3.4.1 | <global> | cpp/offset-use-before-range-check | 246 | FP | FP | 切片代码显示，在for循环的条件中，对数组索引'i'的使用（src[i]）之前，已经通过'i < len'进行了范围检查，确保了访问的安全性。因此该告警是误报。 |
| 152 | openssl-openssl-3.4.1 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 切片代码显示，在告警行之前的代码路径中，如果 keySpec 不为 NULL，其指向的内存可能已被 sk_OSSL_CMP_ATAV_pop_free 释放并置为 NULL，因此后续的 `if (keySpec != NULL)` 检... |
| 154 | openssl-openssl-3.4.1 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 告警指向的循环条件 'i < (maskedDBLen - 1)' 已包含对变量 i 的范围检查，确保其在访问 DB[i] 之前不会越界。代码逻辑正确，工具误报了顺序问题。 |
| 155 | openssl-openssl-3.4.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 489 | FP | FP | 切片代码中，在调用`CRYPTO_THREAD_get_local`后，立即使用`assert(data != NULL)`对返回值进行了严格的非空断言。这表明代码逻辑明确要求`data`不为空，否则程序将终止。因此，该告警是误报，因... |
| 156 | openssl-openssl-3.4.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 索引越界时返回 NULL，而调用前 `enc_level` 已由上层逻辑保证有效。后续代码... |
| 160 | openssl-openssl-3.4.1 | <global> | cpp/unbounded-write | 30 | FP | FP | 函数CRYPTO_strdup在调用strcpy前，已通过CRYPTO_malloc分配了strlen(str) + 1大小的内存，目标缓冲区大小与源字符串长度精确匹配，不存在缓冲区溢出的风险。 |
| 161 | openssl-openssl-3.4.1 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码显示，在调用strcpy前已通过`len + 1 >= size`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 162 | openssl-openssl-3.4.1 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码中，在调用strcpy之前，已通过条件`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，确保不会发生缓冲区溢出。 |
| 158 | openssl-openssl-3.4.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 切片代码显示，在调用`ossl_list_uint_set_head(s)`获取`f`后，立即在条件`if (start <= f->range.start && end >= z->range.end)`中解引用了`f->range... |
| 164 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3149 | FP | FP | 告警提示调用 `quic_raise_non_normal_error` 应使用 0 作为终止符，但切片代码显示该调用是通过宏 `QUIC_RAISE_NON_NORMAL_ERROR` 进行的，该宏的展开格式固定，其最后一个参数 `... |
| 165 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3158 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数（reason 和 msg），其展开后的函数 `quic_raise_non_normal_error` 的变参部分由宏定义保证以 `N... |
| 166 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3168 | FP | FP | 告警指出的调用 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_INTERNAL_ERROR, "ref")` 符合宏定义，其最后一个参数 `"ref"` 是一个字符串字面量，并非可变参数列表，因此不... |
| 167 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3174 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数（reason 和 msg），其展开后的函数 `quic_raise_non_normal_error` 是一个可变参数函数，但切片中该... |
| 168 | openssl-openssl-3.4.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3090 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了终止符0，因为其展开后的函数 `quic_raise_non_normal_error` 是一个固定参数函数，并非可变参数函数，因此不存在未终止... |
| 169 | openssl-openssl-3.4.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3102 | FP | FP | 告警指出的宏 QUIC_RAISE_NON_NORMAL_ERROR 在展开时，其最后一个参数 'msg' 是一个字符串字面量，并非可变参数列表。该宏的定义和调用方式固定，不会导致未终止的可变参数调用问题。 |
| 171 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1553 | FP | FP | 宏 QUIC_RAISE_NON_NORMAL_ERROR 的展开显示其调用 quic_raise_non_normal_error 时，变参部分 (msg) 是一个字符串字面量，并非可变数量的参数，因此不存在未终止的可变参数调用风险。 |
| 170 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1546 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数 `(ctx), (reason), (msg)`，与宏定义 `quic_raise_non_normal_error((ctx), O... |
| 172 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1563 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已提供了三个固定参数，符合其定义 `(ctx), (reason), (msg)`，没有证据表明存在未终止的可变参数调用问题。该告警可能是工具对... |
| 173 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 代码使用了恒定时间操作（constant_time_is_zero, mask等）来安全地处理边界条件，循环中的指针运算和掩码确保了不会发生越界读取。告警点 `*--em = *from & mask;` 在 `flen` 递减和 `... |
| 175 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 切片代码显示，循环访问 `from` 指针时使用了掩码 `mask` 进行条件控制，当 `flen` 减至零时 `mask` 为零，后续访问被安全地屏蔽，不会发生越界读取。代码使用了常数时间操作来确保安全。 |
| 176 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 `em[0]` 的访问是安全的，因为 `em` 指针指向 `OPENSSL_malloc(num)` 分配的内存块起始位置，且循环 `for (from += flen, em += num, i = 0; i < num; ... |
| 174 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 处的指针 `em` 已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，且后续循环 `for (from ... |
| 177 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警指向的 `em[1]` 访问是安全的，因为 `em` 指向 `OPENSSL_malloc(num)` 分配的内存块起始位置，且循环 `for (from += flen, em += num, i = 0; i < num; i... |
| 178 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1138 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后对新分配的内存进行了空指针检查，访问 `sc->ext.sess... |
| 180 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1140 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保sc->ext.session_ticket不为NULL，并且对ext_data进行了非空检查。代码逻辑正确，不存在对已释放内存的访问。 |
| 179 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1139 | FP | FP | 告警指向的指针 `sc->ext.session_ticket->data` 被赋值为 `sc->ext.session_ticket + 1`，这是一个指向新分配内存块内部的指针，并非指向已释放的内存。代码逻辑正确，不存在对已释放内... |
| 181 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1140 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保sc->ext.session_ticket不为NULL，且对ext_data进行了非空检查。代码逻辑正确，不存在对已释放内存的访问。 |
| 183 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1143 | FP | FP | 切片代码显示，在将 `sc->ext.session_ticket->data` 赋值为 NULL 之前，已经通过 `OPENSSL_malloc` 为新结构体分配了内存，并检查了分配结果。`data` 字段被设置为 NULL 是 `... |
| 182 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1142 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，随后立即检查新分配的内存是否为 NULL。在 `ext_data` 为 NULL 的分支中，对 ... |
| 184 | openssl-openssl-3.2.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1626 | FP | FP | 切片代码显示，在调用memcmp比较`s->session->ext.alpn_selected`之前，已通过`OPENSSL_free`释放了`s->s3.alpn_selected`，但随后立即为其重新分配了内存（`OPENSSL... |
| 185 | openssl-openssl-3.2.1 | tls_parse_stoc_npn | cpp/use-after-free | 1581 | FP | FP | 切片代码显示，在调用memcpy之前，已通过OPENSSL_free释放了s->ext.npn，并立即通过OPENSSL_malloc重新分配了内存。这是对同一指针的合法释放后重新分配，并非对已释放内存的非法使用（use-after-... |
| 186 | openssl-openssl-3.2.1 | RSA_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 109 | FP | FP | 告警指向的循环条件 'DB[i] == 0 && i < (maskedDBLen - 1)' 已包含对索引 i 的范围检查，确保 i 在访问 DB[i] 时不会越界。该代码逻辑是安全的，属于工具误报。 |
| 187 | openssl-openssl-3.2.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 无效时返回 NULL，而调用前 `enc_level` 已在 `ossl_qrl_enc_... |
| 189 | openssl-openssl-3.2.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 后，代码立即在 `if (start <= f->range.start && end >= z->range.end)` 中解引用了 `f->range.start`... |
| 194 | openssl-openssl-3.2.1 | RAND_file_name | cpp/unbounded-write | 309 | FP | FP | 切片代码显示，在调用strcpy之前，已通过条件`len + 1 >= size`检查了目标缓冲区大小，确保不会发生溢出。该防护机制使告警无效。 |
| 193 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 29 | FP | FP | 函数CRYPTO_strdup在调用strcpy前，已通过CRYPTO_malloc分配了strlen(str) + 1大小的内存，目标缓冲区大小与源字符串长度精确匹配，不存在缓冲区溢出的风险。 |
| 195 | openssl-openssl-3.2.1 | RAND_file_name | cpp/unbounded-write | 313 | FP | FP | 切片代码显示，在调用strcpy之前，已通过`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，防止了缓冲区溢出。 |
| 198 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3063 | FP | FP | 切片代码显示，宏 QUIC_RAISE_NON_NORMAL_ERROR 的定义明确包含两个参数 `(reason)` 和 `(msg)`，告警点调用时传递了两个参数，与宏定义匹配，不存在未终止的可变参数调用问题。 |
| 197 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3054 | FP | FP | 切片代码显示，宏 QUIC_RAISE_NON_NORMAL_ERROR 的调用格式与规则期望的 variadic 函数调用模式不符，它被定义为固定参数的宏，且切片中未发现其底层函数 'quic_raise_non_normal_er... |
| 199 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3073 | FP | FP | 告警指出的调用是宏 QUIC_RAISE_NON_NORMAL_ERROR 的展开，该宏已正确传递了所有参数（包括一个字符串字面量 msg），并调用了底层函数 quic_raise_non_normal_error。切片中未显示该底层... |
| 200 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3079 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数（reason 和 msg），其展开后的函数 `quic_raise_non_normal_error` 的变参列表由宏定义和调用方式保... |
| 201 | openssl-openssl-3.2.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 2995 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了终止符 `NULL` 作为最后一个参数，符合规则要求。切片代码显示该宏展开为 `quic_raise_non_normal_error` 函数调... |
| 202 | openssl-openssl-3.2.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3007 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了终止符0。从切片代码可见，该宏展开为 `quic_raise_non_normal_error` 函数调用，其最后一个参数 `(msg)` 是一... |
| 203 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1520 | FP | FP | 切片代码显示，宏 QUIC_RAISE_NON_NORMAL_ERROR 被正确调用，其参数数量与宏定义匹配，且宏展开后调用 quic_raise_non_normal_error 的参数列表是完整的，不存在未终止的可变参数调用问题。... |
| 204 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1527 | FP | FP | QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，展开为对 quic_raise_non_normal_error 的调用，其参数列表是固定的，切片中未显示该函数是可变参数函数，且所有调用点都提供了确切数量的参数，不存... |
| 205 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1537 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，展开为对 quic_raise_non_normal_error 的调用，其参数列表是固定的，不存在未终止的可变参数调用风险。 |
| 206 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 221 | FP | FP | 代码使用恒定时间操作（constant_time_is_zero, mask）来安全地处理边界条件，循环中的指针递减和掩码操作确保了不会发生越界读取。告警点位于受控的复制循环内，该循环显式地处理了 flen 和 num 的关系，防止了... |
| 208 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来安全地处理边界条件，确保指针访问不会越界。循环中的 flen 递减和 from 指针移动受 ma... |
| 207 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 229 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 处的 `em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，并在循环 `for (from +... |
| 209 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 `em[0]` 的访问是安全的，因为 `em` 指向由 `OPENSSL_malloc(num)` 分配的内存块起始位置，且循环 `for (from += flen, em += num, i = 0; i < num; i... |
| 213 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保sc->ext.session_ticket不为NULL，并且对ext_data进行了非空检查。代码逻辑正确，不存在对已释放内存的访问。 |
| 211 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1182 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后对新分配的内存进行了空指针检查，访问 `sc->ext.sess... |
| 212 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1183 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，随后立即检查新分配的内存是否为 NULL。`sc->ext.session_ticket->da... |
| 210 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警指出的指针运算 `em[0]` 和 `em[1]` 是在 `em = OPENSSL_malloc(num)` 分配的内存块内进行的访问，且循环 `for (from += flen, em += num, i = 0; i < ... |
| 214 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且已为新分配的sc->ext.session_ticket分配了足够的内存（包括扩展长度ext_len），因此不存在对已释放内存的访问。 |
| 215 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1186 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已调用 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后对新分配的内存进行判空检查，逻辑安全，不存在对已释放内存的访问。 |
| 216 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1187 | FP | FP | 切片代码显示，在将`sc->ext.session_ticket->data`赋值为NULL之前，已经通过`OPENSSL_free`释放了旧指针并分配了新内存，不存在对已释放内存的访问。告警点是对新分配结构体成员的初始化，是安全的。 |
| 218 | openssl-openssl-3.4.0 | tls_parse_stoc_npn | cpp/use-after-free | 1619 | FP | FP | 切片代码显示，在调用memcpy之前，已通过OPENSSL_malloc为s->ext.npn分配了新内存，并检查了分配结果。对同一指针的释放和重新分配是安全的操作序列，不存在对已释放内存的访问。 |
| 220 | openssl-openssl-3.4.0 | <global> | cpp/offset-use-before-range-check | 246 | FP | FP | 循环条件 `src[i] != '\0' && i < len` 已确保索引 `i` 在访问 `src[i]` 和 `tgt[i]` 前会进行范围检查（`i < len`），因此不存在越界访问风险。 |
| 219 | openssl-openssl-3.4.0 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 切片代码显示，在告警行之前的代码路径中，`*keySpec` 可能已被 `sk_OSSL_CMP_ATAV_pop_free` 释放并设置为 NULL，因此后续的 `if (keySpec != NULL)` 检查是必要的，用于防止对... |
| 217 | openssl-openssl-3.4.0 | tls_parse_stoc_alpn | cpp/use-after-free | 1688 | FP | FP | 切片代码显示，在调用memcmp比较s->session->ext.alpn_selected和s->s3.alpn_selected之前，s->s3.alpn_selected已通过OPENSSL_malloc分配内存，而s->se... |
| 221 | openssl-openssl-3.4.0 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 切片代码显示，在警告行 'for (i = 0; DB[i] == 0 && i < (maskedDBLen - 1); i++) ;' 中，变量 'i' 的使用已通过条件 'i < (maskedDBLen - 1)' 进行了范围... |
| 222 | openssl-openssl-3.4.0 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 470 | FP | FP | 切片代码中，在调用 CRYPTO_THREAD_get_local 后，立即使用 `assert(data != NULL);` 对返回值进行了断言检查，这确保了在调试构建中数据不为空，且表明程序逻辑预期此处数据有效。因此，未进行显式... |
| 223 | openssl-openssl-3.4.0 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 索引越界时返回 NULL，而 `enc_level` 由调用者传入且已通过 `ossl_q... |
| 227 | openssl-openssl-3.4.0 | <global> | cpp/unbounded-write | 30 | FP | FP | 函数CRYPTO_strdup在调用strcpy前，已通过CRYPTO_malloc分配了strlen(str) + 1字节的内存，目标缓冲区大小与源字符串长度精确匹配，不存在缓冲区溢出的风险。 |
| 228 | openssl-openssl-3.4.0 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码显示，在调用strcpy之前，函数已通过`len + 1 >= size`检查确保目标缓冲区`buf`的大小`size`足以容纳源字符串`s`及其终止符，因此不会发生缓冲区溢出。 |
| 229 | openssl-openssl-3.4.0 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码显示，在调用strcpy之前，函数已通过`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 225 | openssl-openssl-3.4.0 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 函数 `ossl_uint_set_insert` 在调用 `ossl_list_uint_set_head(s)` 后，立即在 `if (start <= f->range.start && end >= z->range.end)... |
| 232 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3145 | FP | FP | 切片代码显示，对宏 QUIC_RAISE_NON_NORMAL_ERROR 的两次调用均提供了三个参数（ctx, reason, msg），符合其定义。该告警提示应使用值0作为终止符，但此宏并非可变参数函数，其参数数量固定，因此告警不适用。 |
| 231 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3136 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_PASSED_NULL_PARAMETER, "stream to attach must be a valid QUIC strea... |
| 233 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3155 | FP | FP | 告警指出的QUIC_RAISE_NON_NORMAL_ERROR宏调用缺少终止符0，但根据提供的宏定义和函数调用，该宏是一个包装器，其参数列表是固定的，并不需要可变参数终止符。代码逻辑正确，属于工具规则误判。 |
| 235 | openssl-openssl-3.4.0 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3077 | FP | FP | 告警指出的宏 QUIC_RAISE_NON_NORMAL_ERROR 在切片代码中已明确定义，其参数列表以 `(msg)` 结尾，并非未终止的可变参数调用。该宏的调用方式符合其定义，属于工具误报。 |
| 234 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3161 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数（reason 和 msg），其展开后的函数 `quic_raise_non_normal_error` 的变参列表由宏定义保证以 `N... |
| 237 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1546 | FP | FP | 告警指出的宏 QUIC_RAISE_NON_NORMAL_ERROR 在切片代码中被正确调用，其参数数量与宏定义匹配，且宏展开后对 quic_raise_non_normal_error 的调用格式在切片中无法验证存在未终止的可变参数... |
| 236 | openssl-openssl-3.4.0 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3089 | FP | FP | 告警提示的宏 QUIC_RAISE_NON_NORMAL_ERROR 在切片中已明确定义，其展开为对 quic_raise_non_normal_error 的调用，且参数列表以宏参数 (msg) 结尾，符合C语言可变参数函数的调用规... |
| 239 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1563 | FP | FP | 告警指出的宏调用 QUIC_RAISE_NON_NORMAL_ERROR 已正确提供了三个参数（ctx, reason, msg），与宏定义要求一致，不存在未终止的可变参数调用问题。 |
| 238 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1553 | FP | FP | QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，展开后调用 quic_raise_non_normal_error 函数。切片中该宏的定义显示其参数列表是固定的（ctx, reason, msg），并非可变参数函数调... |
| 240 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 代码使用恒定时间操作（constant_time_is_zero, mask）来安全地处理边界条件，循环中的指针运算和访问受 `flen` 和 `num` 控制，切片内未发现越界访问的证据。告警可能源于工具对恒定时间逻辑的误判。 |
| 242 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用了恒定时间操作（constant_time_*函数）和掩码（mask）来安全地处理边界条件，指针访问受`flen`和`mask`的控制，不会发生越界读取。 |
| 241 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 告警点 'good = constant_time_is_zero(em[0]);' 处的数组访问 'em[0]' 是安全的。代码在第253行之前已通过 'em = OPENSSL_malloc(num);' 分配了大小为 'num'... |
| 244 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警指向的数组访问 `em[1]` 是安全的，因为 `em` 指向通过 `OPENSSL_malloc(num)` 分配的内存块，且循环 `for (i = 0; i < num; i++)` 确保 `num` 至少为 1，使得 `e... |
| 243 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 'good = constant_time_is_zero(em[0]);' 中，指针 'em' 在循环 'for (from += flen, em += num, i = 0; i < num; i++)' 后已指向分配内... |
| 245 | git-2.47.1 | is_command | cpp/redundant-null-check-simple | 2602 | FP | FP | 告警指出的空指针检查冗余，是因为在函数 `skip_prefix` 中，对指针 `prefix` 的解引用（`*prefix`）发生在检查 `!*prefix` 之后，而 `prefix` 参数来自 `todo_command_inf... |
| 248 | git-2.47.1 | ce_write_entry | cpp/offset-use-before-range-check | 2687 | FP | FP | 变量 `common` 在 for 循环条件中已通过 `common < previous_name->len` 进行了范围检查，确保其不会超过 `previous_name->len`。后续使用 `ce->name + common... |
| 247 | git-2.47.1 | fill_es_indent_data | cpp/offset-use-before-range-check | 894 | FP | FP | 告警点 `off < len - 1` 中的 `off` 在循环中递增，但循环条件 `s[off] == '\r'` 已确保对 `s[off]` 的访问在 `off` 递增前是安全的。`len` 是字符串长度，`off` 从0开始递增... |
| 246 | git-2.47.1 | refname_is_safe | cpp/no-space-for-terminator | 350 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，即字符串 `rest` 的长度。`rest` 是 `skip_prefix` 处理后指向 `refname` 中 `"refs/"` 之后部分的指针，其长度 `restle... |
| 251 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 792 | FP | FP | 循环条件 `pos < len` 确保了变量 `pos` 在用作偏移量之前已经过范围检查，不会导致越界访问。 |
| 254 | git-2.47.1 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的函数 branch_get 在传入空名或 "HEAD" 时返回 current_branch，否则通过 make_branch 创建，两者均返回有效的 struct branch 指针，函数本身不会返回 NULL。因此调用后无... |
| 256 | git-2.47.1 | update_head | cpp/inconsistent-null-check | 685 | FP | FP | 代码中 `refs_update_ref` 调用指定了 `UPDATE_REFS_DIE_ON_ERR` 标志，当操作失败时会调用 `die` 函数终止程序，这提供了错误处理机制，使得对 `lookup_commit_referenc... |
| 253 | git-2.47.1 | setup_scoreboard | cpp/inconsistent-null-check | 2857 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，该条件已确保 `sb->final` 非空且其 OID 为空。函数 `get_blame_suspects` 的定义显示它可能返... |
| 258 | git-2.47.1 | do_fetch | cpp/inconsistent-null-check | 1628 | FP | FP | 告警点调用的 branch_get(NULL) 返回值在后续的 branch_has_merge_config(branch) 中被显式检查，该函数内部已包含对 branch 指针的 NULL 检查，因此不会导致空指针解引用。 |
| 260 | git-2.47.1 | refspec_append_mapped | cpp/inconsistent-null-check | 90 | FP | FP | 被调用的 branch_get 函数内部已对空指针输入进行了处理，并始终返回一个有效的 struct branch 指针（例如，当 name 为 NULL 或 "HEAD" 时返回 current_branch，否则创建或获取分支）。... |
| 259 | git-2.47.1 | get_ref_map | cpp/inconsistent-null-check | 552 | FP | FP | 切片代码显示，在调用 branch_get(NULL) 后，其返回值 branch 被直接传递给 branch_has_merge_config 函数。该函数内部已包含对 branch 指针的显式空值检查（`return branch... |
| 261 | git-2.47.1 | do_create_stash | cpp/inconsistent-null-check | 1390 | FP | FP | 代码中 `head_commit` 在后续被 `repo_find_unique_abbrev` 和 `pp_commit_easy` 等函数直接解引用，表明调用者确信 `lookup_commit` 会返回有效对象；在 Git 上下... |
| 262 | git-2.47.1 | reset_tree | cpp/inconsistent-null-check | 285 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将返回值传递给 parse_tree 函数进行检查，如果解析失败会返回 -1，这相当于对返回值进行了有效性检查。因此，该告警属于误报。 |
| 266 | git-2.47.1 | verify_one_commit_graph | cpp/inconsistent-null-check | 2774 | FP | FP | lookup_commit 函数在内部已处理了空对象的情况，若对象不存在则会创建新对象，因此其返回值不会为 NULL，无需额外检查。 |
| 265 | git-2.47.1 | update_one | cpp/inconsistent-null-check | 328 | FP | FP | 在调用 find_subtree 时，create 参数为 1，根据 find_subtree 函数定义，当 create 为 1 时，函数会分配并返回一个新的 cache_tree_sub 结构体，不会返回 NULL。因此，此处无需... |
| 264 | git-2.47.1 | write_bundle_refs | cpp/inconsistent-null-check | 435 | FP | FP | 在调用 lookup_commit_reference 后，代码立即通过 e->item == &(one->object) 访问 one->object，这隐含地假设 one 非空。然而，该调用位于 if (!oideq(&oid,... |
| 267 | git-2.47.1 | unparse_commit | cpp/inconsistent-null-check | 188 | FP | FP | 函数 `lookup_commit` 在内部已处理了 `obj` 为 NULL 的情况，会调用 `create_object` 返回一个有效的对象，因此其返回值不会为 NULL，无需额外检查。 |
| 271 | git-2.47.1 | get_parent | cpp/inconsistent-null-check | 1107 | FP | FP | 代码在调用 lookup_commit_reference 后，立即将结果传递给 repo_parse_commit 进行校验。repo_parse_commit 会检查提交对象的有效性，如果 commit 为 NULL 或无效，该函... |
| 272 | git-2.47.1 | show_ambiguous_object | cpp/inconsistent-null-check | 442 | FP | FP | 代码在调用 `lookup_tag` 后立即将其结果传递给 `parse_tag` 进行解析，`parse_tag` 函数内部会检查 `tag` 指针的有效性（例如通过 `item->object.parsed` 或 `repo_re... |
| 273 | git-2.47.1 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3344 | FP | FP | 函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到项（`!ref->base`）的情况进行了处理并返回 NULL，调用方 `leave_one_treesame_to_parent` 将返回... |
| 274 | git-2.47.1 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 701 | FP | FP | 根据提供的lookup_commit函数定义，当查找对象不存在时，函数会调用create_object创建一个新的对象并返回，因此该函数不会返回NULL。代码无需检查NULL，告警为误报。 |
| 270 | git-2.47.1 | find_merge_parents | cpp/inconsistent-null-check | 616 | FP | FP | parse_object 的返回值 obj 在后续代码中仅用于获取其 oid 成员（&obj->oid），该操作在 obj 为 NULL 时会导致崩溃，但切片显示 obj 仅在 add_merge_parent 调用中使用，而 add... |
| 275 | git-2.47.1 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在内部已处理了空对象指针的情况，若 `lookup_object` 返回 NULL，它会调用 `create_object` 创建一个新对象并返回，因此调用方无需进行额外的空指针检查。 |
| 287 | git-2.47.1 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1660 | FP | FP | 告警指出的写操作 `buffer[size] = '\0'` 是安全的，因为 `buffer` 由 `xmallocz_gently(size)` 分配，该函数分配 `size + 1` 字节的内存，确保索引 `size` 在边界内。... |
| 289 | git-2.50.1 | refname_is_safe | cpp/no-space-for-terminator | 353 | FP | FP | 函数 `xmallocz` 的定义显示它调用了 `do_xmallocz(size, 0)`，其中第二个参数为0，表明该分配函数内部已为字符串终止符预留了空间，因此分配大小 `restlen` 是足够的，不存在缺少空终止符空间的问题。 |
| 295 | git-2.50.1 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的函数 branch_get 在输入为 NULL 或空字符串时会返回 the_repository->remote_state->current_branch，而非 NULL，因此调用后无需进行 NULL 检查。切片代码中包含了... |
| 296 | git-2.50.1 | write_index_patch | cpp/inconsistent-null-check | 1435 | FP | FP | lookup_tree 被调用时传入的是 the_repository->hash_algo->empty_tree，这是一个已知的、有效的空树对象ID，不可能返回NULL。因此，无需进行空值检查，告警为误报。 |
| 294 | git-2.50.1 | setup_scoreboard | cpp/inconsistent-null-check | 2858 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，该条件已确保 `sb->final` 非空且其 object.oid 为空哈希。函数 `get_blame_suspects` ... |
| 300 | git-2.50.1 | get_ref_map | cpp/inconsistent-null-check | 550 | FP | FP | 切片代码显示，在调用branch_has_merge_config(branch)之前，branch变量已通过branch_get(NULL)获取，而branch_has_merge_config函数内部已包含对branch是否为NU... |
| 299 | git-2.50.1 | <global> | cpp/inconsistent-null-check | 547 | FP | FP | lookup_tree 调用传入的是 the_repository->hash_algo->empty_tree，这是一个已知的常量空树对象ID，不可能返回 NULL。因此无需进行空指针检查，告警为误报。 |
| 301 | git-2.50.1 | refspec_append_mapped | cpp/inconsistent-null-check | 92 | FP | FP | 被调用的branch_get函数在输入为NULL或空字符串时会返回the_repository->remote_state->current_branch，该返回值是一个有效的结构体指针，不会返回NULL。因此，调用后无需进行NULL检查。 |
| 302 | git-2.50.1 | do_create_stash | cpp/inconsistent-null-check | 1397 | FP | FP | 切片代码显示，在调用 `lookup_commit` 后，其返回值 `head_commit` 被直接用于 `head_commit->object.oid` 等操作，这表明代码逻辑假设该调用总是成功。结合上下文，`info->b_c... |
| 303 | git-2.50.1 | reset_tree | cpp/inconsistent-null-check | 286 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将结果传递给 parse_tree 函数进行检查，如果解析失败会返回错误。这构成了对返回值的有效检查，因此工具报告的 null 检查不一致问题是误报。 |
| 305 | git-2.50.1 | update_one | cpp/inconsistent-null-check | 333 | FP | FP | find_subtree 在 create=1 模式下被调用，根据其函数定义，当 create 为真时，函数会分配并返回一个新的子树节点，不会返回 NULL。因此，对返回值的空指针检查是不必要的，告警属于误报。 |
| 306 | git-2.50.1 | verify_one_commit_graph | cpp/inconsistent-null-check | 2798 | FP | FP | lookup_commit 函数在内部已处理了对象不存在的情况，会通过 create_object 创建新对象，因此调用方无需检查空指针。代码后续对 graph_commit 的使用（如访问 graph_commit->parents... |
| 312 | git-2.50.1 | show_ambiguous_object | cpp/inconsistent-null-check | 443 | FP | FP | 代码在调用 `lookup_tag` 后，立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析和错误检查。`parse_tag` 函数内部会处理 `tag` 为 NULL 或无效的情况并返回错误，因此即使 `... |
| 310 | git-2.50.1 | find_merge_parents | cpp/inconsistent-null-check | 617 | FP | FP | parse_object 返回的指针 obj 在后续代码中仅用于获取其 oid 成员（&obj->oid），该操作在 obj 为 NULL 时会导致未定义行为。然而，在调用 parse_object 之前，代码已通过 parse_oi... |
| 313 | git-2.50.1 | setup_pending_objects | cpp/inconsistent-null-check | 333 | FP | FP | 切片代码显示，在调用strmap_get获取root_tree_list后，仅在后续的OBJ_TREE分支中使用了该指针（root_tree_list->oids）。该分支仅在root_tree_list不为NULL时才会执行，因为对... |
| 314 | git-2.50.1 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3351 | FP | FP | 函数 `lookup_decoration` 在内部已对 `n->size` 进行空值检查，若为空则直接返回 NULL。调用方 `leave_one_treesame_to_parent` 获取的指针 `ts` 在后续循环中未被解引用... |
| 315 | git-2.50.1 | add_cache_tree | cpp/inconsistent-null-check | 1775 | FP | FP | 函数`lookup_tree`的定义显示，当查找的对象不存在时，它会调用`create_object`创建一个新对象并返回，因此该函数永远不会返回NULL。代码直接使用返回值是安全的，无需NULL检查。 |
| 317 | git-2.50.1 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | lookup_commit函数在传入对象不存在时会创建新对象并返回，不会返回NULL，因此无需进行空指针检查。 |
| 318 | git-2.50.1 | has_uncommitted_changes | cpp/inconsistent-null-check | 2642 | FP | FP | lookup_tree 被调用时传入的是 the_hash_algo->empty_tree，这是一个已知的、有效的常量对象ID，用于表示空树，因此该调用不会返回 NULL，无需检查。 |
| 319 | git-2.50.1 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | FP | FP | 宏 TEST_CHAR_CLASS 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时可能产生负索引，但宏内包含 `BUILD_ASSERT_OR_ZERO(ARRAY_... |
| 321 | git-2.50.1 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但宏内包含 `BUILD_ASSERT_OR_ZERO(ARRAY... |
| 320 | git-2.50.1 | test_ctype__ispunct | cpp/overflow-buffer | 91 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但宏内已通过 `BUILD_ASSERT_OR_ZERO(ARRA... |
| 322 | git-2.50.1 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被调用时传入的 `string` 是一个字符串字面量，其 `ARRAY_SIZE` 结果大于0，因此... |
| 323 | git-2.50.1 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string) > 0` 时执行，而 `BUILD_ASSERT_OR_ZERO` 宏确保了该条件成立，因此... |
| 324 | git-2.50.1 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，其中 `string` 是字符串字面量 `"*?[\\"`，其 `ARRAY_SIZE` 肯定大于0，因此... |
| 325 | git-2.50.1 | test_ctype__isalnum | cpp/overflow-buffer | 51 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，其中 `string` 是宏参数 `LOWER UPPER DIGIT`，这是一个字符串字面量。`ARR... |
| 326 | git-2.50.1 | test_ctype__isalpha | cpp/overflow-buffer | 46 | FP | FP | 宏定义中 `ARRAY_SIZE(string) - 1` 的索引操作在 `ARRAY_SIZE(string) > 0` 的编译时断言保护下，不会导致负索引访问。切片中的 `BUILD_ASSERT_OR_ZERO` 确保了数组大小... |
| 327 | git-2.50.1 | test_ctype__isdigit | cpp/overflow-buffer | 41 | FP | FP | 告警针对宏展开后的数组索引 `string[-1]`，但宏 `BUILD_ASSERT_OR_ZERO` 在编译时确保 `ARRAY_SIZE(string) > 0`，因此 `len` 计算中的 `ARRAY_SIZE(string... |
| 328 | git-2.50.1 | <global> | cpp/overflow-buffer | 36 | FP | FP | 切片代码显示函数体为空，未定义任何数组或索引操作，因此告警所报告的负索引访问在实际代码中不存在，属于工具误报。 |
| 332 | git-2.49.0 | is_command | cpp/redundant-null-check-simple | 2614 | FP | FP | 告警指出的冗余空值检查是针对指针 'p' 的解引用，但 'p' 在函数开始时已通过 '*bol' 赋值，且 'bol' 作为参数传入，其有效性由调用方保证。在 skip_prefix 函数和后续逻辑中，'p' 的解引用是安全的，因为代... |
| 333 | git-2.49.0 | refname_is_safe | cpp/no-space-for-terminator | 353 | FP | FP | 函数 xmallocz 内部实现未在切片中完全展示，但根据其名称和常见模式，它很可能分配了 size+1 的空间并清零。此外，buf 被传递给 normalize_path_copy，该函数期望目标缓冲区有足够空间，且后续的 strc... |
| 335 | git-2.49.0 | ce_write_entry | cpp/offset-use-before-range-check | 2689 | FP | FP | 变量 'common' 在 for 循环条件中已通过 'common < previous_name->len' 进行了范围检查，确保其不会超过 previous_name->len，因此后续使用 'ce->name + common... |
| 342 | git-2.49.0 | write_index_patch | cpp/inconsistent-null-check | 1433 | FP | FP | lookup_tree 被调用时传入的是已知的、有效的空树对象ID (the_repository->hash_algo->empty_tree)，该调用预期不会返回NULL。切片中显示的代码逻辑确保了该路径下 tree 变量是有效的... |
| 340 | git-2.49.0 | setup_scoreboard | cpp/inconsistent-null-check | 2858 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，该条件已确保 `sb->final` 非空且其 `object.oid` 为空 OID。`get_blame_suspects`... |
| 346 | git-2.49.0 | do_fetch | cpp/inconsistent-null-check | 1756 | FP | FP | 切片代码显示，在调用 branch_has_merge_config(branch) 之前，已经对 branch 进行了空指针检查，因为 branch_has_merge_config 函数内部会检查 branch && !!bran... |
| 348 | git-2.49.0 | refspec_append_mapped | cpp/inconsistent-null-check | 92 | FP | FP | 被调用的 branch_get 函数内部已对空指针输入进行了检查，并始终返回一个有效的 struct branch 指针（例如，当 name 为 NULL 或 "HEAD" 时返回 current_branch，否则通过 make_b... |
| 345 | git-2.49.0 | <global> | cpp/inconsistent-null-check | 546 | FP | FP | lookup_tree 返回的 tree 指针被立即传递给 add_pending_object，后者内部会处理空指针情况或后续代码会进行空值检查（如 deref_tag 和 die 调用）。告警点位于一个特定条件分支（rev.pen... |
| 347 | git-2.49.0 | get_ref_map | cpp/inconsistent-null-check | 551 | FP | FP | 代码中调用 branch_get(NULL) 后，其返回值被立即传递给 branch_has_merge_config 函数，该函数内部已包含对指针是否为 NULL 的检查（`return branch && !!branch->me... |
| 350 | git-2.49.0 | reset_tree | cpp/inconsistent-null-check | 287 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将返回值传递给 parse_tree 函数进行检查，如果 parse_tree 失败会返回 -1，这间接验证了 tree 指针的有效性，因此无需显式的空指针检查。 |
| 349 | git-2.49.0 | do_create_stash | cpp/inconsistent-null-check | 1398 | FP | FP | 代码中 `head_commit` 变量在后续被 `repo_find_unique_abbrev` 和 `pp_commit_easy` 等函数直接解引用，表明调用者确信 `lookup_commit` 会返回有效对象。在 Git ... |
| 352 | git-2.49.0 | update_one | cpp/inconsistent-null-check | 329 | FP | FP | find_subtree 在 create=1 模式下被调用，根据其定义，当找不到子树时会创建并返回一个新的非空子树对象，因此返回值不可能为 NULL，无需检查。 |
| 354 | git-2.49.0 | unparse_commit | cpp/inconsistent-null-check | 188 | FP | FP | 函数 `lookup_commit` 在内部已处理了 `obj` 为 NULL 的情况，会调用 `create_object` 返回一个有效的对象，因此其返回值不会为 NULL，无需额外检查。 |
| 356 | git-2.49.0 | deref_without_lazy_fetch | cpp/inconsistent-null-check | 156 | FP | FP | 在调用 parse_object 后，代码立即通过 tag->tagged 访问了返回的 tag 结构体成员，这隐含了对 tag 指针的非空检查，因为如果 parse_object 返回 NULL，解引用会导致崩溃。因此，代码逻辑实际... |
| 353 | git-2.49.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2788 | FP | FP | 代码中`lookup_commit`的返回值`graph_commit`在后续被直接用于`parse_commit_in_graph_one`和`get_commit_tree_in_graph_one`等函数调用，这些函数内部已对无... |
| 358 | git-2.49.0 | get_parent | cpp/inconsistent-null-check | 1108 | FP | FP | 代码在调用 lookup_commit_reference 后，立即将结果传递给 repo_parse_commit 进行校验，若解析失败则返回 MISSING_OBJECT，这隐含了对 commit 对象有效性的检查，提供了必要的错... |
| 357 | git-2.49.0 | find_merge_parents | cpp/inconsistent-null-check | 617 | FP | FP | `parse_object`的返回值被赋值给变量`obj`，并立即传递给`repo_peel_to_type`函数，该函数内部会检查对象是否有效（`if (!o ｜｜ (!o->parsed && !parse_object(r, &... |
| 359 | git-2.49.0 | show_ambiguous_object | cpp/inconsistent-null-check | 443 | FP | FP | 代码在调用 `lookup_tag` 后立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析，`parse_tag` 函数内部会检查 `tag` 是否为 NULL 并处理错误。因此，虽然未显式检查 `look... |
| 360 | git-2.49.0 | setup_pending_objects | cpp/inconsistent-null-check | 333 | FP | FP | 切片代码显示，在调用strmap_get获取root_tree_list后，后续代码（如oid_array_append(&root_tree_list->oids, &obj->oid)）直接使用了该指针。这表明代码逻辑预期该指针非... |
| 362 | git-2.49.0 | add_cache_tree | cpp/inconsistent-null-check | 1783 | FP | FP | lookup_tree函数内部已对空指针进行了检查，若obj为空则调用create_object创建新对象，因此调用方无需再次检查返回值。切片代码中可见的lookup_tree实现保证了返回有效的tree指针。 |
| 361 | git-2.49.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3357 | FP | FP | 函数 `lookup_decoration` 在内部已对空指针 `n->size` 进行了检查，若为空则直接返回 NULL。调用方 `leave_one_treesame_to_parent` 虽未显式检查返回值，但后续循环仅遍历 `... |
| 363 | git-2.49.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 703 | FP | FP | lookup_commit函数在传入的oid无效时会创建并返回一个新的commit对象，不会返回NULL，因此无需进行空指针检查。 |
| 364 | git-2.49.0 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | lookup_commit函数在对象不存在时会创建新对象并返回，不会返回NULL，因此无需进行空指针检查。 |
| 365 | git-2.49.0 | has_uncommitted_changes | cpp/inconsistent-null-check | 2642 | FP | FP | lookup_tree 函数被调用时，其参数是 the_hash_algo->empty_tree，这是一个已知的、有效的空树对象ID，因此函数不会返回NULL。代码逻辑保证了调用是安全的，无需NULL检查。 |
| 366 | git-2.49.0 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是字符串字面量 `"DIGIT \"abcdefABCDEF\""`，其 `ARRA... |
| 367 | git-2.49.0 | test_ctype__ispunct | cpp/overflow-buffer | 91 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数 `PUNCT`，其定义为字符串字面量，`ARRAY_SIZE` 返回其长度（包括空终... |
| 368 | git-2.49.0 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | FP | FP | 宏定义中 `ARRAY_SIZE(string) - 1` 的索引操作 `string[0]` 是编译时静态数组大小检查的一部分，`string` 是宏参数，在调用点 `CNTRL` 是一个字符串字面量，其大小在编译时已知且大于0，因... |
| 369 | git-2.49.0 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，其中 `string` 是字符串字面量 `"!\"#%&',-/:;<=>@_`~"`，其大小固定且大于... |
| 370 | git-2.49.0 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | FP | FP | 告警指出的负索引访问发生在宏 `ARRAY_SIZE(string) - 1` 中，其中 `string` 是字符串字面量 `"$()*+.?[\\^{｜"`，其 `ARRAY_SIZE` 计算出的长度至少为1，因此 `ARRAY_S... |
| 371 | git-2.49.0 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，其中 `string` 是字符串字面量 `"*?[\\"`，其 `ARRAY_SIZE` 计算结果大于0... |
| 373 | git-2.49.0 | test_ctype__isalpha | cpp/overflow-buffer | 46 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，但该表达式受 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)... |
| 372 | git-2.49.0 | test_ctype__isalnum | cpp/overflow-buffer | 51 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数 `LOWER UPPER DIGIT`，它是一个字符串字面量，`ARRAY_SIZE... |
| 375 | git-2.49.0 | <global> | cpp/overflow-buffer | 36 | FP | FP | 切片代码显示函数体为空，不存在任何数组索引操作，因此工具报告的访问负索引-1的告警不成立，属于误报。 |
| 374 | git-2.49.0 | test_ctype__isdigit | cpp/overflow-buffer | 41 | FP | FP | 宏 TEST_CHAR_CLASS 中的数组索引 `string[-1]` 仅出现在 `ARRAY_SIZE(string) - 1` 表达式中，用于计算字符串长度，且该宏被 `BUILD_ASSERT_OR_ZERO` 断言保护，确... |
| 379 | git-2.46.0 | is_command | cpp/redundant-null-check-simple | 2601 | FP | FP | 告警指出的冗余空值检查是针对指针 `p` 的解引用，但 `p` 在函数 `skip_prefix` 中被安全地递增，并且 `p` 初始化为 `*bol`，而 `bol` 是函数参数，其有效性由调用方保证。在 `skip_prefix`... |
| 382 | git-2.46.0 | ce_write_entry | cpp/offset-use-before-range-check | 2685 | FP | FP | 变量 'common' 在 for 循环条件中已通过 'common < previous_name->len' 进行了范围检查，确保其不会超过 previous_name->len，因此后续使用 'ce->name + common... |
| 380 | git-2.46.0 | refname_is_safe | cpp/no-space-for-terminator | 345 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，而 `restlen` 是 `strlen(rest)` 的结果，不包含空终止符。但 `normalize_path_copy` 函数要求目标缓冲区足够容纳源字符串及其空终... |
| 388 | git-2.46.0 | do_fetch | cpp/inconsistent-null-check | 1626 | FP | FP | 告警点调用的branch_get(NULL)返回的指针在后续使用前，已通过branch_has_merge_config(branch)函数进行了检查，该函数内部会检查branch是否为NULL，因此不会导致空指针解引用。 |
| 383 | git-2.46.0 | setup_scoreboard | cpp/inconsistent-null-check | 2857 | FP | FP | 函数 get_blame_suspects 的定义显示其可能返回 NULL，但调用点位于条件 `if (is_null_oid(&sb->final->object.oid))` 内部，该条件确保 sb->final 的 OID 为空... |
| 390 | git-2.46.0 | refspec_append_mapped | cpp/inconsistent-null-check | 88 | FP | FP | 被调用的 `branch_get` 函数内部已对 `name` 参数进行了空指针和空字符串检查，并返回有效的 `struct branch` 指针（例如 `current_branch` 或 `make_branch` 的结果），因此... |
| 389 | git-2.46.0 | get_ref_map | cpp/inconsistent-null-check | 551 | FP | FP | 切片代码显示，在调用 branch_get(NULL) 后，其返回值 'branch' 被直接传递给 branch_has_merge_config 函数。该函数内部（已包含在切片中）明确检查了传入的指针是否为 NULL（`retur... |
| 391 | git-2.46.0 | do_create_stash | cpp/inconsistent-null-check | 1388 | FP | FP | 切片代码显示，`head_commit` 变量在后续多处被直接解引用（如 `head_commit->object.oid`），这表明其被假定为非空。结合上下文，`info->b_commit` 应是一个有效的提交对象ID，`look... |
| 392 | git-2.46.0 | reset_tree | cpp/inconsistent-null-check | 283 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将结果传递给 parse_tree 函数进行检查，如果 parse_tree 失败则返回错误。这相当于对 tree 指针的有效性进行了间接验证，因此 null 检查是存在的，... |
| 395 | git-2.46.0 | update_one | cpp/inconsistent-null-check | 327 | FP | FP | 在调用 `find_subtree(it, path + baselen, sublen, 1)` 时，create 参数为 1，根据 find_subtree 函数定义，当 create 为 1 时，函数保证返回一个非空指针（要么找... |
| 396 | git-2.46.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2774 | FP | FP | `lookup_commit` 函数在内部已处理了空对象的情况，若未找到对象会通过 `create_object` 创建一个新的提交对象并返回，因此其返回值不会为 NULL。代码后续对 `graph_commit` 的使用是安全的，无... |
| 397 | git-2.46.0 | ahead_behind | cpp/inconsistent-null-check | 1069 | FP | FP | 函数 `prio_queue_get` 内部已对空队列进行检查并返回 NULL，且调用点位于 `while (queue_has_nonstale(&queue))` 循环内，该循环条件已确保队列非空且包含非陈旧提交，因此 `prio... |
| 394 | git-2.46.0 | write_bundle_refs | cpp/inconsistent-null-check | 430 | FP | FP | 在调用 `lookup_commit_reference` 后，代码立即通过 `e->item == &(one->object)` 访问了 `one->object` 成员，这隐含地假设了 `one` 非空。由于 `e->item`... |
| 398 | git-2.46.0 | paint_down_to_common | cpp/inconsistent-null-check | 81 | FP | FP | 函数 `queue_has_nonstale` 在循环前已检查队列中是否存在非陈旧提交，确保 `prio_queue_get` 被调用时队列非空；且 `prio_queue_get` 内部在 `queue->nr` 为0时返回 NUL... |
| 399 | git-2.46.0 | unparse_commit | cpp/inconsistent-null-check | 182 | FP | FP | 函数 `lookup_commit` 在内部已处理了空对象情况，若 `lookup_object` 返回空，它会调用 `create_object` 创建一个新对象并返回，因此其返回值不会为空指针。切片代码中后续对 `c->objec... |
| 404 | git-2.46.0 | get_parent | cpp/inconsistent-null-check | 1098 | FP | FP | 代码在调用 lookup_commit_reference 后，立即将结果传递给 repo_parse_commit 进行校验；repo_parse_commit 会检查提交对象的有效性，若 commit 为 NULL 或无效，函数将... |
| 405 | git-2.46.0 | show_ambiguous_object | cpp/inconsistent-null-check | 436 | FP | FP | 在调用 `lookup_tag` 后，代码立即检查 `!parse_tag(tag) && tag->tag`，这隐含了对 `tag` 指针非空的假设。`parse_tag` 函数内部会处理 `tag` 为 NULL 的情况（返回错误... |
| 402 | git-2.46.0 | find_merge_parents | cpp/inconsistent-null-check | 616 | FP | FP | 告警点`obj`在后续代码中仅用于调用`add_merge_parent`，该函数仅复制其oid成员，未解引用对象指针本身。即使`parse_object`返回NULL，`obj->oid`的访问（在`add_merge_parent... |
| 407 | git-2.46.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3339 | FP | FP | 函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到项（`!ref->base`）的情况进行了处理并返回 NULL，调用方 `leave_one_treesame_to_parent` 虽未显... |
| 408 | git-2.46.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 690 | FP | FP | lookup_commit函数在传入的oid无效时会创建并返回一个新的commit对象，不会返回NULL，因此无需进行空指针检查。 |
| 409 | git-2.46.0 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在内部已处理空指针情况，当 `obj` 为空时会调用 `create_object` 创建新对象并返回，因此调用方无需检查返回值是否为空。 |
| 422 | git-2.46.0 | should_prune_worktree | cpp/invalid-pointer-deref | 788 | FP | FP | 指针 'path' 由 xmallocz(len) 分配，大小为 len+1 字节，而写入操作 path[len] = '\0' 是在分配的有效内存边界内，因为 xmallocz 会分配 len+1 的空间并清零，所以该写入是安全的。 |
| 423 | git-2.44.0 | is_command | cpp/redundant-null-check-simple | 2522 | FP | FP | 告警指出的空指针解引用检查是冗余的，但分析代码逻辑发现，变量 `nick` 是从结构体数组中获取的字符，并非指针，因此不存在空指针解引用问题。工具可能误判了字符变量与指针变量的区别。 |
| 426 | git-2.44.0 | ce_write_entry | cpp/offset-use-before-range-check | 2713 | FP | FP | 变量 'common' 在 for 循环条件中已通过 'common < previous_name->len' 进行了范围检查，确保其值小于 previous_name->len，后续使用 'ce->name + common' 和... |
| 424 | git-2.44.0 | refname_is_safe | cpp/no-space-for-terminator | 342 | FP | FP | 函数 `xmallocz` 的调用参数 `restlen` 是字符串 `rest` 的长度，而 `rest` 本身是一个以空字符结尾的 C 字符串。`normalize_path_copy` 函数期望目标缓冲区足够容纳源字符串及其空终... |
| 428 | git-2.44.0 | inherit_tracking | cpp/inconsistent-null-check | 224 | FP | FP | 被调用的函数 branch_get 在输入为 NULL 或空字符串时会返回 the_repository->remote_state->current_branch，该指针在代码上下文中应为有效对象，因此函数不会返回 NULL。切片内... |
| 427 | git-2.44.0 | setup_scoreboard | cpp/inconsistent-null-check | 2855 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，该条件已确保 `sb->final` 非空且其 OID 为空。`get_blame_suspects` 函数定义显示，当 `bl... |
| 432 | git-2.44.0 | do_fetch | cpp/inconsistent-null-check | 1611 | FP | FP | 告警点 `branch = branch_get(NULL)` 的返回值在后续的 `branch_has_merge_config(branch)` 调用中被检查，该函数内部已包含对 `branch` 是否为空的检查（`return ... |
| 433 | git-2.44.0 | get_ref_map | cpp/inconsistent-null-check | 550 | FP | FP | 切片代码显示，在调用 branch_get(NULL) 后，其返回值 branch 被直接传递给 branch_has_merge_config 函数。该函数内部已包含对 branch 指针的显式空值检查（`return branch... |
| 435 | git-2.44.0 | refspec_append_mapped | cpp/inconsistent-null-check | 88 | FP | FP | 被调用的branch_get函数内部已对空指针输入进行了检查，并始终返回一个有效的struct branch指针（例如，当name为NULL或空时返回current_branch），因此调用后无需进行空指针检查。 |
| 434 | git-2.44.0 | cmd_merge | cpp/inconsistent-null-check | 1638 | FP | FP | 切片代码显示，在调用 `repo_get_merge_bases` 后，其返回值 `common_one` 被立即解引用（`common_one->item`），但在此之前，代码逻辑（`if (!oideq(&common_item-... |
| 437 | git-2.44.0 | reset_tree | cpp/inconsistent-null-check | 283 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将结果传递给 parse_tree 函数进行校验，若解析失败则返回错误。这相当于对返回值进行了间接的 null 检查，因此告警是误报。 |
| 436 | git-2.44.0 | do_create_stash | cpp/inconsistent-null-check | 1378 | FP | FP | 代码中`head_commit`变量在后续多处被直接解引用（如`head_commit->object.oid`），若其为NULL将导致崩溃。但切片显示`info->b_commit`是函数参数，其来源未知，无法确认`lookup_c... |
| 440 | git-2.44.0 | update_one | cpp/inconsistent-null-check | 325 | FP | FP | find_subtree 在 create=1 模式下被调用，根据其定义，当 create 为真时，函数会分配并返回一个新的子树节点，不会返回 NULL。因此，对返回值的空指针检查是不必要的，告警属于误报。 |
| 441 | git-2.44.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2722 | FP | FP | lookup_commit 函数在对象不存在时会创建新对象并返回，不会返回 NULL。代码后续使用 graph_commit 时，主要进行数据比较和报告生成，不依赖其非空性，因此空值检查在此上下文中不必要。 |
| 442 | git-2.44.0 | ahead_behind | cpp/inconsistent-null-check | 1010 | FP | FP | 函数 `queue_has_nonstale` 在 while 循环条件中已确保队列非空且包含非 STALE 提交，`prio_queue_get` 在队列非空时返回有效指针，NULL 检查在此上下文中是多余的。 |
| 443 | git-2.44.0 | paint_down_to_common | cpp/inconsistent-null-check | 78 | FP | FP | 函数 `queue_has_nonstale` 确保队列非空时才进入循环，且 `prio_queue_get` 在队列为空时返回 NULL 的逻辑已被前置条件防护，因此对返回值的显式 NULL 检查是多余的。 |
| 439 | git-2.44.0 | write_bundle_refs | cpp/inconsistent-null-check | 428 | FP | FP | 在调用 `lookup_commit_reference` 后，其返回值 `one` 被立即用于与 `e->item` 进行指针相等性比较 (`if (e->item == &(one->object))`)。如果 `lookup_c... |
| 444 | git-2.44.0 | unparse_commit | cpp/inconsistent-null-check | 179 | FP | FP | 函数 `lookup_commit` 在内部已处理了 `lookup_object` 返回 `NULL` 的情况，此时会调用 `create_object` 创建一个新对象并返回，因此其返回值不会为 `NULL`。切片代码中 `c` ... |
| 445 | git-2.44.0 | clear_common_flag | cpp/inconsistent-null-check | 2124 | FP | FP | 代码在调用 lookup_object 前，通过 while ((oid = oidset_iter_next(&iter))) 确保 oid 来自有效的对象集合，且该集合中的对象应已存在于哈希表中。因此，lookup_object ... |
| 446 | git-2.44.0 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 141 | FP | FP | 在调用 parse_object 后，代码立即访问了 tag->tagged 成员，这隐含了对 tag 指针的非空检查；如果 parse_object 返回 NULL，解引用 tag->tagged 会导致崩溃，但代码逻辑表明此路径仅... |
| 447 | git-2.44.0 | find_merge_parents | cpp/inconsistent-null-check | 614 | FP | FP | 切片代码显示，parse_object 返回的 obj 指针在后续代码中仅用于获取其 oid 成员（&obj->oid），该操作在 obj 为 NULL 时会导致崩溃。然而，obj 被立即传递给 repo_peel_to_type 函... |
| 449 | git-2.44.0 | get_parent | cpp/inconsistent-null-check | 1063 | FP | FP | 切片代码显示，在调用 `lookup_commit_reference` 后，其返回值 `commit` 立即被传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 函数会检查提交对象的有效... |
| 448 | git-2.44.0 | get_rev | cpp/inconsistent-null-check | 187 | FP | FP | 切片代码显示，在调用 `prio_queue_get` 后，其返回值 `entry` 被直接解引用（`entry->commit`），这表明代码逻辑假设 `prio_queue_get` 在此上下文中不会返回 NULL。结合循环条件 ... |
| 450 | git-2.44.0 | show_ambiguous_object | cpp/inconsistent-null-check | 422 | FP | FP | 在调用 `lookup_tag` 后，代码立即检查 `!parse_tag(tag) && tag->tag`，这隐含了对 `tag` 指针的有效性检查，因为 `parse_tag` 函数内部会处理 `tag` 为 NULL 的情况（... |
| 451 | git-2.44.0 | fill_bitmap_commit | cpp/inconsistent-null-check | 416 | FP | FP | 切片代码显示，调用 prio_queue_get 的循环条件为 `while (queue->nr)`，该条件在 prio_queue_get 函数内部同样存在（`if (!queue->nr) return NULL;`），因此当 ... |
| 453 | git-2.44.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 686 | FP | FP | 根据提供的lookup_commit函数定义，该函数内部已处理了空对象指针的情况（若obj为空则创建新对象），因此调用方不检查返回值是安全的，不会导致空指针解引用。 |
| 452 | git-2.44.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3256 | FP | FP | 函数 `lookup_decoration` 在内部已对空装饰表（`!n->size`）和未找到的条目（`!ref->base`）返回 NULL，调用方 `leave_one_treesame_to_parent` 虽未显式检查返回值... |
| 454 | git-2.44.0 | <global> | cpp/inconsistent-null-check | 27 | FP | FP | 函数 `lookup_commit` 在内部已处理空指针情况：若 `lookup_object` 返回 NULL，它会调用 `create_object` 创建新对象并返回，因此调用方无需额外检查 NULL。切片代码中直接使用返回值是... |
| 455 | git-2.44.0 | test_ctype_isxdigit | cpp/overflow-buffer | 59 | FP | FP | 宏定义中的循环索引 i 范围是 0 到 255，不会产生负索引。对 EOF 的调用 `func(EOF)` 是独立的检查，不涉及数组访问，因此告警是误报。 |
| 457 | git-2.44.0 | test_ctype_iscntrl | cpp/overflow-buffer | 57 | FP | FP | 宏展开后，循环变量 i 的范围是 0 到 255，且对 EOF 的调用是 `func(EOF)`，并非数组索引操作。告警所指的负索引 -1 可能源于工具对宏或 EOF 值的误解，在可见的切片逻辑中不存在实际的负索引访问。 |
| 456 | git-2.44.0 | test_ctype_ispunct | cpp/overflow-buffer | 58 | FP | FP | 切片代码显示，循环变量 i 的范围是 0 到 255，且函数 func(i) 的索引 i 来自此循环，不会出现负索引。对 EOF 的调用 func(EOF) 是独立检查，但宏定义中未显示 func 的实现，无法确认其内部是否存在负索引... |
| 458 | git-2.44.0 | test_ctype_is_pathspec_magic | cpp/overflow-buffer | 53 | FP | FP | 宏定义中的循环索引 i 范围是 0 到 255，且对 EOF 的调用是显式检查，不会导致负索引访问数组。告警是对宏展开的误读。 |
| 461 | git-2.44.0 | test_ctype_isalnum | cpp/overflow-buffer | 50 | FP | FP | 宏定义中的循环索引 i 范围是 0 到 255，不会产生负索引。对 EOF 的调用 `func(EOF)` 是检查函数对 EOF 输入的处理，属于有效的边界测试，并非对数组的负索引访问。 |
| 459 | git-2.44.0 | test_ctype_is_regex_special | cpp/overflow-buffer | 52 | FP | FP | 告警指出的负索引访问发生在宏定义 `TEST_CTYPE_FUNC` 的循环中，循环变量 `i` 的范围是 0 到 255，而 `EOF` 是一个常量（通常为 -1），对 `func(EOF)` 的调用是函数调用，并非对数组 `str... |
| 460 | git-2.44.0 | test_ctype_is_glob_special | cpp/overflow-buffer | 51 | FP | FP | 告警指出的负索引访问发生在宏 TEST_CTYPE_FUNC 中，当 func 参数为 EOF（通常定义为 -1）时，会调用 func(EOF)。切片显示，该宏用于测试字符分类函数，func 是函数指针，其内部实现（如 is_in）可... |
| 462 | git-2.44.0 | test_ctype_isalpha | cpp/overflow-buffer | 49 | FP | FP | 告警指出的负索引访问发生在宏定义中，用于检查EOF（值为-1）作为函数参数，这是对函数`func`的合法调用，并非对数组的直接负索引访问。代码逻辑正确，是静态分析工具对宏展开的误判。 |
| 464 | git-2.44.0 | test_ctype_isdigit | cpp/overflow-buffer | 47 | FP | FP | 切片代码显示，循环变量 i 的范围是 0 到 255，且函数 func 被调用时参数为 i 或 EOF。EOF 是一个常量（通常为 -1），但代码中通过 check(!func(EOF)) 明确检查了 EOF 的情况，这是预期的测试逻... |
| 463 | git-2.44.0 | test_ctype_isspace | cpp/overflow-buffer | 48 | FP | FP | 切片代码显示，宏 `TEST_CTYPE_FUNC` 中的循环索引 `i` 范围是 0 到 255，且对 `func(EOF)` 的调用是显式检查 EOF 常量，并非通过数组索引访问。告警提及的负索引 -1 可能对应 EOF 值，但此... |
| 467 | git-2.44.0 | should_prune_worktree | cpp/invalid-pointer-deref | 791 | FP | FP | 指针 `path` 由 `xmallocz(len)` 分配，其大小为 `len+1` 字节，而写入 `path[len] = '\0'` 是在循环递减 `len` 之后执行的，确保 `len` 小于原始分配大小，因此写入操作在分配的... |
| 468 | curl-8_13_0 | <global> | cpp/invalid-pointer-deref | 89 | FP | FP | 切片代码显示，在写入 `newname[len]` 之前，已通过 `malloc(newlen)` 分配了 `newlen` 字节的内存，其中 `newlen = len + 13`。因此，`newname[len]` 的写入位置在分... |
| 469 | curl-8_15_0 | <global> | cpp/invalid-pointer-deref | 85 | FP | FP | 切片代码显示，在写入 `newname[len]` 之前，已通过 `newlen = len + 13` 为 `newname` 分配了足够的空间（`newlen` 字节），且 `len` 是原始文件名长度，因此 `newname[l... |
| 471 | curl-8_9_1 | <global> | cpp/invalid-pointer-deref | 96 | FP | FP | 切片代码显示，在写入 `newname[len]` 之前，已经通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen = len + 13`，确保了 `len` 索引处是分配内存范围内的有效位置，因此该写入操作... |
| 473 | curl-8_7_1 | <global> | cpp/invalid-pointer-deref | 96 | FP | FP | 代码中 `newname[len] = '.';` 的写入操作是安全的。`newname` 通过 `malloc(newlen)` 分配，其中 `newlen = len + 13`，确保至少有 `len + 1` 的空间。写入索引 ... |
| 472 | curl-8_7_1 | Curl_splayremove | cpp/inconsistent-null-check | 270 | FP | FP | 在调用 `Curl_splay` 前，函数已通过 `if(!t ｜｜ !removenode)` 和 `if(t != removenode)` 对输入进行了有效性检查，确保了 `t->smaller` 在调用点不为空。此外，被调用的... |
| 474 | curl-8_11_1 | <global> | cpp/invalid-pointer-deref | 91 | FP | FP | 告警指出的写入位置 `newname[len]` 是合法的，因为 `newname` 分配的大小为 `newlen`（等于 `len + 13`），而 `len` 是原始文件名长度，`newname[len]` 是分配缓冲区内的第一个... |
| 475 | nginx-1.27.2 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 切片代码中的注释明确指出数组有4个预分配的空元素，因此push操作不会失败，无需进行空指针检查。这是代码逻辑保证的安全情况。 |
| 477 | nginx-1.27.4 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3521 | FP | FP | 切片代码中的注释明确指出数组有4个预分配的空元素，因此push操作不会失败，无需检查NULL。代码逻辑保证了安全性，属于工具误报。 |
| 476 | nginx-1.29.0 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3565 | FP | FP | 切片代码中的注释明确指出数组已预分配了4个空元素，因此push操作不会失败，无需进行空指针检查。这是代码逻辑保证的安全情况。 |
| 478 | nginx-1.25.4 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 切片代码中明确注释说明数组有4个预分配的空元素，因此push操作不会失败，无需进行空指针检查。 |
| 479 | nginx-1.27.0 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 切片代码中的注释明确指出数组有4个预分配的空元素，因此push操作不会失败，无需进行空指针检查。这是代码逻辑保证的安全情况。 |
| 482 | vim-9.1.0550 | findmatchlimit | cpp/offset-use-before-range-check | 2522 | FP | FP | 切片代码显示，在访问 `linep[pos.col]` 和 `linep[pos.col + 1]` 之前，存在对 `pos.col` 的边界检查和调整逻辑（例如 `if (linep[pos.col] == NUL && pos.c... |
| 483 | vim-9.1.0550 | common_function | cpp/inconsistent-null-check | 4856 | FP | FP | 代码在调用 vim_strsave 后，其返回值 'name' 在后续逻辑中会被 vim_free 释放，且存在多处错误处理路径确保内存释放，因此该未检查 null 的调用在实际执行中不会导致空指针解引用或内存泄漏。 |
| 481 | vim-9.1.0550 | <global> | cpp/redundant-null-check-simple | 3576 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 在解引用前已通过 `if (*inc_opt != NUL)` 进行了非空检查，且 `inc_opt` 被赋值为 `p_inc` 或 `cu... |
| 480 | vim-9.1.0550 | <global> | cpp/redundant-null-check-simple | 3494 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 变量在解引用前已通过条件 `if (*inc_opt != NUL)` 确保其非空，且 `inc_opt` 被赋值为 `p_inc` 或 `... |
| 485 | vim-9.1.0550 | get_isolated_shell_name | cpp/inconsistent-null-check | 2695 | FP | FP | 函数 `gettail` 已对 NULL 输入进行了检查并返回空字符串，因此 `vim_strsave` 的输入不会是 NULL，其返回值也无需额外检查。 |
| 488 | vim-9.1.0550 | did_set_background | cpp/inconsistent-null-check | 1079 | FP | FP | 切片代码显示，在调用 vim_strsave 后，其返回值 p_bg 立即被传递给 check_string_option 函数。该函数明确检查指针是否为 NULL，并在为 NULL 时将其赋值为 empty_option，从而确保了... |
| 489 | vim-9.1.0550 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 调用 find_win_by_nr_or_id 后，其返回值 wp->w_popup_prop_win 立即被传递给 win_valid_any_tab 函数进行有效性检查，该检查已隐含了对 NULL 的处理（win_valid_an... |
| 487 | vim-9.1.0550 | did_set_cryptmethod | cpp/inconsistent-null-check | 1766 | FP | FP | 代码中调用 vim_strsave 的参数是字符串字面量 "zip"，分配失败的可能性极低，且即使失败，后续对 p_cm 的使用（如 STRCMP）也能安全处理 NULL 指针（因为 p_cm 可能为 NULL，但 STRCMP 宏使... |
| 490 | vim-9.1.0550 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 告警指出的 `regnext` 调用未检查 null，但切片代码显示 `next` 变量在后续的 `if (scan == NULL)` 和 `if (got_int ｜｜ scan == NULL)` 等条件中已被检查，且 `reg... |
| 492 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 切片代码显示，在调用regnode(NOTHING)之前，存在对reg_toolong全局标志的检查，若该标志为真则函数提前返回NULL。这表明代码逻辑已处理了可能导致regnode失败的条件，因此该处未检查返回值是安全的。 |
| 493 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在切片代码中，`regnext`的返回值被赋值给循环变量`br`，而`br`在后续循环条件`br != lastnode`中被使用。该条件检查`br`是否为NULL（因为`lastnode`是一个非NULL指针），这间接构成了对`re... |
| 491 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 切片代码显示，在调用 `regnode(BRANCH)` 后，其返回值 `br` 被立即用于条件判断 `if (ret == NULL)` 和后续的 `regtail` 操作，但并未直接与 NULL 进行比较。然而，`regnode`... |
| 494 | vim-9.1.0550 | win_redr_custom | cpp/inconsistent-null-check | 1115 | FP | FP | 代码在调用 vim_strsave 后立即将返回值传递给 vim_free 进行释放，虽然未显式检查 NULL，但 vim_free 内部已处理 NULL 指针（if (x != NULL)），因此不会导致空指针解引用。 |
| 495 | vim-9.1.0550 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 函数 `getroom` 在内存分配失败时会返回 NULL，但调用点 `get_wordnode` 在后续的 `#ifdef SPELL_PRINTTREE` 代码块中明确检查了 `n != NULL` 后才使用 `n`，且函数最终返... |
| 496 | vim-9.1.0550 | do_tag | cpp/inconsistent-null-check | 639 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续逻辑中被立即传递给 `vim_free(tofree)`，而 `tofree` 被赋值为 `name`。这表明代码遵循了分配-释放模式，且 `name` 在释放前... |
| 497 | vim-9.1.0550 | define_function | cpp/inconsistent-null-check | 5306 | FP | FP | 告警指出的 `vim_strchr` 调用未检查空指针，但切片代码显示该调用结果仅用于条件判断 `!= NULL`，并未解引用，因此不存在空指针解引用风险。 |
| 501 | vim-9.1.0550 | ex_history | cpp/unsafe-strcat | 780 | FP | FP | 切片代码显示，在调用STRCAT前，已通过条件判断确保目标缓冲区IObuff有足够空间：当字符串长度超过限制时，会调用trunc_string进行截断；否则才执行STRCAT。这保证了不会发生缓冲区溢出。 |
| 500 | vim-9.1.0550 | barline_parse | cpp/inconsistent-null-check | 1122 | FP | FP | 切片代码显示，在调用 vim_strsave 之前，已通过条件 `(s != buf && allocated && !converted)` 确保 s 不是来自已分配的 buf 且未经过转换，此时 allocated 为 TRUE ... |
| 502 | vim-9.1.0550 | helptags_one | cpp/unsafe-strcat | 971 | FP | FP | NameBuff 是一个全局缓冲区，其大小定义为 MAXPATHL（通常足够大），且告警处的 STRCAT 操作拼接的是固定字符串 "/**/*" 和参数 ext，这些字符串长度有限且受控，不会导致缓冲区溢出。 |
| 504 | vim-9.1.0550 | set_init_default_backupskip | cpp/unsafe-strcat | 178 | FP | FP | 切片代码显示，在调用STRCAT前，已通过ga_grow(&ga, len)确保目标缓冲区有足够空间，且len已精确计算了源字符串长度和分隔符。代码逻辑保证了缓冲区不会溢出。 |
| 506 | vim-9.1.0550 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy(newword, ae->ae_add, MAXWLEN - 1)或vim_strncpy(newword, word, MAXWLEN - 1)确保目标缓冲... |
| 518 | vim-9.1.0550 | globpath | cpp/unbounded-write | 3783 | FP | FP | 切片代码显示，在调用STRCAT前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度不会超过MAXPATHL，因此不存在... |
| 523 | vim-9.1.0550 | do_string_sub | cpp/unbounded-write | 7697 | FP | FP | 在调用STRCPY前，代码已通过ga_grow确保目标缓冲区有足够空间容纳剩余字符串tail，因此不会发生缓冲区溢出。 |
| 530 | vim-9.1.0550 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已通过alloc(len)为目标缓冲区buf分配了精确计算的长度len，且后续使用vim_snprintf或STRCPY/STRCAT时，buf和len均被传递，确保了缓冲区大小足... |
| 538 | vim-9.1.0550 | discard_exception | cpp/unbounded-write | 642 | FP | FP | STRCPY 的目标缓冲区 IOBuff 在 smsg 函数中通过 vim_vsnprintf(IObuff, IOSIZE, ...) 使用，表明 IOBuff 的大小为 IOSIZE。源字符串 saved_IObuff 是 IOB... |
| 547 | vim-9.1.0550 | vim_rename | cpp/unbounded-write | 3839 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL+1）不会溢出。 |
| 558 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 801 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，已通过STRLEN检查了源字符串长度，并确保目标缓冲区大小（MAXPATHL）足以容纳，从而防止了缓冲区溢出。 |
| 559 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 815 | FP | FP | 切片代码中，在调用STRCAT（即strcat）前，均存在明确的长度检查（STRLEN(file_path) + STRLEN(...) < MAXPATHL），确保目标缓冲区不会溢出。因此该告警为误报。 |
| 562 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 1104 | FP | FP | 切片代码中，所有对STRCPY的调用前都进行了明确的长度检查（使用STRLEN并与MAXPATHL比较），确保目标缓冲区不会溢出。因此，告警是误报。 |
| 561 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 938 | FP | FP | 切片代码中，在调用STRCAT（即strcat）前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(search_ctx->ffsc_file_to_search) + 1 < MAXPATHL`），确... |
| 563 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 1106 | FP | FP | 切片代码中，在调用STRCAT前，存在明确的长度检查（STRLEN(file_path) + STRLEN(search_ctx->ffsc_fix_path) < MAXPATHL），确保目标缓冲区不会溢出。因此，该告警为误报。 |
| 566 | vim-9.1.0550 | <global> | cpp/unbounded-write | 544 | FP | FP | 切片代码显示，STRCAT 的目标缓冲区 ff_expand_buffer 在告警行之前已通过 alloc(MAXPATHL) 分配了固定大小 MAXPATHL，且其使用前通过 STRLEN 计算了当前长度，并确保拼接的源字符串长度可... |
| 583 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 987 | FP | FP | NameBuff 是一个全局缓冲区，其大小定义为 MAXPATHL（通常为 260 或更大），而 tagfname 是函数参数，其长度在调用上下文中是已知且受控的（例如 "tags" 或 "tags-fr"）。STRCAT 操作前，N... |
| 585 | vim-9.1.0550 | highlight_set_startstop_termcode | cpp/unbounded-write | 1477 | FP | FP | 切片代码中，在调用STRCAT(buf, p)前，已通过条件`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了目标缓冲区buf（大小为100）的剩余空间，确保拼接后不会溢出。该防护机制使告警无效。 |
| 589 | vim-9.1.0550 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码已通过alloc函数为buf分配了精确计算所需的内存大小（amt），sprintf写入的格式化字符串长度与计算值完全匹配，不存在缓冲区溢出风险。 |
| 595 | vim-9.1.0550 | findswapname | cpp/unbounded-write | 4967 | FP | FP | STRCPY 的目标缓冲区 fname2 是通过 alloc(n + 2) 分配的，其大小比源字符串 fname 的长度 n 多 2，确保了足够的空间。因此，该 strcpy 操作不会导致缓冲区溢出。 |
| 603 | vim-9.1.0550 | expand_env_esc | cpp/unbounded-write | 1632 | FP | FP | 在调用STRCPY(dst, var)之前，代码已通过条件`STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen`检查了目标缓冲区dst的剩余空间，确保不会发生缓冲区溢出。 |
| 608 | vim-9.1.0550 | add_to_showcmd | cpp/unbounded-write | 1760 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已通过计算old_len和extra_len检查了缓冲区溢出风险，并在溢出时使用mch_memmove移动内容以腾出空间，确保了目标缓冲区showcmd_buf不会溢出。 |
| 615 | vim-9.1.0550 | option_value2string | cpp/unbounded-write | 8157 | FP | FP | 切片代码显示，告警点位于处理数值型选项（P_NUM）的分支中，其目标缓冲区 `NameBuff` 的大小未在切片中明确给出，但该分支仅在 `wc` 非零时调用 `STRCPY`，且 `transchar` 函数返回的字符串长度有限（通... |
| 642 | vim-9.1.0550 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数 getroom 已根据源字符串长度（STRLEN(s) + 1）分配了足够的内存，STRCPY 操作不会导致缓冲区溢出。 |
| 647 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区大小由getroom函数动态分配，其大小等于源字符串长度加1，因此不会发生缓冲区溢出。告警是基于静态模式匹配，未考虑动态分配逻辑。 |
| 650 | vim-9.1.0550 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | STRCPY 的目标缓冲区 sft->sft_word 的大小是动态分配的，分配大小为 offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1，恰好能容纳源字符串 goodword 及... |
| 652 | vim-9.1.0550 | concat_str | cpp/unbounded-write | 768 | FP | FP | 函数内通过alloc为目标缓冲区分配了精确大小（str1长度+str2长度+1），且STRCPY宏展开为strcpy，但源字符串长度已通过STRLEN计算并用于分配，因此不会发生缓冲区溢出。 |
| 672 | vim-9.1.0550 | update_snapshot | cpp/invalid-pointer-deref | 2068 | FP | FP | 切片代码显示，在访问 p[pos.col + 1] 之前，已通过条件 `width == 2` 确保 `pos.col + 1` 小于 `len`（因为 `width` 是当前字符的单元格宽度，且循环条件为 `pos.col < le... |
| 766 | vim-9.1.1591 | cs_make_vim_style_matches | cpp/unbounded-write | 1647 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了该大小的内存（buf = alloc(amt)），确保了目标缓冲区大小与格式化字符串长度完全匹配，不存在缓冲区溢出的风险。 |
| 846 | vim-9.1.1040 | <global> | cpp/redundant-null-check-simple | 3502 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 在解引用前已通过条件 `if (*inc_opt != NUL)` 确保其非空，因此解引用是安全的，空指针检查确实是冗余的，属于误报。 |
| 848 | vim-9.1.1040 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | FP | FP | 切片代码显示，在访问 `linep[pos.col]` 和 `linep[pos.col + 1]` 之前，存在对 `pos.col` 的边界检查（例如 `if (pos.col > 0)` 和 `if (linep[pos.col ... |
| 847 | vim-9.1.1040 | <global> | cpp/redundant-null-check-simple | 3584 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 指针在解引用前已通过 `if (*inc_opt != NUL)` 进行了有效性检查，该检查确保了指针非空，因此解引用是安全的，空指针检查是... |
| 849 | vim-9.1.1040 | common_function | cpp/inconsistent-null-check | 5061 | FP | FP | 代码在调用 vim_strsave 后，将结果赋值给变量 'name'，并在后续多个分支中检查了 'name' 是否为 NULL，例如在 'if (pt == NULL)' 和 'if (pt->pt_argv == NULL)' 后... |
| 854 | vim-9.1.1040 | did_set_background | cpp/inconsistent-null-check | 1083 | FP | FP | 切片代码显示，vim_strsave的返回值立即传递给check_string_option函数，该函数会检查指针是否为NULL并将其替换为empty_option，从而确保了后续使用p_bg时的安全性。 |
| 851 | vim-9.1.1040 | get_isolated_shell_name | cpp/inconsistent-null-check | 2710 | FP | FP | 函数 `vim_strsave` 的返回值 `p` 被直接返回给调用者，由调用者负责检查空指针。切片中 `get_isolated_shell_name` 的调用方信息缺失，无法确认调用者是否检查，但告警规则仅基于内部一致性统计，代码... |
| 853 | vim-9.1.1040 | did_set_cryptmethod | cpp/inconsistent-null-check | 1832 | FP | FP | 代码中 `vim_strsave` 的参数是字符串字面量 "zip"，分配失败的可能性极低，且即使失败，后续对 `p_cm` 的使用（如 `STRCMP`）也仅涉及读取其内容，不会导致空指针解引用等崩溃风险。 |
| 855 | vim-9.1.1040 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 代码在调用 `find_win_by_nr_or_id` 后，立即使用 `win_valid_any_tab` 检查了返回的窗口指针的有效性，并在无效时回退到 `curwin`。这构成了有效的空值检查和安全回退机制，因此告警是误报。 |
| 856 | vim-9.1.1040 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 代码中已对scan指针进行了NULL检查（if (got_int ｜｜ scan == NULL)），且regnext函数内部也返回NULL，因此该调用点不需要额外的NULL检查，属于工具误报。 |
| 858 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 代码中 `regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `JUST_CALC_SIZE`，不会返回 NULL。告警点 `br = regnode(NOTHING... |
| 857 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 切片代码显示，在调用 `regnode(BRANCH)` 后，其返回值 `br` 被立即用于条件判断 `if (ret == NULL)` 和后续的 `regtail` 调用，但并未直接用于可能导致空指针解引用的危险操作。`regno... |
| 859 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在切片代码的上下文中，`br`变量来源于`regnode`调用或`OPERAND`宏，这些来源在`reg_toolong`为假时不会返回NULL。告警点位于一个循环内，该循环在`ret != JUST_CALC_SIZE`且`reg_... |
| 860 | vim-9.1.1040 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 代码切片显示，在调用 getroom 后，其返回值被赋值给变量 n，并且在后续的 SPELL_PRINTTREE 宏条件编译块中，存在对 n 是否为 NULL 的显式检查（if (n != NULL)）。这表明代码逻辑已经考虑并处理了... |
| 861 | vim-9.1.1040 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续逻辑中被立即赋值给 `tofree`，随后 `name` 被重新赋值为 `tag`，因此原始分配的内存指针已通过 `tofree` 被管理，并将在函数末尾通过 `... |
| 862 | vim-9.1.1040 | define_function | cpp/inconsistent-null-check | 5403 | FP | FP | 告警指出的 vim_strchr 调用结果未检查 NULL，但切片代码显示该调用仅用于检查字符 '(' 是否存在，其返回值被直接用于逻辑判断（!= NULL），这属于有效的使用模式，并非必须检查 NULL 的上下文。 |
| 867 | vim-9.1.1040 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 变量 `name` 指向的字符串长度是已知且有限的（如 "F1"、"X" 或单个字符的 `namebuf`），且 `buf` 在首次使用前已被初始化为空字符串。虽然切片未显示 `buf` 的大小，但根据函数逻辑，拼接后的字符串总长度极... |
| 866 | vim-9.1.1040 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | STRCAT宏被用于拼接已知长度的目录路径和固定字符串，目标缓冲区NameBuff的大小为MAXPATHL，而拼接的字符串长度由输入参数dir和ext决定，切片中未显示对最终长度是否超过MAXPATHL的检查。然而，在代码中，Name... |
| 868 | vim-9.1.1040 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限内容，并确保其以NUL结尾，且缓冲区大小为MAXWLEN。结合上下文对源字符串p（来自word）长度的检查（如STRLEN... |
| 864 | vim-9.1.1040 | exec_instructions | cpp/inconsistent-null-check | 3383 | FP | FP | alloc_clear 返回的指针被直接赋值给 tv->vval.v_object，后续代码立即访问其成员（如 obj_class），若 alloc_clear 返回 NULL 将导致空指针解引用。但切片中可见在调用 alloc_cl... |
| 879 | vim-9.1.1040 | globpath | cpp/unbounded-write | 3809 | FP | FP | 切片代码显示，在调用STRCAT(buf, file)之前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区`buf`（大小为MAXPATHL）的剩余空间，确保... |
| 890 | vim-9.1.1040 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过alloc(len)为目标缓冲区buf分配了精确计算的长度len，且后续使用vim_snprintf和STRCPY/STRCAT时均未超过此预分配大小。len的计算已考虑了... |
| 898 | vim-9.1.1040 | discard_exception | cpp/unbounded-write | 646 | FP | FP | STRCPY 的目标缓冲区 IOBuff 在切片中可见其大小由宏 IOSIZE 定义，且源字符串 saved_IObuff 是之前通过 vim_strsave(IObuff) 保存的副本，长度与原始 IOBuff 相同，因此复制不会导... |
| 905 | vim-9.1.1040 | vim_rename | cpp/unbounded-write | 3858 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过条件`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串的长度，确保其不会超过目标缓冲区tempname（大小为MAXPATHL + 1）的容量，因此... |
| 916 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 805 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）前，已通过条件`STRLEN(search_ctx->ffsc_start_dir) + 1 < MAXPATHL`检查了源字符串长度，确保不会溢出目标缓冲区file_path（大小为M... |
| 918 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 940 | FP | FP | 切片代码中，所有对STRCPY（即strcpy）的调用前都进行了明确的长度检查（例如使用STRLEN计算长度并与MAXPATHL比较），确保目标缓冲区不会溢出。因此，这些调用是安全的，属于误报。 |
| 917 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 819 | FP | FP | 切片代码中，在调用STRCAT（即strcat）前，已通过条件`STRLEN(file_path) + STRLEN(stackp->ffs_fix_path) + 1 < MAXPATHL`明确检查了目标缓冲区`file_path`... |
| 919 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 942 | FP | FP | 切片代码中，在调用STRCAT（即strcat）前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(search_ctx->ffsc_file_to_search) + 1 < MAXPATHL`），确... |
| 920 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 1110 | FP | FP | 切片代码中所有STRCPY调用前均存在明确的长度检查（如STRLEN(...) + ... < MAXPATHL），确保目标缓冲区不会溢出。告警点位于第1110行，其前一行（1109行）已通过长度检查，因此是安全的。 |
| 921 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 1112 | FP | FP | 切片代码中，所有对STRCAT的调用前都有明确的长度检查（如`STRLEN(file_path) + STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区不会溢出。告警点位于条件分支内，该条件已通过长度校验，因此是... |
| 943 | vim-9.1.1040 | highlight_set_startstop_termcode | cpp/unbounded-write | 1481 | FP | FP | 切片代码显示，在调用STRCAT(buf, p)之前，已通过条件`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了目标缓冲区buf（大小为100字节）的剩余空间，确保拼接后不会发生溢出。该防护... |
| 947 | vim-9.1.1040 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...），并分配了相应大小的内存（buf = alloc(amt)），确保了目标缓冲区足以容纳格式化后的字符串，因此不存在缓冲区溢出风险。 |
| 961 | vim-9.1.1040 | expand_env_esc | cpp/unbounded-write | 1647 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`(STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen)`检查了目标缓冲区`dst`的剩余空间，确保复制不会溢出。该防护... |
| 966 | vim-9.1.1040 | add_to_showcmd | cpp/unbounded-write | 1763 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已计算了目标缓冲区showcmd_buf的当前长度old_len和待追加字符串p的长度extra_len，并检查了溢出（overflow）。若溢出发生，会通过mch_memmove... |
| 1000 | vim-9.1.1040 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数 getroom_save 在调用 STRCPY（即 strcpy）前，已通过 getroom 分配了长度为 STRLEN(s) + 1 的内存，目标缓冲区大小与源字符串长度精确匹配，因此不会发生缓冲区溢出。 |
| 1001 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 切片代码显示，strcat操作的目标缓冲区p是通过getroom(spin, ...)动态分配的，其大小已根据源字符串长度计算并预留了足够空间（包括分隔符和终止符），因此不会发生缓冲区溢出。 |
| 1005 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 切片代码显示，strcpy的目标缓冲区是动态分配的，其大小通过STRLEN(items[0]) + STRLEN(items[1]) + 3计算，且源字符串来自items[0]和items[1]，这些是解析自固定格式的affix文件行... |
| 1010 | vim-9.1.1040 | concat_str | cpp/unbounded-write | 811 | FP | FP | 函数内已通过alloc为目标缓冲区分配了精确大小（str1与str2长度之和加1），STRCPY操作不会导致缓冲区溢出。 |
| 1011 | vim-9.1.1040 | concat_str | cpp/unbounded-write | 813 | FP | FP | 函数内通过alloc为目标缓冲区分配了足够容纳str1和str2拼接后字符串的空间（包括结尾空字符），STRCPY（即strcpy）的目标地址和源字符串长度均受控，不会发生缓冲区溢出。 |
| 1020 | vim-9.1.1040 | fname_trans_sid | cpp/unbounded-write | 2212 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，存在明确的长度检查 `if (i + STRLEN(name + llen) < FLEN_FIXED)`，确保目标缓冲区`fname_buf`有足够空间，因此不会发生缓冲区溢出。 |
| 1031 | vim-9.1.1330 | <global> | cpp/redundant-null-check-simple | 3508 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 在解引用前已通过条件 `if (*inc_opt != NUL)` 确保其非空，因此解引用是安全的，空指针检查确实是冗余的，属于误报。 |
| 1032 | vim-9.1.1330 | <global> | cpp/redundant-null-check-simple | 3590 | FP | FP | 告警指出的空指针检查冗余，是因为在切片代码中，变量 `inc_opt` 在解引用前已被明确赋值（来自 `curbuf->b_p_inc` 或 `p_inc`），且解引用前有检查 `*inc_opt != NUL`，因此解引用点 `in... |
| 1034 | vim-9.1.1330 | common_function | cpp/inconsistent-null-check | 5228 | FP | FP | 切片代码显示，在调用 vim_strsave 后，其返回值 'name' 在多个分支中都被正确传递给 vim_free 进行释放，包括在错误处理路径和成功路径中。这表明内存管理是完整的，告警所提示的 null 检查缺失在本上下文中不是... |
| 1033 | vim-9.1.1330 | findmatchlimit | cpp/offset-use-before-range-check | 2529 | FP | FP | 切片代码显示变量 `col` 在 `for (col = pos.col; ...)` 循环中被用作迭代变量，其初始值 `pos.col` 在循环前已通过边界检查（例如 `pos.col` 在多个分支中被调整以确保其指向有效字符），且... |
| 1039 | vim-9.1.1330 | did_set_background | cpp/inconsistent-null-check | 1086 | FP | FP | 切片代码显示，调用 `vim_strsave` 返回的指针 `p_bg` 立即被传递给 `check_string_option` 函数，该函数会检查指针是否为 NULL 并将其设置为安全值 `empty_option`，因此即使分配... |
| 1040 | vim-9.1.1330 | apply_move_options | cpp/inconsistent-null-check | 531 | FP | FP | 代码在调用 find_win_by_nr_or_id 后，立即使用 win_valid_any_tab 函数检查返回的窗口指针是否有效，若无效则回退到 curwin。这构成了有效的空值防护，因此告警为误报。 |
| 1041 | vim-9.1.1330 | <global> | cpp/inconsistent-null-check | 3339 | FP | FP | 告警点位于循环内，且循环条件已包含对scan是否为NULL的检查（if (got_int ｜｜ scan == NULL)），因此即使regnext返回NULL，后续代码也会因scan为NULL而提前退出循环，不会导致空指针解引用。 |
| 1043 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 切片代码显示，在调用 `regnode(NOTHING)` 之前，已有对 `reg_toolong` 全局标志的检查，若该标志为真则函数提前返回 NULL。这表明存在运行时防护机制，且告警点位于受保护的代码块内，因此该处未检查返回值是... |
| 1036 | vim-9.1.1330 | get_isolated_shell_name | cpp/inconsistent-null-check | 2710 | FP | FP | 函数 `gettail` 已对 `fname` 为 NULL 的情况进行了处理，返回空字符串，因此 `vim_strsave` 的参数不会是 NULL，其返回值 `p` 在后续分支中要么是 `vim_strsave` 的结果，要么是 ... |
| 1042 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 切片代码显示，在调用 `regnode(BRANCH)` 后，其返回值 `br` 被立即用于条件判断 `if (ret == NULL)` 和后续的 `regtail` 调用，这表明代码逻辑不依赖 `regnode` 返回空值来指示错... |
| 1044 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 切片代码显示，在调用 `regnext(br)` 之前，已经通过 `if (OP(br) == BRANCH)` 检查了节点类型，并且 `regnext` 函数内部有对 `reg_toolong` 等状态的检查并可能返回 NULL。更... |
| 1046 | vim-9.1.1330 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，对 `vim_strsave` 的返回值 `name` 的后续使用是安全的。`name` 被赋值给 `tofree` 后，在函数末尾通过 `vim_free(tofree)` 被正确释放，不存在因空指针解引用导致崩溃的风险。 |
| 1045 | vim-9.1.1330 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 函数 `getroom` 在内存分配失败时会返回 NULL，但调用点 `get_wordnode` 在 `#ifdef SPELL_PRINTTREE` 块中已对返回值 `n` 进行了非空检查（`if (n != NULL)`），且后... |
| 1047 | vim-9.1.1330 | define_function | cpp/inconsistent-null-check | 5486 | FP | FP | 代码中 `vim_strchr(p, '(')` 的返回值在多个地方被显式检查是否为 NULL，例如 `if (vim_strchr(p, '(') != NULL)` 和 `if (vim_strchr(p, '(') == NUL... |
| 1051 | vim-9.1.1330 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | STRCAT 宏是对标准 strcat 的包装，但切片代码显示其目标缓冲区 NameBuff 在每次使用前都通过 STRCPY 重新初始化，且其大小（MAXPATHL）在上下文中是已知的，足以容纳拼接后的路径字符串。 |
| 1052 | vim-9.1.1330 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 切片代码显示，变量`name`的来源是受控的：它要么指向静态字符串字面量（如"F1"），要么指向大小为2的局部数组`namebuf`（已正确终止）。`buf`参数在首次使用前被置为空字符串，且所有`strcat`操作拼接的字符串总长度... |
| 1053 | vim-9.1.1330 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限内容，并确保其以NUL结尾，且缓冲区大小为MAXWLEN。结合上下文，源字符串p是原始单词word经过安全截断（chop）... |
| 1061 | vim-9.1.1330 | buf_write | cpp/unbounded-write | 2568 | FP | FP | 切片代码中未发现对strcat的调用，告警提及的'call to strcat'在提供的代码片段中不存在。该告警可能是基于不完整或错误的代码分析产生的误报。 |
| 1064 | vim-9.1.1330 | globpath | cpp/unbounded-write | 3864 | FP | FP | 切片代码显示，在调用STRCAT(buf, file)之前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区buf的剩余空间，确保拼接后不会超过MAXPATHL... |
| 1066 | vim-9.1.1330 | win_redr_status_matches | cpp/unbounded-write | 682 | FP | FP | STRCPY宏的目标缓冲区`buf + len`和源字符串`transchar_byte(*s)`的长度均在切片代码中受控。`transchar_byte`函数返回的是单个字符的转义表示（如'\t'），其长度固定且很短，而目标位置`b... |
| 1075 | vim-9.1.1330 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 代码在调用STRCAT前已通过alloc(len)分配了足够大小的缓冲区，且len的计算已考虑了所有待拼接字符串的长度，因此不会发生缓冲区溢出。 |
| 1083 | vim-9.1.1330 | discard_exception | cpp/unbounded-write | 646 | FP | FP | 告警点`STRCPY(IObuff, saved_IObuff)`中的目标缓冲区`IObuff`是全局缓冲区，其大小`IOSIZE`在切片中未直接出现但可推断为固定大小；源字符串`saved_IObuff`是之前通过`vim_strs... |
| 1090 | vim-9.1.1330 | vim_rename | cpp/unbounded-write | 3861 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。 |
| 1104 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 切片代码显示，`res_cidfont->title` 和 `res_cidfont->version` 来自受控的资源文件解析（`prt_open_resource`），其长度在解析时已被限制（如 `vim_strncpy` 使用固... |
| 1110 | vim-9.1.1330 | do_helptags | cpp/unbounded-write | 1210 | FP | FP | STRCPY 宏的目标缓冲区 NameBuff 在代码中未定义大小，但根据上下文推断，它很可能是一个足够大的全局缓冲区（如 MAXPATHL），用于处理文件路径。告警点处的源字符串 dirname 是函数参数，其长度受限于文件系统路径... |
| 1114 | vim-9.1.1330 | highlight_set_startstop_termcode | cpp/unbounded-write | 1485 | FP | FP | 切片代码中，在调用STRCAT(buf, p)前，已通过条件`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了目标缓冲区buf（大小为100字节）的剩余空间，确保拼接后不会溢出。因此，该告警为误报。 |
| 1118 | vim-9.1.1330 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...）并分配了相应大小的内存（buf = alloc(amt)），确保了目标缓冲区足够大，不会发生溢出。 |
| 1124 | vim-9.1.1330 | findswapname | cpp/unbounded-write | 4967 | FP | FP | STRCPY 的目标缓冲区 fname2 的大小为 n+2，而源字符串 fname 的长度为 n，复制操作不会导致缓冲区溢出。 |
| 1129 | vim-9.1.1330 | str2specialbuf | cpp/unbounded-write | 2017 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度小于传入的`len`参数，... |
| 1136 | vim-9.1.1330 | add_to_showcmd | cpp/unbounded-write | 1764 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已通过计算old_len和extra_len检查了缓冲区溢出风险，并在溢出时使用mch_memmove移动了缓冲区内容，确保拼接操作不会越界。 |
| 1141 | vim-9.1.1330 | block_insert | cpp/unbounded-write | 743 | FP | FP | STRCPY宏的目标缓冲区newp是通过alloc函数分配的，其大小计算为ml_get_len(lnum) + spaces + slen + ...，而源字符串oldp来自ml_get(lnum)，其长度ml_get_len(lnu... |
| 1142 | vim-9.1.1330 | option_value2string | cpp/unbounded-write | 8372 | FP | FP | 切片代码显示，告警点STRCPY的目标缓冲区是NameBuff，但切片中未提供其大小定义，无法确认是否存在缓冲区溢出。然而，在P_STRING分支中，对同一缓冲区的操作（如vim_strncpy）使用了明确的长度限制MAXPATHL，... |
| 1143 | vim-9.1.1330 | option_value2string | cpp/unbounded-write | 8374 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，函数wc_use_keyname和transchar的输出是受控的，且目标缓冲区NameBuff的大小在调用点未明确，但告警点位于处理数值选项（P_NUM）的分支，该分支逻辑确保... |
| 1168 | vim-9.1.1330 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数getroom已根据源字符串长度s（通过STRLEN(s) + 1计算）分配了足够的内存，STRCPY操作不会导致缓冲区溢出。 |
| 1176 | vim-9.1.1330 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | STRCPY宏的目标缓冲区`sft->sft_word`的大小已通过`alloc(offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1)`精确分配，长度足以容纳源字符串`goodwo... |
| 1178 | vim-9.1.1330 | concat_str | cpp/unbounded-write | 792 | FP | FP | 函数 `concat_str` 通过 `alloc` 为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加1，随后才调用 `STRCPY`（即 `strcpy`）。这确保了目标缓冲区大小足以容纳源字符串，不会发生缓冲区溢出。 |
| 1179 | vim-9.1.1330 | concat_str | cpp/unbounded-write | 794 | FP | FP | 函数内已通过alloc为目标缓冲区分配了足够空间，其大小为两个源字符串长度之和加1，因此STRCPY操作不会导致缓冲区溢出。 |
| 1177 | vim-9.1.1330 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY 宏的目标缓冲区 fword 大小为 MAXWLEN，而源字符串 su->su_fbadword 是拼写建议算法内部生成的字符串，其长度在算法上下文中已被确保不会超过 MAXWLEN，因此不存在缓冲区溢出风险。 |
| 1189 | vim-9.1.1330 | exec_instructions | cpp/unbounded-write | 3896 | FP | FP | 切片代码中未发现任何对strcpy的调用，告警消息中提到的多个strcpy调用在提供的代码片段中不存在。该告警可能是工具对代码的误解析或指向了不相关的代码位置。 |
| 1198 | vim-9.1.0790 | <global> | cpp/redundant-null-check-simple | 3584 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 指针在解引用前已通过 `if (*inc_opt != NUL)` 进行了有效性检查，该检查确保了指针非空，因此解引用是安全的，空指针检查确... |
| 1197 | vim-9.1.0790 | <global> | cpp/redundant-null-check-simple | 3502 | FP | FP | 告警指出对 inc_opt 的空指针检查是冗余的，因为该变量在检查前已被解引用。切片代码显示 inc_opt 在检查前已通过条件赋值（`inc_opt = (*curbuf->b_p_inc == NUL) ? p_inc : cur... |
| 1200 | vim-9.1.0790 | common_function | cpp/inconsistent-null-check | 4876 | FP | FP | 代码在调用 vim_strsave 后，将返回值赋给变量 name，并在后续多处对 name 进行了检查和使用（如 vim_free(name)），这表明代码逻辑已隐含处理了可能的 NULL 返回值。告警是基于统计模式（84%的调用检... |
| 1199 | vim-9.1.0790 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | FP | FP | 切片代码显示，在访问 `linep[pos.col]` 和 `linep[pos.col + 1]` 之前，存在对 `pos.col` 的边界检查和调整逻辑（例如在循环中检查 `linep[pos.col] == NUL` 并调整 `... |
| 1202 | vim-9.1.0790 | get_isolated_shell_name | cpp/inconsistent-null-check | 2695 | FP | FP | 函数 `gettail` 已处理 NULL 输入并返回空字符串，`vim_strsave` 的参数非 NULL，且其返回值 `p` 被直接返回给调用者，由调用者负责检查。切片中未显示调用者对 `p` 进行解引用等危险操作，因此告警指出... |
| 1204 | vim-9.1.0790 | did_set_cryptmethod | cpp/inconsistent-null-check | 1821 | FP | FP | 代码中调用`vim_strsave`的参数是字符串字面量"zip"，内存分配必然成功，无需检查NULL。该告警是工具基于统计模式（84%的调用检查了NULL）产生的误报，在当前上下文中是安全的。 |
| 1205 | vim-9.1.0790 | did_set_background | cpp/inconsistent-null-check | 1082 | FP | FP | 切片代码显示，在调用 vim_strsave 后，其返回值 p_bg 立即被传递给 check_string_option 函数。该函数明确检查指针是否为 NULL，并在为 NULL 时将其赋值为 empty_option，这构成了有... |
| 1206 | vim-9.1.0790 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 调用 `find_win_by_nr_or_id` 后，其返回值 `wp->w_popup_prop_win` 立即被 `win_valid_any_tab` 函数检查，若无效则回退为 `curwin`。切片代码中已包含此防护逻辑，因... |
| 1208 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 切片代码显示，在调用`regnode(BRANCH)`后，其返回值`br`被立即用于条件判断`if (ret == NULL)`，这表明代码逻辑依赖于`br`的有效性。此外，后续的`regtail`调用和`reg_toolong`检查... |
| 1207 | vim-9.1.0790 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 代码中`regnext`函数的返回值`next`在后续代码中被使用，但切片显示其使用前有对`scan`是否为NULL的检查（`if (got_int ｜｜ scan == NULL)`），且`regnext`函数内部已处理NULL返回... |
| 1209 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 切片代码显示，对 regnode 的调用结果（br）被直接用于后续的 regtail 操作，但该操作仅在 `ret != JUST_CALC_SIZE` 条件下执行，而 `JUST_CALC_SIZE` 是一个特殊的哨兵值，用于指示当... |
| 1210 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在切片代码中，`regnext`的返回值在`for`循环中被直接赋值给`br`用于迭代，其目的并非检查指针有效性，而是遍历链表结构。`regnext`函数内部已对`p == JUST_CALC_SIZE`或`reg_toolong`的... |
| 1211 | vim-9.1.0790 | win_redr_custom | cpp/inconsistent-null-check | 1115 | FP | FP | 代码在调用vim_strsave后，立即将返回值传递给vim_free进行释放，虽然未显式检查NULL，但vim_free内部已处理NULL指针，且后续使用前有transstr等安全处理，未导致解引用空指针的风险。 |
| 1212 | vim-9.1.0790 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 函数 `getroom` 在内存分配失败时会返回 `NULL`，但调用点 `get_wordnode` 在 `#ifdef SPELL_PRINTTREE` 块中已对返回值 `n` 进行了 `NULL` 检查，且后续逻辑（如 `CLE... |
| 1213 | vim-9.1.0790 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续逻辑中被立即赋值给 `tofree`，并由 `vim_free(tofree)` 释放，且 `name` 随后被重新赋值为 `tag`。这表明 `name` 的原... |
| 1214 | vim-9.1.0790 | define_function | cpp/inconsistent-null-check | 5356 | FP | FP | 告警指出的 vim_strchr 调用未检查空指针，但切片代码显示该调用结果仅用于条件判断（!= NULL），并非必须检查空指针。该模式在代码中多次出现，属于正常用法，不构成安全问题。 |
| 1217 | vim-9.1.0790 | barline_parse | cpp/inconsistent-null-check | 1122 | FP | FP | 切片代码显示，在调用 vim_strsave 之前，已通过条件 `s != buf && allocated && !converted` 确保 s 不是已分配的 buf 且未经过转换，但 allocated 仅在特定路径下为 TRU... |
| 1218 | vim-9.1.0790 | ex_history | cpp/unsafe-strcat | 780 | FP | FP | 切片代码显示，在调用STRCAT前，已通过条件`vim_strsize(hist[i].hisstr) > (int)Columns - 10`检查了源字符串长度，若过长则调用trunc_string进行截断，确保不会超出目标缓冲区I... |
| 1219 | vim-9.1.0790 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | STRCAT宏被用于拼接已知的目录路径和文件扩展名，这些字符串长度受控且来自函数参数，目标缓冲区NameBuff的大小在代码其他部分（如后续的mch_fopen调用）被假定为足够大（如MAXPATHL），且未观察到缓冲区溢出的直接风险。 |
| 1220 | vim-9.1.0790 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 切片代码显示，`name` 指针指向的字符串长度是严格受限的（如 "F1"、"X" 或单字符数组 `namebuf`），且 `buf` 在首次使用前被初始化为空字符串。虽然未明确给出 `buf` 的大小，但根据上下文（函数名为 `ne... |
| 1222 | vim-9.1.0790 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy(newword, ae->ae_add, MAXWLEN - 1)确保目标缓冲区newword以NUL结尾且长度受限，且后续拼接的字符串p源自word并受wo... |
| 1233 | vim-9.1.0790 | globpath | cpp/unbounded-write | 3795 | FP | FP | 切片代码显示，在调用STRCAT(buf, file)之前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区buf的剩余空间，确保拼接后不会溢出。因此该告警为误报。 |
| 1244 | vim-9.1.0790 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区buf分配了精确计算的长度len，该长度已包含源字符串cmd的长度及必要的额外字符和终止符，因此不会发生缓冲区溢出。 |
| 1245 | vim-9.1.0790 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 代码在调用STRCAT前，已通过alloc(len)分配了缓冲区，且len的计算已考虑了所有待拼接字符串（cmd, itmp, otmp等）的长度和必要的分隔符，并预留了NUL终止符，因此缓冲区大小足够，不会发生溢出。 |
| 1253 | vim-9.1.0790 | discard_exception | cpp/unbounded-write | 642 | FP | FP | STRCPY的目标缓冲区IObuff是全局缓冲区，其大小在别处定义为IOSIZE；源字符串saved_IObuff是IObuff的副本，由vim_strsave(IObuff)创建，其长度与IObuff相同，因此复制不会导致溢出。 |
| 1262 | vim-9.1.0790 | vim_rename | cpp/unbounded-write | 3839 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。 |
| 1266 | vim-9.1.0790 | concat_fnames | cpp/unbounded-write | 3123 | FP | FP | 代码通过alloc为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcpy操作不会发生缓冲区溢出。 |
| 1273 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 805 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）前，已通过STRLEN检查确保源字符串长度加1小于目标缓冲区大小MAXPATHL，因此不会发生缓冲区溢出。 |
| 1274 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 819 | FP | FP | 切片代码中，在调用STRCAT（即strcat）前，均存在明确的长度检查（STRLEN(file_path) + STRLEN(...) < MAXPATHL），确保目标缓冲区不会溢出。因此，该告警为误报。 |
| 1275 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 940 | FP | FP | 切片代码中，所有对STRCPY（即strcpy）的调用前，均存在明确的长度检查（如`STRLEN(...) + ... < MAXPATHL`），确保目标缓冲区`file_path`（大小为MAXPATHL）不会溢出。因此，这些调用是... |
| 1276 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 942 | FP | FP | 切片代码中，在调用STRCAT（即strcat）前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区`file_path`（大小为MAXPATH... |
| 1277 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 1110 | FP | FP | 切片代码中所有使用STRCPY（即strcpy）的地方，在调用前都通过STRLEN计算了源字符串长度，并与目标缓冲区大小MAXPATHL进行了明确的比较，确保不会发生缓冲区溢出。例如，在告警行附近有`if (STRLEN(search... |
| 1278 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 1112 | FP | FP | 切片代码中所有使用STRCAT的地方，都在调用前通过STRLEN计算了目标缓冲区剩余空间，并与MAXPATHL（最大路径长度）进行了比较，确保不会发生缓冲区溢出。例如，在告警行附近有明确的长度检查：`if (STRLEN(search... |
| 1300 | vim-9.1.0790 | highlight_set_startstop_termcode | cpp/unbounded-write | 1477 | FP | FP | 切片代码显示，在调用STRCAT前有明确的长度检查`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`，确保拼接后的总长度不会超过目标缓冲区buf（大小为100）的容量，因此不存在缓冲区溢出风险。 |
| 1304 | vim-9.1.0790 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了该大小的内存，确保了目标缓冲区大小与格式化字符串长度完全匹配，不存在溢出风险。 |
| 1308 | vim-9.1.0790 | ins_compl_infercase_gettext | cpp/unbounded-write | 653 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区`gap.ga_data`已通过`ga_grow(&gap, IOSIZE)`确保有足够空间，且源字符串`IObuff`的大小受`IOSIZE`常量限制，因此不会发生缓冲区溢出。 |
| 1310 | vim-9.1.0790 | findswapname | cpp/unbounded-write | 4967 | FP | FP | STRCPY 的目标缓冲区 fname2 的大小为 n+2，而源字符串 fname 的长度为 n，复制后目标缓冲区有足够的空间容纳源字符串和额外的字符修改，不会发生缓冲区溢出。 |
| 1315 | vim-9.1.0790 | str2specialbuf | cpp/unbounded-write | 1919 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间是否足以容纳源字符串`s`，因此不会发生缓冲区溢出。 |
| 1318 | vim-9.1.0790 | expand_env_esc | cpp/unbounded-write | 1632 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen`检查了目标缓冲区dst的剩余空间，确保不会发生缓冲区溢出。 |
| 1323 | vim-9.1.0790 | add_to_showcmd | cpp/unbounded-write | 1760 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已计算了目标缓冲区showcmd_buf的当前长度old_len和待追加字符串p的长度extra_len，并检查了溢出（overflow）。若溢出大于0，会通过mch_memmov... |
| 1328 | vim-9.1.0790 | block_insert | cpp/unbounded-write | 607 | FP | FP | STRCPY 的目标缓冲区 newp 是通过 alloc 分配的，其大小为 ml_get_len(lnum) + spaces + slen + (可能的额外空间)，而源字符串 oldp 来自 ml_get 返回的行内容，其长度 ml... |
| 1329 | vim-9.1.0790 | option_value2string | cpp/unbounded-write | 8213 | FP | FP | 切片代码显示，告警点STRCPY的目标缓冲区NameBuff是一个全局数组，其大小未在切片中明确给出，但调用get_special_key_name返回的string缓冲区大小固定为MAX_KEY_NAME_LEN+1，且调用前通过w... |
| 1330 | vim-9.1.0790 | option_value2string | cpp/unbounded-write | 8215 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，存在对目标缓冲区NameBuff大小的明确控制。例如，在P_STRING分支中，调用了home_replace、str2specialbuf和vim_strncpy，这些函数都明... |
| 1344 | vim-9.1.0790 | op_yank | cpp/unbounded-write | 1279 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已通过alloc为目标缓冲区pnew分配了足够的空间，其大小为两个源字符串长度之和加1，因此不会发生缓冲区溢出。 |
| 1356 | vim-9.1.0790 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数 getroom 已根据源字符串长度 s 分配了足够的内存（STRLEN(s) + 1），因此 STRCPY（即 strcpy）操作不会导致缓冲区溢出。 |
| 1360 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 切片代码显示告警点位于处理COMPOUNDRULE规则的代码块中，其中STRCAT的目标缓冲区p是通过getroom(spin, l, FALSE)动态分配的，其大小l已计算为所需字符串的总长度加分隔符，因此不会发生缓冲区溢出。 |
| 1364 | vim-9.1.0790 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | STRCPY宏的目标缓冲区sft->sft_word的大小为STRLEN(goodword) + 1，通过alloc函数精确分配，源字符串goodword的长度已通过STRLEN计算，因此复制操作不会导致缓冲区溢出。 |
| 1366 | vim-9.1.0790 | concat_str | cpp/unbounded-write | 795 | FP | FP | 函数内通过alloc为目标缓冲区分配了精确的、足以容纳源字符串的长度（包括空字符），strcpy操作不会导致缓冲区溢出。 |
| 1367 | vim-9.1.0790 | concat_str | cpp/unbounded-write | 797 | FP | FP | 函数内已通过alloc为目标缓冲区分配了精确的、足以容纳源字符串str1和str2拼接后内容的空间，STRCPY（即strcpy）操作不会导致缓冲区溢出。 |
| 1365 | vim-9.1.0790 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY 宏的目标缓冲区 fword 大小为 MAXWLEN，源字符串 su->su_fbadword 是拼写建议模块内部生成的字符串，其长度在之前的逻辑中已确保不超过 MAXWLEN，因此不会发生缓冲区溢出。 |
| 1387 | musl-1.2.3 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 切片代码显示，分配的内存大小 `sizeof *f + UNGET + BUFSIZ` 是用于 `FILE` 结构体、反推缓冲区（UNGET）和主缓冲区（BUFSIZ）的组合，这是一个典型的、正确的内存布局，并非可疑的分配大小。 |
| 1388 | musl-1.2.3 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat前，代码已通过if (scopeid)确保p非空，且p指向的缓冲区（tmp或num）大小已知且有限（IF_NAMESIZE+1或3*sizeof(int)+1），拼接后的总长度不会超过buf的固定大小256，因此不存... |
| 1390 | musl-1.2.3 | <global> | cpp/unbounded-write | 67 | FP | FP | 在调用strcpy前，代码已通过strlen(canon)+1计算了所需缓冲区大小，并检查了need > buflen，确保目标缓冲区buf有足够空间容纳canon字符串，因此不存在缓冲区溢出风险。 |
| 1391 | musl-1.2.3 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 在调用strcpy(node, buf)之前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1393 | musl-1.2.2 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 分配的内存大小（sizeof *f + UNGET + BUFSIZ）是用于结构体FILE、反推缓冲区UNGET和标准缓冲区BUFSIZ的组合，其对齐和布局由后续代码（如f->buf的赋值）显式管理，并非错误的内存分配。该告警是对特定... |
| 1396 | musl-1.2.2 | <global> | cpp/unbounded-write | 67 | FP | FP | 切片代码显示，在调用strcpy前，已通过strlen(canon)计算了所需缓冲区大小，并与传入的buflen进行了检查（need > buflen），若空间不足函数会提前返回ERANGE。因此，当strcpy执行时，目标缓冲区h-... |
| 1395 | musl-1.2.2 | load_library | cpp/unbounded-write | 1161 | FP | FP | 切片代码显示，在调用strcpy之前，pathname的来源（buf或name）均受到长度检查或路径搜索逻辑的限制，且buf的大小（2*NAME_MAX+2）足以容纳最大路径长度，因此不存在缓冲区溢出风险。 |
| 1394 | musl-1.2.2 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat前，代码已通过inet_ntop将IP地址安全地格式化到buf中，且buf的大小为256字节，而拼接的scopeid字符串长度有限（来自itoa或if_indextoname），不会导致缓冲区溢出。此外，后续有str... |
| 1397 | musl-1.2.2 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 在调用strcpy前，代码已通过'if (strlen(buf) >= nodelen) return EAI_OVERFLOW;'检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1399 | musl-1.2.1 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 分配的内存大小（sizeof *f + UNGET + BUFSIZ）是用于FILE结构体、反推缓冲区（UNGET）和主缓冲区（BUFSIZ）的组合，其对齐和布局由后续代码（如f->buf的偏移计算）显式管理，并非简单的结构体数组分配... |
| 1400 | musl-1.2.1 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat前，代码已通过if (scopeid)确保p非空，且p指向的缓冲区（tmp或num）大小固定且已知，拼接后的总长度已通过前一步的inet_ntop和后续的strlen(buf)检查确保不会溢出目标缓冲区buf（大小为... |
| 1402 | musl-1.2.1 | <global> | cpp/unbounded-write | 67 | FP | FP | 代码在调用strcpy前已通过strlen(canon)计算了所需缓冲区大小，并检查了need > buflen，确保目标缓冲区buf有足够空间，因此不会发生缓冲区溢出。 |
| 1403 | musl-1.2.1 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 在调用strcpy(node, buf)之前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`进行了明确的长度检查，确保目标缓冲区node有足够空间，因此不存在缓冲区溢出风险。 |
| 1407 | musl-1.1.24 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 切片代码显示，分配的内存大小 `sizeof *f + UNGET + BUFSIZ` 是用于 `FILE` 结构体及其后附加的缓冲区的总大小，并非为 `FILE` 类型的数组分配内存，因此分配大小无需是 `sizeof(FILE)`... |
| 1408 | musl-1.1.24 | getnameinfo | cpp/unsafe-strcat | 178 | FP | FP | 在调用strcat前，代码已通过if (scopeid)确保p非空，且p指向的缓冲区（tmp或num）大小已知且有限（IF_NAMESIZE+1或3*sizeof(int)+1）。此外，buf的大小为256字节，并在strcat前已通... |
| 1411 | musl-1.1.24 | getnameinfo | cpp/unbounded-write | 182 | FP | FP | 在调用strcpy前，代码已通过'if (strlen(buf) >= nodelen) return EAI_OVERFLOW;'检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1410 | musl-1.1.24 | <global> | cpp/unbounded-write | 67 | FP | FP | 切片代码显示，在调用strcpy前，已通过need计算确保目标缓冲区buf有足够空间容纳源字符串canon（need += strlen(canon)+1; 且 need > buflen 时返回ERANGE）。canon是内部生成的... |
| 1413 | musl-1.2.4 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 分配的内存大小（sizeof *f + UNGET + BUFSIZ）是用于FILE结构体、反推缓冲区（UNGET）和标准缓冲区（BUFSIZ）的组合，其总大小不要求是FILE结构体大小的整数倍，这是实现上的合理设计，并非错误的内存分配。 |
| 1414 | musl-1.2.4 | getnameinfo | cpp/unsafe-strcat | 180 | FP | FP | 在调用strcat前，代码已通过inet_ntop将IP地址字符串安全地写入固定大小的buf数组，且后续有长度检查确保不会溢出。strcat拼接的字符串（接口名或scopeid）长度受IF_NAMESIZE和整数位数限制，总长度远小于... |
| 1417 | musl-1.2.4 | getnameinfo | cpp/unbounded-write | 184 | FP | FP | 在调用strcpy前，代码已通过'if (strlen(buf) >= nodelen) return EAI_OVERFLOW;'检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1416 | musl-1.2.4 | <global> | cpp/unbounded-write | 69 | FP | FP | 切片代码显示，`canon` 数组在 `__lookup_name` 函数中已通过 `strnlen` 和 `memcpy` 确保了其长度不超过255字节，且目标缓冲区 `h->h_name` 指向的 `buf` 空间大小已通过 `n... |
| 1419 | tmux-3.4 | <global> | cpp/overflow-buffer | 67 | FP | FP | 切片代码显示，在访问 `place[1]` 之前，已经通过 `*(place = nargv[BSDoptind]) != '-'` 和 `place[1] && *++place == '-'` 等条件确保了 `place` 指向的... |
| 1420 | tmux-3.4 | <global> | cpp/overflow-buffer | 68 | FP | FP | 切片代码显示，在访问 `place[1]` 之前，已通过 `*(place = nargv[BSDoptind]) != '-'` 和 `place[1] && *++place == '-'` 等条件确保 `place` 指向的字符... |
| 1421 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 700 | FP | FP | 切片代码显示，在调用 cliConcatArguments 前，已通过 assert 语句确保 args 指针非空且类型为 REDIS_REPLY_ARRAY，这防止了空指针解引用。告警点位于 assert 之后，因此是安全的。 |
| 1424 | redis-7.0.11 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1626 | FP | FP | 告警点调用的`sdsfree`函数内部已包含对NULL指针的检查（`if (s == NULL) return;`），因此即使`state->lines[linenum]`为NULL也不会导致空指针解引用，代码是安全的。 |
| 1422 | redis-7.0.11 | breakstat | Dereference of null pointer | 986 | FP | FP | 切片代码显示，在访问 `bl->nactvar` 之前，`bl` 变量已在 `while` 循环中被更新，且循环条件 `while (bl && !bl->isbreakable)` 确保了只有当 `bl` 非空时才会进入循环体。因此... |
| 1425 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在访问 `help->org.group` 之前，`help` 指针已在函数开头通过 `helpEntry *help = next++;` 被赋值，且 `next` 参数来自调用方，切片内无证据表明其为 NULL。告警... |
| 1428 | redis-7.0.11 | cliConcatArguments | Dereference of null pointer | 542 | FP | FP | 告警点位于循环条件 `arguments->elements` 的访问，但切片代码显示，在调用 `cliConcatArguments` 前，`arguments` 指针已在 `cliAddArgument` 函数中通过 `argMa... |
| 1430 | redis-7.0.11 | sdscat_orempty | Dereference of null pointer | 532 | FP | FP | 告警点 `value[0]` 的访问发生在对 `value` 指针进行空值检查之后，切片代码显示 `value` 作为函数参数传入，其有效性应由调用方保证。在函数内部，直接访问 `value[0]` 是安全的，因为如果 `value`... |
| 1427 | redis-7.0.11 | dictGetRandomKey | Dereference of null pointer | 682 | FP | FP | 切片代码显示，在进入循环前，`he` 指针已通过 `do...while(he == NULL)` 循环确保不为空，且后续的 `while(he)` 循环也确保了 `listlen` 至少为1。因此，`while(listele--)... |
| 1429 | redis-7.0.11 | rewriteConfigRewriteLine | Dereference of null pointer | 1236 | FP | FP | 在调用`sdsfree(state->lines[linenum])`之前，代码已通过`if (l)`检查确保`l`非空，并通过`listFirst(l)`和`ln->value`安全访问获取了`linenum`。`linenum`作... |
| 1433 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 688 | FP | FP | 切片代码显示，在访问 `reply->str` 之前，已通过 `assert(reply->type == REDIS_REPLY_STRING)` 确保 `reply` 是字符串类型，且 `specs` 是有效的数组/映射，其元素指... |
| 1432 | redis-7.0.11 | cliInitGroupHelpEntries | Dereference of null pointer | 771 | FP | FP | 切片代码显示 `helpEntries` 数组的索引 `pos` 由静态变量 `helpEntriesLen` 初始化并递增，但未提供 `helpEntries` 数组本身的声明或大小信息，无法确认 `pos` 是否会越界。然而，结合... |
| 1435 | redis-7.0.11 | _quicklistListpackMerge | Dereference of null pointer | 813 | FP | FP | 告警点位于条件判断 `if (!a->entry)` 处，但根据上下文逻辑，该判断是在 `lpMerge` 函数成功返回（非空）后执行的，此时 `a->entry` 或 `b->entry` 至少有一个非空，因此 `a->entry`... |
| 1437 | redis-7.0.11 | cliOldInitHelp | Dereference of null pointer | 455 | FP | FP | 切片代码显示 `helpEntries` 是一个全局或外部数组，其大小和初始化在切片外，但告警点 `helpEntries[pos++] = tmp;` 的索引 `pos` 在循环中递增，且受限于 `groupslen` 和 `com... |
| 1438 | redis-7.0.11 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 切片代码显示，在访问 `quicklist->head` 和 `quicklist->tail` 之前，函数已通过 `if (quicklist->len == 0) return;` 确保链表非空，且 `assert` 语句进一步确... |
| 1439 | redis-7.0.11 | getKeySizes | Dereference of null pointer | 8193 | FP | FP | 告警行代码 `if(!types[i] ｜｜ (!types[i]->sizecmd && !memkeys))` 在解引用 `types[i]` 前已通过 `!types[i]` 检查其是否为 NULL，因此当 `types[i]`... |
| 1441 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 684 | FP | FP | 切片代码显示，在访问 `help->org.summary` 之前，`help` 指针已在函数开头通过 `help = next++` 被正确赋值，且 `next` 作为参数传入，不存在空指针解引用。告警为误报。 |
| 1442 | redis-7.0.11 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 在警告行 `if (forward == reverse ｜｜ forward->next == reverse)` 之前，代码已通过 `quicklistDecompressNode(forward);` 宏调用对 `forward... |
| 1444 | redis-7.0.11 | moduleFreeContext | Dereference of null pointer | 748 | FP | FP | 在调用 zfree 之前，代码已通过条件判断 `if (ctx->postponed_arrays)` 确保指针非空，因此不会发生空指针解引用。 |
| 1443 | redis-7.0.11 | _quicklistListpackMerge | Dereference of null pointer | 820 | FP | FP | 告警点位于条件分支 `if ((lpMerge(&a->entry, &b->entry)))` 内部，该分支仅在 `lpMerge` 成功（返回非空指针）时执行。在分支内，`keep` 被赋值为 `a` 或 `b`，而 `a` 和 ... |
| 1440 | redis-7.0.11 | json_next_token | Dereference of null pointer | 1022 | FP | FP | 切片代码显示，在访问 `ch2token[ch]` 之前，`ch` 的值来自 `*(json->ptr)`，而 `json->ptr` 在循环中会递增，但关键点在于 `ch2token` 指针来自 `json->cfg->ch2tok... |
| 1445 | redis-7.0.11 | extent_try_coalesce_impl | Dereference of null pointer | 1666 | FP | FP | 切片代码显示，在标记行`*coalesced = false;`之前，`coalesced`指针仅在条件`if (extents->delay_coalesce)`为真时被赋值，且该条件块内已确保`coalesced`不为空（因为存在... |
| 1448 | redis-7.0.11 | extent_try_coalesce_impl | Dereference of null pointer | 1636 | FP | FP | 在调用 extent_unlock 函数前，代码已通过 if (prev != NULL) 和 if (next != NULL) 检查指针非空，且 extent_unlock 函数内部有 assert(extent != NULL)... |
| 1447 | redis-7.0.11 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该分支仅在 `h->size` 为 0 时执行。切片代码显示，在到达该分支前，`h` 指针已通过 `raxAddChild` 或 `raxCompressNode` 等... |
| 1449 | redis-7.0.11 | clusterManagerAddSlots | Dereference of null pointer | 3898 | FP | FP | 告警点 `*err = NULL;` 是对指针 `err` 的解引用，但切片代码显示 `err` 是函数 `clusterManagerAddSlots` 的入参，调用方传入的指针不可能为 NULL，否则无法在函数内进行赋值。该行是安... |
| 1450 | redis-7.0.11 | min_expand | Dereference of null pointer | 322 | FP | FP | 在告警行 `singlematch(uchar(*s), p, ep)` 中，对 `s` 的解引用受前置条件 `s<ms->src_end` 保护，确保了 `s` 指向有效内存，不会发生空指针解引用。 |
| 1451 | redis-7.0.11 | strbuf_init | Dereference of null pointer | 53 | FP | FP | 代码仅对结构体指针`s`的成员`buf`进行赋值操作（赋值为NULL），并未对`s`本身或其成员进行解引用操作，不存在空指针解引用。告警是对代码逻辑的误判。 |
| 1453 | redis-7.0.11 | checkMultiPartAof | Dereference of null pointer | 474 | FP | FP | 切片代码显示，在访问 `am->incr_aof_list` 之前，已经通过 `if (am->incr_aof_list)` 进行了空指针检查，因此后续的 `listLength(am->incr_aof_list)` 调用是安全的... |
| 1455 | redis-7.4.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2891 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，存在 `if (dstkey)` 条件判断。`dstkey` 是函数参数，若其为 NULL，则整个代码块不会执行，从而避免了空指针解引用。告警点位于受保护的代码... |
| 1454 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2541 | FP | FP | 告警点位于宏 dictPauseAutoResize 的调用处，该宏仅对字典的 pauseAutoResize 字段进行自增操作，不会对指针进行解引用。切片代码中 dstzset->dict 在函数入口处已被使用（如 dictAdd）... |
| 1456 | redis-7.4.2 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 切片代码显示`s->buf`被显式赋值为NULL，这是结构体字段的初始化操作，并非对空指针的解引用。该告警是对初始化代码的逻辑误判。 |
| 1457 | redis-7.4.2 | breakstat | Dereference of null pointer | 986 | FP | FP | 在while循环中，变量`bl`被更新，直到找到`isbreakable`为真的块或变为NULL。如果循环后`bl`为NULL，则`if (upval)`条件为假，不会执行到告警行。如果`bl`不为NULL，则其指向一个有效的`Blo... |
| 1459 | redis-7.4.2 | dictGenericDelete | Dereference of null pointer | 628 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，已通过 `dictSize(d) == 0` 检查字典非空，并在循环中通过 `while(he)` 确保指针非空后才解引用。告警点处的指针访问是安全的，因... |
| 1460 | redis-7.4.2 | zdiffAlgorithm1 | Dereference of null pointer | 2497 | FP | FP | 告警点位于 `zslInsert` 调用处，该函数内部已通过 `serverAssert(!isnan(score));` 确保传入的 `score` 有效，且 `zuiNext` 函数会为 `zval.score` 赋值，切片中未发... |
| 1462 | redis-7.4.2 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `*coalesced = false;` 是对布尔指针的赋值操作，切片代码显示该指针 `coalesced` 是函数的有效输入参数，在函数内部多个条件分支中已被安全地赋值，不存在空指针解引用。 |
| 1461 | redis-7.4.2 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1634 | FP | FP | 告警指向的 `sdsfree(state->lines[linenum])` 调用，其参数 `state->lines[linenum]` 在切片中未显示定义，但 `sdsfree` 函数内部已包含对 NULL 指针的检查（`if (... |
| 1463 | redis-7.4.2 | clusterSendPing | Dereference of null pointer | 3650 | FP | FP | 告警行访问 `link->node->ping_sent` 前，切片代码已包含对 `link->node` 的检查（`if (link->node && nodeSupportsExtensions(link->node))`），表明... |
| 1465 | redis-7.4.2 | dictGetVal | Dereference of null pointer | 887 | FP | FP | 函数`dictGetVal`的参数`de`是一个指向`dictEntry`的指针，切片代码中虽未显示其调用上下文，但函数本身是安全的。该告警是静态分析工具对解引用操作的通用警告，在C语言中，解引用指针是常见操作，其安全性由调用者保证。... |
| 1466 | redis-7.4.2 | dictFind | Dereference of null pointer | 762 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，已通过 `dictSize(d) == 0` 检查字典非空，且在循环中 `he` 变量被赋值后立即进入 `while(he)` 循环，该循环仅在 `he`... |
| 1467 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12395 | FP | FP | 告警指向的代码行是对指针 `module` 的成员访问（`module->usedby`），但切片代码显示，在访问前已通过 `if (module == NULL)` 检查了指针为空的情况，并提前返回。因此，当执行到该行时，`modu... |
| 1468 | redis-7.4.2 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 告警点位于对指针`coalesced`的赋值语句，该指针作为函数参数传入，在切片代码中，所有对`*coalesced`的赋值都发生在`coalesced`指针本身被解引用之前，且没有空指针检查。然而，函数调用上下文显示`coalesc... |
| 1470 | redis-7.4.2 | RM_ListInsert | Dereference of null pointer | 4665 | FP | FP | 告警点位于函数`listTypeTryConversionAppend`的调用，其第一个参数`key->value`在`moduleListIteratorSeek`函数中被明确检查是否为NULL。如果`key->value`为NUL... |
| 1471 | redis-7.4.2 | cliInitGroupHelpEntries | Dereference of null pointer | 728 | FP | FP | 告警点 `helpEntries[pos++] = tmp;` 处，`helpEntries` 数组的访问下标 `pos` 由静态变量 `helpEntriesLen` 初始化，并在循环中递增。切片中未显示 `helpEntries`... |
| 1472 | redis-7.4.2 | cliFillInCommandHelpEntry | Dereference of null pointer | 588 | FP | FP | 切片代码显示，对 `help` 指针的访问（`help->argc`）发生在函数参数中，调用方必须传入有效的指针，否则函数无法被正确调用。`zmalloc` 函数内部有内存分配失败的检查和处理（`zmalloc_oom_handler... |
| 1473 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12388 | FP | FP | 告警指向的代码行 `*errmsg = "no such module with that name";` 仅在 `module == NULL` 的条件下执行，此时对空指针 `errmsg` 的解引用是安全的，因为 `errmsg`... |
| 1476 | redis-7.4.2 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查oldlenp是否为NULL，切片代码显示告警点位于VERIFY_READ宏调用处，该宏内部有防护逻辑，因此不会发生空指针解引用。 |
| 1478 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12391 | FP | FP | 告警指向的代码行是字符串字面量赋值，并非指针解引用。切片代码显示，在`module`为NULL的分支中，`errmsg`被赋值为一个字符串常量，这是一个安全的赋值操作，不会导致空指针解引用。 |
| 1477 | redis-7.4.2 | xgroupCommand | Dereference of null pointer | 2707 | FP | FP | 在SETID子命令中，对`s->last_id`的访问发生在`s`被确认非空之后。代码路径显示，当`opt`为"SETID"且`s`为NULL时，程序会提前返回或进入其他分支，不会执行到有问题的行。 |
| 1475 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2559 | FP | FP | 告警点 `dictShrinkIfNeeded(dstzset->dict)` 的参数 `dstzset->dict` 在函数逻辑中已被确保非空。在 `j == 0` 的分支中，`dstzset->dict` 通过 `dictAdd`... |
| 1479 | redis-7.4.2 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 切片代码显示，在调用`assert`之前，函数已通过`if (quicklist->len == 0) return;`确保链表非空，因此`quicklist->head`和`quicklist->tail`不应为空指针。该断言是用于... |
| 1480 | redis-7.4.2 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警指向的宏 VERIFY_READ 在 oldp 或 oldlenp 为 NULL 时会设置错误码并跳转返回，不会发生空指针解引用。代码逻辑确保了指针在解引用前已被验证。 |
| 1481 | redis-7.4.2 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 切片代码显示，在访问 `ch2token[ch]` 之前，`ch2token` 指针已从 `json->cfg->ch2token` 获取，而 `json->cfg` 在函数入口处被使用且未被修改，没有证据表明 `ch2token` ... |
| 1482 | redis-7.4.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2874 | FP | FP | 切片代码显示，在调用 dictExpand(dstzset->dict, dictSize(accumulator)) 之前，dstzset 已通过 dstobj = createZsetObject() 初始化，其 dict 成员在... |
| 1483 | redis-7.4.2 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 切片代码显示，在访问 `forward->next` 之前，`forward` 变量已通过 `quicklistDecompressNode(forward)` 宏调用，该宏包含对 `(_node)` 的非空检查，且 `forward... |
| 1485 | redis-7.4.2 | moduleFreeContext | Dereference of null pointer | 815 | FP | FP | 告警指向的代码行是 `serverLog` 调用，该行仅使用 `ctx->module->name`，而 `ctx` 已在函数入口通过 `if (ctx->postponed_arrays)` 进行了非空检查，且 `ctx->modu... |
| 1484 | redis-7.4.2 | _quicklistListpackMerge | Dereference of null pointer | 882 | FP | FP | 告警点位于条件分支 `if ((lpMerge(&a->entry, &b->entry)))` 内部，该条件确保 `lpMerge` 成功返回非空指针。在成功分支内，`keep` 指针被赋值为 `a` 或 `b`，且通过 `if (... |
| 1486 | redis-7.4.2 | rewriteConfigRewriteLine | Dereference of null pointer | 1243 | FP | FP | 在调用`sdsfree(state->lines[linenum])`之前，代码已通过`if (l)`检查确认`l`非空，并通过`listFirst(l)`获取了`ln`，且`linenum`是从`ln->value`转换而来。这表明... |
| 1487 | redis-7.4.2 | raxGenericInsert | Dereference of null pointer | 869 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该分支仅在 `h->size` 为 0 时执行。根据切片中 `raxAddChild` 和 `raxCompressNode` 的实现，它们都会增加 `h->size`... |
| 1489 | redis-7.4.2 | min_expand | Dereference of null pointer | 322 | FP | FP | 在告警行 `singlematch(uchar(*s), p, ep)` 中，指针 `s` 在调用前已通过条件 `s<ms->src_end` 检查，确保其指向有效内存范围，因此解引用 `*s` 是安全的，不会发生空指针解引用。 |
| 1488 | redis-7.4.2 | clusterManagerAddSlots | Dereference of null pointer | 4762 | FP | FP | 告警点 `*err = NULL;` 是对指针 `err` 的解引用，但切片代码显示 `err` 是函数 `clusterManagerAddSlots` 的传入参数，且后续调用 `clusterManagerCheckRedisRe... |
| 1490 | redis-7.4.2 | usUntilEarliestTimer | Dereference of null pointer | 257 | FP | FP | 在while循环中，如果存在有效的te（te->id != AE_DELETED_EVENT_ID），变量`earliest`会被赋值。循环结束后，`earliest`不可能为NULL，因为函数入口已检查`eventLoop->tim... |
| 1492 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12399 | FP | FP | 告警指向的代码行是字符串字面量赋值，并非指针解引用。切片代码显示，在访问 `module->blocked_clients` 之前，已对 `module` 指针进行了非空检查，因此不存在空指针解引用风险。 |
| 1495 | redis-7.4.2 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | VERIFY_READ宏在解引用oldlenp指针前已检查其是否为NULL，切片代码显示告警点存在空指针检查，因此不会发生空指针解引用。 |
| 1494 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12403 | FP | FP | 切片代码显示，在调用 `moduleHoldsTimer(module)` 之前，已经对 `module` 指针进行了空值检查（`if (module == NULL)`），并且后续所有条件判断（包括对 `module->types`... |
| 1496 | redis-7.4.2 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查其是否为NULL，切片代码显示告警点存在防护逻辑，解引用操作仅在指针非空时执行，因此是误报。 |
| 1497 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2537 | FP | FP | 告警点位于 `zslInsert(dstzset->zsl,zval.score,tmp)` 调用处，工具可能认为 `dstzset->zsl` 可能为空。但切片代码显示 `dstzset` 是函数参数，且在调用 `zslInsert... |
| 1502 | redis-7.2.1 | breakstat | Dereference of null pointer | 986 | FP | FP | 告警点前的while循环确保了bl指针不为空，且指向一个可中断的块（isbreakable为真），因此bl->nactvar的访问是安全的。 |
| 1501 | redis-7.2.1 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 代码中对结构体指针`s`的成员`buf`进行了赋值操作（赋值为NULL），并未对`s`指针本身进行解引用。告警规则检测的是解引用空指针，而此处是合法的成员赋值，属于工具误报。 |
| 1500 | redis-7.2.1 | zunionInterDiffGenericCommand | Dereference of null pointer | 2818 | FP | FP | 在告警行 `if (dstzset->zsl->length)` 之前，切片代码中缺少 `dstzset` 的定义和赋值，无法判断其是否为 NULL。但根据告警行所在的 `if (dstkey)` 分支逻辑，`dstkey` 非空时 ... |
| 1503 | redis-7.2.1 | xgroupCommand | Dereference of null pointer | 2697 | FP | FP | 在SETID子命令分支中，cg指针仅在s不为NULL时才会被赋值（通过streamCreateCG），而该分支的代码逻辑保证了当s为NULL时，会先创建stream对象（触发serverAssert），因此cg在解引用前已被正确初始化。 |
| 1504 | redis-7.2.1 | zdiffAlgorithm1 | Dereference of null pointer | 2432 | FP | FP | 告警点位于 zslInsert 调用，该函数内部已通过 serverAssert(!isnan(score)) 确保 score 非 NaN，且切片中未显示 dstzset 或 dstzset->zsl 为 NULL 的赋值路径。代码... |
| 1505 | redis-7.2.1 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1643 | FP | FP | 切片代码显示，在调用`sdsfree(state->lines[linenum])`前，`state->lines`数组的访问依赖于`linenum`变量，但该变量在切片中未定义或赋值。然而，结合告警点所在的循环上下文（`while(... |
| 1506 | redis-7.2.1 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `*coalesced = false;` 是对指针 `coalesced` 的赋值操作，而非解引用。`coalesced` 是函数的入参（`bool *coalesced`），在函数入口处已确保其非空，因此不存在空... |
| 1509 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12227 | FP | FP | 告警指向的代码行是对指针`module`的成员`usedby`的访问，但切片代码显示，在访问`module->usedby`之前，已经通过`if (module == NULL)`检查排除了指针为NULL的情况，因此该解引用是安全的。 |
| 1508 | redis-7.2.1 | dictGetVal | Dereference of null pointer | 805 | FP | FP | 函数 `dictGetVal` 的参数 `de` 是一个指向 `dictEntry` 的指针，切片代码中虽未显示调用方，但该函数是典型的访问器（getter），其设计前提是调用者传入有效的指针。直接解引用参数是此类访问器的标准实现，若... |
| 1510 | redis-7.2.1 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 告警指向的代码行 `*coalesced = true;` 是对非空指针 `coalesced` 的解引用，该指针是函数的传入参数，在切片中可见其被调用前已存在且非空，不存在空指针解引用风险。 |
| 1515 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12220 | FP | FP | 在`module == NULL`的分支中，代码仅对指针`errmsg`进行赋值，并未解引用空指针。告警点所在的赋值操作是安全的，因为`errmsg`是一个有效的指针参数。 |
| 1514 | redis-7.2.1 | cliFillInCommandHelpEntry | Dereference of null pointer | 584 | FP | FP | 切片代码显示，在调用zmalloc后，未对返回值进行空指针检查便直接赋值给help->argv。然而，zmalloc函数内部已包含内存分配失败的处理（zmalloc_oom_handler），该处理函数通常会终止程序或抛出异常，使得后... |
| 1512 | redis-7.2.1 | RM_ListInsert | Dereference of null pointer | 4585 | FP | FP | 告警点位于函数 `listTypeTryConversionAppend` 的调用处，其第一个参数 `key->value` 在 `moduleListIteratorSeek` 函数中有明确的空指针检查（`if (!key->val... |
| 1513 | redis-7.2.1 | cliInitGroupHelpEntries | Dereference of null pointer | 724 | FP | FP | 切片代码显示，`helpEntries` 数组的索引 `pos` 由静态变量 `helpEntriesLen` 初始化并递增，但切片中未定义 `helpEntries` 数组本身或其大小，无法判断 `pos` 是否会越界导致访问空指针... |
| 1517 | redis-7.2.1 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查其是否为NULL，告警点处的解引用操作在oldlenp非NULL的条件下才会执行，因此不存在空指针解引用。 |
| 1518 | redis-7.2.1 | xgroupCommand | Dereference of null pointer | 2693 | FP | FP | 在SETID子命令中，对`s->last_id`的访问发生在`s`已被验证为非NULL的代码路径中。告警点之前的逻辑已确保`s`不为NULL，因此解引用是安全的。 |
| 1519 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12223 | FP | FP | 告警指向的代码行是字符串字面量赋值，并非指针解引用。切片代码显示，在`module == NULL`时，`*errmsg`的赋值是安全的，因为`errmsg`是函数的输入参数，调用方必须提供有效的指针。后续所有对`*errmsg`的赋... |
| 1520 | redis-7.2.1 | __quicklistCompress | Dereference of null pointer | 313 | FP | FP | 切片代码显示，在访问 `quicklist->head` 和 `quicklist->tail` 之前，函数已通过 `if (quicklist->len == 0) return;` 确保链表非空，且 `assert` 语句进一步确... |
| 1521 | redis-7.2.1 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏已对指针 oldp 和 oldlenp 进行了非空和长度校验，若校验失败会通过 goto 跳转返回错误码，不会发生空指针解引用。 |
| 1522 | redis-7.2.1 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 告警行 `token->type = ch2token[ch];` 中，`ch2token` 指针来自 `json->cfg->ch2token`，切片代码显示 `json` 和 `json->cfg` 在函数入口处已解引用，且后续逻... |
| 1523 | redis-7.2.1 | zunionInterDiffGenericCommand | Dereference of null pointer | 2801 | FP | FP | 切片代码显示，在调用 dictExpand(dstzset->dict, dictSize(accumulator)) 之前，dstzset 已通过 dstobj = createZsetObject() 初始化，其 dict 成员由... |
| 1525 | redis-7.2.1 | _quicklistListpackMerge | Dereference of null pointer | 827 | FP | FP | 切片代码逻辑保证了在调用 `keep->count = lpLength(keep->entry);` 时，`keep` 指针指向的节点其 `entry` 字段不为 NULL。`lpMerge` 成功后，`a->entry` 和 `b... |
| 1526 | redis-7.2.1 | moduleFreeContext | Dereference of null pointer | 816 | FP | FP | 在调用 `zfree` 前，代码已通过 `if (ctx->postponed_arrays)` 检查指针非空，且 `zfree` 函数内部也有 `if (ptr == NULL) return;` 的空指针保护，因此不会发生空指针解引用。 |
| 1524 | redis-7.2.1 | __quicklistCompress | Dereference of null pointer | 366 | FP | FP | 在条件 `forward == reverse ｜｜ forward->next == reverse` 中，`forward` 和 `reverse` 指针在循环开始时已分别初始化为链表的头和尾，且循环体确保了 `forward` ... |
| 1528 | redis-7.2.1 | zsetRemoveFromSkiplist | Dereference of null pointer | 1502 | FP | FP | 告警点位于条件判断 `if (de != NULL)` 之前，但该条件明确检查了指针 `de` 是否为 NULL，只有在非 NULL 的情况下才会解引用 `dictGetVal(de)`。切片代码中的逻辑确保了不会发生空指针解引用。 |
| 1527 | redis-7.2.1 | rewriteConfigRewriteLine | Dereference of null pointer | 1252 | FP | FP | 在调用 sdsfree(state->lines[linenum]) 之前，代码已通过 'if (l)' 检查确保 l 非空，并通过 listFirst(l) 获取 ln，且 linenum 是从 ln->value 转换而来。这表明... |
| 1530 | redis-7.2.1 | clusterManagerAddSlots | Dereference of null pointer | 4641 | FP | FP | 告警行 `*err = NULL;` 是对指针 `err` 的解引用，但切片代码显示 `err` 是函数参数，在调用 `clusterManagerCheckRedisReply` 时作为非空参数传入，且该函数内部已检查 `err !... |
| 1531 | redis-7.2.1 | min_expand | Dereference of null pointer | 322 | FP | FP | 在调用 `singlematch` 前，代码已通过 `s<ms->src_end` 检查确保指针 `s` 未越界，因此 `*s` 的解引用是安全的，不会发生空指针解引用。 |
| 1529 | redis-7.2.1 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该分支仅在 `h->size` 为 0 时执行。切片代码显示，在进入此分支前，`h` 已通过 `raxReallocForData` 函数处理，且 `raxReallo... |
| 1532 | redis-7.2.1 | usUntilEarliestTimer | Dereference of null pointer | 276 | FP | FP | 在while循环中，如果存在有效的te（te->id != AE_DELETED_EVENT_ID），变量earliest会被赋值，不会为NULL。循环前已检查eventLoop->timeEventHead不为NULL，且循环条件为... |
| 1534 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12231 | FP | FP | 告警指向的代码行是字符串字面量赋值，并非指针解引用。切片代码显示，在`module`为NULL的分支中，`errmsg`被赋值为一个字符串常量，这是一个安全的赋值操作，不存在空指针解引用。 |
| 1537 | redis-7.2.1 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查其是否为NULL，切片代码显示该宏包含'if (oldp == NULL ｜｜ oldlenp == NULL ｜｜ *oldlenp != sizeof(t))'的条件判断，因此... |
| 1536 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12235 | FP | FP | 告警指向的代码行是字符串字面量赋值，并非指针解引用。切片代码显示，在调用 `moduleHoldsTimer(module)` 之前，`module` 指针已通过 `dictFetchValue` 获取，并在多个条件分支中进行了非空检... |
| 1539 | redis-7.2.1 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | VERIFY_READ宏在解引用oldlenp指针前，已通过条件`oldp == NULL ｜｜ oldlenp == NULL`进行了空指针检查，确保了不会发生空指针解引用。 |
| 1538 | redis-7.2.1 | zdiffAlgorithm2 | Dereference of null pointer | 2492 | FP | FP | 告警行 `htNeedsResize(dstzset->dict)` 检查了 `dstzset->dict` 是否为 NULL，但切片代码显示 `dstzset` 作为函数参数传入，且在函数内部通过 `dictAdd` 和 `zset... |
| 1540 | redis-7.2.1 | zdiffAlgorithm2 | Dereference of null pointer | 2472 | FP | FP | 告警点位于 `zslInsert` 调用，该函数内部有 `serverAssert(!isnan(score));` 断言，且 `zval` 在循环前已通过 `memset(&zval, 0, sizeof(zval));` 初始化，... |
| 1543 | redis-7.2.5 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 代码中`s->buf = NULL;`是对结构体指针`s`的成员进行赋值，并非解引用空指针。该操作是安全的初始化，不构成空指针解引用错误。 |
| 1544 | redis-7.2.5 | breakstat | Dereference of null pointer | 986 | FP | FP | 切片代码显示，在调用`luaK_codeABC`函数前，`bl`指针已通过while循环确保不为空（`while (bl && !bl->isbreakable)`），且后续使用`bl->nactvar`和`&bl->breaklis... |
| 1542 | redis-7.2.5 | zunionInterDiffGenericCommand | Dereference of null pointer | 2819 | FP | FP | 在切片代码中，对 `dstzset` 的访问位于 `if (dstkey)` 条件块内，且其解引用 `dstzset->zsl->length` 之前存在对 `dstobj` 的引用和操作，这表明 `dstobj` 及其内部结构 `d... |
| 1548 | redis-7.2.5 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 告警点是对布尔变量`*coalesced`的赋值，该指针由调用方传入且切片中已通过`if (ecache->delay_coalesce)`条件保护，不存在空指针解引用。 |
| 1547 | redis-7.2.5 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1643 | FP | FP | 告警点位于`sdsfree(state->lines[linenum])`，但切片中未定义变量`linenum`，这很可能是一个拼写错误或未显示的局部变量。结合上下文，`state->lines`数组的访问应在循环控制范围内，且`sd... |
| 1546 | redis-7.2.5 | zdiffAlgorithm1 | Dereference of null pointer | 2433 | FP | FP | 告警点位于 `zslInsert` 调用处，该函数内部已通过 `serverAssert(!isnan(score));` 对输入参数 `score` 进行了断言检查，且 `zval.score` 来源于 `zuiNext` 函数，该... |
| 1551 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12235 | FP | FP | 告警指向的代码行是字符串字面量赋值，不存在对空指针的解引用。切片代码显示，在解引用 errmsg 指针之前，函数已通过多个条件检查确保指针有效，且 errmsg 是函数的输入参数，调用方应保证其非空。 |
| 1552 | redis-7.2.5 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 告警指向的代码行 `*coalesced = true;` 是对非空指针 `coalesced` 的解引用，该指针是函数参数，在切片中可见其作为传入的布尔指针被使用，没有证据表明其为空。工具报告的逻辑错误不成立。 |
| 1550 | redis-7.2.5 | dictGetVal | Dereference of null pointer | 805 | FP | FP | 函数 `dictGetVal` 接收一个指向 `dictEntry` 的指针 `de`，并直接返回其成员 `v.val`。该函数本身不包含空指针检查，但这是一个简单的访问器函数，其调用方有责任确保传入的指针非空。根据常见的编程约定和切... |
| 1556 | redis-7.2.5 | cliFillInCommandHelpEntry | Dereference of null pointer | 584 | FP | FP | 切片代码显示，对help->argv的赋值是调用zmalloc的结果，而zmalloc函数内部已包含对空指针返回的处理（调用zmalloc_oom_handler），因此不会发生空指针解引用。 |
| 1554 | redis-7.2.5 | RM_ListInsert | Dereference of null pointer | 4585 | FP | FP | 在函数moduleListIteratorSeek中，对key、key->value和key->iter进行了明确的空指针检查，并在条件不满足时提前返回0，确保了后续对key->u.list.entry的访问是安全的。切片代码中包含了... |
| 1557 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12228 | FP | FP | 在 module 为 NULL 的分支中，代码直接返回 C_ERR，仅对 errmsg 指针进行了合法的赋值操作，并未解引用空指针。告警点处的代码逻辑是安全的。 |
| 1559 | redis-7.2.5 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查其是否为NULL，告警点位于检查之后，因此解引用是安全的。 |
| 1555 | redis-7.2.5 | cliInitGroupHelpEntries | Dereference of null pointer | 724 | FP | FP | 切片代码显示 `helpEntries` 是一个全局数组，其长度 `helpEntriesLen` 在函数开始时被读取并赋值给 `pos`。在循环中，`pos` 被用作索引递增。虽然切片未显示 `helpEntries` 的声明和 `... |
| 1563 | redis-7.2.5 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警指向的宏 VERIFY_READ 在解引用 oldlenp 前已检查其是否为 NULL，切片代码显示该检查逻辑完整，不存在空指针解引用。 |
| 1560 | redis-7.2.5 | xgroupCommand | Dereference of null pointer | 2693 | FP | FP | 在SETID子命令中，当c->argv[4]为'$'时，访问s->last_id。切片代码显示，s仅在o存在且类型正确时被赋值，否则为NULL。但告警行位于SETID分支，该分支仅在c->argc >= 4且!mkstream时进入，... |
| 1561 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12231 | FP | FP | 告警指向的代码行是字符串字面量赋值给指针，并非解引用空指针。切片代码显示，在`module`为NULL的分支中，`*errmsg`的赋值操作是安全的，因为`errmsg`本身作为函数参数是有效的指针。 |
| 1562 | redis-7.2.5 | __quicklistCompress | Dereference of null pointer | 316 | FP | FP | 告警指向的assert语句用于调试，其条件`quicklist->head->recompress == 0 && quicklist->tail->recompress == 0`仅在`quicklist->head`或`quick... |
| 1566 | redis-7.2.5 | __quicklistCompress | Dereference of null pointer | 369 | FP | FP | 在警告行 `if (forward == reverse ｜｜ forward->next == reverse)` 之前，`forward` 和 `reverse` 已通过 `quicklistDecompressNode` 宏进行... |
| 1565 | redis-7.2.5 | zunionInterDiffGenericCommand | Dereference of null pointer | 2802 | FP | FP | 切片代码显示，在调用 dictExpand(dstzset->dict, dictSize(accumulator)) 之前，dstzset 已通过 dstobj = createZsetObject() 初始化，其 dict 成员在... |
| 1564 | redis-7.2.5 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 切片代码显示，在访问 `ch2token[ch]` 之前，`ch2token` 指针已从 `json->cfg->ch2token` 获取，且 `json->cfg` 在函数入口处被解引用，表明其非空。`ch` 的值来自 `json-... |
| 1567 | redis-7.2.5 | _quicklistListpackMerge | Dereference of null pointer | 869 | FP | FP | 告警点位于条件分支 `if ((lpMerge(&a->entry, &b->entry)))` 内部，该条件确保 `lpMerge` 成功返回非空指针。在成功合并后，`keep` 指针被赋值为 `a` 或 `b`，且其 `entry... |
| 1568 | redis-7.2.5 | moduleFreeContext | Dereference of null pointer | 816 | FP | FP | 在调用 zfree 之前，代码已通过 `if (ctx->postponed_arrays)` 检查指针非空，因此不会发生空指针解引用。告警是工具的逻辑误判。 |
| 1570 | redis-7.2.5 | zsetRemoveFromSkiplist | Dereference of null pointer | 1503 | FP | FP | 告警点位于条件判断 `if (de != NULL)` 之前，但切片代码显示 `de` 被使用前已明确进行了空指针检查，后续的 `dictGetVal(de)` 调用仅在 `de` 非空时执行，逻辑安全。 |
| 1569 | redis-7.2.5 | rewriteConfigRewriteLine | Dereference of null pointer | 1252 | FP | FP | 在调用`sdsfree(state->lines[linenum])`之前，代码已通过`if (l)`检查确保`l`非空，并通过`listFirst(l)`获取`ln`，且`linenum`来自`ln->value`。`state->... |
| 1572 | redis-7.2.5 | clusterManagerAddSlots | Dereference of null pointer | 4642 | FP | FP | 告警指向的代码行 '*err = NULL;' 是对指针的直接赋值，而非解引用空指针。切片代码显示，在后续调用 clusterManagerCheckRedisReply 时，err 指针作为参数传递，其值（NULL）被安全检查 'i... |
| 1573 | redis-7.2.5 | min_expand | Dereference of null pointer | 322 | FP | FP | 在警告行 `singlematch(uchar(*s), p, ep)` 中，对 `s` 的指针解引用受 `s<ms->src_end` 条件保护，确保了 `s` 在解引用前不为空且指向有效内存。切片代码显示了完整的防护逻辑，因此是误报。 |
| 1574 | redis-7.2.5 | usUntilEarliestTimer | Dereference of null pointer | 276 | FP | FP | 在while循环中，如果存在有效的te（te->id != AE_DELETED_EVENT_ID），变量`earliest`会被赋值。循环结束后，`earliest`不可能为NULL，因为函数入口已检查`eventLoop->tim... |
| 1571 | redis-7.2.5 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该分支仅在 `h->size` 为 0 时执行。根据切片代码，`h` 是 `raxReallocForData` 的返回值，该函数在 `data` 不为 NULL 时会... |
| 1576 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12239 | FP | FP | 切片代码显示，在访问 `module->blocked_clients` 之前，已经通过 `if (module == NULL)` 检查了指针 `module` 是否为空。只有当 `module` 不为空时，才会执行到后续的 `el... |
| 1579 | redis-7.2.5 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查其是否为NULL，切片代码显示告警点存在空指针检查，因此不会发生空指针解引用。 |
| 1578 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12243 | FP | FP | 告警指向的代码行是字符串字面量赋值，不存在指针解引用操作。切片代码显示，在调用 `moduleHoldsTimer(module)` 之前，`module` 指针已通过 `dictFetchValue` 获取并进行了非空检查，后续所有... |
| 1577 | redis-7.2.5 | checkMultiPartAof | Dereference of null pointer | 486 | FP | FP | 告警点位于条件判断 `if (listLength(am->incr_aof_list))`，但指针 `am` 已在上一行 `if (am->incr_aof_list)` 中解引用，表明 `am` 非空。切片中 `am` 来自 `a... |
| 1581 | redis-7.2.5 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏已对指针 oldlenp 进行了空值检查（`oldlenp == NULL`），并会在其为空时设置错误码并跳转返回，因此不会发生空指针解引用。 |
| 1580 | redis-7.2.5 | zdiffAlgorithm2 | Dereference of null pointer | 2493 | FP | FP | 告警行调用 htNeedsResize(dstzset->dict) 检查字典是否需要调整大小，该函数内部会检查 dict 指针的有效性（如 dictSlots 和 dictSize 调用），且 dictResize 函数在调用 di... |
| 1582 | redis-7.2.5 | zdiffAlgorithm2 | Dereference of null pointer | 2473 | FP | FP | 告警点位于 `zslInsert` 调用处，但切片代码显示 `dstzset` 和 `dstzset->zsl` 在函数入口处已作为非空参数传入，且 `zslInsert` 函数内部有 `serverAssert(!isnan(sco... |
| 1584 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12586 | FP | FP | 告警指向的代码行是字符串字面量赋值，不存在空指针解引用。在函数的所有错误路径中，`module` 指针在解引用前都经过了 `if (module == NULL)` 的检查，因此该告警是误报。 |
| 1585 | redis-8.0.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2871 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，已经通过 `if (dstkey)` 条件判断了 `dstkey` 非空，并且 `dstzset` 是 `dstobj` 的内部结构，`dstobj` 在函数逻... |
| 1591 | redis-8.0.2 | zdiffAlgorithm1 | Dereference of null pointer | 2494 | FP | FP | 告警点位于 zslInsert 调用，该函数内部已通过 serverAssert(!isnan(score)) 确保 score 非 NaN，且切片中未发现任何可能导致 dstzset 或 dstzset->zsl 为 NULL 的代... |
| 1592 | redis-8.0.2 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1645 | FP | FP | 告警指向的 `sdsfree(state->lines[linenum])` 调用，其参数 `state->lines[linenum]` 在切片中未显示来源，但 `sdsfree` 函数内部已包含对 NULL 指针的检查（`if (... |
| 1589 | redis-8.0.2 | exprTokenToNum | Dereference of null pointer | 688 | FP | FP | 切片代码显示，在访问指针 t 的成员 token_type 之前，函数 exprTokenToNum 的入口处没有对指针 t 进行空值检查。然而，该告警点位于函数内部的条件判断 `if (t->token_type == EXPR_T... |
| 1590 | redis-8.0.2 | dictGenericDelete | Dereference of null pointer | 661 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，已通过 `dictSize(d) == 0` 检查确保字典非空，并且 `idx` 的计算基于哈希值和掩码，是有效的数组索引。告警点位于链表遍历循环中，指针... |
| 1593 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12578 | FP | FP | 切片代码显示，在访问 `module->loadmod->path` 之前，已经对指针 `module` 进行了空值检查（`if (module == NULL)`），并且所有后续的 `else if` 分支都仅在 `module` ... |
| 1596 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12568 | FP | FP | 告警指向的代码行 `*errmsg = "no such module with that name";` 位于 `if (module == NULL)` 条件分支内，对空指针 `errmsg` 的解引用已被前置的指针非空检查所保护... |
| 1595 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12571 | FP | FP | 告警指向的代码行 `*errmsg = "the module can't be unloaded";` 位于 `module == NULL` 检查之后，且 `module->loadmod->path` 的访问发生在 `modul... |
| 1600 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12582 | FP | FP | 切片代码显示，在访问 `module->loadmod->path` 之前，已经检查了 `module` 是否为 NULL。只有当 `module` 不为 NULL 时，才会执行后续的 `sdslen(module->loadmod-... |
| 1599 | redis-8.0.2 | dictGetVal | Dereference of null pointer | 937 | FP | FP | 函数`dictGetVal`接收一个指向`dictEntry`的指针`de`，并直接返回其成员`v.val`。这是一个简单的访问器函数，其安全性完全依赖于调用方传入的指针`de`是否为NULL。切片代码本身没有空指针检查，但这是此类访... |
| 1597 | redis-8.0.2 | clusterSendPing | Dereference of null pointer | 3670 | FP | FP | 告警点 'link->node->ping_sent = mstime();' 位于条件 'if (!link->inbound && type == CLUSTERMSG_TYPE_PING)' 内部，该条件已确保 link->no... |
| 1603 | redis-8.0.2 | RM_ListInsert | Dereference of null pointer | 4704 | FP | FP | 切片代码显示，在调用 `listTypeTryConversionAppend` 前，`key` 指针已在 `moduleListIteratorSeek` 函数中进行了非空检查（`if (!key)`），且该函数在 `key` 为空... |
| 1604 | redis-8.0.2 | cliInitGroupHelpEntries | Dereference of null pointer | 729 | FP | FP | 切片代码显示 `helpEntries` 数组的索引 `pos` 由静态变量 `helpEntriesLen` 初始化并递增，但未提供 `helpEntries` 数组本身的声明或大小信息，无法确认 `pos` 是否会越界。然而，结合... |
| 1605 | redis-8.0.2 | cliFillInCommandHelpEntry | Dereference of null pointer | 589 | FP | FP | 切片代码显示，对指针 `help` 的访问（`help->argc`）发生在函数参数中，该指针由调用者传入，在函数内部未进行空值检查。然而，该告警为逻辑错误类空指针解引用，通常要求指针明确为空。在给定切片中，`help` 作为函数参数... |
| 1607 | redis-8.0.2 | zdiffAlgorithm2 | Dereference of null pointer | 2556 | FP | FP | 告警点 `dictShrinkIfNeeded(dstzset->dict)` 被调用时，`dstzset->dict` 不可能为空指针。在函数逻辑中，`dstzset` 作为参数传入，其内部字典在 `j == 0` 分支中通过 `d... |
| 1609 | redis-8.0.2 | xgroupCommand | Dereference of null pointer | 2726 | FP | FP | 在SETID子命令中，对`s->last_id`的访问发生在`s`被确认非空之后。代码逻辑显示，当`opt`为'SETID'且参数数量正确时，`s`变量已在之前的`lookupKeyWrite`和类型检查中被赋值或确认为NULL，并且... |
| 1610 | redis-8.0.2 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 告警行是一个assert语句，用于在调试时验证条件，在生产环境中会被编译优化掉，不会导致空指针解引用。切片代码显示assert检查的是quicklist->head和quicklist->tail的recompress字段，即使条件不... |
| 1611 | redis-8.0.2 | exprTokensEqual | Dereference of null pointer | 717 | FP | FP | 函数入口处未对指针a和b进行空指针检查，但告警点位于函数内部的条件判断分支，该分支仅在指针非空且token_type为特定值时才会执行。调用memcmp前已通过a->token_type和b->token_type的访问隐式确认了指针... |
| 1616 | redis-8.0.2 | moduleFreeContext | Dereference of null pointer | 827 | FP | FP | 在调用 `zfree(ctx->postponed_arrays)` 之前，代码已通过 `if (ctx->postponed_arrays)` 检查指针非空，因此不会发生空指针解引用。 |
| 1615 | redis-8.0.2 | _quicklistListpackMerge | Dereference of null pointer | 882 | FP | FP | 切片代码逻辑保证了在调用 `keep->count = lpLength(keep->entry);` 时，`keep` 指针指向的节点其 `entry` 字段不为 NULL。因为 `keep` 被赋值为 `a` 或 `b` 的条件是... |
| 1614 | redis-8.0.2 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 在告警行 `if (forward == reverse ｜｜ forward->next == reverse)` 中，对 `forward` 和 `reverse` 的访问受前序循环条件 `depth++ < quicklist-... |
| 1618 | redis-8.0.2 | raxGenericInsert | Dereference of null pointer | 870 | FP | FP | 切片代码显示，在访问 h->size 之前，h 已被重新赋值（例如 h = child 或 h = newh），且这些赋值来自安全的函数调用（如 raxAddChild、raxCompressNode），这些函数返回非空指针或跳转到 ... |
| 1617 | redis-8.0.2 | rewriteConfigRewriteLine | Dereference of null pointer | 1251 | FP | FP | 在调用`sdsfree(state->lines[linenum])`之前，代码已通过`if (l)`检查确保`l`非空，并通过`listFirst(l)`获取`ln`，且`linenum`是从`ln->value`转换而来。这表明`... |
| 1619 | redis-8.0.2 | clusterManagerAddSlots | Dereference of null pointer | 4769 | FP | FP | 告警指向的代码行 '*err = NULL;' 是对指针变量 err 的赋值操作，而非解引用空指针。切片代码中 err 作为参数传入，其本身不为空，且后续在 clusterManagerCheckRedisReply 函数中对其解引用... |
| 1621 | redis-8.0.2 | usUntilEarliestTimer | Dereference of null pointer | 275 | FP | FP | 切片代码显示，函数在遍历链表后，仅在earliest指针非空时才会使用它。earliest的赋值条件确保了它要么指向一个有效的te节点（其id不为AE_DELETED_EVENT_ID），要么保持为NULL。如果链表中的所有节点id都... |
| 1624 | redis-8.0.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2813 | FP | FP | 切片代码显示，在调用 dictExpand(dstzset->dict, ...) 之前，已通过条件 `if (!cardinality_only)` 创建了 dstobj 并赋值 dstzset = dstobj->ptr，且 cr... |
| 1627 | redis-8.0.2 | zdiffAlgorithm2 | Dereference of null pointer | 2534 | FP | FP | 告警点位于 `zslInsert` 调用处，该函数内部已通过 `serverAssert(!isnan(score));` 对输入参数 `score` 进行了断言检查，且 `dstzset->zsl` 在函数调用前已通过 `zuiLe... |
| 1628 | redis-8.0.2 | exprTokenToBool | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问指针 `t` 的成员（如 `token_type`）之前，函数 `exprTokenToBool` 的入口处没有对 `t` 进行空指针检查。然而，该告警点位于 `if (t->token_type == EXPR_... |
| 1634 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 299 | FP | FP | 切片代码显示告警行是对指针 `src` 进行类型转换和数组索引，`src` 是函数入参，在切片内未见其被赋值为 NULL 或存在空指针解引用路径。该行代码逻辑是安全的指针解引用，工具可能误判了指针状态。 |
| 1633 | ffmpeg-7.1.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 413 | FP | FP | 切片代码显示，在访问 `ctx->buffers[buf.index]` 之前，`buf.index` 来自 `ioctl(VIDIOC_DQBUF)` 系统调用，该调用成功返回后 `buf.index` 应为有效值。同时，代码在多个... |
| 1632 | ffmpeg-7.1.1 | finalize_packet | Dereference of null pointer | 678 | FP | FP | 告警指向的代码行`s->st->time_base.den`在调用前已通过`s->st`的指针解引用，但切片代码显示`s->st`仅在条件`s->ic->nb_streams > 1`中被使用，而`s->ic`的指针解引用发生在同一条... |
| 1636 | ffmpeg-7.1.1 | ebml_read_binary | Dereference of null pointer | 1095 | FP | FP | 在调用 `av_buffer_realloc` 成功后，`bin->buf` 指针已被有效分配或重新分配，因此 `bin->buf->data` 不会是空指针。切片代码中 `av_buffer_realloc` 的实现表明，只有在内存... |
| 1637 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 209 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被分配内存（`ptr2 = av_malloc_array(...)`）或设置为 `p->dat... |
| 1639 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 切片代码显示，在告警行`uint8_t *val = in->data[plane];`之前，`in`指针已作为函数参数传入，且后续代码中`in->linesize[plane]`和`in->data[plane]`被多次安全使用，表... |
| 1640 | ffmpeg-7.1.1 | unsharp_slice_16 | Dereference of null pointer | 172 | FP | FP | 切片代码显示，宏定义中 `sc` 和 `sr` 指针的赋值来源于 `fp->sc` 和 `fp->sr`，其值在切片内未显示为空。告警行 `{ NULL }` 是宏展开后函数体的一部分，并非对空指针的解引用。切片中无证据表明 `sc`... |
| 1641 | ffmpeg-7.1.1 | ebml_parse | Dereference of null pointer | 1363 | FP | FP | 切片代码显示，在访问 `level->length` 之前，已通过 `if (matroska->num_levels > 0)` 检查确保 `level` 指针非空。`level` 是从 `matroska->levels` 数组中... |
| 1642 | ffmpeg-7.1.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警位于宏 UPDATE_CACHE 的展开行，该宏本身不包含指针解引用操作。切片代码中未发现对空指针的直接解引用，且关键宏 BITS_AVAILABLE 被定义为常量 1，表明工具可能误判了宏展开的逻辑。 |
| 1645 | ffmpeg-7.1.1 | ebml_read_sint | Dereference of null pointer | 1022 | FP | FP | 告警指向的指针 `num` 是函数参数，由调用者传入，在切片代码中未见其被赋值为 NULL。函数 `avio_r8` 内部有缓冲区边界检查，不会返回空指针解引用。因此，该告警是误报。 |
| 1644 | ffmpeg-7.1.1 | rtp_set_prft | Dereference of null pointer | 646 | FP | FP | 切片代码显示，在调用`av_rescale_q`之前，已对`s->st`的父指针`s`进行了空值检查（`if (!prft)`），且`s->st`的访问发生在该检查之后。在`rtp_set_prft`的函数上下文中，`s`和`s->s... |
| 1646 | ffmpeg-7.1.1 | safe_filename | Dereference of null pointer | 98 | FP | FP | 代码逻辑中，指针 `f` 在循环条件 `*f` 处被解引用前，已通过函数参数传入且循环会检查其是否为 null 终止符，不会解引用 null 指针。该告警是工具对循环条件中指针解引用的误判。 |
| 1649 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，在访问 `in->linesize[plane]` 之前，`in` 指针作为函数参数传入且未被置空，并且在 `s->planeheight[plane] > 1` 的条件下才会使用该值，否则 `linesize` 被赋值... |
| 1650 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 236 | FP | FP | 告警指向的代码行是 `av_assert0` 宏调用，该宏在条件为假时会调用 `abort()` 终止程序。这是一个断言，用于在开发阶段捕获编程错误，其目的就是主动触发程序终止，并非运行时可能发生的空指针解引用漏洞。 |
| 1648 | ffmpeg-7.1.1 | dump_stream_group | Dereference of null pointer | 788 | FP | FP | 切片代码显示，在访问 `stg->streams[i]` 之前，已通过 `if (avctx && stg->nb_streams && ...)` 条件检查了 `stg->nb_streams` 大于0，且循环 `for (int ... |
| 1651 | ffmpeg-7.1.1 | ff_encode_encode_cb | Dereference of null pointer | 275 | FP | FP | 告警点位于条件判断 `if (frame->duration)`，但切片代码显示，在进入该分支前，外层条件 `if (!ret && *got_packet)` 已确保 `frame` 指针非空（因为 `frame` 作为函数参数传入... |
| 1652 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 219 | FP | FP | 告警指向的代码行位于av_assert0宏内部，该宏用于开发调试，在条件不满足时会调用abort()终止程序。这属于主动触发的断言失败，而非意外的空指针解引用，因此是误报。 |
| 1657 | ffmpeg-7.1.1 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 切片代码显示，在DIR_DURATION指令执行前，file指针已通过DIR_FILE指令调用add_file函数进行了有效初始化，并赋值给局部变量file。因此，在访问file->user_duration时，file指针不可能为N... |
| 1656 | ffmpeg-7.1.1 | hls_append_segment | Dereference of null pointer | 1185 | FP | FP | 在警告行 'if (!en->next->discont_program_date_time && !en->discont_program_date_time)' 中，访问 'en->next' 之前，代码逻辑已确保 'en' 不为... |
| 1658 | ffmpeg-7.1.1 | dump_argument | Dereference of null pointer | 516 | FP | FP | 函数参数 `a` 在循环条件 `*p` 中被直接解引用，但切片代码显示 `a` 作为 `const char*` 参数传入，且函数内部逻辑始终在检查 `*p` 非空后才进行后续操作。代码逻辑保证了在 `a` 为 NULL 时，`for... |
| 1660 | ffmpeg-7.1.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 告警点位于条件语句 `if (dpd[pos])` 内部，对 `dpd[pos]` 的访问发生在已确认其为非零值之后，因此不会发生空指针解引用。 |
| 1659 | ffmpeg-7.1.1 | kalman_smoothen | Dereference of null pointer | 585 | FP | FP | 在循环中，`best_hist_ptr` 被初始化为 NULL，但随后在 `dot > optimal_gain` 的条件下被赋值为 `ptr`。只有当 `optimal_gain > 0` 时，函数才会继续执行到告警行，而此条件成立... |
| 1661 | ffmpeg-7.1.1 | id3v2_parse | Dereference of null pointer | 1055 | FP | FP | 告警点位于条件分支 `extra_func->read(...)`，但切片代码显示 `extra_func` 仅在 `get_extra_meta_func` 返回非空指针时被赋值，且该函数调用前已通过 `extra_meta && ... |
| 1664 | ffmpeg-7.1.1 | ebml_read_ascii | Dereference of null pointer | 1077 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，因此对 `*str` 的解引用不会发生，不存在空指针解引用风险。 |
| 1663 | ffmpeg-7.1.1 | split_commandline | Dereference of null pointer | 809 | FP | FP | 告警点位于检查字符串是否为双破折号'--'的逻辑，代码已通过`opt[0] == '-' && opt[1] == '-' && !opt[2]`确保在访问`opt[2]`前已确认`opt`非空且长度至少为2，不会发生空指针解引用。 |
| 1662 | ffmpeg-7.1.1 | set_bframe_chain_length | Dereference of null pointer | 1596 | FP | FP | 在告警行`s->input_picture[i - 1]->f->data[0]`处，切片代码显示其位于`s->b_frame_strategy == 1`的条件分支内，且外层有`if (s->input_picture[i] && ... |
| 1665 | ffmpeg-7.1.1 | output_packet | Dereference of null pointer | 1103 | FP | FP | 在访问 timestamp_packet 指针前，代码已通过 `if (timestamp_packet)` 进行了非空检查，确保了指针的有效性。因此，后续对 `timestamp_packet->unwritten_size` 的访... |
| 1666 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 286 | FP | FP | 切片代码显示，在访问 `ost->ist->par` 之前，`ost` 和 `ost->ist` 的有效性已在函数入口处通过 `av_assert0` 宏间接保证，且告警行位于 `enc_ctx->codec_type == AVME... |
| 1668 | ffmpeg-7.1.1 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 切片代码显示，在访问 `file->inpoint` 之前，`file` 指针已在 `DIR_FILE` 分支通过 `add_file` 成功初始化并赋值给局部变量 `file`。该分支在 `DIR_INPOINT` 之前执行，确保了... |
| 1669 | ffmpeg-7.1.1 | sb_decode | Dereference of null pointer | 1348 | FP | FP | 在访问 `innov_save` 指针前，代码已通过 `if (st->innov_save)` 检查其非空，并随后在循环内通过 `if (st->innov_save)` 再次确认后才进行赋值操作，因此不会发生空指针解引用。 |
| 1670 | ffmpeg-7.1.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警行位于条件 `if ((*child)->state * 2 == -t->state)` 内，该条件已确保 `*child` 非空（因为 `t->state` 非零且 `t->state & 1` 为假，且 `child` 指向... |
| 1671 | ffmpeg-7.1.1 | check_header_mismatch | Dereference of null pointer | 519 | FP | FP | 告警指向的代码行 'curr = curr->next;' 位于一个受循环条件 'curr != child' 和 'i < FLAC_MAX_SEQUENTIAL_HEADERS' 严格保护的循环体内，且循环前有 'curr = h... |
| 1674 | ffmpeg-7.1.1 | mpegts_open_filter | Dereference of null pointer | 495 | FP | FP | 告警指向的 `av_log` 调用被宏定义为空操作 `while(0)`，因此其第一个参数 `ts->stream` 不会被解引用，不存在空指针解引用风险。 |
| 1676 | ffmpeg-7.1.1 | build_table | Dereference of null pointer | 204 | FP | FP | 告警点位于 `table[j].len = -subtable_bits;`，但切片代码显示 `table` 指针在赋值前已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_i... |
| 1675 | ffmpeg-7.1.1 | guess_mv | Dereference of null pointer | 432 | FP | FP | 在告警行 `else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])` 之前，已有条件 `if (s->last_pic.motion_val[0])` 检查了同一指针，... |
| 1677 | ffmpeg-7.1.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警点位于循环内部，该循环受条件 `if (chapters && nb_chapters)` 保护。切片代码显示，在告警行 `AVChapter *chp = chapters[i];` 被执行之前，已经通过 `if (chapte... |
| 1679 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 78 | FP | FP | 告警位于宏 UPDATE_CACHE 的展开行，该宏及其相关宏（如 GET_CACHE）仅操作结构体字段，不涉及指针解引用。切片代码中未发现对空指针的实际解引用操作，因此该告警为误报。 |
| 1680 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警点位于对 `in->data[plane]` 的强制类型转换，切片代码显示 `in` 是函数参数且非空，且其数据指针 `data[plane]` 在循环前已多次使用，表明指针有效。工具可能误判了类型转换的上下文。 |
| 1681 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 333 | FP | FP | 告警点位于条件语句 `if (s->do_video)` 内部，该条件确保 `outlink` 不为 NULL 时才会执行到 `av_rescale_q` 调用。切片代码显示 `outlink` 在 `s->do_video` 为真时... |
| 1682 | ffmpeg-7.1.1 | av_dump_format | Dereference of null pointer | 898 | FP | FP | 切片代码显示，在访问 printed 数组前，已通过条件 'if (ic->nb_streams && !printed) return;' 确保 printed 非空。后续访问 printed[program->stream_ind... |
| 1683 | ffmpeg-7.1.1 | check_header_mismatch | Dereference of null pointer | 475 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 之前，`curr` 变量通过 `curr = curr->next;` 在 while 循环中迭代，且循环条件 `curr != child` 确保了 `curr`... |
| 1684 | ffmpeg-7.1.1 | update_context_from_thread | Dereference of null pointer | 438 | FP | FP | 切片代码显示，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 条件确保 `hwaccel` 指针... |
| 1685 | ffmpeg-7.1.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 告警位于宏 UPDATE_CACHE_32 的展开处，该宏最终展开为对 GetBitContext 结构体指针 's' 的访问。函数 get_bits_long 的入口处有 'av_assert2' 断言，且其调用者 get_bits... |
| 1686 | ffmpeg-7.1.1 | activate | Dereference of null pointer | 186 | FP | FP | 在告警行（frame->pts = s->pts;）之前，代码已通过条件分支（s->stop_mode == MODE_ADD 或 MODE_CLONE）为 frame 指针分配了有效的 AVFrame 对象（通过 ff_get_vi... |
| 1687 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 200 | FP | FP | 切片代码显示，在访问ptr2[x]之前，ptr2已通过av_malloc_array分配内存，且分配失败时函数会提前返回错误，因此ptr2不为空。此外，访问发生在条件分支`if (depth == 1)`内部，该分支仅在`avctx-... |
| 1688 | ffmpeg-7.1.1 | check_available | Dereference of null pointer | 616 | FP | FP | 告警指向的代码行中，`TAB_MVF` 是一个宏，用于索引数组 `tab_mvf`。切片代码显示 `min_pu_width` 已定义且为正数，索引计算有效。`is_available` 函数被调用并作为逻辑与的一部分，其返回值用于判... |
| 1689 | ffmpeg-7.1.1 | ff_encode_encode_cb | Dereference of null pointer | 272 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，该行代码仅在 `avpkt->pts` 为 `AV_NOPTS_VALUE` 时才会执行对 `frame->pts` 的访问。切片代码显... |
| 1690 | ffmpeg-7.1.1 | rtp_parse_one_packet | Dereference of null pointer | 888 | FP | FP | 切片代码显示，在告警行访问 `buf[0]` 之前，已存在条件判断 `if (!buf)` 和 `if (len < 12)`。若 `buf` 为 NULL，函数会提前返回；若 `len` 小于12，也会提前返回。因此，在到达告警行时... |
| 1691 | ffmpeg-7.1.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已经通过条件 `if (dpd[pos])` 和 `if (s->peak[i][j] && ...)` 进行了检查，确保了指针 `dpd` 指向的数组内存已被成功分配和初始化，因此不... |
| 1692 | ffmpeg-7.1.1 | ost_add | Dereference of null pointer | 1541 | FP | FP | 切片代码显示，在访问 `ist->st->duration` 之前，存在条件 `if (ost->ist && ost->ist->st->duration > 0)`，该条件已检查 `ost->ist` 和 `ost->ist->s... |
| 1694 | ffmpeg-7.1.1 | nal_parse_units | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `list->nalus` 之前，已通过 `if (!tmp)` 检查了 `av_fast_realloc` 的返回值，若分配失败会提前返回错误。因此，后续对 `list->nalus` 的赋值和使用是在确保指针... |
| 1693 | ffmpeg-7.1.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1420 | FP | FP | 切片代码显示 `scale_matrix` 在赋值前已初始化为 NULL，且其使用点 `scale_m = scale_matrix[pos];` 受条件 `if (sps->scaling_list_enabled && !(tra... |
| 1696 | ffmpeg-7.1.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 切片代码显示`s->buffer`是一个数组访问，`s`指针本身在函数调用时已通过上下文（未在切片中显示）被验证为非空，且数组索引`index >> 3`是安全的位运算，不会导致空指针解引用。该告警是工具对数组访问的误判。 |
| 1695 | ffmpeg-7.1.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1513 | FP | FP | 告警点位于`ff_get_audio_buffer(link, frame->nb_samples)`调用，工具可能认为`frame`指针为空。但在调用此函数前，代码已通过`if (av_frame_is_writable(frame... |
| 1697 | ffmpeg-7.1.1 | asf_parse_packet | Dereference of null pointer | 1307 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data` 之前，已通过 `av_assert0(asf_st)` 确保 `asf_st` 非空，且 `asf_st->pkt.data` 的赋值来源于 `av_new_packet` 或... |
| 1698 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 146 | FP | FP | 告警行代码 `*(const void**)&alpMmxFilter[s*i] = alpSrcPtr[i];` 在 `if (CONFIG_SWSCALE_ALPHA && hasAlpha)` 条件保护下执行，切片代码显示 `a... |
| 1699 | ffmpeg-7.1.1 | choose_rct_params | Dereference of null pointer | 1008 | FP | FP | 告警指向的代码行 `r = *((const uint16_t *)(src[2] + x*2 + stride[2]*y));` 位于 `else if (f->use32bit ｜｜ transparency)` 分支内，该分支仅... |
| 1701 | ffmpeg-7.1.1 | unsharp_slice_8 | Dereference of null pointer | 173 | FP | FP | 切片代码显示，宏定义中 `sc` 和 `sr` 是从 `fp` 结构体获取的指针，并在循环中使用 `memset` 对 `sc[sc_offset + y]` 进行初始化，这表明指针在使用前已被赋值和访问，未发现空指针解引用。告警点 ... |
| 1704 | ffmpeg-7.1.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码显示，对指针 `dpd` 的访问发生在对其有效性进行明确检查之后（`if (dpd[pos] && ...)`），且 `dpd` 指向 `out->data` 数组的有效元素，不存在空指针解引用。 |
| 1703 | ffmpeg-7.1.1 | ebml_parse | Dereference of null pointer | 1380 | FP | FP | 切片代码显示，在告警行（line 1380）访问`level`指针前，已通过`if (matroska->num_levels > 0)`进行了检查，确保了`level`不为NULL。该指针是从`matroska->levels`数组... |
| 1707 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 683 | FP | FP | 告警指向的FFSWAP宏调用位于条件分支`if (js_databuf == q->decoded_bytes_buffer)`内部，该分支仅在指针相等时执行交换操作，而交换操作本身不会导致空指针解引用。切片代码显示`ptr1`和`p... |
| 1702 | ffmpeg-7.1.1 | mov_write_trak_tag | Dereference of null pointer | 4191 | FP | FP | 告警指向的代码行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 中，`st` 是函数参数，在切片代码的多个调用路径中（如 `mov_write_tkhd... |
| 1708 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 303 | FP | FP | 切片代码显示告警行是对指针进行类型转换和位移操作，指针'src'作为函数参数传入且已在循环中被使用，其有效性应在调用前得到保证。切片内无证据表明'src'为NULL，且其解引用发生在安全的数组索引访问内，属于工具误判。 |
| 1709 | ffmpeg-7.1.1 | ff_rdt_parse_header | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在调用 init_get_bits 函数时，已对 buffer 指针（即参数 buf）进行了空指针检查（if (!buffer)），若为空则返回错误，因此后续对 buf 的访问是安全的。 |
| 1710 | ffmpeg-7.1.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 代码在访问 `info->key_ids[i]` 前已通过 `if (info)` 检查了指针非空，且循环条件 `i < info->num_key_ids` 确保了 `key_ids` 数组索引有效。告警点 `av_free(inf... |
| 1712 | ffmpeg-7.1.1 | build_table | Dereference of null pointer | 170 | FP | FP | 告警点位于循环内部，`table`指针在循环开始前已通过`table = &vlc->table[table_index];`正确初始化，且`j`的计算范围受`table_size`限制，不会越界。切片代码逻辑保证了`table`非空... |
| 1714 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 293 | FP | FP | 告警指向的代码行 `sample[0][x] = src[x * pixel_stride + stride * y];` 是对数组元素的赋值，`src` 是函数参数，`sample[0]` 指向已分配内存的缓冲区，不存在对空指针的解... |
| 1713 | ffmpeg-7.1.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 告警指向的 `memcpy(info->key_ids[j], side_data, key_id_size)` 行，其 `info->key_ids[j]` 指针已在 `av_encryption_init_info_alloc` ... |
| 1716 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 166 | FP | FP | alpMmxFilter 的赋值操作受条件 `CONFIG_SWSCALE_ALPHA && hasAlpha` 保护，当条件不满足时 alpMmxFilter 为 NULL，但告警点处的赋值仅在条件为真时执行，因此不会发生空指针解引用。 |
| 1717 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的调用，该宏在切片中已定义，且其展开依赖于有效的 GetBitContext 指针 's'。函数 get_vlc2 的调用约定要求传入非空的 's' 和 'table' 指针，且切片内没有证据表明... |
| 1718 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在告警行（linesize 计算）之前，已通过条件 `s->planeheight[plane] > 1` 进行保护。当 `s->planeheight[plane]` 不大于1时，`linesize` 被赋值为0，从而... |
| 1720 | ffmpeg-7.1.1 | mov_write_trak_tag | Dereference of null pointer | 4196 | FP | FP | 切片代码中，告警行 `is_clcp_track(track) && st->sample_aspect_ratio.num` 的条件检查确保了 `st` 指针在解引用其成员 `sample_aspect_ratio.num` 之前已... |
| 1719 | ffmpeg-7.1.1 | set_bframe_chain_length | Dereference of null pointer | 1611 | FP | FP | 切片代码显示，在访问 `s->input_picture[i]` 前，循环条件 `i < b_frames + 1` 已确保 `i` 不会超过 `b_frames`，且前面的逻辑（如 `b_frames = FFMAX(0, i - ... |
| 1721 | ffmpeg-7.1.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示 get_bits 函数在调用宏前已通过参数接收 GetBitContext *s 指针，且函数内所有宏调用均使用该指针。没有证据表明指针 s 在函数入口或宏展开前为 nul... |
| 1722 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 472 | FP | FP | 告警指向宏 `DECODE_CODEWORD` 的调用，但切片代码显示该宏内部包含 `UPDATE_CACHE` 和 `GET_CACHE` 操作，这些操作负责从比特流上下文 `gb` 中安全地读取数据并更新状态。`gb` 指针在函数... |
| 1724 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确初始化为 `q->decoded_bytes_buffer`，这是一个有效的缓冲区指针。循环条件检查... |
| 1723 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 687 | FP | FP | 告警指向的代码行 `q->decoded_bytes_buffer[i] = *ptr2--;` 中，`ptr2` 被初始化为 `js_databuf + js_block_align - 1`，而 `js_databuf` 是函数参... |
| 1726 | ffmpeg-7.0.1 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 切片代码显示，在访问 `s->st->time_base.den` 和 `s->st->time_base.num` 之前，已经通过条件 `s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->i... |
| 1727 | ffmpeg-7.0.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 412 | FP | FP | 切片代码显示，在访问 `ctx->buffers[buf.index]` 之前，`buf.index` 已通过 `ioctl(ctx_to_m2mctx(ctx)->fd, VIDIOC_DQBUF, &buf)` 调用从驱动成功获取... |
| 1729 | ffmpeg-7.0.1 | ebml_read_binary | Dereference of null pointer | 1088 | FP | FP | 在调用`memset`之前，`av_buffer_realloc`函数已成功返回（`ret < 0`条件未触发），这保证了`bin->buf`和`bin->buf->data`是有效的非空指针。切片代码显示了完整的成功路径，不存在空指... |
| 1730 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问`ptr2[x]`之前，`ptr2`已在条件分支中通过`av_malloc_array`分配内存或赋值为`p->data[0]`，且后续循环条件`x < (w + 7 >> 3) * depth`确保了索引`x`在... |
| 1732 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 告警点位于宏展开内部，其访问的数组索引 `val[(x)]` 等受循环变量 `x` 和 `y` 的严格约束，且循环边界已通过 `s->planewidth[plane] - 1` 和 `s->planeheight[plane] - ... |
| 1733 | ffmpeg-7.0.1 | unsharp_slice_16 | Dereference of null pointer | 141 | FP | FP | 切片代码显示，在宏展开的函数中，指针 'sc' 在循环内被使用前，已通过 'fp->sc' 赋值，且循环内 'sc[sc_offset + y]' 的访问基于该指针。没有证据表明 'sc' 或 'fp->sc' 在此上下文中为 nul... |
| 1734 | ffmpeg-7.0.1 | ebml_parse | Dereference of null pointer | 1354 | FP | FP | 切片代码显示，在访问 `level->length` 之前，已通过 `if (matroska->num_levels > 0)` 检查确保 `level` 指针非空。因此，对 `level` 的访问是安全的，不存在空指针解引用。 |
| 1735 | ffmpeg-7.0.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警指向的宏 `UPDATE_CACHE` 展开后不直接解引用指针，且切片中 `BITS_AVAILABLE` 宏被定义为常量1，表明循环条件 `BITS_AVAILABLE(re, gb)` 恒为真，代码逻辑旨在持续读取比特流，而非... |
| 1737 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码显示告警行是对指针'src'进行类型转换和偏移访问，该指针是函数参数，在调用前已由调用者确保非空。代码逻辑是安全的数组索引访问，不存在对空指针的解引用。 |
| 1738 | ffmpeg-7.0.1 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 告警点 's->st->time_base' 的访问发生在对 'prft' 指针进行非空检查之后，且切片中未显示 's' 或 's->st' 可能为空的赋值或检查。代码逻辑表明，在到达告警行之前，程序已因内存分配失败而提前返回，因此该... |
| 1739 | ffmpeg-7.0.1 | ebml_read_sint | Dereference of null pointer | 1015 | FP | FP | 切片代码显示，avio_r8函数内部已对AVIOContext指针s进行了空指针检查（s->buf_ptr >= s->buf_end），且当缓冲区耗尽时返回0，因此对pb的间接解引用是安全的。 |
| 1740 | ffmpeg-7.0.1 | safe_filename | Dereference of null pointer | 97 | FP | FP | 代码逻辑中，指针 `f` 在循环条件 `*f` 处被解引用，但该指针作为函数参数传入，并在循环前已用于赋值给 `start`，表明其非空。循环条件 `*f` 是检查字符是否为 `'\0'`，这是安全的字符串遍历方式，不会解引用空指针。 |
| 1743 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，当 `s->planeheight[plane] > 1` 为假时，`linesize` 被显式赋值为 0，此时 `val` 指针的偏移计算 `val += linesize;` 不会导致空指针解引用，因为偏移量为0。代... |
| 1744 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 225 | FP | FP | 告警点位于av_assert0宏内，该宏用于调试断言，在条件不满足时会调用abort()终止程序，这是预期的错误处理行为，并非逻辑错误导致的空指针解引用。 |
| 1742 | ffmpeg-7.0.1 | dump_stream_group | Dereference of null pointer | 751 | FP | FP | 切片代码显示，在访问 `stg->streams[i]` 之前，已通过 `if (avctx && stg->nb_streams && ...)` 条件检查了 `stg->nb_streams` 大于0，且后续循环 `for (in... |
| 1746 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 208 | FP | FP | 告警点位于av_assert0宏内部，该宏用于开发调试，在条件不满足时会调用abort()终止程序，这属于主动的防御性断言而非空指针解引用错误。切片代码显示该断言检查了frame指针的多个字段，逻辑正确，不会导致运行时空指针解引用。 |
| 1745 | ffmpeg-7.0.1 | ff_encode_encode_cb | Dereference of null pointer | 274 | FP | FP | 切片代码显示，在访问 `frame->duration` 之前，已经存在条件 `if (frame && (codec->caps_internal & FF_CODEC_CAP_EOF_FLUSH))` 的检查，并且告警所在行位于 ... |
| 1752 | ffmpeg-7.0.1 | concat_parse_script | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `file->user_duration` 之前，`file` 指针已在 `DIR_FILE` 分支通过 `add_file` 成功初始化并赋值，且存在前置检查 `(dir->flags & NEEDS_FILE... |
| 1753 | ffmpeg-7.0.1 | dump_argument | Dereference of null pointer | 507 | FP | FP | 函数参数 `a` 被直接用于循环条件 `*p`，若 `a` 为 NULL 指针，解引用前已发生段错误，但函数为静态内部函数，其调用方应在调用前确保参数非空。切片中虽无直接调用点，但基于函数语义（打印参数）和常见编码实践，可推断调用方会... |
| 1751 | ffmpeg-7.0.1 | hls_append_segment | Dereference of null pointer | 1171 | FP | FP | 在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 之前，代码已通过 `en = vs->segments;` 赋值，且... |
| 1754 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 297 | FP | FP | 告警指向的代码行 `sample[0][x] = ((uint16_t*)(src + stride*y))[x];` 是对指针 `src` 的合法解引用，切片中 `src` 是函数入参且非空，且该行代码本身不涉及空指针解引用。工具可... |
| 1755 | ffmpeg-7.0.1 | kalman_smoothen | Dereference of null pointer | 584 | FP | FP | 切片代码显示，在解引用 `best_hist_ptr` 之前，已通过 `if (optimal_gain <= 0)` 和 `if (dot <= 0)` 等条件检查确保其不为空，且 `best_hist_ptr` 仅在 `optim... |
| 1756 | ffmpeg-7.0.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 告警点位于条件语句 `if (dpd[pos])` 内部，对 `dp1` 和 `dp2` 的赋值仅在 `dpd[pos]` 为真（非零）时执行。切片代码显示 `dpd` 数组在多个循环中被赋值，其元素值可能为零，因此条件检查有效，不会... |
| 1757 | ffmpeg-7.0.1 | id3v2_parse | Dereference of null pointer | 1054 | FP | FP | 告警点位于条件分支 `extra_func->read(...)` 的调用处，但切片代码显示 `extra_func` 仅在 `get_extra_meta_func(tag, isv34)` 返回非空指针时被赋值。该函数返回指针或 ... |
| 1759 | ffmpeg-7.0.1 | split_commandline | Dereference of null pointer | 800 | FP | FP | 切片代码显示，在调用 `find_option` 后，对指针 `po` 的访问 `po->name` 位于 `if (po->name)` 条件判断内部。该条件判断确保了只有当 `po->name` 非空（即 `po` 指向有效结构体... |
| 1760 | ffmpeg-7.0.1 | ebml_read_ascii | Dereference of null pointer | 1070 | FP | FP | 切片代码显示 `av_free(*str)` 被宏定义为 `while(0)`，这是一个空操作宏，不会发生解引用。因此，不存在对空指针的解引用逻辑错误。 |
| 1761 | ffmpeg-7.0.1 | output_packet | Dereference of null pointer | 1102 | FP | FP | 在访问 `timestamp_packet->unwritten_size` 之前，代码已通过 `if (timestamp_packet)` 检查了指针非空，因此不会发生空指针解引用。告警点位于该条件判断的保护块内，是安全的。 |
| 1758 | ffmpeg-7.0.1 | choose_rct_params | Dereference of null pointer | 983 | FP | FP | 告警点位于条件分支 `else` 块中，该分支仅在 `lbd` 为假时执行。切片代码中未显示 `lbd` 变量的定义，但告警规则为'空指针解引用'，而解引用对象是 `src[1]` 和 `src[2]`。`src` 是函数的传入参数，... |
| 1764 | ffmpeg-7.0.1 | concat_parse_script | Dereference of null pointer | 561 | FP | FP | 告警点位于DIR_INPOINT分支，该分支仅在dir->flags包含NEEDS_FILE且cat->nb_files>0时可达。切片代码显示，在进入switch前已检查NEEDS_FILE标志，若cat->nb_files为0则会... |
| 1767 | ffmpeg-7.0.1 | sb_decode | Dereference of null pointer | 1347 | FP | FP | 告警点位于 `if (st->innov_save)` 条件块内，该条件已确保 `innov_save` 指针不为空。在条件块内部，`innov_save` 被赋值为 `st->innov_save + 2 * offset`，且 `... |
| 1769 | ffmpeg-7.0.1 | check_header_mismatch | Dereference of null pointer | 520 | FP | FP | 切片代码显示，在访问 `header->link_penalty[i]` 之前，`i` 的值由 `for` 循环控制，且循环条件 `curr != child` 和 `i < FLAC_MAX_SEQUENTIAL_HEADERS` ... |
| 1770 | ffmpeg-7.0.1 | get_pict_type | Dereference of null pointer | 135 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效范围，这确保了 `unit->conte... |
| 1768 | ffmpeg-7.0.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警行位于条件 `if ((*child)->state * 2 == -t->state)` 内，该条件仅在 `t->state` 非零且 `t->state` 为偶数（`!(t->state & 1)`）时才会被评估。进入此分支前... |
| 1772 | ffmpeg-7.0.1 | mpegts_open_filter | Dereference of null pointer | 497 | FP | FP | 告警指向的 `av_log` 调用被宏定义为 `while(0)`，这是一个空操作，不会发生空指针解引用。切片代码中 `ts->stream` 的值虽未知，但宏展开确保了该表达式不会被求值，因此告警是误报。 |
| 1773 | ffmpeg-7.0.1 | guess_mv | Dereference of null pointer | 428 | FP | FP | 切片代码显示，在告警行使用 `s->last_pic.f->data[0]` 之前，已通过 `if (s->last_pic.f && s->last_pic.f->data[0])` 进行了非空检查，确保了指针的有效性。因此，该处解... |
| 1774 | ffmpeg-7.0.1 | build_table | Dereference of null pointer | 204 | FP | FP | 告警点位于 `table[j].len = -subtable_bits;`，但切片代码显示 `table` 指针在赋值前已通过 `alloc_table` 成功分配并检查了 `table_index`，且 `j` 的计算范围受 `t... |
| 1775 | ffmpeg-7.0.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `chapters[i]` 之前，外层条件 `if (chapters && nb_chapters)` 和 `if (m)` 已确保 `chapters` 非空且 `nb_chapters` 大于0，同时循环 ... |
| 1777 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警点位于宏展开内部，涉及对指针`val`的偏移访问。切片代码显示`val`被正确初始化为指向`in->data[plane]`，且循环边界`x`和`linesize`的计算确保了访问不会越界或解引用空指针。代码逻辑保证了指针的有效性... |
| 1778 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 332 | FP | FP | 告警点位于条件分支 `if (s->do_video)` 内部，该分支仅在 `s->do_video` 为真时执行。切片代码显示 `outlink` 在同一分支的上一行被定义为 `s->do_video ? ctx->outputs[... |
| 1780 | ffmpeg-7.0.1 | check_header_mismatch | Dereference of null pointer | 476 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 之前，`curr` 变量通过 `curr = curr->next;` 在 `while (curr != child)` 循环中遍历链表，该循环条件确保了 `cu... |
| 1779 | ffmpeg-7.0.1 | av_dump_format | Dereference of null pointer | 834 | FP | FP | 切片代码显示，在访问 `printed` 数组前，已通过 `if (ic->nb_streams && !printed) return;` 确保了当 `ic->nb_streams` 非零时 `printed` 指针非空。后续对 `... |
| 1781 | ffmpeg-7.0.1 | update_context_from_thread | Dereference of null pointer | 360 | FP | FP | 切片代码显示，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 条件确保 `hwaccel` 不为... |
| 1782 | ffmpeg-7.0.1 | choose_rct_params | Dereference of null pointer | 984 | FP | FP | 切片代码显示，在lbd为假的分支中，对src[0]、src[1]、src[2]进行了指针解引用。告警点位于src[2]的解引用行。函数参数`const uint8_t *src[3]`表明src是一个包含三个有效指针的数组，且切片中未... |
| 1784 | ffmpeg-7.0.1 | activate | Dereference of null pointer | 186 | FP | FP | 告警点位于`s->eof`为真的分支内，该分支中`frame`变量在赋值后（通过`ff_get_video_buffer`或`av_frame_clone`）均进行了空指针检查，确保非空后才执行解引用`frame->pts`。因此不存... |
| 1783 | ffmpeg-7.0.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 告警点位于宏 UPDATE_CACHE_32 的展开处，该宏最终调用 UPDATE_CACHE_LE_32，其内部逻辑包含对指针 'gb' 的访问。切片代码显示，在调用 OPEN_READER(re, s) 时，'s' 指针已通过宏展... |
| 1787 | ffmpeg-7.0.1 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 在告警行`if ((buf[0] & 0xc0) != (RTP_VERSION << 6))`之前，代码已通过`if (!buf)`和`if (len < 12)`检查，确保`buf`非空且长度足够，因此对`buf[0]`的解引用是... |
| 1785 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 199 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被分配内存（`ptr2 = av_malloc_array(...)`）或设置为 `p->dat... |
| 1788 | ffmpeg-7.0.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 告警点 `dpd[pos] = 255;` 处的指针 `dpd` 在函数开头已通过三元条件运算符赋值，其来源为 `out->data[s->pd]` 或 `out->data[0]`。`out` 是传入的非空 AVFrame 指针，其... |
| 1786 | ffmpeg-7.0.1 | ff_encode_encode_cb | Dereference of null pointer | 271 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，其访问 `frame->pts` 的前提是 `frame` 指针非空。切片代码显示，在该条件块之前存在 `if (frame && (c... |
| 1790 | ffmpeg-7.0.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 切片代码显示`s->buffer`是一个数组访问，`s`指针本身在函数参数中已传入，其有效性应由调用者保证。函数内部逻辑是安全的数组索引操作，不存在对空指针的直接解引用。该告警可能是工具对指针别名或结构体成员访问的误判。 |
| 1789 | ffmpeg-7.0.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1507 | FP | FP | 告警点位于switch-case分支内，该分支仅在link->type为AVMEDIA_TYPE_AUDIO时执行。切片代码显示，函数入口处已对输入指针*rframe解引用并赋值给frame，且在此之前调用了av_frame_is_w... |
| 1792 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 148 | FP | FP | 切片代码显示，在解引用 alpSrcPtr 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，alpSrcPtr 仅在条件为真时被赋值，否则为 NULL。在告警行所在的代码块中，该条... |
| 1791 | ffmpeg-7.0.1 | asf_parse_packet | Dereference of null pointer | 1306 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data[i]` 之前，已通过 `av_assert0(asf_st)` 断言 `asf_st` 非空，且 `asf_st->pkt.data` 在循环前已通过 `av_new_packe... |
| 1793 | ffmpeg-7.0.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在访问 dp1[pos] 和 dp2[pos] 之前，已通过条件 `if (dpd[pos])` 进行了检查，这确保了指针 dpd 在解引用时不为空，从而防止了空指针解引用。 |
| 1795 | ffmpeg-7.0.1 | unsharp_slice_8 | Dereference of null pointer | 142 | FP | FP | 切片代码显示，在宏展开的函数定义中，`sc` 和 `sr` 等指针在解引用前已从 `fp` 结构体明确赋值，且存在 `if (!amount)` 的早期返回路径，该路径使用安全的 `av_image_copy_plane` 函数，不会... |
| 1796 | ffmpeg-7.0.1 | mov_write_trak_tag | Dereference of null pointer | 3899 | FP | FP | 告警指向的代码行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 中，`st` 是函数参数，在切片代码的调用上下文中（如 `mov_write_trak_... |
| 1797 | ffmpeg-7.0.1 | ebml_parse | Dereference of null pointer | 1371 | FP | FP | 告警行位于条件分支 `else if (level->length != EBML_UNKNOWN_LENGTH)` 中，该分支仅在 `level` 指针非空时才会执行。切片代码显示，`level` 在函数开头被赋值为 `matros... |
| 1798 | ffmpeg-7.0.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码显示，在访问 `dpd[pos - 1]`、`dpd[pos + 1]`、`dpd[poa]` 和 `dpd[pob]` 之前，已通过条件 `(!j ｜｜ ...)`、`(j == (out->width - 1) ｜｜ ..... |
| 1801 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 682 | FP | FP | 告警指向的FFSWAP宏用于交换两个uint8_t变量的值，其参数ptr1和ptr2在切片中均有明确的非空定义和赋值，不存在空指针解引用。 |
| 1802 | ffmpeg-7.0.1 | ff_rdt_parse_header | Dereference of null pointer | 201 | FP | FP | 告警指向的代码行 `while (len >= 5 && buf[1] == 0xFF)` 是对指针 `buf` 的数组索引访问，而非解引用。切片代码显示 `buf` 是函数参数，且在该行之前没有对其赋值为 NULL 的操作，因此不存... |
| 1803 | ffmpeg-7.0.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 告警点位于 `if (info)` 条件块内部，已确保 `info` 指针非空。`info->key_ids[i]` 的访问受 `i < info->num_key_ids` 循环条件保护，且 `info->key_ids` 在循环后... |
| 1805 | ffmpeg-7.0.1 | build_table | Dereference of null pointer | 170 | FP | FP | 告警点位于循环内部，`table`指针在循环开始前已通过`table = &vlc->table[table_index];`正确初始化，且`j`的计算范围受`table_size`限制，不会越界。切片代码中未发现`table`为空的... |
| 1806 | ffmpeg-7.0.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用memcpy访问info->key_ids[j]之前，已通过av_encryption_init_info_alloc函数分配了内存，并且该函数内部对key_ids数组的每个元素都进行了检查，确保分配成功。此外，循... |
| 1808 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 168 | FP | FP | 告警点位于条件分支 `if (CONFIG_SWSCALE_ALPHA && hasAlpha)` 内部，该条件确保 `alpSrcPtr` 不为空时才执行解引用。切片代码显示 `alpSrcPtr` 在该分支前被初始化为 `NULL... |
| 1809 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的使用，但切片代码显示该宏最终展开为 UPDATE_CACHE_LE，其具体实现未在切片中提供。然而，在 FFmpeg 的上下文中，GET_VLC 宏及其相关位读取操作是经过充分验证的、用于解析变... |
| 1810 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在告警行使用 `in->linesize[plane]` 之前，`in` 指针作为函数参数传入且未被置空，并且在 `s->planeheight[plane] > 1` 的条件保护下才进行除法操作，因此不会发生对空指针的... |
| 1811 | ffmpeg-7.0.1 | mov_write_trak_tag | Dereference of null pointer | 3904 | FP | FP | 切片代码中，告警行 `is_clcp_track(track) && st->sample_aspect_ratio.num` 在调用 `st->sample_aspect_ratio.num` 前已通过 `if (st)` 检查 `... |
| 1812 | ffmpeg-7.0.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警点位于宏 UPDATE_CACHE 的展开处，该宏操作的是结构体指针 s 的成员。切片代码显示 s 作为函数参数传入，在函数内部被直接使用，没有对 s 进行空指针检查或赋值。然而，该函数是内联的位读取辅助函数，其正确使用依赖于调用... |
| 1814 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 291 | FP | FP | 告警指向的代码行 `sample[0][x] = src[x * pixel_stride + stride * y];` 是对数组元素的赋值，`src` 是函数入参指针，切片中未见其被赋值为 NULL 或存在导致其为 NULL 的逻... |
| 1815 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 686 | FP | FP | 切片代码显示，在警告行`q->decoded_bytes_buffer[i] = *ptr2--;`中，`ptr2`被赋值为`js_databuf + js_block_align - 1`，而`js_databuf`是`databu... |
| 1816 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 691 | FP | FP | 指针 `ptr1` 在循环 `for (i = 4; *ptr1 == 0xF8; i++, ptr1++)` 中被解引用前，已在切片代码中被明确初始化为 `q->decoded_bytes_buffer`，该缓冲区在之前的代码分支中... |
| 1818 | ffmpeg-6.1.1 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 告警指向的代码行`s->st->time_base.den`位于条件`s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->ic->nb_streams > 1`的保护块内，且其上层已存在对`s-... |
| 1821 | ffmpeg-6.1.1 | ebml_read_binary | Dereference of null pointer | 1087 | FP | FP | 在调用memset之前，已检查av_buffer_realloc的返回值，若成功（ret >= 0），则bin->buf及其data成员已被有效分配或重新分配，不会为NULL。切片代码中的逻辑保证了指针的有效性。 |
| 1819 | ffmpeg-6.1.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 412 | FP | FP | 切片代码显示，在访问 `ctx->buffers` 之前，存在条件判断 `if (ctx->buffers)` 和 `if (ctx->buffers[i].status == ...)`，这表明代码已对指针进行了空值检查。告警点 `... |
| 1822 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问`ptr[2*x]`和`ptr[2*x+1]`之前，`ptr2`已通过`av_malloc_array`分配内存，且循环条件`x < (w + 7 >> 3) * depth`确保了索引在分配范围内，不存在空指针解引用。 |
| 1823 | ffmpeg-6.1.1 | vc1_decode_intra_block | Dereference of null pointer | 964 | FP | FP | 在函数ff_vc1_pred_dc中，dc_val被明确赋值为s->dc_val[0] + s->block_index[n]（非空指针），然后通过*dc_val_ptr = &dc_val[0]传递给调用者。因此，在调用点*dc_v... |
| 1824 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 切片代码显示，在告警行`uint8_t *val = in->data[plane];`之前，`in`指针已作为函数参数传入且未被置空，且后续代码中`in->linesize[plane]`和`in->data[plane]`被多次安... |
| 1825 | ffmpeg-6.1.1 | unsharp_slice_16 | Dereference of null pointer | 141 | FP | FP | 切片代码显示，宏 `DEF_UNSHARP_SLICE_FUNC` 展开后，告警行 `{ NULL }` 是函数体的一部分，但该函数体在宏展开后已被完整的实现代码所替代。告警点处的 `{ NULL }` 并非实际执行的代码，而是宏定义... |
| 1826 | ffmpeg-6.1.1 | enc_open | Dereference of null pointer | 271 | FP | FP | 切片代码显示，在访问 `ost->ist->par->width` 和 `height` 之前，`ost->ist` 和 `ost->ist->par` 的指针有效性已通过 `set_encoder_id` 函数中的 `ost->en... |
| 1827 | ffmpeg-6.1.1 | ebml_parse | Dereference of null pointer | 1353 | FP | FP | 切片代码显示，在访问 `level->length` 之前，存在条件 `if (matroska->num_levels > 0)` 确保 `level` 指针非空。`level` 在函数开头被定义为 `matroska->num_l... |
| 1828 | ffmpeg-6.1.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警指向的宏`UPDATE_CACHE`展开后涉及对`gb`的访问，但切片中`gb`作为函数参数传入，且其调用方及有效性未知。然而，根据提供的宏定义，`UPDATE_CACHE`等宏操作的是与`gb`关联的局部变量（如`re_cach... |
| 1830 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码显示，在调用 `encode_line` 函数前，`sample` 数组的指针已通过 `s->sample_buffer` 的有效内存区域进行赋值，且 `s->sample_buffer` 已在函数开头通过 `memset` ... |
| 1833 | ffmpeg-6.1.1 | safe_filename | Dereference of null pointer | 97 | FP | FP | 代码逻辑确保了指针 `f` 在解引用前已通过循环条件 `*f` 进行了非空检查，不会发生空指针解引用。 |
| 1831 | ffmpeg-6.1.1 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 告警点位于对`s->st`指针的解引用，但切片代码显示，在调用`av_packet_new_side_data`后，若其返回NULL，函数会直接返回错误码，不会执行到告警行。因此，告警行执行时`s->st`必然非空，解引用是安全的。 |
| 1836 | ffmpeg-6.1.1 | ff_encode_encode_cb | Dereference of null pointer | 285 | FP | FP | 切片代码显示，在访问 `frame->duration` 之前，已经存在条件 `if (frame && (codec->caps_internal & FF_CODEC_CAP_EOF_FLUSH))` 或 `if (!(avctx... |
| 1835 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，在告警行访问 `in->linesize[plane]` 之前，`in` 指针作为函数参数传入且未被置空，并且在后续逻辑中被多处使用，表明其非空。此外，`out` 指针在 `ff_get_video_buffer` 调用... |
| 1832 | ffmpeg-6.1.1 | ebml_read_sint | Dereference of null pointer | 1014 | FP | FP | 切片代码显示，在调用`avio_r8(pb)`前未对指针`pb`进行空值检查，但被调用的`avio_r8`函数内部已包含对`s`（即`pb`）的成员访问检查，若`s`为空指针，则访问`s->buf_ptr`将导致解引用空指针。然而，该... |
| 1839 | ffmpeg-6.1.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1476 | FP | FP | 切片代码显示，在访问 `scale_matrix[pos]` 之前，已通过条件 `if (s->ps.sps->scaling_list_enable_flag && !(transform_skip_flag && log2_tra... |
| 1843 | ffmpeg-6.1.1 | concat_parse_script | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `file->user_duration` 之前，`file` 指针已在 `DIR_FILE` 分支通过 `add_file` 函数成功初始化并赋值，且 `DIR_DURATION` 分支仅在 `(dir->fl... |
| 1844 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 297 | FP | FP | 切片代码显示，告警行 `sample[0][x] = ((uint16_t*)(src + stride*y))[x];` 中 `src` 是函数参数，`stride` 和 `y` 是局部变量，不存在对空指针的解引用。指针运算和数组访... |
| 1841 | ffmpeg-6.1.1 | hls_read_header | Dereference of null pointer | 2123 | FP | FP | 切片代码显示，在访问 `in_fmt->name` 之前，`in_fmt` 已在 `av_demuxer_iterate` 循环中被赋值，或通过 `av_probe_input_buffer` 成功返回。告警点位于 `if (strs... |
| 1847 | ffmpeg-6.1.1 | id3v2_parse | Dereference of null pointer | 1054 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 获取的，该函数返回一个有效的函数指针或 NULL。调用点位于 `extra_func` 被... |
| 1846 | ffmpeg-6.1.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在访问 `dp1[pos]` 和 `dp2[pos]` 之前，存在条件 `if (dpd[pos])` 进行保护，确保只有在 `dpd[pos]` 非零时才进行解引用。`dpd` 是 `dst[pd]` 的别名，而 `d... |
| 1848 | ffmpeg-6.1.1 | choose_rct_params | Dereference of null pointer | 983 | FP | FP | 切片代码显示，在访问 src[1] 和 src[2] 之前，代码处于 `lbd` 为 false 的 else 分支，这表明 src 数组的三个元素（src[0], src[1], src[2]）在此上下文中都被假定为非空。告警点位于... |
| 1850 | ffmpeg-6.1.1 | ebml_read_ascii | Dereference of null pointer | 1069 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，因此对 `*str` 的解引用不会实际发生，不存在空指针解引用风险。 |
| 1849 | ffmpeg-6.1.1 | split_commandline | Dereference of null pointer | 731 | FP | FP | 告警点位于检查字符串是否为双破折号'--'的逻辑，切片代码显示在解引用`opt[1]`和`opt[2]`之前，已通过`opt[0] == '-'`和`opt[1] == '-'`进行了非空验证，且`opt`来源于`argv`数组，在循... |
| 1851 | ffmpeg-6.1.1 | output_packet | Dereference of null pointer | 1102 | FP | FP | 切片代码显示，在访问 `timestamp_packet->unwritten_size` 之前，`timestamp_packet` 被赋值为 `stream->premux_packet`。`stream->premux_pack... |
| 1854 | ffmpeg-6.1.1 | ost_add | Dereference of null pointer | 1456 | FP | FP | 切片代码中，变量 `ist` 在条件 `if (ost->ist && ost->ist->st->duration > 0)` 之前已被检查为非空，且 `ms->stream_duration = ist->st->duration... |
| 1853 | ffmpeg-6.1.1 | concat_parse_script | Dereference of null pointer | 561 | FP | FP | 切片代码显示，在访问`file->inpoint`之前，`file`指针已在`DIR_FILE`分支通过`add_file`函数成功赋值，且该分支有错误检查。此外，`DIR_INPOINT`分支仅在`(dir->flags & NEE... |
| 1855 | ffmpeg-6.1.1 | sb_decode | Dereference of null pointer | 1346 | FP | FP | 在访问 innov_save 指针前，代码已通过条件 'if (st->innov_save)' 检查其非空，确保了指针的有效性。因此，后续的数组索引操作 'innov_save[2 * i] = exc[i]' 是安全的，不会发生空... |
| 1857 | ffmpeg-6.1.1 | check_header_mismatch | Dereference of null pointer | 520 | FP | FP | 切片代码显示，在访问 `header->link_penalty[i]` 之前，`i` 的值由 `for` 循环控制，且循环条件 `i < FLAC_MAX_SEQUENTIAL_HEADERS && curr != child` 确... |
| 1856 | ffmpeg-6.1.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警行 `if ((*child)->state * 2 == -t->state)` 位于 `if (t->state)` 和 `if (!(t->state & 1))` 条件块内，且前有 `if ((*child)->state... |
| 1860 | ffmpeg-6.1.1 | mpegts_open_filter | Dereference of null pointer | 493 | FP | FP | 告警指向的 `av_log` 调用被宏定义为 `while(0)`，这是一个空操作，不会发生对空指针的解引用。切片代码中 `ts->stream` 的值虽未知，但宏展开确保了该行代码无实际执行效果，因此是误报。 |
| 1862 | ffmpeg-6.1.1 | fg_output_frame | Dereference of null pointer | 2111 | FP | FP | 告警行代码为三元运算符的条件表达式部分，仅用于计算赋值，不涉及对指针的显式解引用操作。切片代码中未发现对空指针的直接解引用，且该行逻辑是安全的赋值计算。 |
| 1861 | ffmpeg-6.1.1 | guess_mv | Dereference of null pointer | 428 | FP | FP | 切片代码显示，在告警行访问 `s->last_pic.f->data[0]` 之前，已通过 `if (s->last_pic.f && s->last_pic.f->data[0])` 检查了指针非空，确保了访问的安全性，因此是误报。 |
| 1863 | ffmpeg-6.1.1 | build_table | Dereference of null pointer | 204 | FP | FP | 告警行`table[j].len = -subtable_bits;`中的`table`指针在切片代码中已通过`table = &vlc->table[table_index];`正确初始化，且`table_index`的有效性已在前... |
| 1864 | ffmpeg-6.1.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警位于第93行 'AVChapter *chp = chapters[i];'，但切片代码显示，包含该行的 for 循环仅在 'if (chapters && nb_chapters)' 条件为真时才执行，这确保了 chapters... |
| 1866 | ffmpeg-6.1.1 | guess_status_pts | Dereference of null pointer | 462 | FP | FP | 切片代码显示告警行访问的是结构体成员 `status_out`，而非对指针 `ctx->inputs[i]` 本身进行解引用。循环条件 `i < ctx->nb_inputs` 确保了索引有效，且 `ctx->inputs` 是一个指... |
| 1867 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警点位于宏展开内部，其`val`变量已通过`in->data[plane]`赋值，`in`指针在函数入口非空且被使用，切片中无证据表明`in->data[plane]`为空。宏内对`val`数组的访问是安全的，属于工具误判。 |
| 1869 | ffmpeg-6.1.1 | av_dump_format | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `printed` 数组前，已通过 `if (ic->nb_streams && !printed) return;` 确保了当 `printed` 为 NULL 时函数会提前返回，因此后续的 `printed[... |
| 1868 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 332 | FP | FP | 告警点位于条件语句 `if (s->do_video)` 内部，该条件确保 `outlink` 不为 NULL 时才会执行 `av_rescale_q` 调用。切片代码显示 `outlink` 在 `s->do_video` 为真时被... |
| 1870 | ffmpeg-6.1.1 | check_header_mismatch | Dereference of null pointer | 476 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 之前，`curr` 变量通过 `curr = curr->next;` 在 while 循环中遍历链表，且循环条件 `curr != child` 确保了 `cur... |
| 1871 | ffmpeg-6.1.1 | update_context_from_thread | Dereference of null pointer | 366 | FP | FP | 告警点位于条件 `if (hwaccel->priv_data_size)` 内，该条件检查 `priv_data_size` 是否非零。切片中 `hwaccel` 指针来源于 `ffhwaccel(src->hwaccel)`，且其... |
| 1872 | ffmpeg-6.1.1 | choose_rct_params | Dereference of null pointer | 984 | FP | FP | 告警点位于对指针 `src[2]` 的间接引用，但切片代码显示 `src` 是函数参数，且在同一分支中 `src[0]` 和 `src[1]` 也被类似使用。代码逻辑表明 `src` 数组在 `lbd` 为假时被正常访问，没有证据表明... |
| 1873 | ffmpeg-6.1.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 告警点位于宏 UPDATE_CACHE_32 的展开处，该宏最终会解引用 GetBitContext 指针 's'。切片代码显示 's' 是函数参数，在调用前已通过 av_assert2 进行断言，且函数内所有宏调用均以 's' 为参... |
| 1874 | ffmpeg-6.1.1 | activate | Dereference of null pointer | 186 | FP | FP | 告警点位于 `frame->pts = s->pts;`，但在此行执行前，`frame` 指针已在多个分支中被明确赋值（通过 `ff_get_video_buffer` 或 `av_frame_clone`），且每个赋值点都有空指针检... |
| 1875 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 199 | FP | FP | 切片代码显示，在访问 ptr2[x] 之前，ptr2 已通过 av_malloc_array 分配内存，且分配失败时函数会提前返回。在后续使用 ptr2 的循环中，其访问范围受 (w + 7 >> 3) * depth 限制，该值小于... |
| 1877 | ffmpeg-6.1.1 | ff_encode_encode_cb | Dereference of null pointer | 282 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，对 `frame->pts` 的访问受外层 `if (frame && ...)` 保护。切片代码显示，当 `frame` 为 NULL... |
| 1876 | ffmpeg-6.1.1 | h264_field_start | Dereference of null pointer | 1426 | FP | FP | 切片代码显示`sps`指针在解引用前已通过`h264_init_ps`函数初始化，且该函数返回成功（`ret < 0`时已提前返回），因此`sps`非空。工具误判了数据流，导致虚假的空指针解引用告警。 |
| 1878 | ffmpeg-6.1.1 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，代码已通过 `if (!buf) { ... }` 检查了 `buf` 是否为 NULL，并确保在 `buf` 为 NULL 时... |
| 1880 | ffmpeg-6.1.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1442 | FP | FP | 告警点位于switch-case分支内，该分支仅在link->type为AVMEDIA_TYPE_AUDIO时执行。切片代码显示，函数入口处已对输入指针*rframe解引用并赋值给frame，且在此之前调用了av_frame_is_w... |
| 1882 | ffmpeg-6.1.1 | asf_parse_packet | Dereference of null pointer | 1306 | FP | FP | 切片代码中，在访问 asf_st->pkt.data[i] 之前，已通过条件 'asf_st->pkt.size > 100' 确保数据包大小足够，且循环访问是在有效大小范围内进行的。此外，asf_st->pkt.data 在之前已通... |
| 1879 | ffmpeg-6.1.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已通过条件 `if (s->peak[i][j] && ...)` 确保 `s->peak[i][j]` 为真，而 `s->peak[i][j]` 仅在循环前段 `if (dpd[po... |
| 1881 | ffmpeg-6.1.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 切片代码显示`s->buffer`被直接索引访问，但未提供`s`或`s->buffer`的初始化或空值检查上下文。然而，`get_bits1`是一个内联辅助函数，其调用方（未在切片中）应确保传入有效的`GetBitContext`指针... |
| 1883 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 148 | FP | FP | 告警行 `*(const void**)&alpMmxFilter[s*i] = alpSrcPtr[i];` 中，`alpSrcPtr` 在切片代码中已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)... |
| 1885 | ffmpeg-6.1.1 | avc_parse_nal_units | Dereference of null pointer | 92 | FP | FP | 告警指向的代码行 `list->nb_nalus >= nalu_limit` 是对 `list->nb_nalus` 的读取操作，而非解引用。切片代码显示 `list` 参数非空，且在该行之前 `list` 已被安全使用（如访问 `... |
| 1884 | ffmpeg-6.1.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 告警点位于条件语句 `if (dpd[pos])` 内部，这表明对指针 `dpd` 的解引用发生在已确认该指针非空之后。切片代码显示 `dpd` 是 `dst` 数组的一个元素，而外层循环 `for (k = 0; k < 4 && ... |
| 1888 | ffmpeg-6.1.1 | ebml_parse | Dereference of null pointer | 1370 | FP | FP | 切片代码显示，在访问 `level->length` 之前，已通过 `if (matroska->num_levels > 0)` 检查确保 `level` 指针非空。因此，对 `level` 的访问是安全的，不存在空指针解引用。 |
| 1887 | ffmpeg-6.1.1 | mov_write_trak_tag | Dereference of null pointer | 3818 | FP | FP | 告警指向的代码行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 中，`st` 是函数参数，在切片代码中已通过调用链（如 `mov_write_tkhd_... |
| 1889 | ffmpeg-6.1.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码显示，对指针 `dpd` 的访问均发生在对其有效性进行明确检查之后（如 `if (dpd[pos] && ...)`），且 `dpd` 被赋值为 `out->data[...]`，而 `out` 作为函数参数，在调用上下文中应... |
| 1893 | ffmpeg-6.1.1 | ff_rdt_parse_header | Dereference of null pointer | 200 | FP | FP | 告警指向的代码行 `while (len >= 5 && buf[1] == 0xFF)` 是对指针 `buf` 的读取操作，而非解引用。切片代码显示 `buf` 是函数参数，在 `init_get_bits` 函数中有明确的空指针检... |
| 1892 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 682 | FP | FP | 告警指向的FFSWAP宏调用位于条件分支`if (js_databuf == q->decoded_bytes_buffer)`内部，该宏仅交换两个已知局部指针`ptr1`和`ptr2`指向的值，不会对空指针进行解引用。切片代码显示`... |
| 1894 | ffmpeg-6.1.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 告警点位于 `if (info) {` 条件块内部，且 `info->key_ids[i]` 的访问受 `i < info->num_key_ids` 循环条件保护。切片代码显示 `info` 已非空，且 `key_ids` 数组的索... |
| 1896 | ffmpeg-6.1.1 | build_table | Dereference of null pointer | 170 | FP | FP | 告警点位于循环内部，访问 `table[j]` 前，`j` 的值由 `code` 右移计算或经 `bitswap_32` 转换得到，其范围受 `table_nb_bits` 控制，且 `table` 指针指向通过 `alloc_tab... |
| 1898 | ffmpeg-6.1.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], side_data, key_id_size)` 之前，`info->key_ids` 数组及其每个元素 `info->key_ids[j]` 已在 `av_e... |
| 1899 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 168 | FP | FP | alpSrcPtr 的赋值受条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 保护，当条件不满足时其值为 NULL，但后续使用该指针的代码 `*(const void**)&alpMmxFilter[4*... |
| 1902 | ffmpeg-6.1.1 | mov_write_trak_tag | Dereference of null pointer | 3823 | FP | FP | 告警指向的代码行 `is_clcp_track(track) && st->sample_aspect_ratio.num` 中，`st` 是函数参数，在切片中可见其被多处使用且未被置空，没有证据表明它是空指针。静态分析工具可能误判了... |
| 1900 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警位于宏 UPDATE_CACHE 的调用处，该宏最终展开为 UPDATE_CACHE_LE。切片代码中未显示该宏的具体实现，但根据上下文，它是对 GetBitContext 结构体指针 's' 的操作。函数 get_vlc2 的调... |
| 1903 | ffmpeg-6.1.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警位于宏 UPDATE_CACHE 的展开处，该宏操作的是指针 s，但函数 get_bits 是静态内联函数，其指针参数 s 由调用方传入。在切片代码中，没有证据表明 s 为 NULL，且函数内部逻辑是常规的位读取操作。工具可能因宏... |
| 1901 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在计算 `linesize` 时存在条件判断 `s->planeheight[plane] > 1`，当条件不满足时 `linesize` 被赋值为 0。后续在宏 `CHECK_BIT` 中使用 `linesize` 进... |
| 1905 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 291 | FP | FP | 告警指向的代码行 `sample[0][x] = src[x * pixel_stride + stride * y];` 是对数组元素的赋值，`src` 是函数参数，`sample[0]` 指向已分配内存的 `s->sample_b... |
| 1907 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 691 | FP | FP | 切片代码显示，在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确赋值为 `q->decoded_bytes_buffer`，这是一个有效的数组指针，不可能为 NUL... |
| 1904 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 471 | FP | FP | 告警点位于宏 `DECODE_CODEWORD` 内部，该宏展开后包含 `UPDATE_CACHE` 和 `GET_CACHE` 操作，这些操作从 `GetBitContext *gb` 中读取比特流。`gb` 指针在函数参数中传入，... |
| 1906 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 686 | FP | FP | 告警指向的代码行 `q->decoded_bytes_buffer[i] = *ptr2--;` 中，`ptr2` 被初始化为 `js_databuf + js_block_align - 1`，而 `js_databuf` 是传入的... |
| 1909 | ffmpeg-7.1 | finalize_packet | Dereference of null pointer | 678 | FP | FP | 告警指向的代码行`s->st->time_base.den`在调用前已通过条件`s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->ic->nb_streams > 1`和`s->st`的隐式存... |
| 1910 | ffmpeg-7.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 413 | FP | FP | 切片代码显示，在访问 `ctx->buffers[buf.index]` 之前，`buf.index` 来自 `ioctl(VIDIOC_DQBUF)` 系统调用，该调用由内核填充，应保证其值在有效范围内。此外，`ctx->buffe... |
| 1911 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 299 | FP | FP | 切片代码显示，在指针解引用前，`src` 作为函数参数传入，其值由调用方决定。在告警所在行，`src` 被用于计算地址并与 `stride*y` 偏移量相加，这是访问数组元素的常规模式，没有证据表明该指针为 null 或计算出的地址无... |
| 1914 | ffmpeg-7.1 | <global> | Dereference of null pointer | 209 | FP | FP | 切片代码显示，在访问`ptr2[x]`之前，`ptr2`已在条件分支`if (maplength && depth < 8)`中被`av_malloc_array`分配内存，且后续循环条件`x < (w + 7 >> 3) * dep... |
| 1913 | ffmpeg-7.1 | ebml_read_binary | Dereference of null pointer | 1095 | FP | FP | 告警行 `memset(bin->buf->data + length, 0, AV_INPUT_BUFFER_PADDING_SIZE);` 仅在 `av_buffer_realloc` 成功（`ret >= 0`）后执行，而 `a... |
| 1916 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 切片代码显示，在访问 `in->data[plane]` 之前，`in` 指针作为函数参数传入且未被修改，且函数逻辑表明 `in` 是有效的输入帧。告警点位于对有效指针的访问，不存在空指针解引用。 |
| 1917 | ffmpeg-7.1 | unsharp_slice_16 | Dereference of null pointer | 172 | FP | FP | 切片代码显示，宏展开后的函数中，指针 `sc` 和 `sr` 均从传入的 `ThreadData *td` 结构体中获取，且 `sc` 在循环中被 `memset` 使用，表明其已被赋值且非空。告警点 `{ NULL }` 是宏定义的... |
| 1918 | ffmpeg-7.1 | ebml_parse | Dereference of null pointer | 1363 | FP | FP | 切片代码显示，在访问 `level->length` 之前，已通过 `if (matroska->num_levels > 0)` 检查确保 `level` 指针非空。因此，对 `level` 的访问是安全的，不存在空指针解引用。 |
| 1919 | ffmpeg-7.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警位于宏 UPDATE_CACHE 的调用处，该宏展开后不直接涉及指针解引用。切片代码中未发现对空指针的显式解引用操作，且关键宏 BITS_AVAILABLE 被定义为常量 1，表明该代码路径可能被简化或用于特定配置，不构成实际的空... |
| 1921 | ffmpeg-7.1 | rtp_set_prft | Dereference of null pointer | 646 | FP | FP | 切片代码显示，在调用av_rescale_q之前，已对av_packet_new_side_data的返回值prft进行了空指针检查，若为空则直接返回错误。因此，后续使用s->st->time_base时，程序已处于prft非空的执行... |
| 1922 | ffmpeg-7.1 | ebml_read_sint | Dereference of null pointer | 1022 | FP | FP | 切片代码显示，在调用 avio_r8 前未检查指针 pb 是否为 NULL，但 avio_r8 函数内部会检查其参数 s 的缓冲区指针，并在缓冲区耗尽时返回 0，这避免了空指针解引用。此外，sign_extend 函数处理的是整数值，... |
| 1923 | ffmpeg-7.1 | safe_filename | Dereference of null pointer | 98 | FP | FP | 代码逻辑确保了指针 `f` 在解引用前已通过循环条件 `*f` 进行了非空检查，且函数参数 `f` 在切片中作为输入，其解引用操作发生在明确的非空判断之后，不存在空指针解引用风险。 |
| 1926 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，在访问 `in->linesize[plane]` 之前，已通过条件 `s->planeheight[plane] > 1` 进行检查。当 `planeheight` 不大于1时，`linesize` 被赋值为0，不会解... |
| 1925 | ffmpeg-7.1 | dump_stream_group | Dereference of null pointer | 788 | FP | FP | 切片代码显示，在访问 `stg->streams[i]` 之前，已通过条件 `if (avctx && stg->nb_streams && ...)` 检查了 `stg->nb_streams` 大于0，且循环 `for (int ... |
| 1927 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 236 | FP | FP | 告警点位于av_assert0宏内部，该宏用于开发调试，在条件不满足时会调用abort()终止程序。这属于防御性编程断言，并非运行时可能发生的空指针解引用逻辑错误。 |
| 1928 | ffmpeg-7.1 | ff_encode_encode_cb | Dereference of null pointer | 275 | FP | FP | 切片代码显示，在访问 `frame->duration` 之前，已经存在条件 `if (frame && (codec->caps_internal & FF_CODEC_CAP_EOF_FLUSH))` 或 `if (frame)`... |
| 1929 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 219 | FP | FP | 告警指向的代码行位于 av_assert0 宏内部，该宏用于开发调试，在条件不满足时会调用 abort() 终止程序，不会导致空指针解引用。切片代码显示该断言检查了 frame 指针非空或编码器类型非音视频，逻辑上用于确保前置条件，并... |
| 1934 | ffmpeg-7.1 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 切片代码显示，在访问 `file->user_duration` 之前，`file` 指针已在 `DIR_FILE` 分支通过 `add_file` 函数成功初始化并赋值，且该分支执行失败时会通过 `goto fail` 跳转，确保了... |
| 1933 | ffmpeg-7.1 | hls_append_segment | Dereference of null pointer | 1183 | FP | FP | 告警点位于条件判断 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)`，但切片代码显示，在进入该分支前，`en` 已被赋值为 `v... |
| 1936 | ffmpeg-7.1 | kalman_smoothen | Dereference of null pointer | 585 | FP | FP | 在切片代码中，`best_hist_ptr` 在循环中被赋值，且仅在 `optimal_gain > 0` 和 `dot > 0` 的条件下才会被后续使用。当 `optimal_gain <= 0` 或 `dot <= 0` 时函数提... |
| 1937 | ffmpeg-7.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 告警点位于条件语句 `if (dpd[pos])` 内部，该条件确保了对 `dpd[pos]` 的访问仅在指针非空时执行。切片代码显示 `dpd` 指向 `dst[pd]`，而 `dst` 来自 `out->data`，在函数开头有循... |
| 1938 | ffmpeg-7.1 | id3v2_parse | Dereference of null pointer | 1055 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 获取的，该函数仅在找到匹配的tag时才返回非空指针。因此，当执行到该行时，`extra_f... |
| 1940 | ffmpeg-7.1 | split_commandline | Dereference of null pointer | 809 | FP | FP | 切片代码显示，在调用 `find_option` 后，对返回的指针 `po` 的访问（`po->name`）位于 `if (po->name)` 条件判断之后。`find_option` 函数保证始终返回一个有效的 `OptionDe... |
| 1939 | ffmpeg-7.1 | set_bframe_chain_length | Dereference of null pointer | 1590 | FP | FP | 在告警行`s->input_picture[i - 1]->f->data[0]`处，切片代码显示其位于`s->b_frame_strategy == 1`的条件分支内，且外层有`if (s->input_picture[i] && ... |
| 1941 | ffmpeg-7.1 | ebml_read_ascii | Dereference of null pointer | 1077 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 1943 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 286 | FP | FP | 告警点位于 `enc_ctx->width = ost->ist->par->width;`，但切片代码显示该赋值仅在 `enc_ctx->codec_type == AVMEDIA_TYPE_SUBTITLE` 且 `!enc_ct... |
| 1945 | ffmpeg-7.1 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 告警点位于DIR_INPOINT分支，该分支仅在解析到'inpoint'指令时执行。切片代码显示，该分支执行前有严格的标志检查（NEEDS_FILE），确保cat->nb_files > 0，且file变量已在DIR_FILE分支通过... |
| 1946 | ffmpeg-7.1 | sb_decode | Dereference of null pointer | 1348 | FP | FP | 告警点位于 `if (st->innov_save)` 条件块内，切片代码显示 `innov_save` 在该条件块前已被明确赋值为 `st->innov_save + 2 * offset`，且 `st->innov_save` 在... |
| 1948 | ffmpeg-7.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警行位于条件判断 `if ((*child)->state * 2 == -t->state)` 内部，该条件已确保 `*child` 非空（因为 `child` 指向 `t->child[i]`，且外层 `if (t->state... |
| 1950 | ffmpeg-7.1 | get_pict_type | Dereference of null pointer | 136 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效范围，这确保了 `unit->conte... |
| 1949 | ffmpeg-7.1 | check_header_mismatch | Dereference of null pointer | 519 | FP | FP | 告警指向的代码行 `curr = curr->next;` 位于一个受循环条件 `i < FLAC_MAX_SEQUENTIAL_HEADERS && curr != child` 严格保护的循环体内。切片代码显示，在循环体之后紧跟着... |
| 1952 | ffmpeg-7.1 | mpegts_open_filter | Dereference of null pointer | 495 | FP | FP | 告警指向的 `av_log` 调用行已被宏定义为空操作 `while(0)`，不会发生空指针解引用。切片中 `ts->stream` 的值虽未知，但宏展开确保了该表达式不会被执行，因此告警为误报。 |
| 1953 | ffmpeg-7.1 | guess_mv | Dereference of null pointer | 432 | FP | FP | 切片代码显示，在警告行访问 `s->last_pic.f->data[0]` 之前，已存在条件 `if (s->last_pic.f && s->last_pic.f->data[0])` 进行空指针检查，确保了指针的有效性。因此，该... |
| 1955 | ffmpeg-7.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警点位于循环内部，该循环的条件为 `if (chapters && nb_chapters)` 和 `for (int i = 0; i < nb_chapters; i++)`，已确保 `chapters` 非空且 `i` 在有效... |
| 1954 | ffmpeg-7.1 | build_table | Dereference of null pointer | 204 | FP | FP | 告警点位于 `table[j].len = -subtable_bits;`，其中 `table` 指针由 `table = &vlc->table[table_index];` 初始化，而 `table_index` 来自 `all... |
| 1957 | ffmpeg-7.1 | <global> | Dereference of null pointer | 78 | FP | FP | 告警点位于宏 UPDATE_CACHE 的展开处，该宏展开为 UPDATE_CACHE_LE，其定义未在切片中提供。但根据上下文，该函数是标准解码函数，其参数 gb 在调用前应已正确初始化。切片中未显示 gb 为 null 的证据，且... |
| 1958 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警指向的代码行 `uint16_t *val = (uint16_t *)in->data[plane];` 中，`in` 指针已在函数入口处作为参数传入，且切片内未显示其为空。在 `s->depth <= 8` 的分支中也直接使用... |
| 1960 | ffmpeg-7.1 | av_dump_format | Dereference of null pointer | 898 | FP | FP | 切片代码显示，在访问 printed 数组前，已通过条件 'if (ic->nb_streams && !printed) return;' 确保 printed 非空。后续访问 printed[program->stream_ind... |
| 1961 | ffmpeg-7.1 | check_header_mismatch | Dereference of null pointer | 475 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 之前，`curr` 变量通过 `curr = curr->next;` 在 while 循环中迭代，且循环条件 `curr != child` 确保了 `curr`... |
| 1962 | ffmpeg-7.1 | update_context_from_thread | Dereference of null pointer | 438 | FP | FP | 切片代码显示，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 条件确保 `hwaccel` 指针... |
| 1963 | ffmpeg-7.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 告警点位于宏 UPDATE_CACHE_32 的展开处，该宏用于位读取器操作。切片代码显示，在调用 UPDATE_CACHE_32 之前，已通过 OPEN_READER 宏初始化了读取器，并且传入的 GetBitContext 指针 ... |
| 1966 | ffmpeg-7.1 | check_available | Dereference of null pointer | 616 | FP | FP | 切片代码显示，在访问 `TAB_MVF(n->x, n->y).pred_flag` 之前，已通过 `is_available(fc, n->x, n->y)` 检查了坐标的有效性，这确保了 `tab_mvf` 数组访问不会越界或导致... |
| 1965 | ffmpeg-7.1 | <global> | Dereference of null pointer | 200 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被 `av_malloc_array` 分配内存，且分配失败时函数已提前返回。在告警所在循环中，... |
| 1967 | ffmpeg-7.1 | ff_encode_encode_cb | Dereference of null pointer | 272 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，该行代码 `avpkt->pts = frame->pts;` 仅在 `frame` 指针非空时才会执行。切片代码显示，外层条件 `if... |
| 1968 | ffmpeg-7.1 | rtp_parse_one_packet | Dereference of null pointer | 888 | FP | FP | 切片代码显示，在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，函数开头已通过 `if (!buf) { ... }` 和 `if (len < 12) return -1;` ... |
| 1969 | ffmpeg-7.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已通过条件 `if (dpd[pos])` 和 `if (s->peak[i][j] && ...)` 进行了检查，确保了指针 `dpd` 指向的缓冲区有效且访问位置 `pos` 在边... |
| 1972 | ffmpeg-7.1 | nal_parse_units | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `list->nalus` 之前，已通过 `if (!tmp)` 检查了 `av_fast_realloc` 的返回值，若分配失败会提前返回错误。因此，在后续 `tmp[list->nb_nalus++]` 中使... |
| 1971 | ffmpeg-7.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1420 | FP | FP | 切片代码显示，在访问 `scale_matrix[pos]` 之前，存在条件 `if (sps->scaling_list_enabled && !(transform_skip_flag && log2_trafo_size > 2... |
| 1973 | ffmpeg-7.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1513 | FP | FP | 告警点位于switch-case分支内，该行代码仅在`link->type == AVMEDIA_TYPE_AUDIO`且`frame`非空时才会执行。函数开头已对`frame`（即`*rframe`）进行了`av_frame_is_... |
| 1974 | ffmpeg-7.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 切片代码显示`s->buffer`是一个数组访问，`s`和`s->buffer`的指针有效性依赖于调用者传入的上下文。在典型的比特流读取器中，`GetBitContext`结构会在初始化时确保`buffer`指向有效内存，且`inde... |
| 1975 | ffmpeg-7.1 | asf_parse_packet | Dereference of null pointer | 1307 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data[i]` 之前，已通过 `av_assert0(asf_st)` 确保 `asf_st` 非空，且 `asf_st->pkt.data` 在循环前已通过 `av_new_packe... |
| 1976 | ffmpeg-7.1 | <global> | Dereference of null pointer | 146 | FP | FP | 告警行代码 `*(const void**)&alpMmxFilter[s*i] = alpSrcPtr[i];` 位于 `if (CONFIG_SWSCALE_ALPHA && hasAlpha)` 条件块内，切片代码显示 `alp... |
| 1977 | ffmpeg-7.1 | choose_rct_params | Dereference of null pointer | 991 | FP | FP | 切片代码显示，在 `lbd` 为假的分支中，对 `src[0]`、`src[1]`、`src[2]` 进行了指针解引用。告警点位于 `src[2]` 的解引用。这些 `src` 指针作为函数参数传入，在切片内没有显式赋值为 NULL ... |
| 1980 | ffmpeg-7.1 | mov_write_trak_tag | Dereference of null pointer | 4187 | FP | FP | 告警指向的代码行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 中，`st` 是函数参数，在切片代码中已通过调用链（如 `mov_write_tkhd_... |
| 1981 | ffmpeg-7.1 | ebml_parse | Dereference of null pointer | 1380 | FP | FP | 切片代码显示，在告警行（第1380行）访问`level`指针前，已通过`if (matroska->num_levels > 0)`检查确保`level`非空。该条件分支仅在`level`有效时才会进入，因此不会发生空指针解引用。 |
| 1979 | ffmpeg-7.1 | unsharp_slice_8 | Dereference of null pointer | 173 | FP | FP | 切片代码显示，在宏展开的函数中，`sc` 和 `sr` 指针在循环 `memset` 调用前已从 `fp` 结构体获取，且 `fp` 来自传入的 `arg`（ThreadData）。虽然切片未显示 `fp->sc` 和 `fp->sr... |
| 1982 | ffmpeg-7.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码显示，在访问 `dpd[pos - 1]`、`dpd[pos + 1]`、`dpd[poa]`、`dpd[pob]` 等指针偏移位置前，已通过条件 `(!j ｜｜ ...)`、`(j == (out->width - 1) ｜... |
| 1985 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 683 | FP | FP | 告警指向的FFSWAP宏操作的是已定义的局部变量`ptr1`和`ptr2`，切片代码显示`ptr1`在条件分支内被赋值，`ptr2`是循环内的局部变量，两者均非空指针，因此不存在空指针解引用。 |
| 1986 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 303 | FP | FP | 告警指向的代码行是对一个已知非空指针 `src` 进行类型转换和数组索引访问，切片代码显示 `src` 是函数参数且已在循环中被安全使用，没有证据表明其为空指针。 |
| 1987 | ffmpeg-7.1 | ff_rdt_parse_header | Dereference of null pointer | 202 | FP | FP | 告警指向的代码行是 while 循环的条件判断，其中 `buf` 是函数参数，在循环内被安全地递增和边界检查。切片中未发现 `buf` 为 NULL 的路径，且 `init_get_bits` 函数内部已对 NULL 缓冲区进行了处理... |
| 1988 | ffmpeg-7.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 告警点位于 `if (info)` 条件块内部，已确保 `info` 非空。循环条件 `i < info->num_key_ids` 使用 `info` 的成员，但 `info` 已通过前置检查，因此对 `info->key_ids[... |
| 1990 | ffmpeg-7.1 | build_table | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `table[j].len` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 初始化，且 `table_index` 的有效性已通过 `if (table... |
| 1991 | ffmpeg-7.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], side_data, key_id_size);` 之前，`info->key_ids` 数组及其每个元素 `info->key_ids[j]` 已在 `av_... |
| 1992 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 293 | FP | FP | 告警指向的代码行 `sample[0][x] = src[x * pixel_stride + stride * y];` 是对数组元素的赋值，`src` 是函数入参指针，切片中未见其被赋值为 NULL 或存在导致其为 NULL 的逻... |
| 1996 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在`linesize`被使用前，已通过条件`s->planeheight[plane] > 1`进行保护。当条件不满足时，`linesize`被显式赋值为0，避免了空指针解引用。 |
| 1994 | ffmpeg-7.1 | <global> | Dereference of null pointer | 166 | FP | FP | alpSrcPtr 的赋值在切片代码中受条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 保护，当条件不满足时其值为 NULL，但告警所在行 `*(const void**)&alpMmxFilter[4... |
| 1995 | ffmpeg-7.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该宏最终展开为 UPDATE_CACHE_LE，其具体实现未在切片中提供。然而，该函数是FFmpeg中广泛使用的、经过验证的比特流读取辅助函数，其内部指针操作（如对gb的访问... |
| 1997 | ffmpeg-7.1 | set_bframe_chain_length | Dereference of null pointer | 1605 | FP | FP | 在循环 `for (i = 0; i < b_frames + 1; i++)` 中，`b_frames` 的值由 `FFMAX(0, i - 1)` 计算得出，其中 `i` 是前一个循环的终止索引，该循环确保 `i` 至少为 0，因... |
| 1999 | ffmpeg-7.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后仅对结构体指针 s 的成员进行操作，并未直接解引用指针 s 本身。函数 get_bits 的调用者需确保传入的 GetBitContext *s 指针有效，这是函数使用的前提... |
| 1998 | ffmpeg-7.1 | mov_write_trak_tag | Dereference of null pointer | 4192 | FP | FP | 切片代码中，告警行 `is_clcp_track(track) && st->sample_aspect_ratio.num` 在调用 `st->sample_aspect_ratio.num` 前已通过 `if (st)` 检查了 ... |
| 2002 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在解引用指针 `ptr1` 之前，它已被明确初始化为指向 `q->decoded_bytes_buffer`，这是一个有效的缓冲区。循环条件 `*ptr1 == 0xF8` 是读取操作，而非解引用空指针。 |
| 2004 | ffmpeg-6.0 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 告警指向的代码行`s->st->time_base.den`在调用前已通过条件`s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->ic->nb_streams > 1`和`s->st`的隐式存... |
| 2001 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 687 | FP | FP | 切片代码显示，在指针 `ptr2` 被解引用之前，其值被赋为 `js_databuf + js_block_align - 1`。`js_databuf` 是 `databuf` 的偏移量，而 `databuf` 是函数参数，非空。`... |
| 2007 | ffmpeg-6.0 | ebml_read_binary | Dereference of null pointer | 1073 | FP | FP | 在调用memset之前，av_buffer_realloc函数已成功返回（ret >= 0），这保证了bin->buf和bin->buf->data是有效的非空指针。切片代码中的控制流和数据流足以确认不存在空指针解引用。 |
| 2005 | ffmpeg-6.0 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 408 | FP | FP | 切片代码显示，在访问 `ctx->buffers` 之前，存在条件判断 `if (ctx->buffers)` 和循环 `for (i = 0; i < ctx->num_buffers; i++)`，这确保了当 `ctx->buff... |
| 2008 | ffmpeg-6.0 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问 `ptr[2*x]` 和 `ptr[2*x+1]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且 `x` 的循环范围 `(w + 7 >> 3) * depth` 受控，不会越界。... |
| 2010 | ffmpeg-6.0 | unsharp_slice_16 | Dereference of null pointer | 142 | FP | FP | 告警指向的宏定义行 `{ NULL }` 是函数体结束的语法标记，并非对空指针的解引用。切片代码中未发现任何对空指针的实际解引用操作，因此该告警为误报。 |
| 2009 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 119 | FP | FP | 切片代码显示，在告警行`uint8_t *val = in->data[plane];`之前，`in`指针已作为函数参数传入且未被修改，其有效性由调用者保证。在`if (!out)`分支中，`out`可能被`ff_get_video_... |
| 2012 | ffmpeg-6.0 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警位于宏 UPDATE_CACHE 的调用处，但切片代码显示该宏最终展开为 UPDATE_CACHE_LE，其具体实现未在切片中提供。然而，根据上下文，该函数是解码器内部读取比特流的常用辅助函数，其参数 gb 通常由调用者正确初始化... |
| 2011 | ffmpeg-6.0 | ebml_parse | Dereference of null pointer | 1339 | FP | FP | 切片代码显示，在访问 `level->length` 之前，已通过 `if (matroska->num_levels > 0)` 检查确保 `level` 指针非空。`level` 在函数开头被定义为 `matroska->leve... |
| 2014 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码显示，`sample[0]` 在循环中被明确赋值，指向 `s->sample_buffer` 的有效偏移地址，不存在空指针解引用。告警点 `sample[0][x]` 的访问是安全的。 |
| 2015 | ffmpeg-6.0 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 332 | FP | FP | 切片代码显示，在访问 `ctx->buffers[i]` 之前，存在 `if (ctx->buffers)` 的检查，确保了指针不为空。告警所在行的循环受此前置条件保护，因此不会发生空指针解引用。 |
| 2018 | ffmpeg-6.0 | safe_filename | Dereference of null pointer | 97 | FP | FP | 代码逻辑已通过指针解引用前的条件判断 `for (; *f; f++)` 确保了指针 `f` 不为空，因为循环仅在 `*f` 为真（即非零字符，也隐含指针非空）时执行。该告警是工具对循环条件中解引用操作的误判。 |
| 2016 | ffmpeg-6.0 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 告警点位于对`s->st`指针的访问，但切片代码显示，在调用`av_packet_new_side_data`后，仅检查了`prft`是否为NULL，并未检查`s`或`s->st`是否为NULL。然而，函数`rtp_set_prft`... |
| 2019 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 117 | FP | FP | 切片代码显示，在访问 `in->linesize[plane]` 之前，`in` 指针作为函数参数传入且未被置空，并且在 `s->planeheight[plane] > 1` 条件为假时，`linesize` 被赋值为0，不会发生空... |
| 2017 | ffmpeg-6.0 | ebml_read_sint | Dereference of null pointer | 1000 | FP | FP | 切片代码显示，在调用`avio_r8(pb)`前未对指针`pb`进行空值检查，但被调用的`avio_r8`函数内部已包含对`s`（即`pb`）的成员`buf_ptr`和`buf_end`的访问。这表明`pb`在调用点已被假定为非空，且... |
| 2020 | ffmpeg-6.0 | of_open | Dereference of null pointer | 2303 | FP | FP | 切片代码显示，在访问 `ost->enc_ctx->codec` 之前，已经通过 `if (ost->filter)` 条件进行了检查，并且 `ost->enc_ctx` 在 `of_open` 函数的上下文中被使用，表明它很可能已被... |
| 2022 | ffmpeg-6.0 | get_sbits | Dereference of null pointer | 315 | FP | FP | 告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后仅涉及位操作，不会直接解引用指针。切片代码中未显示任何对空指针的显式解引用操作，且函数 get_sbits 的参数 s 在切片中未显示其来源，无法确认其为空。因此，该告警很可... |
| 2024 | ffmpeg-6.0 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1476 | FP | FP | 切片代码显示 scale_matrix 在条件分支中被赋值，且其使用点位于同一条件分支内（s->ps.sps->scaling_list_enable_flag 为真且 transform_skip_flag 为假或 log2_tra... |
| 2026 | ffmpeg-6.0 | hls_read_header | Dereference of null pointer | 2131 | FP | FP | 切片代码显示，在访问 `in_fmt->name` 之前，`in_fmt` 已通过 `av_demuxer_iterate` 或 `av_probe_input_buffer` 被赋值，且存在对 `seg` 和 `in_fmt` 的非... |
| 2028 | ffmpeg-6.0 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 切片代码显示，在访问 `file->user_duration` 之前，`file` 指针已在 `DIR_FILE` 分支通过 `add_file` 函数成功分配并赋值，且该分支有错误检查确保 `file` 不为 NULL。此外，`D... |
| 2021 | ffmpeg-6.0 | ff_encode_encode_cb | Dereference of null pointer | 244 | FP | FP | 告警指向的代码行 `if (frame->duration)` 位于 `if (frame)` 条件块内部，切片代码显示在调用该行之前，函数末尾有 `if (frame) av_frame_unref(frame);` 的检查，但更关... |
| 2029 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 297 | FP | FP | 切片代码显示，`src` 是函数参数，在循环内被用作基地址进行指针运算和类型转换。告警行 `((uint16_t*)(src + stride*y))[x]` 的访问依赖于 `src` 是否为空。函数是静态的且被调用，参数 `src`... |
| 2030 | ffmpeg-6.0 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 告警点位于条件语句`if (dpd[pos])`内部，对`dp1`和`dp2`的赋值仅在`dpd[pos]`为真（非零）时执行，这确保了指针`dp1`和`dp2`在解引用前已被检查。切片代码中`dp1`和`dp2`虽未显式定义，但根据... |
| 2034 | ffmpeg-6.0 | ebml_read_ascii | Dereference of null pointer | 1055 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 2033 | ffmpeg-6.0 | split_commandline | Dereference of null pointer | 713 | FP | FP | 切片代码显示，在访问 `opt[0]` 和 `opt[1]` 之前，变量 `opt` 已通过 `argv[optindex++]` 赋值，且 `argv` 来自命令行参数，在正常执行流程中不会为 NULL。告警点 `opt[0] ==... |
| 2037 | ffmpeg-6.0 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 告警点位于DIR_INPOINT分支，该分支仅在解析到'inpoint'指令时执行。切片代码显示，执行此分支前已通过条件`(dir->flags & NEEDS_FILE) && !cat->nb_files`检查，确保`file`指... |
| 2038 | ffmpeg-6.0 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警指向的代码行位于条件 `if ((*child)->state * 2 == -t->state)` 内部，该条件已确保 `*child` 非空（因为 `t->state` 非零且 `t->state & 1` 为假，且 `chi... |
| 2042 | ffmpeg-6.0 | build_table | Dereference of null pointer | 203 | FP | FP | 告警点 `table[j].len = -subtable_bits;` 处的 `table` 指针在切片代码中已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index`... |
| 2043 | ffmpeg-6.0 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警点位于 `if (chapters && nb_chapters)` 条件块内部，该条件已确保 `chapters` 非空且 `nb_chapters` 大于零。在后续循环中访问 `chapters[i]` 是安全的，不会发生空指... |
| 2041 | ffmpeg-6.0 | guess_mv | Dereference of null pointer | 428 | FP | FP | 在告警行 `else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])` 之前，已有条件 `if (s->last_pic.f && s->last_pic.f->data... |
| 2046 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 148 | FP | FP | 切片代码显示，在告警行`uint16_t *val = (uint16_t *)in->data[plane];`之前，`in`指针已作为函数参数传入，且后续代码中`in->data[plane]`被多次安全使用，未发现`in`为空的... |
| 2047 | ffmpeg-6.0 | av_dump_format | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `printed[program->stream_index[k]]` 之前，已通过 `if (ic->nb_streams && !printed) return;` 确保了当 `printed` 为 NULL... |
| 2049 | ffmpeg-6.0 | activate | Dereference of null pointer | 168 | FP | FP | 告警点位于`s->eof`为真的分支内，该分支中`frame`变量在赋值后（通过`ff_get_video_buffer`或`av_frame_clone`）均进行了空指针检查，仅在检查通过后才进行解引用操作。切片代码逻辑保证了`fr... |
| 2048 | ffmpeg-6.0 | choose_rct_params | Dereference of null pointer | 980 | FP | FP | 切片代码显示，在lbd为假的分支中，对src[0]、src[1]、src[2]进行了指针解引用。告警点位于对src[2]的解引用。函数参数src被声明为`const uint8_t *src[3]`，表明src是一个包含三个有效指针的... |
| 2050 | ffmpeg-6.0 | <global> | Dereference of null pointer | 199 | FP | FP | 切片代码显示，在访问 `ptr[8*x]` 等数组元素前，已通过 `if (x < len)` 和循环条件 `x < (w + 7 >> 3) * depth` 确保了索引 `x` 在有效范围内，且 `ptr2` 已通过 `av_ma... |
| 2051 | ffmpeg-6.0 | ff_encode_encode_cb | Dereference of null pointer | 241 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，其执行前提是 `frame` 指针非空（由外层条件 `(frame && ...)` 保证）。切片代码显示，在告警行之前，`frame`... |
| 2052 | ffmpeg-6.0 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 在告警行 `buf[0] & 0xc0` 之前，代码已通过 `if (!buf)` 检查了 `buf` 是否为 NULL，并且当 `buf` 为 NULL 时，函数会提前返回。因此，在到达告警行时，`buf` 保证为非 NULL 指针... |
| 2053 | ffmpeg-6.0 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已通过条件 `if (dpd[pos])` 和 `if (s->peak[i][j] && ...)` 进行了检查，确保了指针 `dpd` 指向的内存位置有效且不为空。告警点 `dpd... |
| 2055 | ffmpeg-6.0 | get_bits1 | Dereference of null pointer | 381 | FP | FP | 切片代码显示`s->buffer`被直接解引用，但函数`get_bits1`是内联的位读取辅助函数，其正确性依赖于调用者确保`GetBitContext *s`已正确初始化且`buffer`指针有效。在典型的流解析上下文中，调用前会进... |
| 2057 | ffmpeg-6.0 | <global> | Dereference of null pointer | 148 | FP | FP | 告警点位于条件`if (CONFIG_SWSCALE_ALPHA && hasAlpha)`内部，alpSrcPtr仅在条件为真时被赋值且不为NULL，否则为NULL。切片代码显示，在告警行使用alpSrcPtr之前，已通过同一条件检... |
| 2054 | ffmpeg-6.0 | ff_inlink_make_frame_writable | Dereference of null pointer | 1423 | FP | FP | 告警点位于对函数`ff_get_audio_buffer`的调用，其参数`frame->nb_samples`来自已检查过的`frame`指针。在调用前，函数已通过`av_frame_is_writable(frame)`和`av_l... |
| 2056 | ffmpeg-6.0 | asf_parse_packet | Dereference of null pointer | 1302 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data[i]` 之前，已通过 `av_new_packet` 或 `av_buffer_alloc` 等函数为 `asf_st->pkt.data` 分配了内存，且存在对 `asf_st... |
| 2059 | ffmpeg-6.0 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在访问 `dp1[pos]` 和 `dp2[pos]` 之前，已通过 `if (dpd[pos])` 条件进行了检查，这确保了指针 `dpd` 不为空，因此不会发生空指针解引用。 |
| 2058 | ffmpeg-6.0 | add_interval | Dereference of null pointer | 1035 | FP | FP | 告警点位于条件判断 `ri->type == type`，但前置条件 `if (ref >= 0)` 已确保 `ri` 是 `&inter->inter[ref]` 的有效指针，且 `ref` 在有效范围内时 `inter->inte... |
| 2060 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 335 | FP | FP | 告警点位于`s->out->pts = in->pts;`，但切片代码显示`s->out`在`if (s->do_video && (!s->out ｜｜ ...))`分支中通过`ff_get_video_buffer`分配，或在`e... |
| 2061 | ffmpeg-6.0 | unsharp_slice_8 | Dereference of null pointer | 143 | FP | FP | 切片代码显示，在宏展开的函数中，`sc` 和 `sr` 等指针在解引用前已从 `fp` 结构体中获取，且存在 `if (!amount)` 的早期返回路径。告警点 `{ NULL }` 是宏定义的一部分，并非实际执行代码，工具可能误解... |
| 2062 | ffmpeg-6.0 | ebml_parse | Dereference of null pointer | 1356 | FP | FP | 告警指向的代码行位于一个条件分支内，该分支在`level->length != EBML_UNKNOWN_LENGTH`时执行错误处理和返回，不会对空指针进行解引用。切片代码显示`level`变量在解引用前已通过`matroska->... |
| 2063 | ffmpeg-6.0 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码显示，`dpd` 指针是从 `out->data` 数组的某个元素赋值而来，而 `out` 是一个有效的 `AVFrame` 指针，其 `data` 字段在正常使用中应已被正确初始化。告警点是对 `dpd` 解引用，而非对 `... |
| 2066 | ffmpeg-6.0 | av_encryption_init_info_free | Dereference of null pointer | 219 | FP | FP | 代码在访问 `info->key_ids[i]` 前已通过 `if (info)` 检查了指针 `info` 非空，且循环条件 `i < info->num_key_ids` 确保了 `info->key_ids` 数组索引有效。告警... |
| 2071 | ffmpeg-6.0 | <global> | Dereference of null pointer | 168 | FP | FP | alpSrcPtr 的赋值在条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 下进行，告警行访问 alpSrcPtr 前有相同的条件保护，因此不会发生空指针解引用。 |
| 2070 | ffmpeg-6.0 | av_encryption_init_info_get_side_data | Dereference of null pointer | 278 | FP | FP | 告警指向的 `memcpy(info->key_ids[j], side_data, key_id_size)` 行，其 `info->key_ids[j]` 指针已在 `av_encryption_init_info_alloc` ... |
| 2068 | ffmpeg-6.0 | build_table | Dereference of null pointer | 169 | FP | FP | 告警点位于循环内部，访问 `table[j]` 前，`j` 的值由 `code` 移位计算或 `bitswap_32` 转换得到，且受循环条件 `k < nb` 限制，其中 `nb` 由 `table_nb_bits` 和 `n` 计... |
| 2072 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 146 | FP | FP | 切片代码显示，在警告行（`const int linesize = s->planeheight[plane] > 1 ? in->linesize[plane] / 2 : 0;`）中，对`in->linesize[plane]`的... |
| 2073 | ffmpeg-6.0 | get_bits | Dereference of null pointer | 330 | FP | FP | 告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后仅涉及对结构体指针 s 的成员访问。切片代码显示 get_bits 函数入口处未对 s 进行空指针检查，但该函数为内联静态函数，其调用上下文（调用方是否已校验指针）在切片中未... |
| 2074 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 291 | FP | FP | 切片代码显示，`sample[0]` 在循环中被明确赋值（`sample[i] = s->sample_buffer + ...`），且 `s->sample_buffer` 已通过 `memset` 初始化，因此 `sample[0... |
| 2075 | ffmpeg-6.0 | bits_priv_refill_32_be | Dereference of null pointer | 85 | FP | FP | 切片代码显示，在调用AV_RB32(bc->ptr)之前，存在条件判断`if (bc->ptr >= bc->buffer_end) return -1;`，这确保了当指针可能越界时函数会提前返回，从而防止了对无效指针的解引用。因此，... |
| 2076 | git-2.46.0 | add_parents_only | Dereference of null pointer | 1929 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且当 `it` 为 NULL 且 `revs->ignor... |
| 2077 | git-2.46.0 | get_mode | Dereference of null pointer | 63 | FP | FP | 告警点 `*special = SPECIAL_STDIN;` 位于 `path == file_from_standard_input` 的条件分支内，`special` 指针作为函数参数传入，在调用前已被检查非空（`if (spe... |
| 2079 | git-2.46.0 | crlf_to_git | Dereference of null pointer | 573 | FP | FP | 告警点位于循环内部，其指针 'src' 在进入循环前已通过条件 'if (!buf && !src)' 和 'if (!buf)' 等检查，且循环条件 'while (--len)' 确保了 'len' 在递减前为正数，因此指针解引用... |
| 2080 | git-2.46.0 | cwexec | Dereference of null pointer | 673 | FP | FP | 告警行 `d = delta[c = (end += d)[-1]];` 中，`end` 指针在循环条件 `while (lim - end >= d)` 和 `end += d` 操作下被确保不会越界，且 `d` 在循环开始时被检查... |
| 2082 | git-2.46.0 | parse_options_step | Dereference of null pointer | 900 | FP | FP | 告警点位于条件判断 `if (internal_help && *ctx->opt == 'h')`，其中 `ctx->opt` 在进入该分支前已通过 `ctx->opt = arg + 1;` 赋值，且 `arg` 是 `ctx->... |
| 2081 | git-2.46.0 | diffcore_merge_broken | Dereference of null pointer | 295 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环已通过 `struct diff_filepair *pp = q->queue[j];` 获取了 `pp` 指针，且外层循环已确保 `q->queue[i]` 非空（若为空则... |
| 2084 | git-2.46.0 | parse_options | Dereference of null pointer | 1046 | FP | FP | 告警点位于检查 `ctx->opt` 是否为 ASCII 字符的条件分支中，该分支仅在 `ctx->opt` 不为 NULL 时才会被评估。切片代码显示，在调用 `parse_options_step` 函数时，`ctx->opt` ... |
| 2085 | git-2.46.0 | process_entry | Dereference of null pointer | 3413 | FP | FP | 切片代码显示，在告警行`b->path = ci->ren2->pair->two->path;`之前，已通过`if (ci->ren2)`对`ci->ren2`进行了非空检查，确保了指针的有效性。因此，该行不会发生空指针解引用。 |
| 2086 | git-2.46.0 | verify_absent | Dereference of null pointer | 2526 | FP | FP | 告警点位于条件判断 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))`，其中 `ce` 和 `o` 均为函数入参，切片代码中未见其被赋值为 ... |
| 2088 | git-2.46.0 | output | Dereference of null pointer | 548 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `j < b->nr` 条件确保非空，且 `b_util->matching` 在 `while (j < b-... |
| 2087 | git-2.46.0 | show_pack_info | Dereference of null pointer | 1688 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，否则为 NULL。在告警行使用 `chain_histogram` 前，存在条件判断 ... |
| 2090 | git-2.46.0 | add_lines_to_move_detection | Dereference of null pointer | 1055 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，确保了数组访... |
| 2089 | git-2.46.0 | limit_list | Dereference of null pointer | 1492 | FP | FP | 切片代码显示，在告警行 `if (obj->flags & UNINTERESTING)` 中，`obj` 指针来自 `&commit->object`，而 `commit` 指针来自 `pop_commit` 函数。`pop_com... |
| 2091 | git-2.46.0 | limit_list | Dereference of null pointer | 1488 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量来自 `pop_commit(&original_list)` 的返回值，而 `pop_commit` 函数在输入指针非空时返回有效项，在输入为空时返回 ... |
| 2093 | git-2.46.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当`strmap_get_entry`返回NULL时，函数直接返回`map->default_value`，并未对空指针进行解引用。告警是对控制流逻辑的误判。 |
| 2095 | git-2.46.0 | merge_ort_internal | Dereference of null pointer | 5217 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--` 之前，`opt->priv->call_depth++` 已确保 `opt->priv` 不为空。该操作位于同一函数内的循环中，且 `opt->priv` 在函... |
| 2094 | git-2.46.0 | coalesce_lines | Dereference of null pointer | 264 | FP | FP | 在告警行 'newend = newend->prev;' 之前，'newend' 仅在 'directions[i][j] == MATCH' 分支内被赋值，而该分支仅在 'i != 0 ｜｜ j != 0' 循环中且 'direc... |
| 2097 | git-2.46.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1364 | FP | FP | 告警点位于对 `msg->buf` 的访问，切片代码显示 `msg` 是函数参数且非空，其 `buf` 成员在调用 `write_message` 前已被使用，不存在空指针解引用。 |
| 2096 | git-2.46.0 | process_parents | Dereference of null pointer | 1175 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，并且 `repo_parse_commit_gently` 调用成功（返回值为0）后才会执行该行，因此 `p` 是有效的，不会发生空指针解引用。 |
| 2101 | git-2.46.0 | add_lines_to_move_detection | Dereference of null pointer | 1058 | FP | FP | 切片代码显示，在访问 entry_list[l->id] 之前，已通过 ALLOC_GROW_BY 宏确保了 entry_list 数组的大小至少为 id+1，并且该宏会将新分配的内存清零，因此 entry_list 指针不可能为 N... |
| 2102 | git-2.46.0 | coalesce_lines | Dereference of null pointer | 272 | FP | FP | 在警告行`if (lline->prev)`之前，`lline`被赋值为`newend`，而`newend`在循环中通过`newend = newend->prev;`更新，这确保了`newend`（以及`lline`）是链表中的一个... |
| 2103 | git-2.46.0 | apply_one_fragment | Dereference of null pointer | 3025 | FP | FP | 切片代码显示，在访问 `postimage.line_allocated[postimage.nr - 1]` 之前，`postimage.nr` 已通过 `add_line_info` 函数递增，确保了数组索引有效。此外，访问操作位... |
| 2105 | git-2.46.0 | prepare_attr_stack | Dereference of null pointer | 1013 | FP | FP | 在调用 `bootstrap_attr_stack` 后，`*stack` 保证非空，且 `info = *stack` 赋值成功，因此 `info->prev` 的访问是安全的。后续的 `while ((*stack)->origi... |
| 2104 | git-2.46.0 | try_to_commit | Dereference of null pointer | 1698 | FP | FP | 告警指向的代码行 `commit_tree_extended(msg->buf, msg->len, &tree, parents, oid, author, committer, opts->gpg_sign, extra)` 中，... |
| 2108 | git-2.46.0 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数体为空，没有对指针进行解引用操作，因此不存在空指针解引用问题，属于工具误报。 |
| 2109 | git-2.46.0 | find_bisection | Dereference of null pointer | 439 | FP | FP | 在告警行`list->item = best->item;`之前，`best`指针已在`if (best)`条件中确认非空，且`list`指针由`last`赋值，而`last`在循环中被正确初始化并更新，不会为NULL。因此，对`li... |
| 2107 | git-2.46.0 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 切片代码显示，当 `line` 为 0 时直接返回 `data`，否则才进行指针运算。`ends` 数组的访问发生在 `line != 0` 的分支，且 `line` 作为参数传入，其值在切片中未显示来源。但根据函数逻辑，`ends`... |
| 2110 | git-2.46.0 | verify_absent_1 | Dereference of null pointer | 2485 | FP | FP | 告警点 `ce->name` 的指针 `ce` 由函数参数传入，切片中调用 `verify_absent_1` 的上下文缺失，无法证明其为空。同时，函数内部多处使用 `ce->name` 和 `ce->ce_mode` 等成员，若 `... |
| 2113 | git-2.46.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点是对指针`ce`的成员访问，而`ce`是函数的形参，在切片代码中，该函数的所有调用点均未展示，无法证明`ce`为NULL。根据函数定义和常规使用模式，传入NULL指针的可能性极低，且静态分析工具可能误判了指针的非空保证。 |
| 2112 | git-2.46.0 | try_to_commit | Dereference of null pointer | 1582 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，工具认为 `current_head` 可能为 NULL 导致空指针解引用。但在切片代码中，该行位于 `if (fl... |
| 2117 | git-2.46.0 | process_entries | Dereference of null pointer | 4451 | FP | FP | 告警点位于BUG宏调用前的错误检查分支，该分支仅在dir_metadata.offsets.nr不等于1或其首项util不为0时执行。切片代码显示，此分支的目的是打印调试信息并主动触发程序终止（BUG），这是预期的错误处理逻辑，而非对... |
| 2115 | git-2.46.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 677 | FP | FP | 在函数入口处，对指针 `tws` 的解引用 `tws->next` 发生在对其有效性进行检查之前。然而，该函数是静态的，其调用上下文未在切片中提供。根据常见的编码模式，此类内部辅助函数通常由上层函数在确保参数非空后调用。切片中未显示 ... |
| 2116 | git-2.46.0 | unload_one_branch | Dereference of null pointer | 2049 | FP | FP | 在进入while循环前，条件`cur_active_branches && cur_active_branches >= max_active_branches`确保了`cur_active_branches`大于0，因此`activ... |
| 2118 | git-2.46.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已在循环中被填充，且条件 `remotes->nr == 1` 确保了列表至少有一个元... |
| 2120 | git-2.46.0 | cmd_merge | Dereference of null pointer | 1529 | FP | FP | 切片代码显示告警行 `use_strategies[i]->attr` 位于循环中，且 `use_strategies` 数组在循环前已通过 `git_config` 等函数初始化，`i` 的边界由 `use_strategies_n... |
| 2119 | git-2.46.0 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警位于循环条件 'curr = curr->next' 中，但切片代码显示，在该循环之前，'curr' 被初始化为 'kwset->trie->next'，而 'kwset->trie' 在之前的代码路径中已被确保为非空（例如，在 ... |
| 2121 | git-2.46.0 | get_ref_map | Dereference of null pointer | 545 | FP | FP | 告警指向的循环条件 `for (i = 0; i < fetch_refspec->nr; i++)` 中，`fetch_refspec` 变量在切片代码中已明确赋值：当 `refmap.nr` 为真时指向 `&refmap`，否则指... |
| 2122 | git-2.46.0 | setup_scoreboard | Dereference of null pointer | 2841 | FP | FP | 在while循环条件`c->parents`之前，`final_commit`已通过`find_single_final`函数赋值，且该函数在正常情况下返回非空指针或调用`die`终止程序。切片中`find_single_final`... |
| 2123 | git-2.46.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `sb->buf[len]` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 确保 `sb->buf` 不是指向静态缓冲区 `strbuf_slopbuf` 的空指针或无效指针... |
| 2125 | git-2.46.0 | assert_sane_strbuf | Dereference of null pointer | 36 | FP | FP | 切片代码显示，在解引用 `buf->buf` 之前，已通过 `check(!!buf->buf)` 宏对指针进行了非空检查。该检查确保了后续访问 `buf->buf[buf->len]` 时指针有效，因此告警为误报。 |
| 2126 | git-2.46.0 | show_pack_info | Dereference of null pointer | 1710 | FP | FP | 切片代码显示，在访问 `chain_histogram[i]` 之前，`chain_histogram` 已在 `if (deepest_delta)` 条件下通过 `CALLOC_ARRAY` 分配了内存，且循环条件 `i < de... |
| 2127 | git-2.49.0 | image_remove_last_line | Dereference of null pointer | 363 | FP | FP | 切片代码显示，在访问 `img->line[img->line_nr - 1]` 之前，没有检查 `img->line_nr` 是否大于0。然而，函数名 `image_remove_last_line` 暗示其调用上下文应确保 `im... |
| 2128 | git-2.49.0 | add_parents_only | Dereference of null pointer | 1941 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且当 `revs->ignore_missing` 为真时... |
| 2129 | git-2.49.0 | get_mode | Dereference of null pointer | 65 | FP | FP | 告警点位于 `*special = SPECIAL_STDIN;`，但切片代码显示，该赋值仅在 `path == file_from_standard_input` 条件成立时执行，而 `file_from_standard_inpu... |
| 2131 | git-2.49.0 | <global> | Dereference of null pointer | 88 | FP | FP | 告警指向的代码行 `check_str(out[0], "a");` 位于单元测试函数中，`out` 指针已通过 `check(out != NULL);` 进行了非空检查，且 `parse_names` 函数在成功时返回非空指针。切... |
| 2133 | git-2.49.0 | cwexec | Dereference of null pointer | 675 | FP | FP | 告警指向的代码行 `d = delta[c = (end += d)[-1]];` 在切片上下文中，`end` 和 `d` 变量在循环前已被初始化，且循环条件 `while (lim - end >= d)` 保证了 `end` 指针... |
| 2132 | git-2.49.0 | crlf_to_git | Dereference of null pointer | 583 | FP | FP | 切片代码显示，在解引用 `src` 指针之前，函数已通过条件 `if (src && !len)` 和 `if (!buf && !src)` 对 `src` 进行了空指针检查。在后续循环中，`src` 仅在 `len > 0` 时被... |
| 2134 | git-2.49.0 | diffcore_merge_broken | Dereference of null pointer | 291 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环已确保 `pp = q->queue[j]` 被赋值，且外层循环已对 `q->queue[i]` 进行了空指针检查，代码逻辑保证了 `pp` 不为空。告警点位于 `if (pp... |
| 2137 | git-2.49.0 | clar_summary_init | Dereference of null pointer | 76 | FP | FP | 切片代码显示，在`summary->filename = filename;`执行前，若`fopen`失败会调用`clar_abort`，该函数会调用`exit(-1)`终止程序，因此`summary`指针不可能为NULL时执行到告警行。 |
| 2135 | git-2.49.0 | parse_options_step | Dereference of null pointer | 906 | FP | FP | 告警点 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 在进入该分支前已被检查为非空（`if (ctx->opt)`），且其值来源于 `arg + 1`（`ctx->opt ... |
| 2139 | git-2.49.0 | <global> | Dereference of null pointer | 82 | FP | FP | 告警点位于单元测试代码中，对 `out[0]` 的访问前已有 `check(out != NULL)` 断言，且 `parse_names` 函数在成功时返回非空指针。切片内逻辑保证了 `out` 非空，不会发生空指针解引用。 |
| 2138 | git-2.49.0 | parse_options | Dereference of null pointer | 1052 | FP | FP | 告警点位于 `isascii(*ctx.opt)`，但切片代码显示，在进入该分支前，`ctx.opt` 已在 `parse_options_step` 函数中被显式重置为 `NULL`，且只有当 `parse_options_step... |
| 2141 | git-2.49.0 | verify_absent | Dereference of null pointer | 2537 | FP | FP | 告警点位于条件判断 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))`，工具可能认为 `o` 或 `ce` 可能为空指针。但根据函数签名和上... |
| 2142 | git-2.49.0 | show_pack_info | Dereference of null pointer | 1776 | FP | FP | 切片代码显示，在访问 `chain_histogram` 数组之前，存在条件 `if (deepest_delta)` 保护了对 `CALLOC_ARRAY(chain_histogram, deepest_delta)` 的调用。只... |
| 2143 | git-2.49.0 | output | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `b_util = j < b->nr ? b->items[j].util : NULL;` 赋值，且后续有 ... |
| 2145 | git-2.49.0 | limit_list | Dereference of null pointer | 1499 | FP | FP | 告警点位于检查 `obj->flags & UNINTERESTING` 的条件判断中，`obj` 由 `&commit->object` 赋值，`commit` 来自 `pop_commit` 函数，该函数在栈非空时返回有效指针，在... |
| 2149 | git-2.49.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当`strmap_get_entry`返回NULL时，函数直接返回`map->default_value`，并未对空指针进行解引用。告警是对函数返回路径的误判。 |
| 2147 | git-2.49.0 | limit_list | Dereference of null pointer | 1495 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量来自 `pop_commit(&original_list)`，该函数在栈非空时返回有效指针，在栈空时返回 NULL。但告警所在行位于 `while (o... |
| 2152 | git-2.49.0 | assert_sane_strbuf | Dereference of null pointer | 35 | FP | FP | 切片代码显示，`cl_assert` 是一个宏，用于单元测试断言。该行代码的目的是验证 `strbuf` 结构体内部缓冲区以空字符结尾，是主动进行的健全性检查，而非对可能为空的指针进行解引用。这是一个防御性编程检查，不是逻辑错误。 |
| 2151 | git-2.49.0 | merge_ort_internal | Dereference of null pointer | 5219 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--` 之前，`opt->priv->call_depth` 已在同一循环中被递增（`opt->priv->call_depth++`），且 `opt->priv` 在... |
| 2150 | git-2.49.0 | coalesce_lines | Dereference of null pointer | 251 | FP | FP | 在告警行 `newend = newend->prev;` 之前，`newend` 仅在 `directions[i][j] == MATCH` 分支内被赋值，而该分支仅在 `i != 0 ｜｜ j != 0` 循环中进入。切片代码显... |
| 2153 | git-2.49.0 | process_parents | Dereference of null pointer | 1182 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查确保指针 `p` 非空，且 `repo_parse_commit_gently` 调用失败时会跳过后续处理，因此对 `p->parents` 的访问是安全的。 |
| 2156 | git-2.49.0 | clar_parse_args | Dereference of null pointer | 496 | FP | FP | 告警点位于 `explicit->suite_idx = j;`，该赋值操作仅涉及局部变量 `j`，其值由循环 `for (j = 0; j < _clar_suite_count; ++j)` 控制，已确保在有效范围内，不存在空指针... |
| 2154 | git-2.49.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1366 | FP | FP | 告警指向的代码行 `write_message(msg->buf, msg->len, name, 0)` 中，`msg` 参数由调用方传入，切片内未显示其为空。函数 `write_message` 内部对 `buf` 和 `file... |
| 2157 | git-2.49.0 | append_strategy | Dereference of null pointer | 234 | FP | FP | 切片代码显示`s`作为参数传入，在函数内部被直接使用，没有显式的空指针检查。然而，该函数是静态的，其调用上下文未知。在典型的C语言实践中，数组`use_strategies`的索引`use_strategies_nr`应在递增前确保未... |
| 2155 | git-2.49.0 | gather_stats | Dereference of null pointer | 52 | FP | FP | 切片代码显示函数参数`buf`在循环访问前未进行空指针检查，但函数签名表明`buf`是一个`const char*`指针，且函数内部对其进行了数组式访问`buf[i]`和`buf[i+1]`。在C语言中，向函数传递一个空指针并试图解引... |
| 2160 | git-2.49.0 | add_lines_to_move_detection | Dereference of null pointer | 1063 | FP | FP | 切片代码显示，在访问 entry_list[l->id] 之前，l->id 的值由条件分支明确赋值（来自 s->es->id 或递增的 id），且 entry_list 数组通过 ALLOC_GROW_BY 宏随 id 增长而动态扩容... |
| 2163 | git-2.49.0 | write_table | Dereference of null pointer | 65 | FP | FP | 切片代码显示，`(*names)[i]` 的赋值来自 `xstrfmt` 的返回值，该函数内部会分配内存并返回有效指针，不会返回 NULL。因此，对 `(*names)[i]` 的后续使用（如 `logs[i].refname = (... |
| 2162 | git-2.49.0 | coalesce_lines | Dereference of null pointer | 259 | FP | FP | 在警告所在行 'if (lline->prev)' 之前，'lline' 被赋值为 'newend'，而 'newend' 在循环中通过 'newend = newend->prev' 或 'newend = lline->prev'... |
| 2164 | git-2.49.0 | strvec_splice | Dereference of null pointer | 69 | FP | FP | 切片代码显示，在调用ALLOC_GROW宏之前，如果`array->v == empty_strvec`，会将其设置为NULL。ALLOC_GROW宏内部包含REALLOC_ARRAY，该宏会处理NULL指针的重新分配，因此`arra... |
| 2166 | git-2.49.0 | try_to_commit | Dereference of null pointer | 1700 | FP | FP | 告警指向的代码行 `commit_tree_extended(msg->buf, msg->len, ...)` 中，`msg` 指针在调用前已被检查并确保非空（例如在 `if (!msg) { ... msg = &commit_m... |
| 2167 | git-2.49.0 | prepare_attr_stack | Dereference of null pointer | 978 | FP | FP | 在调用 `*stack = info->prev;` 之前，`info` 被赋值为 `*stack`，而 `*stack` 由 `bootstrap_attr_stack` 初始化。`bootstrap_attr_stack` 确保 ... |
| 2169 | git-2.49.0 | get_nth_line | Dereference of null pointer | 879 | FP | FP | 切片代码显示，函数在访问 `ends[line]` 前已通过 `if (line == 0)` 分支处理了索引为0的情况，且 `line` 参数为 `long` 类型，`ends` 为 `unsigned long*` 类型。对于 `... |
| 2170 | git-2.49.0 | <global> | Dereference of null pointer | 15 | FP | FP | 提供的切片代码仅为一个空函数定义，函数体为空，不存在任何指针解引用操作，因此工具报告的'空指针解引用'逻辑错误不成立。 |
| 2171 | git-2.49.0 | find_bisection | Dereference of null pointer | 440 | FP | FP | 告警点位于 `if (best) {` 条件块内，`list` 指针在进入该块前已通过 `list = last;` 被赋值，且 `last` 在循环中被初始化为 `NULL` 后更新为有效链表节点，因此 `list` 不可能为 NU... |
| 2173 | git-2.49.0 | verify_absent_1 | Dereference of null pointer | 2496 | FP | FP | 告警点位于对 `ce_namelen(ce)` 宏的调用，该宏展开为 `((ce)->ce_namelen)`。切片代码显示，函数入口处 `ce` 作为参数传入，并在多处被直接使用（如 `ce->name`），表明 `ce` 指针在调... |
| 2174 | git-2.49.0 | <global> | Dereference of null pointer | 182 | FP | FP | 告警位于单元测试代码中，对指针 `arr` 的访问（`arr[0] = 42;`）发生在 `REFTABLE_ALLOC_GROW_OR_NULL` 宏调用之后，且紧跟着 `check(arr != NULL);` 断言。切片代码显示... |
| 2172 | git-2.49.0 | <global> | Dereference of null pointer | 1541 | FP | FP | 切片代码显示告警行 `use_strategies[i]->attr & NO_FAST_FORWARD` 位于循环 `for (i = 0; i < use_strategies_nr; i++)` 内，循环条件确保了 `i` 在有... |
| 2176 | git-2.49.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点是对结构体指针`ce`成员的访问，切片代码显示`ce`是函数参数，调用方未在切片内，但函数逻辑本身是安全的。该告警是静态分析工具对指针可能为空的过度推断，在正常使用场景下，传入的`ce`应为有效指针，因此判定为误报。 |
| 2175 | git-2.49.0 | try_to_commit | Dereference of null pointer | 1584 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，其中 `current_head` 在 `if (flags & AMEND_MSG)` 分支中已通过 `parse... |
| 2177 | git-2.49.0 | cmp_local_packs | Dereference of null pointer | 509 | FP | FP | 函数`cmp_local_packs`被声明为static，仅在文件内部调用。切片代码显示`local_packs`是全局变量，其初始化值`NULL`在函数调用前可能已被其他代码修改。告警点`if (!pl->next)`假设`pl`... |
| 2178 | git-2.49.0 | t_log_write_read | Dereference of null pointer | 224 | FP | FP | 告警指向的 `names[i] = xstrdup(name);` 行，`name` 是局部数组，`xstrdup` 内部会检查 `strdup` 的返回值并在失败时调用 `die` 终止程序，因此不会返回空指针给 `names[i]... |
| 2179 | git-2.49.0 | reftable_stack_reload_once | Dereference of null pointer | 351 | FP | FP | 切片代码显示，在告警行 `new_readers[new_readers_len] = rd;` 之前，`new_readers` 已在条件 `if (names_len)` 下通过 `reftable_calloc` 分配了内存，且... |
| 2181 | git-2.49.0 | unload_one_branch | Dereference of null pointer | 2065 | FP | FP | 在进入while循环前，代码已检查`cur_active_branches`非零，且`active_branches`在循环内被赋值给`e`，因此`e`在解引用时不可能为NULL。 |
| 2180 | git-2.49.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 678 | FP | FP | 在函数入口处，指针 `tws` 被解引用以访问其 `next` 成员，但该操作仅在 `if (n)` 条件块之前执行。切片代码显示，`tws` 作为函数参数传入，其有效性应由调用者保证。更重要的是，对 `tws->next` 的访问结... |
| 2182 | git-2.49.0 | cmd_add | Dereference of null pointer | 431 | FP | FP | 切片代码显示函数参数 `repo` 被直接解引用，但该函数签名表明 `repo` 是一个指向 `struct repository` 的指针，且作为参数传入。在典型的函数调用上下文中，传入的指针参数应为有效对象，否则调用方逻辑本身存在... |
| 2183 | git-2.49.0 | apply_one_fragment | Dereference of null pointer | 2991 | FP | FP | 切片代码显示，在访问 `postimage.line[postimage.line_nr - 1]` 之前，`postimage.line_nr` 已通过 `image_add_line` 函数递增，且 `postimage.line... |
| 2185 | git-2.49.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已在循环中被填充，且 `remotes->nr == 1` 的条件确保了列表至少有一个... |
| 2184 | git-2.49.0 | process_entries | Dereference of null pointer | 4453 | FP | FP | 告警点位于BUG宏调用前的错误信息打印语句中，该语句仅在dir_metadata.offsets.nr != 1或dir_metadata.offsets.items[0].util != 0时执行，这是一个明确的错误处理路径，旨在触... |
| 2186 | git-2.49.0 | clar_run_suite | Dereference of null pointer | 399 | FP | FP | 告警点 `report->suite = _clar.active_suite;` 中，`report` 指针由 `calloc` 分配，分配失败时会调用 `clar_abort` 退出程序，因此 `report` 不可能为 NULL... |
| 2188 | git-2.49.0 | <global> | Dereference of null pointer | 188 | FP | FP | 告警位于单元测试代码中，该行 `arr[alloc - 1] = 42;` 前有明确的 `check(arr != NULL);` 断言，确保指针非空后才进行解引用。这是测试逻辑的一部分，用于验证内存分配功能，并非实际的空指针解引用漏洞。 |
| 2187 | git-2.49.0 | kwsprep | Dereference of null pointer | 504 | FP | FP | 告警位于循环条件 'curr = kwset->trie->next'，但切片代码显示，在进入该循环前，'kwset->trie' 已在 'for (curr = last = kwset->trie; curr; curr = cu... |
| 2189 | git-2.49.0 | get_ref_map | Dereference of null pointer | 545 | FP | FP | 告警指向的代码行 `for (i = 0; i < fetch_refspec->nr; i++)` 中，`fetch_refspec` 变量在切片内已明确赋值：它要么指向 `&refmap`（当 `refmap.nr` 非零时），要... |
| 2190 | git-2.49.0 | setup_scoreboard | Dereference of null pointer | 2842 | FP | FP | 切片代码显示，在访问 `c->parents` 之前，`c` 被赋值为 `final_commit`，而 `final_commit` 仅在 `sb->reverse && sb->revs->first_parent_only` 条... |
| 2191 | git-2.49.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `sb->buf[len]` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 确保 `sb->buf` 不是指向静态缓冲区 `strbuf_slopbuf` 的空指针或无效指针... |
| 2194 | git-2.49.0 | show_pack_info | Dereference of null pointer | 1798 | FP | FP | 切片代码显示，在访问`chain_histogram[i]`之前，已通过`if (deepest_delta)`条件判断并调用了`CALLOC_ARRAY`进行分配，且循环边界为`deepest_delta`，确保了指针非空且访问在有... |
| 2195 | git-2.44.0 | add_parents_only | Dereference of null pointer | 1898 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且当 `revs->ignore_missing` 为真时... |
| 2196 | git-2.44.0 | table_iter_next_block | Dereference of null pointer | 327 | FP | FP | 切片代码显示，在计算 `next_block_off` 时，`src->bi.br` 已被使用，这表明在调用 `table_iter_next_block` 之前，`src->bi.br` 已被正确初始化且不为空，否则程序无法运行到该... |
| 2197 | git-2.44.0 | get_mode | Dereference of null pointer | 63 | FP | FP | 告警点 `*special = SPECIAL_STDIN;` 位于 `if (path == file_from_standard_input)` 分支内，该分支仅在 `path` 指向常量字符串 `"-"` 时执行。切片代码显示 ... |
| 2199 | git-2.44.0 | crlf_to_git | Dereference of null pointer | 569 | FP | FP | 告警点位于循环内部，其指针'src'在进入循环前已通过条件'if (!buf && !src)'和'if (!buf)'等检查确保非空，且循环条件'--len'保证了在len>0时才会解引用，切片内代码逻辑已防止空指针解引用。 |
| 2200 | git-2.44.0 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码显示，在访问 `trie->accepting` 和 `trie->shift` 之前，`trie` 变量已通过 `trie = next[c]` 赋值，且 `next` 数组来自 `kwset->next`。虽然存在 `if... |
| 2202 | git-2.44.0 | parse_options_step | Dereference of null pointer | 891 | FP | FP | 告警点 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 在多个分支（如 `parse_short_opt` 成功时）会被设置为 `NULL`，但在执行到该行时，`ctx->o... |
| 2204 | git-2.44.0 | parse_options | Dereference of null pointer | 1037 | FP | FP | 在告警行 `isascii(*ctx.opt)` 之前，`ctx.opt` 已在 `parse_options_step` 函数中被显式初始化为 `NULL`，并且在 `PARSE_OPT_UNKNOWN` 分支中，只有当 `ctx-... |
| 2205 | git-2.44.0 | process_entry | Dereference of null pointer | 3357 | FP | FP | 告警指向的代码行位于switch语句的RENAME_ONE_FILE_TO_TWO分支内，该分支仅在ci->ren2不为空时才会执行。切片代码显示，在进入此分支前，存在对ci->ren2的显式检查（if (ci->ren2) { as... |
| 2206 | git-2.44.0 | verify_absent | Dereference of null pointer | 2523 | FP | FP | 告警行代码 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))` 中，`ce` 和 `o` 均为函数入参，在调用前已被检查，且切片内 `ver... |
| 2207 | git-2.44.0 | show_pack_info | Dereference of null pointer | 1698 | FP | FP | 切片代码显示，在访问 `chain_histogram` 数组前，已通过条件 `if (deepest_delta)` 进行保护，仅当 `deepest_delta` 为真（非零）时才会分配内存。因此，在循环内访问 `chain_hi... |
| 2208 | git-2.44.0 | output | Dereference of null pointer | 546 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `j < b->nr` 条件确保非空，且 `b_util->matching` 在 `while (j < b-... |
| 2209 | git-2.44.0 | limit_list | Dereference of null pointer | 1460 | FP | FP | 告警点位于检查 `obj->flags & UNINTERESTING` 的条件判断处，`obj` 指针由 `&commit->object` 赋值，而 `commit` 来自 `pop_commit` 函数。切片代码显示 `pop_... |
| 2211 | git-2.44.0 | limit_list | Dereference of null pointer | 1456 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量来自 `pop_commit` 函数，该函数在栈非空时返回有效指针，在栈为空时返回 NULL。告警所在行位于 `while (original_list)... |
| 2213 | git-2.44.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 切片代码显示，当 `result` 为 NULL 时，函数直接返回 `map->default_value`，并未对空指针进行解引用。告警的逻辑错误不成立。 |
| 2215 | git-2.44.0 | process_parents | Dereference of null pointer | 1143 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查确保指针 `p` 非空，且 `repo_parse_commit_gently` 调用后 `p` 仍有效。因此，对 `p->parents` 的访问是安全的，不... |
| 2214 | git-2.44.0 | coalesce_lines | Dereference of null pointer | 262 | FP | FP | 在告警行 'newend = newend->prev;' 之前，代码已通过 'if (directions[i][j] == MATCH)' 条件确保进入该分支，且 'directions' 数组已正确初始化并赋值，'newend'... |
| 2216 | git-2.44.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1282 | FP | FP | 告警点 `msg->buf` 的指针 `msg` 是函数参数，由调用者传入，在切片代码中未发现其被赋值为 NULL 的路径。函数逻辑在调用 `write_message` 前未对 `msg` 进行空指针检查，但调用者可能已确保其非空。... |
| 2218 | git-2.44.0 | append_strategy | Dereference of null pointer | 227 | FP | FP | 切片代码显示`s`作为参数传入，函数内部仅将其赋值给数组。在函数内部没有对`s`进行空指针解引用操作，且告警点所在行是数组赋值，并非解引用指针。该告警是工具的逻辑误判。 |
| 2219 | git-2.44.0 | add_lines_to_move_detection | Dereference of null pointer | 1037 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，确保索引在已... |
| 2220 | git-2.44.0 | coalesce_lines | Dereference of null pointer | 270 | FP | FP | 在警告所在行 'if (lline->prev)' 之前，'lline' 被赋值为 'newend'，而 'newend' 在循环中通过 'newend = newend->prev' 更新，其值在进入该分支时由 'direction... |
| 2222 | git-2.44.0 | try_to_commit | Dereference of null pointer | 1615 | FP | FP | 告警指向的 `commit_tree_extended` 函数调用行，其 `parents` 参数在切片代码的所有可达路径中均被正确初始化（可能为 NULL 或指向有效链表），且该函数内部已对 NULL `parents` 指针进行安... |
| 2221 | git-2.44.0 | apply_one_fragment | Dereference of null pointer | 2990 | FP | FP | 切片代码显示，在访问 `postimage.line_allocated[preimage.nr - 1]` 之前，`preimage.nr` 已通过 `add_line_info` 函数递增，确保了 `preimage.nr - 1... |
| 2223 | git-2.44.0 | prepare_attr_stack | Dereference of null pointer | 1011 | FP | FP | 在调用 `*stack = info->prev;` 之前，`info` 被赋值为 `*stack`，而 `*stack` 在 `bootstrap_attr_stack` 函数中被确保为非空（若为空则初始化）。切片代码中的 `ass... |
| 2228 | git-2.44.0 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对指针 `ref_iterator` 进行解引用操作，因此不存在空指针解引用问题。 |
| 2226 | git-2.44.0 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 切片代码显示，函数在 `line == 0` 时直接返回 `(char *)data`，否则返回一个基于 `ends[line]` 的偏移量。`ends` 数组的访问依赖于参数 `line`，但函数内部没有对 `line` 进行边界检... |
| 2229 | git-2.44.0 | find_bisection | Dereference of null pointer | 437 | FP | FP | 告警点位于条件分支 `if (best)` 内部，`best` 指针非空时才会执行 `list->item = best->item;`，因此不会发生空指针解引用。切片代码已显示 `best` 在解引用前已通过条件检查，逻辑安全。 |
| 2233 | git-2.44.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点是对函数`match_pathspec`的调用，其参数`ce`来自函数入参，且切片中`ce`被用于访问`ce->name`和`ce->ce_mode`，表明`ce`在调用前已被解引用，若其为空指针则程序已在前序逻辑中崩溃。因此，... |
| 2230 | git-2.44.0 | verify_absent_1 | Dereference of null pointer | 2482 | FP | FP | 告警点位于对 `ce_namelen(ce)` 宏的调用，该宏展开为 `((ce)->ce_namelen)`。切片代码显示，函数入口参数 `ce` 被直接使用，没有对其进行空指针检查。然而，该函数 `verify_absent_1`... |
| 2232 | git-2.44.0 | try_to_commit | Dereference of null pointer | 1499 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，工具认为 `current_head` 可能为空指针。但在切片代码中，该行位于 `if (flags & AMEND... |
| 2235 | git-2.44.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 673 | FP | FP | 在函数入口处，指针 `tws` 被解引用以访问 `tws->next`，但该指针在调用前已被调用方检查为非空，且切片代码中未显示任何可能使其为空的赋值路径。对 `tws` 的解引用发生在对其成员 `n` 的 null 检查之前，但逻辑... |
| 2236 | git-2.44.0 | unload_one_branch | Dereference of null pointer | 2052 | FP | FP | 在进入while循环前，条件`cur_active_branches && cur_active_branches >= max_active_branches`确保了`cur_active_branches`大于0，因此`activ... |
| 2234 | git-2.44.0 | cmp_local_packs | Dereference of null pointer | 479 | FP | FP | 告警点检查 `pl->next` 前，`pl` 已从全局变量 `local_packs` 初始化。`local_packs` 在文件作用域初始化为 NULL，但 `cmp_local_packs` 是静态函数，其调用时机未知。切片中无... |
| 2237 | git-2.44.0 | process_entries | Dereference of null pointer | 4329 | FP | FP | 告警点位于一个BUG断言检查的printf语句中，该代码路径仅在内部一致性检查失败时触发，用于输出调试信息并终止程序。对空指针的访问（dir_metadata.offsets.items[0].util）发生在条件判断之后，该条件已确... |
| 2238 | git-2.44.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 169 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已在循环中被填充，且 `remotes->nr == 1` 的条件保证了列表至少有一个... |
| 2239 | git-2.44.0 | merge_ort_internal | Dereference of null pointer | 5056 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--` 之前，`opt->priv->call_depth` 已通过 `opt->priv->call_depth++` 进行了递增，确保了 `opt->priv` 不... |
| 2240 | git-2.44.0 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警位于循环条件 'curr = kwset->trie->next'，但切片代码显示，在进入该循环前，'kwset->trie' 已在 'for (curr = last = kwset->trie; curr; curr = cu... |
| 2241 | git-2.44.0 | cmd_merge | Dereference of null pointer | 1509 | FP | FP | 告警点位于条件判断语句中，访问的是结构体指针的成员属性，该指针在循环前已通过数组索引访问，且数组在切片中未见为空。代码逻辑保证了指针的有效性，不存在空指针解引用。 |
| 2242 | git-2.44.0 | get_ref_map | Dereference of null pointer | 544 | FP | FP | 切片代码显示，在访问 `remote->fetch` 之前，函数开头已通过 `if (remote)` 对 `remote` 指针进行了非空检查。告警点位于 `for (i = 0; i < remote->fetch.nr; i++... |
| 2243 | git-2.44.0 | setup_scoreboard | Dereference of null pointer | 2839 | FP | FP | 在while循环条件`c->parents`之前，`final_commit`已通过`find_single_final(sb->revs, NULL)`赋值，且该函数在切片中显示会返回有效提交或调用`die`终止程序，因此`c`不为... |
| 2244 | git-2.44.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 代码在访问 `sb->buf[len]` 前已通过 `if (sb->buf != strbuf_slopbuf)` 检查，确保 `sb->buf` 不为空或指向特殊缓冲区；即使进入 else 分支，也是安全的断言检查，不存在空指针解引用。 |
| 2246 | git-2.44.0 | assert_sane_strbuf | Dereference of null pointer | 34 | FP | FP | 告警点位于宏展开的检查函数中，其逻辑是检查条件是否成立，而非直接解引用空指针。切片代码显示，在调用 `check_char` 之前，已通过 `check(!!buf->buf)` 验证了 `buf->buf` 非空，因此解引用是安全的。 |
| 2247 | git-2.44.0 | show_pack_info | Dereference of null pointer | 1720 | FP | FP | 切片代码显示，在for循环访问`chain_histogram[i]`之前，已通过条件`if (deepest_delta)`判断，若条件为真则调用`CALLOC_ARRAY`为指针分配内存，否则指针保持为NULL。循环条件`i < ... |
| 2248 | git-2.50.1 | image_remove_last_line | Dereference of null pointer | 363 | FP | FP | 切片代码显示，在访问 `img->line[img->line_nr - 1]` 之前，没有检查 `img->line` 是否为 NULL 或 `img->line_nr` 是否大于 0。然而，函数 `image_remove_las... |
| 2249 | git-2.50.1 | add_parents_only | Dereference of null pointer | 1933 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且当 `revs->ignore_missing` 为真时... |
| 2250 | git-2.50.1 | reftable_stack_reload_once | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在告警行`new_tables[new_tables_len] = table;`之前，`new_tables`已通过`reftable_calloc`分配了内存，且分配大小`names_len`与后续循环写入的数组长度... |
| 2251 | git-2.50.1 | get_mode | Dereference of null pointer | 65 | FP | FP | 告警点位于检查 `path == file_from_standard_input` 为真的分支内，此时 `special` 指针作为函数参数传入，在该分支内被直接解引用赋值，并非空指针解引用。切片代码逻辑表明该路径是安全的。 |
| 2254 | git-2.50.1 | crlf_to_git | Dereference of null pointer | 583 | FP | FP | 告警指向的指针解引用发生在条件判断 `if (! (c == '\r' && (1 < len && *src == '\n')))` 内部，该条件已通过 `(1 < len && *src == '\n')` 确保在解引用 `*sr... |
| 2256 | git-2.50.1 | diffcore_merge_broken | Dereference of null pointer | 291 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环已确保 `pp = q->queue[j]` 赋值，且外层循环已对 `q->queue[i]` 进行了空指针检查，代码逻辑保证了 `pp` 不为空。切片中未显示 `q->que... |
| 2255 | git-2.50.1 | cwexec | Dereference of null pointer | 679 | FP | FP | 告警指向的代码行 `d = delta[c = (end += d)[-1]];` 在 `else` 分支内，该分支仅在 `qlim` 为真且 `end > qlim` 时执行。切片显示 `qlim` 可能为 `NULL`，但进入此分... |
| 2257 | git-2.50.1 | parse_options_step | Dereference of null pointer | 958 | FP | FP | 在警告行 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 的赋值在切片代码中清晰可见（例如 `ctx->opt = arg + 1;`），且其值来源于命令行参数 `arg`。... |
| 2259 | git-2.50.1 | clar_summary_init | Dereference of null pointer | 76 | FP | FP | 在调用 `summary->filename = filename` 之前，`summary` 指针的初始化或分配未包含在切片中，但告警点位于 `fopen` 失败检查之后。如果 `fopen` 失败，`clar_abort` 函数将... |
| 2260 | git-2.50.1 | parse_options | Dereference of null pointer | 1104 | FP | FP | 告警点位于条件分支 `else if (isascii(*ctx.opt))`，但切片代码显示，在进入该分支前，`ctx.opt` 已在 `parse_options_step` 函数中被显式重置为 `NULL`，且该分支仅在 `ct... |
| 2261 | git-2.50.1 | allocate_snapshot_buffer | Dereference of null pointer | 533 | FP | FP | 告警指向的 `die_errno` 函数调用是错误处理路径，用于在 `read_in_full` 读取失败或读取字节数不匹配时终止程序，并非对空指针的解引用。`snapshot->buf` 在调用前已通过 `xmalloc` 分配，若... |
| 2263 | git-2.50.1 | verify_absent | Dereference of null pointer | 2537 | FP | FP | 告警点检查的是指针 `o` 是否为 null，但在切片代码中，`o` 作为函数参数传入，并在多处被直接解引用（如 `o->skip_sparse_checkout`、`o->index_only` 等），且无前置空指针检查。这表明调用... |
| 2264 | git-2.50.1 | show_pack_info | Dereference of null pointer | 1784 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，否则保持为 NULL。在告警行使用 `chain_histogram` 前，存在条件判... |
| 2265 | git-2.50.1 | output | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `b_util = j < b->nr ? b->items[j].util : NULL;` 赋值，且外层循环... |
| 2267 | git-2.50.1 | limit_list | Dereference of null pointer | 1491 | FP | FP | 切片代码显示，在访问 `obj->flags` 之前，`obj` 已通过 `obj = &commit->object` 被正确赋值，且 `commit` 是从非空的 `original_list` 中通过 `pop_commit` ... |
| 2268 | git-2.50.1 | add_lines_to_move_detection | Dereference of null pointer | 1060 | FP | FP | 切片代码显示，在访问 entry_list[l->id] 之前，l->id 的值由条件分支确保被赋值，并且 ALLOC_GROW_BY 宏会确保 entry_list 数组被正确分配和初始化，因此不会发生空指针解引用。 |
| 2271 | git-2.50.1 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当 `strmap_get_entry` 返回 NULL 时，函数直接返回 `map->default_value`，没有对空指针进行解引用。告警是对控制流逻辑的误判。 |
| 2269 | git-2.50.1 | limit_list | Dereference of null pointer | 1487 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量来自 `pop_commit` 函数，该函数在栈非空时返回有效指针，在栈为空时返回 NULL。但在 while 循环条件 `while (original... |
| 2272 | git-2.50.1 | coalesce_lines | Dereference of null pointer | 251 | FP | FP | 在警告所在行（newend = newend->prev;）之前，代码已通过 while 循环条件 (i != 0 ｜｜ j != 0) 和 if (directions[i][j] == MATCH) 确保了进入该分支时 i 和 j... |
| 2274 | git-2.50.1 | assert_sane_strbuf | Dereference of null pointer | 35 | FP | FP | 切片代码显示告警点位于一个断言宏`cl_assert`内，该宏用于单元测试。`buf`指针在调用前应已被验证，且此断言旨在验证`strbuf`结构的内部不变性，是主动的完整性检查，而非对未经验证的空指针的盲目解引用。 |
| 2273 | git-2.50.1 | merge_ort_internal | Dereference of null pointer | 5277 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--` 之前，同一函数内存在对应的 `opt->priv->call_depth++` 操作，且该操作位于同一循环迭代内。这确保了 `opt->priv` 指针在递减前... |
| 2275 | git-2.50.1 | process_parents | Dereference of null pointer | 1174 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查确保指针 `p` 非空，且 `repo_parse_commit_gently` 调用失败时会 `continue`，因此 `p` 在后续使用中是有效的。告警为误报。 |
| 2278 | git-2.50.1 | clar_parse_args | Dereference of null pointer | 496 | FP | FP | 告警点位于 `explicit->suite_idx = j;`，变量 `j` 是循环计数器，其值由 `_clar_suite_count` 控制，不可能为 NULL。指针 `explicit` 在赋值前已通过 `calloc` 分配... |
| 2276 | git-2.50.1 | run_prepare_commit_msg_hook | Dereference of null pointer | 1352 | FP | FP | 告警点位于对 `msg->buf` 的访问，切片代码显示 `msg` 是函数参数且已作为指针传递，在调用 `write_message` 前未显式检查其是否为 NULL。然而，该函数是静态辅助函数，其调用方（未在切片中）很可能已确保 ... |
| 2277 | git-2.50.1 | gather_stats | Dereference of null pointer | 52 | FP | FP | 切片代码显示函数参数 `buf` 被直接用于数组索引 `buf[i]`，但函数签名表明 `buf` 是一个指针参数，其来源未知。然而，在循环访问 `buf[i]` 之前，代码通过 `if (size >= 1 && buf[size-... |
| 2282 | git-2.50.1 | add_lines_to_move_detection | Dereference of null pointer | 1063 | FP | FP | 切片代码显示，在访问 entry_list[l->id] 之前，l->id 的值由条件分支确保为有效索引（要么来自 hashmap 中已存在的条目，要么通过 ALLOC_GROW_BY 分配并递增），且 ALLOC_GROW_BY 宏... |
| 2284 | git-2.50.1 | coalesce_lines | Dereference of null pointer | 259 | FP | FP | 在警告所在行 `if (lline->prev)` 之前，`lline` 被赋值为 `newend`，而 `newend` 在循环中通过 `newend = newend->prev;` 更新，其值来自链表遍历，不会为 NULL。切片... |
| 2286 | git-2.50.1 | strvec_splice | Dereference of null pointer | 69 | FP | FP | 切片代码显示，在调用ALLOC_GROW宏后，数组`array->v`已被重新分配或确保有足够容量，因此对`array->v[array->nr + (replacement_len - len)]`的赋值是安全的，不会解引用空指针。 |
| 2287 | git-2.50.1 | <global> | Dereference of null pointer | 30 | FP | FP | 提供的切片代码仅为函数`is_absolute_path`的空声明，未包含任何实际执行逻辑或指针解引用操作，因此不存在空指针解引用问题。 |
| 2288 | git-2.50.1 | prepare_attr_stack | Dereference of null pointer | 978 | FP | FP | 在调用 `*stack = info->prev;` 之前，`info` 已通过 `info = *stack;` 赋值，而 `*stack` 在 `bootstrap_attr_stack` 函数中确保非空（若为空则初始化），因此 ... |
| 2291 | git-2.50.1 | <global> | Dereference of null pointer | 15 | FP | FP | 提供的切片代码仅为一个空函数定义，没有实际的指针解引用操作，因此不存在空指针解引用问题。 |
| 2290 | git-2.50.1 | get_nth_line | Dereference of null pointer | 879 | FP | FP | 切片代码显示，函数在line为0时直接返回data，否则返回data + ends[line] + 1。该逻辑本身不会导致空指针解引用，因为data和ends作为参数传入，其有效性由调用者保证。告警点仅涉及指针运算，并无直接的解引用操... |
| 2292 | git-2.50.1 | find_bisection | Dereference of null pointer | 440 | FP | FP | 在切片代码中，`list` 变量在 `best = do_find_bisection(...)` 之前通过 `list = last;` 被明确赋值，且 `last` 在循环中被初始化并更新，因此 `list` 不可能为 NULL。... |
| 2293 | git-2.50.1 | try_to_commit | Dereference of null pointer | 1570 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，工具认为 `current_head` 可能为 NULL 导致空指针解引用。但在切片代码中，该行位于 `if (fl... |
| 2295 | git-2.50.1 | verify_absent_1 | Dereference of null pointer | 2496 | FP | FP | 告警点 `ce->name` 的指针 `ce` 由函数参数传入，切片中调用该函数 `verify_absent_1` 的上下文缺失，无法确认 `ce` 是否为 NULL。但根据函数名和代码逻辑，`ce` 应为有效的缓存条目指针，且后续... |
| 2296 | git-2.50.1 | try_to_commit | Dereference of null pointer | 1686 | FP | FP | 告警指向的代码行 `commit_tree_extended(msg->buf, msg->len, &tree, parents, oid, author, committer, opts->gpg_sign, extra)` 中，... |
| 2299 | git-2.50.1 | cmp_local_packs | Dereference of null pointer | 509 | FP | FP | 切片代码显示，`local_packs` 是一个静态变量，在函数入口处被赋值给 `pl`。虽然其初始值为 NULL，但该函数是静态的，其调用上下文未知。在函数内部，对 `pl` 的访问（`pl->next`）仅在 `pl` 不为 NU... |
| 2298 | git-2.50.1 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点是对指针 `ce` 的成员 `name` 和 `ce_mode` 的访问，但 `ce` 是函数的形参，由调用方传入。在切片代码中，`ce` 本身没有显式的空值检查，但函数 `ce_path_match` 是一个内联辅助函数，其调... |
| 2301 | git-2.50.1 | tree_write_stack_finish_subtree | Dereference of null pointer | 679 | FP | FP | 在函数入口处，指针 `tws` 被解引用以访问 `tws->next`，但切片代码显示该函数仅在 `tws->next` 不为空（`if (n)`）时才执行后续可能解引用 `n` 的代码。告警点 `n = tws->next` 本身是... |
| 2302 | git-2.50.1 | unload_one_branch | Dereference of null pointer | 2066 | FP | FP | 在进入while循环前，条件`cur_active_branches && cur_active_branches >= max_active_branches`已确保`cur_active_branches`非零，因此`active... |
| 2303 | git-2.50.1 | apply_one_fragment | Dereference of null pointer | 2991 | FP | FP | 切片代码显示，在调用 `postimage.line[postimage.line_nr - 1].len--` 之前，已通过 `if (inaccurate_eof && old > oldlines && ... && newli... |
| 2304 | git-2.50.1 | process_entries | Dereference of null pointer | 4486 | FP | FP | 告警点位于一个BUG断言宏的调用路径中，该代码路径仅在内部一致性检查失败时触发，用于打印调试信息并终止程序，并非正常的程序逻辑。切片代码显示对`dir_metadata.offsets.items[0].util`的访问发生在条件判断... |
| 2305 | git-2.50.1 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过循环被填充，且 `remotes->nr == 1` 的条件保证了列表至少有一个... |
| 2306 | git-2.50.1 | clar_run_suite | Dereference of null pointer | 399 | FP | FP | 切片代码显示，在报告行`report->suite = _clar.active_suite;`之前，`report`指针已通过`calloc`分配并检查了是否为NULL，若分配失败会调用`clar_abort`退出程序，因此后续对`... |
| 2309 | git-2.50.1 | get_ref_map | Dereference of null pointer | 544 | FP | FP | 切片代码显示，在告警行`for (i = 0; i < fetch_refspec->nr; i++)`之前，`fetch_refspec`指针已通过条件判断被明确赋值为`&refmap`或`&remote->fetch`，两者均非空... |
| 2310 | git-2.50.1 | setup_scoreboard | Dereference of null pointer | 2842 | FP | FP | 告警点位于 while 循环条件 `c->parents` 的检查，但切片显示 `c` 被赋值为 `final_commit`，而 `final_commit` 仅在 `sb->reverse && sb->revs->first_p... |
| 2307 | git-2.50.1 | kwsprep | Dereference of null pointer | 507 | FP | FP | 告警位于循环 'for (curr = kwset->trie->next; curr; curr = curr->next)' 的初始化部分，其中 'kwset->trie' 在切片代码的早期逻辑分支中已被访问且未发现为空，且该循环... |
| 2312 | git-2.50.1 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `sb->buf[len]` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 确保 `sb->buf` 不是指向静态缓冲区 `strbuf_slopbuf` 的空指针或无效指针... |
| 2311 | git-2.50.1 | clear_snapshot_buffer | Dereference of null pointer | 185 | FP | FP | 告警点位于die_errno函数调用内部，该函数用于打印错误信息并终止程序，其参数访问snapshot->refs->path是在munmap调用失败后执行的错误处理路径。切片代码显示，在访问snapshot->refs之前，程序已通... |
| 2315 | git-2.50.1 | show_pack_info | Dereference of null pointer | 1806 | FP | FP | 切片代码显示，在循环访问 `chain_histogram[i]` 之前，已通过条件 `if (deepest_delta)` 检查，并在此条件下使用 `CALLOC_ARRAY` 为指针分配了内存。循环边界 `deepest_del... |
| 2317 | git-2.47.1 | add_parents_only | Dereference of null pointer | 1934 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且当 `revs->ignore_missing` 为真时... |
| 2316 | git-2.47.1 | image_remove_last_line | Dereference of null pointer | 362 | FP | FP | 切片代码显示，在访问 `img->line[img->line_nr - 1]` 之前，虽然没有显式的空指针检查，但函数 `image_remove_last_line` 的上下文（如函数名和操作）暗示 `img` 和 `img->l... |
| 2318 | git-2.47.1 | get_mode | Dereference of null pointer | 63 | FP | FP | 告警点 `*special = SPECIAL_STDIN;` 位于 `if (path == file_from_standard_input)` 分支内，该分支仅在 `path` 指向常量字符串 `"-"` 时执行，此时 `spe... |
| 2321 | git-2.47.1 | cwexec | Dereference of null pointer | 673 | FP | FP | 告警点 `d = delta[c = (end += d)[-1]];` 中，`end` 指针在循环条件 `while (lim - end >= d)` 和 `end += d` 操作下被严格约束，确保其不会超过 `lim` 边界，... |
| 2320 | git-2.47.1 | crlf_to_git | Dereference of null pointer | 582 | FP | FP | 告警点位于循环内，其条件 `while (--len)` 保证了在解引用 `src` 指针前，`len` 已通过前置检查 `if (src && !len)` 和循环递减确保大于零，且 `src` 在进入循环前已被验证非空或逻辑上可安... |
| 2322 | git-2.47.1 | diffcore_merge_broken | Dereference of null pointer | 295 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环已确保 `pp = q->queue[j]` 被赋值，且外层循环已处理了 `q->queue[i]` 为 NULL 的情况并跳过。切片代码的逻辑表明，在访问 `pp->brok... |
| 2323 | git-2.47.1 | parse_options_step | Dereference of null pointer | 906 | FP | FP | 告警点位于条件判断 `if (internal_help && *ctx->opt == 'h')`，其中 `ctx->opt` 在进入该分支前已通过 `ctx->opt = arg + 1` 赋值，且 `arg` 是 `ctx->a... |
| 2326 | git-2.47.1 | process_entry | Dereference of null pointer | 3413 | FP | FP | 告警点位于RENAME_ONE_FILE_TO_TWO分支内，该分支仅在ci->ren2不为NULL时才会执行。切片代码显示，在进入此分支前有'if (ci->ren2)'的断言，确保了ci->ren2的有效性，因此b->path的赋... |
| 2325 | git-2.47.1 | parse_options | Dereference of null pointer | 1052 | FP | FP | 告警点位于条件分支 `else if (isascii(*ctx.opt))`，但切片显示在进入该分支前，`ctx->opt` 已在 `parse_options_step` 函数中被显式重置为 `NULL`，且 `parse_opt... |
| 2327 | git-2.47.1 | verify_absent | Dereference of null pointer | 2534 | FP | FP | 告警点 `ce` 是函数参数，由调用方传入，在切片代码中未见其被赋值为 NULL 的逻辑。函数内对 `ce` 的访问（如 `ce->ce_flags`）均发生在参数非空的假设下，且无代码路径显示 `ce` 可能为空。该告警是基于静态推... |
| 2330 | git-2.47.1 | limit_list | Dereference of null pointer | 1497 | FP | FP | 告警指向的代码行 `if (obj->flags & UNINTERESTING)` 是对结构体成员 `flags` 的位操作，`obj` 指针在切片中已通过 `&commit->object` 明确赋值，且 `commit` 来自 ... |
| 2329 | git-2.47.1 | output | Dereference of null pointer | 550 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `b_util = j < b->nr ? b->items[j].util : NULL;` 赋值，且 `j ... |
| 2328 | git-2.47.1 | show_pack_info | Dereference of null pointer | 1689 | FP | FP | 切片代码显示，在访问 `chain_histogram` 数组前，已通过条件 `if (deepest_delta)` 进行保护，并调用了 `CALLOC_ARRAY(chain_histogram, deepest_delta)` ... |
| 2332 | git-2.47.1 | limit_list | Dereference of null pointer | 1493 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量来自 `pop_commit` 函数，该函数在栈非空时返回有效指针，在 `while (original_list)` 循环条件下，`original_l... |
| 2334 | git-2.47.1 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 切片代码显示，当 `result` 为 NULL 时，函数直接返回 `map->default_value`，并未对空指针进行解引用。告警的逻辑错误不成立。 |
| 2337 | git-2.47.1 | process_parents | Dereference of null pointer | 1180 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，且 `repo_parse_commit_gently` 调用失败时会 `continue`，不会执行到对 `p->parents` 的访... |
| 2336 | git-2.47.1 | merge_ort_internal | Dereference of null pointer | 5218 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--` 之前，`opt->priv->call_depth++` 已确保 `opt->priv` 不为空。该操作位于递归调用 `merge_ort_internal` ... |
| 2335 | git-2.47.1 | coalesce_lines | Dereference of null pointer | 264 | FP | FP | 在告警行 'newend = newend->prev;' 之前，代码已通过 'if (directions[i][j] == MATCH)' 条件确保进入该分支，且 'directions' 数组已通过 CALLOC_ARRAY 正... |
| 2338 | git-2.47.1 | run_prepare_commit_msg_hook | Dereference of null pointer | 1365 | FP | FP | 告警点位于对 `msg->buf` 的访问，但切片代码显示 `msg` 是函数参数，其来源未知。然而，该告警是空指针解引用，而 `msg->buf` 的访问发生在 `msg->len` 之后，若 `msg` 为 NULL，则 `msg... |
| 2339 | git-2.47.1 | gather_stats | Dereference of null pointer | 51 | FP | FP | 切片代码显示函数参数 `buf` 被直接用于数组索引访问 `buf[i]`，但函数签名表明 `buf` 是一个指针参数，其有效性由调用者保证。在函数内部循环中，访问前通过 `i < size` 和 `i+1 < size` 等条件确保... |
| 2342 | git-2.47.1 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码显示对数组指针 `array->v` 进行了直接解引用，但函数名 `strvec_push_nodup` 暗示这是一个内部数据结构操作函数，通常由调用者保证 `array` 及其内部数组 `v` 已正确初始化且容量足够。切片内... |
| 2343 | git-2.47.1 | add_lines_to_move_detection | Dereference of null pointer | 1062 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，并与数组大小... |
| 2345 | git-2.47.1 | coalesce_lines | Dereference of null pointer | 272 | FP | FP | 告警指向的代码行 `lline->prev->next = lline->next;` 受前一行 `if (lline->prev)` 的保护，仅在 `lline->prev` 非空时才会解引用，因此不会发生空指针解引用。 |
| 2346 | git-2.47.1 | try_to_commit | Dereference of null pointer | 1699 | FP | FP | 告警点位于 commit_tree_extended 函数调用处，该函数内部已对传入的 msg 参数进行空字节检查（memchr(msg, '\0', msg_len)），若存在空字节会提前返回错误，因此不会发生空指针解引用。切片代码... |
| 2347 | git-2.47.1 | prepare_attr_stack | Dereference of null pointer | 1013 | FP | FP | 在调用 `*stack = info->prev;` 之前，`info` 被赋值为 `*stack`，而 `*stack` 由 `bootstrap_attr_stack` 函数初始化，该函数确保 `*stack` 不为空（若为空则进... |
| 2350 | git-2.47.1 | <global> | Dereference of null pointer | 13 | FP | FP | 提供的切片代码仅为一个空函数定义，函数体为空，不存在任何指针解引用操作，因此工具报告的'空指针解引用'逻辑错误不成立。 |
| 2351 | git-2.47.1 | find_bisection | Dereference of null pointer | 439 | FP | FP | 在调用 `list->item = best->item;` 之前，代码已通过 `if (best)` 检查了 `best` 指针非空，且 `list` 在循环中被正确初始化并赋值，因此不存在空指针解引用。 |
| 2349 | git-2.47.1 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 切片代码显示，函数在访问 `ends[line]` 前已通过 `if (line == 0)` 分支处理了索引为0的情况。对于 `line > 0` 的情况，`ends` 数组的边界和有效性依赖于调用方传入的 `ends` 和 `da... |
| 2352 | git-2.47.1 | <global> | Dereference of null pointer | 1537 | FP | FP | 告警点位于检查策略属性的条件判断语句中，`use_strategies` 数组及其元素在切片中已通过 `add_strategies` 函数初始化，访问前有明确的空指针检查（`if (!use_strategies)`），因此不会发生... |
| 2353 | git-2.47.1 | verify_absent_1 | Dereference of null pointer | 2493 | FP | FP | 告警点 `ce->name` 的指针 `ce` 由函数参数传入，在切片代码中，`ce` 在调用 `ce_namelen` 和 `submodule_from_ce` 等函数时已被安全解引用，表明其不为空。工具可能未能正确推断函数调用上... |
| 2355 | git-2.47.1 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点是对函数`match_pathspec`的调用，其参数`ce`来自函数参数且被直接使用。切片代码显示`ce`被用于宏`ce_namelen`和访问`ce->name`、`ce->ce_mode`，但没有任何证据表明`ce`可能为... |
| 2357 | git-2.47.1 | tree_write_stack_finish_subtree | Dereference of null pointer | 677 | FP | FP | 代码在解引用指针 'n' 之前，已通过 'if (n)' 进行了明确的非空检查，确保了指针的有效性，因此不存在空指针解引用问题。 |
| 2354 | git-2.47.1 | try_to_commit | Dereference of null pointer | 1583 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，工具认为 `current_head` 可能为 NULL 导致空指针解引用。但在切片代码中，该行位于 `if (fl... |
| 2358 | git-2.47.1 | unload_one_branch | Dereference of null pointer | 2049 | FP | FP | 在进入while循环前，条件`cur_active_branches && cur_active_branches >= max_active_branches`确保了`cur_active_branches`大于0，因此`activ... |
| 2361 | git-2.47.1 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已在循环中被填充，且 `remotes->nr == 1` 的条件保证了列表至少有一个... |
| 2360 | git-2.47.1 | process_entries | Dereference of null pointer | 4452 | FP | FP | 告警点位于BUG宏调用前的错误信息打印代码中，该代码仅在程序检测到内部状态不一致（dir_metadata.offsets.nr != 1）时执行，属于错误处理路径。对items[0].util的访问已通过前置条件检查offsets.... |
| 2359 | git-2.47.1 | apply_one_fragment | Dereference of null pointer | 2987 | FP | FP | 切片代码中，在访问 `postimage.line[postimage.line_nr - 1]` 之前，`postimage.line_nr` 已通过 `image_add_line` 函数递增，且 `postimage.line`... |
| 2364 | git-2.47.1 | setup_scoreboard | Dereference of null pointer | 2841 | FP | FP | 在while循环条件`c->parents`之前，`final_commit`已通过`find_single_final`函数赋值，且该函数在切片中可见，其逻辑保证了返回有效指针或调用`die`终止程序，因此`c`不为空。告警为误报。 |
| 2365 | git-2.47.1 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 代码在访问 `sb->buf[len]` 前已通过 `if (sb->buf != strbuf_slopbuf)` 检查，确保 `sb->buf` 不为空指针。`strbuf_slopbuf` 是一个静态的空缓冲区，该条件逻辑保证了... |
| 2362 | git-2.47.1 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警指向的代码行 'curr = kwset->trie->next' 位于一个循环条件中，该循环仅在 'curr' 非空时执行。切片显示 'kwset->trie' 在函数入口处被赋值给 'curr' 和 'last'，并在后续的 ... |
| 2363 | git-2.47.1 | get_ref_map | Dereference of null pointer | 546 | FP | FP | 切片代码显示，在告警行`for (i = 0; i < fetch_refspec->nr; i++)`之前，`fetch_refspec`指针已通过条件判断被明确赋值为`&refmap`或`&remote->fetch`，两者均非空... |
| 2368 | git-2.47.1 | show_pack_info | Dereference of null pointer | 1711 | FP | FP | 切片代码显示，在访问 `chain_histogram[i]` 之前，已通过 `if (deepest_delta)` 条件判断，并在条件成立时通过 `CALLOC_ARRAY` 为指针分配了内存。循环条件 `i < deepest_... |
| 2371 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警行 `so = pmatch[bt].rm_so;` 访问 `pmatch` 数组前，代码已通过 `if (tnfa->num_submatches)` 检查并分配了内存，且 `bt` 是来自 `trans_i->u.backre... |
| 2372 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在访问 `tags[*next_tags]` 之前，`next_tags` 指针已通过 `if (next_tags)` 检查非空，且循环条件 `*next_tags >= 0` 确保指针解引用时索引值有效。此外，`ta... |
| 2369 | musl-1.2.1 | iconv | Dereference of null pointer | 373 | FP | FP | 告警指向的代码行 `case 'J': scd->state=1; continue;` 是对 `scd->state` 的赋值，而非解引用。在切片代码中，`scd` 仅在 `if (!((size_t)cd & 1))` 为真时被赋... |
| 2373 | musl-1.2.1 | do_relocs | Dereference of null pointer | 435 | FP | FP | 告警指向的代码行位于switch-case的REL_COPY分支，该分支仅在def.sym和sym_val有效时执行memcpy，而切片代码显示sym_val的计算已检查def.sym是否为非空，且sym_val来自laddr函数，该... |
| 2374 | musl-1.2.1 | iconv | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在switch语句中使用scd->state前，已通过条件判断确保scd不为空指针（当cd为偶数时scd被赋值），且state字段的访问位于scd被初始化的代码路径内。因此，不存在对空指针的解引用。 |
| 2377 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用 next_tags 指针前，存在 'if (next_tags)' 的条件检查，确保指针非空。因此，该解引用操作是安全的，属于静态分析工具的误报。 |
| 2378 | musl-1.2.1 | iconv | Dereference of null pointer | 374 | FP | FP | 告警指向的代码行位于switch-case语句的注释行（case 'I': scd->state=4; continue;  // The line where the warning is located），该行是注释，不包含任何可... |
| 2375 | musl-1.2.1 | iconv | Dereference of null pointer | 372 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件判断 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`。当 `cd` 的最低有效位为 1 时，`scd` 保持为 0（NULL）... |
| 2379 | musl-1.2.1 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].so_tag]` 之前，已通过 `if (submatch_data[i].so_tag == tnfa->end_tag)` 条件判断，确保 `so_tag` 不等... |
| 2383 | musl-1.2.1 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 条件判断，确保仅在 `eo_tag` ... |
| 2382 | musl-1.2.1 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点位于条件判断 `if (!scd->state)` 中，但根据切片代码，当执行到该分支时，`scd` 指针已在函数开头通过 `scd = (void *)cd;` 被正确赋值（前提是 `cd` 的最低有效位为0）。因此，只要 `... |
| 2381 | musl-1.2.1 | iconv | Dereference of null pointer | 375 | FP | FP | 告警指向的代码行 `scd->state=2;` 位于 `ISO2022_JP` 编码处理的 `switch` 分支中，该分支仅在 `scd` 指针非空时才会执行。切片代码显示，`scd` 仅在 `if (!((size_t)cd &... |
| 2384 | musl-1.2.1 | queue_ctors | Dereference of null pointer | 1452 | FP | FP | 在告警行访问 `p->deps[p->next_dep]` 之前，代码逻辑已通过 `while (p->next_dep < p->ndeps_direct)` 确保索引 `p->next_dep` 在数组 `p->deps` 的有效... |
| 2387 | musl-1.2.1 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警指向的代码行 `regset = xmalloc(...)` 在调用前已通过 `if (regset == NULL)` 检查了返回值，后续使用前也进行了空指针检查。切片代码中未发现对空指针的直接解引用，工具可能误判了控制流或数据流。 |
| 2385 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，存在 `if (stack->prev)` 条件检查，确保 `stack` 不为空；同时，`states_seen` 数组在函数开头已... |
| 2386 | musl-1.2.1 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于switch-case语句的标签位置（case 128+'B':），该行是标签而非可执行语句，不会发生空指针解引用。切片代码显示scd指针在进入该分支前已通过条件检查确保非空或状态有效，因此该告警为误报。 |
| 2388 | musl-1.2.4 | iconv | Dereference of null pointer | 373 | FP | FP | 告警指向的代码行 `case 'J': scd->state=1; continue;` 是对 `scd->state` 的赋值操作，并非解引用。切片代码显示 `scd` 指针在函数入口处已通过条件 `if (!((size_t)cd... |
| 2391 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，已通过 `if (next_tags)` 进行了空指针检查，因此不会发生空指针解引用。 |
| 2390 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警行 `so = pmatch[bt].rm_so;` 访问 `pmatch` 数组，但切片代码显示 `pmatch` 已通过 `xmalloc` 分配内存，且 `bt` 索引值 `trans_i->u.backref` 源自有限状... |
| 2392 | musl-1.2.4 | do_relocs | Dereference of null pointer | 484 | FP | FP | 告警指向的代码行位于switch-case的REL_COPY分支，该分支仅在sym_val和sym->st_size有效时执行memcpy。切片代码显示，sym_val由def.sym计算而来，而def.sym在之前的逻辑中已被检查（... |
| 2393 | musl-1.2.4 | iconv | Dereference of null pointer | 380 | FP | FP | 告警指向的代码行位于switch语句内部，该语句在多个case分支中处理scd->state变量。切片代码显示，在进入该switch语句前，scd指针仅在特定条件（(size_t)cd & 1为假）下被赋值，且该条件在函数入口处已检查... |
| 2395 | musl-1.2.4 | do_relocs | Dereference of null pointer | 519 | FP | FP | 在警告行`if (def.dso->tls_id > static_tls_cnt)`之前，存在对`def.sym`的检查（`if (!def.sym)`），并且当`def.sym`为空时，`def.dso`被明确赋值为`dso`。因... |
| 2396 | musl-1.2.4 | do_relocs | Dereference of null pointer | 458 | FP | FP | 告警点位于一个条件判断分支内，该分支在条件满足时会调用error函数并执行longjmp跳转，不会发生空指针解引用。切片代码显示reloc_addr由laddr函数计算返回，该函数逻辑保证了返回值非空（返回p->base + v或有效... |
| 2394 | musl-1.2.4 | iconv | Dereference of null pointer | 372 | FP | FP | 告警指向的代码行 `case 'B': scd->state=0; continue;` 是对 `scd->state` 的赋值操作，而非解引用。切片代码显示 `scd` 指针在函数入口处已通过条件 `if (!((size_t)cd... |
| 2398 | musl-1.2.4 | do_relocs | Dereference of null pointer | 500 | FP | FP | 在REL_DTPMOD分支中，`def.dso`被赋值为`dso`（见`sym_index`为0时的`else`分支），因此`def.dso->tls_id`的访问是安全的，不会解引用空指针。 |
| 2399 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，存在 `if (next_tags)` 的条件检查，确保指针非空。因此，该解引用操作是安全的，属于静态分析工具的误报。 |
| 2400 | musl-1.2.4 | iconv | Dereference of null pointer | 374 | FP | FP | 切片代码显示，在访问 scd->state 之前，已通过条件 `if (!((size_t)cd & 1))` 确保 scd 被正确初始化，且后续仅在 scd 非空时才使用其 state 字段。因此，不存在对空指针的解引用。 |
| 2401 | musl-1.2.4 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].so_tag]` 之前，`tags` 指针已在函数参数中传入，且其有效性由调用方保证。同时，循环条件 `i < tnfa->num_submatches && i <... |
| 2403 | musl-1.2.4 | iconv | Dereference of null pointer | 375 | FP | FP | 告警指向的代码行 `scd->state=2;` 位于 `ISO2022_JP` 编码处理的 `switch` 分支内，该分支仅在 `scd` 指针非空时才会执行。切片代码显示，`scd` 仅在 `if (!((size_t)cd &... |
| 2406 | musl-1.2.4 | queue_ctors | Dereference of null pointer | 1553 | FP | FP | 切片代码显示，在访问 `p->deps[p->next_dep]` 之前，`p` 来自 `stack`，而 `stack` 指向 `queue`，`queue` 中的元素（如 `dso`）已通过 `stack[--spos] = ds... |
| 2405 | musl-1.2.4 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 条件判断，确保仅在 `eo_tag` ... |
| 2404 | musl-1.2.4 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点位于条件判断 `if (!scd->state)` 中，但根据切片代码，`scd` 仅在 `if (!((size_t)cd & 1))` 为真时才被赋值为非空指针。当 `cd` 的最低有效位为1时，`scd` 保持初始值0，此... |
| 2407 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 在调用 `states_seen[stack->item.state_id] = 0;` 之前，代码已通过 `if (stack->prev)` 检查确保 `stack` 不为空，且 `stack->item.state` 和 `st... |
| 2409 | musl-1.2.4 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警行代码 `regset = xmalloc(sizeof(*regset) * ((tnfa->num_submatches + 1) * 2));` 中，`tnfa` 指针在函数开头已通过 `first_pass = (mem ... |
| 2408 | musl-1.2.4 | iconv | Dereference of null pointer | 376 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，已通过条件 `if (!((size_t)cd & 1))` 检查并确保 `scd` 被正确赋值。当 `cd` 为偶数时，`scd` 被赋值为 `(void *)cd`，此时 `s... |
| 2413 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，存在 `if (next_tags)` 的条件检查，确保指针非空后才进行循环访问，因此不会发生空指针解引用。 |
| 2410 | musl-1.1.24 | iconv | Dereference of null pointer | 373 | FP | FP | 告警指向的代码行 `case 'J': scd->state=1; continue;` 是对 `scd->state` 的赋值，而非解引用。`scd` 指针在函数入口处已通过条件 `if (!((size_t)cd & 1)) { ... |
| 2412 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 切片代码显示，在访问 `pmatch[bt].rm_so` 之前，`pmatch` 已通过 `xmalloc` 分配内存，且 `bt` 是 `trans_i->u.backref`，其值受限于 `tnfa->num_submatche... |
| 2414 | musl-1.1.24 | do_relocs | Dereference of null pointer | 430 | FP | FP | 告警指向的代码行位于switch-case的REL_COPY分支，该分支仅在`def.sym`和`sym_val`有效时执行`memcpy`。切片代码显示，`def.sym`在进入此分支前已通过`if (!def.sym && ...... |
| 2416 | musl-1.1.24 | iconv | Dereference of null pointer | 372 | FP | FP | 在ISO2022_JP编码处理分支中，对scd->state的赋值发生在scd指针被显式初始化为非空之后（通过条件`if (!((size_t)cd & 1)) { scd = (void *)cd; }`），且该分支仅在`type`... |
| 2418 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，存在 `if (next_tags)` 的条件检查，确保指针非空。因此，该行代码不会发生空指针解引用。 |
| 2415 | musl-1.1.24 | iconv | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在switch语句中访问scd->state之前，scd指针仅在条件`if (!((size_t)cd & 1))`为真时被赋值，否则保持为0。然而，在switch语句所在的case ISO2022_JP中，只有当`sc... |
| 2420 | musl-1.1.24 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `if (match_eo >= 0 && !(cflags & REG_NOSUB))` 条件确保函数仅在有效匹配时执行，且 `submatch_data[i].so_tag` 和... |
| 2419 | musl-1.1.24 | iconv | Dereference of null pointer | 374 | FP | FP | 告警指向的代码行 `case 'I': scd->state=4; continue;` 是对 `scd->state` 的赋值操作，并非解引用。切片代码显示 `scd` 指针在函数入口处已通过条件 `if (!((size_t)cd... |
| 2422 | musl-1.1.24 | iconv | Dereference of null pointer | 375 | FP | FP | 告警指向的代码行 `scd->state=2;` 位于 `ISO2022_JP` 编码处理的 switch-case 分支中，该分支仅在 `scd` 非空时可达。切片代码显示，`scd` 仅在 `if (!((size_t)cd & ... |
| 2425 | musl-1.1.24 | queue_ctors | Dereference of null pointer | 1447 | FP | FP | 在警告行之前，代码已通过 `if (!queue)` 检查了 `queue` 的分配结果，并在分配失败时通过 `error` 和 `longjmp` 提前返回，因此 `stack = queue;` 执行时 `queue` 不可能为空... |
| 2424 | musl-1.1.24 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 条件判断，确保仅在 `eo_tag` ... |
| 2423 | musl-1.1.24 | iconv | Dereference of null pointer | 300 | FP | FP | 告警位于条件分支 `if (!scd->state)` 中，但切片代码显示 `scd` 在函数入口处已通过 `if (!((size_t)cd & 1))` 检查并可能被赋值为非空指针。当 `cd` 为奇数时 `scd` 保持为0，但... |
| 2426 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，存在 `if (stack->prev)` 条件检查，确保 `stack` 不为空。此外，`states_seen` 数组在函数开头已... |
| 2427 | musl-1.1.24 | iconv | Dereference of null pointer | 376 | FP | FP | 告警位于switch case标签行（case 128+'B':），该行不涉及任何指针解引用操作。代码逻辑是检查转义序列以设置状态，不存在空指针解引用。 |
| 2428 | musl-1.1.24 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 切片代码显示，在告警行`regset = xmalloc(...)`之前，`tnfa`指针已在条件`first_pass = (mem == NULL ｜｜ tnfa == NULL)`中被检查，且后续代码中`tnfa`被直接解引用（... |
| 2432 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，已通过 `if (next_tags)` 进行了空指针检查，因此不会发生空指针解引用。 |
| 2431 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警行 'so = pmatch[bt].rm_so;' 访问的 pmatch 指针在 tnfa->num_submatches 非零时已通过 xmalloc 分配内存，且索引 bt 来自 trans_i->u.backref，在正常... |
| 2429 | musl-1.2.3 | iconv | Dereference of null pointer | 373 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，存在条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }`，当 `cd` 的最低有效位为 1 时，`scd` 保持为 0（NULL）。告... |
| 2433 | musl-1.2.3 | do_relocs | Dereference of null pointer | 440 | FP | FP | 切片代码显示，在调用memcpy前已通过条件判断确保sym和sym_val有效（sym_val来自def.sym，而def.sym在sym_index非零时已通过find_sym查找或设为本地符号，且当def.sym为空时sym_va... |
| 2434 | musl-1.2.3 | iconv | Dereference of null pointer | 380 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，已通过条件 `if (!((size_t)cd & 1))` 检查了 `cd` 的有效性，并仅在条件为真时将 `scd` 指向 `cd`。对于 `ISO2022_JP` 编码处理，... |
| 2437 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，存在 `if (next_tags)` 的条件检查，确保指针非空。因此，该行代码不会发生空指针解引用。 |
| 2435 | musl-1.2.3 | iconv | Dereference of null pointer | 372 | FP | FP | 在ISO2022_JP编码处理分支中，对scd指针的访问（scd->state）受条件'if (!scd->state)'保护。告警行位于'switch (128*(c=='$') + d)'的case 'B'分支，该分支仅设置scd... |
| 2438 | musl-1.2.3 | iconv | Dereference of null pointer | 374 | FP | FP | 告警指向的代码行 `case 'I': scd->state=4; continue;` 位于 switch 语句内，该语句在 `scd` 指针非空时才会执行。切片代码显示 `scd` 仅在 `if (!((size_t)cd & 1... |
| 2439 | musl-1.2.3 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].so_tag]` 之前，循环条件 `i < tnfa->num_submatches && i < nmatch` 确保了索引 `i` 在有效范围内，且 `subma... |
| 2442 | musl-1.2.3 | iconv | Dereference of null pointer | 300 | FP | FP | 切片代码显示，在访问 scd->state 之前，函数开头已通过条件判断确保当 cd 为偶数时 scd 被正确赋值，且 scd 指向有效的 stateful_cd 结构体。因此，在 case UCS2/UTF_16 分支中访问 scd... |
| 2441 | musl-1.2.3 | iconv | Dereference of null pointer | 375 | FP | FP | 切片代码显示，在访问 scd->state 之前，已通过条件 `if (!((size_t)cd & 1)) { scd = (void *)cd; }` 确保 scd 仅在 cd 为有效状态转换描述符时才被赋值，否则 scd 保持为... |
| 2443 | musl-1.2.3 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 条件判断，确保仅在 `eo_tag` ... |
| 2444 | musl-1.2.3 | queue_ctors | Dereference of null pointer | 1487 | FP | FP | 告警点位于条件判断 `if (p->deps[p->next_dep]->mark)` 中，但根据切片代码的上下文，`p` 在循环中由 `stack[spos++]` 赋值，而 `stack` 初始时已确保包含有效的 `dso` 指针... |
| 2445 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，存在 `if (stack->prev)` 检查，确保 `stack` 不为空，且 `stack->item.state` 的访问表明... |
| 2447 | musl-1.2.3 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 切片代码显示，在调用xmalloc分配内存后，立即检查了返回值regset是否为NULL，并在为NULL时返回错误码REG_ESPACE，因此不会发生空指针解引用。 |
| 2446 | musl-1.2.3 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于switch-case语句中，该行仅对scd->state进行赋值，而scd指针在函数入口处已通过条件判断确保非空（当cd为偶数时scd被赋值为(void*)cd，否则为0）。在调用该行的代码路径上，scd已被验证... |
| 2448 | musl-1.2.2 | iconv | Dereference of null pointer | 373 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，已通过条件 `if (!((size_t)cd & 1))` 检查了 `cd` 的有效性，并仅在条件为真时将 `scd` 赋值为非空指针。对于 `ISO2022_JP` 等需要 `... |
| 2451 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，已通过 `if (next_tags)` 进行了非空检查，因此不会发生空指针解引用。 |
| 2450 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警行 `so = pmatch[bt].rm_so;` 中，`pmatch` 指针在 `tnfa->num_submatches` 非零时已通过 `xmalloc` 分配，且 `bt` 是来自 `trans_i->u.backref... |
| 2452 | musl-1.2.2 | do_relocs | Dereference of null pointer | 440 | FP | FP | 告警指向的代码行位于switch-case的REL_COPY分支，该分支仅在`def.sym`和`sym`有效时执行。切片代码显示，在进入此分支前，`def.sym`和`sym`已通过条件检查（如`sym_index`判断），且`me... |
| 2454 | musl-1.2.2 | iconv | Dereference of null pointer | 372 | FP | FP | 告警点位于switch语句的case标签行，该行仅用于设置状态变量，不涉及任何指针解引用操作。切片代码显示scd指针在解引用前已通过条件判断确保非空，逻辑错误告警不成立。 |
| 2453 | musl-1.2.2 | iconv | Dereference of null pointer | 380 | FP | FP | 告警位于switch(scd->state)语句，但切片代码显示scd仅在cd为偶数时被赋值，且state字段在UCS2/UTF_16/UTF_32等分支中被显式初始化。在ISO2022_JP分支中，state在遇到转义序列时被设置，... |
| 2456 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 切片代码显示，在解引用 `next_tags` 指针前，已通过 `if (next_tags)` 条件进行了检查，确保指针非空。因此，该处解引用是安全的，属于静态分析工具的误报。 |
| 2458 | musl-1.2.2 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].so_tag]` 之前，已通过 `if (submatch_data[i].so_tag == tnfa->end_tag)` 进行条件判断，且 `tags` 数组的... |
| 2457 | musl-1.2.2 | iconv | Dereference of null pointer | 374 | FP | FP | 告警指向的代码行 `case 'I': scd->state=4; continue;` 是对 `scd->state` 的赋值，而非解引用。切片代码显示 `scd` 在函数入口处已通过条件 `if (!((size_t)cd & 1... |
| 2459 | musl-1.2.2 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，对数组`tag_directions`的访问发生在条件`IS_TAG(lit) && (flags & COPY_MAXIMIZE_FIRST_TAG) && first_tag`为真时，且索引`max`的值在之前的代码... |
| 2460 | musl-1.2.2 | iconv | Dereference of null pointer | 375 | FP | FP | 告警指向的代码行（case 128+'@': scd->state=2; continue;）位于switch语句内，该语句已通过前置条件确保scd指针非空（scd = (void *)cd; 且cd的有效性已在函数入口检查），因此对... |
| 2462 | musl-1.2.2 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 条件判断，确保仅在 `eo_tag` 不... |
| 2464 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，已通过 `if (stack->prev)` 检查确保 `stack` 不为空，且 `states_seen` 数组在函数开头已根据 ... |
| 2463 | musl-1.2.2 | queue_ctors | Dereference of null pointer | 1486 | FP | FP | 切片代码显示，在访问 `p->deps[p->next_dep]` 之前，`p` 已通过 `stack[--spos] = dso;` 和 `p = stack[spos++];` 被赋值，且 `dso` 作为函数参数非空。同时，`w... |
| 2461 | musl-1.2.2 | iconv | Dereference of null pointer | 300 | FP | FP | 在切片代码中，scd指针仅在条件`!((size_t)cd & 1)`为真时被赋值，否则保持为0。告警点`if (!scd->state)`位于`case UCS2:`或`case UTF_16:`分支内，而这两个分支仅在`type`... |
| 2466 | musl-1.2.2 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警指向的代码行 `regset = xmalloc(...)` 在切片中可见其返回值被立即检查是否为 NULL，并在为 NULL 时返回错误码 `REG_ESPACE`，因此不会发生空指针解引用。 |
| 2467 | tmux-3.3 | recalculate_sizes_now | Dereference of null pointer | 458 | FP | FP | 在告警行访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已对 `c->session` 是否为 NULL 进行了检查，若为 NULL 则直接 `continue`，确保了后续访问 `s... |
| 2465 | musl-1.2.2 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行 `scd->state=3;` 位于 `if (!((size_t)cd & 1)) { scd = (void *)cd; }` 条件块之后，该条件确保当 `cd` 的最低有效位为0时，`scd` 才被赋值为非空指... |
| 2469 | tmux-3.3 | window_copy_search | Dereference of null pointer | 3674 | FP | FP | 在访问 `data->searchmark[at]` 之前，代码已通过 `window_copy_search_mark_at(data, fx, fy, &at) == 0` 检查了 `at` 的有效性，并且 `window_cop... |
| 2468 | tmux-3.3 | mode_tree_draw | Dereference of null pointer | 750 | FP | FP | 告警指向的代码行 `xasprintf(&text, " %s (sort: %s%s)", mti->name, ...);` 中，`mti` 指针在切片代码中已被多次解引用且已通过 `mti = line->item;` 赋值，`... |
| 2470 | tmux-3.3 | grid_string_cells | Dereference of null pointer | 1013 | FP | FP | 告警点位于函数调用 `grid_string_cells_code(*lastgc, ...)`，但在调用前，代码已通过条件 `if (lastgc != NULL && *lastgc == NULL)` 确保 `*lastgc` ... |
| 2471 | tmux-3.3 | mode_tree_draw | Dereference of null pointer | 754 | FP | FP | 告警指向的 `xasprintf(&text, " %s", mti->name);` 行，其参数 `mti` 已在前面通过 `mti = line->item;` 赋值，且 `line` 来自 `mtd->line_list[mtd... |
| 2475 | tmux-3.3 | input_parse | Dereference of null pointer | 907 | FP | FP | 在访问 `ictx->state->transitions` 之前，代码已通过 `if` 条件确保 `ictx->state` 不为 NULL，且当 `itr->first` 或 `itr->last` 为 -1 时，程序会调用 `f... |
| 2476 | tmux-3.2 | recalculate_sizes_now | Dereference of null pointer | 367 | FP | FP | 在访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已检查 `c->session` 是否为 NULL，若为 NULL 则提前返回，确保了后续 `s = c->session` 中的 `... |
| 2477 | tmux-3.2 | mode_tree_draw | Dereference of null pointer | 753 | FP | FP | 告警点位于xasprintf调用，其参数mti->name来自切片中已明确赋值的结构体成员，且mti指针在多个前置条件检查（如mti->key == KEYC_NONE）中已被安全解引用，不存在空指针解引用风险。 |
| 2474 | tmux-3.3 | server_client_reset_state | Dereference of null pointer | 2340 | FP | FP | 告警点位于条件判断 'wp->xoff + s->cx >= ox' 中，涉及指针 s 的解引用。切片代码显示，在告警行之前，s 被赋值为 wp->screen（当 c->overlay_draw 为 NULL 时），而 wp 通过 ... |
| 2478 | tmux-3.2 | window_copy_search | Dereference of null pointer | 3183 | FP | FP | 在访问 data->searchmark[at] 之前，代码已通过 window_copy_search_mark_at(data, fx, fy, &at) == 0 检查了 at 的有效性，并确保 data->searchmark... |
| 2480 | tmux-3.2 | grid_string_cells | Dereference of null pointer | 983 | FP | FP | 告警点位于函数调用 `grid_string_cells_code(*lastgc, ...)`，工具认为 `*lastgc` 可能为空指针。但在切片代码中，函数开头有明确的防护逻辑：当 `lastgc != NULL && *las... |
| 2481 | tmux-3.2 | mode_tree_draw | Dereference of null pointer | 757 | FP | FP | 告警点位于 `xasprintf(&text, " %s", mti->name);`，其中 `mti` 指针在切片代码中已通过 `mti = line->item;` 和 `if (mti->draw_as_parent) mti ... |
| 2484 | tmux-3.2 | server_client_reset_state | Dereference of null pointer | 1672 | FP | FP | 告警行访问的指针 's' 在切片代码中已被检查并确保非空。在 'c->overlay_draw == NULL' 的分支中，'s' 被赋值为 'wp->screen'，而 'wp' 来自 'server_client_get_pane... |
| 2485 | tmux-3.2 | input_parse | Dereference of null pointer | 902 | FP | FP | 在访问 `ictx->state->transitions` 之前，代码逻辑已通过 `if` 条件确保 `ictx->state` 不为 NULL，且 `fatalx` 函数会在 `itr->first` 或 `itr->last` ... |
| 2486 | tmux-3.1 | spawn_window | Dereference of null pointer | 185 | FP | FP | 切片代码显示，在调用 `format_single` 函数前，已通过条件 `if (sc->name != NULL)` 检查了 `sc->name` 指针，确保其非空后才进行调用，因此不会发生空指针解引用。 |
| 2487 | tmux-3.1 | grid_string_cells | Dereference of null pointer | 927 | FP | FP | 告警点位于函数 `grid_string_cells_code` 的调用处，其参数 `*lastgc` 在调用前已被检查并确保非空。当 `lastgc != NULL && *lastgc == NULL` 时，代码会将其指向静态变量... |
| 2489 | tmux-3.1 | grid_reflow_join | Dereference of null pointer | 1126 | FP | FP | 切片代码显示，在访问 `from` 指针前，`from` 已在循环中被赋值为 `&gd->linedata[line]`，且循环条件 `lines == 0` 时函数已提前返回，因此 `from` 在 `left = from->ce... |
| 2493 | tmux-3.1 | recalculate_sizes | Dereference of null pointer | 387 | FP | FP | 在调用`s->statuslines`之前，`ignore_client_size(c)`函数已检查`c->session`是否为NULL，并且只有当`c->session`非NULL时才会跳过该客户端。因此，当代码执行到使用`s`（... |
| 2491 | tmux-3.1 | spawn_window | Dereference of null pointer | 189 | FP | FP | 告警点位于 `w->name = xstrdup(default_window_name(w));`，工具认为 `w` 可能为空指针。切片代码显示，在告警点之前的 `if (~sc->flags & SPAWN_RESPAWN)` 分... |
| 2494 | tmux-3.0 | grid_string_cells | Dereference of null pointer | 918 | FP | FP | 切片代码显示，在调用 `grid_string_cells_code(*lastgc, ...)` 之前，函数开头已通过条件判断 `if (lastgc != NULL && *lastgc == NULL)` 将 `*lastgc`... |
| 2495 | tmux-3.0 | spawn_window | Dereference of null pointer | 183 | FP | FP | 告警点位于 `w->name = xstrdup(sc->name);`，工具认为 `w` 可能为空指针。切片代码显示，在告警点之前，`w` 已在多个分支中被赋值（例如 `w = sc->wl->window;` 或通过 `windo... |
| 2500 | tmux-3.0 | options_array_set | Dereference of null pointer | 368 | FP | FP | 在`CMD_PARSE_EMPTY`分支中，对`*cause`的赋值仅在`cause != NULL`的父条件（第10行）为真时才可能执行，切片代码已显示该条件，因此不会发生空指针解引用。 |
| 2498 | tmux-3.0 | spawn_window | Dereference of null pointer | 186 | FP | FP | 告警点位于 `w->name = xstrdup(default_window_name(w));`，工具认为 `w` 可能为空指针。但在切片代码中，当执行到该行时，`w` 仅在 `if (~sc->flags & SPAWN_RES... |
| 2501 | tmux-3.4 | recalculate_sizes_now | Dereference of null pointer | 458 | FP | FP | 在访问 s->statuslines 之前，代码通过 TAILQ_FOREACH 遍历 clients，并且对每个 client c，其关联的 session s 在 ignore_client_size 函数中已进行空指针检查（c-... |
| 2502 | tmux-3.4 | mode_tree_draw | Dereference of null pointer | 750 | FP | FP | 告警点位于xasprintf调用，该函数内部已对内存分配失败进行处理（调用fatalx），不会返回NULL指针。切片代码显示mti->name是结构体成员，其来源虽未在切片中完全展示，但结合tmux上下文，该字段在模式树数据结构初始化... |
| 2504 | tmux-3.4 | mode_tree_draw | Dereference of null pointer | 754 | FP | FP | 告警点位于 `xasprintf(&text, " %s", mti->name);`，其中 `mti` 指针在切片代码中已通过 `mti = line->item;` 和 `line = &mtd->line_list[mtd->c... |
| 2507 | tmux-3.4 | grid_string_cells | Dereference of null pointer | 1073 | FP | FP | 切片代码显示，在调用 `grid_string_cells_code(*lastgc, ...)` 之前，存在条件判断 `if (lastgc != NULL && *lastgc == NULL)`，若满足条件会将 `*lastgc... |
| 2509 | tmux-3.4 | window_copy_move_after_search_mark | Dereference of null pointer | 3691 | FP | FP | 在调用 `window_copy_search_mark_at` 并返回0后，才访问 `data->searchmark[start]`，此时 `start` 已由该函数有效赋值，且切片中 `searchmark` 数组的访问点均有边... |
| 2510 | tmux-3.4 | input_parse | Dereference of null pointer | 912 | FP | FP | 在访问 `ictx->state->transitions` 之前，代码逻辑已通过 `if` 条件确保 `ictx->state` 不为 NULL，且 `fatalx` 函数会在 `itr` 查找失败时终止程序，防止了空指针解引用。 |
| 2508 | tmux-3.4 | server_client_reset_state | Dereference of null pointer | 2394 | FP | FP | 告警点位于条件判断语句中，访问 `s->cx` 和 `s->cy`。变量 `s` 在切片中已明确赋值：要么通过 `c->overlay_mode` 回调函数（若不为空）返回一个有效的 `struct screen*`，要么直接赋值为 ... |

### 5.3 不一致：算法=TP，LLM=FP（共 71 条）

> 算法认为是真实漏洞（TP），但 LLM 认为是误报（FP）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 276 | git-2.47.1 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | TP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但宏内已通过 `BUILD_ASSERT_OR_ZERO(ARRA... |
| 278 | git-2.47.1 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | TP | FP | 告警源于宏展开，`ARRAY_SIZE(string) - 1` 中的 `string` 是宏参数 `CNTRL`，它是一个字符串字面量，其大小在编译时确定且大于0，因此索引计算不会产生负值。这是一个静态分析工具对宏展开的误判。 |
| 277 | git-2.47.1 | test_ctype__ispunct | cpp/overflow-buffer | 91 | TP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时可能产生负索引，但宏内包含 `BUILD_ASSERT_OR_ZERO(ARRA... |
| 279 | git-2.47.1 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | TP | FP | 告警指出的负索引访问发生在宏 `ARRAY_SIZE(string) - 1` 中，其中 `string` 是字符串字面量 `"!\"#%&',-/:;<=>@_`~"`，其大小固定且大于0，因此 `ARRAY_SIZE(string... |
| 280 | git-2.47.1 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | TP | FP | 宏定义中的数组索引 `string[-1]` 仅出现在 `ARRAY_SIZE(string) - 1` 的计算中，用于获取字符串长度减一，这是安全的惯用法。`BUILD_ASSERT_OR_ZERO` 宏确保数组大小大于0，且 `m... |
| 281 | git-2.47.1 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | TP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时才会产生负索引，但宏内通过 `BUILD_ASSERT_OR_ZERO(ARRA... |
| 282 | git-2.47.1 | test_ctype__isalnum | cpp/overflow-buffer | 51 | TP | FP | 宏 `TEST_CHAR_CLASS` 中的 `len` 计算 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时可能为 -1，但宏内包含 `BUILD_ASSERT_OR_Z... |
| 283 | git-2.47.1 | test_ctype__isalpha | cpp/overflow-buffer | 46 | TP | FP | 宏定义中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但宏内已通过 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > ... |
| 285 | git-2.47.1 | <global> | cpp/overflow-buffer | 36 | TP | FP | 切片代码显示函数体为空，不存在任何数组索引操作，工具报告的访问负索引-1的告警在可见代码中不成立。 |
| 284 | git-2.47.1 | test_ctype__isdigit | cpp/overflow-buffer | 41 | TP | FP | 告警针对宏 `TEST_CHAR_CLASS` 展开后的 `string[-1]` 访问，但宏内 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string) > 0` 时执行，且 `BUILD_AS... |
| 406 | git-2.46.0 | fill_bitmap_commit | cpp/inconsistent-null-check | 493 | TP | FP | 函数 `prio_queue_get` 在队列为空时返回 NULL，但调用点位于 `while (queue->nr)` 循环内，该条件已确保队列非空，因此返回值不可能为 NULL，无需额外检查。 |
| 414 | git-2.46.0 | <global> | cpp/overflow-buffer | 41 | TP | FP | 告警源于宏展开，`ARRAY_SIZE(string) - 1` 中的 `string` 是字符串字面量，其大小在编译时确定且大于0，因此索引操作是安全的。代码是用于字符分类的单元测试，不存在实际的缓冲区溢出风险。 |
| 413 | git-2.46.0 | <global> | cpp/overflow-buffer | 40 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，其中 `string` 是字符串字面量，其 `ARRAY_SIZE` 至少为1，因此 `ARRAY_SIZ... |
| 415 | git-2.46.0 | <global> | cpp/overflow-buffer | 42 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，其中 `string` 是字符串字面量。`ARRAY_SIZE` 宏作用于静态数组，其大小在编译时已知且为... |
| 416 | git-2.46.0 | <global> | cpp/overflow-buffer | 43 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，其中 `string` 是字符串字面量。`ARRAY_SIZE` 宏用于计算数组元素数量，对于非空字符串字... |
| 417 | git-2.46.0 | <global> | cpp/overflow-buffer | 47 | TP | FP | 告警指出的负索引访问发生在宏 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)` 的编译时断言上下文中，其目的是确保数组大小大于0，若断言失败（数组大小为0）则表达式结果为0，不会在运行时产生... |
| 418 | git-2.46.0 | <global> | cpp/overflow-buffer | 48 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，其中 `string` 是字符串字面量。`ARRAY_SIZE` 宏用于计算数组元素数量，对于非空字符串字... |
| 419 | git-2.46.0 | <global> | cpp/overflow-buffer | 49 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是字符串字面量，其 `ARRAY_SIZE` 至少为1，因此 `len` 的计算是安... |
| 470 | curl-8_9_1 | Curl_splayremove | cpp/inconsistent-null-check | 270 | TP | FP | Curl_splay函数在输入指针t为NULL时直接返回t（即NULL），调用方在调用前已检查t不为NULL，且后续逻辑不依赖Curl_splay的返回值必须为非NULL，因此此处的NULL检查是多余的，属于工具误报。 |
| 673 | vim-9.1.1591 | <global> | cpp/redundant-null-check-simple | 3506 | TP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 在解引用前已通过条件 `if (*inc_opt != NUL)` 确保其非空，因此解引用是安全的，空指针检查确实是冗余的，属于误报。 |
| 675 | vim-9.1.1591 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | TP | FP | 切片代码显示，在告警点使用变量 'col' 之前，已通过 'pos.col > 0' 和 'pos.col > 1' 等条件进行了范围检查，确保了数组访问的安全性。 |
| 676 | vim-9.1.1591 | common_function | cpp/inconsistent-null-check | 5253 | TP | FP | 代码在调用 vim_strsave 后，将返回值赋给变量 'name'，并在后续多个分支中检查 'name' 是否为 NULL，若为 NULL 则调用 vim_free(name) 或直接使用，而 vim_free 函数内部已处理 N... |
| 677 | vim-9.1.1591 | common_function | cpp/inconsistent-null-check | 5366 | TP | FP | 告警点位于条件分支 `else if (is_funcref)` 内部，该分支仅在 `trans_name != NULL` 时才会执行。在切片代码中，`trans_name` 由 `save_function_name` 生成，若其... |
| 679 | vim-9.1.1591 | get_isolated_shell_name | cpp/inconsistent-null-check | 2743 | TP | FP | 函数 `gettail` 已对 NULL 输入进行了检查并返回空字符串，因此 `vim_strsave` 的参数不会是 NULL，其返回值 `p` 被直接返回，调用方负责检查。切片内代码逻辑保证了告警点不会出现 NULL 解引用问题。 |
| 682 | vim-9.1.1591 | did_set_background | cpp/inconsistent-null-check | 1098 | TP | FP | 切片代码显示，vim_strsave的返回值立即传递给check_string_option函数，该函数会检查指针是否为NULL并将其替换为empty_option，从而确保了后续使用p_bg时不会出现空指针解引用。 |
| 681 | vim-9.1.1591 | did_set_cryptmethod | cpp/inconsistent-null-check | 1923 | TP | FP | 代码中调用 vim_strsave 的参数是字符串字面量 "zip"，分配失败的可能性极低，且即使失败，后续对 p_cm 的使用（如 STRCMP）也允许其为 NULL（因为宏展开为 strcmp，而 strcmp 接受 NULL 参... |
| 683 | vim-9.1.1591 | apply_move_options | cpp/inconsistent-null-check | 531 | TP | FP | 告警点`find_win_by_nr_or_id`的返回值在下一行立即被`win_valid_any_tab`函数检查，该函数内部已包含对NULL指针的检查（`if (win == NULL) return FALSE;`），因此代码... |
| 684 | vim-9.1.1591 | <global> | cpp/inconsistent-null-check | 3339 | TP | FP | 代码中已对scan指针进行了NULL检查（if (got_int ｜｜ scan == NULL)），且regnext函数内部也包含NULL检查（if (p == JUST_CALC_SIZE ｜｜ reg_toolong) retu... |
| 687 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1579 | TP | FP | 切片代码显示，在调用 `regnext(br)` 之前，已经检查了 `reg_toolong` 标志，如果该标志为真，函数会提前返回 NULL。`regnext` 函数内部也会检查 `reg_toolong` 标志，如果为真则直接返回... |
| 686 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1562 | TP | FP | 切片代码显示，在调用 regnode(NOTHING) 之前，存在对 ret != JUST_CALC_SIZE 的条件检查，这表明该调用处于一个特定的计算模式（JUST_CALC_SIZE）下，该模式下 regnode 函数仅更新 ... |
| 688 | vim-9.1.1591 | get_wordnode | cpp/inconsistent-null-check | 4636 | TP | FP | 函数 `getroom` 在内存分配失败时会返回 NULL，但调用点 `get_wordnode` 在后续的 `#ifdef SPELL_PRINTTREE` 代码块中明确检查了 `n != NULL` 后才使用 `n`，且函数最终返... |
| 685 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1541 | TP | FP | 切片代码显示，在调用 `regnode(BRANCH)` 后，其返回值 `br` 被立即用于条件判断 `if (ret == NULL)` 和后续的 `regtail` 操作，但并未直接用于可能因空指针导致崩溃的敏感操作。更重要的是，... |
| 689 | vim-9.1.1591 | do_tag | cpp/inconsistent-null-check | 638 | TP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续逻辑中被立即传递给 `vim_free(tofree)`，而 `tofree` 被赋值为 `name`，这表明代码已通过 `vim_free` 处理了可能的空指针... |
| 694 | vim-9.1.1591 | helptags_one | cpp/unsafe-strcat | 975 | TP | FP | STRCAT 宏被用于拼接固定字符串 "/**/*" 和参数 ext，但 ext 是函数参数，其来源和长度在切片中未知。然而，NameBuff 是一个全局缓冲区，其大小在代码中未显示，但根据 Vim 的典型实现，它通常被定义为足够大（... |
| 696 | vim-9.1.1591 | store_aff_word | cpp/unsafe-strcat | 3915 | TP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限内容，并确保其大小不超过MAXWLEN-1。后续的STRCAT操作拼接的字符串p是原始单词的一部分，其长度受原始单词长度和... |
| 719 | vim-9.1.1591 | make_filter_cmd | cpp/unbounded-write | 1858 | TP | FP | 代码在调用STRCAT前，已通过alloc(len)分配了缓冲区，且len的计算已考虑了所有待拼接字符串的长度和终止符，确保了缓冲区大小足够，不存在缓冲区溢出风险。 |
| 730 | vim-9.1.1591 | discard_exception | cpp/unbounded-write | 646 | TP | FP | 切片代码显示，目标缓冲区 IObuff 在调用 STRCPY 前，其内容正是由 saved_IObuff 保存的，而 saved_IObuff 是通过 vim_strsave(IObuff) 获得的 IObuff 的副本。因此，将保存... |
| 737 | vim-9.1.1591 | vim_rename | cpp/unbounded-write | 3865 | TP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。 |
| 740 | vim-9.1.1591 | concat_fnames | cpp/unbounded-write | 3134 | TP | FP | 代码通过alloc分配了足够容纳fname1和fname2拼接结果的内存（包括额外字节），STRCPY的目标缓冲区大小是经过计算保证的，不存在缓冲区溢出的风险。 |
| 759 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 975 | TP | FP | NameBuff 缓冲区大小未在切片中明确给出，但根据其使用模式（如存储路径、调用 vim_snprintf 时使用 MAXPATHL）以及 Vim 代码库的惯例，它很可能是一个足够大的静态缓冲区（如 MAXPATHL 大小）。此外，... |
| 762 | vim-9.1.1591 | highlight_set_startstop_termcode | cpp/unbounded-write | 1488 | TP | FP | 切片代码中，在调用STRCAT(buf, p)之前，已通过条件`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了目标缓冲区buf（大小为100）的剩余空间，确保拼接后不会溢出。因此，该告警为误报。 |
| 760 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 991 | TP | FP | NameBuff 缓冲区大小定义为 MAXPATHL，而 tagfname 参数来自调用方，其长度在切片中未见限制。但告警点前的代码路径（如 gen_expand_wildcards）和文件操作（mch_fopen）均依赖 NameB... |
| 779 | vim-9.1.1591 | may_trigger_modechanged | cpp/unbounded-write | 2869 | TP | FP | STRCPY 的目标缓冲区 `last_mode` 和源缓冲区 `curr_mode` 大小均为 `MODE_MAX_LENGTH`，且 `get_mode` 函数确保写入的字符串长度严格受控，不会超过缓冲区大小，因此不存在缓冲区溢出风险。 |
| 784 | vim-9.1.1591 | add_to_showcmd | cpp/unbounded-write | 1764 | TP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已通过计算old_len和extra_len检查了缓冲区溢出风险，并在溢出时通过mch_memmove移动了缓冲区内容，确保了拼接操作不会超出SHOWCMD_COLS的限制。 |
| 816 | vim-9.1.1591 | getroom_save | cpp/unbounded-write | 4341 | TP | FP | 函数 getroom 已根据源字符串长度（STRLEN(s) + 1）分配了足够的内存，STRCPY 的目标缓冲区大小与源字符串长度匹配，不存在缓冲区溢出的风险。 |
| 826 | vim-9.1.1591 | concat_str | cpp/unbounded-write | 792 | TP | FP | 函数内通过alloc为目标缓冲区分配了精确的大小（str1和str2的长度之和加1），然后使用STRCPY（即strcpy）进行拷贝。由于目标缓冲区大小是根据源字符串长度精确计算的，因此strcpy操作不会导致缓冲区溢出。 |
| 828 | vim-9.1.1591 | strlow_save | cpp/unbounded-write | 463 | TP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(STRLEN(res) + 1 + newl - l)为目标缓冲区分配了精确的足够空间，确保目标缓冲区大小足以容纳源字符串，因此不存在缓冲区溢出风险。 |
| 1586 | redis-8.0.2 | strbuf_init | Dereference of null pointer | 55 | TP | FP | 代码中`s->buf = NULL;`是对结构体指针`s`的成员进行赋值，并非解引用空指针。该操作是安全的初始化，不构成空指针解引用错误。 |
| 1587 | redis-8.0.2 | breakstat | Dereference of null pointer | 986 | TP | FP | 在调用 `luaK_codeABC` 前，`bl` 变量已通过 `while` 循环确保其不为空（`while (bl && !bl->isbreakable)`），且循环条件 `bl` 为真时才会继续。因此，当代码执行到使用 `bl... |
| 1594 | redis-8.0.2 | extent_try_coalesce_impl | Dereference of null pointer | 869 | TP | FP | 告警指向对指针`coalesced`的赋值，但切片代码显示该指针在函数入口处作为参数传入，并在循环内部多个分支中被赋值，表明它是一个有效的非空指针。对`*coalesced = false`的解引用是安全的，不存在空指针解引用风险。 |
| 1601 | redis-8.0.2 | extent_try_coalesce_impl | Dereference of null pointer | 844 | TP | FP | 告警点位于对指针`coalesced`的赋值语句，该指针作为函数参数传入，在切片代码中，所有对`*coalesced`的赋值操作前都明确检查了`ecache->delay_coalesce`不为空，且指针本身在函数入口处已被使用（作为... |
| 1608 | redis-8.0.2 | tcache_create_ctl | Dereference of null pointer | 2467 | TP | FP | VERIFY_READ宏在解引用oldlenp前已检查oldlenp是否为NULL，切片代码显示告警点位于VERIFY_READ宏调用处，该宏包含空指针检查，因此不会发生空指针解引用。 |
| 1612 | redis-8.0.2 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | TP | FP | 告警指向的 VERIFY_READ 宏在解引用 oldlenp 前已检查其是否为 NULL，切片中未发现空指针解引用路径。该宏的逻辑是：若 oldp 或 oldlenp 为 NULL，则直接跳转返回，不会执行后续解引用。因此，该告警为误报。 |
| 1613 | redis-8.0.2 | json_next_token | Dereference of null pointer | 1024 | TP | FP | 切片代码显示，在访问 `ch2token[ch]` 之前，`ch` 的值来自 `*(json->ptr)`，而 `json->ptr` 在循环中会递增，但始终指向 `json->data` 字符串缓冲区内部。只要输入字符串非空且以空字... |
| 1620 | redis-8.0.2 | min_expand | Dereference of null pointer | 322 | TP | FP | 在告警行 `singlematch(uchar(*s), p, ep)` 中，指针 `s` 在解引用前已通过条件 `s<ms->src_end` 进行了边界检查，确保了 `s` 指向有效内存，因此不会发生空指针解引用。 |
| 1622 | redis-8.0.2 | strbuf_ensure_null | Dereference of null pointer | 134 | TP | FP | 切片代码显示函数为内联静态函数，其参数`s`在调用前必须非空，且`s->buf`和`s->length`的合法性由调用方保证。函数逻辑是安全的字符串终止操作，工具误报了空指针解引用。 |
| 1625 | redis-8.0.2 | arenas_create_ctl | Dereference of null pointer | 3101 | TP | FP | VERIFY_READ宏在解引用oldlenp前已检查其不为NULL，且切片代码中malloc_mutex_unlock调用前已通过ctl_arena_init等路径确保tsd_tsdn(tsd)返回有效指针，不存在空指针解引用。 |
| 1626 | redis-8.0.2 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | TP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在解引用 oldlenp 前已检查其是否为 NULL。切片代码显示，只有当 oldp 或 oldlenp 为 NULL 时，宏会提前返回，因此解引用 *oldlenp 是安全的，不会发生... |
| 1749 | ffmpeg-7.0.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1428 | TP | FP | 切片代码显示，在访问 `scale_matrix[pos]` 之前，存在条件 `if (s->ps.sps->scaling_list_enable_flag && !(transform_skip_flag && log2_traf... |
| 1765 | ffmpeg-7.0.1 | check_available | Dereference of null pointer | 608 | TP | FP | 切片代码显示，在访问 `TAB_MVF(n->x, n->y).pred_flag` 之前，`n->available` 的计算已包含对 `sps->r` 指针的访问，且该访问未发生空指针解引用，表明 `sps` 及其成员 `r` 在... |
| 1794 | ffmpeg-7.0.1 | avc_parse_nal_units | Dereference of null pointer | 92 | TP | FP | 在切片代码中，对指针`list`的访问（如`list->nalus`）发生在`list`作为函数参数传入之后，且没有证据表明`list`在函数入口处为NULL。告警点`list->nb_nalus >= nalu_limit`位于`i... |
| 2140 | git-2.49.0 | process_entry | Dereference of null pointer | 3413 | TP | FP | 切片代码显示，在访问 `ci->ren2->pair->two->path` 之前，已经通过 `if (ci->ren2)` 检查了 `ci->ren2` 不为空。该告警位于 `RENAME_ONE_FILE_TO_TWO` 分支内，... |
| 2253 | git-2.50.1 | <global> | Dereference of null pointer | 88 | TP | FP | 告警位于单元测试代码中，切片显示在调用 check_str(out[0], "a") 前已通过 check(out != NULL) 验证了指针非空，且测试数据 in2 是静态字符串常量，parse_names 函数逻辑保证了返回的数... |
| 2262 | git-2.50.1 | <global> | Dereference of null pointer | 82 | TP | FP | 告警位于单元测试代码中，`check_str(out[0], "line");` 前已通过 `check(out != NULL);` 确保 `out` 非空，且 `parse_names` 函数在切片中可见其返回 NULL 终止的字... |
| 2285 | git-2.50.1 | write_table | Dereference of null pointer | 65 | TP | FP | 告警点 `(*names)[i]` 的赋值来自 `xstrfmt` 的返回值，该函数返回新分配的内存指针，不会为 NULL。切片中 `refs` 和 `logs` 数组通过 `REFTABLE_CALLOC_ARRAY` 分配，且循环... |
| 2297 | git-2.50.1 | <global> | Dereference of null pointer | 200 | TP | FP | 切片代码显示告警行位于单元测试中，且紧接在REFTABLE_ALLOC_GROW_OR_NULL宏调用之后，该宏已确保arr非空（check(arr != NULL)），因此arr[0] = 42不会发生空指针解引用。 |
| 2300 | git-2.50.1 | t_log_write_read | Dereference of null pointer | 224 | TP | FP | 告警指向的 `names[i] = xstrdup(name);` 行，`name` 是局部数组，`xstrdup` 内部会检查 `strdup` 的返回值并在失败时调用 `die` 终止程序，因此不会发生空指针解引用。切片代码中 `... |
| 2308 | git-2.50.1 | <global> | Dereference of null pointer | 206 | TP | FP | 告警位于单元测试代码中，该行 `arr[alloc - 1] = 42;` 前已通过 `check(arr != NULL);` 和 `check_uint(alloc, >, old_alloc);` 确保了 `arr` 非空且 `... |
| 2313 | git-2.50.1 | t_table_refs_for | Dereference of null pointer | 577 | TP | FP | 切片代码显示 `want_names` 数组在循环中被 `xstrdup` 返回的指针填充，`free_names` 函数会安全地处理空指针，且 `xstrdup` 在内存分配失败时会调用 `die` 终止程序，因此不存在对空指针的解引用。 |
| 2367 | git-2.47.1 | assert_sane_strbuf | Dereference of null pointer | 36 | TP | FP | 切片代码显示，在解引用 `buf->buf` 之前，已通过 `check(!!buf->buf)` 宏检查了 `buf->buf` 是否为非空。该检查确保了后续 `buf->buf[buf->len]` 的访问是安全的，因此告警为误报。 |
| 2488 | tmux-3.1 | <global> | Dereference of null pointer | 74 | TP | FP | 告警点位于条件分支 `if (wme == NULL ｜｜ wme->mode->key_table == NULL)` 为真时，此时 `wme` 或 `wme->mode->key_table` 为 NULL，但代码在解引用 `fs... |

### 5.4 不一致：算法=FP，LLM=TP（共 789 条）

> 算法认为是误报（FP），但 LLM 认为是真实漏洞（TP）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 1 | ffmpeg-6.1.1 | upcase_string | cpp/offset-use-before-range-check | 1053 | FP | TP | 循环条件 `src[i] && i < dst_size-1` 在检查 `i` 是否小于 `dst_size-1` 之前，先访问了 `src[i]`，这可能导致在 `i` 等于或超过 `dst_size-1` 时，`src[i]` 的... |
| 6 | ffmpeg-6.1.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | TP | 在while循环条件中，先使用`entries[m].flags`访问数组，后进行`m < b && m < nb_entries - 1`范围检查，存在数组索引越界访问的风险。 |
| 10 | ffmpeg-6.1.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回了 `av_mallocz` 的调用结果，未对返回值进行空指针检查。根据告警信息和 `av_mallocz` 的定义，内存分配可能失败并返回 NULL，直接使用该返回... |
| 13 | ffmpeg-6.1.1 | get_frag_time | cpp/inconsistent-null-check | 1383 | FP | TP | 函数 get_frag_stream_info 可能返回 NULL，但调用后未检查返回值就直接解引用访问其成员（如 frag_stream_info->sidx_pts），存在空指针解引用风险。 |
| 15 | ffmpeg-6.1.1 | url_alloc_for_protocol | cpp/unbounded-write | 101 | FP | TP | 代码使用strcpy将filename参数复制到新分配的内存中，而filename来自函数参数，其长度可能超过目标缓冲区大小。切片中未显示对filename长度的任何验证或使用安全函数，存在缓冲区溢出风险。 |
| 21 | ffmpeg-7.1.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 148 | FP | TP | 在while循环条件 `m < b && m < nb_entries - 1` 中，先使用了 `entries[m].flags`，然后才检查 `m < nb_entries - 1`。如果 `m` 初始值等于或大于 `nb_ent... |
| 23 | ffmpeg-7.1.1 | enc_open | cpp/inconsistent-null-check | 189 | FP | TP | 代码直接解引用 `desc->props` 而未检查 `av_frame_side_data_desc` 的返回值是否为 NULL，存在空指针解引用风险。切片中提供的 `av_frame_side_data_desc` 函数定义明确显... |
| 25 | ffmpeg-7.1.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回了 `av_mallocz` 的调用结果，未检查其是否为 NULL。根据告警信息和切片代码，这违反了项目中 99% 的调用模式，可能导致后续对空指针的解引用，存在安全风险。 |
| 30 | ffmpeg-7.1.1 | cmp_dm_level0 | cpp/overflow-buffer | 294 | FP | TP | memcmp调用使用结构体总大小减去成员偏移量来计算长度，但该长度（24字节）超过了结构体中剩余成员的实际总大小（22字节），可能导致缓冲区溢出。切片代码中的计算逻辑清晰，存在明确的越界访问风险。 |
| 32 | ffmpeg-7.0.1 | upcase_string | cpp/offset-use-before-range-check | 1108 | FP | TP | 循环条件 `src[i] && i < dst_size-1` 在检查 `i < dst_size-1` 前先访问了 `src[i]`，若 `i` 等于或大于 `dst_size-1` 但小于 `src` 数组的实际边界，则存在对 `... |
| 31 | ffmpeg-7.1.1 | url_alloc_for_protocol | cpp/unbounded-write | 146 | FP | TP | 代码使用strcpy将filename参数复制到新分配的内存中，而filename来自函数参数，其来源可能不受控（如环境变量、命令行参数等）。虽然目标缓冲区大小是strlen(filename)+1，但strcpy本身不检查边界，若f... |
| 37 | ffmpeg-7.0.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | TP | 在while循环条件中，先使用`entries[m].flags`访问数组元素，后进行`m < b && m < nb_entries - 1`范围检查，存在数组越界访问的风险。 |
| 40 | ffmpeg-7.0.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回了 `av_mallocz` 的调用结果，未检查其是否为 NULL。根据提供的 `av_mallocz` 定义，内存分配可能失败并返回 NULL，直接使用该返回值可能... |
| 44 | ffmpeg-7.0.1 | get_frag_time | cpp/inconsistent-null-check | 1541 | FP | TP | 函数 get_frag_stream_info 可能返回 NULL，但调用后未检查返回值就直接解引用其成员（如 frag_stream_info->sidx_pts），存在空指针解引用风险。 |
| 46 | ffmpeg-7.0.1 | url_alloc_for_protocol | cpp/unbounded-write | 145 | FP | TP | 代码使用strcpy将filename参数复制到新分配的内存中，虽然分配大小为strlen(filename)+1，但filename可能来自不受控的输入（如环境变量、命令行参数），且切片中未见任何对filename长度的前置校验或使... |
| 47 | ffmpeg-7.1 | upcase_string | cpp/offset-use-before-range-check | 1109 | FP | TP | 在循环终止条件 `src[i] && i < dst_size-1` 中，对 `src[i]` 的访问发生在对 `i` 的范围检查 `i < dst_size-1` 之前，存在潜在的越界读取风险。 |
| 52 | ffmpeg-7.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 148 | FP | TP | 在while循环条件中，先使用`entries[m].flags`访问数组元素，后进行`m < b && m < nb_entries - 1`的边界检查，存在明显的数组越界访问风险。 |
| 56 | ffmpeg-7.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回了 `av_mallocz` 的调用结果，未检查其是否为 NULL。切片代码中未显示任何前置校验或错误处理逻辑，这可能导致后续代码在分配失败时使用空指针，引发未定义行... |
| 59 | ffmpeg-7.1 | intercept_id3 | cpp/inconsistent-null-check | 1191 | FP | TP | 函数 current_segment 可能返回 NULL，但调用结果 seg 被直接传递给 read_from_url 等函数使用，未进行空指针检查，存在潜在的空指针解引用风险。 |
| 60 | ffmpeg-7.1 | get_frag_time | cpp/inconsistent-null-check | 1630 | FP | TP | 函数 get_frag_stream_info 可能返回 NULL，但调用后未检查返回值就直接解引用其成员（如 frag_stream_info->sidx_pts），存在空指针解引用风险。 |
| 63 | ffmpeg-7.1 | url_alloc_for_protocol | cpp/unbounded-write | 146 | FP | TP | 代码使用strcpy将外部传入的filename参数复制到新分配的内存中，未检查目标缓冲区大小，存在缓冲区溢出风险。告警指出filename可能来自环境变量、命令行参数或文件读取，表明其为外部可控输入。 |
| 62 | ffmpeg-7.1 | cmp_dm_level0 | cpp/overflow-buffer | 294 | FP | TP | memcmp调用试图访问从结构体成员signal_eotf到结构体末尾的整个内存区域，其大小计算为`sizeof(AVDOVIColorMetadata) - offsetof(AVDOVIColorMetadata, signal_... |
| 64 | ffmpeg-6.0 | upcase_string | cpp/offset-use-before-range-check | 1044 | FP | TP | 在循环条件 `src[i] && i < dst_size-1` 中，对 `src[i]` 的访问发生在对 `i` 的范围检查 `i < dst_size-1` 之前。如果 `dst_size` 为 0，则 `dst_size-1` ... |
| 67 | ffmpeg-6.0 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | TP | 在while循环条件`(entries[m].flags & AVINDEX_DISCARD_FRAME) && m < b && m < nb_entries - 1`中，先访问了`entries[m]`，然后才检查`m < nb_... |
| 70 | ffmpeg-6.0 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 203 | FP | TP | 函数 `ff_iir_filter_init_state` 直接返回了 `av_mallocz` 的调用结果，未检查其是否为 NULL。根据告警信息和被调用函数的定义，`av_mallocz` 可能返回 NULL，且绝大多数调用点都进... |
| 73 | ffmpeg-6.0 | get_frag_time | cpp/inconsistent-null-check | 1286 | FP | TP | 函数 `get_frag_stream_info` 可能返回 NULL，但调用后未检查返回值便直接解引用其成员 `sidx_pts`，存在空指针解引用风险。切片中未见任何防护机制。 |
| 83 | openssl-openssl-3.5.1 | tls_parse_stoc_npn | cpp/use-after-free | 1660 | FP | TP | 切片代码显示在调用`OPENSSL_free(s->ext.npn)`释放内存后，紧接着在`memcpy`中使用了指针`s->ext.npn`指向的目标缓冲区`selected`，而`selected`和`selected_len`的... |
| 88 | openssl-openssl-3.5.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 可能返回 NULL，但调用后未检查返回值，直接解引用 `el->state`，存在空指针解引用风险。 |
| 91 | openssl-openssl-3.5.1 | ts_check_status_info | cpp/unsafe-strcat | 385 | FP | TP | 代码在循环中使用strcat向固定大小的缓冲区failure_text追加字符串，未检查缓冲区剩余空间，存在缓冲区溢出的风险。 |
| 89 | openssl-openssl-3.5.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 在特定条件下（如 `enc_level` 无效或 `require_prov` 为真且状态不满足）会返回 NULL，但调用方 `ossl_qrl_enc_level_se... |
| 95 | openssl-openssl-3.5.1 | main | cpp/unbounded-write | 82 | FP | TP | 代码使用`strcpy`将命令行参数`argv[n]`复制到固定大小的缓冲区`pathname`（大小为`PATH_MAX`），而`argv[n]`的长度`dirname_len`可能大于或等于`PATH_MAX`，导致缓冲区溢出。切... |
| 121 | openssl-openssl-3.3.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 在特定条件下（如 `enc_level >= QUIC_ENC_LEVEL_NUM` 或 `require_prov` 条件不满足）会返回 NULL，但调用方 `ossl... |
| 123 | openssl-openssl-3.3.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | TP | 代码在循环中使用`strcat`向固定大小的缓冲区`failure_text`拼接字符串，未检查缓冲区剩余大小，存在缓冲区溢出的风险。 |
| 124 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 2582 | FP | TP | sprintf 使用 evp_mac_mdname 作为格式化字符串的一部分，而 evp_mac_mdname 来自用户输入（命令行参数或环境变量），且切片中未显示对其长度进行任何限制或验证，存在缓冲区溢出风险。 |
| 125 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 2860 | FP | TP | sprintf 使用未经验证的字符串 evp_mac_ciphername 作为格式化参数，该字符串来自命令行参数（opt_arg），可能导致缓冲区溢出。切片中未显示对 evp_mac_ciphername 长度的检查或防护。 |
| 129 | openssl-openssl-3.3.1 | main | cpp/unbounded-write | 82 | FP | TP | 代码使用strcpy将命令行参数argv[n]复制到固定大小(PATH_MAX)的缓冲区pathname中，argv[n]长度可能超过PATH_MAX，导致缓冲区溢出。切片中未见对argv[n]长度的前置校验。 |
| 150 | openssl-openssl-3.4.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1689 | FP | TP | 切片代码显示，在调用 `memcmp` 比较 `s->session->ext.alpn_selected` 和 `s->s3.alpn_selected` 时，`s->s3.alpn_selected` 可能为 NULL（因为前面的... |
| 157 | openssl-openssl-3.4.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 在特定条件下（如断言失败或状态不满足 `require_prov`）会返回 NULL，但调用方 `ossl_qrl_enc_level_set_have_el` 未检查返... |
| 159 | openssl-openssl-3.4.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | TP | 代码使用strcat向固定大小的缓冲区failure_text追加字符串，但未检查缓冲区剩余空间。循环中多次追加，存在缓冲区溢出的风险。 |
| 163 | openssl-openssl-3.4.1 | main | cpp/unbounded-write | 82 | FP | TP | 代码使用strcpy将命令行参数argv[n]复制到固定大小的缓冲区pathname（大小为PATH_MAX），若argv[n]长度大于或等于PATH_MAX，将导致缓冲区溢出。切片中未见对argv[n]长度的前置校验，存在明确的安全风险。 |
| 188 | openssl-openssl-3.2.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 在特定条件下（如 `enc_level` 越界或 `require_prov` 为真且状态不满足）会返回 NULL，但调用方 `ossl_qrl_enc_level_se... |
| 190 | openssl-openssl-3.2.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | TP | 代码使用strcat向固定大小的缓冲区failure_text追加字符串，但未检查缓冲区剩余空间。循环中多次追加，存在缓冲区溢出的风险。 |
| 191 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 2530 | FP | TP | sprintf 使用未经验证的用户输入 evp_mac_mdname 作为格式化字符串的一部分，目标缓冲区 evp_hmac_name 的大小仅基于固定字符串 "hmac()" 和 evp_mac_mdname 的长度分配，若 evp... |
| 192 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 2826 | FP | TP | sprintf 使用来自命令行参数或环境变量的 evp_mac_ciphername 作为输入，目标缓冲区 evp_cmac_name 的大小为固定计算值（'cmac()' 长度 + 字符串长度），但若 evp_mac_ciphern... |
| 196 | openssl-openssl-3.2.1 | main | cpp/unbounded-write | 82 | FP | TP | 代码使用strcpy将命令行参数argv[n]复制到固定大小（PATH_MAX）的缓冲区pathname中，未检查源字符串长度，存在缓冲区溢出风险。切片中未见对argv[n]长度的前置校验。 |
| 224 | openssl-openssl-3.4.0 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | TP | 函数 `ossl_qrl_enc_level_set_get` 在特定条件下（如断言失败或状态不满足 `require_prov`）会返回 NULL，但调用方 `ossl_qrl_enc_level_set_have_el` 未对返回... |
| 226 | openssl-openssl-3.4.0 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | TP | 代码使用strcat向固定大小的缓冲区failure_text追加字符串，未检查源字符串长度或目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 230 | openssl-openssl-3.4.0 | main | cpp/unbounded-write | 82 | FP | TP | 代码使用strcpy将命令行参数argv[n]复制到固定大小的缓冲区pathname（大小为PATH_MAX），若argv[n]长度大于或等于PATH_MAX，将导致缓冲区溢出。切片中未显示对argv[n]长度的前置检查，存在安全风险。 |
| 249 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 757 | FP | TP | 在for循环条件 's1[pos] == s2[pos] && pos < len' 中，访问 s1[pos] 和 s2[pos] 发生在检查 pos < len 之前，可能导致越界访问。这是一个典型的数组下标使用前未进行范围检查的缺陷。 |
| 250 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 757 | FP | TP | 在for循环条件 's1[pos] == s2[pos] && pos < len' 中，访问 s1[pos] 和 s2[pos] 发生在检查 pos < len 之前，可能导致在 pos 等于 len 时发生越界读取。 |
| 252 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 792 | FP | TP | 在for循环条件`wcs1[pos] == wcs2[pos] && pos < len`中，对数组`wcs1`和`wcs2`的访问`wcs1[pos]`和`wcs2[pos]`发生在范围检查`pos < len`之前，存在越界访问的风险。 |
| 255 | git-2.47.1 | bisect_successful | cpp/inconsistent-null-check | 646 | FP | TP | 函数 `lookup_commit_reference_by_name` 的返回值 `commit` 被直接传递给 `repo_format_commit_message` 使用，未进行空指针检查。根据规则描述，该函数在大多数情况下（... |
| 257 | git-2.47.1 | describe_commit | cpp/inconsistent-null-check | 324 | FP | TP | 函数 `lookup_commit_reference` 可能返回 NULL，但调用后未检查返回值，后续代码直接解引用 `cmit->object.oid`，存在空指针解引用风险。 |
| 263 | git-2.47.1 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1924 | FP | TP | 代码直接解引用 submodule_from_path 返回的指针 sub->name，未检查其是否为 NULL，存在空指针解引用风险。切片中无任何防护或校验逻辑。 |
| 268 | git-2.47.1 | clear_common_flag | cpp/inconsistent-null-check | 2132 | FP | TP | 代码在调用lookup_object后未检查返回值是否为NULL，直接解引用obj->flags，存在空指针解引用风险。切片显示lookup_object可能返回NULL，且无任何防护机制。 |
| 269 | git-2.47.1 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 143 | FP | TP | 代码直接使用 parse_object 的返回值（tag）访问其成员（tag->tagged），而未检查返回值是否为 NULL。根据规则描述，绝大多数调用都会检查 NULL，此处的遗漏可能导致空指针解引用。 |
| 286 | git-2.47.1 | add_patterns | cpp/invalid-pointer-deref | 1151 | FP | TP | 代码在分配大小为 `size` 的缓冲区 `buf` 后，执行了 `buf[size++] = '\n';` 写入操作。`xmallocz` 分配的是 `size` 字节，索引 `size` 已超出缓冲区边界一个字节，存在明确的越界写... |
| 290 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | TP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，访问 `s1[pos]` 和 `s2[pos]` 发生在检查 `pos < len` 之前，存在越界访问的风险。 |
| 291 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | TP | 在for循环条件中，变量`pos`在`s1[pos] == s2[pos]`处被用作数组下标，然后才在`pos < len`处进行范围检查，存在越界访问的风险。 |
| 288 | git-2.47.1 | should_prune_worktree | cpp/invalid-pointer-deref | 788 | FP | TP | 代码在循环中递减 `len` 后，使用 `path[len] = '\0';` 进行写操作。由于 `path` 是通过 `xmallocz(len)` 分配的，其大小为 `len` 字节，有效索引为 `0` 到 `len-1`。当循环... |
| 292 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | TP | 在for循环条件`wcs1[pos] == wcs2[pos] && pos < len`中，先访问`wcs1[pos]`和`wcs2[pos]`，后进行`pos < len`范围检查，存在潜在的越界访问风险。 |
| 293 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | TP | 在for循环条件`wcs1[pos] == wcs2[pos] && pos < len`中，先访问了`wcs1[pos]`和`wcs2[pos]`，然后才检查`pos < len`，存在数组越界访问的风险。 |
| 297 | git-2.50.1 | bisect_successful | cpp/inconsistent-null-check | 648 | FP | TP | 代码在调用 lookup_commit_reference_by_name 后，未检查返回的 commit 指针是否为 NULL，便直接将其传递给 repo_format_commit_message 和 oid_to_hex 函数使... |
| 298 | git-2.50.1 | describe_commit | cpp/inconsistent-null-check | 326 | FP | TP | 代码在调用 lookup_commit_reference 后未检查返回值是否为 NULL，随后直接解引用 cmit->object.oid，存在空指针解引用风险。 |
| 304 | git-2.50.1 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1932 | FP | TP | 代码在调用 submodule_from_path 后未检查返回值是否为 NULL，随后直接解引用 sub->name，存在空指针解引用风险。切片中未见任何防护或确保非空的逻辑。 |
| 307 | git-2.50.1 | unparse_commit | cpp/inconsistent-null-check | 189 | FP | TP | 代码在调用lookup_commit后未检查返回值是否为NULL，直接解引用c->object.parsed，存在空指针解引用风险。切片中未显示任何前置校验或防护机制。 |
| 308 | git-2.50.1 | clear_common_flag | cpp/inconsistent-null-check | 2146 | FP | TP | 代码在调用 `lookup_object` 后未检查返回的指针 `obj` 是否为 NULL，便直接解引用 `obj->flags`，存在空指针解引用风险。切片中未显示任何前置校验能保证 `lookup_object` 一定返回非空对象。 |
| 309 | git-2.50.1 | deref_without_lazy_fetch | cpp/inconsistent-null-check | 156 | FP | TP | 代码直接使用 parse_object 的返回值作为指针进行解引用（tag->tagged），而未检查其是否为 NULL，这违反了大多数调用点（94%）的惯例，存在空指针解引用的风险。 |
| 311 | git-2.50.1 | get_parent | cpp/inconsistent-null-check | 1110 | FP | TP | 代码在调用 lookup_commit_reference 后未检查返回值是否为 NULL，随后直接将其传递给 repo_parse_commit，可能导致空指针解引用。切片中未见任何前置防护确保该调用不会返回 NULL。 |
| 329 | git-2.50.1 | add_patterns | cpp/invalid-pointer-deref | 1152 | FP | TP | 代码在分配大小为 `size` 的缓冲区 `buf` 后，执行了 `buf[size++] = '\n';`，这明显是对缓冲区末尾之后一个字节的越界写入，存在内存损坏风险。 |
| 330 | git-2.50.1 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1684 | FP | TP | 代码在解压循环后，直接执行 `buffer[size] = '\0';` 写入操作。如果解压过程恰好写满了 `size` 个字节（即 `stream.avail_out` 变为0），那么 `buffer[size]` 的写入将超出 `... |
| 331 | git-2.50.1 | should_prune_worktree | cpp/invalid-pointer-deref | 965 | FP | TP | 代码在分配大小为`len`的内存后，执行`path[len] = '\0'`写入操作，这超出了分配的内存边界（有效索引为0到len-1），存在缓冲区溢出风险。切片中未显示有防护措施确保`len`不为零或调整指针位置。 |
| 334 | git-2.49.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 895 | FP | TP | 在第一个while循环的条件判断中，使用`s[off]`访问数组前，仅检查了`s[off] == '\r' && off < len - 1`，未对`s[off] == '\f'`和`s[off] == '\v'`的情况进行`off ... |
| 336 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | TP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，访问 `s1[pos]` 和 `s2[pos]` 发生在检查 `pos < len` 之前，存在越界读取的风险。 |
| 337 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | TP | 在for循环条件 's1[pos] == s2[pos] && pos < len' 中，访问 s1[pos] 和 s2[pos] 发生在检查 pos < len 之前，存在越界访问的风险。 |
| 338 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | TP | 在for循环条件`wcs1[pos] == wcs2[pos] && pos < len`中，访问`wcs1[pos]`和`wcs2[pos]`发生在检查`pos < len`之前，存在越界访问的风险。 |
| 339 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | TP | 在for循环条件`wcs1[pos] == wcs2[pos] && pos < len`中，先访问`wcs1[pos]`和`wcs2[pos]`，后进行`pos < len`范围检查，存在越界访问风险。 |
| 341 | git-2.49.0 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | TP | 代码在调用 branch_get 后未检查返回值是否为 NULL，随后直接解引用 branch->remote_name，存在空指针解引用风险。被调用函数 branch_get 在特定条件下（如 name 为 NULL 或 "HEAD... |
| 343 | git-2.49.0 | bisect_successful | cpp/inconsistent-null-check | 648 | FP | TP | 函数 `lookup_commit_reference_by_name` 返回的 `commit` 指针在后续 `commit->object.oid` 中被直接解引用，未进行空值检查。切片代码中未显示任何前置校验能保证该指针非空，存... |
| 344 | git-2.49.0 | describe_commit | cpp/inconsistent-null-check | 326 | FP | TP | 代码在调用 lookup_commit_reference 后未检查返回值是否为 NULL，随后直接解引用 cmit->object.oid，存在空指针解引用风险。切片中未见任何前置校验或防护机制确保 oid 参数有效。 |
| 351 | git-2.49.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1932 | FP | TP | 代码在调用 submodule_from_path 后未检查返回值是否为 NULL，随后直接解引用 sub->name，存在空指针解引用风险。切片中未见任何防护或确保非空的逻辑。 |
| 355 | git-2.49.0 | clear_common_flag | cpp/inconsistent-null-check | 2147 | FP | TP | 代码在调用 `lookup_object` 后未检查返回的指针是否为 NULL，便直接解引用 `obj->flags`，存在空指针解引用风险。切片中未显示任何前置校验能保证 `lookup_object` 一定返回非空对象。 |
| 376 | git-2.49.0 | add_patterns | cpp/invalid-pointer-deref | 1152 | FP | TP | 代码在分配大小为 `size` 的缓冲区 `buf` 后，执行了 `buf[size++] = '\n';` 写入操作。`xmallocz(size)` 分配了 `size` 字节，有效索引范围为 `[0, size-1]`，因此写入... |
| 378 | git-2.49.0 | should_prune_worktree | cpp/invalid-pointer-deref | 960 | FP | TP | 代码在分配大小为 len 的内存后，执行了 `path[len] = '\0';` 写入操作。若 len 等于分配的大小，该写入将越界，导致缓冲区溢出。切片中未显示有确保 len 小于分配大小的防护逻辑。 |
| 377 | git-2.49.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1677 | FP | TP | 代码在解压循环后，直接执行 `buffer[size] = '\0';` 写入操作。`buffer` 由 `xmallocz_gently(size)` 分配，大小为 `size`，因此有效索引范围为 `0` 到 `size-1`。`... |
| 381 | git-2.46.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 890 | FP | TP | 在第一个while循环的条件判断中，访问`s[off]`发生在检查`off < len - 1`之前，存在数组越界读取的风险。 |
| 384 | git-2.46.0 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | TP | 代码在调用 branch_get 后未检查返回值是否为 NULL，随后直接解引用 branch->remote_name，存在空指针解引用风险。被调用的 branch_get 函数在某些条件下（如 name 为 NULL 或 "HEA... |
| 385 | git-2.46.0 | bisect_successful | cpp/inconsistent-null-check | 644 | FP | TP | 函数 lookup_commit_reference_by_name 可能返回 NULL，但调用后未检查返回值，后续直接解引用 commit->object.oid，存在空指针解引用风险。 |
| 386 | git-2.46.0 | update_head | cpp/inconsistent-null-check | 684 | FP | TP | 代码直接使用 lookup_commit_reference 的返回值，未检查其是否为 NULL，随后解引用 c->object.oid，存在空指针解引用风险。切片中未见任何前置校验或防护机制保证返回值非空。 |
| 387 | git-2.46.0 | describe_commit | cpp/inconsistent-null-check | 323 | FP | TP | 代码直接使用 `lookup_commit_reference` 的返回值 `cmit` 访问其成员（如 `cmit->object.oid`），而该函数可能返回 NULL（根据其内部实现 `lookup_commit_referen... |
| 393 | git-2.46.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1900 | FP | TP | 代码在调用 submodule_from_path 后未检查返回值是否为 NULL，随后直接解引用 sub->name，存在空指针解引用风险。切片中未见任何防护或确保非空的逻辑。 |
| 400 | git-2.46.0 | clear_common_flag | cpp/inconsistent-null-check | 2130 | FP | TP | 代码在调用 `lookup_object` 后未检查返回的 `obj` 是否为 NULL，便直接对其成员 `flags` 进行解引用操作，存在空指针解引用风险。切片中未显示任何前置校验能保证 `lookup_object` 返回非空。 |
| 401 | git-2.46.0 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 143 | FP | TP | 代码直接使用 parse_object 的返回值作为指针，未检查其是否为 NULL 就解引用 tag->tagged，存在空指针解引用风险。切片中未见任何前置检查或保证该调用不会返回 NULL 的逻辑。 |
| 420 | git-2.46.0 | add_patterns | cpp/invalid-pointer-deref | 1150 | FP | TP | 代码在分配大小为size的缓冲区后，执行了`buf[size++] = '\n';`，这明显是对缓冲区末尾之后一个字节的越界写入，存在内存损坏风险。切片中无任何防护或校验表明该操作是安全的。 |
| 421 | git-2.46.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1649 | FP | TP | 代码在解压循环后，无条件执行 `buffer[size] = '\0';` 写入操作。`buffer` 由 `xmallocz_gently(size)` 分配，大小为 `size` 字节，因此 `buffer[size]` 是分配内... |
| 425 | git-2.44.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 869 | FP | TP | 在第一个while循环的条件判断中，访问`s[off]`发生在检查`off < len - 1`之前，存在数组越界读取的风险。切片代码清晰地展示了这一错误的顺序。 |
| 429 | git-2.44.0 | bisect_successful | cpp/inconsistent-null-check | 640 | FP | TP | 函数 lookup_commit_reference_by_name 可能返回 NULL，但调用后未检查返回值就直接传递给 repo_format_commit_message 使用，存在空指针解引用风险。 |
| 430 | git-2.44.0 | update_head | cpp/inconsistent-null-check | 648 | FP | TP | 代码直接使用 lookup_commit_reference 的返回值，未检查其是否为 NULL，随后解引用 c->object.oid，存在空指针解引用风险。切片中未见任何前置校验或防护机制。 |
| 431 | git-2.44.0 | describe_commit | cpp/inconsistent-null-check | 320 | FP | TP | 代码直接使用 `lookup_commit_reference` 的返回值 `cmit` 访问其成员（如 `cmit->object.oid`），未检查返回值是否为 NULL。根据 `lookup_commit_reference_g... |
| 438 | git-2.44.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1838 | FP | TP | 代码在调用 submodule_from_path 后未检查返回值是否为 NULL，随后直接解引用 sub->name，存在空指针解引用风险。切片中未见任何防护或空值检查。 |
| 465 | git-2.44.0 | add_patterns | cpp/invalid-pointer-deref | 1117 | FP | TP | 代码在分配大小为size的缓冲区后，执行了`buf[size++] = '\n';`，这明显是在缓冲区末尾之后写入一个字节，属于典型的越界写入漏洞。切片代码中没有任何防护或校验来阻止此操作。 |
| 466 | git-2.44.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1647 | FP | TP | 代码在解压循环后，直接对 buffer[size] 进行写操作（buffer[size] = '\0'），而 buffer 是通过 xmallocz_gently(size) 分配的，其有效索引范围为 [0, size-1]，因此该写... |
| 484 | vim-9.1.0550 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数getcell可能返回NULL，但调用后未检查返回值，直接解引用cell->chars，存在空指针解引用风险。 |
| 486 | vim-9.1.0550 | get_isolated_shell_name | cpp/inconsistent-null-check | 2706 | FP | TP | 代码直接使用 vim_strnsave 的返回值，未检查其是否为 NULL。vim_strnsave 在内存分配失败时会返回 NULL，后续对 p 的解引用可能导致程序崩溃。 |
| 503 | vim-9.1.0550 | netbeans_keyname | cpp/unsafe-strcat | 2444 | FP | TP | 函数使用strcat向固定大小的缓冲区buf追加字符串，但未检查buf的剩余容量。当name指向较长的字符串（如'F12'）且ctrl、shift、alt标志被设置时，多次strcat调用可能导致缓冲区溢出。切片中未显示buf的大小，... |
| 505 | vim-9.1.0550 | do_put | cpp/unsafe-strcat | 2095 | FP | TP | 切片代码中直接使用了不安全的 `STRCAT` 宏（即 `strcat`），将 `y_array[y_size - 1]` 的内容拼接到 `newp` 缓冲区，而 `newp` 的大小为 `ml_get_len(lnum) - col... |
| 507 | vim-9.1.0550 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 '%6ld' 写入最多6位数字、符号和终止符，最多需要21字节，但目标缓冲区 tbuf 仅20字节，存在缓冲区溢出风险。 |
| 508 | vim-9.1.0550 | highlight_color | cpp/overrunning-write | 3254 | FP | TP | sprintf 目标缓冲区 'buf' 大小为10字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少10字节，当 rgb 值较大时（例如 0xffffffff），输出字符串长度可能超过10字节，导致缓冲区溢出。 |
| 509 | vim-9.1.0550 | msg_outnum | cpp/overrunning-write | 1555 | FP | TP | 目标缓冲区 'buf' 大小为20字节，但格式化输出长整型数 'n' 的字符串表示最多可能占用21字节（包括负号和终止空字符），存在缓冲区溢出风险。 |
| 510 | vim-9.1.0550 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 函数的目标缓冲区 'reply' 大小为 32 字节，但格式化字符串 "%d %ld\n" 在极端情况下（如 cmdno 为负数且结果值很大）可能产生超过 32 字节的输出，导致缓冲区溢出。切片代码中未显示任何对输入值... |
| 511 | vim-9.1.0550 | uc_check_code | cpp/overrunning-write | 1764 | FP | TP | sprintf 的目标缓冲区 num_buf 大小为 20 字节，但格式化长整型（%ld）的最大长度可能超过 20 字节（例如 -9223372036854775808 需要 21 字节），存在缓冲区溢出风险。 |
| 512 | vim-9.1.0550 | ga_concat_strings | cpp/unbounded-write | 788 | FP | TP | 代码使用不安全的strcpy函数，将长度未知的字符串((char_u **)(gap->ga_data))[i]复制到固定大小的缓冲区p中，且切片内未见任何对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 513 | vim-9.1.0550 | maketitle | cpp/unbounded-write | 4112 | FP | TP | 代码使用 STRCPY（即 strcpy）将指针 p 指向的字符串复制到 icon_str 缓冲区，而 p 来源于 gettail 函数处理的文件路径，其长度可能超过目标缓冲区大小（icon_str 指向 buf 或 p_iconst... |
| 514 | vim-9.1.0550 | buf_write | cpp/unbounded-write | 1208 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将fname复制到固定大小的IObuff缓冲区，未检查fname长度是否超过IObuff大小，存在缓冲区溢出风险。切片中未显示IObuff的大小定义，但strcpy的不安全使用模式是明确的。 |
| 517 | vim-9.1.0550 | transstr | cpp/unbounded-write | 366 | FP | TP | 切片代码显示，`res` 缓冲区的大小由 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 分配，但后续循环中多次使用 `STRCAT`（即 `strcat`）向其追加内容。`strcat`... |
| 516 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2138 | FP | TP | 切片代码中直接使用了未经验证的宏STRCAT（即strcat），将p_extra拼接到leader缓冲区，而leader缓冲区的大小是动态计算的（lead_len + lead_repl_len + extra_space + ext... |
| 519 | vim-9.1.0550 | win_redr_status_matches | cpp/unbounded-write | 634 | FP | TP | 代码使用STRCPY（即strcpy）宏将字符串复制到固定大小的缓冲区buf中，而源字符串s来自外部输入（如环境变量、文件读取等），其长度未经验证，可能导致缓冲区溢出。切片中未显示对s的长度检查或使用安全复制函数。 |
| 520 | vim-9.1.0550 | win_redr_status_matches | cpp/unbounded-write | 653 | FP | TP | 代码使用STRCPY（即strcpy）宏将transchar_byte函数的返回值复制到缓冲区，目标缓冲区大小固定（Columns+1或Columns*MB_MAXBYTES+1），而源字符串长度未知且未进行边界检查，存在缓冲区溢出风险。 |
| 521 | vim-9.1.0550 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的源字符串（fname + 3）复制到固定大小的目标缓冲区（name + 5），存在缓冲区溢出风险。切片中未显示对fname长度的检查或使用安全函数。 |
| 522 | vim-9.1.0550 | has_profiling | cpp/unbounded-write | 973 | FP | TP | 代码使用STRCPY（即strcpy）将fname复制到新分配的内存pe->pen_name，而fname是外部传入的字符串参数，其长度未经验证。虽然分配的内存大小为STRLEN(fname)+1，但STRCPY本身是不安全的函数，若... |
| 524 | vim-9.1.0550 | make_expanded_name | cpp/unbounded-write | 6918 | FP | TP | 代码使用STRCPY（即strcpy）将in_start的内容复制到新分配的缓冲区retval中，但未检查in_start的长度是否超过retval的大小。虽然retval的大小是根据temp_result、in_start和expr... |
| 525 | vim-9.1.0550 | make_expanded_name | cpp/unbounded-write | 6920 | FP | TP | 代码使用strcat拼接字符串，目标缓冲区retval的大小基于temp_result的长度计算，但后续递归调用make_expanded_name可能修改retval内容并重新分配，而告警点STRCAT(retval, expr_e... |
| 526 | vim-9.1.0550 | set_var_const | cpp/unbounded-write | 4183 | FP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname是用户提供的变量名，其长度未经验证，可能导致目标缓冲区溢出。切片中未显示对varname长度的限制或安全复制机制。 |
| 527 | vim-9.1.0550 | cat_prefix_varname | cpp/unbounded-write | 2504 | FP | TP | 代码使用strcpy将外部输入（name）复制到固定大小的缓冲区（varnamebuf），虽然缓冲区大小根据输入长度动态分配，但分配逻辑存在缺陷：分配前计算的长度len已包含name长度，但若varnamebuf为NULL或分配失败，... |
| 529 | vim-9.1.0550 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | TP | 代码在多个分支中直接使用 STRCPY（即 strcpy）将外部传入的 cmd 字符串复制到固定大小的缓冲区 buf 中，而 buf 的大小基于 cmd 的长度计算，但未考虑目标缓冲区大小限制，存在缓冲区溢出风险。 |
| 528 | vim-9.1.0550 | ex_substitute | cpp/unbounded-write | 4862 | FP | TP | 切片代码中直接使用了未进行边界检查的STRCAT宏（即strcat），将sub_firstline + copycol的内容追加到new_start缓冲区。new_start缓冲区的大小通过new_start_len管理，但追加前未检... |
| 531 | vim-9.1.0550 | ex_sort | cpp/unbounded-write | 605 | FP | TP | 代码使用STRCPY宏（即strcpy）将长度未知的源字符串`s`复制到固定大小的缓冲区`sortbuf1`中，而`sortbuf1`的大小仅基于`maxlen`分配（`maxlen + 1`），但`s`来自`ml_get`，其长度可... |
| 532 | vim-9.1.0550 | expand_sfile | cpp/unbounded-write | 9823 | FP | TP | 代码使用STRCPY（即strcpy）将可变长度的字符串repl复制到固定大小的缓冲区newres中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 533 | vim-9.1.0550 | repl_cmdline | cpp/unbounded-write | 5332 | FP | TP | 代码使用STRCPY（即strcpy）将未限制长度的源字符串复制到固定大小的缓冲区new_cmdline中，且切片内未见对源字符串长度进行校验或使用安全函数，存在缓冲区溢出风险。 |
| 535 | vim-9.1.0550 | replace_makeprg | cpp/unbounded-write | 5039 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串p复制到固定大小的缓冲区ptr，p来源于用户输入的命令行参数，可能导致缓冲区溢出。切片中未显示对p长度的检查或限制。 |
| 534 | vim-9.1.0550 | repl_cmdline | cpp/unbounded-write | 5338 | FP | TP | 代码使用STRCPY（即strcpy）将eap->nextcmd复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小i是根据多个字符串长度计算分配的，但未对eap->nextcmd的长度进行校验以确保其不会超... |
| 536 | vim-9.1.0550 | replace_makeprg | cpp/unbounded-write | 5054 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串（program和p）复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小是基于STRLEN(program)和STRLEN(p)计算分配的，但后续... |
| 537 | vim-9.1.0550 | do_one_cmd | cpp/unbounded-write | 2677 | FP | TP | 切片代码中明确使用了不安全的STRCPY宏（即strcpy），将未知长度的字符串（如来自环境变量、文件读取等）复制到固定大小的缓冲区IObuff中，存在缓冲区溢出风险。 |
| 539 | vim-9.1.0550 | get_exception_string | cpp/unbounded-write | 473 | FP | TP | 代码使用strcat向固定大小的缓冲区val追加内容，而val指向由vim_strnsave分配的缓冲区的一部分，其剩余空间大小未经验证。由于mesg和p的内容可能较长，strcat操作可能导致缓冲区溢出。 |
| 540 | vim-9.1.0550 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 代码使用`sprintf`将`&mesg[1]`（来自外部输入`mesg`）格式化写入固定缓冲区`val`，而`val`指向的缓冲区大小由`vim_strnsave`分配，其长度计算未考虑`sprintf`添加的额外字符`" (%s)... |
| 541 | vim-9.1.0550 | escape_fname | cpp/unbounded-write | 4072 | FP | TP | 代码使用strcpy将源字符串(*pp)复制到目标缓冲区(p+1)，目标缓冲区大小根据源字符串长度加2分配，但strcpy不检查目标缓冲区大小，若源字符串长度在分配后被修改或包含未预期的空终止符，可能导致缓冲区溢出。 |
| 544 | vim-9.1.0550 | <global> | cpp/unbounded-write | 5375 | FP | TP | sprintf 使用未限制长度的字符串 vim_tempdir 和递增的整数 temp_count 作为输入，目标缓冲区 itmp 大小固定为 TEMPNAMELEN，存在缓冲区溢出风险。 |
| 542 | vim-9.1.0550 | cmdline_browse_history | cpp/unbounded-write | 1484 | FP | TP | 代码使用STRCPY（即strcpy）将历史条目字符串p复制到ccline.cmdbuff，而目标缓冲区大小由alloc_cmdbuff根据p的长度分配，但分配后未检查p的长度是否超过缓冲区大小，存在缓冲区溢出风险。 |
| 543 | vim-9.1.0550 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 861 | FP | TP | 代码使用STRCPY（即strcpy）将动态长度的字符串p复制到固定缓冲区ccline.cmdbuff，虽然之前调用了realloc_cmdbuff(len + 1)来调整缓冲区大小，但STRCPY本身是不安全的，若后续代码或并发修改... |
| 545 | vim-9.1.0550 | vim_settempdir | cpp/unbounded-write | 5235 | FP | TP | 切片代码显示，当`vim_FullName`调用失败时，程序使用宏`STRCPY`（即`strcpy`）将未知长度的源字符串`tempdir`复制到固定大小的缓冲区`buf`中，而`buf`的大小为`MAXPATHL + 2`。由于`... |
| 548 | vim-9.1.0550 | buf_modname | cpp/unbounded-write | 3620 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的fname复制到新分配的缓冲区retval中，而retval的大小仅基于fnamelen + extlen + 3分配，未限制源字符串fname的长度，存在缓冲区溢出风险。 |
| 546 | vim-9.1.0550 | <global> | cpp/unbounded-write | 4352 | FP | TP | 代码使用`sprintf(tbuf, mesg, path)`，其中`tbuf`的大小基于`STRLEN(path) + STRLEN(mesg) + STRLEN(mesg2) + 2`计算，但`mesg`是包含`%s`格式符的字符... |
| 549 | vim-9.1.0550 | addfile | cpp/unbounded-write | 4196 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证的外部文件名`f`复制到新分配的缓冲区`p`，虽然`p`的大小基于`STRLEN(f) + 1`分配，但若`f`在分配后、复制前被并发修改或指向非字符串数据，仍可能导致缓冲区溢出。切片中... |
| 550 | vim-9.1.0550 | unix_expandpath | cpp/unbounded-write | 3833 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将路径字符串复制到缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中可见目标缓冲区大小由`buflen`定义，但未在复制前验证源字符串长度。 |
| 551 | vim-9.1.0550 | concat_fnames | cpp/unbounded-write | 3123 | FP | TP | 代码使用strcpy将fname1复制到新分配的缓冲区dest，虽然缓冲区大小通过STRLEN(fname1) + STRLEN(fname2) + 3计算，但strcpy本身不检查目标缓冲区大小，若fname1不是以空字符结尾的字符... |
| 552 | vim-9.1.0550 | concat_fnames | cpp/unbounded-write | 3126 | FP | TP | 函数使用strcat拼接两个输入字符串，但目标缓冲区大小仅基于两个输入字符串的当前长度计算，未考虑strcat会从目标缓冲区当前末尾开始写入，若fname1在STRCPY后未以空字符结尾或缓冲区计算有误，可能导致缓冲区溢出。切片中未显... |
| 554 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1720 | FP | TP | 代码中存在对STRCPY宏（即strcpy）的不安全调用，将外部输入（如rel_fname或*file_to_find）复制到固定大小的缓冲区NameBuff（大小为MAXPATHL），未检查源字符串长度是否超过目标缓冲区大小，存在缓... |
| 553 | vim-9.1.0550 | uniquefy_paths | cpp/unbounded-write | 2362 | FP | TP | 代码使用`STRCAT(file_pattern, pattern)`将`pattern`拼接到`file_pattern`，而`file_pattern`是通过`alloc(len + 2)`分配的，其大小仅比`pattern`长度... |
| 555 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1721 | FP | TP | 代码使用STRCPY（即strcpy）将rel_fname复制到NameBuff，然后紧接着用gettail的结果覆盖部分内容，但未检查目标缓冲区NameBuff（大小为MAXPATHL）是否足以容纳源字符串rel_fname和*fi... |
| 556 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1726 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串复制到固定大小的缓冲区NameBuff（大小为MAXPATHL），存在缓冲区溢出风险。切片显示源字符串来自用户输入或环境变量，且未进行长度检查。 |
| 557 | vim-9.1.0550 | ff_check_visited | cpp/unbounded-write | 1364 | FP | TP | 代码使用STRCPY（即strcpy）将ff_expand_buffer的内容复制到新分配的内存vp->ffv_fname中，目标缓冲区大小由STRLEN(ff_expand_buffer) + 1决定，但strcpy不检查边界，若源... |
| 560 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 936 | FP | TP | 代码在多个位置使用STRCPY（即strcpy）将可变长度的字符串复制到固定大小的缓冲区file_path中，虽然存在长度检查（STRLEN(...) + STRLEN(...) + 1 < MAXPATHL），但这些检查位于STRC... |
| 565 | vim-9.1.0550 | <global> | cpp/unbounded-write | 541 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区（如ff_expand_buffer，大小为MAXPATHL），且未检查源字符串长度，存在缓冲区溢出风险。 |
| 564 | vim-9.1.0550 | <global> | cpp/unbounded-write | 533 | FP | TP | 代码中多处使用STRCPY宏（即strcpy）将未知长度的字符串复制到固定大小的缓冲区（如ff_expand_buffer，大小为MAXPATHL），且源字符串（如search_ctx->ffsc_start_dir、search_c... |
| 567 | vim-9.1.0550 | <global> | cpp/unbounded-write | 586 | FP | TP | 切片代码中直接使用了未经验证长度的源字符串调用STRCPY（即strcpy），目标缓冲区大小未知，存在缓冲区溢出的风险。告警指出的多个输入源（如环境变量、文件读取）均未在切片内显示有长度检查或安全拷贝。 |
| 569 | vim-9.1.0550 | <global> | cpp/unbounded-write | 3793 | FP | TP | 代码使用 strcat 将未经验证长度的字符串 s 追加到缓冲区 r 中，而 r 的分配大小已固定，存在缓冲区溢出风险。 |
| 568 | vim-9.1.0550 | <global> | cpp/unbounded-write | 587 | FP | TP | 代码使用STRCAT宏（即strcat）将search_ctx->ffsc_wc_path拼接到temp缓冲区，但temp缓冲区的大小计算仅基于两个源字符串的长度，未预留终止空字符的空间，且未检查缓冲区边界，存在缓冲区溢出的风险。 |
| 570 | vim-9.1.0550 | foldDelMarker | cpp/unbounded-write | 1892 | FP | TP | 代码使用STRCPY宏（即strcpy）将源字符串p+len复制到目标缓冲区newline + (p - line)，未检查目标缓冲区大小。newline通过alloc分配，大小为ml_get_len(lnum) - len + 1，... |
| 572 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2899 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_prolog->title复制到固定大小的buffer[256]中，而title来源于外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 571 | vim-9.1.0550 | foldAddMarker | cpp/unbounded-write | 1810 | FP | TP | 代码使用STRCPY（即strcpy）将line复制到newline，而newline的分配大小基于line_len、markerlen和STRLEN(cms)计算，但STRCPY本身不检查目标缓冲区大小，若line长度超过分配大小（... |
| 573 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2901 | FP | TP | 代码使用STRCAT宏（即strcat）将res_prolog->title和res_prolog->version拼接到固定大小的buffer[256]中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 576 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2912 | FP | TP | 告警点 `STRCPY(buffer, res_cmap->title);` 中，目标缓冲区 `buffer` 大小为 256 字节，而源字符串 `res_cmap->title` 来自外部资源文件，其长度未在切片内进行验证或限制，存... |
| 574 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2905 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而res_cidfont->title是从外部资源文件读取的，其长度未经验证，存在缓冲区溢出风险。 |
| 575 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2907 | FP | TP | 代码使用STRCAT宏（即strcat）将res_cidfont->title和res_cidfont->version拼接到固定大小的buffer[256]中，未检查目标缓冲区长度，存在缓冲区溢出风险。 |
| 577 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2914 | FP | TP | 代码使用STRCAT宏（即strcat）将资源文件的标题和版本号拼接到固定大小的缓冲区buffer（256字节）中，未检查缓冲区边界。若拼接后的字符串长度超过256字节，将导致缓冲区溢出。 |
| 580 | vim-9.1.0550 | prt_resource_name | cpp/unbounded-write | 1659 | FP | TP | 代码使用strcpy进行字符串复制，虽然对源字符串长度进行了检查，但检查的目标是filename而非目标缓冲区resource_filename的大小。目标缓冲区的大小未知，存在缓冲区溢出风险。 |
| 579 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2922 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的字符串（如res_encoding->title和res_encoding->version）长度未经验证，存在缓冲区溢出的风险。 |
| 578 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2920 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_encoding->title复制到固定大小的buffer[256]中，而title来源于外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 581 | vim-9.1.0550 | do_helptags | cpp/unbounded-write | 1206 | FP | TP | 代码中直接使用STRCPY（即strcpy）将参数dirname复制到固定大小的缓冲区NameBuff中，未检查目标缓冲区大小，存在缓冲区溢出风险。告警指出输入可能来自环境变量等外部源，切片中未见任何长度校验。 |
| 582 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 971 | FP | TP | 代码使用STRCAT宏（即strcat）向NameBuff缓冲区追加内容，而NameBuff的大小未知，且切片中未显示其大小定义或边界检查。根据告警，输入来自fread读取的字符串，可能导致缓冲区溢出。 |
| 584 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 1108 | FP | TP | sprintf 使用未限制长度的动态字符串 p1 和 fname 作为输入，目标缓冲区 s 的大小仅根据这两个字符串的长度计算，未进行边界检查，存在缓冲区溢出风险。 |
| 586 | vim-9.1.0550 | load_colors | cpp/unbounded-write | 602 | FP | TP | sprintf 使用未经验证的输入 'name' 直接格式化字符串到固定大小的缓冲区 'buf'，缓冲区大小仅为 STRLEN(name) + 12，而格式化字符串 "colors/%s.vim" 的长度加上 name 的长度可能超过... |
| 587 | vim-9.1.0550 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | sprintf 使用未经验证的字符串拼接，目标缓冲区 `fullname` 的大小 `len` 可能小于拼接后字符串的长度，存在缓冲区溢出风险。切片代码中未显示对输入 `name` 或路径长度的安全校验。 |
| 588 | vim-9.1.0550 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | TP | 代码使用`sprintf`将多个字符串拼接写入固定大小的缓冲区`buf`，缓冲区大小`amt`的计算依赖于`strlen`对输入参数的测量。如果输入参数（如`tagstr`、`fname`、`slno`、`search`）在调用此函数... |
| 590 | vim-9.1.0550 | <global> | cpp/unbounded-write | 1456 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，未检查源字符串长度是否超过目标缓冲区大小。虽然目标缓冲区大小根据strlen(fname)+1分配，但若fname在分配后、复制前被恶意修改（如并发环境），仍可能导致溢出。切片中未... |
| 591 | vim-9.1.0550 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是函数参数，其长度未经验证。虽然分配了strlen(fname)+1的空间，但strcpy本身不检查边界，若fname在调用后被恶意修改或来源不可信，仍存在缓冲区溢出风险... |
| 592 | vim-9.1.0550 | cs_add_common | cpp/unbounded-write | 604 | FP | TP | 代码使用`sprintf`拼接`fname`和`CSCOPE_DBFILE`，`fname`来自用户输入且经过环境变量展开，长度可能超过目标缓冲区`fname2`的大小（`strlen(CSCOPE_DBFILE) + strlen(... |
| 593 | vim-9.1.0550 | ins_compl_infercase_gettext | cpp/unbounded-write | 658 | FP | TP | 代码使用STRCPY（即strcpy）将IObuff的内容复制到gap.ga_data中，但未检查IObuff的长度是否超过gap.ga_data的缓冲区大小。IObuff是一个固定大小的数组（IOSIZE），而gap.ga_data... |
| 594 | vim-9.1.0550 | <global> | cpp/unbounded-write | 3097 | FP | TP | 代码使用`sprintf`将`transchar(from)`的结果写入固定大小的缓冲区`args->os_errbuf`，而`transchar`的返回值长度未受限制，可能导致缓冲区溢出。切片中未见任何对目标缓冲区大小的检查或使用安... |
| 596 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2157 | FP | TP | 代码使用STRCPY（即strcpy）将fix_fname返回的字符串f复制到新分配的内存s中，s的大小为STRLEN(f)+1，仅比源字符串长度多一个字节用于空终止符。如果fix_fname函数在某些情况下（例如处理包含'..'或'... |
| 597 | vim-9.1.0550 | <global> | cpp/unbounded-write | 811 | FP | TP | 代码使用宏 STRCPY（即 strcpy）将 call_data 字符串复制到固定大小的缓冲区 menu->strings[i] 中，而 menu->strings[i] 的大小仅通过 alloc(STRLEN(call_data)... |
| 599 | vim-9.1.0550 | msg_show_console_dialog | cpp/unbounded-write | 4387 | FP | TP | 代码使用STRCPY宏（即strcpy）将message字符串复制到confirm_msg缓冲区，而confirm_msg的大小仅由len决定，len的计算包含了STRLEN(message)，但未预留额外的空间来容纳源字符串的终止空... |
| 598 | vim-9.1.0550 | <global> | cpp/unbounded-write | 815 | FP | TP | 代码中直接使用宏 STRCPY（即 strcpy）将 call_data 复制到固定大小的缓冲区 menu->strings[i] 中，而 menu->strings[i] 的大小仅通过 alloc(STRLEN(call_data)... |
| 600 | vim-9.1.0550 | str2specialbuf | cpp/unbounded-write | 1919 | FP | TP | 切片代码显示，在调用strcat前仅检查了当前拼接后的总长度是否小于目标缓冲区长度len，但未检查每次拼接时目标缓冲区buf的剩余空间。如果buf在循环过程中被其他代码修改或初始长度不为零，可能导致缓冲区溢出。这是一个真实的安全缺陷。 |
| 602 | vim-9.1.0550 | may_trigger_modechanged | cpp/unbounded-write | 2821 | FP | TP | 代码使用STRCPY（即strcpy）将curr_mode复制到last_mode，而last_mode未在切片中声明其大小，且curr_mode来自get_mode函数，其内容长度可能超过MODE_MAX_LENGTH，存在缓冲区溢... |
| 601 | vim-9.1.0550 | get_emsg_source | cpp/unbounded-write | 484 | FP | TP | 代码使用`sprintf`将`sname`和`p`格式化到`Buf`中，`Buf`的大小由`STRLEN(sname) + STRLEN(p)`分配，但`sprintf`写入的字符串长度是`strlen(p) - 2 + strlen... |
| 604 | vim-9.1.0550 | call_shell | cpp/unbounded-write | 1877 | FP | TP | 代码使用strcat向固定大小的缓冲区ncmd追加内容，ncmd的大小基于ecmd和p_sxq的长度计算，但未考虑strcat追加时目标缓冲区已有内容，可能导致缓冲区溢出。 |
| 607 | vim-9.1.0550 | push_showcmd | cpp/unbounded-write | 1805 | FP | TP | 代码直接使用不安全的strcpy宏将内容从showcmd_buf复制到old_showcmd_buf，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 606 | vim-9.1.0550 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf 使用未受控的 `result` 参数作为格式化字符串的一部分，而 `result` 可能来自外部输入（如环境变量、文件读取等），且分配的缓冲区大小仅为 `STRLEN(result) + 32`，当 `result` ... |
| 605 | vim-9.1.0550 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 代码中直接使用STRCAT宏（即strcat）拼接字符串，未检查目标缓冲区大小，存在缓冲区溢出风险。告警指出输入可能来自环境变量、文件读取等外部源，切片中未见任何长度校验或边界检查。 |
| 609 | vim-9.1.0550 | op_change | cpp/unbounded-write | 1866 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将源字符串复制到目标缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未显示任何边界检查或安全防护措施。 |
| 611 | vim-9.1.0550 | op_replace | cpp/unbounded-write | 1171 | FP | TP | 代码中直接使用不安全的STRCPY（即strcpy）宏，将源字符串复制到固定大小的目标缓冲区，且切片中未显示对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 610 | vim-9.1.0550 | op_replace | cpp/unbounded-write | 1162 | FP | TP | 代码中直接使用STRCPY（即strcpy）宏，将源字符串复制到目标缓冲区，未检查源字符串长度是否超过目标缓冲区大小。切片代码显示目标缓冲区`newp`的大小为`oldlen + 1 + n`，而源字符串来自`oldp + bd.te... |
| 612 | vim-9.1.0550 | op_delete | cpp/unbounded-write | 825 | FP | TP | 代码使用STRCPY宏（即strcpy）将源字符串复制到新分配的缓冲区，但未检查源字符串长度是否小于目标缓冲区大小。目标缓冲区大小由`ml_get_len(lnum) + 1 - n`计算，而源字符串`oldp + bd.textco... |
| 613 | vim-9.1.0550 | block_insert | cpp/unbounded-write | 607 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串oldp复制到目标缓冲区newp + offset，目标缓冲区newp的大小由alloc分配，其大小计算复杂且依赖于多个变量，而源字符串oldp来自ml_get获取的行内容，其长度可能超... |
| 614 | vim-9.1.0550 | option_value2string | cpp/unbounded-write | 8155 | FP | TP | 代码使用STRCPY（即strcpy）将get_special_key_name的返回值复制到NameBuff，而get_special_key_name返回的静态缓冲区string最大长度为MAX_KEY_NAME_LEN+1，但N... |
| 617 | vim-9.1.0550 | set_init_default_backupskip | cpp/unbounded-write | 169 | FP | TP | 代码使用STRCPY（即strcpy）将环境变量值复制到固定大小的缓冲区item，而item的大小仅基于环境变量字符串长度加3分配，未考虑目标缓冲区大小限制，存在缓冲区溢出风险。 |
| 616 | vim-9.1.0550 | stropt_expand_envvar | cpp/unbounded-write | 1757 | FP | TP | 代码使用STRCPY（即strcpy）将option_expand返回的字符串s复制到newval中，newval的大小由alloc(newlen)分配，而newlen的计算依赖于STRLEN(s) + 1，但s来自expand_en... |
| 618 | vim-9.1.0550 | mch_expand_wildcards | cpp/unbounded-write | 6931 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区`command`追加内容，而`command`的大小`len`是根据多个变量（如`tempname`、`pat`等）的长度计算分配的。如果这些输入变量的总长度超过`len`的... |
| 619 | vim-9.1.0550 | mch_expand_wildcards | cpp/unbounded-write | 7277 | FP | TP | 代码在循环中使用STRCPY宏（即strcpy）将长度未知的字符串复制到固定大小的缓冲区p中，p的大小仅为目标字符串长度加1，未检查源字符串长度，存在缓冲区溢出风险。 |
| 620 | vim-9.1.0550 | mch_FullName | cpp/unbounded-write | 2816 | FP | TP | 代码在调用STRCAT（即strcat）前，仅检查了目标缓冲区buf和源字符串fname的总长度是否小于len，但未检查buf的剩余空间是否足以容纳fname。strcat会从buf的当前结尾开始追加，若buf中已有内容，则存在缓冲区... |
| 621 | vim-9.1.0550 | qf_store_title | cpp/unbounded-write | 1932 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的title字符串复制到新分配的缓冲区p中，虽然p的大小根据STRLEN(title)+2分配，但title可能来自不可信源（如环境变量、文件读取等），且切片中未显示对title长度进行... |
| 622 | vim-9.1.0550 | reg_submatch | cpp/unbounded-write | 2689 | FP | TP | 代码在多个位置使用STRCPY（即strcpy）宏，将长度未知的源字符串（如来自reg_getline_submatch的返回值）复制到固定大小的缓冲区retval中，而retval的大小仅由alloc(len)分配，但strcpy调... |
| 623 | vim-9.1.0550 | reg_submatch | cpp/unbounded-write | 2698 | FP | TP | 代码在循环中使用 STRCPY（即 strcpy）将 reg_getline_submatch 返回的字符串复制到固定大小的缓冲区 retval 中，而 retval 的大小仅由 alloc(len) 分配，但复制前未检查源字符串长度... |
| 624 | vim-9.1.0550 | regtilde | cpp/unbounded-write | 1925 | FP | TP | 代码使用STRCPY（即strcpy）将postfix复制到tmpsub缓冲区，其目标缓冲区大小tmpsublen+1由alloc分配，但postfix长度postfixlen未经验证，若postfixlen大于tmpsublen -... |
| 625 | vim-9.1.0550 | match_with_backref | cpp/unbounded-write | 1600 | FP | TP | 代码使用STRCPY（即strcpy）将rex.line复制到reg_tofree，而reg_tofree的大小仅基于STRLEN(rex.line) + 50分配，若rex.line在分配后、复制前被修改或增长，或存在并发修改，可能... |
| 626 | vim-9.1.0550 | get_reg_contents | cpp/unbounded-write | 2668 | FP | TP | 代码使用不安全的strcpy函数，将y_current->y_array[i]的内容复制到目标缓冲区retval + len，而目标缓冲区的大小是根据字符串长度累加预先分配的，但strcpy不检查目标缓冲区大小，若源字符串未正确以空字... |
| 628 | vim-9.1.0550 | do_put | cpp/unbounded-write | 2095 | FP | TP | 切片代码中直接使用了未经验证长度的外部输入（如环境变量、文件读取内容）作为strcat的源字符串，目标缓冲区大小未知，存在缓冲区溢出风险。 |
| 627 | vim-9.1.0550 | do_put | cpp/unbounded-write | 2094 | FP | TP | 切片代码中直接使用了未经验证长度的源字符串（如 y_array[i]）调用 STRCPY（即 strcpy）宏，目标缓冲区大小未知，存在缓冲区溢出风险。 |
| 629 | vim-9.1.0550 | op_yank | cpp/unbounded-write | 1278 | FP | TP | 代码中直接使用不安全的strcpy宏（STRCPY）进行字符串拼接，目标缓冲区大小由alloc动态分配，但分配大小基于两个源字符串长度之和，未考虑strcpy可能导致的缓冲区溢出风险。 |
| 630 | vim-9.1.0550 | op_yank | cpp/unbounded-write | 1279 | FP | TP | 代码使用STRCAT宏（即strcat）拼接两个字符串，目标缓冲区pnew的大小为两个源字符串长度之和加1，但strcat不检查目标缓冲区剩余空间，若源字符串长度计算有误或缓冲区被修改，可能导致缓冲区溢出。切片中未显示对pnew缓冲区... |
| 632 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2755 | FP | TP | 代码使用strcat将用户输入（name参数）拼接到固定大小的缓冲区（scriptname）中，而scriptname的分配大小仅基于name的长度加上固定偏移，未考虑拼接后字符串的总长度可能超过缓冲区容量，存在缓冲区溢出风险。 |
| 633 | vim-9.1.0550 | ExpandPackAddDir | cpp/unbounded-write | 1226 | FP | TP | sprintf 使用未经验证的用户输入 `pat` 作为格式化字符串的一部分，目标缓冲区 `s` 的大小为 `pat_len + 26`，但格式化字符串 `"pack/*/opt/%s*"` 在拼接 `pat` 后可能超过该缓冲区大小... |
| 631 | vim-9.1.0550 | stuff_yank | cpp/unbounded-write | 452 | FP | TP | 代码使用STRCPY（即strcpy）将字符串从*pp复制到新分配的内存lp，目标缓冲区大小基于STRLEN(*pp) + STRLEN(p) + 1计算，但*pp的内容可能来自外部输入（如环境变量、文件读取等），若其长度被恶意修改或... |
| 635 | vim-9.1.0550 | dump_word | cpp/unbounded-write | 4187 | FP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或外部数据（如环境变量、文件读取内容），且切片中未显示对p的长度进行任何校验，存在缓冲区溢出风险。 |
| 634 | vim-9.1.0550 | sign_jump | cpp/unbounded-write | 1324 | FP | TP | sprintf 使用未限制长度的缓冲区 buf->b_fname 作为格式化字符串的一部分，且目标缓冲区 cmd 的大小仅基于 buf->b_fname 的当前长度加上固定偏移分配，若 buf->b_fname 在分配后、sprint... |
| 636 | vim-9.1.0550 | make_case_word | cpp/unbounded-write | 3140 | FP | TP | 代码直接使用不安全的strcpy宏复制字符串，未检查目标缓冲区大小，且切片中未显示对源字符串fword的长度有任何限制或验证，存在缓冲区溢出风险。 |
| 637 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2998 | FP | TP | 代码使用STRCPY宏（即strcpy）将repl_to复制到新分配的缓冲区p中，未检查目标缓冲区大小。repl_to是全局变量，其长度可能超过目标缓冲区p中剩余的空间，导致缓冲区溢出。 |
| 638 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2999 | FP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p中，但p的大小为ml_get_curline_len() + addlen + 1，而拼接的源字符串长度未经验证，可能导致缓冲区溢出。切片中未见对源字符串长度的检查或... |
| 639 | vim-9.1.0550 | count_common_word | cpp/unbounded-write | 1919 | FP | TP | 代码使用STRCPY（即strcpy）将长度未知的字符串p复制到新分配的内存wc->wc_word中，分配大小基于STRLEN(p)计算，但strcpy不检查目标缓冲区大小，若p在复制前被修改或分配计算有误，可能导致缓冲区溢出。切片中... |
| 640 | vim-9.1.0550 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）将参数`lang`复制到固定大小的结构体字段`sl.sl_lang`中，但切片中未显示`sl.sl_lang`的大小定义，也未对`lang`的长度进行任何校验。由于`lang`是函数参数，其来源可... |
| 641 | vim-9.1.0550 | spell_move_to | cpp/unbounded-write | 1420 | FP | TP | 代码使用STRCPY宏（即strcpy）将长度不确定的字符串`line`复制到固定大小的缓冲区`buf`中，而`buf`的大小基于`len + MAXWLEN + 2`分配，但`line`可能包含空字符，导致strcpy复制超过`le... |
| 643 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2369 | FP | TP | 代码使用STRCAT宏（即strcat）将items[0]和items[1]拼接到缓冲区p中，而p的大小仅根据spin->si_info、items[0]和items[1]的长度计算，未考虑strcat可能导致的缓冲区溢出风险。 |
| 644 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2371 | FP | TP | 代码使用STRCAT宏（即strcat）将items[1]拼接到指针p指向的缓冲区，而p的空间分配仅基于items[0]和items[1]的长度计算，未考虑p的原始内容长度，可能导致缓冲区溢出。 |
| 645 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2464 | FP | TP | 代码使用STRCPY宏（即strcpy）将items[1]复制到缓冲区p，而items[1]来源于外部文件读取的未经验证的行数据，可能导致目标缓冲区溢出。切片中未显示对items[1]长度的检查或安全限制。 |
| 646 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2495 | FP | TP | 代码在拼接字符串时使用STRCAT宏（即strcat），目标缓冲区大小未知，且源字符串来自fgets读取的文件行，可能导致缓冲区溢出。切片中未显示目标缓冲区的大小检查或边界限制。 |
| 648 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2746 | FP | TP | 代码中使用 sprintf 将 items[4] 拼接到固定大小的缓冲区 buf 中，items[4] 来源于外部文件读取，未检查长度，存在缓冲区溢出风险。 |
| 649 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2748 | FP | TP | 切片代码中第2748行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，其长度未经验证，可能导致缓冲区溢出。 |
| 651 | vim-9.1.0550 | suggest_try_change | cpp/unbounded-write | 1199 | FP | TP | 代码使用STRCPY宏（即strcpy）将su->su_fbadword复制到固定大小的缓冲区fword[MAXWLEN]中，未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 654 | vim-9.1.0550 | expand_tag_fname | cpp/unbounded-write | 4121 | FP | TP | 代码使用不安全的STRCPY（即strcpy）将tag_fname复制到固定大小的缓冲区retval（大小为MAXPATHL），而tag_fname的来源（如环境变量、文件读取等）在切片中未显示有长度限制，存在缓冲区溢出风险。 |
| 653 | vim-9.1.0550 | concat_str | cpp/unbounded-write | 770 | FP | TP | 函数`concat_str`使用`STRCPY`（即`strcpy`）进行字符串复制，其目标缓冲区`dest`的大小由`alloc`根据源字符串长度计算分配，但`strcpy`本身不检查边界，若源字符串未正确以空字符结尾（例如`str... |
| 655 | vim-9.1.0550 | findtags_add_match | cpp/unbounded-write | 2624 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的目标缓冲区，且未在切片内看到对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 657 | vim-9.1.0550 | show_one_termcode | cpp/unbounded-write | 7058 | FP | TP | 代码使用STRCPY（即strcpy）将get_special_key_name返回的字符串复制到IObuff+5位置，但未检查目标缓冲区IObuff的大小，且源字符串p的长度可能超过IObuff的剩余空间，存在缓冲区溢出风险。 |
| 659 | vim-9.1.0550 | uc_check_code | cpp/unbounded-write | 1691 | FP | TP | 代码在多个分支中直接使用STRCPY（即strcpy）将外部输入（如eap->arg）复制到固定大小的缓冲区buf中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 658 | vim-9.1.0550 | current_tagblock | cpp/unbounded-write | 1386 | FP | TP | sprintf 使用未限制长度的字符串 p 作为格式化输入，且 p 来自 ml_get_cursor() 获取的缓冲区内容，其长度可能超过目标缓冲区 spat/epat 的分配大小（len + 39 或 len + 9），存在缓冲区溢... |
| 656 | vim-9.1.0550 | findtags_add_match | cpp/unbounded-write | 2703 | FP | TP | 代码中直接使用 STRCPY（即 strcpy）将 st->tag_fname、st->ebuf、st->lbuf 等字符串复制到固定大小的缓冲区 mfp 中，而 mfp 的大小由 alloc 根据字符串长度计算分配，但 STRCPY... |
| 660 | vim-9.1.0550 | get_scriptlocal_funcname | cpp/unbounded-write | 4608 | FP | TP | 代码使用STRCAT宏（即strcat）将未经验证长度的字符串拼接到固定大小的缓冲区newname中，newname的大小仅根据sid_buf和p+off的长度分配，但strcat操作未检查目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 663 | vim-9.1.0550 | fname_trans_sid | cpp/unbounded-write | 2127 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串（name + llen）复制到固定大小的缓冲区（fname_buf + i 或动态分配的fname），未检查源字符串长度是否小于目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 661 | vim-9.1.0550 | trans_function_name_ext | cpp/unbounded-write | 4521 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将sid_buf的内容复制到目标缓冲区，而sid_buf的大小为20字节，但复制源sid_buf可能包含格式化后的字符串，其长度未进行限制检查，存在缓冲区溢出风险。 |
| 662 | vim-9.1.0550 | fname_trans_sid | cpp/unbounded-write | 2115 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串`name + llen`复制到固定大小的缓冲区`fname_buf + i`中，虽然存在长度检查`i + STRLEN(name + llen) < FLEN_FIXED`... |
| 664 | vim-9.1.0550 | set_ufunc_name | cpp/unbounded-write | 663 | FP | TP | 代码使用不安全的strcpy函数，将外部传入的字符串name复制到固定大小的缓冲区fp->uf_name中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 666 | vim-9.1.0550 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到固定大小的缓冲区`funcname`中，而`funcname`的大小仅为`STRLEN(name) + 3`，未预留终止符空间，导致strcpy可能写入超出分配的内存边... |
| 667 | vim-9.1.0550 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | TP | 代码使用STRCPY（即strcpy）将变量name复制到newsav->sav_key，而name是函数参数，其长度可能超过目标缓冲区大小（newsav->sav_key的空间仅为STRLEN(name)+1），存在缓冲区溢出风险。 |
| 668 | vim-9.1.0550 | find_exported | cpp/unbounded-write | 756 | FP | TP | 代码使用`sprintf`将外部输入（`script->sn_autoload_prefix`和`name`）写入固定大小的缓冲区`buffer[200]`或动态分配的`funcname`，但动态分配的大小`len`仅基于输入字符串长... |
| 669 | vim-9.1.0550 | find_exported | cpp/unbounded-write | 763 | FP | TP | 代码使用`sprintf`将外部输入`name`和`sid`格式化到固定大小的缓冲区`funcname`中，`name`参数来自函数外部调用，其长度未经验证，存在缓冲区溢出风险。 |
| 671 | vim-9.1.0550 | ExpandBufnames | cpp/invalid-pointer-deref | 2904 | FP | TP | 切片代码显示，在`round == 1`且`!fuzzy`时，`*file`指针通过`alloc`分配内存，但分配大小`count`在循环中递增，存在写入时`count`超出分配大小的风险，导致越界写入。 |
| 670 | vim-9.1.0550 | xxdline | cpp/unbounded-write | 533 | FP | TP | 函数`xxdline`中的`strcpy(z, l)`调用，目标缓冲区`z`为固定大小的静态数组（大小`LLEN+1`），而源字符串`l`是函数参数，其内容未在切片代码中显示任何验证或长度检查。这可能导致缓冲区溢出，符合规则描述的潜在风险。 |
| 665 | vim-9.1.0550 | exec_instructions | cpp/unbounded-write | 3487 | FP | TP | 切片代码中明确使用了不安全的 STRCPY 宏（即 strcpy），且目标缓冲区 'cmd' 的大小由运行时计算的 'len' 决定，而源字符串 'str' 来自栈上的变量，其长度未经验证。这可能导致缓冲区溢出，符合 unbounde... |
| 695 | vim-9.1.1591 | netbeans_keyname | cpp/unsafe-strcat | 2449 | FP | TP | 函数使用strcat向固定大小的缓冲区buf追加内容，但未检查buf的剩余容量。当name指向较长的字符串（如'F12'）且ctrl、shift、alt标志被设置时，多次strcat调用可能导致缓冲区溢出。切片中未显示buf的大小，也... |
| 700 | vim-9.1.1591 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 的目标缓冲区 'reply' 大小为 32 字节，但格式化字符串 "%d %ld\n" 在最坏情况下（如 cmdno 为负数且 result 为长整型最小值）可能产生超过 32 字节的输出，导致缓冲区溢出。切片代码中未... |
| 764 | vim-9.1.1591 | cs_resolve_file | cpp/unbounded-write | 2438 | FP | TP | sprintf 使用 csinfo[i].ppath 和 name 拼接，目标缓冲区 fullname 的大小为 len，而 len 的计算包含了这两个字符串的长度，但未为 sprintf 添加的 '/' 分隔符和字符串终止符预留空间... |
| 765 | vim-9.1.1591 | cs_make_vim_style_matches | cpp/unbounded-write | 1639 | FP | TP | 代码使用`sprintf`将多个字符串拼接写入固定大小的缓冲区`buf`，缓冲区大小`amt`的计算已包含所有源字符串的长度及定界符，确保了目标缓冲区大小足够，因此不存在缓冲区溢出风险，属于误报。 |
| 768 | vim-9.1.1591 | <global> | cpp/unbounded-write | 1463 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，未检查目标缓冲区大小，而fname是函数参数，其长度可能超过分配的大小，存在缓冲区溢出风险。 |
| 769 | vim-9.1.1591 | cs_add_common | cpp/unbounded-write | 603 | FP | TP | sprintf 使用未限制长度的字符串拼接，fname 和 CSCOPE_DBFILE 的长度可能超过 fname2 的分配大小，存在缓冲区溢出风险。 |
| 767 | vim-9.1.1591 | <global> | cpp/unbounded-write | 1454 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，而fname是函数参数，其长度可能超过目标缓冲区大小。虽然分配了strlen(fname)+1字节，但strcpy本身不检查边界，若fname在分配后被修改或存在并发问题，仍可能导... |
| 782 | vim-9.1.1591 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | 代码使用`sprintf`将外部输入`result`和整数`cmdno`格式化写入固定大小的缓冲区`reply`，而`reply`的大小仅基于`result`的当前长度分配，未考虑格式化字符串`"%d %s\n"`引入的额外字符，存在... |
| 781 | vim-9.1.1591 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 代码中直接使用STRCAT宏（即strcat）拼接字符串，未检查目标缓冲区大小，存在缓冲区溢出风险。告警点位于'insert'命令处理逻辑中，拼接的源字符串来自外部输入（args），目标缓冲区newline的大小为ml_get_len... |
| 850 | vim-9.1.1040 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数`getcell`在越界或缓冲区为空时返回NULL，但调用点`vterm_screen_is_eol`未检查返回值，直接解引用`cell->chars[0]`，存在空指针解引用风险。 |
| 852 | vim-9.1.1040 | get_isolated_shell_name | cpp/inconsistent-null-check | 2721 | FP | TP | 函数`vim_strnsave`可能返回NULL，但调用后未检查返回值便直接赋值给指针`p`并返回，存在空指针解引用风险。切片中未显示任何对`p`的后续空值检查或防护。 |
| 865 | vim-9.1.1040 | barline_parse | cpp/inconsistent-null-check | 1153 | FP | TP | 代码在条件分支中调用 vim_strnsave 后未检查返回值是否为 NULL，直接将其赋值给指针变量 s 并随后使用，存在空指针解引用的风险。切片中未显示任何针对此返回值的空指针检查。 |
| 869 | vim-9.1.1040 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 '%6ld' 写入最多6位数字加符号和终止符，最多需要8字节，但目标缓冲区 tbuf 大小为20字节，足够容纳，因此告警是误报。缓冲区大小足以安全存储格式化后的行号字符串。 |
| 871 | vim-9.1.1040 | msg_outnum | cpp/overrunning-write | 1653 | FP | TP | 目标缓冲区`buf`大小为20字节，但`sprintf`写入格式为`%ld`的`long`类型整数，当`n`为最小值`-9223372036854775808`（长度为20个字符加1个空终止符）时，需要21字节，存在缓冲区溢出风险。 |
| 872 | vim-9.1.1040 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 函数将格式化的字符串写入大小为 32 字节的栈数组 reply 中，格式化字符串 "%d %ld\n" 在最坏情况下（如 cmdno 为负大整数，result 为负长整数）的长度可能超过 32 字节，导致缓冲区溢出。切... |
| 873 | vim-9.1.1040 | ga_concat_strings | cpp/unbounded-write | 788 | FP | TP | 代码使用不安全的strcpy函数，将gap->ga_data中的字符串复制到固定大小的缓冲区s中，而s的大小仅由字符串长度总和计算得出，未考虑strcpy会复制源字符串的终止空字符，导致目标缓冲区可能缺少一个字节的空间，存在缓冲区溢出... |
| 870 | vim-9.1.1040 | highlight_color | cpp/overrunning-write | 3259 | FP | TP | sprintf 目标缓冲区 buf 大小为 10 字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少 8 个字符（# + 6个十六进制数字 + '\0'），计算为 8 字节，未超过 10 字节。然而，告警指出需要... |
| 874 | vim-9.1.1040 | maketitle | cpp/unbounded-write | 4147 | FP | TP | 代码使用STRCPY宏（即strcpy）将指针p的内容复制到icon_str缓冲区，而p指向的文件名长度可能超过目标缓冲区大小（IOSIZE），且切片中未见对源字符串长度的限制检查，存在缓冲区溢出风险。 |
| 875 | vim-9.1.1040 | buf_write | cpp/unbounded-write | 1208 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将fname复制到固定大小的IObuff缓冲区，未检查fname长度是否超过IObuff大小，存在缓冲区溢出风险。切片中未显示IObuff的大小定义，但strcpy的不安全使用模式是明确的。 |
| 878 | vim-9.1.1040 | transstr | cpp/unbounded-write | 400 | FP | TP | 代码使用STRCAT宏（即strcat）将transchar_byte函数的返回值追加到res缓冲区，但res缓冲区的大小是根据输入字符串s计算的长度（len或vim_strsize(s)）加上1分配的，而transchar_byte... |
| 877 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2138 | FP | TP | 代码中直接使用STRCAT宏（即strcat）将p_extra拼接到leader缓冲区，而leader缓冲区的大小是动态计算的（lead_len + lead_repl_len + extra_space + extra_len + ... |
| 881 | vim-9.1.1040 | win_redr_status_matches | cpp/unbounded-write | 659 | FP | TP | 代码使用STRCPY（即strcpy）将transchar_byte函数的返回值复制到缓冲区，目标缓冲区大小固定（Columns+1或Columns*MB_MAXBYTES+1），但源字符串长度未经验证，存在缓冲区溢出风险。 |
| 880 | vim-9.1.1040 | win_redr_status_matches | cpp/unbounded-write | 640 | FP | TP | 代码使用STRCPY（即strcpy）宏将字符串复制到固定大小的缓冲区buf中，而buf的大小基于Columns分配。源字符串s来自外部输入（如环境变量、文件读取等），其长度未经验证，可能导致缓冲区溢出。 |
| 882 | vim-9.1.1040 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串fname复制到新分配的内存name中，未检查目标缓冲区大小。由于fname是函数参数，其长度可能超过name的分配大小（STRLEN(fname) + 3），导致缓冲区溢出。 |
| 883 | vim-9.1.1040 | has_profiling | cpp/unbounded-write | 973 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的源字符串fname复制到固定大小的目标缓冲区pe->pen_name，存在缓冲区溢出风险。切片中未显示对fname长度的检查或使用安全函数。 |
| 885 | vim-9.1.1040 | do_string_sub | cpp/unbounded-write | 7726 | FP | TP | 代码在STRCPY宏（即strcpy）调用时，目标缓冲区ga.ga_data + ga.ga_len的大小未明确验证，而源字符串tail的长度可能超过剩余空间，存在缓冲区溢出风险。切片中未见对目标缓冲区大小的检查或对源字符串长度的限制。 |
| 886 | vim-9.1.1040 | set_var_const | cpp/unbounded-write | 4184 | FP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname长度未受限制，可能导致目标缓冲区溢出。切片中未显示对varname长度的检查或安全复制措施。 |
| 887 | vim-9.1.1040 | cat_prefix_varname | cpp/unbounded-write | 2505 | FP | TP | 代码使用不安全的strcpy函数，将外部传入的name字符串复制到固定大小的缓冲区varnamebuf+2位置，而缓冲区大小仅通过alloc(len)分配，未对name的长度进行限制，存在缓冲区溢出风险。 |
| 884 | vim-9.1.1040 | ex_diffpatch | cpp/unbounded-write | 1363 | FP | TP | 代码中直接使用 STRCPY（即 strcpy）将 tmp_new 复制到 buf，而 buf 的大小是根据 tmp_orig、esc_name 和 tmp_new 的长度计算分配的，但 tmp_new 是临时文件名，其长度可能超过 ... |
| 889 | vim-9.1.1040 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | TP | 代码在多个分支中直接使用 STRCPY（即 strcpy）将未经验证的外部命令字符串 cmd 复制到固定大小的缓冲区 buf 中，存在缓冲区溢出风险。虽然缓冲区大小 len 根据 cmd 长度计算，但若 cmd 在分配后、复制前被修改... |
| 888 | vim-9.1.1040 | ex_substitute | cpp/unbounded-write | 4883 | FP | TP | 切片代码中直接使用了未进行边界检查的STRCAT宏（即strcat），将sub_firstline + copycol的内容追加到new_start指向的缓冲区。new_start缓冲区的大小由new_start_len决定，但追加前... |
| 891 | vim-9.1.1040 | ex_sort | cpp/unbounded-write | 605 | FP | TP | 代码使用STRCPY宏（即strcpy）将`s`指向的字符串复制到固定大小的缓冲区`sortbuf1`中，而`s`来自`ml_get`函数，其长度可能超过`sortbuf1`的大小（`maxlen + 1`）。`maxlen`是之前计... |
| 892 | vim-9.1.1040 | expand_sfile | cpp/unbounded-write | 10068 | FP | TP | 代码使用STRCPY（即strcpy）将可变长度字符串repl复制到固定大小的缓冲区newres中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未显示对repl长度的任何限制或验证。 |
| 893 | vim-9.1.1040 | repl_cmdline | cpp/unbounded-write | 5307 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串（src + srclen）复制到固定大小的缓冲区new_cmdline中，且目标缓冲区大小i的计算未考虑目标字符串的终止符，存在缓冲区溢出风险。 |
| 894 | vim-9.1.1040 | repl_cmdline | cpp/unbounded-write | 5313 | FP | TP | 代码使用STRCPY（即strcpy）将eap->nextcmd复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小i是根据多个字符串长度计算分配的，但未检查eap->nextcmd的长度是否超过目标缓冲区剩... |
| 895 | vim-9.1.1040 | replace_makeprg | cpp/unbounded-write | 5014 | FP | TP | 代码使用STRCPY（即strcpy）宏将用户控制的参数p复制到新分配的缓冲区ptr中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未显示对p的长度有任何限制或验证。 |
| 896 | vim-9.1.1040 | replace_makeprg | cpp/unbounded-write | 5029 | FP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串（program和p）复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小是基于STRLEN(program)和STRLEN(p)动态计算的，但S... |
| 899 | vim-9.1.1040 | get_exception_string | cpp/unbounded-write | 473 | FP | TP | 代码使用strcat向缓冲区val追加内容，而val指向由vim_strnsave分配的缓冲区，其大小在分配时已固定。后续的STRCAT操作未检查目标缓冲区剩余空间，若mesg或p指向的字符串长度超过缓冲区剩余容量，将导致缓冲区溢出。 |
| 897 | vim-9.1.1040 | do_one_cmd | cpp/unbounded-write | 2678 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将未知长度的字符串复制到固定大小的IObuff缓冲区，存在缓冲区溢出风险。切片中未显示对源字符串长度的检查或限制。 |
| 900 | vim-9.1.1040 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 代码使用`sprintf`将未限制长度的字符串`&mesg[1]`写入缓冲区`val`，而`val`指向的缓冲区大小由`vim_strnsave`分配，其长度未考虑`sprintf`添加的额外字符，存在缓冲区溢出风险。 |
| 901 | vim-9.1.1040 | escape_fname | cpp/unbounded-write | 4105 | FP | TP | 代码使用strcpy将源字符串(*pp)复制到目标缓冲区(p+1)，目标缓冲区大小根据源字符串长度加2分配，但strcpy不检查目标缓冲区大小，若源字符串长度在分配后被外部修改或未正确终止，可能导致缓冲区溢出。 |
| 903 | vim-9.1.1040 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 860 | FP | TP | 代码使用STRCPY（即strcpy）将动态获取的字符串p复制到固定缓冲区ccline.cmdbuff，虽然之前调用了realloc_cmdbuff，但该函数仅在长度不足时重新分配缓冲区，并未对源字符串p的长度进行限制或检查，存在缓冲... |
| 902 | vim-9.1.1040 | cmdline_browse_history | cpp/unbounded-write | 1494 | FP | TP | 代码使用STRCPY（即strcpy）将历史记录字符串p复制到ccline.cmdbuff中，而ccline.cmdbuff的大小由alloc_cmdbuff根据plen分配，但分配时仅额外增加20字节，若p的长度（plen）接近或超... |
| 904 | vim-9.1.1040 | vim_settempdir | cpp/unbounded-write | 5286 | FP | TP | 代码使用STRCPY（即strcpy）将参数tempdir直接复制到固定大小的缓冲区buf中，而buf的大小为MAXPATHL+2，但tempdir作为外部输入（如环境变量）其长度可能超过目标缓冲区，存在缓冲区溢出风险。切片中未见对t... |
| 906 | vim-9.1.1040 | buf_modname | cpp/unbounded-write | 3636 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的fname复制到新分配的缓冲区retval中，而retval的大小仅基于fnamelen + extlen + 3计算，未限制源字符串fname的长度，存在缓冲区溢出风险。 |
| 907 | vim-9.1.1040 | addfile | cpp/unbounded-write | 4202 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证的外部输入（参数f）复制到新分配的缓冲区p，虽然p的大小根据f的长度分配，但strcpy本身不检查边界，若f在调用后被修改或分配逻辑有误，仍存在缓冲区溢出风险。切片中未见对f进行长度验证... |
| 908 | vim-9.1.1040 | unix_expandpath | cpp/unbounded-write | 3837 | FP | TP | 代码在行 `STRCPY(s, path_end + 1);` 处使用了不安全的 `strcpy`，目标缓冲区 `s` 指向 `buf` 内部，而源字符串 `path_end + 1` 来自外部输入 `path`，其长度可能超过目标缓... |
| 909 | vim-9.1.1040 | concat_fnames | cpp/unbounded-write | 3127 | FP | TP | 代码使用strcpy将fname1复制到新分配的缓冲区dest，但dest的大小仅基于fname1和fname2的当前长度计算。如果fname1或fname2在调用后内容被外部修改（如环境变量、文件读取等），其长度可能超过分配大小，导... |
| 910 | vim-9.1.1040 | concat_fnames | cpp/unbounded-write | 3130 | FP | TP | 代码使用alloc分配目标缓冲区，其大小基于两个输入字符串的长度计算，但后续使用STRCAT（即strcat）进行拼接。strcat不检查目标缓冲区剩余空间，若fname2指向的字符串内容在分配后被外部修改（如通过环境变量、文件读取等... |
| 911 | vim-9.1.1040 | uniquefy_paths | cpp/unbounded-write | 2364 | FP | TP | 代码中 `file_pattern` 缓冲区大小为 `len + 2`，随后使用 `STRCAT(file_pattern, pattern)` 将 `pattern` 字符串追加到缓冲区。`pattern` 是函数参数，其长度未在切... |
| 912 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1718 | FP | TP | 代码使用STRCPY（即strcpy）将rel_fname复制到NameBuff，而NameBuff大小为MAXPATHL，但rel_fname长度未经验证，且切片中无任何长度检查或安全拷贝机制，存在缓冲区溢出风险。 |
| 913 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1719 | FP | TP | 代码使用STRCPY（即strcpy）将rel_fname复制到NameBuff，然后紧接着用gettail的结果覆盖部分内容，但未检查组合后的路径长度是否超过NameBuff的大小（MAXPATHL）。虽然切片显示有长度检查（STR... |
| 914 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1724 | FP | TP | 代码使用STRCPY（即strcpy）将*file_to_find复制到NameBuff，而*file_to_find可能来自环境变量等外部输入，且NameBuff大小为MAXPATHL，但未检查源字符串长度，存在缓冲区溢出风险。 |
| 915 | vim-9.1.1040 | ff_check_visited | cpp/unbounded-write | 1370 | FP | TP | 代码使用STRCPY（即strcpy）将ff_expand_buffer的内容复制到新分配的内存vp->ffv_fname中，而目标缓冲区的大小是根据源字符串长度（STRLEN(ff_expand_buffer) + 1）精确分配的，... |
| 922 | vim-9.1.1040 | <global> | cpp/unbounded-write | 537 | FP | TP | 代码中多处使用STRCPY宏（即strcpy）将未知长度的字符串复制到固定大小的缓冲区（如ff_expand_buffer，大小为MAXPATHL），且源字符串（如search_ctx->ffsc_start_dir、search_c... |
| 924 | vim-9.1.1040 | <global> | cpp/unbounded-write | 548 | FP | TP | 代码使用STRCAT宏（即strcat）将search_ctx->ffsc_fix_path拼接到ff_expand_buffer，而ff_expand_buffer是固定大小的缓冲区（MAXPATHL），但未检查拼接后的总长度是否超... |
| 923 | vim-9.1.1040 | <global> | cpp/unbounded-write | 545 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区（如ff_expand_buffer，大小为MAXPATHL），且源字符串（如search_ctx->ffsc_fix_path）来自外部输入... |
| 926 | vim-9.1.1040 | <global> | cpp/unbounded-write | 591 | FP | TP | 代码使用STRCAT宏（即strcat）将search_ctx->ffsc_wc_path拼接到temp缓冲区，但temp缓冲区的大小仅基于两个字符串长度之和分配，未考虑strcat需要目标缓冲区已有内容后的空终止符空间，存在缓冲区溢... |
| 925 | vim-9.1.1040 | <global> | cpp/unbounded-write | 590 | FP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将未知长度的字符串（search_ctx->ffsc_fix_path + len）复制到固定大小的缓冲区temp中，而temp的大小计算依赖于另一个未知长度的字符串（se... |
| 927 | vim-9.1.1040 | <global> | cpp/unbounded-write | 3798 | FP | TP | 代码使用 strcat 将未限制长度的字符串 s 追加到缓冲区 r 中，而 r 的分配大小仅考虑了 s 的初始长度，未考虑 s 可能被 foldtext_cleanup 函数修改后变长，存在缓冲区溢出风险。 |
| 928 | vim-9.1.1040 | foldDelMarker | cpp/unbounded-write | 1897 | FP | TP | 代码使用STRCPY宏（即strcpy）将源字符串p+len复制到目标缓冲区newline + (p - line)，未检查目标缓冲区大小。目标缓冲区newline通过alloc分配，大小为ml_get_len(lnum) - len... |
| 930 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2899 | FP | TP | 代码使用STRCPY（即strcpy）将res_prolog->title复制到固定大小的buffer[256]中，而res_prolog->title来自外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 931 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2901 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的字符串（res_prolog->title和res_prolog->version）长度在切片中未经验证，存在缓冲区溢出的风险。 |
| 932 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2905 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而res_cidfont->title来源于外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 933 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2907 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的源字符串（res_cidfont->version）长度未知，存在缓冲区溢出的风险。切片中未显示对res_cidfont->vers... |
| 929 | vim-9.1.1040 | foldAddMarker | cpp/unbounded-write | 1815 | FP | TP | 代码使用STRCPY（即strcpy）将'line'（来自ml_get的缓冲区）复制到'newline'，而'newline'的大小为'line_len + markerlen + STRLEN(cms) + 1'。由于'line'的... |
| 934 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2912 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cmap->title复制到固定大小的buffer[256]中，而title来源于外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 935 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2914 | FP | TP | 代码使用STRCAT宏（即strcat）将资源文件的版本字符串拼接到固定大小的缓冲区buffer中，未检查缓冲区长度，存在缓冲区溢出风险。 |
| 936 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2920 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_encoding->title复制到固定大小的buffer[256]中，而title来源于外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 937 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2922 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的源字符串（res_encoding->title和res_encoding->version）来自外部资源文件，其长度未经验证，可能... |
| 938 | vim-9.1.1040 | prt_resource_name | cpp/unbounded-write | 1659 | FP | TP | 代码使用strcpy复制字符串，虽然对源字符串长度进行了检查，但检查目标是filename而非目标缓冲区resource_filename。目标缓冲区resource_filename的大小未知，若其小于MAXPATHL，则strcp... |
| 939 | vim-9.1.1040 | do_helptags | cpp/unbounded-write | 1210 | FP | TP | 代码使用STRCPY（即strcpy）将未知长度的字符串复制到固定大小的缓冲区NameBuff中，存在缓冲区溢出风险。切片中未显示对输入字符串长度的检查或限制。 |
| 940 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 975 | FP | TP | 代码使用STRCAT宏（即strcat）向NameBuff缓冲区拼接未经验证长度的字符串ext，存在缓冲区溢出风险。NameBuff的大小未知，且切片中未显示对ext长度的检查或对NameBuff边界的防护。 |
| 941 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 991 | FP | TP | 代码使用STRCAT宏（即strcat）将参数tagfname拼接到NameBuff缓冲区，而NameBuff的大小未知（切片中未定义其大小），且tagfname是函数参数，其长度不受控制，存在缓冲区溢出风险。 |
| 942 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 1112 | FP | TP | sprintf 使用未限制长度的动态字符串 p1 和 fname 作为输入，目标缓冲区 s 的大小为 p2 - p1 + STRLEN(fname) + 2，但 sprintf 格式字符串 "%s\t%s" 未指定最大长度，存在缓冲区... |
| 945 | vim-9.1.1040 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | sprintf 使用未经验证的字符串拼接，目标缓冲区长度 'len' 的计算可能无法容纳拼接后的完整路径，存在缓冲区溢出风险。 |
| 944 | vim-9.1.1040 | load_colors | cpp/unbounded-write | 602 | FP | TP | 代码使用`sprintf`将用户控制的`name`参数拼接到固定大小的缓冲区`buf`中，而`buf`的大小仅基于`STRLEN(name) + 12`分配，未考虑格式字符串`"colors/%s.vim"`中额外字符的占用，存在缓冲... |
| 946 | vim-9.1.1040 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | TP | 代码使用`sprintf`将多个字符串拼接至固定大小的缓冲区`buf`，缓冲区大小`amt`的计算已包含所有源字符串的长度及定界符，但计算时未考虑`sprintf`自动添加的字符串终止符'\0'，导致缓冲区大小不足，存在缓冲区溢出的风险。 |
| 948 | vim-9.1.1040 | <global> | cpp/unbounded-write | 1456 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是函数参数，其长度未经验证。虽然分配了strlen(fname)+1字节，但若fname在调用后被恶意修改或并发修改，仍可能导致溢出。切片中未见对fname内容的任何校验... |
| 949 | vim-9.1.1040 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是外部传入的文件名字符串，其长度未经验证。虽然分配了strlen(fname)+1字节，但若fname在调用cs_insert_filelist后被恶意修改或本身过长，s... |
| 950 | vim-9.1.1040 | cs_add_common | cpp/unbounded-write | 604 | FP | TP | 代码使用sprintf拼接路径和文件名，未对拼接后的总长度进行限制，存在缓冲区溢出风险。fname来自用户输入的环境变量，其长度可能超过fname2的分配大小。 |
| 951 | vim-9.1.1040 | ins_compl_infercase_gettext | cpp/unbounded-write | 653 | FP | TP | 代码使用STRCPY宏（即strcpy）将IObuff的内容复制到gap.ga_data中，而IObuff的大小为IOSIZE（切片中可见其边界检查），但目标缓冲区gap.ga_data的大小未知且未在切片中显示有任何大小限制或边界检... |
| 952 | vim-9.1.1040 | <global> | cpp/unbounded-write | 3129 | FP | TP | 代码使用`sprintf`将`transchar(from)`的结果写入固定大小的缓冲区`args->os_errbuf`，而`transchar`的返回值长度未在切片内受限，存在缓冲区溢出风险。 |
| 954 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2157 | FP | TP | 代码使用STRCPY（即strcpy）将fix_fname返回的字符串复制到新分配的缓冲区s中，虽然s的大小根据STRLEN(f)+1分配，但fix_fname可能返回一个比原输入更长的路径（例如解析'..'或符号链接），导致strc... |
| 953 | vim-9.1.1040 | findswapname | cpp/unbounded-write | 4967 | FP | TP | 代码使用STRCPY宏（即strcpy）将fname复制到新分配的缓冲区fname2，而fname2的大小为n+2，fname的长度为n。虽然缓冲区大小足够，但STRCPY本身是不安全的函数，存在潜在的缓冲区溢出风险，符合规则检测的'... |
| 955 | vim-9.1.1040 | <global> | cpp/unbounded-write | 811 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将call_data复制到固定大小的缓冲区menu->strings[i]中，而call_data是外部传入的字符串，其长度未经验证，存在缓冲区溢出风险。 |
| 956 | vim-9.1.1040 | <global> | cpp/unbounded-write | 815 | FP | TP | 代码中直接使用宏 STRCPY（即 strcpy）将 call_data 复制到固定大小的缓冲区 menu->strings[i] 中，而 menu->strings[i] 的大小仅通过 alloc(STRLEN(call_data)... |
| 957 | vim-9.1.1040 | msg_show_console_dialog | cpp/unbounded-write | 4502 | FP | TP | 代码使用STRCPY宏（即strcpy）将message字符串复制到confirm_msg缓冲区，目标缓冲区大小由alloc(len)分配，而len的计算包含了STRLEN(message)，但未预留strcpy所需的终止空字符空间，... |
| 958 | vim-9.1.1040 | str2specialbuf | cpp/unbounded-write | 2017 | FP | TP | 切片代码显示，在调用STRCAT（即strcat）前，仅检查了源字符串长度与目标缓冲区当前长度之和是否小于参数len，但未检查目标缓冲区buf的原始大小，存在缓冲区溢出的风险。 |
| 959 | vim-9.1.1040 | get_emsg_source | cpp/unbounded-write | 502 | FP | TP | sprintf 使用未受控的 sname 和 p 作为格式化字符串和参数，且目标缓冲区 Buf 的大小仅为 STRLEN(sname) + STRLEN(p)，未考虑 sprintf 添加的格式化字符和终止符，存在缓冲区溢出风险。 |
| 960 | vim-9.1.1040 | may_trigger_modechanged | cpp/unbounded-write | 2836 | FP | TP | 代码使用STRCPY（即strcpy）将curr_mode复制到last_mode，而last_mode的大小未知，curr_mode来自get_mode函数，其长度可能超过last_mode的缓冲区大小，存在缓冲区溢出风险。 |
| 962 | vim-9.1.1040 | call_shell | cpp/unbounded-write | 1877 | FP | TP | 代码使用strcat向固定大小的缓冲区ncmd追加内容，ncmd的大小基于ecmd和p_sxq的长度计算，但未考虑strcat追加的字符串长度可能超过缓冲区剩余空间，存在缓冲区溢出风险。 |
| 964 | vim-9.1.1040 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf 使用未受控的外部输入 result 直接格式化到固定大小的缓冲区 reply 中，reply 的大小仅基于 result 的当前长度分配，但 sprintf 的格式化输出可能包含额外的数字和换行符，若 result 内... |
| 965 | vim-9.1.1040 | push_showcmd | cpp/unbounded-write | 1808 | FP | TP | 代码使用不安全的strcpy函数，将源缓冲区showcmd_buf的内容复制到目标缓冲区old_showcmd_buf，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 963 | vim-9.1.1040 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 切片代码中直接使用了未经验证长度的用户输入（args）与固定大小的缓冲区（newline）进行拼接，存在缓冲区溢出风险。具体在`insert`命令处理中，`args`被直接用于`STRCAT`，且未检查目标缓冲区大小。 |
| 968 | vim-9.1.1040 | op_replace | cpp/unbounded-write | 1299 | FP | TP | 代码中直接使用STRCPY（即strcpy）宏，将源字符串复制到目标缓冲区，未检查目标缓冲区大小。切片显示目标缓冲区newp通过alloc(oldlen + 1 + n)分配，但源字符串oldp + bd.textcol + bd.t... |
| 967 | vim-9.1.1040 | op_change | cpp/unbounded-write | 2003 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将源字符串复制到目标缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未显示任何边界检查或安全防护措施。 |
| 969 | vim-9.1.1040 | op_replace | cpp/unbounded-write | 1308 | FP | TP | 切片代码中直接使用STRCPY（即strcpy）宏将未知长度的源字符串（oldp + bd.textcol + bd.textlen）复制到固定大小的目标缓冲区（after_p），而after_p的分配大小基于计算值oldlen + ... |
| 970 | vim-9.1.1040 | op_delete | cpp/unbounded-write | 962 | FP | TP | 代码在行962处使用STRCPY宏（即strcpy）复制字符串，目标缓冲区`newp`的大小为`ml_get_len(lnum) + 1 - n`，而源字符串`oldp + bd.textcol + bd.textlen`的长度未经验... |
| 972 | vim-9.1.1040 | option_value2string | cpp/unbounded-write | 8324 | FP | TP | 代码中直接使用不安全的strcpy宏（STRCPY）将get_special_key_name等函数的返回值复制到固定大小的缓冲区NameBuff，未检查源字符串长度，存在缓冲区溢出风险。 |
| 971 | vim-9.1.1040 | block_insert | cpp/unbounded-write | 743 | FP | TP | 代码使用STRCPY（即strcpy）将字符串oldp复制到缓冲区newp + offset处，未检查目标缓冲区newp的大小，而oldp是来自文件行的未经验证的数据，存在缓冲区溢出风险。 |
| 973 | vim-9.1.1040 | option_value2string | cpp/unbounded-write | 8326 | FP | TP | 代码在多个分支中直接使用STRCPY（即strcpy）将内容复制到NameBuff，但未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 974 | vim-9.1.1040 | stropt_expand_envvar | cpp/unbounded-write | 1803 | FP | TP | 代码使用strcpy将option_expand返回的字符串复制到新分配的缓冲区，但分配的大小仅基于源字符串长度计算，未考虑目标缓冲区大小限制，存在缓冲区溢出风险。 |
| 976 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 7029 | FP | TP | 代码使用strcat向固定大小的缓冲区command追加内容，但缓冲区大小len的计算依赖于环境变量、用户输入等外部数据，若这些数据长度超过缓冲区剩余空间，将导致缓冲区溢出。切片中未见任何边界检查。 |
| 975 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 6989 | FP | TP | 代码使用strcat向固定大小的缓冲区`command`追加内容，而`command`的大小`len`是基于多个变量（如`tempname`、`pat[i]`等）的长度计算得出的。这些变量可能包含用户输入或环境变量，若其总长度超过`a... |
| 978 | vim-9.1.1040 | mch_FullName | cpp/unbounded-write | 2819 | FP | TP | 代码在调用STRCAT（即strcat）前，仅检查了目标缓冲区buf的当前长度与待追加字符串fname的长度之和是否小于缓冲区总长度len，但未检查strcat操作本身是否会导致缓冲区溢出。strcat会一直复制直到遇到源字符串的终止... |
| 977 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 7335 | FP | TP | 代码在行`STRCPY(p, (*file)[i]);`处使用STRCPY（即strcpy）宏，将长度未知的字符串`(*file)[i]`复制到固定大小的缓冲区`p`中，而`p`的大小仅为`STRLEN((*file)[i]) + 1... |
| 979 | vim-9.1.1040 | qf_store_title | cpp/unbounded-write | 1934 | FP | TP | 代码使用strcpy复制未限制长度的字符串'title'到新分配的缓冲区，虽然缓冲区大小根据STRLEN(title)+2分配，但strcpy本身不检查边界，若'title'在分配后、复制前被修改或存在并发问题，仍可能导致溢出。告警指... |
| 980 | vim-9.1.1040 | reg_submatch | cpp/unbounded-write | 2723 | FP | TP | 代码使用STRCPY（即strcpy）将未知长度的字符串（来自reg_getline_submatch）复制到固定大小的缓冲区retval中，而retval的大小仅由alloc(len)分配，但STRCPY调用前未确保目标缓冲区足够大... |
| 982 | vim-9.1.1040 | regtilde | cpp/unbounded-write | 1959 | FP | TP | 代码使用STRCPY（即strcpy）将postfix复制到tmpsub缓冲区，其目标缓冲区大小tmpsublen+1由alloc分配，但postfix长度postfixlen未经验证，且postfix源自用户输入source，存在缓... |
| 984 | vim-9.1.1040 | get_reg_contents | cpp/unbounded-write | 2733 | FP | TP | 代码使用 STRCPY（即 strcpy）将 y_current->y_array[i].string 复制到固定大小的缓冲区 retval 中，但未检查源字符串长度是否超过目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 981 | vim-9.1.1040 | reg_submatch | cpp/unbounded-write | 2732 | FP | TP | 代码在循环中使用STRCPY（即strcpy）将长度未知的字符串`s`复制到固定大小的缓冲区`retval`中，`retval`的大小由`alloc(len)`分配，但`len`的计算包含了`s`的长度，而`s`来自`reg_getl... |
| 983 | vim-9.1.1040 | match_with_backref | cpp/unbounded-write | 1600 | FP | TP | 代码使用STRCPY（即strcpy）将长度未知的rex.line复制到固定大小的缓冲区reg_tofree中，而reg_tofree的大小仅基于rex.line的长度加上固定偏移（len += 50）分配，未对源字符串长度进行边界检... |
| 986 | vim-9.1.1040 | do_put | cpp/unbounded-write | 2160 | FP | TP | 切片代码中直接使用了不安全的STRCPY宏（即strcpy），将y_array[i].string等源字符串复制到固定大小的缓冲区newp中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 987 | vim-9.1.1040 | op_yank | cpp/unbounded-write | 1315 | FP | TP | 代码使用STRCPY（即strcpy）宏进行字符串拼接，目标缓冲区pnew的大小基于两个字符串长度之和计算，但strcpy不检查目标缓冲区大小，若源字符串未以空字符结尾或长度计算错误，可能导致缓冲区溢出。切片中未显示对源字符串内容或长... |
| 988 | vim-9.1.1040 | op_yank | cpp/unbounded-write | 1316 | FP | TP | 代码使用STRCPY宏（即strcpy）进行字符串拼接，目标缓冲区大小由alloc分配，其大小为两个源字符串长度之和加1，但STRCPY调用未检查目标缓冲区剩余空间，若第一个STRCPY写入的字符串长度超过分配的大小，则第二个STRC... |
| 985 | vim-9.1.1040 | do_put | cpp/unbounded-write | 2159 | FP | TP | 切片代码中直接使用 STRCPY 宏（即 strcpy）将 y_array[y_size - 1].string 复制到固定大小的缓冲区 newp 中，而 newp 的大小由 ml_get_len(lnum) - col + totl... |
| 989 | vim-9.1.1040 | stuff_yank | cpp/unbounded-write | 470 | FP | TP | 代码使用不安全的strcpy函数，将源字符串（pp->string）复制到目标缓冲区（tmp），未检查源字符串长度是否超过目标缓冲区大小（tmplen + 1），存在缓冲区溢出风险。 |
| 990 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2838 | FP | TP | 代码使用strcat向固定大小的缓冲区scriptname追加内容，而scriptname的大小仅基于输入name的长度计算，未考虑已拼接的'autoload/'前缀长度，存在缓冲区溢出风险。 |
| 991 | vim-9.1.1040 | ExpandPackAddDir | cpp/unbounded-write | 1309 | FP | TP | sprintf 使用未经验证的用户输入 `pat` 构造目标字符串，目标缓冲区 `s` 的大小为 `pat_len + 26`，而格式化字符串 "pack/*/opt/%s*" 的长度加上 `pat` 的长度可能超过该缓冲区大小，存在... |
| 992 | vim-9.1.1040 | sign_jump | cpp/unbounded-write | 1313 | FP | TP | sprintf 使用未限制长度的缓冲区 buf->b_fname 作为格式化字符串的一部分，且目标缓冲区 cmd 的大小仅基于 buf->b_fname 的当前长度计算，未考虑 lnum 可能的最大长度，存在缓冲区溢出风险。 |
| 994 | vim-9.1.1040 | make_case_word | cpp/unbounded-write | 3140 | FP | TP | 代码直接使用不安全的strcpy宏（STRCPY）复制字符串，未检查目标缓冲区大小，且切片中未显示对源字符串fword的长度有任何限制或验证，存在缓冲区溢出风险。 |
| 993 | vim-9.1.1040 | dump_word | cpp/unbounded-write | 4187 | FP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或外部数据（如环境变量、文件读取内容），且切片中未显示对p的长度进行任何校验，存在缓冲区溢出风险。 |
| 995 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2998 | FP | TP | 代码使用STRCPY宏（即strcpy）将repl_to复制到新分配的缓冲区p中，未检查目标缓冲区大小，而repl_to是全局变量，其长度可能超过目标缓冲区p的剩余空间，存在缓冲区溢出风险。 |
| 996 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2999 | FP | TP | 代码使用 STRCAT（即 strcat）将源字符串拼接到目标缓冲区 p 中，但 p 的大小是基于 ml_get_curline_len() + addlen + 1 分配的，而 STRCAT 的源字符串长度未经验证，可能导致缓冲区溢出。 |
| 998 | vim-9.1.1040 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）将参数lang直接复制到固定大小的数组sl.sl_lang中，切片未显示对lang的长度有任何校验或限制，存在缓冲区溢出风险。 |
| 997 | vim-9.1.1040 | count_common_word | cpp/unbounded-write | 1919 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串p复制到固定大小的缓冲区wc->wc_word中，而p的来源（word）长度可能超过目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何长度检查或安全复制机制。 |
| 999 | vim-9.1.1040 | spell_move_to | cpp/unbounded-write | 1420 | FP | TP | 代码使用STRCPY宏（即strcpy）将长度不确定的line字符串复制到固定大小的buf缓冲区，而buf的大小仅根据len + MAXWLEN + 2分配，未限制源字符串长度，存在缓冲区溢出风险。 |
| 1002 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2371 | FP | TP | 代码使用STRCAT宏（即strcat）将items[1]拼接到缓冲区p中，而p的大小仅根据items[0]和items[1]的长度计算，未考虑p的原始内容长度，可能导致缓冲区溢出。 |
| 1004 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2495 | FP | TP | 代码在拼接字符串时使用STRCAT宏（即strcat），目标缓冲区大小未知，且源字符串来自fgets读取的外部文件，存在缓冲区溢出风险。 |
| 1003 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2464 | FP | TP | 代码在行`STRCPY(p, items[1]);`处使用`strcpy`将`fgets`读取的字符串`items[1]`复制到缓冲区`p`中，而`p`的大小为`STRLEN(items[1]) + 2`，仅比源字符串长度多2字节，未... |
| 1006 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2746 | FP | TP | 代码在行号2746处使用sprintf将items[4]拼接到buf中，而items[4]来自外部文件读取的未经验证的用户输入，可能导致缓冲区溢出。 |
| 1007 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2748 | FP | TP | 代码在行号2748处使用sprintf将items[4]拼接到固定大小的缓冲区buf中，items[4]来源于外部文件读取的未经验证的行，可能导致缓冲区溢出。 |
| 1008 | vim-9.1.1040 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | TP | 代码使用STRCPY宏（即strcpy）将goodword复制到sft->sft_word，而goodword是函数参数，其长度可能超过目标缓冲区sft->sft_word的大小（该缓冲区大小仅为STRLEN(goodword) + ... |
| 1009 | vim-9.1.1040 | suggest_try_change | cpp/unbounded-write | 1199 | FP | TP | 代码使用不安全的strcpy函数将su->su_fbadword复制到固定大小的缓冲区fword中，未检查源字符串长度是否超过目标缓冲区大小MAXWLEN，存在缓冲区溢出风险。 |
| 1013 | vim-9.1.1040 | findtags_add_match | cpp/unbounded-write | 2623 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串（如st->help_lang、st->tag_fname、st->lbuf）复制到固定大小的缓冲区中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1012 | vim-9.1.1040 | expand_tag_fname | cpp/unbounded-write | 4125 | FP | TP | 代码使用不安全的STRCPY（即strcpy）将tag_fname复制到固定大小的缓冲区retval（大小为MAXPATHL），而tag_fname的来源（如环境变量、文件读取等）在切片中未显示有长度限制或验证，存在缓冲区溢出风险。 |
| 1014 | vim-9.1.1040 | findtags_add_match | cpp/unbounded-write | 2702 | FP | TP | 切片代码中多次使用STRCPY（即strcpy）宏，将来源未知或长度未经验证的外部数据（如st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区，存在缓冲区溢出风险。 |
| 1015 | vim-9.1.1040 | show_one_termcode | cpp/unbounded-write | 7059 | FP | TP | 代码使用STRCPY（即strcpy）将get_special_key_name返回的字符串复制到IObuff+5位置，但IObuff的大小未知且未在切片中显示，而源字符串p的长度也未经验证，存在缓冲区溢出风险。 |
| 1016 | vim-9.1.1040 | current_tagblock | cpp/unbounded-write | 1386 | FP | TP | sprintf 使用未限制长度的用户输入 p 作为格式化字符串的一部分，且目标缓冲区 spat 和 epat 的大小仅基于 len 计算，未考虑格式化字符串本身的固定开销，存在缓冲区溢出风险。 |
| 1017 | vim-9.1.1040 | uc_check_code | cpp/unbounded-write | 1782 | FP | TP | 代码在多个分支中直接使用STRCPY（即strcpy）将外部输入（如eap->arg）复制到缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何长度校验或安全复制机制。 |
| 1018 | vim-9.1.1040 | get_scriptlocal_funcname | cpp/unbounded-write | 4705 | FP | TP | 代码使用STRCAT宏（即strcat）将未经验证长度的字符串`p + off`拼接到固定大小的缓冲区`newname`中，而`newname`的大小仅根据`sid_buf`和`p + off`的长度之和分配，未考虑strcat会覆盖... |
| 1019 | vim-9.1.1040 | trans_function_name_ext | cpp/unbounded-write | 4618 | FP | TP | 代码使用宏 STRCPY（即 strcpy）将 sid_buf 的内容复制到 name 缓冲区，而 sid_buf 的大小为 20 字节，name 缓冲区的大小为 len + lead + extra + 1 字节。当 sid_buf... |
| 1021 | vim-9.1.1040 | fname_trans_sid | cpp/unbounded-write | 2224 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串`name + llen`复制到缓冲区`fname + i`中，虽然存在缓冲区大小检查，但该检查依赖于`STRLEN`计算源字符串长度，若源字符串在复制前被修改或未正确终止，... |
| 1022 | vim-9.1.1040 | set_ufunc_name | cpp/unbounded-write | 664 | FP | TP | 代码使用不安全的strcpy函数，将未经验证的外部输入（参数name）复制到固定大小的缓冲区fp->uf_name中，存在缓冲区溢出风险。切片中未显示对name长度的任何检查或对目标缓冲区大小的验证。 |
| 1024 | vim-9.1.1040 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证的字符串name复制到固定大小的缓冲区funcname中，而funcname的大小仅基于STRLEN(name)+3分配，未对源字符串长度进行限制，存在缓冲区溢出风险。 |
| 1025 | vim-9.1.1040 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串`name`复制到固定大小的缓冲区`newsav->sav_key`中，存在缓冲区溢出风险。切片中未显示对`name`长度的检查或使用安全函数。 |
| 1026 | vim-9.1.1040 | find_exported | cpp/unbounded-write | 756 | FP | TP | 代码使用sprintf将外部可控的字符串（如环境变量、文件读取内容）拼接到固定大小的缓冲区中，且未对目标缓冲区大小进行校验，存在缓冲区溢出风险。 |
| 1027 | vim-9.1.1040 | find_exported | cpp/unbounded-write | 763 | FP | TP | 代码使用`sprintf`将外部输入的`name`和`sid`拼接到固定大小的缓冲区`funcname`中，而`name`的长度未经验证，可能导致缓冲区溢出。切片中未显示对`name`进行长度检查或使用安全函数。 |
| 1028 | vim-9.1.1040 | xxdline | cpp/unbounded-write | 537 | FP | TP | 函数`xxdline`中的`strcpy(z, l)`调用将外部输入`l`复制到固定大小的缓冲区`z`（大小为`LLEN+1`），未检查`l`的长度，存在缓冲区溢出风险。切片代码中未见对`l`长度的任何验证或限制。 |
| 1029 | vim-9.1.1040 | ExpandBufnames | cpp/invalid-pointer-deref | 2939 | FP | TP | 在循环中，`(*file)[count++] = p;` 处对指针 `*file` 进行写入，但切片显示 `*file` 仅在 `round == 1` 且 `*file == NULL` 时通过 `*file = ALLOC_MUL... |
| 1030 | vim-9.1.1040 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | TP | 当 width 为 2 且 len 等于 pos.col + 1 时，访问 p[pos.col + 1] 会越界，因为 p 仅分配了 len 个元素，索引最大为 len-1。切片代码中缺少对 width 和 len 关系的检查，存在缓... |
| 1035 | vim-9.1.1330 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数getcell在特定条件下（如行列越界或buffer为空）会返回NULL，但调用点vterm_screen_is_eol未对返回值进行空指针检查，直接解引用cell->chars，存在空指针解引用风险。 |
| 1038 | vim-9.1.1330 | did_set_cryptmethod | cpp/inconsistent-null-check | 1894 | FP | TP | 代码直接调用 vim_strsave 并将返回值赋值给全局变量 p_cm，未检查返回值是否为 NULL。vim_strsave 内部调用 alloc 可能失败返回 NULL，后续对 p_cm 的解引用（如 *p_cm）可能导致空指针解... |
| 1037 | vim-9.1.1330 | get_isolated_shell_name | cpp/inconsistent-null-check | 2721 | FP | TP | 函数`vim_strnsave`可能返回NULL，但调用结果`p`被直接返回给调用者，未进行空指针检查。根据规则描述，大多数调用点都检查了空指针，此处缺失检查可能导致调用者解引用空指针。 |
| 1050 | vim-9.1.1330 | barline_parse | cpp/inconsistent-null-check | 1153 | FP | TP | 代码在调用 vim_strnsave 后未检查返回值是否为 NULL，直接将其赋值给 bv_string 使用。vim_strnsave 内部调用 alloc，在内存分配失败时会返回 NULL，后续使用该指针可能导致程序崩溃。 |
| 1054 | vim-9.1.1330 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 '%6ld' 写入最多6位数字加符号和终止符，最多需要21字节，但目标缓冲区 tbuf 仅20字节，存在缓冲区溢出风险。 |
| 1055 | vim-9.1.1330 | highlight_color | cpp/overrunning-write | 3275 | FP | TP | sprintf 调用将格式化字符串写入大小为10字节的静态缓冲区 'buf'，格式化字符串 '#%02x%02x%02x' 加上终止符需要至少10字节，但计算出的值可能超过255，导致十六进制表示超过2位，从而可能发生缓冲区溢出。 |
| 1056 | vim-9.1.1330 | msg_outnum | cpp/overrunning-write | 1653 | FP | TP | sprintf 的目标缓冲区 `buf` 大小为 20 字节，但格式化长整型 `%ld` 最多可能产生 21 字节（包括负号和终止符），存在缓冲区溢出风险。 |
| 1057 | vim-9.1.1330 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 写入的目标缓冲区 `reply` 大小为 32 字节，但格式化字符串 `"%d %ld\n"` 在最坏情况下（如 cmdno 和 result 均为大整数）可能超过 32 字节，导致缓冲区溢出。切片代码中未见任何长度检... |
| 1058 | vim-9.1.1330 | ga_concat_strings | cpp/unbounded-write | 788 | FP | TP | 代码使用不安全的strcpy函数，将来自动态数组gap->ga_data的字符串复制到固定大小的缓冲区p中，而p的大小由alloc(len+1)分配，但p在循环中不断移动，其剩余空间未进行边界检查，可能导致缓冲区溢出。 |
| 1059 | vim-9.1.1330 | maketitle | cpp/unbounded-write | 4230 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串复制到固定大小的缓冲区buf中，存在缓冲区溢出风险。切片显示name变量来自外部文件名，其长度可能超过buf的大小，且没有边界检查。 |
| 1060 | vim-9.1.1330 | buf_write | cpp/unbounded-write | 1208 | FP | TP | 代码中直接使用STRCPY（即strcpy）将fname复制到IObuff缓冲区，未检查fname的长度是否超过IObuff的大小，存在缓冲区溢出风险。切片中未显示IObuff的大小定义，但根据strcpy的固有风险，此模式是典型的安... |
| 1062 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2144 | FP | TP | 代码中直接使用STRCAT宏（即strcat）将p_extra拼接到leader缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未显示对leader缓冲区大小的任何限制或检查。 |
| 1063 | vim-9.1.1330 | transstr | cpp/unbounded-write | 400 | FP | TP | 切片代码显示，`STRCAT(res, transchar_byte(*p++))` 宏展开为 `strcat`，目标缓冲区 `res` 由 `alloc(len + 1)` 分配，其大小 `len` 是计算出的字符显示宽度，而非存储... |
| 1065 | vim-9.1.1330 | win_redr_status_matches | cpp/unbounded-write | 663 | FP | TP | 代码使用STRCPY（即strcpy）宏将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区buf中，而buf的大小基于Columns计算，未对输入长度进行验证，存在缓冲区溢出风险。 |
| 1067 | vim-9.1.1330 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的源字符串（fname + 3）复制到固定大小的目标缓冲区（name + 5），存在缓冲区溢出风险。切片中未显示对fname长度的检查或安全复制机制。 |
| 1068 | vim-9.1.1330 | has_profiling | cpp/unbounded-write | 973 | FP | TP | 代码使用 STRCPY（即 strcpy）将 fname 复制到新分配的缓冲区 pe->pen_name，而 fname 是函数参数，可能来自外部输入（如环境变量、文件读取等）。切片中未显示对 fname 长度的检查或限制，存在缓冲区... |
| 1070 | vim-9.1.1330 | do_string_sub | cpp/unbounded-write | 8014 | FP | TP | 代码使用STRCPY宏（即strcpy）将'tail'指向的字符串复制到动态分配的缓冲区'ga.ga_data'中，未检查目标缓冲区剩余空间是否足够，存在缓冲区溢出风险。切片中可见目标缓冲区通过ga_grow进行过扩展，但该扩展计算未... |
| 1072 | vim-9.1.1330 | cat_prefix_varname | cpp/unbounded-write | 2576 | FP | TP | 代码使用strcpy将外部传入的name字符串复制到varnamebuf缓冲区，虽然根据name长度动态分配了缓冲区，但分配后未检查alloc是否成功（varnamebuf可能为NULL），且strcpy本身不检查目标缓冲区大小，存在... |
| 1069 | vim-9.1.1330 | ex_diffpatch | cpp/unbounded-write | 1390 | FP | TP | 代码中直接使用STRCPY（即strcpy）将tmp_new复制到buf，而buf的大小是根据tmp_orig、esc_name和tmp_new的长度计算分配的，但tmp_new是vim_tempname生成的临时文件名，其长度可能超... |
| 1071 | vim-9.1.1330 | set_var_const | cpp/unbounded-write | 4271 | FP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname长度由STRLEN(varname)计算，但目标缓冲区di->di_key的大小仅为STRLEN(varname) + 1字节，没有预... |
| 1074 | vim-9.1.1330 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | TP | 代码在多个分支中直接使用 STRCPY（即 strcpy）将外部传入的 cmd 字符串复制到固定大小的缓冲区 buf 中，未对源字符串长度进行校验，存在缓冲区溢出风险。 |
| 1076 | vim-9.1.1330 | ex_sort | cpp/unbounded-write | 605 | FP | TP | 代码使用STRCPY宏（即strcpy）将行内容复制到固定大小的缓冲区sortbuf1，而sortbuf1的大小基于maxlen+1分配，但maxlen是当前排序范围内行的最大长度，后续复制的行可能来自任意行（通过ml_get获取），... |
| 1073 | vim-9.1.1330 | ex_substitute | cpp/unbounded-write | 4883 | FP | TP | 代码中直接使用宏STRCAT(d, s)（即strcat）将sub_firstline + copycol的内容追加到new_start指向的缓冲区，未检查目标缓冲区new_start的剩余空间是否足够，存在缓冲区溢出的风险。 |
| 1077 | vim-9.1.1330 | expand_sfile | cpp/unbounded-write | 10101 | FP | TP | 代码使用STRCPY（即strcpy）将可变长度字符串repl复制到固定大小的缓冲区newres中，而newres的大小仅通过resultlen + 1分配，未验证repllen是否超过目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 1078 | vim-9.1.1330 | repl_cmdline | cpp/unbounded-write | 5311 | FP | TP | 代码使用STRCPY（即strcpy）复制未经验证长度的字符串（src + srclen 和 eap->nextcmd），目标缓冲区new_cmdline的大小由alloc(i)分配，但i的计算未确保能容纳源字符串，存在缓冲区溢出风险。 |
| 1079 | vim-9.1.1330 | repl_cmdline | cpp/unbounded-write | 5317 | FP | TP | 代码使用STRCPY（即strcpy）将eap->nextcmd复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小由变量i决定，i的计算包含了eap->nextcmd的长度，但未对eap->nextcmd的... |
| 1080 | vim-9.1.1330 | replace_makeprg | cpp/unbounded-write | 5018 | FP | TP | 代码使用STRCPY（即strcpy）将用户控制的参数p复制到目标缓冲区ptr，目标缓冲区大小由alloc分配，但分配时仅考虑了program长度和p的长度，未对p的长度进行独立限制，若p长度超过预期，STRCPY可能导致缓冲区溢出。 |
| 1081 | vim-9.1.1330 | replace_makeprg | cpp/unbounded-write | 5033 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区，且切片中未显示对目标缓冲区大小或源字符串长度的检查，存在缓冲区溢出风险。 |
| 1082 | vim-9.1.1330 | do_one_cmd | cpp/unbounded-write | 2678 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将未知长度的字符串复制到固定大小的IObuff缓冲区，存在缓冲区溢出风险。切片中未显示对源字符串长度的检查或限制。 |
| 1085 | vim-9.1.1330 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 代码使用`sprintf`将外部来源的字符串`&mesg[1]`写入缓冲区`val`，但未检查其长度是否超过目标缓冲区剩余空间，存在缓冲区溢出风险。切片中未显示对`mesg`长度的验证或使用安全函数。 |
| 1084 | vim-9.1.1330 | get_exception_string | cpp/unbounded-write | 473 | FP | TP | 代码使用strcat向固定大小的缓冲区val追加内容，而val指向由vim_strnsave分配的缓冲区，其大小基于mesg长度计算。但mesg内容可能包含用户输入或外部数据，且切片中未显示对mesg长度的验证或对strcat目标缓冲... |
| 1086 | vim-9.1.1330 | escape_fname | cpp/unbounded-write | 4116 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串*pp复制到目标缓冲区p+1，而p的大小仅为STRLEN(*pp) + 2。虽然目标缓冲区大小与源字符串长度匹配，但strcpy不检查目标缓冲区大小，若源字符串未以空字符结尾或长度计算有... |
| 1087 | vim-9.1.1330 | cmdline_browse_history | cpp/unbounded-write | 1498 | FP | TP | 代码使用STRCPY宏（即strcpy）将历史记录字符串p复制到固定大小的缓冲区ccline.cmdbuff中，而p的长度plen可能超过alloc_cmdbuff分配的缓冲区大小，存在缓冲区溢出风险。 |
| 1089 | vim-9.1.1330 | vim_settempdir | cpp/unbounded-write | 5289 | FP | TP | 代码使用STRCPY（即strcpy）将参数tempdir复制到固定大小的缓冲区buf中，而buf的大小为MAXPATHL+2，但tempdir作为函数参数来源未知，若其长度超过MAXPATHL+1将导致缓冲区溢出。切片中未显示对te... |
| 1088 | vim-9.1.1330 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 860 | FP | TP | 代码使用STRCPY（即strcpy）将动态长度的字符串p复制到固定大小的缓冲区ccline.cmdbuff，虽然之前调用了realloc_cmdbuff(len + 1)来调整缓冲区大小，但该函数内部使用alloc_cmdbuff(... |
| 1091 | vim-9.1.1330 | buf_modname | cpp/unbounded-write | 3639 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的fname复制到新分配的缓冲区retval中，而retval的大小仅基于fnamelen + extlen + 3计算，未对源字符串fname的长度进行限制，存在缓冲区溢出风险。 |
| 1092 | vim-9.1.1330 | addfile | cpp/unbounded-write | 4219 | FP | TP | 代码使用STRCPY（即strcpy）将参数f复制到新分配的内存p中，虽然p的大小根据f的长度（STRLEN(f) + 1 + isdir）分配，但strcpy本身不检查目标缓冲区大小，若f在调用后被修改或不是以空字符结尾，可能导致溢... |
| 1093 | vim-9.1.1330 | concat_fnames | cpp/unbounded-write | 3134 | FP | TP | 代码使用strcpy将fname1复制到新分配的缓冲区dest，虽然dest的大小是根据fname1和fname2的长度计算分配的，但strcpy本身不检查目标缓冲区大小，若fname1不是以空字符结尾的字符串，或分配计算有误，仍可能... |
| 1094 | vim-9.1.1330 | concat_fnames | cpp/unbounded-write | 3137 | FP | TP | 代码使用strcat拼接两个外部传入的字符串，虽然为目标缓冲区分配了基于两个输入字符串长度计算的空间，但未对输入字符串fname1和fname2进行任何长度验证或边界检查，若调用者传入恶意构造的超长字符串，仍可能导致缓冲区溢出。 |
| 1095 | vim-9.1.1330 | uniquefy_paths | cpp/unbounded-write | 2569 | FP | TP | 代码使用STRCPY（即strcpy）将用户可控的`pattern`参数复制到固定大小的缓冲区`file_pattern`中，而`file_pattern`的大小仅基于`pattern`的长度分配，未考虑目标缓冲区偏移，存在缓冲区溢出风险。 |
| 1096 | vim-9.1.1330 | find_file_in_path_option | cpp/unbounded-write | 1912 | FP | TP | 代码中直接使用STRCPY（即strcpy）将外部输入（*file_to_find）复制到固定大小的缓冲区NameBuff（大小为MAXPATHL），未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1098 | vim-9.1.1330 | <global> | cpp/unbounded-write | 3794 | FP | TP | 代码使用 strcat 将未经验证长度的字符串 s 追加到缓冲区 r 中，而 r 的分配大小仅考虑了 s 的初始长度，未考虑 s 可能被 foldtext_cleanup 函数修改后变长，存在缓冲区溢出风险。 |
| 1097 | vim-9.1.1330 | ff_check_visited | cpp/unbounded-write | 1537 | FP | TP | 代码使用STRCPY（即strcpy）将ff_expand_buffer.string复制到vp->ffv_fname，而目标缓冲区vp->ffv_fname的大小为ff_expand_buffer.length + 1，源字符串长度... |
| 1099 | vim-9.1.1330 | foldDelMarker | cpp/unbounded-write | 1897 | FP | TP | 代码使用STRCPY宏（即strcpy）将源字符串复制到目标缓冲区，目标缓冲区newline的大小为ml_get_len(lnum) - len + 1，而源字符串p + len的长度未经验证，可能导致缓冲区溢出。 |
| 1100 | vim-9.1.1330 | foldAddMarker | cpp/unbounded-write | 1815 | FP | TP | 代码使用STRCPY（即strcpy）宏将line和cms等字符串复制到newline缓冲区，而newline的大小基于line_len、markerlen和STRLEN(cms)计算，未考虑strcpy可能写入的终止空字符，且未对源... |
| 1101 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2899 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_prolog->title复制到固定大小的buffer[256]中，而title来源于外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 1102 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2901 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（大小为256字节）追加内容，而追加的字符串（res_prolog->title和res_prolog->version）长度在切片中未经验证，存在缓冲区溢出的风险。 |
| 1103 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2905 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而res_cidfont->title来自外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 1105 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2912 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cmap->title复制到固定大小的缓冲区buffer中，未检查源字符串长度，存在缓冲区溢出风险。切片中未显示对res_cmap->title长度的任何验证。 |
| 1106 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2914 | FP | TP | 代码使用固定大小的缓冲区`buffer[256]`，并通过`STRCAT`（即`strcat`）拼接来自外部资源文件（`res_cmap->title`和`res_cmap->version`）的字符串，未检查长度，存在缓冲区溢出风险。 |
| 1107 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2920 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_encoding->title复制到固定大小的buffer[256]中，而title来自外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 1108 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2922 | FP | TP | 代码使用strcat将资源文件的title和version拼接到固定大小的缓冲区buffer（256字节）中，未检查目标缓冲区长度，存在缓冲区溢出风险。 |
| 1109 | vim-9.1.1330 | prt_resource_name | cpp/unbounded-write | 1659 | FP | TP | 代码使用strcpy将源字符串复制到目标缓冲区，虽然存在长度检查，但检查条件为`STRLEN(filename) >= MAXPATHL`时截断，而`STRCPY`在长度小于`MAXPATHL`时执行，未限制目标缓冲区大小，若`res... |
| 1111 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 975 | FP | TP | 代码使用STRCAT宏（即strcat）向NameBuff缓冲区拼接未经验证长度的字符串ext，而ext是函数参数，其来源和长度在切片内未显示受控，存在缓冲区溢出风险。 |
| 1112 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 991 | FP | TP | 代码使用STRCAT宏（即strcat）将参数tagfname拼接到NameBuff缓冲区，而NameBuff缓冲区大小未知（切片中未定义其大小），且tagfname是函数参数，其长度不受控制，存在缓冲区溢出风险。 |
| 1113 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 1112 | FP | TP | sprintf 使用未限制长度的动态字符串 p1 和 fname 作为输入，目标缓冲区 s 的大小为 p2 - p1 + STRLEN(fname) + 2，若拼接后字符串长度超过缓冲区大小，将导致缓冲区溢出。 |
| 1115 | vim-9.1.1330 | load_colors | cpp/unbounded-write | 606 | FP | TP | sprintf 使用未经验证的用户输入 name 构造文件路径，目标缓冲区大小仅为 STRLEN(name) + 12，当 name 长度超过缓冲区容量时会发生缓冲区溢出。切片中未显示对 name 长度的任何校验或使用安全函数。 |
| 1116 | vim-9.1.1330 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | sprintf 使用 `csinfo[i].ppath` 和 `name` 拼接字符串，目标缓冲区 `fullname` 的大小 `len` 仅基于 `name` 和 `ppath` 的长度计算，未考虑格式化字符串 `"%s/%s"`... |
| 1117 | vim-9.1.1330 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | TP | 代码使用`sprintf`将多个字符串拼接至固定大小的缓冲区`buf`，缓冲区大小`amt`的计算基于`strlen`结果，但计算时未考虑`sprintf`添加的格式化字符（如制表符、分号、引号）所占的确切字节数，可能导致缓冲区大小不... |
| 1119 | vim-9.1.1330 | <global> | cpp/unbounded-write | 1456 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是函数参数，其长度未经验证，而分配的大小仅为strlen(fname)+1，strcpy可能因fname被后续修改或未以空字符结尾而溢出目标缓冲区。 |
| 1120 | vim-9.1.1330 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是函数参数，其长度未经验证，而strcpy不检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1121 | vim-9.1.1330 | cs_add_common | cpp/unbounded-write | 604 | FP | TP | 代码使用`sprintf`拼接`fname`和`CSCOPE_DBFILE`，其中`fname`来自用户输入参数`arg1`并经过环境变量展开，长度未受限制，可能导致目标缓冲区`fname2`溢出。 |
| 1122 | vim-9.1.1330 | ins_compl_infercase_gettext | cpp/unbounded-write | 688 | FP | TP | 代码使用 STRCPY（即 strcpy）将 IObuff 的内容复制到 gap.ga_data 中，而 IObuff 的大小为 IOSIZE，但切片中未显示对 gap.ga_data 分配大小的检查或确保其足够大的防护，存在缓冲区溢... |
| 1123 | vim-9.1.1330 | <global> | cpp/unbounded-write | 3129 | FP | TP | 代码使用`sprintf`将`transchar(from)`的结果写入固定大小的缓冲区`args->os_errbuf`，而`transchar`的返回值长度未知，可能导致缓冲区溢出。切片中未显示对目标缓冲区大小的检查或使用安全的`... |
| 1126 | vim-9.1.1330 | <global> | cpp/unbounded-write | 811 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将call_data复制到新分配的缓冲区，未检查源字符串长度是否超过目标缓冲区大小。call_data是外部传入的参数，可能导致缓冲区溢出。 |
| 1127 | vim-9.1.1330 | <global> | cpp/unbounded-write | 815 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将call_data复制到固定大小的缓冲区menu->strings[i]中，而call_data是外部传入的字符串，其长度未经验证，存在缓冲区溢出风险。 |
| 1128 | vim-9.1.1330 | msg_show_console_dialog | cpp/unbounded-write | 4502 | FP | TP | 代码使用STRCPY（即strcpy）将message字符串复制到confirm_msg缓冲区，目标缓冲区大小由alloc(len)分配，而len的计算包含了STRLEN(message)，但未预留strcpy所需的终止空字符空间，存... |
| 1125 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2157 | FP | TP | 代码使用STRCPY（即strcpy）将fix_fname返回的字符串复制到新分配的缓冲区s中，而s的大小仅比源字符串长度多1字节，未考虑strcpy会复制末尾空字符，因此缓冲区大小恰好足够，不会溢出。但告警指出源可能来自环境变量等外... |
| 1130 | vim-9.1.1330 | get_emsg_source | cpp/unbounded-write | 502 | FP | TP | 代码使用sprintf格式化字符串，目标缓冲区大小由STRLEN(sname) + STRLEN(p)计算分配，但sprintf的格式字符串p包含一个'%s'占位符，其输出长度可能超过两个字符串长度的简单相加，存在缓冲区溢出风险。 |
| 1131 | vim-9.1.1330 | may_trigger_modechanged | cpp/unbounded-write | 2836 | FP | TP | 代码使用STRCPY（即strcpy）将curr_mode复制到last_mode，而last_mode是一个未在切片中定义大小的外部数组，curr_mode的长度由get_mode函数决定，可能达到MODE_MAX_LENGTH，若... |
| 1134 | vim-9.1.1330 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf 使用未受控的 `result` 参数作为格式化字符串的一部分，目标缓冲区 `reply` 的大小为 `STRLEN(result) + 32`，但 sprintf 的格式化输出长度可能超过此大小，导致缓冲区溢出。切片中... |
| 1132 | vim-9.1.1330 | expand_env_esc | cpp/unbounded-write | 1647 | FP | TP | 代码使用strcpy复制环境变量内容到目标缓冲区，虽然存在长度检查（STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen），但该检查依赖于STRLEN(var)的结果，而环境变量值可能被恶... |
| 1133 | vim-9.1.1330 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 切片代码中直接使用了未经验证长度的外部输入（如环境变量、文件读取内容）作为strcat的源字符串，而目标缓冲区大小未知，存在缓冲区溢出的真实风险。 |
| 1135 | vim-9.1.1330 | push_showcmd | cpp/unbounded-write | 1809 | FP | TP | 代码使用不安全的strcpy函数将内容从showcmd_buf复制到old_showcmd_buf，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未显示任何边界检查或安全防护措施。 |
| 1139 | vim-9.1.1330 | op_replace | cpp/unbounded-write | 1308 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的目标缓冲区，且切片内未见对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 1138 | vim-9.1.1330 | op_replace | cpp/unbounded-write | 1299 | FP | TP | 代码中直接使用STRCPY（即strcpy）将源字符串复制到目标缓冲区，未检查源字符串长度是否超过目标缓冲区大小。目标缓冲区newp的大小为oldlen + 1 + n，而源字符串来自oldp + bd.textcol + bd.te... |
| 1140 | vim-9.1.1330 | op_delete | cpp/unbounded-write | 962 | FP | TP | 代码在STRCPY宏（即strcpy）调用中，使用`oldp + bd.textcol + bd.textlen`作为源字符串，该源字符串来自缓冲区读取（ml_get），其长度未经验证，直接复制到目标缓冲区`newp + bd.tex... |
| 1145 | vim-9.1.1330 | mch_expand_wildcards | cpp/unbounded-write | 7371 | FP | TP | 代码在循环中使用宏 STRCPY（即 strcpy）将文件名复制到新分配的缓冲区，未检查目标缓冲区大小，而源字符串长度可能超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 1144 | vim-9.1.1330 | stropt_expand_envvar | cpp/unbounded-write | 1803 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串`s`复制到新分配的目标缓冲区`newval`，但未检查源字符串长度是否超过目标缓冲区大小。虽然`newlen`是根据`s`的长度计算分配的，但`s`来自`option_expand`函... |
| 1147 | vim-9.1.1330 | qf_store_title | cpp/unbounded-write | 1940 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的title字符串复制到新分配的缓冲区p中，虽然p的大小根据STRLEN(title)+2分配，但若title字符串在分配后、复制前被并发修改或本身不是以空字符结尾，strcpy可能引发... |
| 1146 | vim-9.1.1330 | mch_FullName | cpp/unbounded-write | 2829 | FP | TP | 代码在调用STRCPY（即strcpy）前，仅通过长度检查`(int)(buflen + STRLEN(fname)) >= len`来防止溢出，但未对源字符串`fname`的长度进行独立验证。若`fname`来自外部输入（如告警信息... |
| 1149 | vim-9.1.1330 | reg_submatch | cpp/unbounded-write | 2732 | FP | TP | 代码在多个位置使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区retval中，而retval的大小仅由alloc(len)分配，未对源字符串长度进行验证，存在缓冲区溢出风险。 |
| 1148 | vim-9.1.1330 | reg_submatch | cpp/unbounded-write | 2723 | FP | TP | 切片代码中，STRCPY宏被直接用于将未知长度的源字符串复制到固定大小的目标缓冲区，且未在复制前检查目标缓冲区大小。目标缓冲区retval由alloc(len)分配，其大小len基于外部输入（如匹配位置）计算，但STRCPY调用时未验... |
| 1151 | vim-9.1.1330 | match_with_backref | cpp/unbounded-write | 1600 | FP | TP | 代码使用STRCPY（即strcpy）将长度未知的源字符串rex.line复制到固定大小的缓冲区reg_tofree中，而reg_tofree的大小仅基于源字符串长度加50字节分配，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1150 | vim-9.1.1330 | regtilde | cpp/unbounded-write | 1959 | FP | TP | 代码使用STRCPY（即strcpy）将postfix复制到tmpsub缓冲区，而tmpsub的大小由tmpsublen计算得出。虽然tmpsublen计算了前缀、reg_prev_sublen和后缀的长度，但postfixlen是从... |
| 1152 | vim-9.1.1330 | get_reg_contents | cpp/unbounded-write | 2741 | FP | TP | 代码使用宏 STRCPY（即 strcpy）将 y_current->y_array[i].string 复制到固定大小的缓冲区 retval 中，而源字符串长度可能超过目标缓冲区剩余空间，存在缓冲区溢出风险。切片中未显示对源字符串长... |
| 1153 | vim-9.1.1330 | do_put | cpp/unbounded-write | 2164 | FP | TP | 切片代码中直接使用 STRCPY 宏（即 strcpy）将 y_array[y_size - 1].string 复制到固定大小的缓冲区 newp 中，而 newp 的大小由表达式 `ml_get_len(lnum) - col + ... |
| 1154 | vim-9.1.1330 | do_put | cpp/unbounded-write | 2165 | FP | TP | 切片代码中直接使用了未经验证长度的源字符串（如 y_array[i].string）作为 strcpy 的目标，且目标缓冲区大小未在切片中明确验证，存在缓冲区溢出风险。 |
| 1155 | vim-9.1.1330 | op_yank | cpp/unbounded-write | 1317 | FP | TP | 代码使用STRCPY（即strcpy）宏进行字符串拼接，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中可见目标缓冲区pnew是通过alloc分配，但拼接前未验证其长度是否足以容纳源字符串。 |
| 1156 | vim-9.1.1330 | op_yank | cpp/unbounded-write | 1318 | FP | TP | 代码使用STRCPY（即strcpy）宏进行字符串拼接，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中可见源字符串长度来自用户控制的寄存器内容，且无边界检查。 |
| 1157 | vim-9.1.1330 | stuff_yank | cpp/unbounded-write | 470 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串复制到目标缓冲区，目标缓冲区大小由`tmplen`决定，但strcpy不检查目标缓冲区大小，若源字符串长度超过`tmplen`（已分配的大小减1），将导致缓冲区溢出。切片中未见任何对源字... |
| 1158 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2838 | FP | TP | 代码使用strcat将用户输入（name参数）拼接到固定大小的缓冲区（scriptname）中，而scriptname的大小仅基于name的长度分配，未考虑已拼接的'autoload/'前缀和后续添加的'.vim'后缀，存在缓冲区溢出... |
| 1159 | vim-9.1.1330 | ExpandPackAddDir | cpp/unbounded-write | 1309 | FP | TP | sprintf 使用未经验证的用户输入 `pat` 作为格式化字符串的一部分，目标缓冲区 `s` 的大小为 `pat_len + 26`，但格式化字符串 `"pack/*/opt/%s*"` 在拼接 `pat` 后可能超过缓冲区大小，... |
| 1160 | vim-9.1.1330 | sign_jump | cpp/unbounded-write | 1313 | FP | TP | sprintf 使用未限制长度的缓冲区 buf->b_fname 作为输入，该缓冲区内容来自外部文件路径，可能导致目标缓冲区 cmd 溢出，因为 cmd 的分配大小仅基于当前 b_fname 长度，无法防御更长的恶意输入。 |
| 1162 | vim-9.1.1330 | make_case_word | cpp/unbounded-write | 3140 | FP | TP | 代码直接使用不安全的strcpy宏复制字符串，未检查目标缓冲区大小，且告警信息指出输入源包括环境变量、外部输入和文件读取等，存在缓冲区溢出风险。 |
| 1161 | vim-9.1.1330 | dump_word | cpp/unbounded-write | 4187 | FP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或外部数据（如word或cword），且切片中未显示对p的长度进行任何校验，存在缓冲区溢出风险。 |
| 1163 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2998 | FP | TP | 代码使用STRCPY宏（即strcpy）将repl_to复制到新分配的缓冲区p中，未检查目标缓冲区大小，而repl_to是全局变量，其长度可能超过目标缓冲区p的剩余空间，存在缓冲区溢出风险。 |
| 1164 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2999 | FP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p中，但p的大小是基于ml_get_curline_len() + addlen + 1分配的，而addlen可能为负数（当repl_to_len < repl_fro... |
| 1165 | vim-9.1.1330 | count_common_word | cpp/unbounded-write | 1919 | FP | TP | 代码使用STRCPY（即strcpy）将未限制长度的字符串p复制到新分配的内存wc->wc_word中，而p的来源是用户输入参数word，存在缓冲区溢出风险。切片中未见对输入长度进行校验或使用安全复制函数。 |
| 1166 | vim-9.1.1330 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）将参数lang直接复制到固定大小的数组sl.sl_lang中，但切片未显示对lang的长度有任何校验或限制。由于lang是函数参数，其来源可能不受控，存在缓冲区溢出风险。 |
| 1167 | vim-9.1.1330 | spell_move_to | cpp/unbounded-write | 1420 | FP | TP | 代码使用STRCPY宏（即strcpy）将长度不确定的字符串`line`复制到固定大小的缓冲区`buf`中，而`buf`的大小仅根据`len + MAXWLEN + 2`分配，未限制源字符串长度，存在缓冲区溢出风险。 |
| 1169 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2369 | FP | TP | 代码在构建警告信息字符串时，使用STRCAT将items[0]和items[1]拼接到一个缓冲区p中，但p的大小是根据spin->si_info的当前长度加上items[0]和items[1]的长度动态计算的，没有检查缓冲区边界。如果... |
| 1170 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2371 | FP | TP | 代码在行号2371处使用STRCAT(p, items[1])，其中items[1]来自外部文件读取的输入（通过fgets），且目标缓冲区p的大小由动态计算的长度决定，未检查拼接后是否超出缓冲区边界，存在缓冲区溢出的风险。 |
| 1172 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2495 | FP | TP | 代码在拼接字符串时使用STRCAT宏（即strcat），目标缓冲区p的大小由动态计算的长度决定，但未检查拼接后是否超出分配的内存大小，存在缓冲区溢出的风险。 |
| 1171 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2464 | FP | TP | 代码使用STRCPY宏（即strcpy）将items[1]复制到缓冲区p，而items[1]来自外部文件行（通过fgets读取），其长度可能超过p的分配大小（STRLEN(items[1]) + 2），导致缓冲区溢出。切片中未见对it... |
| 1173 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2644 | FP | TP | 代码使用STRCPY宏（即strcpy）将items[1]复制到p，而items[1]来自外部文件读取的未经验证的行，可能导致目标缓冲区溢出。切片中未显示对items[1]长度的检查或安全限制。 |
| 1174 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2746 | FP | TP | 代码中直接使用 sprintf 将 items[4] 拼接到 buf 中，而 items[4] 来源于外部文件读取的未经验证的行数据，可能导致缓冲区溢出。切片中未显示对 items[4] 长度的检查或防护。 |
| 1175 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2748 | FP | TP | 切片代码中第2748行使用sprintf将items[4]拼接到buf中，buf大小为MAXLINELEN，但items[4]来自外部文件行解析，未检查长度，可能导致缓冲区溢出。 |
| 1180 | vim-9.1.1330 | expand_tag_fname | cpp/unbounded-write | 4129 | FP | TP | 代码使用STRCPY（即strcpy）将tag_fname复制到固定大小的缓冲区retval（大小为MAXPATHL），但未检查tag_fname的长度是否超过MAXPATHL，存在缓冲区溢出风险。 |
| 1182 | vim-9.1.1330 | findtags_add_match | cpp/unbounded-write | 2624 | FP | TP | 代码中直接使用 STRCPY（即 strcpy）将来源未知的字符串（如 st->help_lang）复制到固定大小的缓冲区中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1184 | vim-9.1.1330 | show_one_termcode | cpp/unbounded-write | 7050 | FP | TP | 代码使用STRCPY（即strcpy）将get_special_key_name返回的字符串复制到IObuff缓冲区，目标缓冲区大小未知，而源字符串长度可能超过目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 1183 | vim-9.1.1330 | findtags_add_match | cpp/unbounded-write | 2703 | FP | TP | 切片代码中多次使用STRCPY（即strcpy）宏，将长度未知的源字符串（如st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区，未进行边界检查，存在缓冲区溢出风险。 |
| 1181 | vim-9.1.1330 | get_tagfname | cpp/unbounded-write | 3435 | FP | TP | 代码在行`STRCPY(buf, fname);`处使用`strcpy`将`vim_findfile`返回的路径字符串`fname`复制到固定大小的缓冲区`buf`中。`vim_findfile`函数内部路径构建逻辑复杂，可能返回超过... |
| 1185 | vim-9.1.1330 | current_tagblock | cpp/unbounded-write | 1392 | FP | TP | sprintf 使用未限制长度的用户输入（来自缓冲区 p 和变量 len）格式化字符串到固定大小的缓冲区（spat/epat），存在缓冲区溢出风险。切片中未显示对 len 或 p 的长度校验或安全边界检查。 |
| 1186 | vim-9.1.1330 | uc_check_code | cpp/unbounded-write | 1782 | FP | TP | 代码在多个分支中直接使用STRCPY（即strcpy）将外部输入（如eap->arg、*split_buf）复制到固定缓冲区buf，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1188 | vim-9.1.1330 | alloc_ufunc | cpp/unbounded-write | 728 | FP | TP | 代码使用不安全的strcpy函数，将外部传入的name字符串复制到固定大小的缓冲区fp->uf_name中，而缓冲区大小由namelen参数决定，若name长度超过namelen或namelen计算错误，将导致缓冲区溢出。切片中未见对... |
| 1187 | vim-9.1.1330 | fname_trans_sid | cpp/unbounded-write | 2259 | FP | TP | 代码使用STRCPY（即strcpy）将script_name复制到fname_buf + fname_buflen处，目标缓冲区大小FLEN_FIXED固定，但源字符串script_name长度未经验证，且条件fnamelen < ... |
| 1190 | vim-9.1.1330 | generate_PUSHFUNC | cpp/unbounded-write | 1041 | FP | TP | 代码使用 STRCPY（即 strcpy）将外部传入的 name 字符串复制到固定大小的缓冲区 funcname 中，而 funcname 的大小仅为 STRLEN(name) + 3，未考虑目标缓冲区大小，存在缓冲区溢出风险。 |
| 1191 | vim-9.1.1330 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串name复制到固定大小的缓冲区newsav->sav_key中，存在缓冲区溢出风险。切片显示name是函数参数，其来源和长度未知，且没有边界检查。 |
| 1192 | vim-9.1.1330 | find_exported | cpp/unbounded-write | 756 | FP | TP | 代码使用`sprintf`将外部可控的`name`参数和`script->sn_autoload_prefix`拼接到固定大小的缓冲区`buffer`或动态分配的`funcname`中，未对`name`的长度进行限制，存在缓冲区溢出风险。 |
| 1193 | vim-9.1.1330 | find_exported | cpp/unbounded-write | 763 | FP | TP | sprintf 使用不受控的 `name` 参数和 `sid` 格式化字符串，目标缓冲区 `funcname` 的大小基于 `len` 计算，但 `len` 的计算未考虑格式化后的实际长度，存在缓冲区溢出风险。 |
| 1194 | vim-9.1.1330 | xxdline | cpp/unbounded-write | 537 | FP | TP | 函数`xxdline`中的`strcpy(z, l)`将参数`l`直接复制到固定大小的缓冲区`z`（大小为`LLEN+1`），而`l`是外部输入（如命令行参数），切片中未显示对`l`长度的任何校验，存在缓冲区溢出风险。 |
| 1195 | vim-9.1.1330 | ExpandBufnames | cpp/invalid-pointer-deref | 2971 | FP | TP | 切片代码显示，在循环中`(*file)[count++] = p;`处对`*file`数组进行写入，但`*file`仅在`round == 2`时通过`*file = ALLOC_MULT(char_u *, count);`分配内存... |
| 1196 | vim-9.1.1330 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | TP | 当 width 为 2 时，代码在 p[pos.col + 1] = p[pos.col] 处存在越界写入风险，因为 p 被分配了 len 个元素，而 pos.col + 1 可能等于 len，导致写入超出分配的内存边界。 |
| 1201 | vim-9.1.0790 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数 getcell 可能返回 NULL，但调用后未检查返回值就直接解引用 cell->chars[0]，存在空指针解引用风险。切片代码中无任何防护机制。 |
| 1203 | vim-9.1.0790 | get_isolated_shell_name | cpp/inconsistent-null-check | 2706 | FP | TP | 函数`vim_strnsave`可能返回NULL，但调用者`get_isolated_shell_name`未检查返回值，直接将其赋值给指针`p`并返回，存在解引用空指针的风险。 |
| 1221 | vim-9.1.0790 | do_put | cpp/unsafe-strcat | 2095 | FP | TP | 代码中直接使用了不安全的STRCAT宏（即strcat），且切片内未显示对目标缓冲区大小进行任何检查，存在缓冲区溢出的风险。 |
| 1224 | vim-9.1.0790 | highlight_color | cpp/overrunning-write | 3254 | FP | TP | sprintf 目标缓冲区 'buf' 大小为10字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少10字节，当 rgb 值较大时（如0xffffffff）输出将超过10字节，导致缓冲区溢出。 |
| 1223 | vim-9.1.0790 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 目标缓冲区 tbuf 大小为 20 字节，但格式化字符串 '%6ld' 最多可产生 6 位数字加符号和终止符，共 8 字节，不会溢出。然而，告警指出需要 21 字节，这可能是因为 long 类型在特定平台上的最大值（如... |
| 1225 | vim-9.1.0790 | msg_outnum | cpp/overrunning-write | 1555 | FP | TP | 函数使用`sprintf`将长整型数`n`写入大小为20字节的缓冲区`buf`，当`n`为最小值（如-9223372036854775808）时，格式化字符串`"%ld"`将产生21字节（包括负号和终止空字符），导致缓冲区溢出。 |
| 1226 | vim-9.1.0790 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 写入的目标缓冲区 'reply' 大小为 32 字节，但格式化字符串 "%d %ld\n" 在极端情况下（如 cmdno 为负且结果值很大）可能产生超过 32 字节的字符串，导致缓冲区溢出。切片代码中未见任何长度检查或... |
| 1227 | vim-9.1.0790 | ga_concat_strings | cpp/unbounded-write | 788 | FP | TP | 代码使用不安全的strcpy函数，将长度未知的源字符串（来自gap->ga_data数组）复制到固定大小的缓冲区p中，而p的大小仅由之前的alloc(len+1)分配，但循环中多次调用STRCPY可能导致p指针越界，存在缓冲区溢出风险。 |
| 1228 | vim-9.1.0790 | maketitle | cpp/unbounded-write | 4145 | FP | TP | 代码使用STRCPY（即strcpy）将变量p的内容复制到icon_str中，而icon_str指向大小为IOSIZE的缓冲区buf。p来源于文件路径，其长度未经验证，可能超过IOSIZE，导致缓冲区溢出。 |
| 1229 | vim-9.1.0790 | buf_write | cpp/unbounded-write | 1208 | FP | TP | 代码中直接使用STRCPY（即strcpy）将fname复制到IObuff缓冲区，未检查fname长度是否超过IObuff大小，存在缓冲区溢出风险。切片中未显示IObuff的大小定义，但strcpy的固有缺陷是已知的，且fname是外... |
| 1232 | vim-9.1.0790 | transstr | cpp/unbounded-write | 366 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区res追加内容，而res的大小由alloc(len + 1)分配，其长度len由输入字符串s计算得出。由于transchar_byte函数可能返回长度大于1的字符串（如转义序列... |
| 1231 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2138 | FP | TP | 代码中直接使用STRCAT宏（即strcat）将p_extra拼接到leader缓冲区，而leader缓冲区的大小由alloc分配，其大小计算涉及多个变量（lead_len、lead_repl_len、extra_space、extr... |
| 1234 | vim-9.1.0790 | win_redr_status_matches | cpp/unbounded-write | 639 | FP | TP | 代码在多个位置使用STRCPY（即strcpy）宏，将外部来源（如环境变量、文件读取）的数据复制到固定大小的缓冲区中，且切片内未见对源数据长度的检查或限制，存在缓冲区溢出风险。 |
| 1235 | vim-9.1.0790 | win_redr_status_matches | cpp/unbounded-write | 658 | FP | TP | 代码使用STRCPY（即strcpy）将transchar_byte函数的返回值复制到固定大小的缓冲区buf中，未检查目标缓冲区剩余空间，存在缓冲区溢出风险。切片中未显示对目标缓冲区边界的任何防护。 |
| 1236 | vim-9.1.0790 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的源字符串（fname + 3）复制到固定大小的目标缓冲区（name + 5），存在缓冲区溢出风险。切片中未显示对fname长度的检查或使用安全函数。 |
| 1237 | vim-9.1.0790 | has_profiling | cpp/unbounded-write | 973 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的源字符串fname复制到固定大小的目标缓冲区pe->pen_name，存在缓冲区溢出风险。切片显示目标缓冲区大小基于STRLEN(fname)+1动态分配，但strcpy本身不检查... |
| 1238 | vim-9.1.0790 | do_string_sub | cpp/unbounded-write | 7697 | FP | TP | 代码在告警行使用STRCPY（即strcpy）将'tail'字符串复制到动态分配的缓冲区'ga.ga_data'的末尾，但未检查目标缓冲区剩余空间是否足够容纳源字符串。'tail'是用户输入'str'的子串，其长度未经验证，可能导致缓... |
| 1239 | vim-9.1.0790 | make_expanded_name | cpp/unbounded-write | 6918 | FP | TP | 代码使用STRCPY（即strcpy）将in_start复制到新分配的缓冲区retval，但未检查in_start的长度是否超过retval的大小。虽然retval的大小是根据表达式结果动态计算的，但in_start是函数参数，其长度... |
| 1240 | vim-9.1.0790 | make_expanded_name | cpp/unbounded-write | 6920 | FP | TP | 代码使用strcat拼接字符串，目标缓冲区retval的大小基于temp_result的长度计算，但temp_result来自eval_to_string的返回值，其内容可能包含用户输入或环境变量，长度可能超过分配的空间，导致缓冲区溢出。 |
| 1241 | vim-9.1.0790 | set_var_const | cpp/unbounded-write | 4183 | FP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname长度未受限制，可能导致目标缓冲区溢出。切片中未显示对varname长度的检查或使用安全函数。 |
| 1242 | vim-9.1.0790 | cat_prefix_varname | cpp/unbounded-write | 2504 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的`name`字符串复制到固定大小的缓冲区`varnamebuf`中，虽然缓冲区大小`len`根据`name`长度动态分配，但分配后立即执行复制，未检查`name`在分配后是否被修改或是... |
| 1247 | vim-9.1.0790 | expand_sfile | cpp/unbounded-write | 9801 | FP | TP | 代码使用STRCPY（即strcpy）将可变长度字符串repl复制到固定大小的缓冲区newres中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1243 | vim-9.1.0790 | ex_substitute | cpp/unbounded-write | 4883 | FP | TP | 切片代码中明确使用了未进行边界检查的STRCAT宏（即strcat），将sub_firstline + copycol的内容追加到new_start指向的缓冲区。new_start缓冲区的大小通过new_start_len管理，但追加... |
| 1246 | vim-9.1.0790 | ex_sort | cpp/unbounded-write | 605 | FP | TP | 代码使用STRCPY宏（即strcpy）将ml_get返回的字符串s复制到固定大小的缓冲区sortbuf1中，而sortbuf1的大小基于maxlen+1分配。maxlen是待排序行的最大长度，但ml_get返回的缓冲区内容可能被外部... |
| 1248 | vim-9.1.0790 | repl_cmdline | cpp/unbounded-write | 5302 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串复制到固定大小的缓冲区new_cmdline中，且目标缓冲区大小由变量i决定，而i的计算依赖于多个外部输入（如repl, src, eap->nextcmd），未进行边界检查... |
| 1249 | vim-9.1.0790 | repl_cmdline | cpp/unbounded-write | 5308 | FP | TP | 代码使用STRCPY（即strcpy）向固定大小的缓冲区new_cmdline写入数据，而目标缓冲区的大小'i'是根据多个字符串长度计算得出，但写入的源字符串eap->nextcmd长度未经验证，可能导致缓冲区溢出。 |
| 1250 | vim-9.1.0790 | replace_makeprg | cpp/unbounded-write | 5009 | FP | TP | 代码使用STRCPY（即strcpy）宏将用户控制的参数p复制到新分配的缓冲区ptr中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未显示对p的长度有任何限制或验证。 |
| 1251 | vim-9.1.0790 | replace_makeprg | cpp/unbounded-write | 5024 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入（program和p）复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小通过alloc动态分配，但分配的长度计算未考虑strcpy可能添加的终止空字符，且未对... |
| 1254 | vim-9.1.0790 | get_exception_string | cpp/unbounded-write | 473 | FP | TP | 代码使用strcat向固定大小的缓冲区val追加内容，而val指向由vim_strnsave分配的缓冲区的一部分，其剩余空间取决于mesg的长度。由于mesg来自外部输入（如环境变量、文件读取等），且切片中未显示对mesg长度的检查或... |
| 1252 | vim-9.1.0790 | do_one_cmd | cpp/unbounded-write | 2673 | FP | TP | 切片代码中明确存在对STRCPY宏（即strcpy）的调用，且其目标缓冲区IObuff的大小未知，而源数据来自外部输入（如errormsg），存在缓冲区溢出的风险。 |
| 1255 | vim-9.1.0790 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 代码使用`sprintf`将未受控的字符串`&mesg[1]`写入缓冲区`val`，而`val`指向的缓冲区大小由`vim_strnsave`分配，其大小基于`mesg`长度计算，但`&mesg[1]`可能包含任意内容，长度可能超过剩... |
| 1257 | vim-9.1.0790 | cmdline_browse_history | cpp/unbounded-write | 1498 | FP | TP | 代码使用STRCPY宏（即strcpy）将历史记录字符串p复制到固定大小的缓冲区ccline.cmdbuff，而p的长度plen可能超过alloc_cmdbuff分配的缓冲区大小，存在缓冲区溢出风险。 |
| 1256 | vim-9.1.0790 | escape_fname | cpp/unbounded-write | 4109 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串(*pp)复制到目标缓冲区(p+1)，目标缓冲区大小仅为源字符串长度加2（alloc(STRLEN(*pp) + 2)），未预留字符串终止符'\0'的空间，strcpy会复制终止符，因此... |
| 1258 | vim-9.1.0790 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 864 | FP | TP | 代码使用STRCPY（即strcpy）将动态长度的字符串p复制到固定大小的缓冲区ccline.cmdbuff，虽然之前调用了realloc_cmdbuff来调整缓冲区大小，但strcpy本身不检查目标缓冲区边界，若p长度超过缓冲区分配... |
| 1259 | vim-9.1.0790 | <global> | cpp/unbounded-write | 5375 | FP | TP | sprintf 使用未限制长度的字符串 vim_tempdir 和递增的整数 temp_count 进行拼接，目标缓冲区 itmp 大小固定为 TEMPNAMELEN，存在缓冲区溢出风险。 |
| 1260 | vim-9.1.0790 | vim_settempdir | cpp/unbounded-write | 5235 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的源字符串tempdir复制到固定大小的缓冲区buf中，存在缓冲区溢出风险。切片显示buf大小为MAXPATHL+2，但tempdir作为参数传入，其来源和长度未在切片内验证，直接使... |
| 1261 | vim-9.1.0790 | <global> | cpp/unbounded-write | 4352 | FP | TP | 代码使用sprintf将用户控制的路径和消息字符串格式化到固定大小的缓冲区tbuf中，tbuf的大小基于字符串长度计算，但sprintf的格式字符串mesg来自外部资源（翻译字符串），若其包含额外的格式说明符将导致缓冲区溢出。 |
| 1263 | vim-9.1.0790 | buf_modname | cpp/unbounded-write | 3620 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证的外部输入fname复制到新分配的缓冲区retval，且未检查fname长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 1264 | vim-9.1.0790 | addfile | cpp/unbounded-write | 4198 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证的外部文件名`f`复制到新分配的缓冲区`p`，虽然缓冲区大小基于`STRLEN(f) + 1`分配，但若`f`在分配后、复制前被并发修改或指向非字符串数据，仍可能导致缓冲区溢出。切片中未... |
| 1265 | vim-9.1.0790 | unix_expandpath | cpp/unbounded-write | 3833 | FP | TP | 代码在多个位置使用STRCPY宏（即strcpy）将未知长度的字符串（如环境变量、外部输入、文件读取内容）复制到固定大小的缓冲区中，存在缓冲区溢出的风险。切片中未显示对源字符串长度的检查或使用安全函数。 |
| 1267 | vim-9.1.0790 | concat_fnames | cpp/unbounded-write | 3126 | FP | TP | 函数使用strcat拼接两个字符串，但目标缓冲区大小仅根据两个输入字符串的当前长度分配，若fname2在调用后被外部修改或指向的缓冲区内容被恶意扩展，则后续的STRCAT可能导致缓冲区溢出。切片中未显示对输入字符串的不可变性或长度限制... |
| 1268 | vim-9.1.0790 | uniquefy_paths | cpp/unbounded-write | 2364 | FP | TP | 代码使用STRCAT宏（即strcat）向file_pattern缓冲区追加内容，而file_pattern的大小仅根据pattern长度加2分配，未考虑追加后可能超出缓冲区边界，存在缓冲区溢出风险。 |
| 1269 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1718 | FP | TP | 代码中直接使用STRCPY（即strcpy）将外部输入（如rel_fname或*file_to_find）复制到固定大小的缓冲区NameBuff，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1270 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1719 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区NameBuff（大小为MAXPATHL），未检查源字符串长度，存在缓冲区溢出风险。 |
| 1271 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1724 | FP | TP | 代码中直接使用STRCPY（即strcpy）将用户控制的输入（*file_to_find）复制到固定大小的缓冲区NameBuff，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1272 | vim-9.1.0790 | ff_check_visited | cpp/unbounded-write | 1370 | FP | TP | 代码使用STRCPY（即strcpy）将ff_expand_buffer复制到vp->ffv_fname，而目标缓冲区vp->ffv_fname的大小是根据源字符串长度动态分配的，但分配大小仅为字符串长度加1，未包含结构体本身可能需要... |
| 1279 | vim-9.1.0790 | <global> | cpp/unbounded-write | 537 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将长度未知的字符串复制到固定大小的缓冲区ff_expand_buffer，而该缓冲区在切片中被分配为MAXPATHL大小。多个STRCPY调用未检查源字符串长度，存在缓冲区溢出的风险。 |
| 1281 | vim-9.1.0790 | <global> | cpp/unbounded-write | 548 | FP | TP | 代码使用STRCAT宏（即strcat）将search_ctx->ffsc_fix_path拼接到ff_expand_buffer，而ff_expand_buffer是固定大小为MAXPATHL的缓冲区。切片中未显示对拼接后总长度是否... |
| 1282 | vim-9.1.0790 | <global> | cpp/unbounded-write | 590 | FP | TP | 切片代码中多次使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的缓冲区（如ff_expand_buffer），且源字符串（如search_ctx->ffsc_fix_path + len）来自外部输入，未进行长度... |
| 1280 | vim-9.1.0790 | <global> | cpp/unbounded-write | 545 | FP | TP | 切片代码中多次使用STRCPY（即strcpy）宏，将长度未知的源字符串复制到固定大小的缓冲区（如ff_expand_buffer），且未检查源字符串长度是否小于目标缓冲区大小。例如，`STRCPY(ff_expand_buffer,... |
| 1283 | vim-9.1.0790 | <global> | cpp/unbounded-write | 591 | FP | TP | 切片代码中，`STRCAT(temp, search_ctx->ffsc_wc_path)` 使用了不安全的 `strcat` 函数，且 `temp` 缓冲区的大小为 `STRLEN(search_ctx->ffsc_wc_path)... |
| 1285 | vim-9.1.0790 | foldDelMarker | cpp/unbounded-write | 1897 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串p+len复制到目标缓冲区newline + (p - line)，未检查目标缓冲区大小，而源字符串长度可能超过目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 1284 | vim-9.1.0790 | <global> | cpp/unbounded-write | 3798 | FP | TP | 代码使用 strcat 将未经验证长度的字符串 s 追加到缓冲区 r 中，而 r 的分配大小虽然考虑了 s 的长度，但 s 的内容来自文件行（ml_get），其长度可能超过分配时预留的空间（因为 STRLEN(s) 在分配时计算，但后... |
| 1286 | vim-9.1.0790 | foldAddMarker | cpp/unbounded-write | 1815 | FP | TP | 代码使用STRCPY（即strcpy）将未知长度的字符串line复制到固定大小的缓冲区newline中，而newline的大小基于line_len、markerlen和STRLEN(cms)计算，但line的内容来自ml_get，其长... |
| 1287 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2899 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_prolog->title复制到固定大小的buffer[256]中，而res_prolog->title是从外部资源文件读取的，其长度未经验证，存在缓冲区溢出风险。 |
| 1288 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2901 | FP | TP | 代码使用STRCAT宏（即strcat）将res_prolog->version拼接到固定大小的buffer数组，而buffer在之前已存储了res_prolog->title和一个空格，存在缓冲区溢出风险。切片中未显示对versio... |
| 1289 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2905 | FP | TP | 代码使用STRCPY（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而title来源于外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 1290 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2907 | FP | TP | 代码使用STRCAT宏（即strcat）将res_cidfont->version拼接到buffer中，而buffer是大小为256的固定数组。切片显示version字段来自外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 1291 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2912 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_cmap->title复制到固定大小的buffer[256]中，而title来源于外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 1293 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2920 | FP | TP | 代码使用STRCPY宏（即strcpy）将res_encoding->title复制到固定大小的buffer[256]中，而title来源于外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 1292 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2914 | FP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的源字符串（res_cmap->version）长度未知，存在缓冲区溢出的风险。切片中未显示对源字符串长度的检查或限制。 |
| 1294 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2922 | FP | TP | 代码使用STRCAT宏（即strcat）将资源文件的title和version字段拼接到固定大小的缓冲区buffer（256字节）中，未检查长度，存在缓冲区溢出风险。切片中未显示对title或version长度的任何限制或验证。 |
| 1295 | vim-9.1.0790 | prt_resource_name | cpp/unbounded-write | 1659 | FP | TP | 代码使用strcpy复制字符串，虽然对源字符串长度进行了检查，但检查目标是MAXPATHL，而目标缓冲区resource_filename的大小未知，存在缓冲区溢出风险。 |
| 1296 | vim-9.1.0790 | do_helptags | cpp/unbounded-write | 1210 | FP | TP | 代码中多次使用STRCPY宏（即strcpy）将外部输入（如环境变量、文件读取内容）复制到固定大小的缓冲区（如NameBuff、fname、ext），未检查长度，存在缓冲区溢出风险。 |
| 1297 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 975 | FP | TP | 代码使用STRCAT宏（即strcat）向NameBuff缓冲区追加内容，而NameBuff的大小未在切片中明确限定，存在缓冲区溢出的风险。告警指出输入来自fread读取的字符串，进一步确认了数据源可能不受控。 |
| 1298 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 991 | FP | TP | 代码使用STRCAT宏（即strcat）将参数tagfname拼接到NameBuff缓冲区，而NameBuff的大小未知（切片中未定义其大小），且tagfname是函数参数，其长度不受控，存在缓冲区溢出风险。 |
| 1299 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 1112 | FP | TP | 代码使用 sprintf 将未经验证长度的字符串 p1 和 fname 写入固定大小的缓冲区 s，缓冲区大小计算为 p2 - p1 + STRLEN(fname) + 2，但 p1 和 p2 指向从文件读取的 IObuff 缓冲区，其... |
| 1301 | vim-9.1.0790 | load_colors | cpp/unbounded-write | 602 | FP | TP | 代码使用`sprintf`将外部输入`name`拼接到固定大小的缓冲区`buf`中，而`buf`的大小仅基于`STRLEN(name) + 12`分配，未考虑`sprintf`添加的格式字符串`"colors/%s.vim"`可能导致... |
| 1302 | vim-9.1.0790 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | sprintf 使用用户控制的 `name` 和 `csinfo[i].ppath` 拼接字符串，目标缓冲区 `fullname` 的大小 `len` 基于这两个字符串的长度计算，但未考虑格式化字符串 `"%s/%s"` 中额外添加的... |
| 1303 | vim-9.1.0790 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | TP | 代码使用`sprintf`将多个字符串拼接写入固定大小的缓冲区`buf`，缓冲区大小`amt`的计算基于`strlen`结果，但计算时未考虑`sprintf`添加的格式化字符（如制表符、分号、引号）所占的确切字节数，可能导致缓冲区大小... |
| 1306 | vim-9.1.0790 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，未检查fname长度是否超过分配的大小（strlen(fname)+1），存在缓冲区溢出风险。 |
| 1305 | vim-9.1.0790 | <global> | cpp/unbounded-write | 1456 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，未检查fname长度是否超过目标缓冲区大小。alloc(strlen(fname)+1)分配了精确长度，但strcpy本身不检查边界，若fname在分配后被修改或存在并发问题，仍可... |
| 1307 | vim-9.1.0790 | cs_add_common | cpp/unbounded-write | 604 | FP | TP | 代码使用sprintf拼接路径和文件名，未检查目标缓冲区大小。fname2的分配大小基于strlen(fname)和strlen(CSCOPE_DBFILE)计算，但sprintf可能写入额外的字符（如'/'和字符串终止符），存在缓冲... |
| 1309 | vim-9.1.0790 | <global> | cpp/unbounded-write | 3119 | FP | TP | 代码使用`sprintf`将`transchar(from)`的结果写入固定大小的缓冲区`args->os_errbuf`，未进行长度检查，存在缓冲区溢出风险。切片中未显示对`args->os_errbuf`大小的限制或对`trans... |
| 1312 | vim-9.1.0790 | <global> | cpp/unbounded-write | 811 | FP | TP | 代码使用宏STRCPY（即strcpy）将call_data复制到固定大小的缓冲区menu->strings[i]中，而call_data是外部传入的字符串，其长度未经验证，存在缓冲区溢出风险。 |
| 1311 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2157 | FP | TP | 代码使用STRCPY（即strcpy）将fix_fname返回的字符串复制到新分配的缓冲区s中，而s的大小仅为STRLEN(f) + 1，与源字符串长度相同，未预留额外空间。若fix_fname内部处理（如路径展开）导致返回的字符串长... |
| 1313 | vim-9.1.0790 | <global> | cpp/unbounded-write | 815 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将call_data字符串复制到固定大小的缓冲区menu->strings[i]中，而目标缓冲区的大小仅通过alloc(STRLEN(call_data) + 5)分配，未对源字符串长度进... |
| 1314 | vim-9.1.0790 | msg_show_console_dialog | cpp/unbounded-write | 4387 | FP | TP | 代码使用STRCPY（即strcpy）将message字符串复制到confirm_msg缓冲区，而confirm_msg的大小仅由len决定，len的计算包含了STRLEN(message)，但未预留额外的空间来确保目标缓冲区能容纳源... |
| 1316 | vim-9.1.0790 | get_emsg_source | cpp/unbounded-write | 484 | FP | TP | 代码使用sprintf格式化字符串，目标缓冲区Buf的大小通过alloc(STRLEN(sname) + STRLEN(p))分配，但sprintf的格式字符串p包含一个'%s'占位符，其总长度应为STRLEN(p) - 2 + ST... |
| 1317 | vim-9.1.0790 | may_trigger_modechanged | cpp/unbounded-write | 2821 | FP | TP | 代码使用STRCPY（即strcpy）将curr_mode复制到last_mode，而last_mode未在切片中声明其大小，且curr_mode来自get_mode函数，其长度可能达到MODE_MAX_LENGTH，存在缓冲区溢出风险。 |
| 1319 | vim-9.1.0790 | call_shell | cpp/unbounded-write | 1877 | FP | TP | 代码使用strcat向固定大小的缓冲区ncmd追加内容，ncmd的大小基于ecmd和p_sxq的长度计算，但未考虑追加的第三个字符串的长度，存在缓冲区溢出的风险。 |
| 1321 | vim-9.1.0790 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf 使用未受控的外部输入 result 作为格式化字符串的一部分，且分配的缓冲区大小仅基于 result 的长度加上固定偏移，未考虑格式化后字符串的总长度可能超过分配大小，存在缓冲区溢出风险。 |
| 1322 | vim-9.1.0790 | push_showcmd | cpp/unbounded-write | 1805 | FP | TP | 代码使用不安全的strcpy函数将内容从showcmd_buf复制到old_showcmd_buf，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1320 | vim-9.1.0790 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | TP | 切片代码中明确存在对`STRCAT`宏（即`strcat`）的不安全调用，目标缓冲区`newline`的大小为`ml_get_len(lnum) + len + 1`，而追加的源字符串`oldline + col`长度未知，可能导致缓... |
| 1324 | vim-9.1.0790 | op_change | cpp/unbounded-write | 1867 | FP | TP | 代码中直接使用STRCPY（即strcpy）宏，将源字符串（oldp + bd.textcol）复制到目标缓冲区（newp + newlen + ins_len），未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1325 | vim-9.1.0790 | op_replace | cpp/unbounded-write | 1163 | FP | TP | 代码中直接使用STRCPY（即strcpy）宏，将源字符串复制到目标缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。告警消息指出源数据可能来自环境变量、外部输入或文件读取，切片代码中未见任何长度校验或安全复制机制。 |
| 1326 | vim-9.1.0790 | op_replace | cpp/unbounded-write | 1172 | FP | TP | 代码中直接使用STRCPY宏（即strcpy）将未知长度的源字符串复制到固定大小的目标缓冲区，且切片中未显示对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 1327 | vim-9.1.0790 | op_delete | cpp/unbounded-write | 826 | FP | TP | 代码中直接使用STRCPY（即strcpy）宏，将源字符串`oldp + bd.textcol + bd.textlen`复制到目标缓冲区`newp + bd.textcol + bd.startspaces + bd.endspac... |
| 1331 | vim-9.1.0790 | stropt_expand_envvar | cpp/unbounded-write | 1800 | FP | TP | 代码使用STRCPY（即strcpy）将环境变量扩展后的字符串`s`复制到新分配的缓冲区`newval`中，未检查`s`的长度是否超过`newlen`（已分配大小）。`newlen`的计算基于`STRLEN(s) + 1`，但`s`来... |
| 1332 | vim-9.1.0790 | mch_expand_wildcards | cpp/unbounded-write | 6937 | FP | TP | 代码使用宏STRCAT（即strcat）向固定大小的缓冲区`command`追加内容，而`command`的大小`len`是基于多个变量（如`tempname`、`pat`等）的长度计算分配的。若这些输入源（如环境变量、外部输入）的总... |
| 1333 | vim-9.1.0790 | mch_expand_wildcards | cpp/unbounded-write | 7283 | FP | TP | 代码中存在多处对 STRCPY 宏（即 strcpy）的调用，其目标缓冲区大小由 alloc 分配，但源数据（如环境变量、外部输入、文件读取内容）长度未经验证，可能导致缓冲区溢出。切片中未见对源数据长度的检查或使用安全函数。 |
| 1335 | vim-9.1.0790 | qf_store_title | cpp/unbounded-write | 1934 | FP | TP | 代码使用strcpy复制未经验证的外部输入（title），且目标缓冲区大小仅比源字符串长度多2字节，若title长度被恶意控制或未正确终止，可能导致缓冲区溢出。切片中未见对title内容的任何验证或边界检查。 |
| 1334 | vim-9.1.0790 | mch_FullName | cpp/unbounded-write | 2819 | FP | TP | 代码在调用STRCAT（即strcat）前，仅检查了目标缓冲区buf的总长度（STRLEN(buf) + STRLEN(fname)）是否小于len，但未检查追加fname后是否会超出buf的原始容量。strcat操作依赖于buf以空... |
| 1336 | vim-9.1.0790 | reg_submatch | cpp/unbounded-write | 2723 | FP | TP | 切片代码显示，在`reg_submatch`函数中，`STRCPY`宏（即`strcpy`）被用于将`reg_getline_submatch`返回的未知长度字符串复制到固定大小的缓冲区`retval`中，而`retval`的大小`l... |
| 1337 | vim-9.1.0790 | reg_submatch | cpp/unbounded-write | 2732 | FP | TP | 切片代码中，`STRCPY`宏直接展开为不安全的`strcpy`，且目标缓冲区`retval`的大小`len`是根据匹配文本动态计算的，但`strcpy`的源字符串`s`来自`reg_getline_submatch`，其长度可能超过... |
| 1338 | vim-9.1.0790 | regtilde | cpp/unbounded-write | 1959 | FP | TP | 代码使用STRCPY（即strcpy）将postfix复制到tmpsub缓冲区，其目标缓冲区大小tmpsublen+1由alloc分配，但postfix长度postfixlen未经验证，可能超过分配的空间，导致缓冲区溢出。切片中未见对... |
| 1339 | vim-9.1.0790 | match_with_backref | cpp/unbounded-write | 1600 | FP | TP | 代码使用STRCPY（即strcpy）将长度未知的源字符串rex.line复制到固定大小的缓冲区reg_tofree中，且切片显示reg_tofree的大小仅基于STRLEN(rex.line) + 50分配，未对源字符串长度进行限制... |
| 1340 | vim-9.1.0790 | get_reg_contents | cpp/unbounded-write | 2668 | FP | TP | 代码使用STRCPY（即strcpy）将y_current->y_array[i]的内容复制到固定大小的缓冲区retval中，而retval的大小仅由len计算分配，未检查单个源字符串长度是否超过目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 1341 | vim-9.1.0790 | do_put | cpp/unbounded-write | 2094 | FP | TP | 切片代码中直接使用了未经验证长度的源字符串（y_array[i]）作为strcpy的目标，且目标缓冲区大小未明确检查，存在缓冲区溢出的风险。 |
| 1343 | vim-9.1.0790 | op_yank | cpp/unbounded-write | 1278 | FP | TP | 代码中直接使用STRCPY（即strcpy）宏，将两个字符串拼接，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未发现任何边界检查或安全防护措施。 |
| 1342 | vim-9.1.0790 | do_put | cpp/unbounded-write | 2095 | FP | TP | 切片代码中明确存在对 `STRCAT` 宏（即 `strcat`）的调用，且其目标缓冲区 `newp` 的大小由 `alloc` 分配，而源字符串 `ptr` 来自 `ml_get` 读取的行内容，长度未经验证。这可能导致缓冲区溢出，... |
| 1345 | vim-9.1.0790 | stuff_yank | cpp/unbounded-write | 452 | FP | TP | 代码使用STRCPY（即strcpy）将字符串从*pp复制到新分配的内存lp，目标缓冲区大小基于STRLEN(*pp) + STRLEN(p) + 1计算，但*pp是来自y_current->y_array的指针，其内容可能来自外部输... |
| 1346 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2755 | FP | TP | 代码使用strcat将用户输入（参数name）拼接到固定大小的缓冲区scriptname中，而scriptname的分配大小仅基于name的长度加上固定值14，未考虑已拷贝的'auto/'前缀和后续的'.vim'后缀，存在缓冲区溢出的风险。 |
| 1347 | vim-9.1.0790 | ExpandPackAddDir | cpp/unbounded-write | 1226 | FP | TP | sprintf 使用未经验证的用户输入 `pat` 作为格式化字符串的一部分，目标缓冲区 `s` 的大小为 `pat_len + 26`，但格式化字符串 `"pack/*/opt/%s*"` 的长度加上 `pat` 的长度可能超过该缓... |
| 1348 | vim-9.1.0790 | sign_jump | cpp/unbounded-write | 1324 | FP | TP | sprintf 使用未限制长度的缓冲区 buf->b_fname 作为输入，该缓冲区内容可能来自外部文件或环境变量，且目标缓冲区 cmd 的大小仅基于当前 b_fname 长度计算，无法防御 b_fname 被后续修改或包含格式化字符... |
| 1350 | vim-9.1.0790 | make_case_word | cpp/unbounded-write | 3140 | FP | TP | 代码直接使用不安全的strcpy宏复制字符串，未检查目标缓冲区大小，且切片中未显示对源字符串fword的长度有任何限制或验证，存在缓冲区溢出风险。 |
| 1349 | vim-9.1.0790 | dump_word | cpp/unbounded-write | 4187 | FP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或外部数据（如环境变量、文件读取内容），且切片中未显示对p的长度进行任何校验，存在缓冲区溢出风险。 |
| 1351 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2998 | FP | TP | 代码使用STRCPY宏（即strcpy）将repl_to复制到新分配的缓冲区p中，未检查目标缓冲区大小，而repl_to是全局变量，其长度可能超过目标缓冲区p的剩余空间，存在缓冲区溢出风险。 |
| 1352 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2999 | FP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p中，但p的大小为ml_get_curline_len() + addlen + 1，而拼接的源字符串长度未经验证，可能导致缓冲区溢出。 |
| 1354 | vim-9.1.0790 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）将参数lang直接复制到固定大小的数组sl.sl_lang中，但切片未显示对lang的长度有任何校验或限制。由于lang是函数参数，其来源可能不受控（如来自环境变量或外部输入），存在缓冲区溢出风险。 |
| 1353 | vim-9.1.0790 | count_common_word | cpp/unbounded-write | 1919 | FP | TP | 代码使用STRCPY（即strcpy）将字符串p复制到新分配的内存wc->wc_word中，而p的来源是用户输入参数word，其长度未在切片中显示有任何限制或验证。由于目标缓冲区大小基于STRLEN(p)+1动态分配，虽然避免了缓冲区... |
| 1355 | vim-9.1.0790 | spell_move_to | cpp/unbounded-write | 1420 | FP | TP | 代码使用STRCPY宏（即strcpy）将长度不确定的字符串`line`复制到固定大小的缓冲区`buf`中，而`buf`的大小仅根据`len + MAXWLEN + 2`分配，未限制源字符串长度，存在缓冲区溢出风险。 |
| 1358 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2371 | FP | TP | 代码使用STRCAT宏（即strcat）将items[1]拼接到指针p指向的缓冲区，而p指向的缓冲区大小由动态计算的长度分配，但未检查items[1]的长度是否会导致缓冲区溢出，存在潜在的缓冲区溢出风险。 |
| 1357 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2369 | FP | TP | 代码在循环中多次使用STRCAT向缓冲区p追加内容，而p的大小由getroom分配，其长度计算仅基于spin->si_info、items[0]和items[1]的当前长度，未考虑后续追加操作可能导致的缓冲区溢出。items来源于外部... |
| 1359 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2464 | FP | TP | 代码在行`STRCPY(p, items[1]);`处使用`strcpy`将`fgets`读取的字符串`items[1]`复制到缓冲区`p`中，而`p`的大小仅为`STRLEN(items[1]) + 2`，若`items[1]`长度... |
| 1362 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2746 | FP | TP | 代码在行号2746处使用`sprintf`将用户控制的字符串`items[4]`格式化到固定大小的缓冲区`buf`中，未检查长度，存在缓冲区溢出风险。 |
| 1361 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2644 | FP | TP | 代码使用STRCPY宏（即strcpy）将items[1]复制到缓冲区p，而p的大小为STRLEN(items[1]) + 2，但items[1]来源于从文件读取的未经验证的行，若其长度超过目标缓冲区大小则会导致缓冲区溢出。 |
| 1363 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2748 | FP | TP | 代码在行号2748处使用sprintf将items[4]的内容拼接到buf中，而items[4]来自外部文件读取的未经验证的行数据，可能导致缓冲区溢出，因为buf的大小为MAXLINELEN但输入长度未受限制。 |
| 1368 | vim-9.1.0790 | expand_tag_fname | cpp/unbounded-write | 4125 | FP | TP | 代码使用STRCPY（即strcpy）将tag_fname复制到固定大小的缓冲区retval中，未检查源字符串长度是否超过目标缓冲区大小MAXPATHL，存在缓冲区溢出风险。 |
| 1369 | vim-9.1.0790 | findtags_add_match | cpp/unbounded-write | 2623 | FP | TP | 代码中直接使用STRCPY（即strcpy）宏将来源未知的字符串（如st->help_lang）复制到固定大小的缓冲区中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1370 | vim-9.1.0790 | findtags_add_match | cpp/unbounded-write | 2702 | FP | TP | 切片代码中多次使用STRCPY（即strcpy）宏，将来源未知或长度未经验证的外部数据（如st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区，存在缓冲区溢出风险。 |
| 1371 | vim-9.1.0790 | show_one_termcode | cpp/unbounded-write | 7058 | FP | TP | 代码使用STRCPY（即strcpy）将get_special_key_name返回的字符串p复制到IObuff+5位置，但未检查p的长度是否超过IObuff剩余空间，存在缓冲区溢出风险。切片中未显示对p的长度或IObuff大小进行任... |
| 1372 | vim-9.1.0790 | current_tagblock | cpp/unbounded-write | 1386 | FP | TP | sprintf 使用未限制长度的字符串 p 作为格式化输入，而 p 来自 ml_get_cursor() 获取的缓冲区内容，其长度可能超过目标缓冲区 spat/epat 的分配大小（len + 39 或 len + 9），存在缓冲区溢... |
| 1373 | vim-9.1.0790 | uc_check_code | cpp/unbounded-write | 1778 | FP | TP | 代码在多个分支中直接使用STRCPY（即strcpy）将外部输入（如eap->arg）复制到固定大小的缓冲区buf中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1374 | vim-9.1.0790 | get_scriptlocal_funcname | cpp/unbounded-write | 4658 | FP | TP | 代码使用STRCAT宏（即strcat）将未经验证长度的字符串`p + off`拼接到固定大小的缓冲区`newname`中，而`newname`的大小仅根据`sid_buf`和`p + off`的长度之和分配，未预留字符串终止符空间，... |
| 1375 | vim-9.1.0790 | trans_function_name_ext | cpp/unbounded-write | 4571 | FP | TP | 代码中直接使用 STRCPY 宏（即 strcpy）将 sid_buf 内容复制到目标缓冲区，而 sid_buf 的大小为 20 字节，但复制源 sid_buf 的内容可能通过 vim_snprintf 格式化生成，其长度未在切片中显... |
| 1376 | vim-9.1.0790 | fname_trans_sid | cpp/unbounded-write | 2115 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入（name + llen）复制到固定大小的缓冲区（fname_buf），且仅通过长度检查（i + STRLEN(name + llen) < FLEN_FIXED）来防止溢出，但若检查失... |
| 1378 | vim-9.1.0790 | set_ufunc_name | cpp/unbounded-write | 663 | FP | TP | 代码使用不安全的strcpy函数，将外部传入的字符串name复制到固定大小的缓冲区fp->uf_name中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1377 | vim-9.1.0790 | fname_trans_sid | cpp/unbounded-write | 2127 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入（name + llen）复制到固定大小的缓冲区（fname_buf）或动态分配的缓冲区（fname），但未检查源字符串长度是否小于目标缓冲区大小。切片中显示目标缓冲区大小由FLEN_F... |
| 1380 | vim-9.1.0790 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的变量`name`复制到新分配的缓冲区`funcname`中，虽然分配大小为`STRLEN(name) + 3`，但`STRCPY(funcname, "g:")`和`STRCPY(fu... |
| 1382 | vim-9.1.0790 | find_exported | cpp/unbounded-write | 756 | FP | TP | 代码使用sprintf将外部可控的`script->sn_autoload_prefix`和`name`拼接到固定大小的缓冲区`funcname`中，而`funcname`的大小仅由`len`决定，`len`的计算可能不足以容纳拼接后... |
| 1381 | vim-9.1.0790 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | TP | 代码使用STRCPY（即strcpy）将变量`name`复制到新分配的内存`newsav->sav_key`中，而`name`是函数参数，其来源在切片中未显示任何验证或长度限制。目标缓冲区大小仅为`STRLEN(name) + 1`，... |
| 1384 | vim-9.1.0790 | xxdline | cpp/unbounded-write | 534 | FP | TP | 函数`xxdline`中的`strcpy(z, l)`调用将外部输入`l`复制到固定大小的缓冲区`z`（大小为`LLEN+1`），未检查`l`的长度，存在缓冲区溢出风险。 |
| 1385 | vim-9.1.0790 | ExpandBufnames | cpp/invalid-pointer-deref | 2937 | FP | TP | 切片代码显示，在`round == 1`且`!fuzzy`时，`*file`指针可能为NULL，但后续在`(*file)[count++] = p;`处直接进行数组索引写入，存在对NULL指针或未分配内存的越界写入风险。 |
| 1383 | vim-9.1.0790 | find_exported | cpp/unbounded-write | 763 | FP | TP | 代码使用`sprintf`将外部输入`name`和脚本ID`sid`写入固定大小的栈缓冲区`buffer`或动态分配的`funcname`，当`len`计算错误或输入过长时，可能导致缓冲区溢出。切片中未显示对`name`长度的有效限制... |
| 1386 | vim-9.1.0790 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | TP | 当 width 为 2 且 pos.col 等于 len-1 时，p[pos.col + 1] 会越界写入，因为 p 仅分配了 len 个元素。切片代码中缺少对 pos.col 和 len 关系的边界检查，存在缓冲区溢出风险。 |
| 1379 | vim-9.1.0790 | exec_instructions | cpp/unbounded-write | 3496 | FP | TP | 切片代码中明确存在对 STRCPY 宏的不安全调用，该宏展开为 strcpy，且目标缓冲区 'cmd' 的大小由运行时计算的 'len' 决定，而源字符串 'str' 来自用户可控的栈变量，长度可能超过目标缓冲区大小，导致缓冲区溢出。 |
| 1389 | musl-1.2.3 | load_library | cpp/unbounded-write | 1162 | FP | TP | 代码使用strcpy将pathname复制到p->name，而pathname可能来自环境变量env_path或用户输入，且切片中未显示对pathname长度的检查，存在缓冲区溢出风险。 |
| 1392 | musl-1.2.3 | <global> | cpp/unbounded-write | 10 | FP | TP | 代码从环境变量LOGNAME获取字符串，虽在strcpy前检查了长度，但getlogin()返回的指针可能为NULL，此时strlen(logname)会导致未定义行为，存在安全风险。 |
| 1398 | musl-1.2.2 | <global> | cpp/unbounded-write | 10 | FP | TP | 代码从环境变量LOGNAME获取字符串，虽在strcpy前检查了长度，但getlogin返回的指针可能因环境变量被后续修改而失效，导致strcpy时源字符串长度已超过目标缓冲区，存在潜在的缓冲区溢出风险。 |
| 1401 | musl-1.2.1 | load_library | cpp/unbounded-write | 1138 | FP | TP | strcpy 的目标缓冲区 p->name 指向 p->buf，其大小由 alloc_size 决定，而 alloc_size 基于 strlen(pathname) + 1 计算，但 pathname 可能来自环境变量 env_pa... |
| 1405 | musl-1.1.24 | getname | cpp/offset-use-before-range-check | 89 | FP | TP | 在循环条件中，变量 `i` 在访问 `(*p)[i]` 之后才进行 `i<TZNAME_MAX` 范围检查，存在越界读取的风险，可能导致缓冲区溢出。 |
| 1404 | musl-1.2.1 | <global> | cpp/unbounded-write | 10 | FP | TP | 代码从环境变量LOGNAME获取字符串，虽在strcpy前检查了长度，但若size参数为0，strlen(logname) >= size条件为真，函数将返回ERANGE，但strcpy仍可能被后续逻辑错误调用。然而，根据给定切片，g... |
| 1406 | musl-1.1.24 | getname | cpp/offset-use-before-range-check | 93 | FP | TP | 在循环条件中，变量 `i` 被用作数组 `(*p)` 的索引，但该索引的使用 (`(*p)[i]`) 发生在对 `i` 的范围检查 (`i<TZNAME_MAX`) 之前，这违反了先检查后使用的安全原则，存在潜在的越界读取风险。 |
| 1409 | musl-1.1.24 | load_library | cpp/unbounded-write | 1133 | FP | TP | 代码使用strcpy将pathname复制到固定大小的缓冲区p->name，而pathname可能来自环境变量env_path或用户输入，其长度未在复制前进行限制，存在缓冲区溢出风险。 |
| 1412 | musl-1.1.24 | <global> | cpp/unbounded-write | 10 | FP | TP | 代码从环境变量LOGNAME获取字符串，虽在strcpy前检查了长度，但若环境变量在getlogin和strlen调用之间被恶意修改，可能导致缓冲区溢出，存在TOCTOU风险。 |
| 1415 | musl-1.2.4 | load_library | cpp/unbounded-write | 1224 | FP | TP | strcpy 的目标缓冲区 p->name 的大小为 alloc_size，其长度基于 strlen(pathname) + 1 计算，而源字符串 pathname 可能来自环境变量 env_path 或 sys_path，其长度未在... |
| 1418 | musl-1.2.4 | <global> | cpp/unbounded-write | 10 | FP | TP | 代码中`strcpy`的目标缓冲区`name`大小由参数`size`限定，但源字符串`logname`来自环境变量`LOGNAME`，其内容用户可控且长度未经验证。虽然存在`strlen(logname) >= size`的长度检查，... |
| 1423 | redis-7.0.11 | xgroupCommand | Dereference of null pointer | 2700 | FP | TP | 在SETID子命令分支中，当s为NULL时，代码直接解引用s->last_id，存在空指针解引用风险。切片显示该分支未检查s是否为NULL，而s可能因键不存在且未设置MKSTREAM选项而为NULL。 |
| 1436 | redis-7.0.11 | xgroupCommand | Dereference of null pointer | 2696 | FP | TP | 在SETID子命令分支中，当参数为'$'时，代码直接使用`s->last_id`，但`s`可能为NULL（当key不存在且未设置MKSTREAM时），这将导致空指针解引用。切片代码显示`s`的赋值依赖于`lookupKeyWrite`... |
| 1458 | redis-7.4.2 | xgroupCommand | Dereference of null pointer | 2711 | FP | TP | 在SETID子命令分支中，当`s`为NULL时，代码直接解引用`s->last_id`（`id = s->last_id;`），存在空指针解引用风险。切片代码显示`s`可能为NULL，且该路径无前置检查。 |
| 1493 | redis-7.4.2 | checkMultiPartAof | Dereference of null pointer | 488 | FP | TP | 在调用 aofLoadManifestFromFile 后，未检查返回值 am 是否为 NULL 就直接解引用 am->incr_aof_list，存在空指针解引用风险。 |
| 1499 | redis-7.4.2 | auxHumanNodenameSetter | Dereference of null pointer | 233 | FP | TP | 在 `else if (sdslen(n->human_nodename) != 0)` 这一行，当 `n` 为 `NULL` 时，代码会解引用空指针 `n` 以访问其成员 `human_nodename`，这是一个明确的空指针解引用... |
| 1535 | redis-7.2.1 | checkMultiPartAof | Dereference of null pointer | 478 | FP | TP | 函数 `aofLoadManifestFromFile` 的返回值 `am` 在未进行空指针检查的情况下，直接在条件判断 `if (am->incr_aof_list)` 和 `listLength(am->incr_aof_list... |
| 1541 | redis-7.2.1 | auxHumanNodenameSetter | Dereference of null pointer | 267 | FP | TP | 在 `else if (sdslen(n->human_nodename) != 0)` 这一行，当 `n` 为 `NULL` 时，代码会直接解引用 `n` 以访问 `n->human_nodename`，这构成了对空指针的明确解引用... |
| 1545 | redis-7.2.5 | xgroupCommand | Dereference of null pointer | 2697 | FP | TP | 在SETID子命令分支中，代码直接解引用指针's'（id = s->last_id;），但's'可能为NULL（当查找的key不存在且未设置MKSTREAM时），这会导致空指针解引用。切片代码显示该路径可达且无防护。 |
| 1623 | redis-8.0.2 | checkMultiPartAof | Dereference of null pointer | 488 | FP | TP | 在调用 aofLoadManifestFromFile 后，未检查返回值 am 是否为 NULL 就直接解引用 am->incr_aof_list，存在空指针解引用风险。 |
| 1630 | redis-8.0.2 | auxHumanNodenameSetter | Dereference of null pointer | 234 | FP | TP | 在 `else if (sdslen(n->human_nodename) != 0)` 这一行，当 `n` 为 `NULL` 时，代码会解引用空指针 `n` 以访问其成员 `human_nodename`，这会导致未定义行为。 |
| 1635 | ffmpeg-7.1.1 | roq_dpcm_encode_frame | Dereference of null pointer | 180 | FP | TP | 在告警行`avpkt->pts = context->input_frames <= 7 ? context->first_pts : frame->pts;`中，当`context->input_frames > 7`时，三元运算符... |
| 1638 | ffmpeg-7.1.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | TP | 切片代码显示`dc_val`被初始化为NULL，随后在未经验证其非空的情况下，通过`*dc_val = dcdiff;`进行解引用赋值，这构成了明确的空指针解引用逻辑错误。 |
| 1647 | ffmpeg-7.1.1 | try_push_frame | Dereference of null pointer | 512 | FP | TP | 在代码行 `frame->pts = s->input_frames[0]->pts;` 中，存在对 `s->input_frames[0]` 指针的潜在空指针解引用。切片代码显示，当 `i=0` 时，`s->input_frames... |
| 1655 | ffmpeg-7.1.1 | try_push_frame | Dereference of null pointer | 241 | FP | TP | 切片代码显示，在访问 `inbuf[0]->pts` 之前，`inbuf` 数组被初始化为 `{ NULL }`，且 `ff_inlink_consume_samples` 的调用可能失败并保持 `inbuf[i]` 为 NULL。如... |
| 1667 | ffmpeg-7.1.1 | ebml_read_uint | Dereference of null pointer | 1002 | FP | TP | 代码在指针`num`可能为空的情况下，无条件地执行了`*num = 0;`，存在对空指针解引用的逻辑错误。切片中未显示对`num`进行空值检查，因此该告警是真实的。 |
| 1678 | ffmpeg-7.1.1 | locate_option | Dereference of null pointer | 495 | FP | TP | 在调用 `find_option` 后，未检查返回值 `po` 是否为 NULL 就直接访问 `po->name`，存在空指针解引用的逻辑错误风险。 |
| 1715 | ffmpeg-7.1.1 | dump_stream_group | Dereference of null pointer | 715 | FP | TP | 在内部循环中，变量 `st` 在未经验证是否为空的情况下被解引用（`st->index` 和 `st->codecpar`）。切片代码显示 `st` 来自 `stg->streams[k]`，但未检查 `stg` 或 `st` 是否为... |
| 1728 | ffmpeg-7.0.1 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | TP | 在告警行`avpkt->pts = context->input_frames <= 7 ? context->first_pts : frame->pts;`中，当`frame`参数为NULL时，三元运算符可能选择`frame->p... |
| 1731 | ffmpeg-7.0.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | TP | 代码中`dc_val`被初始化为NULL，随后在未检查其是否被`ff_vc1_pred_dc`函数有效赋值的情况下，直接进行解引用赋值`*dc_val = dcdiff;`，存在解引用空指针的风险。 |
| 1741 | ffmpeg-7.0.1 | try_push_frame | Dereference of null pointer | 511 | FP | TP | 在代码行 `frame->pts = s->input_frames[0]->pts;` 中，直接解引用了 `s->input_frames[0]`。根据切片代码逻辑，当 `ctx->nb_inputs > 0` 且 `s->inpu... |
| 1750 | ffmpeg-7.0.1 | try_push_frame | Dereference of null pointer | 241 | FP | TP | 切片代码显示，`inbuf`数组初始化为NULL，在循环中可能未成功为`inbuf[0]`赋值（例如`ff_inlink_consume_samples`返回0），随后直接解引用`inbuf[0]->pts`，存在解引用空指针的逻辑错... |
| 1763 | ffmpeg-7.0.1 | ebml_read_uint | Dereference of null pointer | 995 | FP | TP | 在函数开头，当 `size == 0` 时，代码对指针 `num` 进行了赋值 `*num = default_value;`，但随后立即无条件地执行 `*num = 0;`，这导致之前的赋值被覆盖，属于逻辑错误。指针 `num` 本... |
| 1766 | ffmpeg-7.0.1 | ost_add | Dereference of null pointer | 1428 | FP | TP | 在代码行 `ms->stream_duration = ist->st->duration;` 中，直接解引用了指针 `ist`，但根据切片代码中的条件 `if (ost->ist && ost->ist->st->duration ... |
| 1776 | ffmpeg-7.0.1 | locate_option | Dereference of null pointer | 486 | FP | TP | 在调用 `find_option` 后，未检查返回值 `po` 是否为 NULL 就直接访问 `po->name`，存在空指针解引用的逻辑错误。 |
| 1807 | ffmpeg-7.0.1 | dump_stream_group | Dereference of null pointer | 678 | FP | TP | 在内部循环中，变量 `st` 在未经验证是否为空的情况下被解引用（`st->index` 和 `st->codecpar`）。切片代码显示 `st` 未在循环前定义或初始化，直接使用可能导致空指针解引用。 |
| 1820 | ffmpeg-6.1.1 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | TP | 在告警行 `avpkt->pts = context->input_frames <= 7 ? context->first_pts : frame->pts;` 中，当 `frame` 为 NULL 且 `context->inpu... |
| 1834 | ffmpeg-6.1.1 | try_push_frame | Dereference of null pointer | 538 | FP | TP | 在代码行 `frame->pts = s->input_frames[0]->pts;` 中，直接解引用了 `s->input_frames[0]`。根据切片代码，当 `nb_samples` 为0时，函数会跳转到 `eof` 标签，... |
| 1840 | ffmpeg-6.1.1 | try_push_frame | Dereference of null pointer | 244 | FP | TP | 切片代码显示，`inbuf[0]` 在循环中被赋值，但若 `ctx->nb_inputs` 为0，则 `inbuf[0]` 保持初始值 NULL，随后在 `outbuf->pts = inbuf[0]->pts;` 处被解引用，存在空... |
| 1842 | ffmpeg-6.1.1 | hls_append_segment | Dereference of null pointer | 1173 | FP | TP | 在条件分支 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 中，`en` 可能为 NULL（来自 `en = vs->segm... |
| 1845 | ffmpeg-6.1.1 | kalman_smoothen | Dereference of null pointer | 584 | FP | TP | 在循环中，`best_hist_ptr` 可能未被赋值（如果 `optimal_gain <= 0` 始终为真），随后在 `dot = avpriv_scalarproduct_float_c(best_hist_ptr, best_... |
| 1852 | ffmpeg-6.1.1 | ebml_read_uint | Dereference of null pointer | 994 | FP | TP | 在函数入口处，指针 `num` 被直接解引用赋值（`*num = 0;`），但该指针参数可能为 NULL，且切片代码中未显示任何对 `num` 是否为 NULL 的检查，存在解引用空指针的逻辑错误风险。 |
| 1865 | ffmpeg-6.1.1 | locate_option | Dereference of null pointer | 424 | FP | TP | 在调用 `find_option` 后，代码直接解引用其返回的指针 `po`（如 `if (!po->name ...)`），而未检查 `po` 是否为 NULL。`find_option` 函数在遍历完选项表后，可能返回一个 `na... |
| 1897 | ffmpeg-6.1.1 | ff_inlink_evaluate_timeline_at_frame | Dereference of null pointer | 1485 | FP | TP | 函数参数 `frame` 被直接解引用以获取 `pts`，但调用方可能传入空指针。切片代码中未对 `frame` 进行空指针检查，存在解引用空指针的逻辑错误风险。 |
| 1912 | ffmpeg-7.1 | roq_dpcm_encode_frame | Dereference of null pointer | 180 | FP | TP | 在告警行 `avpkt->pts = context->input_frames <= 7 ? context->first_pts : frame->pts;` 中，当 `context->input_frames > 7` 时，三... |
| 1915 | ffmpeg-7.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | TP | 切片代码显示`dc_val`被初始化为NULL，随后在未进行空指针检查的情况下，直接通过`*dc_val = dcdiff;`进行解引用赋值，存在明确的空指针解引用风险。 |
| 1924 | ffmpeg-7.1 | try_push_frame | Dereference of null pointer | 512 | FP | TP | 在代码行 `frame->pts = s->input_frames[0]->pts;` 中，直接解引用了 `s->input_frames[0]`。根据切片代码，当 `ctx->nb_inputs` 大于0时，`s->input_f... |
| 1932 | ffmpeg-7.1 | try_push_frame | Dereference of null pointer | 241 | FP | TP | 代码在访问 `inbuf[0]->pts` 前未检查 `inbuf[0]` 是否为 NULL。`inbuf` 数组初始化为 NULL，且 `ff_inlink_consume_samples` 可能返回 NULL 指针，直接解引用会导... |
| 1935 | ffmpeg-7.1 | dump_argument | Dereference of null pointer | 516 | FP | TP | 函数`dump_argument`的参数`a`可能为NULL，而代码在循环条件`for (p = a; *p; p++)`中直接解引用`a`（即`*p`），这会导致空指针解引用。切片代码中未显示对`a`进行NULL检查，存在明显的逻辑... |
| 1942 | ffmpeg-7.1 | output_packet | Dereference of null pointer | 1103 | FP | TP | 在代码行`timestamp_packet = stream->premux_packet;`之后，直接解引用了`timestamp_packet->unwritten_size`，而`stream->premux_packet`可能... |
| 1944 | ffmpeg-7.1 | ebml_read_uint | Dereference of null pointer | 1002 | FP | TP | 在函数入口处，指针 `num` 被直接解引用赋值（`*num = 0;`），但该指针参数可能为 NULL，且切片代码中未包含任何对 `num` 是否为 NULL 的检查，存在空指针解引用风险。 |
| 1956 | ffmpeg-7.1 | locate_option | Dereference of null pointer | 495 | FP | TP | 在调用 `find_option` 后，未检查返回值 `po` 是否为 NULL 就直接访问 `po->name`，存在空指针解引用的逻辑错误。切片代码中未显示 `find_option` 能保证返回非空指针，且后续条件判断 `if ... |
| 1959 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 333 | FP | TP | 当 `s->do_video` 为真但 `outlink` 为 NULL 时，代码在 `av_rescale_q` 调用中会解引用空指针 `outlink->time_base`。切片代码显示 `outlink` 在函数开头被有条件地... |
| 1964 | ffmpeg-7.1 | activate | Dereference of null pointer | 186 | FP | TP | 在`s->eof`为真且`s->stop_mode == MODE_CLONE`的分支中，`frame`由`av_frame_clone(s->cache_stop)`赋值，若`s->cache_stop`为NULL，则`av_fra... |
| 1970 | ffmpeg-7.1 | ost_add | Dereference of null pointer | 1541 | FP | TP | 在切片代码的第1541行（ms->stream_duration = ist->st->duration;），存在对指针`ist`的成员`st`的访问。根据切片上下文，`ist`可能为NULL（例如当`if (ist ｜｜ ofilt... |
| 1993 | ffmpeg-7.1 | dump_stream_group | Dereference of null pointer | 715 | FP | TP | 在内部循环中，变量 `st` 在解引用前（`st->index` 和 `st->codecpar`）未被初始化或赋值，切片代码中未显示其来源，这很可能导致空指针解引用。 |
| 2006 | ffmpeg-6.0 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | TP | 在告警行`avpkt->pts = context->input_frames <= 7 ? context->first_pts : frame->pts;`中，当`frame`为NULL且`context->input_frame... |
| 2025 | ffmpeg-6.0 | try_push_frame | Dereference of null pointer | 243 | FP | TP | 切片代码显示，`inbuf`数组初始化为NULL，在循环中可能未成功为`inbuf[0]`赋值，随后直接解引用`inbuf[0]->pts`，存在解引用空指针的风险。 |
| 2027 | ffmpeg-6.0 | hls_append_segment | Dereference of null pointer | 1180 | FP | TP | 在条件分支 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 中，`en` 可能为 NULL（来自 `en = vs->segm... |
| 2036 | ffmpeg-6.0 | ebml_read_uint | Dereference of null pointer | 980 | FP | TP | 在指针`num`可能为NULL的情况下，代码在第980行直接对其解引用（`*num = 0;`），存在空指针解引用风险。切片中未显示对`num`的NULL检查，且函数逻辑要求`num`必须为非空指针才能正确赋值。 |
| 2035 | ffmpeg-6.0 | output_packet | Dereference of null pointer | 1092 | FP | TP | 在告警行`timestamp_packet->unwritten_size`处，`timestamp_packet`被赋值为`stream->premux_packet`。切片代码显示，`stream->premux_packet`可... |
| 2040 | ffmpeg-6.0 | init_output_stream_encode | Dereference of null pointer | 3153 | FP | TP | 切片代码显示，在访问 `ost->ist->par->width` 和 `ost->ist->par->height` 之前，未对指针 `ost->ist` 或 `ost->ist->par` 进行空值检查。若这些指针为空，将导致空指... |
| 2044 | ffmpeg-6.0 | locate_option | Dereference of null pointer | 424 | FP | TP | 在调用 `find_option` 后，代码直接解引用其返回值 `po`（如 `!po->name`），而未检查 `po` 是否为 NULL。`find_option` 函数在遍历完选项数组后，可能返回一个 `name` 为 NULL... |
| 2069 | ffmpeg-6.0 | ff_inlink_evaluate_timeline_at_frame | Dereference of null pointer | 1466 | FP | TP | 函数参数 `link` 在切片代码中未经空指针检查即被解引用（`link->time_base`），若传入的 `link` 为 NULL，将导致空指针解引用。切片中未见任何防护逻辑。 |
| 2078 | git-2.46.0 | sync_submodule | Dereference of null pointer | 1273 | FP | TP | 代码在调用 `submodule_from_path` 后未检查返回值 `sub` 是否为 NULL，便直接解引用 `sub->name`，存在空指针解引用风险。 |
| 2083 | git-2.46.0 | rstrip_ref_components | Dereference of null pointer | 2117 | FP | TP | 在for循环条件 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 不为空字符且不等于 '/' 时，会执行 `*p++`，这等价于 `*p; p++`。由于 `p` 是 `const char*` 指针，`*... |
| 2092 | git-2.46.0 | lstrip_ref_components | Dereference of null pointer | 2079 | FP | TP | 在for循环条件 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 不为空字符且不等于 '/' 时，会执行 `*p++` 对指针 `p` 进行解引用。然而，`p` 被初始化为 `refname`，而 `ref... |
| 2106 | git-2.46.0 | split_graph_merge_strategy | Dereference of null pointer | 2269 | FP | TP | 在条件 `ctx->num_commit_graphs_after == 2` 成立时，变量 `g` 可能为 NULL（例如，当 `flags` 为 `COMMIT_GRAPH_SPLIT_MERGE_PROHIBITED` 或 `C... |
| 2111 | git-2.46.0 | merge_ref_iterator_advance | Dereference of null pointer | 202 | FP | TP | 在while循环中，当`selection`包含`ITER_YIELD_CURRENT`时，代码直接解引用`*iter->current`以访问其成员（如`refname`）。然而，切片代码显示`iter->current`可能为NU... |
| 2114 | git-2.46.0 | cmp_local_packs | Dereference of null pointer | 481 | FP | TP | 函数入口处`pl`被赋值为全局变量`local_packs`，而`local_packs`初始化为NULL。在未检查`pl`是否为NULL的情况下，代码直接访问`pl->next`，存在解引用空指针的风险。 |
| 2124 | git-2.46.0 | prepare_attr_stack | Dereference of null pointer | 1021 | FP | TP | 在 while ((*stack)->origin) 循环中，*stack 可能为 NULL，因为前一行 *stack = info->prev 可能将 *stack 设置为 NULL（如果 info->prev 为 NULL），导致... |
| 2130 | git-2.49.0 | sync_submodule | Dereference of null pointer | 1288 | FP | TP | 切片代码显示 `sub` 变量由 `submodule_from_path` 返回，该函数可能返回 NULL，但后续代码 `sub->name` 直接解引用 `sub` 指针，未进行 NULL 检查，存在空指针解引用风险。 |
| 2136 | git-2.49.0 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | TP | 在for循环条件 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 为 '\0' 时，表达式 `*p++` 会解引用空指针 `p`，因为此时 `p` 指向字符串结尾的空字符，解引用它是未定义行为。 |
| 2144 | git-2.49.0 | clar__fail | Dereference of null pointer | 698 | FP | TP | 切片代码中直接对指针 `error` 进行解引用赋值，但未显示 `error` 被初始化或进行空值检查，存在解引用空指针的逻辑错误风险。 |
| 2146 | git-2.49.0 | add_lines_to_move_detection | Dereference of null pointer | 1060 | FP | TP | 切片代码显示，在`entry_list[l->id].add = entry;`和`entry_list[l->id].del = entry;`处，`entry_list`可能为NULL，因为`ALLOC_GROW_BY`仅在`s`... |
| 2148 | git-2.49.0 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | TP | 在for循环条件 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 不为空字符且不等于 '/' 时，会执行 `*p++` 对指针 `p` 进行解引用。然而，在循环初始化和迭代中，`p` 被赋值为 `refna... |
| 2158 | git-2.49.0 | merge_ref_iterator_advance | Dereference of null pointer | 205 | FP | TP | 在`iter->current`为NULL的情况下，代码会进入`while (1)`循环，并在`selection & ITER_YIELD_CURRENT`条件成立时，直接解引用`*iter->current`（例如`(*iter-... |
| 2168 | git-2.49.0 | split_graph_merge_strategy | Dereference of null pointer | 2281 | FP | TP | 在条件 `ctx->num_commit_graphs_after == 2` 成立时，变量 `g` 可能为 NULL（例如当 `flags` 为 `COMMIT_GRAPH_SPLIT_MERGE_PROHIBITED` 或 `CO... |
| 2192 | git-2.49.0 | t_table_refs_for | Dereference of null pointer | 577 | FP | TP | 代码中 `want_names` 数组指针在未初始化的状态下被直接使用（`want_names[want_names_len++] = ...`），随后传递给 `free_names` 函数，这会导致对空指针的间接引用，构成逻辑错误。 |
| 2193 | git-2.49.0 | prepare_attr_stack | Dereference of null pointer | 986 | FP | TP | 在while循环条件`(*stack)->origin`中直接解引用了指针`*stack`，但循环前的赋值`*stack = info->prev;`可能导致`*stack`为NULL，从而引发空指针解引用。切片代码中未见对`*sta... |
| 2198 | git-2.44.0 | sync_submodule | Dereference of null pointer | 1267 | FP | TP | 代码在调用 `submodule_from_path` 后未检查返回值 `sub` 是否为 NULL，便直接解引用 `sub->name`，存在空指针解引用风险。 |
| 2201 | git-2.44.0 | diffcore_merge_broken | Dereference of null pointer | 292 | FP | TP | 在内部循环中，指针 `pp` 从 `q->queue[j]` 获取，但 `q->queue[j]` 可能为 NULL（因为前面的代码 `q->queue[j] = NULL;`），随后直接解引用 `pp->broken_pair`，存... |
| 2203 | git-2.44.0 | rstrip_ref_components | Dereference of null pointer | 2113 | FP | TP | 在for循环条件 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 不为空字符且不等于 '/' 时，会执行 `*p++`，但此时 `p` 可能为 NULL（例如当 `refname` 为 NULL 时），导致... |
| 2210 | git-2.44.0 | add_lines_to_move_detection | Dereference of null pointer | 1034 | FP | TP | 在 `entry_list[l->id].add = entry;` 和 `entry_list[l->id].del = entry;` 处，`l->id` 可能等于 `entry_list` 的当前分配大小（`id`），因为 `A... |
| 2212 | git-2.44.0 | lstrip_ref_components | Dereference of null pointer | 2075 | FP | TP | 在for循环的条件表达式 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 不为 '/' 时，会执行 `*p++` 对指针 `p` 进行解引用。然而，如果 `p` 是空指针（例如 `refname` 为 NU... |
| 2225 | git-2.44.0 | read_cached_dir | Dereference of null pointer | 2515 | FP | TP | 切片代码显示，在while循环条件中直接解引用`cdir->untracked`指针，但未检查其是否为NULL。若`cdir->untracked`为NULL，将导致空指针解引用。 |
| 2224 | git-2.44.0 | split_graph_merge_strategy | Dereference of null pointer | 2239 | FP | TP | 在条件`ctx->num_commit_graphs_after == 2`成立时，变量`g`可能为NULL（例如当`flags`为`COMMIT_GRAPH_SPLIT_MERGE_PROHIBITED`或`COMMIT_GRAPH... |
| 2231 | git-2.44.0 | merge_ref_iterator_advance | Dereference of null pointer | 161 | FP | TP | 在 `iter->current` 为 NULL 的情况下，代码会进入 `if (!iter->current)` 分支，但随后在 while 循环中，`iter->select` 函数可能返回 `ITER_YIELD_CURRENT... |
| 2245 | git-2.44.0 | prepare_attr_stack | Dereference of null pointer | 1019 | FP | TP | 在while循环条件`(*stack)->origin`中直接解引用指针`*stack`，但前序代码`*stack = info->prev;`可能使`*stack`为NULL，导致空指针解引用。切片中未见对`*stack`进行NUL... |
| 2252 | git-2.50.1 | sync_submodule | Dereference of null pointer | 1288 | FP | TP | 代码在调用 `submodule_from_path` 后未检查返回值 `sub` 是否为 NULL，便直接解引用 `sub->name`，存在空指针解引用风险。 |
| 2258 | git-2.50.1 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | TP | 在for循环的条件表达式 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 不为空字符且不等于 '/' 时，会执行 `*p++`。此时 `p` 是一个指向 `refname` 的指针，解引用 `*p` 是安全... |
| 2266 | git-2.50.1 | clar__fail | Dereference of null pointer | 698 | FP | TP | 切片代码中直接对指针`error`进行解引用赋值，但未显示`error`的初始化或空值检查，存在解引用空指针的风险。 |
| 2270 | git-2.50.1 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | TP | 在for循环条件 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 不为空字符且不等于 '/' 时，会执行 `*p++`，但此时 `p` 是一个 `const char*` 指针，解引用 `*p` 是合法的，... |
| 2280 | git-2.50.1 | merge_ref_iterator_advance | Dereference of null pointer | 214 | FP | TP | 在 `iter->current` 为 NULL 的分支中，代码会进入 `while (1)` 循环并调用 `iter->select`。如果 `select` 函数返回 `ITER_YIELD_CURRENT`，代码将无条件解引用 ... |
| 2289 | git-2.50.1 | split_graph_merge_strategy | Dereference of null pointer | 2284 | FP | TP | 在条件 `ctx->num_commit_graphs_after == 2` 分支内，变量 `g` 可能为 NULL（例如当 `flags` 为 `COMMIT_GRAPH_SPLIT_MERGE_PROHIBITED` 或 `CO... |
| 2314 | git-2.50.1 | prepare_attr_stack | Dereference of null pointer | 986 | FP | TP | 在 while ((*stack)->origin) 循环中，*stack 可能为 NULL，因为前一行 *stack = info->prev 可能将 *stack 设置为 NULL（如果 info->prev 为 NULL），导致... |
| 2319 | git-2.47.1 | sync_submodule | Dereference of null pointer | 1283 | FP | TP | 代码在调用 `submodule_from_path` 后未检查返回值 `sub` 是否为 NULL，便直接解引用 `sub->name`，存在空指针解引用风险。 |
| 2324 | git-2.47.1 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | TP | 在for循环的条件表达式 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 不为空字符且不等于 '/' 时，会执行 `*p++`。此时 `p` 是一个指向 `refname` 的指针，解引用 `*p` 是安全... |
| 2333 | git-2.47.1 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | TP | 在for循环的条件表达式 `p[i] == '/' ? i++ : *p++` 中，当 `p[i]` 不为 '/' 时，会执行 `*p++` 对指针 `p` 进行解引用。然而，如果 `p` 是空指针（即 `refname` 为 NUL... |
| 2331 | git-2.47.1 | add_lines_to_move_detection | Dereference of null pointer | 1059 | FP | TP | 切片代码显示，在`entry_list[l->id].add = entry;`和`entry_list[l->id].del = entry;`处，通过`l->id`索引访问`entry_list`数组。`l->id`的值在循环中可... |
| 2341 | git-2.47.1 | merge_ref_iterator_advance | Dereference of null pointer | 203 | FP | TP | 在`iter->current`为NULL的情况下，代码会进入`if (!iter->current)`分支，但后续的`while`循环中，`iter->select`的调用结果可能导致`selection & ITER_YIELD_... |
| 2348 | git-2.47.1 | split_graph_merge_strategy | Dereference of null pointer | 2269 | FP | TP | 在条件`ctx->num_commit_graphs_after == 2`成立时，代码直接使用指针`g`调用`get_commit_graph_filename(g->odb)`，但切片显示`g`可能在前面的while循环中被赋值为... |
| 2356 | git-2.47.1 | cmp_local_packs | Dereference of null pointer | 482 | FP | TP | 函数入口处`pl`被赋值为全局变量`local_packs`，而`local_packs`初始化为NULL。在未检查`pl`是否为NULL的情况下，直接解引用`pl->next`，存在空指针解引用风险。 |
| 2366 | git-2.47.1 | prepare_attr_stack | Dereference of null pointer | 1021 | FP | TP | 在while循环条件`(*stack)->origin`中直接解引用指针`*stack`，但前一行`*stack = info->prev;`可能将`*stack`赋值为NULL，导致空指针解引用。切片代码中未发现对`*stack`进... |
| 2370 | musl-1.2.1 | load_direct_deps | Dereference of null pointer | 1194 | FP | TP | 在切片代码中，`p->deps` 可能为 NULL（当 `p==head && cnt<2` 时，`p->deps` 被赋值为 `builtin_deps`，但 `builtin_deps` 的值未知），随后在未检查其是否为 NULL... |
| 2376 | musl-1.2.1 | load_direct_deps | Dereference of null pointer | 1206 | FP | TP | 切片代码显示，在未检查指针 `p->deps` 是否为 NULL 的情况下，直接对其进行了数组下标访问和赋值操作（`p->deps[cnt] = 0;`），这构成了对潜在空指针的解引用，是一个明确的逻辑错误。 |
| 2380 | musl-1.2.1 | tre_copy_ast | Dereference of null pointer | 1741 | FP | TP | 在代码行 `tag_directions[max] = TRE_TAG_MAXIMIZE;` 中，数组索引 `max` 的值可能为 -1（来自前一个分支 `max = pos = -1;`），这会导致对 `tag_directions... |
| 2389 | musl-1.2.4 | load_direct_deps | Dereference of null pointer | 1280 | FP | TP | 在切片代码中，`p->deps` 可能为 null 指针。在警告行 `p->deps[cnt++] = q;` 之前，`p->deps` 被赋值为 `builtin_deps` 或某个条件表达式的结果，但随后立即检查 `if (!p-... |
| 2397 | musl-1.2.4 | load_direct_deps | Dereference of null pointer | 1292 | FP | TP | 切片代码显示，在未检查 `p->deps` 是否为有效指针的情况下，直接将其作为数组进行下标访问和赋值 (`p->deps[cnt] = 0;`)，这构成了对潜在空指针的解引用，是一个明确的逻辑错误。 |
| 2402 | musl-1.2.4 | tre_copy_ast | Dereference of null pointer | 1741 | FP | TP | 在代码行 `tag_directions[max] = TRE_TAG_MAXIMIZE;` 中，数组索引 `max` 的值可能为 -1（来自前一个条件分支 `max = pos = -1;`），这会导致对 `tag_directio... |
| 2411 | musl-1.1.24 | load_direct_deps | Dereference of null pointer | 1189 | FP | TP | 在切片代码中，`p->deps` 可能为 NULL（当 `p==head && cnt<2` 时，`p->deps` 被赋值为 `builtin_deps`，但 `builtin_deps` 的值未知，且后续未检查其是否为 NULL ... |
| 2417 | musl-1.1.24 | load_direct_deps | Dereference of null pointer | 1201 | FP | TP | 切片代码显示，在未检查指针 `p->deps` 是否为 `NULL` 的情况下，直接将其作为数组进行下标访问 `p->deps[cnt] = 0;`，这构成了对可能为空的指针的解引用，是一个明确的逻辑错误。 |
| 2421 | musl-1.1.24 | tre_copy_ast | Dereference of null pointer | 1741 | FP | TP | 在代码行 `tag_directions[max] = TRE_TAG_MAXIMIZE;` 中，数组索引 `max` 的值可能为 -1（来自前一个分支 `max = pos = -1;`），这会导致对 `tag_directions... |
| 2430 | musl-1.2.3 | load_direct_deps | Dereference of null pointer | 1218 | FP | TP | 在警告所在行 `p->deps[cnt++] = q;` 之前，存在条件分支 `if (!p->deps) { error(...); longjmp(...); }`，该分支在 `p->deps` 为空时会跳转退出函数。然而，警告行... |
| 2436 | musl-1.2.3 | load_direct_deps | Dereference of null pointer | 1230 | FP | TP | 切片代码显示，在未检查指针 `p->deps` 是否为 `NULL` 的情况下，直接将其作为数组进行下标访问（`p->deps[cnt] = 0;`），这构成了对潜在空指针的解引用，是一个明确的逻辑错误。 |
| 2440 | musl-1.2.3 | tre_copy_ast | Dereference of null pointer | 1741 | FP | TP | 在代码行 `tag_directions[max] = TRE_TAG_MAXIMIZE;` 中，数组索引 `max` 的值可能为 -1（来自前一个条件分支 `max = pos = -1;`），这会导致对数组 `tag_direct... |
| 2449 | musl-1.2.2 | load_direct_deps | Dereference of null pointer | 1217 | FP | TP | 切片代码显示，在警告行`p->deps[cnt++] = q;`之前，存在条件分支`if (!p->deps) { error(...); ... }`，若`p->deps`为NULL，程序会提前报错并退出。然而，警告行位于该条件检查... |
| 2455 | musl-1.2.2 | load_direct_deps | Dereference of null pointer | 1229 | FP | TP | 切片代码显示，在未检查指针 `p->deps` 是否为 `NULL` 的情况下，直接对其进行了数组下标访问 `p->deps[cnt] = 0;`，这构成了对空指针的解引用，是一个明确的逻辑错误。 |
| 2473 | tmux-3.3 | spawn_window | Dereference of null pointer | 180 | FP | TP | 在切片代码中，当条件 `(~sc->flags & SPAWN_RESPAWN)` 成立时，变量 `w` 被赋值为 `NULL`，随后在 `free(w->name);` 处直接解引用了 `w`，这会导致空指针解引用。 |
| 2472 | tmux-3.3 | grid_reflow_join | Dereference of null pointer | 1212 | FP | TP | 在切片代码中，变量 `from` 在循环外被初始化为 NULL，在循环内可能被赋值。但在第1212行 `left = from->cellused - want;` 处，如果循环从未执行（即 `lines == 0` 时提前返回），或... |
| 2483 | tmux-3.2 | grid_reflow_join | Dereference of null pointer | 1182 | FP | TP | 在切片代码中，变量 `from` 在循环外被初始化为 NULL，但在循环内可能未被赋值（例如当 `gd->linedata[line].cellused == 0` 且 `wrapped` 为假时，循环会提前退出）。随后在 `left... |
| 2490 | tmux-3.1 | mode_tree_build | Dereference of null pointer | 407 | FP | TP | 在`tag == UINT64_MAX`的分支中，代码直接访问`mtd->line_list[mtd->current].item->tag`，但此时`mtd->line_list`可能为NULL（如函数开头检查所示），这将导致空指针... |
| 2492 | tmux-3.1 | cmdq_get_command | Dereference of null pointer | 248 | FP | TP | 在首次循环迭代时，若cmd->group != group条件不成立，shared将保持为NULL，随后在'shared->references++'处被解引用，导致空指针解引用。 |
| 2496 | tmux-3.0 | grid_reflow_join | Dereference of null pointer | 1117 | FP | TP | 在循环中，变量`line`在未初始化的情况下被用于数组索引`gd->linedata[line]`，这可能导致空指针解引用或访问越界，构成逻辑错误。 |
| 2497 | tmux-3.0 | mode_tree_build | Dereference of null pointer | 407 | FP | TP | 在`tag == UINT64_MAX`的分支中，代码直接解引用`mtd->line_list[mtd->current].item->tag`，但此时`mtd->line_list`可能为NULL（根据第4行的条件判断），这将导致空... |
| 2499 | tmux-3.0 | cmdq_get_command | Dereference of null pointer | 233 | FP | TP | 在TAILQ_FOREACH循环的第一次迭代中，如果cmd->group != group条件不成立，shared将保持为NULL，随后在`shared->references++`处被解引用，导致空指针解引用。 |
| 2505 | tmux-3.4 | grid_reflow_join | Dereference of null pointer | 1286 | FP | TP | 在切片代码中，变量`from`在循环外被初始化为NULL，在循环内可能被赋值。但在第1286行（`left = from->cellused - want;`）使用`from`之前，存在一条代码路径（当`lines == 0`时直接`... |
| 2506 | tmux-3.4 | spawn_window | Dereference of null pointer | 181 | FP | TP | 在切片代码中，当 `(~sc->flags & SPAWN_RESPAWN)` 条件成立时，`w` 被赋值为 `NULL`，随后在相同条件下执行 `free(w->name)`，这导致了对空指针 `w` 的解引用，构成逻辑错误。 |

### 5.5 Unknown：算法=TP，LLM=Unknown（共 12 条）

> 算法判定为 TP，LLM 无法判定。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 410 | git-2.46.0 | <global> | cpp/overflow-buffer | 37 | TP | Unknown | 切片代码仅包含空函数定义，完全缺失与告警相关的数组访问操作、变量定义及数据流信息，无法判断是否存在负索引访问问题。 |
| 411 | git-2.46.0 | <global> | cpp/overflow-buffer | 38 | TP | Unknown | 切片代码仅包含空函数定义，未提供任何关于数组访问或相关变量赋值的上下文，无法判断是否存在负索引访问或评估其安全性。 |
| 412 | git-2.46.0 | <global> | cpp/overflow-buffer | 39 | TP | Unknown | 切片代码仅包含空函数定义，完全缺失与告警相关的数组索引操作、变量定义及数据流信息，无法判断是否存在负索引访问问题。 |
| 690 | vim-9.1.1591 | is_duplicate_variable | cpp/inconsistent-null-check | 1044 | TP | Unknown | 切片代码仅包含函数签名和空函数体，缺少对 `vim_strnsave` 函数调用的任何上下文，无法判断其返回值是否被检查或使用，因此无法评估告警的有效性。 |
| 704 | vim-9.1.1591 | buf_write | cpp/unbounded-write | 2568 | TP | Unknown | 切片代码中未包含触发告警的strcat调用位置，无法确认具体是哪一行代码存在缓冲区溢出风险。告警信息指向的read函数输入来源在切片中不可见，无法判断数据流是否受控。 |
| 1426 | redis-7.0.11 | rb_gen | Dereference of null pointer | 273 | TP | Unknown | 切片代码仅为宏或函数声明，未包含任何实际执行逻辑或数据流，无法判断是否存在空指针解引用。 |
| 1431 | redis-7.0.11 | <global> | Dereference of null pointer | 307 | TP | Unknown | 提供的切片代码仅为函数名片段，完全缺失任何变量定义、赋值或使用上下文，无法判断是否存在空指针解引用。 |
| 1434 | redis-7.0.11 | <global> | Dereference of null pointer | 288 | TP | Unknown | 提供的切片代码仅为字符串 'prof_gctx_comp)\n'，完全缺失任何程序逻辑、变量定义或数据流信息，无法判断是否存在空指针解引用问题。 |
| 1598 | redis-8.0.2 | rb_gen | Dereference of null pointer | 88 | TP | Unknown | 切片代码仅包含宏调用，未展示任何指针变量的定义、赋值或解引用操作，无法判断是否存在空指针解引用。 |
| 1602 | redis-8.0.2 | <global> | Dereference of null pointer | 122 | TP | Unknown | 提供的切片代码仅为字符串 'prof_tdata_comp)\n'，完全缺失任何与空指针解引用相关的变量定义、赋值或使用上下文，无法判断是否存在空指针解引用问题。 |
| 1606 | redis-8.0.2 | <global> | Dereference of null pointer | 103 | TP | Unknown | 提供的切片代码仅为字符串 'prof_gctx_comp)\n'，完全缺失任何变量声明、赋值或指针解引用操作，无法判断是否存在空指针解引用问题。 |
| 1813 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 471 | TP | Unknown | 切片代码中缺少对宏 `DECODE_CODEWORD` 内部函数 `UPDATE_CACHE` 和 `GET_CACHE` 的定义，无法判断其是否可能返回空指针并导致后续解引用。告警点位于宏展开内部，关键数据流信息缺失。 |

### 5.6 Unknown：算法=FP，LLM=Unknown（共 90 条）

> 算法判定为 FP，LLM 无法判定。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 117 | openssl-openssl-3.3.1 | tls_parse_stoc_npn | cpp/use-after-free | 1581 | FP | Unknown | 切片代码中缺少对关键变量 `selected` 和 `selected_len` 的来源、赋值或验证逻辑，无法判断其值是否有效或受控，因此无法评估 `memcpy` 操作的安全性。 |
| 316 | git-2.50.1 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 706 | FP | Unknown | 切片代码中未提供 `lookup_commit` 函数调用时使用的 `oid` 参数来源，无法判断传入的对象ID是否有效或受控，因此无法评估空指针检查的必要性。 |
| 498 | vim-9.1.0550 | is_duplicate_variable | cpp/inconsistent-null-check | 909 | FP | Unknown | 切片代码仅提供了函数签名和空函数体，完全缺失对 `vim_strnsave` 的调用以及其返回值的处理逻辑，无法判断是否存在空指针检查或相关数据流。 |
| 515 | vim-9.1.0550 | buf_write | cpp/unbounded-write | 2566 | FP | Unknown | 切片代码中未包含触发告警的 strcat 调用点，无法定位具体是哪一行代码存在缓冲区溢出风险。告警信息指向的 read 函数调用也未在切片中明确出现，无法追踪数据流以判断是否确实存在溢出。 |
| 863 | vim-9.1.1040 | is_duplicate_variable | cpp/inconsistent-null-check | 991 | FP | Unknown | 切片代码仅包含函数签名和空函数体，未包含调用 `vim_strnsave` 的语句或其返回值的使用点，无法判断是否存在空指针检查缺失的问题。 |
| 876 | vim-9.1.1040 | buf_write | cpp/unbounded-write | 2566 | FP | Unknown | 切片代码中未包含触发告警的 strcat 调用位置，无法确认具体是哪一行代码存在缓冲区溢出风险。告警信息指向的 read 函数调用也未在切片中明确出现，无法追踪数据流以判断输入是否受控。 |
| 1048 | vim-9.1.1330 | is_duplicate_variable | cpp/inconsistent-null-check | 1011 | FP | Unknown | 切片代码仅包含函数签名和空函数体，未提供任何关于 `vim_strnsave` 调用的具体代码、其返回值的使用方式或任何相关的空值检查逻辑，因此无法判断告警描述的问题是否存在。 |
| 1215 | vim-9.1.0790 | is_duplicate_variable | cpp/inconsistent-null-check | 909 | FP | Unknown | 切片代码仅包含函数签名和空函数体，未提供任何关于 `vim_strnsave` 调用的上下文、其返回值的使用方式或任何错误处理逻辑，无法判断是否存在不一致的空指针检查问题。 |
| 1230 | vim-9.1.0790 | buf_write | cpp/unbounded-write | 2566 | FP | Unknown | 切片代码中未找到告警信息中提到的 'call to strcat' 语句，无法定位具体的缓冲区溢出风险点。切片虽然包含了 buf_write 函数的完整实现，但缺少触发该告警的具体代码行上下文，无法判断是否存在真实的缓冲区溢出漏洞。 |
| 1446 | redis-7.0.11 | streamPropagateXCLAIM | Dereference of null pointer | 1564 | FP | Unknown | 切片代码中缺少对关键指针 `nack->consumer` 是否为空的检查或赋值路径，无法判断其是否可能为空，因此无法确定解引用是否会导致空指针解引用。 |
| 1452 | redis-7.0.11 | strbuf_ensure_null | Dereference of null pointer | 142 | FP | Unknown | 切片代码仅包含函数定义和告警行，缺少对关键参数 `s` 和其成员 `buf`、`length` 的来源、有效性（如是否为NULL）以及调用上下文的任何信息，无法判断空指针解引用是否必然发生。 |
| 1464 | redis-7.4.2 | rb_gen | Dereference of null pointer | 88 | FP | Unknown | 切片代码仅为宏调用，未展示宏定义或具体实现，无法判断是否存在空指针解引用。缺少判断所需的核心代码逻辑。 |
| 1469 | redis-7.4.2 | <global> | Dereference of null pointer | 122 | FP | Unknown | 提供的切片代码仅为字符串 'prof_tdata_comp)\n'，完全缺失与空指针解引用相关的任何代码上下文、变量定义或数据流信息，无法进行任何判断。 |
| 1474 | redis-7.4.2 | <global> | Dereference of null pointer | 103 | FP | Unknown | 提供的切片代码仅为字符串 'prof_gctx_comp)\n'，完全缺失任何程序逻辑、变量定义或数据流信息，无法判断是否存在空指针解引用问题。 |
| 1491 | redis-7.4.2 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | Unknown | 切片代码仅包含函数定义和告警行，缺少对关键参数 `s` 和其成员 `buf`、`length` 的来源、有效性（如是否为NULL）或前置条件的任何信息，无法判断空指针解引用是否必然发生。 |
| 1498 | redis-7.4.2 | connClose | Dereference of null pointer | 229 | FP | Unknown | 切片代码仅显示通过指针conn访问其成员type，但未提供conn指针的来源、有效性检查或赋值上下文，无法判断conn是否为NULL。 |
| 1507 | redis-7.2.1 | rb_gen | Dereference of null pointer | 88 | FP | Unknown | 切片代码仅为宏调用，未展示任何指针变量的定义、赋值或使用上下文，无法判断是否存在空指针解引用。 |
| 1511 | redis-7.2.1 | <global> | Dereference of null pointer | 122 | FP | Unknown | 提供的切片代码仅为一行函数名，完全缺失与空指针解引用相关的任何代码上下文、变量定义或数据流信息，无法进行任何判断。 |
| 1516 | redis-7.2.1 | <global> | Dereference of null pointer | 103 | FP | Unknown | 提供的切片代码仅为字符串 'prof_gctx_comp)\n'，不包含任何有意义的程序逻辑、变量定义或数据流信息，无法判断是否存在空指针解引用问题。 |
| 1533 | redis-7.2.1 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | Unknown | 切片代码仅包含函数定义和使用点，缺少对关键参数 `s` 和其成员 `buf`、`length` 的来源、有效性（如是否为NULL）以及它们之间关系的任何信息，无法判断是否存在空指针解引用。 |
| 1549 | redis-7.2.5 | rb_gen | Dereference of null pointer | 88 | FP | Unknown | 切片代码仅为宏定义或函数声明，未包含任何实际执行逻辑或数据流，无法判断是否存在空指针解引用。 |
| 1553 | redis-7.2.5 | <global> | Dereference of null pointer | 122 | FP | Unknown | 提供的切片代码仅为一行函数名或比较操作符，完全缺失任何变量定义、赋值、控制流或指针解引用上下文，无法判断是否存在空指针解引用问题。 |
| 1558 | redis-7.2.5 | <global> | Dereference of null pointer | 103 | FP | Unknown | 提供的切片代码仅为变量名片段，完全缺失任何赋值、使用或控制流上下文，无法判断是否存在空指针解引用或相关防护逻辑。 |
| 1575 | redis-7.2.5 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | Unknown | 切片代码仅包含函数定义和使用点，缺少对关键参数 `s` 及其成员 `buf` 和 `length` 的来源、有效性（如是否为NULL）或前置条件的任何信息，无法判断是否存在空指针解引用。 |
| 1629 | redis-8.0.2 | connClose | Dereference of null pointer | 235 | FP | Unknown | 切片代码仅包含函数调用，未提供 `conn` 或 `conn->type` 是否为 NULL 的任何赋值、校验或传递路径信息，无法判断空指针解引用是否必然发生。 |
| 1631 | ffmpeg-7.1.1 | show_bits | Dereference of null pointer | 376 | FP | Unknown | 切片代码仅展示了宏展开，未提供关键指针 `s` 或 `gb` 的来源、初始化或空值检查信息，无法判断 `s` 是否为 NULL 或是否已在调用前被有效初始化。 |
| 1643 | ffmpeg-7.1.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | Unknown | 切片代码中缺少对指针 `s` 是否为空的检查或赋值信息，无法判断 `s` 是否可能为空。告警点 `s->bit_buf` 直接解引用 `s`，但切片内没有提供 `s` 的来源或任何空值防护逻辑，因此无法确定解引用是否安全。 |
| 1654 | ffmpeg-7.1.1 | envelope_peak | Dereference of null pointer | 375 | FP | Unknown | 切片代码中变量 `dpd` 的来源和定义完全缺失，无法判断其是否为有效的指针或是否可能为 NULL，因此无法评估空指针解引用风险。 |
| 1653 | ffmpeg-7.1.1 | get_sbits | Dereference of null pointer | 325 | FP | Unknown | 切片代码仅展示了宏展开后的函数框架，未提供关键参数 `GetBitContext *s` 的来源、初始化状态或调用上下文，无法判断其是否为 NULL。告警涉及空指针解引用，但切片缺少评估指针有效性的必要信息。 |
| 1673 | ffmpeg-7.1.1 | ogg_write_header | Dereference of null pointer | 629 | FP | Unknown | 切片代码仅包含对指针`oggstream`的成员赋值，但未包含`oggstream`指针本身的来源、初始化或空值检查。无法判断在解引用`oggstream->page`时，`oggstream`是否可能为空。 |
| 1672 | ffmpeg-7.1.1 | get_pict_type | Dereference of null pointer | 136 | FP | Unknown | 切片代码中缺少对关键变量 `pu` 是否为 `NULL` 的检查或保证。告警点 `slice->header.sh_slice_type` 的访问依赖于 `unit->content` 赋值给 `slice`，而 `unit` 又来自... |
| 1700 | ffmpeg-7.1.1 | vectorscope8 | Dereference of null pointer | 775 | FP | Unknown | 切片代码中缺少对关键指针变量 `dpd` 和 `dp1`、`dp2` 的定义、赋值或来源的说明，无法判断 `dpd[pos]` 是否可能为空，因此无法确定解引用 `dpd[pos]` 是否会导致空指针解引用。 |
| 1705 | ffmpeg-7.1.1 | get_bits_le | Dereference of null pointer | 361 | FP | Unknown | 切片代码仅展示了宏展开后的函数框架，缺少对关键参数 `s`（GetBitContext *）是否为空的任何检查或赋值信息，无法判断其是否可能为空指针。 |
| 1706 | ffmpeg-7.1.1 | ac3_apply_rematrixing | Dereference of null pointer | 598 | FP | Unknown | 切片代码中变量 `flags` 的来源和赋值完全缺失，无法判断其是否为空指针。告警点 `if (flags[bnd])` 直接解引用 `flags`，但切片内无任何关于 `flags` 定义或初始化的信息，缺少做出判断所必须的核心信息。 |
| 1711 | ffmpeg-7.1.1 | shift_frame | Dereference of null pointer | 152 | FP | Unknown | 切片代码中变量 `frame` 的来源和赋值完全缺失，无法判断其是否为 null 指针。告警点直接解引用了 `frame->pts`，但切片内没有 `frame` 的定义或初始化信息，缺少做出判断的核心依据。 |
| 1725 | ffmpeg-7.0.1 | show_bits | Dereference of null pointer | 376 | FP | Unknown | 切片代码仅包含宏定义和函数框架，缺少对关键指针 `s` 和 `gb` 的赋值、传递或有效性检查的上下文，无法判断 `s` 是否为 NULL 或是否已正确初始化，因此无法确定是否存在空指针解引用。 |
| 1736 | ffmpeg-7.0.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | Unknown | 切片代码中缺少对关键指针 `s` 是否为空的判断依据。告警点 `s->bit_buf` 直接解引用 `s`，但切片内没有显示 `s` 的来源、调用方对其的校验或赋值，无法确定其是否可能为空。 |
| 1748 | ffmpeg-7.0.1 | envelope_peak | Dereference of null pointer | 375 | FP | Unknown | 切片代码中变量`dpd`的来源和初始化状态完全缺失，无法判断其是否为有效的非空指针，因此无法确定空指针解引用是否会发生。 |
| 1747 | ffmpeg-7.0.1 | get_sbits | Dereference of null pointer | 325 | FP | Unknown | 切片代码仅展示了宏展开后的函数框架，缺少对关键参数 `s`（GetBitContext *）是否为 NULL 的赋值、传递或校验信息。无法判断在调用点 `UPDATE_CACHE(re, s)` 时指针 `s` 是否可能为空，因此无法... |
| 1762 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 293 | FP | Unknown | 切片代码中，在解引用 `ost->ist->par` 之前，未包含对 `ost->ist` 或 `ost->ist->par` 是否为 NULL 的检查。告警点位于条件分支 `if (!enc_ctx->width)` 内部，但无法从... |
| 1771 | ffmpeg-7.0.1 | ogg_write_header | Dereference of null pointer | 628 | FP | Unknown | 切片代码中变量 `oggstream` 的来源和赋值完全缺失，无法判断其是否为 null，因此无法确定解引用是否会发生。 |
| 1799 | ffmpeg-7.0.1 | get_bits_le | Dereference of null pointer | 361 | FP | Unknown | 切片代码仅展示了宏定义和内联函数的调用，未提供关键参数 `s`（GetBitContext *）的来源、初始化或验证信息，无法判断其是否可能为NULL，因此无法确定空指针解引用是否会发生。 |
| 1800 | ffmpeg-7.0.1 | ac3_apply_rematrixing | Dereference of null pointer | 387 | FP | Unknown | 切片代码中缺少对关键变量 `flags` 的定义、赋值或来源信息，无法判断其是否可能为 NULL，因此无法确定解引用 `flags[bnd]` 是否会导致空指针解引用。 |
| 1804 | ffmpeg-7.0.1 | shift_frame | Dereference of null pointer | 153 | FP | Unknown | 切片代码中变量`frame`的来源和定义完全缺失，无法判断其是否为NULL指针。告警点位于对`frame->pts`的访问，但切片未包含`frame`的赋值、传递或空值检查的任何上下文。 |
| 1817 | ffmpeg-6.1.1 | show_bits | Dereference of null pointer | 376 | FP | Unknown | 切片代码仅展示了宏展开，未提供 `UPDATE_CACHE_LE` 宏的具体实现以及 `GetBitContext *s` 指针的来源和有效性检查，无法判断空指针解引用是否必然发生。 |
| 1829 | ffmpeg-6.1.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | Unknown | 切片代码中缺少对关键指针 `s` 是否为空的判断或赋值信息，无法确认在函数入口处 `s` 是否已被有效初始化或校验，因此无法判断空指针解引用是否必然发生。 |
| 1838 | ffmpeg-6.1.1 | envelope_peak | Dereference of null pointer | 375 | FP | Unknown | 切片代码中变量 `dpd` 的来源和初始化信息完全缺失，无法判断其是否为有效的非空指针，因此无法确定空指针解引用是否会发生。 |
| 1837 | ffmpeg-6.1.1 | get_sbits | Dereference of null pointer | 325 | FP | Unknown | 切片代码仅展示了宏展开后的函数框架，缺少对关键参数 `s`（GetBitContext *）是否为空的任何检查或赋值信息。无法判断在调用 `UPDATE_CACHE` 时指针 `s` 是否可能为空，这是判断空指针解引用告警的核心依据。 |
| 1859 | ffmpeg-6.1.1 | ogg_write_header | Dereference of null pointer | 628 | FP | Unknown | 切片代码仅显示对结构体成员`page.start_granule`的赋值，未包含`oggstream`指针的声明、初始化或空值检查。无法判断`oggstream`是否为NULL，因此无法确定是否存在空指针解引用。 |
| 1858 | ffmpeg-6.1.1 | get_pict_type | Dereference of null pointer | 135 | FP | Unknown | 切片代码中缺少对关键变量 `has_p` 的声明和初始化，无法判断其初始值，进而无法确定函数返回路径是否安全。同时，`slice->header.sh_slice_type` 的访问依赖于 `unit->content` 的赋值，但切... |
| 1886 | ffmpeg-6.1.1 | unsharp_slice_8 | Dereference of null pointer | 142 | FP | Unknown | 切片代码仅展示了宏定义和部分函数框架，未包含触发空指针解引用的具体执行路径或变量赋值上下文，无法判断指针 'sc' 或 'sr' 在解引用前是否已被正确初始化或验证。 |
| 1890 | ffmpeg-6.1.1 | get_bits_le | Dereference of null pointer | 361 | FP | Unknown | 切片代码仅展示了宏定义和函数框架，缺少对关键参数 `s`（GetBitContext *）是否为空的任何检查或赋值信息，无法判断其是否可能为空指针。 |
| 1891 | ffmpeg-6.1.1 | ac3_apply_rematrixing | Dereference of null pointer | 411 | FP | Unknown | 切片代码中缺少对关键变量 `flags` 的定义、初始化或赋值，无法判断其来源及是否为非空指针，因此无法确定对 `flags[bnd]` 的解引用是否安全。 |
| 1895 | ffmpeg-6.1.1 | shift_frame | Dereference of null pointer | 153 | FP | Unknown | 切片代码中变量`frame`的来源和定义完全缺失，无法判断其是否为NULL，也无法评估`frame->pts`解引用操作的安全性。 |
| 1908 | ffmpeg-7.1 | show_bits | Dereference of null pointer | 376 | FP | Unknown | 切片代码仅包含宏定义和函数框架，未提供 `GetBitContext *s` 参数的具体来源、初始化状态或空值检查，无法判断指针 `s` 是否可能为空。 |
| 1920 | ffmpeg-7.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | Unknown | 切片代码中缺少对关键指针 `s` 是否为空的判断依据。告警发生在对 `s->bit_buf` 的访问，但函数入口处没有对 `s` 进行空指针检查，且切片中未包含任何调用方信息来推断 `s` 的来源和有效性，无法确定该解引用是否必然为空。 |
| 1930 | ffmpeg-7.1 | get_sbits | Dereference of null pointer | 325 | FP | Unknown | 切片代码仅展示了宏展开后的函数框架，缺少对关键参数 `s`（GetBitContext *）是否为空的任何检查或赋值信息。无法判断在调用 `UPDATE_CACHE` 宏时 `s` 是否可能为空指针，这是判断空指针解引用的核心依据。 |
| 1931 | ffmpeg-7.1 | envelope_peak | Dereference of null pointer | 375 | FP | Unknown | 切片代码中，在第二个循环内使用了变量 `dpd[pos]`，但该变量在切片中未定义，也未显示其来源或初始化。无法判断 `dpd` 是否为有效的非空指针，因此无法确定空指针解引用是否会发生。 |
| 1947 | ffmpeg-7.1 | choose_rct_params | Dereference of null pointer | 990 | FP | Unknown | 切片代码中未包含对关键数组 `src` 的初始化或赋值信息，无法判断 `src[1]` 和 `src[2]` 是否为非空指针，因此无法确定是否存在空指针解引用。 |
| 1951 | ffmpeg-7.1 | ogg_write_header | Dereference of null pointer | 629 | FP | Unknown | 切片代码仅包含对结构体成员`page.start_granule`的赋值操作，未提供`oggstream`指针的来源、初始化或空值检查信息，无法判断其是否可能为NULL，因此无法确定是否存在空指针解引用。 |
| 1978 | ffmpeg-7.1 | vectorscope8 | Dereference of null pointer | 775 | FP | Unknown | 切片代码中缺少对关键指针变量 `dpd` 和 `dp1`、`dp2` 的定义、赋值或来源信息，无法判断 `dpd[pos]` 是否可能为空，因此无法确定解引用 `dpd[pos]` 是否会导致空指针解引用。 |
| 1983 | ffmpeg-7.1 | get_bits_le | Dereference of null pointer | 361 | FP | Unknown | 切片代码仅展示了宏定义和函数框架，缺少对关键参数 `s`（GetBitContext *）是否为空的判断逻辑。无法从切片中追踪 `s` 的来源或验证其非空性，因此无法确定空指针解引用是否必然发生。 |
| 1984 | ffmpeg-7.1 | ac3_apply_rematrixing | Dereference of null pointer | 598 | FP | Unknown | 切片代码中变量 `flags` 的来源和赋值完全缺失，无法判断其是否为空指针。告警点 `if (flags[bnd])` 直接解引用了 `flags`，但切片内无任何关于 `flags` 定义或初始化的信息，缺少做出判断所必须的核心信息。 |
| 1989 | ffmpeg-7.1 | shift_frame | Dereference of null pointer | 152 | FP | Unknown | 切片代码中，告警点引用的变量 `frame` 未在可见的上下文中定义或赋值，无法判断其来源及是否为 null，缺少做出判断所必须的核心信息。 |
| 2000 | ffmpeg-7.1 | <global> | Dereference of null pointer | 472 | FP | Unknown | 切片代码仅展示了宏定义，未包含宏展开后对指针 `gb` 的实际操作代码，无法判断 `gb` 是否为 NULL 以及是否会发生空指针解引用。 |
| 2003 | ffmpeg-6.0 | show_bits | Dereference of null pointer | 366 | FP | Unknown | 切片代码仅展示了宏展开，未提供关键结构体指针 `s` 的赋值、初始化或校验信息，无法判断其是否为 NULL。告警涉及对 `s` 的潜在空指针解引用，但切片中缺少判断其状态所必需的核心数据流。 |
| 2013 | ffmpeg-6.0 | put_bits_no_assert | Dereference of null pointer | 202 | FP | Unknown | 切片代码中缺少对指针`s`进行空值检查的上下文，无法判断调用此函数前`s`是否已被验证为非空。告警点直接解引用`s->bit_buf`，但切片未包含`s`的来源或任何前置的空指针校验。 |
| 2023 | ffmpeg-6.0 | envelope_peak | Dereference of null pointer | 375 | FP | Unknown | 切片代码中变量`dpd`的来源和初始化状态完全缺失，无法判断其是否为有效的非空指针，因此无法确定对`dpd[pos]`的访问是否会导致空指针解引用。 |
| 2032 | ffmpeg-6.0 | choose_rct_params | Dereference of null pointer | 979 | FP | Unknown | 切片代码中未包含对关键指针数组 `src` 的初始化或赋值信息，无法判断 `src[1]` 和 `src[2]` 是否为 NULL。告警点位于对 `src[1]` 和 `src[2]` 的解引用处，缺少判断其有效性的核心上下文。 |
| 2039 | ffmpeg-6.0 | ogg_write_header | Dereference of null pointer | 628 | FP | Unknown | 切片代码仅包含对指针`oggstream`的成员赋值，但未包含`oggstream`指针本身的定义、初始化或空值检查。无法判断该指针在解引用前是否已分配内存或进行过非空验证，缺少做出判断的核心信息。 |
| 2045 | ffmpeg-6.0 | guess_status_pts | Dereference of null pointer | 446 | FP | Unknown | 切片代码中未包含对指针 `ctx->inputs[i]` 是否为空的检查或赋值信息，无法判断该指针在解引用前是否已被安全初始化或验证，缺少做出判断所必需的核心信息。 |
| 2064 | ffmpeg-6.0 | get_bits_le | Dereference of null pointer | 351 | FP | Unknown | 切片代码仅展示了宏展开后的形式，缺少对关键指针 `(gb)->buffer` 是否为空进行验证的上下文。告警点位于宏 `UPDATE_CACHE_LE` 中，该宏直接解引用了 `(gb)->buffer`，但切片中未包含 `get_b... |
| 2065 | ffmpeg-6.0 | ac3_apply_rematrixing | Dereference of null pointer | 410 | FP | Unknown | 切片代码中变量 `flags` 的来源和赋值完全缺失，无法判断其是否为空指针。告警点 `if (flags[bnd])` 直接解引用 `flags`，但切片内无任何关于 `flags` 定义或初始化的信息，缺少做出判断所必须的核心信息。 |
| 2067 | ffmpeg-6.0 | shift_frame | Dereference of null pointer | 150 | FP | Unknown | 切片代码中，告警行引用了未定义的变量 `frame`，且切片内未包含该变量的声明、赋值或来源信息，无法判断其是否为空指针。 |
| 2098 | git-2.46.0 | gather_stats | Dereference of null pointer | 51 | FP | Unknown | 切片代码存在语法错误和不完整（如多余的右花括号、不完整的switch语句），无法正确解析函数逻辑，因此无法判断空指针解引用是否真实存在。 |
| 2099 | git-2.46.0 | append_strategy | Dereference of null pointer | 229 | FP | Unknown | 切片代码仅包含函数定义和告警行，未提供调用方信息，无法判断传入的指针`s`是否为NULL，缺少做出判断所必需的核心上下文。 |
| 2100 | git-2.46.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | Unknown | 切片代码仅包含函数定义和告警行，缺少对关键参数 `array` 和 `value` 的来源、有效性（如是否为NULL）以及 `array->v` 容量是否足够的任何检查或上下文，无法判断空指针解引用是否必然发生。 |
| 2159 | git-2.49.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | Unknown | 切片代码仅包含赋值语句，缺少对关键指针`array`和`array->v`是否为NULL的检查或赋值来源信息，无法判断空指针解引用是否必然发生。 |
| 2161 | git-2.49.0 | image_remove_first_line | Dereference of null pointer | 355 | FP | Unknown | 切片代码中缺少对关键指针 `img` 和其成员 `img->line` 是否为 NULL 的验证信息，无法判断空指针解引用是否必然发生。 |
| 2165 | git-2.49.0 | <global> | Dereference of null pointer | 30 | FP | Unknown | 切片代码仅提供了函数签名和空函数体，缺少判断空指针解引用告警所必需的核心逻辑。无法从切片中获知函数内部是否存在解引用操作、`path`参数的使用方式或任何控制流信息。 |
| 2217 | git-2.44.0 | gather_stats | Dereference of null pointer | 49 | FP | Unknown | 切片代码不完整且存在语法错误（如多余的右花括号），无法可靠分析函数入口条件及`buf`指针的有效性。关键信息缺失，无法判断空指针解引用是否必然发生。 |
| 2227 | git-2.44.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | Unknown | 切片代码仅包含函数内部赋值语句，未提供任何关于指针`array`或数组`array->v`是否已正确初始化的上下文信息，无法判断`array`是否为NULL或`array->v`是否已分配足够空间，缺少做出判断所必需的核心信息。 |
| 2279 | git-2.50.1 | append_strategy | Dereference of null pointer | 233 | FP | Unknown | 切片代码仅包含函数定义和告警行，完全缺失对关键变量 `s` 的来源、赋值或是否为空的任何检查信息，无法判断其是否可能为 null 指针。 |
| 2281 | git-2.50.1 | strvec_push_nodup | Dereference of null pointer | 19 | FP | Unknown | 切片代码仅包含函数内部的一行赋值语句，缺少对关键参数 `array` 是否为 NULL 的检查逻辑。无法判断调用方是否保证了 `array` 非空，或函数内部是否有前置的 NULL 指针校验，因此无法确定是否存在空指针解引用。 |
| 2283 | git-2.50.1 | image_remove_first_line | Dereference of null pointer | 355 | FP | Unknown | 切片代码中缺少对关键指针 `img` 和其成员 `img->line` 是否为空的检查或赋值信息，无法判断在调用 `strbuf_remove` 时 `img->line[0].len` 的访问是否安全。 |
| 2340 | git-2.47.1 | append_strategy | Dereference of null pointer | 231 | FP | Unknown | 切片代码仅包含函数定义和告警行，未提供调用方上下文。无法判断传入的指针`s`是否可能为NULL，因此无法确定解引用是否安全。 |
| 2344 | git-2.47.1 | image_remove_first_line | Dereference of null pointer | 354 | FP | Unknown | 切片代码中缺少对关键变量 `img` 和 `img->line` 的初始化、有效性检查或调用前状态的判断，无法确认 `img` 或 `img->line[0]` 是否为非空，因此无法评估空指针解引用风险。 |
| 2479 | tmux-3.2 | spawn_window | Dereference of null pointer | 181 | FP | Unknown | 切片代码中未包含对指针变量 `w` 的初始化或赋值，无法判断其是否为 NULL。告警点 `w->latest = sc->tc;` 存在对 `w` 的解引用，但 `w` 的来源在切片中完全缺失，无法确定是否存在空指针解引用风险。 |
| 2482 | tmux-3.2 | spawn_window | Dereference of null pointer | 185 | FP | Unknown | 切片代码中，在告警行 `w->name = default_window_name(w);` 之前，变量 `w` 的赋值路径不明确。存在 `w = NULL;` 和 `w = sc->wl->window;` 等不同分支，但无法确定在... |
| 2503 | tmux-3.4 | mode_tree_get_tag | Dereference of null pointer | 309 | FP | Unknown | 切片代码中未包含变量 `i` 的声明和初始化，无法判断循环条件 `i < mtd->line_size` 是否会导致 `i` 超出 `mtd->line_list` 的有效索引范围，从而无法确认 `mtd->line_list[i].... |

---

*报告由 `analyze_results.py` 自动生成，生成时间：2026-03-03 20:10:02*
