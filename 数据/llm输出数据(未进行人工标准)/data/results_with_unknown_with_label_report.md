# LLM 分类结果分析报告

- **分析文件**：`results_with_unknown_with_label.json`
- **完整路径**：`/home/lg/Documents/projects/毕设/大仓/匹配/llm-match/output/results_with_unknown_with_label.json`
- **生成时间**：2026-03-05 23:16:20

---

## 1. 数据总览

| 指标 | 数值 |
|---|---|
| 数据总条数 | 2510 |
| 有效条目数（含 label / llm_label） | 2510 |
| 跳过条目数（字段缺失或无效） | 0 |
| Unknown 条目数 | 49 |
| Unknown 比率 | 2.0% |
| 已判定条目数（非 Unknown） | 2461 |
| 判定一致数 | 2277 |
| 判定不一致数 | 184 |

## 2. 算法标注（label）分布

| label | 数量 | 占比 |
|---|---|---|
| TP | 218 | 8.7% |
| FP | 2292 | 91.3% |

## 3. label × llm_label 交叉矩阵

| label \ llm_label | TP | FP | Unknown | **合计** |
|---|---|---|---|---|
| **TP** | 133 | 74 | 11 | **218** |
| **FP** | 110 | 2144 | 38 | **2292** |
| **合计** | 243 | 2218 | 49 | **2510** |

## 4. 汇总指标

> 以下指标仅基于**已判定（非 Unknown）**条目计算。

| 指标 | 数值 |
|---|---|
| 准确率（Accuracy） | 92.5% |
| 精确率（Precision，以 TP 为正类） | 54.7% |
| 召回率（Recall，以 TP 为正类） | 64.3% |
| F1 分数（以 TP 为正类） | 59.1% |

## 5. 各分类条目详情

### 5.1 一致：算法=TP，LLM=TP（共 133 条）

> 算法与 LLM 均判定为真阳性（True Positive）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 678 | vim-9.1.1591 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | TP | TP | 函数 `getcell` 可能返回 NULL，但调用点 `vterm_screen_is_eol` 在使用 `cell->chars[0]` 前未进行空指针检查，存在解引用空指针的风险。 |
| 680 | vim-9.1.1591 | get_isolated_shell_name | cpp/inconsistent-null-check | 2754 | TP | TP | 函数`vim_strnsave`在内存分配失败时会返回NULL，但调用点`p = vim_strnsave(p1, p - p1);`未检查返回值，后续直接返回给调用者，可能导致空指针解引用。切片中未见任何防护机制。 |
| 693 | vim-9.1.1591 | common_function | cpp/unsafe-strcat | 5401 | TP | TP | 代码在行`STRCAT(IObuff, start_bracket);`处使用了不安全的`strcat`宏（即`strcat`），将`start_bracket`的内容追加到固定大小的缓冲区`IObuff`中，而`start_brac... |
| 696 | vim-9.1.1591 | store_aff_word | cpp/unsafe-strcat | 3915 | TP | TP | 代码使用宏`STRCAT`（即`strcat`）向固定大小的缓冲区`newword`（大小为`MAXWLEN`）追加内容，但未检查追加后总长度是否超过缓冲区大小，存在缓冲区溢出的风险。 |
| 697 | vim-9.1.1591 | prt_line_number | cpp/overrunning-write | 387 | TP | TP | sprintf 使用格式字符串 '%6ld' 写入一个长整型，在最坏情况下（如 lnum 为负值且绝对值很大）需要至少 7 个字符（符号+6位数字），加上字符串终止符 '\0' 共需 8 字节，但目标缓冲区 tbuf 仅 20 字节，... |
| 698 | vim-9.1.1591 | highlight_color | cpp/overrunning-write | 3278 | TP | TP | sprintf 目标缓冲区 'buf' 大小为10字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少10字节，当三个十六进制数均为最大值（ffffff）时，生成的字符串长度为 '#fffffffff'（9个字符加... |
| 699 | vim-9.1.1591 | msg_outnum | cpp/overrunning-write | 1651 | TP | TP | 目标缓冲区`buf`大小为20字节，但`sprintf`格式化长整数`%ld`时，对于某些负数值（如-9223372036854775808）需要21字节（包括负号、20位数字和空终止符），存在缓冲区溢出风险。 |
| 701 | vim-9.1.1591 | ga_concat_strings | cpp/unbounded-write | 788 | TP | TP | 代码使用宏STRCPY（即strcpy）将未知长度的字符串复制到固定大小的缓冲区s中，s的大小由累加计算得出，但目标缓冲区p在循环中移动，若源字符串长度超过剩余缓冲区大小，将导致缓冲区溢出。 |
| 702 | vim-9.1.1591 | maketitle | cpp/unbounded-write | 4239 | TP | TP | 代码使用 STRCPY（即 strcpy）将 `name` 复制到固定大小的缓冲区 `buf` 中，而 `name` 可能来自 `buf_spname` 或 `gettail`，其长度未经验证，存在缓冲区溢出风险。 |
| 703 | vim-9.1.1591 | buf_write | cpp/unbounded-write | 1208 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将fname复制到固定大小的IObuff缓冲区，未检查fname长度，存在缓冲区溢出风险。切片中未显示IObuff的大小定义，但根据常见模式及告警规则，这是典型的未受控拷贝。 |
| 704 | vim-9.1.1591 | buf_write | cpp/unbounded-write | 2568 | TP | TP | 代码中存在对 `STRCAT` 宏的调用，该宏展开为 `strcat`，且目标缓冲区 `IObuff` 的大小为 `IOSIZE`。告警指出 `strcat` 的输入来自 `read` 读取的缓冲区，可能导致目标缓冲区溢出。切片中可见... |
| 705 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2150 | TP | TP | 代码中直接使用宏STRCAT（即strcat）将p_extra追加到leader缓冲区，未检查目标缓冲区leader的大小，存在缓冲区溢出风险。 |
| 706 | vim-9.1.1591 | transstr | cpp/unbounded-write | 400 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区res追加内容，而res的大小由alloc(len + 1)分配，但追加的字符串长度未受限制，存在缓冲区溢出风险。 |
| 707 | vim-9.1.1591 | globpath | cpp/unbounded-write | 4180 | TP | TP | 代码使用STRCPY（即strcpy）将用户控制的`file`参数复制到固定大小的缓冲区`buf`中，虽然存在长度检查`pathlen + seplen + filelen + 1 <= MAXPATHL`，但`filelen`的计算... |
| 708 | vim-9.1.1591 | expand_shellcmd | cpp/unbounded-write | 3902 | TP | TP | 代码使用STRCPY（即strcpy）将可变长度的字符串`pat`复制到固定大小的缓冲区`buf`中，虽然存在长度检查`pathlen + seplen + patlen + 1 <= MAXPATHL`，但`pat`在循环中被修改（... |
| 709 | vim-9.1.1591 | win_redr_status_matches | cpp/unbounded-write | 698 | TP | TP | 代码使用STRCPY（即strcpy）宏将字符串复制到固定大小的缓冲区buf中，而buf的大小基于Columns分配。源字符串s来自外部输入（如环境变量、文件读取等），其长度未经验证，可能导致缓冲区溢出。 |
| 711 | vim-9.1.1591 | debuggy_find | cpp/unbounded-write | 1067 | TP | TP | 代码使用宏 STRCPY（即 strcpy）将源字符串 fname 复制到目标缓冲区 name，而 name 的大小仅为 STRLEN(fname) + 3，strcpy 会复制整个源字符串包括终止空字符，若 fname 长度恰好使目... |
| 712 | vim-9.1.1591 | has_profiling | cpp/unbounded-write | 973 | TP | TP | 代码使用 STRCPY（即 strcpy）将未限制长度的源字符串 fname 复制到固定大小的目标缓冲区 pe->pen_name，存在缓冲区溢出风险。虽然 pe 的内存分配考虑了 fname 的长度，但 STRCPY 本身不检查边界... |
| 713 | vim-9.1.1591 | ex_diffpatch | cpp/unbounded-write | 1512 | TP | TP | 代码中直接使用不安全的 STRCPY 宏（即 strcpy）将字符串复制到固定大小的缓冲区 buf 中，而 buf 的大小是根据多个字符串长度计算得到的，但后续的 STRCPY 和 STRCAT 操作可能使写入超出 buf 的边界，存... |
| 714 | vim-9.1.1591 | do_string_sub | cpp/unbounded-write | 8057 | TP | TP | 代码在告警行使用STRCPY（即strcpy）将`tail`指向的字符串复制到`ga.ga_data`缓冲区的末尾，而`tail`是用户输入字符串`str`的一部分，其长度可能超过目标缓冲区剩余空间（`ga.ga_maxlen - g... |
| 715 | vim-9.1.1591 | set_var_const | cpp/unbounded-write | 4300 | TP | TP | 代码使用STRCPY宏（即strcpy）将varname复制到di->di_key，而varname是用户提供的变量名，其长度未经验证，可能导致目标缓冲区溢出。 |
| 716 | vim-9.1.1591 | cat_prefix_varname | cpp/unbounded-write | 2578 | TP | TP | 代码使用STRCPY（即strcpy）将外部传入的字符串name复制到缓冲区varnamebuf+2，虽然缓冲区大小len根据name长度动态分配，但分配后立即将varnamebuf[1]和varnamebuf[0]赋值，未保留空字符... |
| 717 | vim-9.1.1591 | ex_substitute | cpp/unbounded-write | 5115 | TP | TP | 代码中直接使用宏 `STRCAT(d, s)`（即 `strcat`）将 `sub_firstline + copycol` 的内容追加到 `new_start` 缓冲区，但 `new_start` 缓冲区的大小 `new_start... |
| 718 | vim-9.1.1591 | make_filter_cmd | cpp/unbounded-write | 1854 | TP | TP | 代码在多个分支中直接使用不安全的STRCPY（即strcpy）宏将外部传入的cmd字符串复制到固定大小的缓冲区buf中，而buf的大小len是基于cmd等字符串的长度计算分配的，但strcpy本身不检查目标缓冲区大小，若cmd等字符串... |
| 719 | vim-9.1.1591 | make_filter_cmd | cpp/unbounded-write | 1858 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buf追加内容，而buf的大小len是基于多个字符串长度计算分配的。虽然计算了总长度，但后续的STRCAT操作未检查剩余缓冲区空间，存在缓冲区溢出的风险。 |
| 720 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 795 | TP | TP | 代码使用宏STRCPY（即strcpy）将长度不确定的字符串&s[start_col]复制到固定大小的缓冲区sortbuf1中，而sortbuf1的大小仅由maxlen+1决定，无法保证源字符串长度不超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 721 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 815 | TP | TP | 代码使用宏STRCPY（即strcpy）将长度不确定的字符串&s[start_col]复制到固定大小的缓冲区sortbuf1中，而sortbuf1的大小由maxlen+1分配，但&s[start_col]可能来自外部输入（如文件行），... |
| 722 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 833 | TP | TP | 代码使用STRCPY宏（即strcpy）将长度不确定的字符串`s[start_col]`复制到固定大小的缓冲区`sortbuf1`中，而`sortbuf1`的大小仅根据`maxlen`分配，无法保证源字符串长度不超过目标缓冲区大小，存... |
| 723 | vim-9.1.1591 | ex_sort | cpp/unbounded-write | 605 | TP | TP | 代码使用STRCPY宏（即strcpy）将长度未知的字符串s复制到固定大小的缓冲区sortbuf1中，而sortbuf1的大小仅基于maxlen+1分配，但s可能来自外部输入（如文件读取），存在缓冲区溢出风险。 |
| 724 | vim-9.1.1591 | expand_sfile | cpp/unbounded-write | 10143 | TP | TP | 代码使用STRCPY（即strcpy）将可变长度字符串repl复制到固定大小的缓冲区newres中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 725 | vim-9.1.1591 | repl_cmdline | cpp/unbounded-write | 5330 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串'src + srclen'复制到目标缓冲区，目标缓冲区大小'i'虽经计算，但未确保复制前目标位置有足够空间，存在缓冲区溢出风险。 |
| 726 | vim-9.1.1591 | repl_cmdline | cpp/unbounded-write | 5336 | TP | TP | 代码使用STRCPY（即strcpy）向固定大小的缓冲区new_cmdline写入数据，写入位置由new_cmdlinelen偏移计算，但未检查偏移后剩余缓冲区大小是否足以容纳源字符串src + srclen或eap->nextcmd... |
| 727 | vim-9.1.1591 | replace_makeprg | cpp/unbounded-write | 5037 | TP | TP | 代码使用STRCPY（即strcpy）将用户控制的参数p复制到目标缓冲区ptr，目标缓冲区大小由alloc分配，但分配时未考虑p的长度可能超过剩余空间，存在缓冲区溢出风险。 |
| 728 | vim-9.1.1591 | replace_makeprg | cpp/unbounded-write | 5052 | TP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串`p`和`program`复制到固定大小的缓冲区`new_cmdline`中，而`new_cmdline`的大小是通过alloc动态分配的，其计算依赖于STRLEN(pro... |
| 729 | vim-9.1.1591 | do_one_cmd | cpp/unbounded-write | 2686 | TP | TP | 代码中直接使用宏STRCPY（即strcpy）将可变长度的错误消息字符串复制到固定大小的缓冲区IObuff，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 730 | vim-9.1.1591 | discard_exception | cpp/unbounded-write | 646 | TP | TP | 代码使用STRCPY（即strcpy）将saved_IObuff复制回IObuff，而saved_IObuff是之前通过vim_strsave(IObuff)分配的副本，其长度与原始IObuff相同。但IObuff是一个固定大小的全局... |
| 731 | vim-9.1.1591 | get_exception_string | cpp/unbounded-write | 473 | TP | TP | 代码使用`strcat`向缓冲区`val`追加内容，而`val`指向的缓冲区大小由`vim_strnsave`分配，其大小计算依赖于`mesg`的长度。由于`mesg`内容可能包含用户输入或外部数据，且追加操作前未检查目标缓冲区剩余空... |
| 732 | vim-9.1.1591 | get_exception_string | cpp/unbounded-write | 484 | TP | TP | 代码使用`sprintf`将`&mesg[1]`的内容格式化写入`val`缓冲区，而`val`指向的缓冲区大小由`vim_strnsave`分配，其大小仅考虑了`mesg`的原始长度和固定前缀，未考虑`sprintf`添加的额外格式字... |
| 733 | vim-9.1.1591 | escape_fname | cpp/unbounded-write | 4193 | TP | TP | 代码使用STRCPY（即strcpy）将源字符串复制到新分配的目标缓冲区，目标缓冲区大小仅比源字符串长度大2字节，若源字符串长度未知或未以空字符结尾，strcpy可能写入超出分配边界，导致缓冲区溢出。 |
| 734 | vim-9.1.1591 | cmdline_browse_history | cpp/unbounded-write | 1528 | TP | TP | 代码使用STRCPY宏（即strcpy）将历史记录字符串p复制到ccline.cmdbuff中，而ccline.cmdbuff的大小由alloc_cmdbuff根据plen分配，但p的来源（get_histentry）是外部历史数据，... |
| 735 | vim-9.1.1591 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 879 | TP | TP | 代码使用STRCPY（即strcpy）将动态长度的字符串p复制到固定大小的缓冲区ccline.cmdbuff中，虽然之前调用了realloc_cmdbuff(len + 1)来调整缓冲区大小，但该函数内部使用alloc_cmdbuff... |
| 736 | vim-9.1.1591 | vim_settempdir | cpp/unbounded-write | 5293 | TP | TP | 代码使用STRCPY（即strcpy）将参数tempdir直接复制到固定大小的缓冲区buf中，而tempdir是外部传入的路径字符串，其长度未经验证。缓冲区buf的大小为MAXPATHL+2，若tempdir长度超过MAXPATHL，... |
| 738 | vim-9.1.1591 | buf_modname | cpp/unbounded-write | 3643 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的fname复制到新分配的retval缓冲区，若fnamelen大于目标缓冲区大小（由alloc分配）将导致缓冲区溢出。切片中未见对fname长度的前置校验或使用安全函数。 |
| 740 | vim-9.1.1591 | concat_fnames | cpp/unbounded-write | 3134 | TP | TP | 代码使用STRCPY（即strcpy）将fname1复制到新分配的缓冲区dest，但未对fname1的长度进行任何检查。虽然dest的大小已根据fname1和fname2的长度计算分配，但若fname1在分配后、复制前被外部修改或本身... |
| 741 | vim-9.1.1591 | concat_fnames | cpp/unbounded-write | 3137 | TP | TP | 函数`concat_fnames`使用`alloc`分配缓冲区，其大小为`STRLEN(fname1) + STRLEN(fname2) + 3`，随后使用`STRCAT(dest, fname2)`进行拼接。虽然分配大小考虑了源字符... |
| 742 | vim-9.1.1591 | uniquefy_paths | cpp/unbounded-write | 2568 | TP | TP | 代码中使用了不安全的 STRCPY（即 strcpy）宏，将长度未知的 pattern 字符串复制到固定大小的缓冲区 file_pattern 中，存在缓冲区溢出风险。pattern 的来源在切片中未明确限制，因此该告警是真实的安全问题。 |
| 743 | vim-9.1.1591 | uniquefy_paths | cpp/unbounded-write | 2685 | TP | TP | 代码在行 `STRCPY(fnames[i], short_name);` 处使用 `strcpy` 宏（即 `strcpy`）将 `short_name` 复制到 `fnames[i]` 指向的缓冲区。`short_name` 是 ... |
| 744 | vim-9.1.1591 | find_file_in_path_option | cpp/unbounded-write | 1911 | TP | TP | 代码中直接使用不安全的 STRCPY（即 strcpy）宏将 *file_to_find 复制到 NameBuff 缓冲区，而 NameBuff 的大小为 MAXPATHL，但 *file_to_find 的长度 file_to_fi... |
| 745 | vim-9.1.1591 | ff_check_visited | cpp/unbounded-write | 1537 | TP | TP | 代码使用STRCPY（即strcpy）将ff_expand_buffer.string复制到vp->ffv_fname，而目标缓冲区vp->ffv_fname的大小为ff_expand_buffer.length + 1，源字符串ff... |
| 746 | vim-9.1.1591 | <global> | cpp/unbounded-write | 3794 | TP | TP | 代码使用 `strcat` 将未经验证长度的字符串 `s` 追加到缓冲区 `r` 中，而 `r` 的分配大小虽然考虑了 `s` 的长度，但 `s` 的内容来自文件行，其长度可能超过分配时预留的空间，因为 `s` 在分配后可能已被修改或... |
| 747 | vim-9.1.1591 | foldDelMarker | cpp/unbounded-write | 1897 | TP | TP | 代码使用宏 STRCPY（即 strcpy）将源字符串 `p + len` 复制到目标缓冲区 `newline + (p - line)`，目标缓冲区大小 `alloc(ml_get_len(lnum) - len + 1)` 已根据... |
| 748 | vim-9.1.1591 | foldAddMarker | cpp/unbounded-write | 1815 | TP | TP | 代码使用STRCPY（即strcpy）将`line`复制到新分配的缓冲区`newline`，而`line`是从文件内容中读取的，其长度可能超过目标缓冲区大小。虽然`newline`的大小已根据`line_len`等计算，但若`line... |
| 749 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2899 | TP | TP | 代码使用STRCPY（即strcpy）将res_prolog->title复制到固定大小的buffer[256]中，而res_prolog->title是从外部资源文件读取的，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 750 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2901 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer追加内容，而buffer的大小为256字节。告警点处拼接的字符串（res_prolog->title和res_prolog->version）长度在切片中未显示受控... |
| 751 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2905 | TP | TP | 代码使用STRCPY（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而res_cidfont->title来自外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 752 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2907 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的源字符串（res_cidfont->title和res_cidfont->version）长度在切片中未显示受控，存在缓冲区溢出的风险。 |
| 753 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2912 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_cmap->title复制到固定大小的buffer[256]中，而res_cmap->title的来源是外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 754 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2914 | TP | TP | 代码使用STRCAT宏（即strcat）将资源文件的标题和版本号拼接至固定大小的缓冲区buffer（256字节），而标题和版本号的内容来自外部文件（通过prt_open_resource读取），其长度未经验证，存在缓冲区溢出风险。 |
| 755 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2920 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_encoding->title复制到固定大小的buffer[256]中，而res_encoding->title来源于外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 756 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2922 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer（256字节）追加内容，而追加的源字符串（res_encoding->title和res_encoding->version）来自外部资源文件，其长度未经验证，存在... |
| 757 | vim-9.1.1591 | prt_resource_name | cpp/unbounded-write | 1659 | TP | TP | 代码使用strcpy复制字符串，虽然存在长度检查，但检查对象是源字符串filename的长度，而非目标缓冲区resource_filename的大小。目标缓冲区大小未知，存在缓冲区溢出风险。 |
| 758 | vim-9.1.1591 | do_helptags | cpp/unbounded-write | 1210 | TP | TP | 代码中直接使用 STRCPY（即 strcpy）将未知长度的 `dirname` 参数复制到固定大小的 `NameBuff` 缓冲区，存在缓冲区溢出风险。`dirname` 来自函数参数，其长度未在切片内进行验证或限制。 |
| 759 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 975 | TP | TP | 代码使用STRCAT宏（即strcat）向NameBuff缓冲区拼接未经验证长度的字符串ext和tagfname，这些字符串来自函数参数，可能导致缓冲区溢出，因为NameBuff的大小未在切片中显示，且没有边界检查。 |
| 760 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 991 | TP | TP | 代码使用STRCAT宏（即strcat）将tagfname拼接到NameBuff中，而NameBuff是一个固定大小的缓冲区（MAXPATHL），但tagfname作为函数参数，其长度未在切片内进行任何检查或限制，存在缓冲区溢出风险。 |
| 761 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 1112 | TP | TP | 代码使用 sprintf 将动态长度的字符串 p1 和 fname 写入固定大小的缓冲区 s，其中 s 的分配大小为 (p2 - p1 + STRLEN(fname) + 2)，但 sprintf 未限制写入长度，若 p1 或 fna... |
| 763 | vim-9.1.1591 | load_colors | cpp/unbounded-write | 609 | TP | TP | 代码使用`sprintf`将用户控制的`name`参数拼接到固定大小的缓冲区`buf`中，而`buf`的大小仅为`STRLEN(name) + 12`，未考虑格式化字符串`"colors/%s.vim"`本身增加的额外长度，存在缓冲区... |
| 770 | vim-9.1.1591 | ins_compl_infercase_gettext | cpp/unbounded-write | 723 | TP | TP | 代码使用STRCPY（即strcpy）将IObuff的内容复制到gap.ga_data中，但未检查IObuff的长度是否超过gap.ga_data的容量。虽然gap.ga_data通过ga_grow分配，但STRCPY调用前未确保目标... |
| 771 | vim-9.1.1591 | <global> | cpp/unbounded-write | 3140 | TP | TP | 代码使用`sprintf`将`transchar(from)`的结果写入固定大小的缓冲区`args->os_errbuf`，而`transchar`的返回值长度未知，可能导致缓冲区溢出。切片中未显示对`args->os_errbuf`... |
| 772 | vim-9.1.1591 | findswapname | cpp/unbounded-write | 4967 | TP | TP | 代码使用 STRCPY（即 strcpy）将 fname 复制到新分配的 fname2 缓冲区，而 fname2 的大小为 n+2，fname 的长度为 n。虽然缓冲区大小足够容纳源字符串，但 strcpy 本身不检查边界，且告警提示... |
| 774 | vim-9.1.1591 | <global> | cpp/unbounded-write | 811 | TP | TP | 代码中直接使用宏 STRCPY（即 strcpy）将 call_data 复制到新分配的缓冲区，未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 775 | vim-9.1.1591 | <global> | cpp/unbounded-write | 815 | TP | TP | 代码中直接使用宏 STRCPY（即 strcpy）将 call_data 复制到固定大小的缓冲区 menu->strings[i] 中，而 call_data 是外部传入的字符串，其长度未经验证，存在缓冲区溢出风险。 |
| 776 | vim-9.1.1591 | msg_show_console_dialog | cpp/unbounded-write | 4505 | TP | TP | 代码使用宏 STRCPY（即 strcpy）将 `message` 参数复制到新分配的缓冲区 `confirm_msg + 1` 处，未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 777 | vim-9.1.1591 | str2specialbuf | cpp/unbounded-write | 2015 | TP | TP | 代码在调用STRCAT（即strcat）前，仅检查了`s`和`buf`当前字符串长度之和是否小于`len`，但未考虑strcat操作后目标缓冲区`buf`的总长度（包括终止符）可能超过其分配的大小`len`，存在缓冲区溢出的风险。 |
| 778 | vim-9.1.1591 | get_emsg_source | cpp/unbounded-write | 500 | TP | TP | 代码使用`sprintf`将`sname`格式化到`Buf`中，`Buf`的大小为`STRLEN(sname) + STRLEN(p)`，但`sprintf`写入的字符串长度是格式化后的总长度（包含静态字符串`p`和变量`sname`... |
| 780 | vim-9.1.1591 | expand_env_esc | cpp/unbounded-write | 1678 | TP | TP | 代码在调用STRCPY（即strcpy）前，仅检查了源字符串长度与剩余目标缓冲区长度，但未验证目标缓冲区`dst`的原始大小，存在缓冲区溢出的风险。环境变量`var`的内容可能超过`dst`指向的缓冲区容量。 |
| 783 | vim-9.1.1591 | push_showcmd | cpp/unbounded-write | 1809 | TP | TP | 代码使用不安全的strcpy函数将内容从showcmd_buf复制到old_showcmd_buf，未检查目标缓冲区大小，存在缓冲区溢出风险。告警规则正确识别了此问题。 |
| 785 | vim-9.1.1591 | op_change | cpp/unbounded-write | 2003 | TP | TP | 代码中直接使用宏 STRCPY（即 strcpy）将源字符串 oldp + bd.textcol 复制到目标缓冲区 newp + newlen + ins_len，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 786 | vim-9.1.1591 | op_replace | cpp/unbounded-write | 1299 | TP | TP | 代码中直接使用不安全的 STRCPY（即 strcpy）宏，将源字符串 oldp + bd.textcol + bd.textlen 复制到目标缓冲区 newp + newlen + bd.endspaces，未检查目标缓冲区大小，存... |
| 787 | vim-9.1.1591 | op_replace | cpp/unbounded-write | 1308 | TP | TP | 代码中直接使用 STRCPY（即 strcpy）宏将未知长度的源字符串（oldp + bd.textcol + bd.textlen）复制到固定大小的目标缓冲区（after_p），未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 788 | vim-9.1.1591 | op_delete | cpp/unbounded-write | 962 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将源字符串复制到新分配的缓冲区，未检查源字符串长度是否小于目标缓冲区大小。目标缓冲区`newp`的大小为`ml_get_len(lnum) + 1 - n`，而源字符串`oldp + bd... |
| 789 | vim-9.1.1591 | block_insert | cpp/unbounded-write | 743 | TP | TP | 代码使用STRCPY（即strcpy）将字符串oldp复制到缓冲区newp + offset处，未检查目标缓冲区剩余空间，且oldp是来自ml_get的原始行内容，其长度可能超过目标位置到newp末尾的剩余容量，存在缓冲区溢出风险。 |
| 790 | vim-9.1.1591 | option_value2string | cpp/unbounded-write | 8459 | TP | TP | 代码中直接使用不安全的STRCPY（即strcpy）宏，将get_special_key_name等函数的返回值复制到固定大小的NameBuff缓冲区，未检查源字符串长度，存在缓冲区溢出风险。 |
| 791 | vim-9.1.1591 | option_value2string | cpp/unbounded-write | 8461 | TP | TP | 代码在多个分支中直接使用不安全的STRCPY（即strcpy）宏向固定大小的缓冲区NameBuff复制数据，且未对源字符串长度进行限制。例如，在`wc_use_keyname`和`transchar`返回的字符串长度可能超过NameB... |
| 792 | vim-9.1.1591 | stropt_expand_envvar | cpp/unbounded-write | 1803 | TP | TP | 代码使用STRCPY（即strcpy）将`s`的内容复制到`newval`中，而`newval`的大小`newlen`是根据`s`和`origval`的长度计算分配的。虽然分配了足够空间，但strcpy本身不检查目标缓冲区大小，若`s... |
| 793 | vim-9.1.1591 | mch_expand_wildcards | cpp/unbounded-write | 7445 | TP | TP | 代码在循环中使用宏 STRCPY（即 strcpy）将文件名复制到新分配的缓冲区 p 中，而 p 的大小为 STRLEN((*file)[i]) + 1 + dir，仅比源字符串长度多 1 或 2 个字节，未考虑目标缓冲区大小限制。s... |
| 794 | vim-9.1.1591 | mch_FullName | cpp/unbounded-write | 2846 | TP | TP | 代码在调用STRCPY（即strcpy）前，仅通过`(int)(buflen + STRLEN(fname)) >= len`检查了目标缓冲区总长度，但未对源字符串`fname`的长度进行独立验证，且`fname`可能来自外部输入（如... |
| 795 | vim-9.1.1591 | qf_store_title | cpp/unbounded-write | 1940 | TP | TP | 代码使用strcpy将外部传入的title字符串复制到新分配的内存中，虽然分配的大小为STRLEN(title)+2，但strcpy本身不检查目标缓冲区大小，若title不是以空字符结尾的字符串，将导致缓冲区溢出。切片中未显示对tit... |
| 796 | vim-9.1.1591 | reg_submatch | cpp/unbounded-write | 2723 | TP | TP | 代码在多个位置使用STRCPY（即strcpy）宏，将长度未知的源字符串（如从reg_getline_submatch获取的行内容）复制到固定大小的缓冲区retval中，而retval的分配大小len是基于源字符串内容计算的，但str... |
| 797 | vim-9.1.1591 | reg_submatch | cpp/unbounded-write | 2732 | TP | TP | 代码在循环中使用 STRCPY（即 strcpy）宏将 reg_getline_submatch 返回的字符串复制到 retval 缓冲区，但未检查目标缓冲区 retval 的大小，而源字符串长度由外部输入（文件行内容）决定，可能导致... |
| 798 | vim-9.1.1591 | regtilde | cpp/unbounded-write | 1959 | TP | TP | STRCPY 宏展开为 strcpy，其目标缓冲区 tmpsub 的大小为 tmpsublen+1，源字符串 postfix 的长度未知，若 postfixlen 计算错误或 postfix 未正确终止，可能导致缓冲区溢出。切片中未显... |
| 799 | vim-9.1.1591 | match_with_backref | cpp/unbounded-write | 1600 | TP | TP | 代码使用STRCPY（即strcpy）将长度未知的源字符串rex.line复制到固定大小的缓冲区reg_tofree中，虽然reg_tofree的大小会根据rex.line的长度动态分配，但分配后立即执行复制，未检查分配是否成功或大小... |
| 800 | vim-9.1.1591 | get_reg_contents | cpp/unbounded-write | 2743 | TP | TP | 代码使用宏 STRCPY（即 strcpy）将 y_current->y_array[i].string 复制到目标缓冲区 retval + len，而目标缓冲区 retval 的大小由 alloc(len + 1) 分配，其长度 l... |
| 801 | vim-9.1.1591 | do_put | cpp/unbounded-write | 2166 | TP | TP | 代码中直接使用 STRCPY 宏（即 strcpy）将 y_array[y_size - 1].string 复制到固定大小的缓冲区 newp，而 newp 的大小为 ml_get_len(lnum) - col + totlen +... |
| 802 | vim-9.1.1591 | do_put | cpp/unbounded-write | 2167 | TP | TP | 代码中直接使用 STRCPY 宏（即 strcpy）将 y_array[i].string 复制到固定大小的缓冲区 newp 中，而 y_array[i].string 的长度 yanklen 可能超过目标缓冲区剩余空间，存在缓冲区溢... |
| 803 | vim-9.1.1591 | op_yank | cpp/unbounded-write | 1318 | TP | TP | 代码使用宏 STRCPY（即 strcpy）将两个字符串拼接至新分配的内存 pnew 中，但未检查目标缓冲区大小。虽然 pnew 的大小已根据两个源字符串的长度之和加1计算，但若源字符串长度在分配后被修改（如并发场景），或源字符串未正... |
| 804 | vim-9.1.1591 | op_yank | cpp/unbounded-write | 1319 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）拼接两个字符串，目标缓冲区pnew的大小是两者长度之和加1，但拼接时未检查目标缓冲区边界，存在缓冲区溢出风险。 |
| 805 | vim-9.1.1591 | stuff_yank | cpp/unbounded-write | 471 | TP | TP | 代码使用不安全的STRCPY（即strcpy）宏，将源字符串（pp->string）复制到新分配的目标缓冲区（tmp），未检查目标缓冲区大小。虽然tmp的大小（tmplen + 1）是根据源字符串长度（pp->length）和输入长度... |
| 806 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2850 | TP | TP | 函数`autoload_name`中，目标缓冲区`scriptname`的大小通过`alloc(STRLEN(name) + 14)`分配，但后续的`STRCAT`调用可能拼接一个修改后的`name`字符串（可能跳过前两个字符），其长... |
| 807 | vim-9.1.1591 | ExpandPackAddDir | cpp/unbounded-write | 1321 | TP | TP | sprintf 的目标缓冲区 s 的大小为 pat_len + 26，但格式化字符串 'pack/*/opt/%s*' 中的 %s 直接使用了未经验证的外部输入 pat，其长度可能超过 pat_len，导致缓冲区溢出。 |
| 808 | vim-9.1.1591 | sign_jump | cpp/unbounded-write | 1313 | TP | TP | sprintf 使用未限制长度的缓冲区 buf->b_fname 作为输入，且目标缓冲区 cmd 的大小仅基于 buf->b_fname 的当前长度加上固定偏移分配，无法防御 buf->b_fname 内容被恶意修改或包含超长路径导致... |
| 809 | vim-9.1.1591 | dump_word | cpp/unbounded-write | 4187 | TP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或环境变量等外部数据，且切片中未显示对p的长度进行任何校验，存在缓冲区溢出风险。 |
| 810 | vim-9.1.1591 | make_case_word | cpp/unbounded-write | 3140 | TP | TP | 代码中直接使用不安全的strcpy宏复制字符串，未检查目标缓冲区cword的大小，而源字符串fword可能来自多个不受控的输入源（如环境变量、文件读取），存在缓冲区溢出风险。 |
| 811 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2998 | TP | TP | 代码使用 STRCPY（即 strcpy）将 repl_to 复制到新分配的缓冲区 p 中，未检查目标缓冲区大小，而 repl_to 是全局变量，其长度可能超过目标缓冲区 p 的剩余空间，存在缓冲区溢出风险。 |
| 812 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2999 | TP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p的末尾，但p的大小为ml_get_curline_len() + addlen + 1，而源字符串来自当前行的剩余部分，其长度未经验证，可能导致缓冲区溢出。 |
| 813 | vim-9.1.1591 | count_common_word | cpp/unbounded-write | 1919 | TP | TP | 代码使用STRCPY（即strcpy）将字符串p复制到wc->wc_word，而p的来源是用户输入参数word或经过vim_strncpy处理的buf，其长度未经验证。目标缓冲区wc->wc_word的大小为STRLEN(p) + 1... |
| 814 | vim-9.1.1591 | spell_load_lang | cpp/unbounded-write | 1632 | TP | TP | 代码使用STRCPY（即strcpy）将参数lang直接复制到固定大小的数组sl.sl_lang中，但切片未显示对lang的长度有任何校验或限制，存在缓冲区溢出风险。 |
| 815 | vim-9.1.1591 | spell_move_to | cpp/unbounded-write | 1420 | TP | TP | 代码使用STRCPY宏（即strcpy）将line复制到buf，而buf的大小buflen是根据len + MAXWLEN + 2动态分配的。虽然分配时考虑了MAXWLEN的额外空间，但strcpy本身不检查目标缓冲区大小，若line... |
| 817 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2369 | TP | TP | 代码中在告警行（STRCAT(p, items[0]);）使用strcat拼接字符串，但目标缓冲区p的大小是通过动态计算分配的，其大小仅基于spin->si_info、items[0]和items[1]的长度之和，未考虑strcat可... |
| 818 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2371 | TP | TP | 代码中明确存在对 `STRCAT(p, items[1])` 的调用，其中 `items[1]` 来自文件行读取，长度未经验证，而目标缓冲区 `p` 的大小仅通过 `STRLEN(spin->si_info) + STRLEN(ite... |
| 819 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2464 | TP | TP | 代码中直接使用STRCPY(p, items[1])将items[1]（来自文件行的字符串）复制到缓冲区p，而p的大小仅为STRLEN(items[1]) + 2，未检查items[1]的长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 820 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2495 | TP | TP | 代码中在拼接字符串时使用了不安全的STRCAT宏（即strcat），目标缓冲区p的大小由动态计算的长度分配，但拼接的源字符串items[1]来自外部文件读取，若其长度超过缓冲区剩余空间，将导致缓冲区溢出。 |
| 821 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2644 | TP | TP | 代码中明确存在对 `STRCPY(p, spin->si_info)` 的调用，其中 `p` 指向通过 `getroom` 分配的内存，其大小由 `spin->si_info` 和 `items[0]`、`items[1]` 的长度计... |
| 822 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2746 | TP | TP | 代码中直接使用 sprintf 将 items[4] 拼接到 buf 中，而 items[4] 来自外部文件读取的未经验证的用户输入，可能导致缓冲区溢出。切片中未显示对 items[4] 长度的检查或防护。 |
| 823 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2748 | TP | TP | 代码中直接使用 sprintf 将 items[4] 的内容格式化到固定大小的缓冲区 buf 中，items[4] 来自外部文件读取，未进行长度检查，存在缓冲区溢出风险。 |
| 824 | vim-9.1.1591 | add_sound_suggest | cpp/unbounded-write | 3243 | TP | TP | 代码中直接使用 STRCPY（即 strcpy）宏将 goodword 复制到 sft->sft_word，而 goodword 是函数参数，其长度可能超过 sft_word 的目标缓冲区大小（缓冲区大小由 offsetof(sftw... |
| 825 | vim-9.1.1591 | suggest_try_change | cpp/unbounded-write | 1199 | TP | TP | 代码中直接使用 STRCPY（即 strcpy）将 su->su_fbadword 复制到固定大小的数组 fword[MAXWLEN] 中，未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 829 | vim-9.1.1591 | expand_tag_fname | cpp/unbounded-write | 4141 | TP | TP | 代码使用 STRCPY（即 strcpy）将 tag_fname 复制到固定大小的缓冲区 retval（大小为 MAXPATHL），而 tag_fname 的来源包括环境变量、文件读取等外部输入，其长度未经验证，存在缓冲区溢出风险。 |
| 830 | vim-9.1.1591 | get_tagfname | cpp/unbounded-write | 3436 | TP | TP | 代码在行 `STRCPY(buf, fname);` 处使用 `strcpy` 将 `fname` 复制到 `buf`，而 `buf` 是参数，大小为 `MAXPATHL` 字符。`fname` 来自 `vim_findfile` 函... |
| 831 | vim-9.1.1591 | findtags_add_match | cpp/unbounded-write | 2625 | TP | TP | 代码中直接使用STRCPY（即strcpy）宏，将st->help_lang复制到固定偏移的缓冲区p中，而st->help_lang是环境变量来源的字符串，其长度未经验证，可能导致缓冲区溢出。 |
| 832 | vim-9.1.1591 | findtags_add_match | cpp/unbounded-write | 2704 | TP | TP | 代码中多次使用STRCPY（即strcpy）宏，将来源未知或长度未经验证的外部数据（如st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区mfp中，存在缓冲区溢出的风险。切片中未显示对这些源字符串... |
| 833 | vim-9.1.1591 | show_one_termcode | cpp/unbounded-write | 7054 | TP | TP | 代码使用STRCPY（即strcpy）将get_special_key_name返回的字符串p复制到IObuff+5位置，而IObuff是固定大小的数组，p的长度可能超过目标缓冲区剩余空间，存在缓冲区溢出风险。 |
| 834 | vim-9.1.1591 | current_tagblock | cpp/unbounded-write | 1392 | TP | TP | 代码使用`sprintf`将用户控制的字符串`p`和长度`len`写入固定大小的缓冲区`spat`和`epat`，缓冲区大小仅由`len`加上一个固定常量决定，若`len`值过大或`p`内容不可控，可能导致缓冲区溢出。切片中未见对`l... |
| 835 | vim-9.1.1591 | uc_check_code | cpp/unbounded-write | 1810 | TP | TP | 代码在多个分支中直接使用STRCPY（即strcpy）将来源未知或外部输入（如eap->arg）复制到固定大小的缓冲区buf中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 836 | vim-9.1.1591 | fname_trans_sid | cpp/unbounded-write | 2278 | TP | TP | 代码在条件`fnamelen < FLEN_FIXED`下，使用`STRCPY`（即`strcpy`）将`script_name`复制到`fname_buf`的偏移位置，未检查目标缓冲区`fname_buf`的剩余空间是否足够，存在缓... |
| 838 | vim-9.1.1591 | exec_instructions | cpp/unbounded-write | 3929 | TP | TP | 代码中使用了不安全的STRCPY宏（即strcpy），将未经验证长度的字符串复制到固定大小的缓冲区中，存在缓冲区溢出风险。告警指向的多个数据源（环境变量、文件读取等）都可能提供超长输入，导致目标缓冲区溢出。 |
| 839 | vim-9.1.1591 | generate_PUSHFUNC | cpp/unbounded-write | 1042 | TP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到固定大小的缓冲区`funcname`中，而`funcname`的大小仅为`STRLEN(name) + 3`，未考虑strcpy会复制结尾空字符，导致目标缓冲区缺少一个... |
| 840 | vim-9.1.1591 | update_vim9_script_var | cpp/unbounded-write | 947 | TP | TP | 代码使用 STRCPY（即 strcpy）将 `name` 字符串复制到固定大小的 `newsav->sav_key` 缓冲区，而 `newsav` 的分配大小仅基于 `STRLEN(name) + 1`，未预留额外空间，若 `nam... |
| 841 | vim-9.1.1591 | find_exported | cpp/unbounded-write | 756 | TP | TP | 代码使用`sprintf`将外部可控的`script->sn_autoload_prefix`和`name`拼接到固定大小的缓冲区`funcname`中，而`funcname`的大小仅由`len`决定，`len`的计算包含了这些外部字... |
| 842 | vim-9.1.1591 | find_exported | cpp/unbounded-write | 763 | TP | TP | sprintf 使用不受控的 `name` 参数和 `sid` 格式化字符串，目标缓冲区 `funcname` 的大小由 `len` 计算，但 `len` 的计算包含了 `name` 的长度，而 `name` 是外部传入的变量，其长度... |
| 843 | vim-9.1.1591 | xxdline | cpp/unbounded-write | 600 | TP | TP | 函数`xxdline`中，`strcpy(z, l)`的目标缓冲区`z`是固定大小的静态数组`z[LLEN_NO_COLOR+1]`，而源字符串`l`是函数参数，其长度未在切片内进行任何校验或限制，存在缓冲区溢出风险。 |
| 844 | vim-9.1.1591 | ExpandBufnames | cpp/invalid-pointer-deref | 2980 | TP | TP | 在循环中，`(*file)[count++] = p;` 这一行对指针 `*file` 进行了写入。`*file` 在函数开头被初始化为 NULL，并且在 `round == 1` 且 `*file == NULL` 时，代码会提前返... |
| 845 | vim-9.1.1591 | update_snapshot | cpp/invalid-pointer-deref | 2075 | TP | TP | 在宽度为2的双宽度字符处理中，代码执行 `p[pos.col + 1] = p[pos.col];`，但 `p` 是通过 `ALLOC_MULT(cellattr_T, len)` 分配的，长度为 `len`。当 `pos.col` ... |
| 1583 | redis-7.2.5 | auxHumanNodenameSetter | Dereference of null pointer | 281 | TP | TP | 在 `if (n)` 条件为假的分支中，代码直接访问 `n->human_nodename` 以调用 `sdslen`，此时 `n` 为 NULL，导致对空指针的解引用，构成逻辑错误。 |

### 5.2 一致：算法=FP，LLM=FP（共 2144 条）

> 算法与 LLM 均判定为假阳性（False Positive）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 1 | ffmpeg-6.1.1 | upcase_string | cpp/offset-use-before-range-check | 1053 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了只有当 `i` 小于 `dst_size-1` 且 `src[i]` 不为空字符时才会进入循环体，循环结束后 `i` 的值要么等于 `dst_size-1`，要么指... |
| 2 | ffmpeg-6.1.1 | capture_screen | cpp/offset-use-before-range-check | 479 | FP | FP | 在 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 循环中，条件 `j < tab` 确保了 `j` 在访问 `row[j]` 和 `c... |
| 3 | ffmpeg-6.1.1 | capture_screen | cpp/offset-use-before-range-check | 479 | FP | FP | 在告警所在行 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 中，对变量 `j` 的访问已包含范围检查 `j < tab`，且 `tab... |
| 4 | ffmpeg-6.1.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 告警所在行的循环条件 `i<w_r` 已对索引 `i` 进行了范围检查，确保 `dst[i]` 的访问不会越界。切片代码中 `w_r` 的计算 (`w2 - 1`) 和循环逻辑表明访问是安全的。 |
| 5 | ffmpeg-6.1.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警行使用变量 `i` 的循环条件 `i<w_r` 中，`i` 已与 `w_r` 进行了范围检查，确保了 `i` 在访问数组 `temp[i]` 和 `src[i]` 时不会越界。因此该告警为误报。 |
| 6 | ffmpeg-6.1.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | FP | 在 while 循环条件 `(entries[m].flags & AVINDEX_DISCARD_FRAME) && m < b && m < nb_entries - 1` 中，对 `m` 的访问 `entries[m]` 发生在... |
| 7 | ffmpeg-6.1.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 215 | FP | FP | 在for循环条件 `i < q->nb_subs` 的保护下，循环体内访问 `q->subs[i]` 和 `q->subs[i + 1]` 是安全的。对 `q->subs[i + 1]` 的访问仅在 `i < q->nb_subs -... |
| 8 | ffmpeg-6.1.1 | choose_out_timebase | cpp/inconsistent-null-check | 1850 | FP | FP | 函数 `frame_data` 在 `frame->opaque_ref` 为空时会分配内存，若分配失败则返回 NULL。但在调用点 `choose_out_timebase` 中，后续代码仅通过 `fd->dec.tb` 访问 `f... |
| 9 | ffmpeg-6.1.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | 函数 `skip_space` 内部仅进行简单的指针递增，不会返回空指针，其返回值始终是有效的字符串指针。告警所提示的“未检查空值”在此上下文中不构成安全问题，属于工具误报。 |
| 10 | ffmpeg-6.1.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | FP | 函数 `ff_iir_filter_init_state` 的返回值直接返回给调用者，由调用者负责检查分配是否成功。这是库函数中常见的模式，将内存分配错误的处理责任上移，因此工具报告的未检查空指针问题在此上下文中是误报。 |
| 11 | ffmpeg-6.1.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1392 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 12 | ffmpeg-6.1.1 | intercept_id3 | cpp/inconsistent-null-check | 1185 | FP | FP | 函数`current_segment`的返回值`seg`在后续代码中仅作为参数传递给`read_from_url`，而`read_from_url`内部已通过`FFMIN`宏和`seg->size`检查对读取大小进行了安全限制，且`s... |
| 13 | ffmpeg-6.1.1 | get_frag_time | cpp/inconsistent-null-check | 1383 | FP | FP | 告警点位于条件分支 `if (sc->has_sidx)` 内部，而 `get_frag_stream_info` 函数在参数无效时会返回 NULL。但切片代码显示，在调用 `get_frag_stream_info` 后，代码立即访... |
| 14 | ffmpeg-6.1.1 | init_muxer | cpp/inconsistent-null-check | 189 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，仅将 `AVOutputFormat*` 转换为 `const FFOutputFormat*`，其返回值不可能为 NULL，因此无需进行空指针检查。 |
| 15 | ffmpeg-6.1.1 | url_alloc_for_protocol | cpp/unbounded-write | 101 | FP | FP | 目标缓冲区 `uc->filename` 的大小通过 `strlen(filename) + 1` 精确分配，与源字符串 `filename` 长度匹配，`strcpy` 操作不会导致缓冲区溢出。 |
| 16 | ffmpeg-7.1.1 | upcase_string | cpp/offset-use-before-range-check | 1109 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了只有当 `i` 小于 `dst_size-1` 且 `src[i]` 不为空字符时才会进入循环体，循环结束后 `i` 的值要么等于 `dst_size-1`，要么指... |
| 17 | ffmpeg-7.1.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在警告所在行，`j` 的使用前已通过 `j < tab` 条件进行了范围检查，且 `j` 在循环前被初始化为0，其递增逻辑确保了访问安全，因此该告警为误报。 |
| 18 | ffmpeg-7.1.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警所在行的while循环条件中，已经包含了对变量j的范围检查'j < tab'，确保了j不会越界访问数组，因此该告警是误报。 |
| 19 | ffmpeg-7.1.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码显示，在循环条件 `for(; (((x86_reg)&dst[i]) & 0x1F) && i<w_r; i++)` 中，对索引 `i` 的使用（`&dst[i]`）与范围检查 `i<w_r` 位于同一条件表达式中，且通过逻... |
| 20 | ffmpeg-7.1.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警所在的循环条件 `for(; (((x86_reg)&temp[i]) & 0x1F) && i<w_r; i++)` 中，对索引 `i` 的使用（`temp[i]`）之前已经通过 `i<w_r` 进行了范围检查，... |
| 21 | ffmpeg-7.1.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 148 | FP | FP | 切片代码显示，在访问 `entries[m]` 之前，循环条件 `m < b && m < nb_entries - 1` 已经对 `m` 进行了范围检查，确保了 `m` 不会越界访问数组。因此，该告警是误报。 |
| 22 | ffmpeg-7.1.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 223 | FP | FP | 切片代码显示，在访问 `q->subs[i + 1]` 之前，已通过条件 `i < q->nb_subs - 1` 进行了明确的数组边界检查，确保了 `i+1` 是有效索引，因此不存在越界访问风险。 |
| 23 | ffmpeg-7.1.1 | enc_open | cpp/inconsistent-null-check | 189 | FP | FP | 告警点对 `av_frame_side_data_desc` 的返回值进行了间接的空指针检查。代码在 `if (!(desc->props & AV_SIDE_DATA_PROP_GLOBAL))` 中直接解引用 `desc`，这隐含... |
| 24 | ffmpeg-7.1.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部仅进行简单的空格遍历，不涉及内存分配或可能失败的复杂操作，其返回值不可能为NULL。因此，未检查其返回值是安全的，告警为误报。 |
| 25 | ffmpeg-7.1.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | FP | 函数 `ff_iir_filter_init_state` 的职责是分配并初始化状态结构体，其返回值由调用者检查。切片代码显示，该函数直接返回了 `av_mallocz` 的结果，这是典型的资源分配函数模式，内存分配失败的处理责任应由... |
| 26 | ffmpeg-7.1.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1461 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 27 | ffmpeg-7.1.1 | hls_read_header | cpp/inconsistent-null-check | 2158 | FP | FP | 代码中 `in_fmt` 变量在后续的 `avformat_open_input` 调用中被直接使用，但切片显示该调用会检查返回值（`ret < 0`），且 `in_fmt` 仅在特定条件分支中通过 `av_find_input_fo... |
| 28 | ffmpeg-7.1.1 | intercept_id3 | cpp/inconsistent-null-check | 1240 | FP | FP | 代码切片显示，`seg` 指针在后续使用前（如 `seg->size`）已通过 `seg->size >= 0` 等条件进行了间接校验，且 `read_from_url` 函数内部也安全地处理了 `seg` 参数，未出现空指针解引用。... |
| 29 | ffmpeg-7.1.1 | init_muxer | cpp/inconsistent-null-check | 190 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，仅对传入的指针进行强制类型转换，不会返回空指针。代码中多处直接使用其返回值 `of` 访问成员，表明开发者信任其非空，这是安全的。 |
| 30 | ffmpeg-7.1.1 | cmp_dm_level0 | cpp/overflow-buffer | 294 | FP | FP | memcmp 操作的大小是通过 `sizeof(AVDOVIColorMetadata) - offsetof(AVDOVIColorMetadata, signal_eotf)` 计算得出的，这确保了比较范围严格限定在结构体 `si... |
| 31 | ffmpeg-7.1.1 | url_alloc_for_protocol | cpp/unbounded-write | 146 | FP | FP | 目标缓冲区 uc->filename 的大小通过 `strlen(filename) + 1` 精确分配，与源字符串长度匹配，因此 `strcpy` 操作是安全的，不会发生缓冲区溢出。 |
| 32 | ffmpeg-7.0.1 | upcase_string | cpp/offset-use-before-range-check | 1108 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了只有当 `i` 小于 `dst_size-1` 且 `src[i]` 不为空时才会进入循环体，循环结束后 `i` 的值要么等于 `dst_size-1`，要么指向 ... |
| 33 | ffmpeg-7.0.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警行 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 中，变量 `j` 的访问已通过条件 `j < tab` 进行了范围检查，确保了... |
| 34 | ffmpeg-7.0.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警所在行，`j` 的使用前已通过 `j < tab` 条件进行了范围检查，该条件确保了循环在 `j` 达到 `tab` 值时终止，因此不存在越界访问的风险。 |
| 35 | ffmpeg-7.0.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 告警点位于循环条件 `i<w_r` 之前，该条件确保了循环内对 `dst[i]` 的访问不会越界。切片代码中 `w_r` 的计算（`w2 - 1`）和 `width` 的传递逻辑表明索引 `i` 在进入循环体前已受到范围检查的保护。 |
| 36 | ffmpeg-7.0.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警行使用变量 `i` 进行数组索引之前，`for` 循环的条件 `i<w_r` 已经对 `i` 的范围进行了检查，确保了索引不会越界。因此该告警是误报。 |
| 37 | ffmpeg-7.0.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | FP | 切片代码显示，在 while 循环条件 `(entries[m].flags & AVINDEX_DISCARD_FRAME) && m < b && m < nb_entries - 1` 中，对 `m` 的访问 `entries[... |
| 38 | ffmpeg-7.0.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 215 | FP | FP | 在for循环条件 `i < q->nb_subs` 的保护下，访问 `q->subs[i]` 和 `q->subs[i + 1]` 是安全的。条件 `i < q->nb_subs - 1` 进一步确保了 `i + 1` 不会越界，因此... |
| 39 | ffmpeg-7.0.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | 函数 `skip_space` 内部仅进行简单的空格遍历，不涉及内存分配或可能失败的复杂操作，其返回值不可能为 NULL。代码逻辑上无需检查其返回值，告警为误报。 |
| 40 | ffmpeg-7.0.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | FP | 函数 `ff_iir_filter_init_state` 的职责是分配并初始化状态结构体，其返回值由调用者检查是更合理的模式。切片代码显示该函数直接返回了分配结果，符合许多库函数（如 `malloc`）的设计惯例，将空指针检查的责任... |
| 41 | ffmpeg-7.0.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1455 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 42 | ffmpeg-7.0.1 | hls_read_header | cpp/inconsistent-null-check | 2107 | FP | FP | 代码在调用 av_find_input_format 后，其返回值 in_fmt 仅在后续条件分支中用于访问 in_fmt->name，且该访问被严格限制在 seg && seg->key_type == KEY_SAMPLE_AES... |
| 43 | ffmpeg-7.0.1 | intercept_id3 | cpp/inconsistent-null-check | 1190 | FP | FP | 函数`current_segment`的返回值`seg`在后续代码中仅作为参数传递给`read_from_url`，而`read_from_url`内部已通过`if (seg->size >= 0)`等代码对`seg`进行了访问，这表... |
| 45 | ffmpeg-7.0.1 | init_muxer | cpp/inconsistent-null-check | 189 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，仅执行指针转换，不可能返回空指针。因此，调用结果无需进行空值检查，告警属于误报。 |
| 46 | ffmpeg-7.0.1 | url_alloc_for_protocol | cpp/unbounded-write | 145 | FP | FP | 目标缓冲区 uc->filename 的大小通过 `strlen(filename) + 1` 精确分配，与源字符串长度匹配，strcpy 操作不会导致缓冲区溢出。 |
| 47 | ffmpeg-7.1 | upcase_string | cpp/offset-use-before-range-check | 1109 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了只有当 `i` 小于 `dst_size-1` 且 `src[i]` 不为空时才会进入循环体，循环结束后 `i` 的值要么等于 `dst_size-1`，要么指向 ... |
| 48 | ffmpeg-7.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警所在行，变量 `j` 在循环条件 `j < tab` 中已被检查，确保其值小于 `tab`。`tab` 的值在第一个循环中计算，且 `j` 的初始值为0，循环条件保证了 `j` 的使用在有效范围内，因此不存在越界风险。 |
| 49 | ffmpeg-7.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在警告所在行的while循环条件中，变量j的使用（row[j]和charset[j]）已经与范围检查（j < tab）结合在同一条件表达式中，因此j的访问是受控的，不存在先于范围检查使用的问题。 |
| 50 | ffmpeg-7.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 告警所在行的循环条件 `i<w_r` 已对变量 `i` 进行了范围检查，确保 `i` 在访问数组 `dst` 和 `b` 时不会越界。切片代码中的逻辑是安全的。 |
| 51 | ffmpeg-7.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警所在的for循环条件中，变量'i'的使用（`i<w_r`）与其范围检查（`i<w_r`）是同时进行的，不存在先使用后检查的逻辑。循环条件确保了'i'在访问数组前已通过范围检查，因此是安全的。 |
| 52 | ffmpeg-7.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 148 | FP | FP | 在while循环条件 `m < b && m < nb_entries - 1` 中，对变量 `m` 的访问 `entries[m]` 发生在对其索引范围 `m < nb_entries` 的检查之前。然而，循环条件 `m < b` ... |
| 53 | ffmpeg-7.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 223 | FP | FP | 循环条件 `i < q->nb_subs` 确保了 `i` 的访问在有效范围内，且内部条件 `i < q->nb_subs - 1` 进一步保护了 `q->subs[i + 1]` 的访问，不存在越界风险。 |
| 54 | ffmpeg-7.1 | enc_open | cpp/inconsistent-null-check | 189 | FP | FP | 函数av_frame_side_data_desc的返回值desc在后续代码中立即被使用（检查desc->props），如果desc为NULL，解引用将导致崩溃。但切片中av_frame_side_data_desc的调用位于一个循环... |
| 55 | ffmpeg-7.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | skip_space函数内部仅进行简单的空格字符遍历，不涉及内存分配或可能失败的复杂操作，其返回值始终是有效的指针（指向输入字符串或字符串末尾的空字符），不存在返回NULL的可能性，因此无需进行空指针检查。 |
| 56 | ffmpeg-7.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | FP | 函数 `ff_iir_filter_init_state` 的职责是分配并初始化状态，其返回值由调用者检查和处理。切片代码显示，该函数是内存分配器的一个简单封装，遵循了库的常见模式，将空指针检查的责任交给了上层调用者，因此告警为误报。 |
| 57 | ffmpeg-7.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1461 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 58 | ffmpeg-7.1 | hls_read_header | cpp/inconsistent-null-check | 2109 | FP | FP | 代码中 `in_fmt` 变量在调用 `av_find_input_format` 后，仅在后续的 `if (strstr(in_fmt->name, "mov"))` 中被直接解引用，但该条件判断位于 `avformat_open_... |
| 59 | ffmpeg-7.1 | intercept_id3 | cpp/inconsistent-null-check | 1191 | FP | FP | 函数`current_segment`返回的指针`seg`在后续代码中仅用于传递给`read_from_url`，而该函数内部已对`seg->size`的访问进行了保护性检查（`if (seg->size >= 0)`），即使`seg... |
| 61 | ffmpeg-7.1 | init_muxer | cpp/inconsistent-null-check | 190 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，仅执行指针转换，不可能返回空指针。告警规则建议检查空指针，但在此上下文中该检查是多余的，因此是误报。 |
| 62 | ffmpeg-7.1 | cmp_dm_level0 | cpp/overflow-buffer | 294 | FP | FP | 告警中的 `memcmp` 调用使用 `sizeof(AVDOVIColorMetadata) - offsetof(AVDOVIColorMetadata, signal_eotf)` 作为长度，这是计算结构体从 `signal_e... |
| 63 | ffmpeg-7.1 | url_alloc_for_protocol | cpp/unbounded-write | 146 | FP | FP | 目标缓冲区 uc->filename 的大小通过 `strlen(filename) + 1` 精确分配，与源字符串长度匹配，因此 `strcpy` 操作是安全的，不会发生缓冲区溢出。 |
| 64 | ffmpeg-6.0 | upcase_string | cpp/offset-use-before-range-check | 1044 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了只有当 `i` 小于 `dst_size-1` 且 `src[i]` 不为空时才会进入循环体，循环结束后 `i` 的值要么等于 `dst_size-1`，要么指向 ... |
| 65 | ffmpeg-6.0 | capture_screen | cpp/offset-use-before-range-check | 485 | FP | FP | 在告警所在行的while循环条件中，变量j的使用已包含范围检查'j < tab'，确保j不会超出tab的值。tab的值由第一个循环计算得出，且j的初始化和递增逻辑保证了其在数组边界内安全使用。 |
| 66 | ffmpeg-6.0 | capture_screen | cpp/offset-use-before-range-check | 485 | FP | FP | 在告警所在行，`j` 的使用已通过 `j < tab` 条件进行了范围检查，该条件确保了循环在 `j` 达到 `tab` 值时终止，因此不存在越界访问的风险。 |
| 67 | ffmpeg-6.0 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | FP | 切片代码显示，在 while 循环条件 `m < b && m < nb_entries - 1` 中，对变量 `m` 的访问 `entries[m]` 发生在对其范围的检查之后，确保了数组访问的安全性。 |
| 68 | ffmpeg-6.0 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 207 | FP | FP | 在循环条件 `i < q->nb_subs` 的保护下，访问 `q->subs[i]` 和 `q->subs[i + 1]` 是安全的。对于 `q->subs[i + 1]` 的访问，其前置条件 `i < q->nb_subs - 1... |
| 69 | ffmpeg-6.0 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | 函数 `skip_space` 内部仅进行简单的空格字符遍历，不涉及内存分配或可能失败的复杂操作，其返回值不可能为 NULL。因此，无需检查其返回值是否为 NULL，告警为误报。 |
| 70 | ffmpeg-6.0 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 203 | FP | FP | 函数 `ff_iir_filter_init_state` 的返回值直接返回给调用者，内存分配失败（NULL）的检查责任应由调用者承担。告警规则基于统计模式（99%的调用检查NULL）触发，但此处的设计模式是合理的，并非安全漏洞。 |
| 71 | ffmpeg-6.0 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1373 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 72 | ffmpeg-6.0 | intercept_id3 | cpp/inconsistent-null-check | 1184 | FP | FP | 代码中多处直接使用 `seg->size` 和 `seg` 指针，未进行空指针检查，这表明 `current_segment` 函数预期返回非空指针，且调用上下文假设其有效。告警指出的不一致性检查是代码风格或潜在逻辑问题，但切片内未发... |
| 73 | ffmpeg-6.0 | get_frag_time | cpp/inconsistent-null-check | 1286 | FP | FP | 在调用 `get_frag_stream_info` 后，代码立即访问其返回的指针成员（如 `sidx_pts`），这隐含了对指针非空的假设。结合被调用函数 `get_frag_stream_info` 的定义，它在未找到匹配项时返回... |
| 74 | ffmpeg-6.0 | init_muxer | cpp/inconsistent-null-check | 185 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，仅将 `AVOutputFormat*` 转换为 `const FFOutputFormat*`，其返回值不可能为 NULL。告警规则建议检查 NULL 是基于对函数调用模式的统计... |
| 75 | ffmpeg-6.0 | url_alloc_for_protocol | cpp/unbounded-write | 102 | FP | FP | 目标缓冲区 `uc->filename` 的大小为 `strlen(filename) + 1`，与源字符串 `filename` 的长度精确匹配，`strcpy` 操作不会发生溢出。 |
| 76 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1194 | FP | FP | 在分配新内存给 `sc->ext.session_ticket` 之前，已经调用了 `OPENSSL_free` 释放了旧内存，并且紧接着检查了新分配的内存是否为 NULL。代码逻辑确保了在访问 `sc->ext.session_ti... |
| 77 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1195 | FP | FP | 告警指向的代码行 `sc->ext.session_ticket->data = sc->ext.session_ticket + 1;` 是计算结构体内指针偏移，并非对已释放内存的解引用。`OPENSSL_free` 释放的是旧指针... |
| 78 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1196 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件`if (sc->ext.session_ticket == NULL)`检查内存分配是否成功，并且`sc->ext.session_ticket->data`被正确指向新分配内存的偏移... |
| 79 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1196 | FP | FP | 代码在调用memcpy前已通过条件`if (ext_data != NULL)`确保源指针非空，且已为新分配的`sc->ext.session_ticket`检查了内存分配成功，不存在对已释放内存的访问。告警可能是工具对指针运算`sc... |
| 80 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1198 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后分配新内存，并检查分配是否成功。该流程正确管理了内存，不存在对已释... |
| 81 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1199 | FP | FP | 代码在分配内存后立即检查了分配结果（`if (sc->ext.session_ticket == NULL)`），并在分配失败时提前返回，确保了后续对 `sc->ext.session_ticket` 的访问（如 `sc->ext.s... |
| 82 | openssl-openssl-3.5.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1729 | FP | FP | 切片代码显示，在调用memcmp比较`s->session->ext.alpn_selected`和`s->s3.alpn_selected`之前，已为`s->s3.alpn_selected`分配了内存并检查了分配成功，且`s->s... |
| 83 | openssl-openssl-3.5.1 | tls_parse_stoc_npn | cpp/use-after-free | 1660 | FP | FP | 在调用 `OPENSSL_free(s->ext.npn)` 后，立即为其分配了新的内存 `s->ext.npn = OPENSSL_malloc(...)`，并检查了分配结果。后续的 `memcpy` 操作使用的是新分配的内存指针，... |
| 84 | openssl-openssl-3.5.1 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 告警指出的空指针检查 `if (keySpec != NULL)` 是冗余的，因为其后的 `sk_OSSL_CMP_ATAV_pop_free(*keySpec, ...)` 已经对 `*keySpec` 进行了解引用。然而，`pop... |
| 85 | openssl-openssl-3.5.1 | <global> | cpp/offset-use-before-range-check | 266 | FP | FP | 循环条件 `src[i] != '\0' && i < len` 已确保对数组 `src` 和 `tgt` 的访问索引 `i` 在有效范围内（`i < len`），不存在越界风险。告警所提示的偏移量 `i` 的使用已受到前置范围检查的保护。 |
| 86 | openssl-openssl-3.5.1 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 变量'i'在for循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'中，其使用（DB[i]）与范围检查（i < (maskedDBLen - 1)）是同步进行的，逻辑上确保了访问DB[i]时i不会越界。 |
| 87 | openssl-openssl-3.5.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 345 | FP | FP | 代码在调用 CRYPTO_THREAD_get_local 后，立即使用 `assert(data != NULL);` 对返回值进行了严格的非空断言，这确保了后续使用 data 指针的安全性。assert 在调试模式下会强制检查，且... |
| 88 | openssl-openssl-3.5.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 越界时可能返回 NULL，而调用前 `enc_level` 由上层传入，切片中无越界证据。... |
| 89 | openssl-openssl-3.5.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 索引越界时返回 NULL，而该条件已通过 `ossl_assert` 检查，因此返... |
| 90 | openssl-openssl-3.5.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 函数 `ossl_uint_set_insert` 在调用 `ossl_list_uint_set_head(s)` 后，立即在 `if (start <= f->range.start ...)` 中解引用了 `f->range.s... |
| 91 | openssl-openssl-3.5.1 | ts_check_status_info | cpp/unsafe-strcat | 385 | FP | FP | 代码中`failure_text`数组大小由常量`TS_STATUS_BUF_SIZE`定义，且循环拼接的源字符串`ts_failure_info[i].text`是静态常量数组元素，其长度在编译时已知。通过循环条件`i < (int... |
| 92 | openssl-openssl-3.5.1 | <global> | cpp/unbounded-write | 30 | FP | FP | 函数 CRYPTO_strdup 在调用 strcpy 前，已通过 CRYPTO_malloc(strlen(str) + 1) 为目标缓冲区分配了精确匹配源字符串长度的空间，因此不会发生缓冲区溢出。 |
| 93 | openssl-openssl-3.5.1 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 代码在调用strcpy前，已通过`len + 1 >= size`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 94 | openssl-openssl-3.5.1 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码显示，在调用strcpy之前，函数已通过`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，确保不会发生溢出。 |
| 95 | openssl-openssl-3.5.1 | main | cpp/unbounded-write | 82 | FP | FP | 目标缓冲区 pathname 的大小为 PATH_MAX，而源字符串 argv[n] 的长度 dirname_len 在复制前已通过 strlen 获取，且后续操作确保 dirname_len 在追加 '/' 后仍小于 PATH_MA... |
| 96 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3468 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数（reason 和 msg），符合其定义。切片代码中未发现可变参数（variadic argument）的使用，因此不存在未终止的可变参... |
| 97 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3477 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数（reason 和 msg），符合其定义。切片代码显示该宏展开后调用 `quic_raise_non_normal_error` 时传递... |
| 98 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3487 | FP | FP | 告警指出的调用 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_INTERNAL_ERROR, "ref")` 符合宏定义 `QUIC_RAISE_NON_NORMAL_ERROR(ctx, reas... |
| 99 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3493 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数（ctx, reason, msg），与宏定义完全匹配，不存在未终止的可变参数调用问题。工具可能对宏展开的规则产生了误判。 |
| 100 | openssl-openssl-3.5.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3409 | FP | FP | 告警指出的宏 `QUIC_RAISE_NON_NORMAL_ERROR` 调用已正确传递了所有参数，包括 `(reason)` 和 `(msg)`，切片中未发现变长参数列表或明显的参数缺失。该调用符合宏定义，工具可能误报了格式问题。 |
| 101 | openssl-openssl-3.5.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3421 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数（ctx, reason, msg），与宏定义完全匹配，不存在未终止的可变参数调用问题。代码逻辑正确，属于工具误报。 |
| 102 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1846 | FP | FP | 宏 `QUIC_RAISE_NON_NORMAL_ERROR` 展开后调用 `quic_raise_non_normal_error`，其参数列表末尾的字符串字面量 `"failed to configure channel"` 等是... |
| 103 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1853 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已通过宏定义正确展开为 `quic_raise_non_normal_error` 函数调用，其参数列表（包括文件、行号、函数名、原因和消息）是完整且格式正... |
| 104 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1861 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数，与宏定义 `(ctx, reason, msg)` 的参数数量一致，不存在未终止的可变参数调用问题。工具可能误报了宏展开后的内部函数调... |
| 105 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 代码使用常量时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来安全地处理边界条件，循环中的指针运算和访问受 flen 和 num 的控制，且存在明确的边界检查... |
| 106 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中，`em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，并在循环中从 `em + num` ... |
| 107 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用了恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来控制循环和内存访问，确保指针运算和数组访问在边界内，即使 flen 可能小于 num，mask... |
| 108 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 `em[0]` 的访问是安全的，因为 `em` 指针指向 `OPENSSL_malloc(num)` 分配的内存块起始位置，且循环 `for (from += flen, em += num, i = 0; i < num; ... |
| 109 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的。指针 `em` 指向大小为 `num` 的动态分配内存，且循环 `for (i = 0; i < num; i++)` 确保了 `em` 数组的每个元素（包括索引1）在访问前都已被初始化。代码逻... |
| 110 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1171 | FP | FP | 在调用OPENSSL_free释放sc->ext.session_ticket后，代码立即为其重新分配了新的内存空间，并将结果赋值给同一个指针。这符合安全的内存重新分配模式，不存在对已释放内存的访问。 |
| 111 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1172 | FP | FP | 告警指向的代码行 `sc->ext.session_ticket->data = sc->ext.session_ticket + 1;` 是计算结构体内指针偏移，并非对已释放内存的解引用。`OPENSSL_free` 释放的是旧指针... |
| 112 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1173 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件`if (sc->ext.session_ticket == NULL)`检查内存分配是否成功，并在失败时提前返回。因此，当执行到memcpy时，`sc->ext.session_tic... |
| 113 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1173 | FP | FP | 代码在调用memcpy前已通过条件`if (ext_data != NULL)`进行了检查，确保了源指针非空。同时，目标内存`sc->ext.session_ticket->data`被正确赋值为紧邻结构体的缓冲区地址，且该缓冲区大小... |
| 114 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1175 | FP | FP | 代码在重新分配内存前已正确释放旧指针（OPENSSL_free），并将指针置为NULL，随后检查新分配的内存是否成功。在ext_data为NULL的分支中，对结构体成员的访问（如`sc->ext.session_ticket->len... |
| 115 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1176 | FP | FP | 代码在分配内存后立即检查了分配结果（`if (sc->ext.session_ticket == NULL)`），并在分配失败时提前返回，确保了后续对 `sc->ext.session_ticket` 的访问（如 `sc->ext.s... |
| 116 | openssl-openssl-3.3.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1626 | FP | FP | 切片代码显示，在调用memcmp比较s->session->ext.alpn_selected和s->s3.alpn_selected之前，s->s3.alpn_selected已通过OPENSSL_malloc分配内存并检查了非空，... |
| 117 | openssl-openssl-3.3.1 | tls_parse_stoc_npn | cpp/use-after-free | 1581 | FP | FP | 切片代码显示，在调用 `memcpy` 之前，已通过 `OPENSSL_free(s->ext.npn)` 释放了旧指针，并立即通过 `OPENSSL_malloc` 重新分配了新内存给 `s->ext.npn`。`memcpy` 的... |
| 118 | openssl-openssl-3.3.1 | RSA_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 109 | FP | FP | 切片代码显示，变量 `i` 在 `for (i = 0; DB[i] == 0 && i < (maskedDBLen - 1); i++) ;` 循环中受到 `i < (maskedDBLen - 1)` 条件的严格限制，确保 `i... |
| 119 | openssl-openssl-3.3.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 447 | FP | FP | 提供的切片代码显示函数 `ossl_rcu_read_unlock` 为空实现，未调用 `CRYPTO_THREAD_get_local`，因此工具报告的未检查空指针的调用不存在，属于误报。 |
| 120 | openssl-openssl-3.3.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 索引越界时返回 NULL，而调用前 `enc_level` 已通过 `ossl_qrl_e... |
| 121 | openssl-openssl-3.3.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 索引越界时返回 NULL，而调用时 `require_prov` 为 0，且切片中... |
| 122 | openssl-openssl-3.3.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 函数 `ossl_list_uint_set_head` 的返回值 `f` 在后续代码中直接解引用（`f->range.start`），这表明 `f` 被假定为非空。结合函数逻辑，该操作发生在对列表 `s` 进行插入操作的上下文中，且... |
| 123 | openssl-openssl-3.3.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | `failure_text` 数组大小由 `TS_STATUS_BUF_SIZE` 宏定义，循环拼接的源字符串 `ts_failure_info[i].text` 是静态常量数组元素，其长度固定且已知，总拼接长度受循环次数（即 `OS... |
| 124 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 2582 | FP | FP | 切片代码显示，目标缓冲区 `evp_hmac_name` 是通过 `app_malloc` 动态分配的，其大小为固定字符串 "hmac()" 的长度加上 `evp_mac_mdname` 的长度，这确保了 `sprintf` 写入的内... |
| 125 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 2860 | FP | FP | sprintf的目标缓冲区evp_cmac_name是通过app_malloc动态分配的，其大小精确计算为字符串'cmac()'的长度加上evp_mac_ciphername的长度，确保了缓冲区足以容纳格式化后的完整字符串，因此不会发... |
| 126 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 29 | FP | FP | 函数 CRYPTO_strdup 在调用 strcpy 前，已通过 CRYPTO_malloc(strlen(str) + 1, ...) 为目标缓冲区分配了精确匹配源字符串长度的内存（包含终止符），因此 strcpy 操作是安全的，... |
| 127 | openssl-openssl-3.3.1 | RAND_file_name | cpp/unbounded-write | 309 | FP | FP | 在调用strcpy前，代码已通过`len + 1 >= size`检查了目标缓冲区大小，确保不会发生溢出。环境变量值的长度已通过strlen获取并验证，因此该告警是安全的误报。 |
| 128 | openssl-openssl-3.3.1 | RAND_file_name | cpp/unbounded-write | 313 | FP | FP | 在调用strcpy之前，代码已通过条件`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 129 | openssl-openssl-3.3.1 | main | cpp/unbounded-write | 82 | FP | FP | 代码在调用strcpy前，已为pathname分配了PATH_MAX大小的缓冲区，而argv[n]是目录名，其长度dirname_len在分配前已计算，且后续拼接操作确保不会超过PATH_MAX边界。因此，该strcpy操作是安全的，... |
| 130 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3131 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片中已明确定义，其参数列表以 `(msg)` 结尾，符合C语言可变参数函数调用规范，不存在未正确终止的问题。代码逻辑正确，工具告警为误报。 |
| 131 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3140 | FP | FP | 告警指出的调用点 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_SHOULD_NOT_HAVE_BEEN_CALLED, "connection already has a default stre... |
| 132 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3150 | FP | FP | 告警指出的QUIC_RAISE_NON_NORMAL_ERROR宏调用缺少终止符0，但根据提供的宏定义，该宏展开为对quic_raise_non_normal_error的函数调用，其参数列表是固定的，并非可变参数函数，因此不存在未终... |
| 133 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3156 | FP | FP | 告警指出的调用点 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_PASSED_INVALID_ARGUMENT, ...)` 传递了三个参数，而宏定义 `QUIC_RAISE_NON_NORMAL_... |
| 134 | openssl-openssl-3.3.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3072 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了终止符0。该宏展开为 `quic_raise_non_normal_error` 函数调用，其参数列表末尾的字符串字面量 `"too late ... |
| 135 | openssl-openssl-3.3.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3084 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了终止符0。该宏展开为 `quic_raise_non_normal_error` 函数调用，其参数列表末尾的字符串字面量 `"bad defau... |
| 136 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1544 | FP | FP | 宏 `QUIC_RAISE_NON_NORMAL_ERROR` 的定义显示其最后一个参数 `(msg)` 是一个字符串字面量，并非可变参数列表的一部分；该告警规则要求为可变参数调用添加终止符 `0`，但此处调用的是固定参数的宏包装器，... |
| 137 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1551 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数（ctx, reason, msg），符合其定义 `quic_raise_non_normal_error(ctx, OPENSSL_F... |
| 138 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1561 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确提供了三个参数（ctx, reason, msg），符合其定义。切片代码中未发现任何与可变参数或终止符相关的错误用法，工具规则可能误判了此宏的调用约定。 |
| 139 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 221 | FP | FP | 代码使用恒定时间操作（constant_time_is_zero, mask）来安全地处理边界条件，循环逻辑确保了指针访问不会越界。告警点位于一个精心设计的恒定时间复制循环内，该循环通过掩码（mask）控制，仅当 flen > 0 时... |
| 140 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 229 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中，`em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，并在循环中从 `em + num` ... |
| 141 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来安全地处理边界条件，确保指针访问不会越界。告警点 `*--em = *from & mask;`... |
| 142 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 代码使用常量时间操作（如 constant_time_is_zero）进行边界和内容检查，并通过 good 变量累积验证结果，确保后续数组访问（如 em[i + RSA_PKCS1_PADDING_SIZE]）仅在所有检查通过（goo... |
| 143 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的，因为 `em` 指向大小为 `num` 的动态分配内存，且循环 `for (i = 0; i < num; i++)` 确保了 `em` 指针在数组边界内移动，`em[1]` 的访问不会越界。 |
| 144 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1182 | FP | FP | 在调用 `OPENSSL_free` 释放 `sc->ext.session_ticket` 后，代码立即为其重新分配了新的内存（`OPENSSL_malloc`），并检查了分配结果。因此，后续对 `sc->ext.session_t... |
| 145 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1183 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后分配新内存并检查成功后才进行赋值和使用，不存在对已释放内存的访问。 |
| 146 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件`if (sc->ext.session_ticket == NULL)`检查内存分配是否成功，若失败则函数提前返回。因此，当执行到memcpy时，`sc->ext.session_ti... |
| 147 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件`if (ext_data != NULL)`进行了检查，确保源指针非空；同时，新分配的内存地址已赋值给`sc->ext.session_ticket->data`，作为目标指针，该指针... |
| 148 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1186 | FP | FP | 切片代码显示，在设置 `sc->ext.session_ticket->data = NULL;` 之前，已经通过 `OPENSSL_free` 释放了旧指针并分配了新内存，`sc->ext.session_ticket` 指向的是新... |
| 149 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1187 | FP | FP | 代码在分配新内存并赋值给 `sc->ext.session_ticket` 后，才访问其 `data` 成员并设置为 NULL，不存在对已释放内存的访问。告警点 `sc->ext.session_ticket->data = NULL... |
| 150 | openssl-openssl-3.4.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1689 | FP | FP | 告警指向的 `s->s3.alpn_selected` 在 `memcmp` 调用前已被重新分配内存，其值来自 `OPENSSL_malloc(len)`，并非使用已释放的内存。切片代码清晰地展示了分配新内存后立即使用该指针的逻辑，不... |
| 151 | openssl-openssl-3.4.1 | tls_parse_stoc_npn | cpp/use-after-free | 1620 | FP | FP | 切片代码显示，在调用 `memcpy` 之前，已通过 `OPENSSL_free` 释放了 `s->ext.npn`，但随后立即通过 `OPENSSL_malloc` 为其重新分配了内存。`memcpy` 的目标地址是新分配的内存，并... |
| 152 | openssl-openssl-3.4.1 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 切片代码显示，在告警的冗余空值检查之前，已经存在对 `*keySpec` 的显式解引用和释放操作（`sk_OSSL_CMP_ATAV_pop_free(*keySpec, ...)`），因此 `keySpec` 不可能为 NULL，此... |
| 153 | openssl-openssl-3.4.1 | <global> | cpp/offset-use-before-range-check | 246 | FP | FP | 循环条件 `src[i] != '\0' && i < len` 确保了在访问 `src[i]` 之前，索引 `i` 已通过 `i < len` 检查，因此不存在越界访问风险。告警为误报。 |
| 154 | openssl-openssl-3.4.1 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 变量'i'在for循环中已通过条件'i < (maskedDBLen - 1)'进行了范围检查，确保在后续使用DB[i++]时不会越界。告警所指的'使用前范围检查'实际上已包含在循环条件中。 |
| 155 | openssl-openssl-3.4.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 489 | FP | FP | 代码在调用 `CRYPTO_THREAD_get_local` 后，立即使用 `assert(data != NULL)` 对返回值进行了严格的非空断言，这确保了在调试构建中会立即捕获空值情况。虽然 `assert` 在发布构建中可能... |
| 156 | openssl-openssl-3.4.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 无效时返回 NULL，而 `enc_level` 由调用者传入且已通过 `ossl_qrl... |
| 157 | openssl-openssl-3.4.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在给定参数 `require_prov=0` 时，仅在 `enc_level` 索引越界时返回 NULL，而该越界检查由 `ossl_assert` 宏处理，通常... |
| 158 | openssl-openssl-3.4.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 获取 `f` 后，代码立即在 `if (start <= f->range.start && end >= z->range.end)` 中访问了 `f->range.... |
| 159 | openssl-openssl-3.4.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | 循环中拼接的源字符串 `ts_failure_info[i].text` 来自编译时常量数组 `ts_failure_info`，其长度固定且已知，不会导致 `failure_text` 缓冲区溢出。 |
| 160 | openssl-openssl-3.4.1 | <global> | cpp/unbounded-write | 30 | FP | FP | 函数CRYPTO_strdup在调用strcpy前，已通过CRYPTO_malloc分配了strlen(str) + 1字节的内存，目标缓冲区大小与源字符串长度精确匹配，不存在缓冲区溢出的风险。 |
| 161 | openssl-openssl-3.4.1 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码显示，在调用strcpy之前，函数已通过`len + 1 >= size`检查了目标缓冲区大小，确保不会发生缓冲区溢出。 |
| 162 | openssl-openssl-3.4.1 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码显示，在调用strcpy之前，函数已通过`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`对目标缓冲区大小进行了严格检查，确保不会发生溢出。 |
| 163 | openssl-openssl-3.4.1 | main | cpp/unbounded-write | 82 | FP | FP | 目标缓冲区 `pathname` 的大小为 `PATH_MAX`，而源字符串 `argv[n]` 的长度 `dirname_len` 在复制前已通过 `strlen` 获取，且后续操作确保 `dirname_len` 在追加 '/' ... |
| 164 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3149 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数（reason 和 msg），符合其定义 `quic_raise_non_normal_error(ctx, file, line, f... |
| 165 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3158 | FP | FP | 告警指出的调用点 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_SHOULD_NOT_HAVE_BEEN_CALLED, "connection already has a default stre... |
| 166 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3168 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_INTERNAL_ERROR, "ref")` 提供了三个参数，与宏定义 `(ctx, reason, msg)` 的参数数量一致，且... |
| 167 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3174 | FP | FP | 告警指出的两个 `QUIC_RAISE_NON_NORMAL_ERROR` 宏调用，其最后一个参数（`msg`）均为有效的字符串字面量，并非空指针或未终止的可变参数。宏定义显示该调用格式正确，不存在未终止的可变参数调用问题。 |
| 168 | openssl-openssl-3.4.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3090 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了终止符0。该宏展开为 `quic_raise_non_normal_error` 函数调用，其参数列表中的 `(msg)` 对应宏定义中的最后一... |
| 169 | openssl-openssl-3.4.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3102 | FP | FP | 告警提示调用 `quic_raise_non_normal_error` 应使用值0作为终止符，但切片代码显示该调用是通过宏 `QUIC_RAISE_NON_NORMAL_ERROR` 进行的，该宏的参数列表是固定的，且最后一个参数 ... |
| 170 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1546 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了终止符 `0`，因为其展开后的函数 `quic_raise_non_normal_error` 是一个普通函数，而非可变参数函数，因此不存在未终... |
| 171 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1553 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数（ctx, reason, msg），与宏定义匹配，切片中未发现未终止的可变参数调用问题，属于工具误报。 |
| 172 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1563 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确提供了三个参数（ctx, reason, msg），符合其定义 `quic_raise_non_normal_error(ctx, OPENSSL_F... |
| 173 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 代码使用常量时间操作和掩码（mask）来安全地处理边界条件，`flen` 的递减和 `from` 指针的移动受 `mask` 控制，当 `flen` 为零时操作停止，防止了越界读取。 |
| 174 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中，`em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节的内存，并在循环 `for (from +... |
| 175 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用常量时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来安全地处理边界条件，循环中的指针运算受 flen 和 mask 控制，确保了内存访问不会越界。 |
| 176 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 `em[0]` 的访问是安全的，因为 `em` 指针指向 `OPENSSL_malloc(num)` 分配的内存块起始位置，且循环 `for (from += flen, em += num, i = 0; i < num; ... |
| 177 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的。指针 `em` 指向通过 `OPENSSL_malloc(num)` 分配的内存块，大小为 `num`。在访问 `em[1]` 之前，代码通过循环 `for (i = 0; i < num; i... |
| 178 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1138 | FP | FP | 告警指向的代码行 `sc->ext.session_ticket->length = ext_len;` 是在对 `sc->ext.session_ticket` 进行赋值操作，而该指针在之前已被释放并重新分配了内存。代码逻辑确保了在... |
| 179 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1139 | FP | FP | 代码中 `sc->ext.session_ticket->data` 被赋值为 `sc->ext.session_ticket + 1`，这是一个指向紧邻分配内存块之后地址的指针，是有效的内存操作，并非使用已释放的内存。告警是对指针算... |
| 180 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1140 | FP | FP | 代码在调用memcpy前已通过条件`if (ext_data != NULL)`进行了检查，确保了源指针非空；同时，在分配内存后也检查了`sc->ext.session_ticket`是否为NULL，防止了使用未分配的内存。切片内未发... |
| 181 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1140 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件`if (ext_data != NULL)`进行了检查，确保了源指针非空。同时，目标内存`sc->ext.session_ticket->data`被正确指向新分配的内存区域（`sc-... |
| 182 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1142 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已经调用了 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。后续的 `memcpy` 操作仅在 `ext_data != NU... |
| 183 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1143 | FP | FP | 告警指向的代码行 `sc->ext.session_ticket->data = NULL;` 是在 `ext_data` 为 `NULL` 时执行的，此时 `sc->ext.session_ticket` 刚被分配内存且不为 `NU... |
| 184 | openssl-openssl-3.2.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1626 | FP | FP | 切片代码显示，在调用memcmp比较`s->session->ext.alpn_selected`和`s->s3.alpn_selected`之前，已通过`OPENSSL_free`释放了`s->s3.alpn_selected`的原... |
| 185 | openssl-openssl-3.2.1 | tls_parse_stoc_npn | cpp/use-after-free | 1581 | FP | FP | 切片代码显示，在调用 `memcpy` 使用 `selected` 和 `selected_len` 之前，已通过 `OPENSSL_free` 释放了 `s->ext.npn`，并立即为其重新分配了大小为 `selected_len... |
| 186 | openssl-openssl-3.2.1 | RSA_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 109 | FP | FP | 变量'i'在for循环中作为索引使用，其初始值为0，循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'确保了'i'在递增前始终小于'maskedDBLen - 1'，因此后续的'DB[i++]'访问是安... |
| 187 | openssl-openssl-3.2.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 越界时可能返回 NULL，而调用前 `enc_level` 参数由上层传入，切片中无越界证... |
| 188 | openssl-openssl-3.2.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 索引越界时返回 NULL，而调用时 `require_prov` 为 0，且切片中... |
| 189 | openssl-openssl-3.2.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 获取 `f` 后，代码立即在 `if (start <= f->range.start && end >= z->range.end)` 中解引用 `f->range.... |
| 190 | openssl-openssl-3.2.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | failure_text 数组大小固定为 TS_STATUS_BUF_SIZE，且循环拼接的源字符串 ts_failure_info[i].text 是静态常量数组的元素，其长度已知且有限，不会导致缓冲区溢出。 |
| 191 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 2530 | FP | FP | 代码中 `evp_hmac_name` 已通过 `app_malloc` 分配了足够空间（"hmac()" 的长度加上 `evp_mac_mdname` 的长度），确保 `sprintf` 不会溢出目标缓冲区。 |
| 192 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 2826 | FP | FP | 目标缓冲区 `evp_cmac_name` 的大小已通过 `app_malloc` 精确分配，其大小为字符串字面量 "cmac()" 的长度加上 `evp_mac_ciphername` 的长度，足以容纳 `sprintf` 的输出，... |
| 193 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 29 | FP | FP | 函数 CRYPTO_strdup 在调用 strcpy 前，已通过 CRYPTO_malloc(strlen(str) + 1, ...) 为目标缓冲区分配了精确匹配源字符串长度的空间（包含终止符），因此 strcpy 操作是安全的，... |
| 194 | openssl-openssl-3.2.1 | RAND_file_name | cpp/unbounded-write | 309 | FP | FP | 在调用strcpy之前，代码已通过`len + 1 >= size`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 195 | openssl-openssl-3.2.1 | RAND_file_name | cpp/unbounded-write | 313 | FP | FP | 切片代码显示，在调用strcpy之前，函数已通过`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，确保不会发生溢出。 |
| 196 | openssl-openssl-3.2.1 | main | cpp/unbounded-write | 82 | FP | FP | 代码在调用strcpy前，已为pathname分配了PATH_MAX大小的缓冲区，而argv[n]的长度dirname_len在分配前已通过strlen计算，且后续操作确保dirname_len小于PATH_MAX，因此不会发生缓冲区溢出。 |
| 197 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3054 | FP | FP | 切片代码显示，宏 QUIC_RAISE_NON_NORMAL_ERROR 的最后一个参数在调用时明确为字符串字面量或 NULL，不存在未终止的可变参数列表风险。告警规则针对的是可变参数调用，但此处宏展开后的函数调用参数数量是固定的。 |
| 198 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3063 | FP | FP | 告警指出的调用点 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_SHOULD_NOT_HAVE_BEEN_CALLED, "connection already has a default stre... |
| 199 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3073 | FP | FP | 告警指出的调用 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_INTERNAL_ERROR, "ref")` 提供了三个参数，与宏定义 `QUIC_RAISE_NON_NORMAL_ERROR(ct... |
| 200 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3079 | FP | FP | 切片代码显示，宏 QUIC_RAISE_NON_NORMAL_ERROR 的调用格式与定义一致，其最后一个参数 'msg' 是一个字符串字面量或 NULL，并非可变参数列表，因此不存在未终止的可变参数调用问题。告警是对宏展开形式的误判。 |
| 201 | openssl-openssl-3.2.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 2995 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了终止符 `0`，该终止符作为宏的最后一个参数 `(reason)` 的值传递，符合规则要求。切片代码显示调用格式正确，不存在未终止的可变参数调用问题。 |
| 202 | openssl-openssl-3.2.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3007 | FP | FP | 告警指出的函数调用 `QUIC_RAISE_NON_NORMAL_ERROR` 是一个宏，展开后调用 `quic_raise_non_normal_error`。切片代码显示，该调用已提供了所有必需的参数（ctx, reason, m... |
| 203 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1520 | FP | FP | 告警指出的宏 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已正确定义，其参数列表与调用的变参函数 `quic_raise_non_normal_error` 匹配，且所有调用点（如 `ERR_R_INTER... |
| 204 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1527 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片中已明确定义为 `quic_raise_non_normal_error` 的包装，其参数数量与宏定义匹配。代码逻辑是处理内部错误并返回，不存在未终止... |
| 205 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1537 | FP | FP | 告警指出的宏 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中被正确调用，其展开为 `quic_raise_non_normal_error` 函数，且提供了所有必需的参数（包括文件、行号、函数名、原因和消息）... |
| 206 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 221 | FP | FP | 代码使用常量时间操作（如 `constant_time_is_zero` 和掩码 `mask`）来安全地处理边界条件，循环中的指针运算 `*--em = *from & mask` 在 `flen` 为0时会被掩码清零，避免了越界读取... |
| 207 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 229 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中，`em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，并在循环中从 `em + num` ... |
| 208 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来安全地处理边界条件，确保指针访问不会越界。告警点位于受控循环内，其访问逻辑通过 flen 和 m... |
| 209 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 代码使用恒定时间比较函数（如 constant_time_is_zero）进行边界和条件检查，并通过 good 标志控制内存访问。在 good 为 0 时，对 em[0] 的访问会被屏蔽，不会发生越界读取。算法标签 FP 与此分析一致。 |
| 210 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的。`em` 指向大小为 `num` 的已分配内存，且循环 `for (i = 0; i < num; i++)` 确保了 `em` 数组的每个元素（包括索引1）都已被初始化。因此，该读取操作不会越界。 |
| 211 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1182 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后检查新分配的内存是否为 NULL，并在后续访问前进行了判断。该流... |
| 212 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1183 | FP | FP | 代码中 `sc->ext.session_ticket->data` 被赋值为 `sc->ext.session_ticket + 1`，这是一个指向紧邻分配内存块之后地址的指针，属于有效的内存区域，并非指向已释放的内存。该赋值用于后... |
| 213 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用 memcpy 之前，已通过条件 `if (sc->ext.session_ticket == NULL)` 检查内存分配是否成功，若分配失败则函数提前返回，因此不会发生对已释放内存的访问。告警点 `sc->ext... |
| 214 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用 `memcpy` 之前，已通过 `OPENSSL_malloc` 为 `sc->ext.session_ticket` 分配了新的内存，并检查了分配结果。`memcpy` 使用的目标地址 `sc->ext.ses... |
| 215 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1186 | FP | FP | 告警指向的代码行 `sc->ext.session_ticket->length = 0;` 是在 `sc->ext.session_ticket` 刚被分配内存并检查非空之后执行的，不存在对已释放内存的访问。代码逻辑确保了在访问 `... |
| 216 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1187 | FP | FP | 切片代码显示，在将 `sc->ext.session_ticket->data` 赋值为 NULL 之前，已经通过 `OPENSSL_free` 释放了旧指针并分配了新内存，不存在对已释放内存的访问。告警点是对新分配结构体成员的初始化... |
| 217 | openssl-openssl-3.4.0 | tls_parse_stoc_alpn | cpp/use-after-free | 1688 | FP | FP | 切片代码显示，在调用memcmp比较`s->session->ext.alpn_selected`和`s->s3.alpn_selected`之前，已通过`OPENSSL_free`释放了`s->s3.alpn_selected`，但... |
| 218 | openssl-openssl-3.4.0 | tls_parse_stoc_npn | cpp/use-after-free | 1619 | FP | FP | 代码在重新分配内存前调用了 OPENSSL_free(s->ext.npn)，释放了旧指针，随后立即分配新内存并检查其有效性。该模式是安全的资源管理，不存在对已释放内存的后续使用。 |
| 219 | openssl-openssl-3.4.0 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 告警指出的空指针检查 `if (keySpec != NULL)` 是冗余的，因为其上一行 `sk_OSSL_CMP_ATAV_pop_free(*keySpec, OSSL_CMP_ATAV_free);` 已经对 `*keySpe... |
| 220 | openssl-openssl-3.4.0 | <global> | cpp/offset-use-before-range-check | 246 | FP | FP | 循环条件 `src[i] != '\0' && i < len` 确保了在访问 `src[i]` 之前，索引 `i` 已通过 `i < len` 的范围检查，因此不存在越界访问风险。 |
| 221 | openssl-openssl-3.4.0 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 告警点位于一个用于寻找DB数组中第一个非零字节的循环中，循环条件 `i < (maskedDBLen - 1)` 确保了 `i` 不会超出 `maskedDBLen - 1` 的范围。后续的 `DB[i++]` 访问是安全的，因为循环... |
| 222 | openssl-openssl-3.4.0 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 470 | FP | FP | 代码在调用CRYPTO_THREAD_get_local后，立即使用`assert(data != NULL)`对返回值进行了严格的非空断言，这确保了后续代码路径中data指针的有效性，因此该告警为误报。 |
| 223 | openssl-openssl-3.4.0 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅当 `enc_level` 无效才返回 NULL，而调用方已传入固定值 `enc_level` 且 `require_... |
| 224 | openssl-openssl-3.4.0 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 索引越界时返回 NULL，而该越界检查由 `ossl_assert` 处理，在非调... |
| 225 | openssl-openssl-3.4.0 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 获取 `f` 后，代码立即在 `if (start <= f->range.start && end >= z->range.end)` 中访问了 `f->range.... |
| 226 | openssl-openssl-3.4.0 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | failure_text数组大小由TS_STATUS_BUF_SIZE定义，循环中拼接的字符串ts_failure_info[i].text是静态常量，且循环次数受限于固定大小的ts_failure_info数组，因此strcat操作... |
| 227 | openssl-openssl-3.4.0 | <global> | cpp/unbounded-write | 30 | FP | FP | 函数 CRYPTO_strdup 在调用 strcpy 前，已通过 CRYPTO_malloc(strlen(str) + 1) 为目标缓冲区分配了精确匹配源字符串长度的空间，确保了不会发生缓冲区溢出。 |
| 228 | openssl-openssl-3.4.0 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码显示，在调用strcpy之前，函数已通过`len + 1 >= size`检查确保目标缓冲区`buf`的大小`size`足以容纳源字符串`s`及其终止符，因此不会发生缓冲区溢出。 |
| 229 | openssl-openssl-3.4.0 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 代码在调用strcpy前，已通过条件`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`检查了目标缓冲区大小，确保不会发生溢出。 |
| 230 | openssl-openssl-3.4.0 | main | cpp/unbounded-write | 82 | FP | FP | 目标缓冲区 `pathname` 已通过 `malloc(PATH_MAX)` 分配了固定大小 `PATH_MAX`，而源字符串 `argv[n]` 是命令行参数，其长度受限于操作系统参数长度，通常远小于 `PATH_MAX`，因此 ... |
| 231 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3136 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片中已明确定义，其参数列表以 `(msg)` 结尾，符合C语言可变参数函数调用规范，不存在未正确终止的问题。该告警是工具对宏展开的误判。 |
| 232 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3145 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 宏调用缺少终止符0，但根据提供的宏定义，该宏展开为 `quic_raise_non_normal_error` 函数调用，其参数列表是固定的（包含ctx, fil... |
| 233 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3155 | FP | FP | 告警指出的未终止可变参数调用是针对宏 `QUIC_RAISE_NON_NORMAL_ERROR` 的，该宏的定义显示其最后一个参数 `(msg)` 被传递给 `quic_raise_non_normal_error` 函数。在切片代码... |
| 234 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3161 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已正确使用了三个参数（ctx, reason, msg），符合其定义，未发现参数缺失或终止符使用错误的问题。工具规则可能对可变参数调用的判断存在偏差。 |
| 235 | openssl-openssl-3.4.0 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3077 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确展开为 `quic_raise_non_normal_error` 函数，其参数列表在宏定义和调用处均完整且匹配，切片中未见任何未终止的可变参数调用问题。 |
| 236 | openssl-openssl-3.4.0 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3089 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了两个参数（reason 和 msg），且宏定义明确显示其展开为 `quic_raise_non_normal_error` 函数调用，该函数参数... |
| 237 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1546 | FP | FP | 宏 QUIC_RAISE_NON_NORMAL_ERROR 展开后调用 quic_raise_non_normal_error，其参数列表末尾的字符串字面量 "failed to configure channel" 等是最后一个参数... |
| 238 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1553 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，其展开为对 quic_raise_non_normal_error 的调用，并且该宏已正确传递了所有参数（包括文件、行号、函数名、原因和消息）。没有证据表... |
| 239 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1563 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了三个参数，与宏定义 `(ctx), (reason), (msg)` 的参数数量一致，不存在未终止的可变参数调用问题。该告警是工具对宏展开的误判。 |
| 240 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 代码使用常数时间操作和边界检查（如 `constant_time_is_zero(flen)` 和循环条件 `i < num`），确保指针访问在分配的内存边界内。告警点 `*--em = *from & mask;` 的访问受 `ma... |
| 241 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中，`em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，并在循环 `for (from +=... |
| 242 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来安全地处理边界条件，确保指针访问不会越界。告警点 `*--em = *from & mask;`... |
| 243 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 `em[0]` 的访问是安全的，因为 `em` 指针指向 `OPENSSL_malloc(num)` 分配的内存块起始位置，且循环 `for (from += flen, em += num, i = 0; i < num; ... |
| 244 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的。指针 `em` 指向大小为 `num` 的已分配内存，且循环 `for (i = 0; i < num; i++)` 确保了对 `em[0]` 到 `em[num-1]` 的初始化。只要 `nu... |
| 245 | git-2.47.1 | is_command | cpp/redundant-null-check-simple | 2602 | FP | FP | 告警指出的空指针检查是冗余的，因为变量 `nick` 是从结构体数组 `todo_command_info` 中直接读取的字符，并非指针，不存在空指针解引用风险。代码逻辑正确，工具误报了非指针变量的检查。 |
| 246 | git-2.47.1 | refname_is_safe | cpp/no-space-for-terminator | 350 | FP | FP | 函数 `xmallocz` 的调用参数 `restlen` 是字符串 `rest` 的长度，而 `rest` 本身是一个以空字符结尾的 C 字符串。`normalize_path_copy` 函数要求目标缓冲区足够容纳源字符串及其终止... |
| 247 | git-2.47.1 | fill_es_indent_data | cpp/offset-use-before-range-check | 894 | FP | FP | 在第一个while循环的条件中，对`s[off] == '\r'`的访问已通过`off < len - 1`进行了前置范围检查，确保了off在访问前不会等于或超过len，因此不存在越界读取的风险。 |
| 248 | git-2.47.1 | ce_write_entry | cpp/offset-use-before-range-check | 2687 | FP | FP | 变量 `common` 在 for 循环条件中已通过 `common < previous_name->len` 进行了范围检查，确保其不会超过 `previous_name->len`。后续使用 `ce->name + common... |
| 249 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 757 | FP | FP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，对 `pos` 的访问 `s1[pos]` 和 `s2[pos]` 发生在 `pos < len` 的范围检查之前，这违反了规则。然而，该循环的... |
| 250 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 757 | FP | FP | 循环条件 `s1[pos] == s2[pos] && pos < len` 确保了在访问 `s1[pos]` 和 `s2[pos]` 之前，`pos` 已经通过了 `pos < len` 的范围检查，因此不存在越界访问的风险。 |
| 251 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 792 | FP | FP | 在for循环条件 `wcs1[pos] == wcs2[pos] && pos < len` 中，对 `pos` 的访问 `wcs1[pos]` 和 `wcs2[pos]` 发生在 `pos < len` 的边界检查之前，这违反了先检... |
| 252 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 792 | FP | FP | 循环条件 `wcs1[pos] == wcs2[pos] && pos < len` 确保了在访问 `wcs1[pos]` 和 `wcs2[pos]` 之前，`pos` 已经通过了 `pos < len` 的范围检查，因此不存在越界访... |
| 253 | git-2.47.1 | setup_scoreboard | cpp/inconsistent-null-check | 2857 | FP | FP | 函数 get_blame_suspects 的定义显示，当 blame_suspects_peek 返回 NULL 时，它会返回 NULL。然而，在调用点，代码仅在 is_null_oid(&sb->final->object.oid... |
| 254 | git-2.47.1 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 函数 branch_get 在传入空名或 "HEAD" 时返回 the_repository->remote_state->current_branch，否则通过 make_branch 创建新分支结构体，两者均返回有效指针，不会返回... |
| 255 | git-2.47.1 | bisect_successful | cpp/inconsistent-null-check | 646 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `refs_read_ref` 检查了 `bad_ref` 是否存在，并获取了其 OID。这表明 `bad_ref` 是一个有效的引用，因此... |
| 256 | git-2.47.1 | update_head | cpp/inconsistent-null-check | 685 | FP | FP | 代码中 `refs_update_ref` 调用时指定了 `UPDATE_REFS_DIE_ON_ERR` 标志，若 `lookup_commit_reference` 返回 NULL 导致后续 `c->object.oid` 解引用... |
| 257 | git-2.47.1 | describe_commit | cpp/inconsistent-null-check | 324 | FP | FP | 函数 `lookup_commit_reference` 返回的指针 `cmit` 在后续代码中被直接解引用（如 `cmit->object.oid`），且切片中未包含任何针对该指针的判空检查或错误处理。虽然告警指出大多数调用会检查空... |
| 258 | git-2.47.1 | do_fetch | cpp/inconsistent-null-check | 1628 | FP | FP | 告警点 `branch = branch_get(NULL)` 的返回值被后续的 `branch_has_merge_config(branch)` 函数调用，该函数内部已对 `branch` 指针进行了空值检查（`return br... |
| 259 | git-2.47.1 | get_ref_map | cpp/inconsistent-null-check | 552 | FP | FP | 告警点 `branch_get(NULL)` 的返回值 `branch` 在后续代码中仅用于条件判断 `branch_has_merge_config(branch)`，该函数内部已对 `branch` 指针进行了空值检查（`retu... |
| 260 | git-2.47.1 | refspec_append_mapped | cpp/inconsistent-null-check | 90 | FP | FP | 被调用的 `branch_get` 函数内部已对 `name` 参数进行了空指针检查（`if (!name ｜｜ !*name ...)`），并会返回一个有效的 `struct branch` 指针（可能是 `current_bran... |
| 261 | git-2.47.1 | do_create_stash | cpp/inconsistent-null-check | 1390 | FP | FP | 告警点 `head_commit = lookup_commit(...)` 的返回值在后续代码中被直接使用（如 `head_commit->object.oid`），但切片显示 `info->b_commit` 来源于调用方传入的 ... |
| 262 | git-2.47.1 | reset_tree | cpp/inconsistent-null-check | 285 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将结果传递给 parse_tree 函数进行检查，如果解析失败（返回非零值）则函数返回错误。这构成了对返回值的有效检查，因此告警是误报。 |
| 263 | git-2.47.1 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1924 | FP | FP | 告警点后的代码直接解引用 `sub->name`，表明 `sub` 指针被假定为非空；结合 `submodule_from_path` 函数定义，它返回一个指向 `const struct submodule` 的指针，在 Git 代... |
| 264 | git-2.47.1 | write_bundle_refs | cpp/inconsistent-null-check | 435 | FP | FP | 在 `if (e->item == &(one->object))` 条件判断中，`one` 指针被直接解引用，这表明代码逻辑假设 `lookup_commit_reference` 的返回值非空。如果返回值为空，解引用将导致崩溃，但... |
| 265 | git-2.47.1 | update_one | cpp/inconsistent-null-check | 328 | FP | FP | find_subtree 在 create 参数为 1 时被调用，根据其定义，当找不到子树时会创建并返回一个新节点，不会返回 NULL。因此，对返回值进行空指针检查是多余的，告警为误报。 |
| 266 | git-2.47.1 | verify_one_commit_graph | cpp/inconsistent-null-check | 2774 | FP | FP | 代码中 `lookup_commit` 的返回值 `graph_commit` 被后续代码直接使用，未进行空值检查，但该函数在对象不存在时会通过 `create_object` 创建新对象并返回，不会返回 NULL。切片中 `look... |
| 267 | git-2.47.1 | unparse_commit | cpp/inconsistent-null-check | 188 | FP | FP | 切片代码显示，在调用`lookup_commit`后，代码立即访问`c->object.parsed`，这隐含了对`c`非空的假设。结合`lookup_commit`的实现，当`lookup_object`返回NULL时，它会调用`c... |
| 268 | git-2.47.1 | clear_common_flag | cpp/inconsistent-null-check | 2132 | FP | FP | 代码逻辑保证了`lookup_object`返回的对象指针非空。`oid`来源于`oidset_iter_next`，该迭代器仅在哈希表中存在有效条目时才返回一个有效的`oid`指针。`lookup_object`函数会查找并返回与该... |
| 269 | git-2.47.1 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 143 | FP | FP | 告警点 `parse_object` 的返回值被赋值给 `tag` 指针，并在下一行通过 `if (!tag->tagged)` 进行了隐式的空指针检查，这构成了有效的空值防护，因此该告警为误报。 |
| 270 | git-2.47.1 | find_merge_parents | cpp/inconsistent-null-check | 616 | FP | FP | 代码在调用 `parse_object` 后，其返回值 `obj` 被直接传递给 `add_merge_parent` 函数使用。`add_merge_parent` 函数仅使用 `obj->oid`，而 `obj` 是通过 `par... |
| 271 | git-2.47.1 | get_parent | cpp/inconsistent-null-check | 1107 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将其返回值 `commit` 传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 函数会检查 `commit` 的有... |
| 272 | git-2.47.1 | show_ambiguous_object | cpp/inconsistent-null-check | 442 | FP | FP | 代码在调用 `lookup_tag` 后，立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析和错误检查。`parse_tag` 函数内部会处理 `tag` 为 NULL 或无效的情况并返回错误，因此即使 `... |
| 273 | git-2.47.1 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3344 | FP | FP | 函数 `lookup_decoration` 在 `n->size` 为 0 或未找到匹配项时返回 NULL，但调用方 `leave_one_treesame_to_parent` 并未使用返回值 `ts`，因此空指针检查无关紧要，不... |
| 274 | git-2.47.1 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 701 | FP | FP | 提供的lookup_commit函数定义显示，当查找失败时，它会调用create_object创建一个新对象并返回，因此该函数永远不会返回NULL。代码无需进行空指针检查是安全的。 |
| 275 | git-2.47.1 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在内部已处理了 `NULL` 对象指针的情况，当 `obj` 为 `NULL` 时会调用 `create_object` 创建新对象并返回，因此调用方无需额外检查返回值是否为 `NULL`。 |
| 286 | git-2.47.1 | add_patterns | cpp/invalid-pointer-deref | 1151 | FP | FP | 代码在写入 `buf[size++] = '\n';` 之前，`buf` 是通过 `xmallocz(size)` 分配的，其中 `size` 是文件大小。`xmallocz` 分配的是 `size + 1` 字节（确保零结尾），因此... |
| 287 | git-2.47.1 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1660 | FP | FP | 代码中 `buffer = xmallocz_gently(size);` 分配了 `size` 字节的内存，随后 `stream.avail_out = size + 1;` 设置输出缓冲区大小为 `size + 1`，但 `git... |
| 288 | git-2.47.1 | should_prune_worktree | cpp/invalid-pointer-deref | 788 | FP | FP | 代码在写入 `path[len] = '\0';` 之前，已经通过 `while` 循环确保了 `len` 大于0且 `path[len - 1]` 是换行符时才递减 `len`，因此 `len` 不会变为负数，且 `xmallocz... |
| 289 | git-2.50.1 | refname_is_safe | cpp/no-space-for-terminator | 353 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，这是字符串 `rest` 的长度，而 `rest` 是 `skip_prefix` 处理后指向的原始字符串后缀。`normalize_path_copy` 函数要求目标缓冲... |
| 290 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 变量 `pos` 在 `for` 循环条件 `s1[pos] == s2[pos] && pos < len` 中被使用，但其值在每次迭代中由 `++pos` 更新，且循环条件确保了 `pos` 在访问数组前会先与 `len` 进行比... |
| 291 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，对`s1[pos]`和`s2[pos]`的访问发生在`pos < len`检查之前，这违反了先检查后使用的原则。然而，该循环的逻辑是当`s1[p... |
| 292 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 变量 `pos` 在 `for` 循环条件 `pos < len` 中已进行范围检查，其使用（在 `p_snprintf` 中）位于循环之后，因此不存在使用前未检查范围的问题。告警为误报。 |
| 293 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 变量 `pos` 在 `for` 循环条件 `pos < len` 中已进行范围检查，其值在后续 `p_snprintf` 中使用时是安全的，不会发生越界访问。 |
| 294 | git-2.50.1 | setup_scoreboard | cpp/inconsistent-null-check | 2858 | FP | FP | 告警点位于 `if (is_null_oid(&sb->final->object.oid))` 条件分支内，该条件已确保 `sb->final` 非空且其 OID 为空。`get_blame_suspects` 函数定义显示，当 `... |
| 295 | git-2.50.1 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的 `branch_get` 函数内部已对空指针输入进行了处理，并始终返回一个有效的 `struct branch` 指针（例如，当 `name` 为空时返回 `current_branch`），因此其返回值不可能为 NULL，... |
| 296 | git-2.50.1 | write_index_patch | cpp/inconsistent-null-check | 1435 | FP | FP | lookup_tree 被调用时传入的是已知的、有效的空树对象标识符（the_repository->hash_algo->empty_tree），该函数内部会确保返回一个有效的 tree 对象（通过 lookup_object 或 ... |
| 297 | git-2.50.1 | bisect_successful | cpp/inconsistent-null-check | 648 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `refs_read_ref` 检查了 `bad_ref` 是否存在，并获取了其 OID。后续使用 `commit->object.oid`... |
| 298 | git-2.50.1 | describe_commit | cpp/inconsistent-null-check | 326 | FP | FP | 函数 `lookup_commit_reference` 返回的指针 `cmit` 在后续代码中被直接解引用（如 `cmit->object.oid`），这表明调用者预期它非空。结合上下文，传入的 `oid` 参数应来自有效的对象引用... |
| 299 | git-2.50.1 | <global> | cpp/inconsistent-null-check | 547 | FP | FP | lookup_tree 调用传入的是 the_repository->hash_algo->empty_tree，这是一个已知的常量 OID，用于表示空树对象，不可能返回 NULL。因此无需进行空指针检查，告警为误报。 |
| 300 | git-2.50.1 | get_ref_map | cpp/inconsistent-null-check | 550 | FP | FP | 代码中 `branch_get(NULL)` 的返回值被立即传递给 `branch_has_merge_config` 函数，而该函数内部已包含对 `branch` 指针是否为 NULL 的检查（`return branch && !... |
| 301 | git-2.50.1 | refspec_append_mapped | cpp/inconsistent-null-check | 92 | FP | FP | 告警点位于条件分支 `if (branch->merge_nr == 1 && branch->merge[0]->src)` 内，该条件仅在 `branch` 指针非空时才会被求值。如果 `branch_get` 返回 NULL，程... |
| 302 | git-2.50.1 | do_create_stash | cpp/inconsistent-null-check | 1397 | FP | FP | 告警点 `head_commit = lookup_commit(...)` 的返回值在后续代码中被直接使用（如 `head_commit->object.oid`），但 `lookup_commit` 函数定义显示它不会返回 NUL... |
| 303 | git-2.50.1 | reset_tree | cpp/inconsistent-null-check | 286 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将返回值传递给 parse_tree 函数进行检查。如果 parse_tree_indirect 返回 NULL，parse_tree 会处理该错误并返回 -1，导致函数提前... |
| 304 | git-2.50.1 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1932 | FP | FP | 告警点后的代码直接使用了 `sub->name`，这表明 `sub` 指针被假定为非空。结合 `submodule_from_path` 的函数定义，它返回一个 `const struct submodule *`，且没有文档或代码表... |
| 305 | git-2.50.1 | update_one | cpp/inconsistent-null-check | 333 | FP | FP | 调用 find_subtree 时传入的 create 参数为 1，根据其函数定义，当 create 为真时，函数会分配并返回一个新的子树结构，不会返回 NULL。因此，此处无需检查 NULL，告警为误报。 |
| 306 | git-2.50.1 | verify_one_commit_graph | cpp/inconsistent-null-check | 2798 | FP | FP | 函数 `lookup_commit` 在切片中显示，当对象不存在时会调用 `create_object` 创建一个新的提交对象并返回，因此它不会返回 NULL。代码逻辑保证了返回值非空，无需进行空指针检查。 |
| 307 | git-2.50.1 | unparse_commit | cpp/inconsistent-null-check | 189 | FP | FP | 函数 `lookup_commit` 在内部已处理了 `lookup_object` 返回 NULL 的情况，会调用 `create_object` 创建一个新对象并返回，因此其返回值不会为 NULL。后续代码直接访问 `c->obj... |
| 308 | git-2.50.1 | clear_common_flag | cpp/inconsistent-null-check | 2146 | FP | FP | 代码逻辑保证了`lookup_object`返回的对象指针非空。`oid`来源于`oidset_iter_next`，该函数仅在集合中存在元素时才返回有效的`oid`，且`lookup_object`在哈希表中查找该`oid`对应的对... |
| 309 | git-2.50.1 | deref_without_lazy_fetch | cpp/inconsistent-null-check | 156 | FP | FP | 告警点位于一个已确认对象类型为OBJ_TAG的代码块内，且该代码块仅在oid_object_info_extended调用成功（返回0）后才会执行，这隐含了对象存在且可访问。此外，后续代码直接访问tag->tagged而未发生崩溃，进... |
| 310 | git-2.50.1 | find_merge_parents | cpp/inconsistent-null-check | 617 | FP | FP | parse_object 返回的 obj 指针在后续代码中仅用于获取其 oid 字段（&obj->oid），该操作在 obj 为 NULL 时会导致未定义行为。然而，告警点之前的 parse_oid_hex 调用已对输入格式进行了严格... |
| 311 | git-2.50.1 | get_parent | cpp/inconsistent-null-check | 1110 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将其结果 `commit` 传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 函数会检查提交对象的有效性，如果 `... |
| 312 | git-2.50.1 | show_ambiguous_object | cpp/inconsistent-null-check | 443 | FP | FP | 代码在调用 `lookup_tag` 后，立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析检查，`parse_tag` 函数内部会处理 `tag` 为 NULL 的情况并返回错误，因此存在隐式的空值检查，... |
| 313 | git-2.50.1 | setup_pending_objects | cpp/inconsistent-null-check | 333 | FP | FP | 告警点对 `strmap_get` 的返回值 `root_tree_list` 进行了后续使用（`oid_array_append(&root_tree_list->oids, &obj->oid)`），但切片代码显示，该使用发生在 ... |
| 314 | git-2.50.1 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3351 | FP | FP | 函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到项（`!ref->base`）的情况进行了处理，并明确返回 `NULL`。调用方 `leave_one_treesame_to_parent... |
| 315 | git-2.50.1 | add_cache_tree | cpp/inconsistent-null-check | 1775 | FP | FP | `lookup_tree`函数内部已对空指针进行了检查，若`obj`为空则调用`create_object`创建新对象并返回，因此其返回值不会为空，无需外部检查。 |
| 316 | git-2.50.1 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 706 | FP | FP | 告警点位于循环中，其输入 `oid` 数组来自 `info->shallow->oid`，而循环次数 `nr_shallow` 由 `info->ours` 和 `info->theirs` 数组合并确定，这表明 `lookup_co... |
| 317 | git-2.50.1 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在内部已处理空指针情况，若 `lookup_object` 返回空，它会调用 `create_object` 创建新对象并返回，因此调用方无需额外检查返回值是否为空。 |
| 318 | git-2.50.1 | has_uncommitted_changes | cpp/inconsistent-null-check | 2642 | FP | FP | lookup_tree 的参数是常量 the_hash_algo->empty_tree，代表一个已知存在的空树对象，因此函数不会返回 NULL，无需检查。告警是工具对通用模式的误判。 |
| 319 | git-2.50.1 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是字符串字面量 `DIGIT "abcdefABCDEF"`，其 `ARRAY_SI... |
| 320 | git-2.50.1 | test_ctype__ispunct | cpp/overflow-buffer | 91 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，但 `string` 是宏参数，此处为 `"PUNCT"` 字符串字面量。`ARRAY_SIZE` 计算... |
| 321 | git-2.50.1 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | FP | FP | 宏 `TEST_CHAR_CLASS` 中 `ARRAY_SIZE(string) - 1` 的索引操作 `string[-1]` 仅出现在 `BUILD_ASSERT_OR_ZERO` 宏的编译时断言中，用于确保数组大小大于零，该表... |
| 322 | git-2.50.1 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，其中 `string` 是字符串字面量 `"!\"#%&',-/:;<=>@_`~"`，其大小固定且大于0... |
| 323 | git-2.50.1 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在数组大小为0时结果为-1，但宏内已通过 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)` ... |
| 324 | git-2.50.1 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | FP | FP | 告警指出的负索引访问发生在宏 `ARRAY_SIZE(string) - 1` 中，其中 `string` 是字符串字面量 `"*?[\\"`，其 `ARRAY_SIZE` 计算结果大于0，因此 `ARRAY_SIZE(string)... |
| 325 | git-2.50.1 | test_ctype__isalnum | cpp/overflow-buffer | 51 | FP | FP | 宏定义中 `ARRAY_SIZE(string) - 1` 仅在数组大小为0时结果为-1，但宏内已通过 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)` 断言数组大小大于0，确保了索引非负。... |
| 326 | git-2.50.1 | test_ctype__isalpha | cpp/overflow-buffer | 46 | FP | FP | 宏 `TEST_CHAR_CLASS` 中 `len` 的计算包含 `ARRAY_SIZE(string) - 1`，但 `string` 宏参数为 `LOWER UPPER`，展开后是一个字符串字面量，其 `ARRAY_SIZE` ... |
| 327 | git-2.50.1 | test_ctype__isdigit | cpp/overflow-buffer | 41 | FP | FP | 宏 `TEST_CHAR_CLASS` 中 `ARRAY_SIZE(string) - 1` 的索引操作仅在 `ARRAY_SIZE(string)` 为0时才可能为负，但宏内包含 `BUILD_ASSERT_OR_ZERO(ARRA... |
| 328 | git-2.50.1 | <global> | cpp/overflow-buffer | 36 | FP | FP | 切片代码显示函数体为空，不存在任何数组索引操作，因此告警所描述的访问负索引-1的情况不可能发生，属于工具误报。 |
| 329 | git-2.50.1 | add_patterns | cpp/invalid-pointer-deref | 1152 | FP | FP | 代码在分配缓冲区时使用 `xmallocz(size)`，该函数分配 `size+1` 字节并清零，因此 `buf[size] = '\n'` 的写入操作在分配范围内，不会越界。 |
| 330 | git-2.50.1 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1684 | FP | FP | 代码中 `buffer = xmallocz_gently(size);` 分配了 `size` 字节的内存，但后续 `stream.avail_out = size + 1;` 和循环条件 `if (!stream.avail_ou... |
| 331 | git-2.50.1 | should_prune_worktree | cpp/invalid-pointer-deref | 965 | FP | FP | 告警点 `path[len] = '\0';` 前有 `while` 循环确保 `len` 被递减，只要 `len` 初始值大于0，写入位置 `path + len` 就在 `xmallocz(len)` 分配的缓冲区范围内。`xma... |
| 332 | git-2.49.0 | is_command | cpp/redundant-null-check-simple | 2614 | FP | FP | 告警指出的空指针检查冗余，是针对变量 `nick` 的检查。`nick` 是从结构体数组 `todo_command_info[command].c` 中直接读取的字符，并非指针，因此对其进行的空值检查 `(nick && ...)`... |
| 333 | git-2.49.0 | refname_is_safe | cpp/no-space-for-terminator | 353 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，而 `restlen` 是 `strlen(rest)` 的结果，不包含终止符的长度。`normalize_path_copy` 函数要求目标缓冲区足够容纳源字符串及其终止... |
| 334 | git-2.49.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 895 | FP | FP | 切片代码显示，在第一个while循环的条件中，对`s[off]`的访问已通过`off < len - 1`进行了范围检查，确保了off在访问`s`时不会越界。因此，该告警是误报。 |
| 335 | git-2.49.0 | ce_write_entry | cpp/offset-use-before-range-check | 2689 | FP | FP | 变量 `common` 在 for 循环条件中已通过 `common < previous_name->len` 进行了范围检查，确保其值小于 previous_name 的长度，后续使用 `ce->name + common` 和 ... |
| 336 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 变量 `pos` 在 `for` 循环条件 `s1[pos] == s2[pos] && pos < len` 中，其访问 `s1[pos]` 和 `s2[pos]` 发生在 `pos < len` 的边界检查之前，这触发了告警。然而... |
| 337 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在循环条件 `s1[pos] == s2[pos] && pos < len` 中，对 `pos` 的访问 `s1[pos]` 和 `s2[pos]` 发生在范围检查 `pos < len` 之前，这违反了规则。然而，该循环的目的是在... |
| 338 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 变量 `pos` 在 `for` 循环条件 `pos < len` 中已进行范围检查，确保其值在后续 `p_snprintf` 中使用时不会越界。该告警是工具对循环条件检查顺序的误判。 |
| 339 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 告警点位于一个用于查找两个宽字符串首个不同字节位置的循环条件中，该循环条件 `pos < len` 确保了 `pos` 变量在后续 `p_snprintf` 中使用时不会超出 `len` 的范围，因此不存在越界访问风险。 |
| 340 | git-2.49.0 | setup_scoreboard | cpp/inconsistent-null-check | 2858 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，此时 `sb->final` 非空且其 object.oid 为空哈希。`get_blame_suspects` 函数定义显示，... |
| 341 | git-2.49.0 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的函数 `branch_get` 在传入空名或特定值时会返回 `the_repository->remote_state->current_branch`，否则会调用 `make_branch` 创建新分支对象，两种路径均返回有... |
| 342 | git-2.49.0 | write_index_patch | cpp/inconsistent-null-check | 1433 | FP | FP | lookup_tree 被调用时传入的是 the_repository->hash_algo->empty_tree，这是一个已知的、有效的内部对象标识符，不会返回 NULL。因此，无需进行空值检查，告警为误报。 |
| 343 | git-2.49.0 | bisect_successful | cpp/inconsistent-null-check | 648 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，已经通过 `refs_read_ref` 检查了引用 `bad_ref` 是否存在并获取了其 OID。这表明代码逻辑确保了该引用是有效的，因此后续的 c... |
| 344 | git-2.49.0 | describe_commit | cpp/inconsistent-null-check | 326 | FP | FP | 函数 `lookup_commit_reference` 返回的指针 `cmit` 在后续代码中被直接解引用（如 `cmit->object.oid`），且没有前置的NULL检查。然而，根据告警规则 `cpp/inconsistent... |
| 345 | git-2.49.0 | <global> | cpp/inconsistent-null-check | 546 | FP | FP | 告警点 `lookup_tree` 的返回值 `tree` 被直接传递给 `add_pending_object`，而 `add_pending_object` 的函数定义显示其参数 `obj` 并未被检查是否为 NULL，但调用方 ... |
| 346 | git-2.49.0 | do_fetch | cpp/inconsistent-null-check | 1756 | FP | FP | 告警点 `branch = branch_get(NULL)` 的返回值 `branch` 在后续条件 `branch_has_merge_config(branch)` 中被使用，该函数内部已包含对 `branch` 是否为 `NU... |
| 347 | git-2.49.0 | get_ref_map | cpp/inconsistent-null-check | 551 | FP | FP | 切片代码显示，在调用 `branch_get(NULL)` 后，其返回值 `branch` 被立即传递给 `branch_has_merge_config(branch)` 函数，该函数内部已包含对 `branch` 是否为 NULL... |
| 348 | git-2.49.0 | refspec_append_mapped | cpp/inconsistent-null-check | 92 | FP | FP | 被调用的 `branch_get` 函数内部已对 `name` 参数进行了空指针检查（`if (!name ｜｜ !*name ...)`），并返回一个有效的 `struct branch` 指针（`the_repository->r... |
| 349 | git-2.49.0 | do_create_stash | cpp/inconsistent-null-check | 1398 | FP | FP | `lookup_commit` 函数在失败时会返回一个新建的 commit 对象（通过 `create_object`），而非 NULL，因此调用后无需进行 NULL 检查。切片中提供的函数定义证实了这一点。 |
| 350 | git-2.49.0 | reset_tree | cpp/inconsistent-null-check | 287 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将结果传递给 parse_tree 函数，后者内部会检查指针有效性并返回错误码。函数对 parse_tree 的返回值进行了检查，若失败则返回 -1，这构成了对 parse_... |
| 352 | git-2.49.0 | update_one | cpp/inconsistent-null-check | 329 | FP | FP | 在调用 `find_subtree(it, path + baselen, sublen, 1)` 时，最后一个参数 `create` 为 1，根据 `find_subtree` 函数的定义，当 `create` 为真且子树不存在时，... |
| 353 | git-2.49.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2788 | FP | FP | 函数 `lookup_commit` 在内部已处理了空对象的情况，若对象不存在则会调用 `create_object` 创建一个新的提交对象并返回，因此该调用永远不会返回 NULL，无需进行空值检查。 |
| 354 | git-2.49.0 | unparse_commit | cpp/inconsistent-null-check | 188 | FP | FP | 函数 `lookup_commit` 在内部已处理 `NULL` 情况，当 `lookup_object` 返回 `NULL` 时会创建新对象并返回，因此其返回值不会为 `NULL`，告警为误报。 |
| 355 | git-2.49.0 | clear_common_flag | cpp/inconsistent-null-check | 2147 | FP | FP | 在while循环条件 `while ((oid = oidset_iter_next(&iter)))` 中，`oidset_iter_next` 返回NULL时循环终止，因此循环体内 `oid` 必然非空。`lookup_objec... |
| 356 | git-2.49.0 | deref_without_lazy_fetch | cpp/inconsistent-null-check | 156 | FP | FP | 在调用 parse_object 之前，代码已通过 oid_object_info_extended 检查了对象类型，并确认其为 OBJ_TAG。对于 TAG 对象，parse_object 预期返回有效指针，且后续代码直接访问 ta... |
| 357 | git-2.49.0 | find_merge_parents | cpp/inconsistent-null-check | 617 | FP | FP | 告警点`obj = parse_object(...)`的返回值被立即传递给`repo_peel_to_type`函数，而`repo_peel_to_type`的定义显示其内部会检查`parse_object`的返回值是否为NULL，... |
| 358 | git-2.49.0 | get_parent | cpp/inconsistent-null-check | 1108 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将其结果 `commit` 传递给 `repo_parse_commit` 进行校验。`repo_parse_commit` 会检查提交对象的有效性，若失败则函数... |
| 359 | git-2.49.0 | show_ambiguous_object | cpp/inconsistent-null-check | 443 | FP | FP | 代码在调用 `lookup_tag` 后，立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析。`parse_tag` 函数内部会检查 `tag` 是否为 NULL（通过 `item->object.pars... |
| 360 | git-2.49.0 | setup_pending_objects | cpp/inconsistent-null-check | 333 | FP | FP | 切片代码显示，在调用 `strmap_get` 获取 `root_tree_list` 后，后续代码（`oid_array_append(&root_tree_list->oids, &obj->oid)`）仅在 `root_tree... |
| 361 | git-2.49.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3357 | FP | FP | 函数 `lookup_decoration` 在装饰表为空或未找到对象时明确返回 NULL，但调用方 `leave_one_treesame_to_parent` 并未使用其返回值 `ts`，因此不存在解引用空指针的风险，属于工具误报。 |
| 362 | git-2.49.0 | add_cache_tree | cpp/inconsistent-null-check | 1783 | FP | FP | 函数 `lookup_tree` 在内部已处理空指针情况，若 `lookup_object` 返回空，它会调用 `create_object` 创建新对象并返回，因此其返回值不会为空，无需额外检查。 |
| 363 | git-2.49.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 703 | FP | FP | 函数 `lookup_commit` 在内部已处理了空对象指针的情况，若未找到对象会通过 `create_object` 创建新对象并返回，因此调用方无需进行空指针检查。 |
| 364 | git-2.49.0 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在对象不存在时会调用 `create_object` 创建一个新对象并返回，因此不会返回 NULL。代码后续直接使用 `c->date` 是安全的，告警为误报。 |
| 365 | git-2.49.0 | has_uncommitted_changes | cpp/inconsistent-null-check | 2642 | FP | FP | lookup_tree 函数被调用时，其参数是固定的空树哈希值 `the_hash_algo->empty_tree`，这是一个已知有效的内部常量，因此函数不会返回 NULL，无需检查。告警属于工具对通用模式的误判。 |
| 366 | git-2.49.0 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是字符串字面量 `DIGIT "abcdefABCDEF"`，其 `ARRAY_SI... |
| 367 | git-2.49.0 | test_ctype__ispunct | cpp/overflow-buffer | 91 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在数组大小为0时结果为-1，但宏内已通过 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)` ... |
| 368 | git-2.49.0 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | FP | FP | 宏 `TEST_CHAR_CLASS` 中 `ARRAY_SIZE(string) - 1` 的索引操作是安全的，因为 `ARRAY_SIZE` 宏确保数组大小至少为1，且 `BUILD_ASSERT_OR_ZERO` 在编译时断言数... |
| 369 | git-2.49.0 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | FP | FP | 告警指出的负索引访问发生在宏 `ARRAY_SIZE(string) - 1` 中，但该表达式受 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)` 保护，确保数组大小大于0，因此 `len`... |
| 370 | git-2.49.0 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但传入的 `string` 是一个字符串字面量 `"$()*+.?[\\^{｜"`，其 `ARRAY_SI... |
| 371 | git-2.49.0 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 用于计算字符串长度，当 `string` 为空时可能导致负索引。但此处传入的实参 `"*?[\\"` 是一个非空字符串字面量，`ARRAY... |
| 372 | git-2.49.0 | test_ctype__isalnum | cpp/overflow-buffer | 51 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但该宏内部已通过 `BUILD_ASSERT_OR_ZERO(AR... |
| 373 | git-2.49.0 | test_ctype__isalpha | cpp/overflow-buffer | 46 | FP | FP | 宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含 `ARRAY_SIZE(string) - 1`，但 `string` 宏参数 `LOWER UPPER` 展开后是一个非空字符串字面量，`ARRAY_SIZE` 结... |
| 374 | git-2.49.0 | test_ctype__isdigit | cpp/overflow-buffer | 41 | FP | FP | 告警针对宏 `TEST_CHAR_CLASS` 中的 `string[-1]` 访问，但切片显示 `string` 是宏参数，调用时传入的 `DIGIT` 是一个字符串字面量，其 `ARRAY_SIZE` 必然大于0，因此 `len`... |
| 375 | git-2.49.0 | <global> | cpp/overflow-buffer | 36 | FP | FP | 切片代码显示函数体为空，不存在任何数组索引操作，因此告警所描述的访问负索引-1的情况不可能发生，属于工具误报。 |
| 377 | git-2.49.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1677 | FP | FP | 代码中 `buffer = xmallocz_gently(size);` 分配了 `size` 字节的内存，随后 `stream.avail_out = size + 1;` 设置输出缓冲区大小为 `size + 1`，而 `git... |
| 378 | git-2.49.0 | should_prune_worktree | cpp/invalid-pointer-deref | 960 | FP | FP | 代码在写入 path[len] = '\0' 前，通过 while 循环确保了 len 已递减至最后一个非换行符字符的位置，因此 len 必然小于原始分配大小，写入操作不会越界。 |
| 379 | git-2.46.0 | is_command | cpp/redundant-null-check-simple | 2601 | FP | FP | 告警指出的空指针解引用检查是冗余的，但分析代码逻辑发现，变量 `nick` 是直接从结构体数组中读取的字符，并非指针，因此该告警是对代码的误读。规则误将字符变量识别为指针并触发了冗余检查警告。 |
| 380 | git-2.46.0 | refname_is_safe | cpp/no-space-for-terminator | 345 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，即字符串 `rest` 的长度。由于 `rest` 是 `skip_prefix` 处理后指向的 C 字符串，其长度 `restlen` 由 `strlen(rest)` ... |
| 381 | git-2.46.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 890 | FP | FP | 在第一个while循环的条件中，对`s[off]`的访问已通过`off < len - 1`进行了范围检查，确保了在访问`s[off]`时`off`不会超出`s`的有效长度。因此，该告警是误报。 |
| 382 | git-2.46.0 | ce_write_entry | cpp/offset-use-before-range-check | 2685 | FP | FP | 变量 `common` 在 for 循环条件中已通过 `common < previous_name->len` 进行了范围检查，确保其值小于 previous_name->len，后续使用 `ce->name + common` 和... |
| 383 | git-2.46.0 | setup_scoreboard | cpp/inconsistent-null-check | 2857 | FP | FP | 函数 get_blame_suspects 的定义显示，当查找失败时它会返回 NULL。然而，在调用点之前存在条件 `if (is_null_oid(&sb->final->object.oid))`，这表明 `sb->final` ... |
| 384 | git-2.46.0 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的 `branch_get` 函数内部已对 `name` 参数进行空指针和空字符串检查，并返回一个有效的 `struct branch` 指针（`the_repository->remote_state->current_bra... |
| 385 | git-2.46.0 | bisect_successful | cpp/inconsistent-null-check | 644 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `refs_read_ref` 检查了 `bad_ref` 是否存在，并获取了其 OID。这表明 `bad_ref` 是一个有效的引用，因此... |
| 386 | git-2.46.0 | update_head | cpp/inconsistent-null-check | 684 | FP | FP | 代码中 `refs_update_ref` 调用时指定了 `UPDATE_REFS_DIE_ON_ERR` 标志，若 `lookup_commit_reference` 返回 NULL 导致后续 `c->object.oid` 解引用... |
| 387 | git-2.46.0 | describe_commit | cpp/inconsistent-null-check | 323 | FP | FP | 函数 `lookup_commit_reference` 返回的指针 `cmit` 在后续代码中被直接解引用（如 `cmit->object.oid`），且没有前置的 NULL 检查。然而，根据告警规则 `cpp/inconsiste... |
| 388 | git-2.46.0 | do_fetch | cpp/inconsistent-null-check | 1626 | FP | FP | 告警点调用的 `branch_get(NULL)` 函数在传入 NULL 参数时，其内部逻辑会返回 `the_repository->remote_state->current_branch`，这是一个有效的结构体指针或 NULL，且... |
| 389 | git-2.46.0 | get_ref_map | cpp/inconsistent-null-check | 551 | FP | FP | 代码切片显示，在调用 `branch_get(NULL)` 后，其返回值 `branch` 被立即传递给 `branch_has_merge_config(branch)` 函数。该函数内部已包含对 `branch` 是否为 NULL... |
| 390 | git-2.46.0 | refspec_append_mapped | cpp/inconsistent-null-check | 88 | FP | FP | 函数 branch_get 内部已对 name 参数进行空指针和空字符串检查，并返回有效的 branch 结构体指针或 the_repository->remote_state->current_branch，其返回值不可能为 NUL... |
| 391 | git-2.46.0 | do_create_stash | cpp/inconsistent-null-check | 1388 | FP | FP | `lookup_commit` 函数在失败时会返回一个新建的 commit 对象，而非 NULL，因此调用后无需进行 NULL 检查。切片中提供的函数定义证实了这一点，所以该告警是误报。 |
| 392 | git-2.46.0 | reset_tree | cpp/inconsistent-null-check | 283 | FP | FP | 函数 `parse_tree_indirect` 的返回值 `tree` 在下一行立即作为参数传递给 `parse_tree(tree)`，后者内部会调用 `parse_tree_gently(tree, 0)` 进行解析和错误处理。... |
| 394 | git-2.46.0 | write_bundle_refs | cpp/inconsistent-null-check | 430 | FP | FP | 在调用 `lookup_commit_reference` 后，其返回值 `one` 仅在条件 `if (e->item == &(one->object))` 中被使用。该条件在 `one` 为 NULL 时访问 `one->obj... |
| 395 | git-2.46.0 | update_one | cpp/inconsistent-null-check | 327 | FP | FP | 告警点调用 `find_subtree` 时传入的 `create` 参数为 1，根据其函数定义，当 `create` 为 1 时，函数会分配新子树并返回非空指针，不会返回 NULL。因此无需进行空指针检查，工具告警为误报。 |
| 396 | git-2.46.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2774 | FP | FP | `lookup_commit` 函数在内部处理了空对象的情况，若未找到对象会通过 `create_object` 创建一个新的提交对象并返回，因此其返回值不会为 NULL。代码后续对 `graph_commit` 的使用（如访问 `g... |
| 397 | git-2.46.0 | ahead_behind | cpp/inconsistent-null-check | 1069 | FP | FP | 函数 `prio_queue_get` 在队列为空时返回 NULL，但调用点位于 `while (queue_has_nonstale(&queue))` 循环内，该循环条件已确保队列中存在非 STALE 的提交，因此 `prio_q... |
| 398 | git-2.46.0 | paint_down_to_common | cpp/inconsistent-null-check | 81 | FP | FP | 函数 `prio_queue_get` 在队列为空时返回 NULL，但调用点位于 `while (queue_has_nonstale(&queue))` 循环内，该循环条件已确保队列中至少存在一个非 STALE 的提交，因此 `pr... |
| 399 | git-2.46.0 | unparse_commit | cpp/inconsistent-null-check | 182 | FP | FP | 函数 `lookup_commit` 在内部已处理 `NULL` 情况，当 `lookup_object` 返回 `NULL` 时会调用 `create_object` 创建新对象并返回，因此其返回值不会为 `NULL`，无需额外检查。 |
| 400 | git-2.46.0 | clear_common_flag | cpp/inconsistent-null-check | 2130 | FP | FP | 代码逻辑保证了`lookup_object`的调用不会返回NULL。`oid`来源于`oidset_iter_next`，该函数仅在哈希集中存在有效条目时才返回非空指针，且`while ((oid = oidset_iter_next... |
| 401 | git-2.46.0 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 143 | FP | FP | 告警点位于一个无限循环中，其前置条件 `oid_object_info_extended` 调用已失败返回 NULL，使得 `parse_object` 的调用路径不可达。因此，对 `parse_object` 返回值的空检查是冗余的... |
| 402 | git-2.46.0 | find_merge_parents | cpp/inconsistent-null-check | 616 | FP | FP | 告警点`obj = parse_object(...)`的返回值`obj`在后续代码中直接传递给`add_merge_parent`函数使用，而该函数仅使用`obj->oid`字段。切片显示`obj`来自`parse_object`，... |
| 404 | git-2.46.0 | get_parent | cpp/inconsistent-null-check | 1098 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将其返回值 `commit` 传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 函数会检查提交对象的有效性，如果 ... |
| 405 | git-2.46.0 | show_ambiguous_object | cpp/inconsistent-null-check | 436 | FP | FP | 代码在调用 `lookup_tag` 后，立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析检查。`parse_tag` 函数内部会处理 `tag` 为 NULL 或无效的情况并返回错误，且后续的 `if ... |
| 407 | git-2.46.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3339 | FP | FP | 函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到项（`!ref->base`）的情况进行了处理，并明确返回 NULL。调用方 `leave_one_treesame_to_parent` ... |
| 408 | git-2.46.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 690 | FP | FP | 函数 `lookup_commit` 在切片中显示，当 `obj` 为 NULL 时会调用 `create_object` 创建并返回一个有效的 commit 对象，不会返回 NULL。因此，调用点无需进行 NULL 检查，告警为误报。 |
| 409 | git-2.46.0 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `test_parse_commit_in_graph` 是一个测试函数，其参数 `commit_oid` 由测试用例控制，预期是有效的对象ID。`lookup_commit` 在对象不存在时会创建新对象，不会返回NULL，因此... |
| 421 | git-2.46.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1649 | FP | FP | 代码中 `buffer = xmallocz_gently(size)` 分配了 `size` 字节，但 `stream.avail_out = size + 1` 和 `git_inflate` 循环确保解压后 `stream.av... |
| 422 | git-2.46.0 | should_prune_worktree | cpp/invalid-pointer-deref | 788 | FP | FP | 代码在写入 `path[len] = '\0';` 前，通过 `while` 循环确保了 `len` 已递减至最后一个非换行符字符的位置，因此 `len` 必然小于原始分配的缓冲区大小 `len`（原始值），写入操作在边界内。 |
| 423 | git-2.44.0 | is_command | cpp/redundant-null-check-simple | 2522 | FP | FP | 告警指出的空指针检查冗余，是针对变量 `nick` 的检查 `(nick && *p++ == nick)`。`nick` 是从结构体数组 `todo_command_info[command].c` 中直接读取的字符，并非指针，因此... |
| 424 | git-2.44.0 | refname_is_safe | cpp/no-space-for-terminator | 342 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，即字符串 `rest` 的长度。`rest` 是 `refname` 去掉前缀 `"refs/"` 后的剩余部分，且 `restlen` 由 `strlen(rest)` ... |
| 425 | git-2.44.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 869 | FP | FP | 切片代码显示，在第一个while循环的条件`s[off] == '\r' && off < len - 1`中，对偏移量`off`的访问已受到`off < len - 1`的保护，确保了`off`不会越界访问字符串`s`。因此，该告警... |
| 426 | git-2.44.0 | ce_write_entry | cpp/offset-use-before-range-check | 2713 | FP | FP | 变量 `common` 在 for 循环条件中已通过 `common < previous_name->len` 进行了范围检查，确保其不会超过 `previous_name->len`，后续使用 `ce->name + common... |
| 427 | git-2.44.0 | setup_scoreboard | cpp/inconsistent-null-check | 2855 | FP | FP | 函数 `get_blame_suspects` 的定义显示其可能返回 NULL，但调用点 `o = get_blame_suspects(sb->final);` 位于 `if (is_null_oid(&sb->final->obj... |
| 428 | git-2.44.0 | inherit_tracking | cpp/inconsistent-null-check | 224 | FP | FP | 被调用的函数 branch_get 在输入为 NULL 或空字符串时会返回 the_repository->remote_state->current_branch，该返回值是一个有效的结构体指针，因此调用后无需进行 NULL 检查。 |
| 429 | git-2.44.0 | bisect_successful | cpp/inconsistent-null-check | 640 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `read_ref(bad_ref, &oid)` 读取了引用，若引用不存在，`read_ref` 会失败并导致函数提前返回（未在切片中显示... |
| 430 | git-2.44.0 | update_head | cpp/inconsistent-null-check | 648 | FP | FP | 函数 `lookup_commit_reference` 返回的指针 `c` 被直接传递给 `update_ref`，而 `update_ref` 的最后一个参数是 `UPDATE_REFS_DIE_ON_ERR`，这意味着如果更新引... |
| 431 | git-2.44.0 | describe_commit | cpp/inconsistent-null-check | 320 | FP | FP | 函数 `lookup_commit_reference` 在失败时会返回 NULL，但切片代码显示，在调用 `lookup_commit_reference` 后，代码立即通过 `cmit->object.oid` 访问其成员。如果 ... |
| 432 | git-2.44.0 | do_fetch | cpp/inconsistent-null-check | 1611 | FP | FP | 代码在调用 `branch_get(NULL)` 后，立即在 `if (branch_has_merge_config(branch) && ...)` 中使用了 `branch` 指针。`branch_has_merge_confi... |
| 433 | git-2.44.0 | get_ref_map | cpp/inconsistent-null-check | 550 | FP | FP | 函数 `branch_get(NULL)` 在传入 NULL 参数时返回 `the_repository->remote_state->current_branch`，该返回值可能为 NULL，但后续 `branch_has_merg... |
| 434 | git-2.44.0 | cmd_merge | cpp/inconsistent-null-check | 1638 | FP | FP | 代码在访问 `common_one->item` 前已通过 `repo_get_merge_bases` 获取了有效的合并基列表，且后续逻辑（如 `oideq` 比较）表明 `common_item` 被安全使用，未出现空指针解引用。... |
| 435 | git-2.44.0 | refspec_append_mapped | cpp/inconsistent-null-check | 88 | FP | FP | 被调用的 `branch_get` 函数内部已对 `name` 参数进行了空指针和空字符串检查，并返回有效的 `struct branch` 指针（例如 `the_repository->remote_state->current_b... |
| 436 | git-2.44.0 | do_create_stash | cpp/inconsistent-null-check | 1378 | FP | FP | 函数 `lookup_commit` 在失败时会返回一个新建的 `commit` 对象（见其定义），不会返回 NULL。因此，对该函数的返回值进行 NULL 检查是不必要的，告警属于误报。 |
| 437 | git-2.44.0 | reset_tree | cpp/inconsistent-null-check | 283 | FP | FP | 告警点 `tree = parse_tree_indirect(i_tree);` 的返回值 `tree` 在下一行 `if (parse_tree(tree))` 中被直接使用，`parse_tree` 函数内部会调用 `parse... |
| 438 | git-2.44.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1838 | FP | FP | 切片代码中，在调用 `sub->name` 之前，存在对 `sub->update_strategy.type` 的访问，这表明 `sub` 指针已被解引用且未触发空指针崩溃。结合代码上下文，`submodule_from_path`... |
| 439 | git-2.44.0 | write_bundle_refs | cpp/inconsistent-null-check | 428 | FP | FP | 在调用 `lookup_commit_reference` 后，代码立即通过 `e->item == &(one->object)` 访问了 `one->object` 成员，这隐含地检查了 `one` 不为空指针，因为对空指针解引用... |
| 440 | git-2.44.0 | update_one | cpp/inconsistent-null-check | 325 | FP | FP | find_subtree 函数在 create 参数为 1 时保证返回非空指针（若分配失败会通过 ALLOC_GROW 或 FLEX_ALLOC_MEM 内部的 die 终止程序），因此调用后无需检查 NULL。代码逻辑正确，告警为误报。 |
| 441 | git-2.44.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2722 | FP | FP | lookup_commit 函数在内部已处理了对象不存在的情况（通过 create_object 创建新对象），且后续代码（如 repo_parse_commit_internal）会验证并报告错误，因此此处无需显式检查 NULL。告... |
| 442 | git-2.44.0 | ahead_behind | cpp/inconsistent-null-check | 1010 | FP | FP | 函数 `prio_queue_get` 在队列为空时返回 NULL，但调用点位于 `while (queue_has_nonstale(&queue))` 循环内，该循环条件已确保队列中至少存在一个非 STALE 的提交，因此 `pr... |
| 443 | git-2.44.0 | paint_down_to_common | cpp/inconsistent-null-check | 78 | FP | FP | 函数 `prio_queue_get` 在队列为空时返回 NULL，但调用点位于 `while (queue_has_nonstale(&queue))` 循环内，该循环条件已确保队列中至少存在一个非 STALE 的提交，因此 `pr... |
| 444 | git-2.44.0 | unparse_commit | cpp/inconsistent-null-check | 179 | FP | FP | 函数 `lookup_commit` 在内部已处理了 `obj` 为 NULL 的情况，会调用 `create_object` 返回一个有效的对象，因此其返回值 `c` 不会为 NULL，后续对 `c->object.parsed` ... |
| 445 | git-2.44.0 | clear_common_flag | cpp/inconsistent-null-check | 2124 | FP | FP | 在循环中，`oid` 来自 `oidset_iter_next`，该函数仅在集合中存在有效项时返回非空指针，且 `lookup_object` 在哈希表中查找对应项，若未找到则返回 NULL。然而，`oidset` 中的对象 ID 应... |
| 446 | git-2.44.0 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 141 | FP | FP | 告警点位于 `if (*type == OBJ_TAG)` 分支内，`parse_object` 的返回值被赋值给 `tag` 指针，随后代码立即检查 `if (!tag->tagged)`，这隐含了对 `tag` 是否为空的检查。因... |
| 447 | git-2.44.0 | find_merge_parents | cpp/inconsistent-null-check | 614 | FP | FP | 告警点 `obj = parse_object(...)` 的返回值在后续代码中通过 `add_merge_parent(result, &obj->oid, ...)` 被使用，这隐含了对 `obj` 非空的假设。然而，在调用 `a... |
| 448 | git-2.44.0 | get_rev | cpp/inconsistent-null-check | 187 | FP | FP | 在调用 `prio_queue_get` 后，代码立即通过 `entry->commit` 访问其成员，这隐含了对 `entry` 非空的假设。结合上下文，`prio_queue_get` 仅在队列为空时返回 NULL，而调用前已检查... |
| 449 | git-2.44.0 | get_parent | cpp/inconsistent-null-check | 1063 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将结果传递给 `repo_parse_commit` 进行校验，若解析失败则返回 `MISSING_OBJECT`。这表明代码逻辑已通过后续的 `repo_par... |
| 450 | git-2.44.0 | show_ambiguous_object | cpp/inconsistent-null-check | 422 | FP | FP | 代码在调用 `lookup_tag` 后立即将其传递给 `parse_tag` 进行解析，`parse_tag` 函数内部会检查 `tag` 是否为 `NULL` 并返回错误。因此，即使 `lookup_tag` 返回 `NULL`，... |
| 451 | git-2.44.0 | fill_bitmap_commit | cpp/inconsistent-null-check | 416 | FP | FP | 代码逻辑保证了 `prio_queue_get` 的返回值非空。函数在 `while (queue->nr)` 循环内调用 `prio_queue_get`，而 `prio_queue_get` 仅在 `queue->nr` 为 0 ... |
| 452 | git-2.44.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3256 | FP | FP | 函数 `lookup_decoration` 在内部已对空装饰表（`!n->size`）和未找到项（`!ref->base`）的情况返回 NULL，调用方 `leave_one_treesame_to_parent` 虽未显式检查返回... |
| 453 | git-2.44.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 686 | FP | FP | 函数 `lookup_commit` 在内部已处理空指针情况：若 `lookup_object` 返回空，它会调用 `create_object` 创建并返回一个新对象，因此调用方无需额外检查空值。 |
| 454 | git-2.44.0 | <global> | cpp/inconsistent-null-check | 27 | FP | FP | 函数 `test_parse_commit_in_graph` 是一个测试函数，其参数 `commit_oid` 由测试用例控制，非不可信的外部输入。`lookup_commit` 返回的 `c` 被直接用于访问 `c->date` ... |
| 455 | git-2.44.0 | test_ctype_isxdigit | cpp/overflow-buffer | 59 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 的循环中，循环变量 `i` 的范围是 0 到 255，而 `EOF` 是一个负值常量（通常为 -1）。代码明确检查 `func(EOF)` 并期望结果为假，这是对边界条... |
| 456 | git-2.44.0 | test_ctype_ispunct | cpp/overflow-buffer | 58 | FP | FP | 告警指出的数组负索引访问发生在宏 `TEST_CTYPE_FUNC` 的展开中，其中 `func(i)` 和 `func(EOF)` 被调用。`EOF` 通常定义为 -1，但 `func` 是传递给宏的字符分类函数（如 `ispunc... |
| 457 | git-2.44.0 | test_ctype_iscntrl | cpp/overflow-buffer | 57 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 的展开中，用于检查 `func(EOF)`，其中 `EOF` 通常定义为 -1。这是对字符分类函数的边界测试，是故意的、安全的测试逻辑，并非缓冲区溢出漏洞。 |
| 458 | git-2.44.0 | test_ctype_is_pathspec_magic | cpp/overflow-buffer | 53 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 的展开中，用于检查 `func(EOF)`，其中 `EOF` 通常定义为 -1。这是对函数 `func` 的合法参数测试，并非对数组的直接越界访问。代码逻辑正确，是测试... |
| 459 | git-2.44.0 | test_ctype_is_regex_special | cpp/overflow-buffer | 52 | FP | FP | 宏定义中的循环索引 `i` 范围是 0 到 255，且对 `EOF` 的调用是 `func(EOF)`，并非数组索引操作。告警所指的负索引 -1 可能源于对宏或 `EOF` 值的误解，切片代码中不存在实际的负索引数组访问。 |
| 460 | git-2.44.0 | test_ctype_is_glob_special | cpp/overflow-buffer | 51 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 的循环中，该循环明确限定 `i` 的范围为 0 到 255，且对 `EOF` 的调用是独立的检查，不会导致数组访问。切片代码的逻辑保证了不会发生负索引访问，因此是误报。 |
| 461 | git-2.44.0 | test_ctype_isalnum | cpp/overflow-buffer | 50 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 中，该宏在循环中调用 `func(i)`，其中 `i` 的范围是 0 到 255，而 `func(EOF)` 调用时 `EOF` 通常为 -1。被测试的 `isalnu... |
| 462 | git-2.44.0 | test_ctype_isalpha | cpp/overflow-buffer | 49 | FP | FP | 告警针对宏展开后的数组访问，但切片显示宏`TEST_CTYPE_FUNC`中的循环索引`i`范围明确为0到255，且`EOF`通常定义为-1，但`func(EOF)`是函数调用而非数组索引。切片内无实际数组定义，告警可能是工具对宏的误解析。 |
| 463 | git-2.44.0 | test_ctype_isspace | cpp/overflow-buffer | 48 | FP | FP | 宏定义显示循环索引 i 的范围是 0 到 255，且函数 func(i) 的参数 i 始终为非负，不会出现访问索引 -1 的情况。告警点 `func(EOF)` 中的 EOF 是宏，其值通常为 -1，但这是作为函数参数传递，并非数组索... |
| 464 | git-2.44.0 | test_ctype_isdigit | cpp/overflow-buffer | 47 | FP | FP | 宏展开后，循环变量 i 的范围是 0 到 255，且对 EOF 的调用是 `func(EOF)`，并非数组索引操作。告警所指的负索引 -1 可能源于工具对宏或函数 `func` 内部实现的误判，切片代码中未见实际的数组访问存在越界。 |
| 465 | git-2.44.0 | add_patterns | cpp/invalid-pointer-deref | 1117 | FP | FP | 代码在写入 `buf[size++] = '\n';` 之前，已通过 `buf = xmallocz(size);` 分配了 `size+1` 字节的内存（xmallocz 会分配 size+1 并清零），因此写入位置 `size`（... |
| 466 | git-2.44.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1647 | FP | FP | 代码中 `buffer = xmallocz_gently(size);` 分配了 `size+1` 字节的内存，随后 `stream.avail_out = size + 1;` 和循环条件确保了 `stream.avail_out... |
| 467 | git-2.44.0 | should_prune_worktree | cpp/invalid-pointer-deref | 791 | FP | FP | 代码在写入 `path[len] = '\0';` 之前，已经通过 `while` 循环确保了 `len` 被递减到非零且 `path[len - 1]` 不是换行符，因此 `len` 是有效的索引，不会导致越界写入。 |
| 468 | curl-8_13_0 | <global> | cpp/invalid-pointer-deref | 89 | FP | FP | 代码在写入 `newname[len]` 前已通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen = len + 13`，确保了 `len` 索引在分配的内存边界内，因此该写入操作是安全的，不会越界。 |
| 469 | curl-8_15_0 | <global> | cpp/invalid-pointer-deref | 85 | FP | FP | 代码中 `newname[len] = '.';` 的写入位置是 `newname` 数组的有效索引。`newname` 通过 `malloc(newlen)` 分配，其中 `newlen = len + 13`，因此 `newnam... |
| 471 | curl-8_9_1 | <global> | cpp/invalid-pointer-deref | 96 | FP | FP | 代码在写入 `newname[len]` 前已通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen = len + 13`，确保了 `len` 索引处的写入在分配的内存边界内，不会发生越界。 |
| 472 | curl-8_7_1 | Curl_splayremove | cpp/inconsistent-null-check | 270 | FP | FP | 在调用 `Curl_splay` 的代码路径中，`t->smaller` 已被显式检查为非空，因此 `Curl_splay` 函数内部不会返回空指针，无需额外的空值检查。 |
| 473 | curl-8_7_1 | <global> | cpp/invalid-pointer-deref | 96 | FP | FP | 代码在写入 `newname[len]` 前已通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen = len + 13`，确保了 `len` 索引处的写入在分配的内存边界内，因此该指针解引用是安全的。 |
| 474 | curl-8_11_1 | <global> | cpp/invalid-pointer-deref | 91 | FP | FP | 代码中 `newname[len] = '.';` 的写入操作是安全的，因为 `newname` 是通过 `malloc(newlen)` 分配的，其中 `newlen = len + 13`，确保了 `len` 索引处（即第 `le... |
| 475 | nginx-1.27.2 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 代码注释明确指出数组已预分配了4个空元素，且当前条件 `conf->server_names.nelts == 0` 确保数组未满，因此 `ngx_array_push` 调用不会失败，无需进行空指针检查。 |
| 476 | nginx-1.29.0 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3565 | FP | FP | 代码注释明确指出数组已预分配了4个空元素，因此当前状态下ngx_array_push调用不会失败，无需进行空指针检查。 |
| 477 | nginx-1.27.4 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3521 | FP | FP | 代码注释明确指出数组已预分配了4个空元素，因此`ngx_array_push`调用不会失败，无需进行空指针检查。切片内的逻辑支持这一判断，因此告警为误报。 |
| 478 | nginx-1.25.4 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 代码注释明确指出数组已预分配了4个空元素，因此当前状态下`ngx_array_push`调用不会失败，无需进行空指针检查。 |
| 479 | nginx-1.27.0 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 代码注释明确指出数组已预分配了4个空元素，且当前条件 `conf->server_names.nelts == 0` 确保数组未满，因此 `ngx_array_push` 调用不会失败，无需检查NULL。 |
| 480 | vim-9.1.0550 | <global> | cpp/redundant-null-check-simple | 3494 | FP | FP | 告警指出的空指针检查（`inc_opt != NULL`）并非冗余，因为`inc_opt`可能为NULL（当`*curbuf->b_p_inc == NUL`且`*p_inc == NUL`时），且后续的`strstr`调用仅在`in... |
| 481 | vim-9.1.0550 | <global> | cpp/redundant-null-check-simple | 3576 | FP | FP | 告警指出的空指针检查（`inc_opt != NULL`）并非冗余，因为`inc_opt`可能为`p_inc`（全局变量），其值在切片中未显示，无法保证非空。检查是必要的安全防护。 |
| 482 | vim-9.1.0550 | findmatchlimit | cpp/offset-use-before-range-check | 2522 | FP | FP | 告警点 'col' 在数组访问 `linep[pos.col - 2]` 前，已通过 `pos.col > 1` 条件确保了 `pos.col - 2 >= 0`，因此不会发生越界访问。 |
| 483 | vim-9.1.0550 | common_function | cpp/inconsistent-null-check | 4856 | FP | FP | 代码在调用 `vim_strsave(s)` 后，将返回值赋给变量 `name`，并在后续多个分支中直接使用 `vim_free(name)` 进行释放，这表明代码已处理了内存分配失败的情况（即 `name` 为 NULL）。告警规则... |
| 484 | vim-9.1.0550 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | FP | 函数 `vterm_screen_is_eol` 的循环条件 `pos.col < screen->cols` 确保了 `pos.col` 在有效列范围内，结合 `getcell` 函数内部对行列的边界检查，当 `pos.col` 在... |
| 485 | vim-9.1.0550 | get_isolated_shell_name | cpp/inconsistent-null-check | 2695 | FP | FP | 函数 `get_isolated_shell_name` 的返回值 `p` 在调用 `vim_strsave` 后直接返回给调用者，由调用者负责检查空指针。告警规则要求检查 `vim_strsave` 的返回值，但在此上下文中，空指针... |
| 486 | vim-9.1.0550 | get_isolated_shell_name | cpp/inconsistent-null-check | 2706 | FP | FP | 函数 `vim_strnsave` 的返回值 `p` 被直接返回给调用者，由调用者负责检查其是否为 NULL。告警规则要求函数内部检查，但此代码模式是合理的资源分配与责任传递，并非安全漏洞。 |
| 487 | vim-9.1.0550 | did_set_cryptmethod | cpp/inconsistent-null-check | 1766 | FP | FP | 函数 `vim_strsave` 的返回值被直接赋值给全局变量 `p_cm`，而 `p_cm` 是一个全局配置选项，其后续使用（如 `STRCMP(p_cm, ...)`）在切片中可见。这些使用均未对 `p_cm` 进行空指针解引用，... |
| 488 | vim-9.1.0550 | did_set_background | cpp/inconsistent-null-check | 1079 | FP | FP | 告警点 `p_bg = vim_strsave(...)` 的返回值被立即传递给 `check_string_option(&p_bg)` 函数，该函数内部会检查指针是否为 NULL 并将其替换为安全值 `empty_option`，... |
| 489 | vim-9.1.0550 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 代码在调用 `find_win_by_nr_or_id` 后，立即使用 `win_valid_any_tab` 检查了返回的窗口指针是否有效，若无效则回退到 `curwin`。这构成了对返回值的有效空值检查与防护，因此告警为误报。 |
| 490 | vim-9.1.0550 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 告警指出的`regnext`调用未检查null，但切片代码显示其返回值`next`在后续的`OP(next)`等操作中被直接使用，这表明`regnext`被设计为在特定条件下（如`scan == NULL`）返回NULL，而外层循环已... |
| 491 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 代码中 `regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `regcode`（即 `JUST_CALC_SIZE`），该返回值在调用点仅用于赋值和比较，不进行解引... |
| 492 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 代码中 `regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `ret`（即 `regcode`），不会分配内存或返回 NULL，因此调用处无需检查 NULL。告警点... |
| 493 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在切片代码的上下文中，`regnext` 的返回值 `br` 被用作循环迭代变量，其空值检查由循环条件 `br != lastnode` 间接保证，且 `regnext` 函数内部已处理空指针返回，因此此处的空值检查是冗余的，属于工具误报。 |
| 494 | vim-9.1.0550 | win_redr_custom | cpp/inconsistent-null-check | 1115 | FP | FP | 代码在调用vim_strsave后立即将返回值传递给vim_free进行释放，虽然未显式检查NULL，但vim_free内部已处理NULL指针（if (x != NULL)），因此不会导致空指针解引用。告警属于静态分析工具对未检查返回... |
| 495 | vim-9.1.0550 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 函数 `getroom` 在内存分配失败时会返回 NULL，但调用点 `get_wordnode` 在 `spin->si_first_free == NULL` 时才会调用 `getroom`，且后续的 `#ifdef SPELL_... |
| 496 | vim-9.1.0550 | do_tag | cpp/inconsistent-null-check | 639 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续代码中被立即传递给 `vim_free(tofree)`，而 `tofree` 被赋值为 `name`。这表明代码遵循了 Vim 的内存管理惯例，即 `vim_s... |
| 497 | vim-9.1.0550 | define_function | cpp/inconsistent-null-check | 5306 | FP | FP | 告警指出的 `vim_strchr` 调用结果未检查空指针，但切片代码显示该调用仅用于检查字符是否存在（作为条件判断的一部分），其返回值未被解引用，因此空指针不会导致安全问题。 |
| 499 | vim-9.1.0550 | exec_instructions | cpp/inconsistent-null-check | 3257 | FP | FP | alloc_clear 返回的指针被直接赋值给 tv->vval.v_object，后续代码立即访问该对象的成员（如 obj_class、obj_refcount），若 alloc_clear 返回 NULL 将导致空指针解引用。但切... |
| 500 | vim-9.1.0550 | barline_parse | cpp/inconsistent-null-check | 1122 | FP | FP | 代码中调用 `vim_strsave(s)` 的返回值直接赋值给 `value->bv_string`，但 `value->bv_allocated` 被设置为 `allocated ｜｜ converted`。当 `allocate... |
| 501 | vim-9.1.0550 | ex_history | cpp/unsafe-strcat | 780 | FP | FP | 代码在调用STRCAT前，已通过条件`vim_strsize(hist[i].hisstr) > (int)Columns - 10`确保目标缓冲区IObuff有足够空间，否则会调用trunc_string进行截断处理，因此不存在缓冲... |
| 502 | vim-9.1.0550 | helptags_one | cpp/unsafe-strcat | 971 | FP | FP | 代码中使用了宏`STRCAT`，其底层调用`strcat`，但告警点`NameBuff`缓冲区的大小未在切片中明确给出，无法直接评估是否存在缓冲区溢出风险。然而，结合告警规则`cpp/unsafe-strcat`的通用建议和Vim项目... |
| 503 | vim-9.1.0550 | netbeans_keyname | cpp/unsafe-strcat | 2444 | FP | FP | 函数内部逻辑严格限制了`name`的来源，它要么是指向短字符串字面量（如"F1"），要么是指向大小为2的局部数组`namebuf`（已确保以NUL结尾）。因此，拼接的目标字符串`buf`的内容和长度是完全可控的，不存在缓冲区溢出的风险。 |
| 504 | vim-9.1.0550 | set_init_default_backupskip | cpp/unsafe-strcat | 178 | FP | FP | 代码在调用STRCAT前，通过ga_grow(&ga, len)检查了目标缓冲区ga.ga_data是否有足够空间，且len已精确计算了源字符串长度加分隔符，确保了缓冲区大小充足，因此不存在缓冲区溢出风险。 |
| 505 | vim-9.1.0550 | do_put | cpp/unsafe-strcat | 2095 | FP | FP | 代码中使用了宏 `STRCAT(newp, ptr)`，但 `newp` 是通过 `alloc` 分配的内存，其大小已计算为 `ml_get_len(lnum) - col + totlen + 1`，其中 `totlen` 是 `y... |
| 506 | vim-9.1.0550 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限内容，并确保其以NUL结尾，且后续拼接的字符串p源自原始单词word，其长度wordlen已预先计算并受MAXWLEN限制... |
| 512 | vim-9.1.0550 | ga_concat_strings | cpp/unbounded-write | 788 | FP | FP | 代码中目标缓冲区 `p` 的大小已通过 `alloc(len + 1)` 精确分配，其长度 `len` 已累加了所有源字符串及分隔符的长度，因此 `STRCPY` 操作不会导致缓冲区溢出。 |
| 513 | vim-9.1.0550 | maketitle | cpp/unbounded-write | 4112 | FP | FP | STRCPY的目标缓冲区icon_str指向buf数组，其大小为IOSIZE，而源字符串p是经过截断处理的路径尾部，长度被限制在100字节以内，且后续trans_characters函数调用也确保了操作在IOSIZE范围内，因此不存在... |
| 514 | vim-9.1.0550 | buf_write | cpp/unbounded-write | 1208 | FP | FP | STRCPY宏用于将已知的固定字符串fname复制到固定大小的缓冲区IObuff中，且fname是函数参数，其长度受限于文件系统路径，而IObuff的大小在切片中未明确但通常足够大（如MAXPATHL）。此外，该复制操作发生在受控的备... |
| 515 | vim-9.1.0550 | buf_write | cpp/unbounded-write | 2566 | FP | FP | 切片代码中未发现对strcat的调用，告警消息提及的'call to strcat'在提供的代码片段中不存在。该告警可能是基于不完整的分析或误报。 |
| 516 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2138 | FP | FP | 代码中使用了宏STRCAT，其定义为strcat，但切片显示目标缓冲区'leader'是通过alloc动态分配的，其大小计算包含了源字符串长度、额外空间和填充，且分配前有明确的长度计算和边界检查，因此缓冲区大小足够，不会发生溢出。 |
| 517 | vim-9.1.0550 | transstr | cpp/unbounded-write | 366 | FP | FP | 函数`transstr`通过`alloc`为目标缓冲区`res`分配了精确计算的长度（`len + 1`或`vim_strsize(s) + 1`），并在循环前将其初始化为空字符串。后续的`STRCAT`（即`strcat`）操作是在... |
| 518 | vim-9.1.0550 | globpath | cpp/unbounded-write | 3783 | FP | FP | 在调用STRCAT拼接`file`到`buf`之前，代码已通过`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了缓冲区剩余空间，确保不会发生溢出。 |
| 519 | vim-9.1.0550 | win_redr_status_matches | cpp/unbounded-write | 634 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为buf分配了足够的内存（Columns * MB_MAXBYTES + 1 或 Columns + 1），且后续逻辑严格确保写入长度不超过Columns，因此不存在缓冲区溢... |
| 520 | vim-9.1.0550 | win_redr_status_matches | cpp/unbounded-write | 653 | FP | FP | STRCPY 的目标缓冲区 `buf + len` 和源字符串 `transchar_byte(*s)` 的长度均受控。`buf` 已分配足够大小（`Columns * MB_MAXBYTES + 1` 或 `Columns + 1`... |
| 522 | vim-9.1.0550 | has_profiling | cpp/unbounded-write | 973 | FP | FP | STRCPY的目标缓冲区pe->pen_name的大小是动态分配的，其大小为offsetof(profentry_T, pen_name) + STRLEN(fname) + 1，足以容纳源字符串fname，因此不会发生缓冲区溢出。 |
| 523 | vim-9.1.0550 | do_string_sub | cpp/unbounded-write | 7697 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过ga_grow函数确保目标缓冲区ga.ga_data有足够的剩余空间容纳源字符串tail，因此不会发生缓冲区溢出。 |
| 524 | vim-9.1.0550 | make_expanded_name | cpp/unbounded-write | 6918 | FP | FP | 代码在调用STRCPY前，已通过alloc分配了足够容纳in_start、temp_result和expr_end+1三部分字符串总长度加1的空间，目标缓冲区大小经过精确计算，不存在溢出风险。 |
| 525 | vim-9.1.0550 | make_expanded_name | cpp/unbounded-write | 6920 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够容纳所有字符串拼接结果的内存，缓冲区大小计算正确，不存在溢出风险。 |
| 526 | vim-9.1.0550 | set_var_const | cpp/unbounded-write | 4183 | FP | FP | STRCPY宏的目标缓冲区di->di_key的大小已通过alloc分配，大小为varname长度加1，确保了缓冲区足够容纳源字符串，因此不会发生缓冲区溢出。 |
| 528 | vim-9.1.0550 | ex_substitute | cpp/unbounded-write | 4862 | FP | FP | 切片代码中未发现对strcat函数的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中不存在。该告警可能是工具对宏STRCAT的误判，而STRCAT宏在切片中仅用于字符串拼接，且其目标缓冲区大小在上下文中通过动态分配（如... |
| 529 | vim-9.1.0550 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区buf分配了精确计算的长度len，该长度已包含源字符串cmd的长度和必要的额外字符及终止符，因此不会发生缓冲区溢出。 |
| 530 | vim-9.1.0550 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 代码在调用STRCAT前，已通过alloc(len)分配了缓冲区，且len的计算已考虑了所有待拼接字符串的长度和终止符，缓冲区大小足够，不存在溢出风险。 |
| 531 | vim-9.1.0550 | ex_sort | cpp/unbounded-write | 605 | FP | FP | 代码中 `STRCPY(sortbuf1, s)` 的目标缓冲区 `sortbuf1` 已通过 `alloc(maxlen + 1)` 分配，其大小 `maxlen + 1` 是根据待处理行的最大长度 `maxlen` 计算得出的，且... |
| 532 | vim-9.1.0550 | expand_sfile | cpp/unbounded-write | 9823 | FP | FP | 代码中目标缓冲区 `newres` 的大小为 `resultlen + 1`，而 `repl` 的长度 `repllen` 已通过 `STRLEN(repl)` 获取，且 `resultlen` 已更新为 `resultlen + r... |
| 533 | vim-9.1.0550 | repl_cmdline | cpp/unbounded-write | 5332 | FP | FP | 代码使用alloc(i)为目标缓冲区new_cmdline分配了精确计算的长度i，该长度已包含源字符串长度和必要的空字符，因此strcpy操作不会导致缓冲区溢出。 |
| 534 | vim-9.1.0550 | repl_cmdline | cpp/unbounded-write | 5338 | FP | FP | 代码中目标缓冲区 `new_cmdline` 的大小 `i` 已通过计算 `(src - *cmdlinep) + repllen + taillen + 3` 并加上 `eap->nextcmd` 的长度（若存在）来精确分配，且后续... |
| 537 | vim-9.1.0550 | do_one_cmd | cpp/unbounded-write | 2677 | FP | FP | 告警指向的STRCPY宏在切片中用于将错误消息复制到固定大小的IObuff缓冲区，但切片显示错误消息来源是静态字符串常量或已受长度检查的字符串，不存在缓冲区溢出风险。 |
| 538 | vim-9.1.0550 | discard_exception | cpp/unbounded-write | 642 | FP | FP | STRCPY(IObuff, saved_IObuff) 中的目标缓冲区 IObuff 是全局缓冲区，其大小在代码中定义为 IOSIZE（通常足够大），而源字符串 saved_IObuff 是之前通过 vim_strsave(IObu... |
| 539 | vim-9.1.0550 | get_exception_string | cpp/unbounded-write | 473 | FP | FP | 目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度已包含源字符串 `mesg` 或 `p` 的长度，因此 `STRCAT` 调用不会导致缓冲区溢出。 |
| 541 | vim-9.1.0550 | escape_fname | cpp/unbounded-write | 4072 | FP | FP | 目标缓冲区 `p` 的大小通过 `alloc(STRLEN(*pp) + 2)` 分配，其长度精确为源字符串长度加2，`STRCPY(p + 1, *pp)` 的写入长度与缓冲区大小匹配，不会发生溢出。 |
| 542 | vim-9.1.0550 | cmdline_browse_history | cpp/unbounded-write | 1484 | FP | FP | 在调用STRCPY（即strcpy）之前，代码通过alloc_cmdbuff为目标缓冲区ccline.cmdbuff分配了足够的内存，其大小基于源字符串p的长度（或经过计算的长度len），确保了目标缓冲区大小不小于源字符串长度，因此不... |
| 544 | vim-9.1.0550 | <global> | cpp/unbounded-write | 5375 | FP | FP | 代码中 `sprintf` 的目标缓冲区 `itmp` 大小为 `TEMPNAMELEN`，而源字符串 `vim_tempdir` 是之前通过 `expand_env` 扩展并添加了路径分隔符的目录路径，其长度已通过 `TEMPNAM... |
| 545 | vim-9.1.0550 | vim_settempdir | cpp/unbounded-write | 5235 | FP | FP | 代码中`tempdir`参数来源未知，但告警点`STRCPY(buf, tempdir)`仅在`vim_FullName`调用失败时执行，且目标缓冲区`buf`已通过`alloc(MAXPATHL + 2)`分配了固定大小`MAXPA... |
| 546 | vim-9.1.0550 | <global> | cpp/unbounded-write | 4352 | FP | FP | 代码在调用 sprintf 前，已通过 alloc(STRLEN(path) + STRLEN(mesg) + STRLEN(mesg2) + 2) 为目标缓冲区 tbuf 分配了足够的空间，该空间大小精确计算了所有源字符串的长度总和... |
| 547 | vim-9.1.0550 | vim_rename | cpp/unbounded-write | 3839 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。 |
| 548 | vim-9.1.0550 | buf_modname | cpp/unbounded-write | 3620 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区retval分配了足够空间（fnamelen + extlen + 3），且fnamelen和extlen均来自已知字符串的长度计算，不存在缓冲区溢出风险。 |
| 549 | vim-9.1.0550 | addfile | cpp/unbounded-write | 4196 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区p分配了大小为STRLEN(f) + 1 + isdir的内存，该大小精确匹配源字符串f的长度加1（以及可能的目录分隔符），因此不会发生缓冲区溢出。 |
| 550 | vim-9.1.0550 | unix_expandpath | cpp/unbounded-write | 3833 | FP | FP | STRCPY宏在切片中被定义为strcpy，但调用STRCPY(s, path_end + 1)时，目标缓冲区buf的大小为buflen（STRLEN(path) + MAXPATHL），源字符串path_end + 1是原始路径的一... |
| 551 | vim-9.1.0550 | concat_fnames | cpp/unbounded-write | 3123 | FP | FP | 代码通过alloc为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcpy操作不会发生缓冲区溢出。 |
| 552 | vim-9.1.0550 | concat_fnames | cpp/unbounded-write | 3126 | FP | FP | 函数通过alloc分配了足够大的缓冲区（大小为两个输入字符串长度之和加3），然后使用STRCPY和STRCAT进行安全的字符串拼接，不存在缓冲区溢出的风险。 |
| 553 | vim-9.1.0550 | uniquefy_paths | cpp/unbounded-write | 2362 | FP | FP | 代码中 `file_pattern` 缓冲区的大小为 `len + 2`，其中 `len` 是 `pattern` 的长度。`STRCAT` 操作是将 `pattern` 追加到 `file_pattern` 之后，而 `file_p... |
| 554 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1720 | FP | FP | 代码中 STRCPY 宏的目标缓冲区 NameBuff 大小为 MAXPATHL，而源字符串 *file_to_find 或 rel_fname 在复制前已通过 expand_env_esc 处理并受 MAXPATHL 限制，且拼接前... |
| 556 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1726 | FP | FP | STRCPY 宏的目标缓冲区 NameBuff 大小为 MAXPATHL，而源字符串 *file_to_find 在复制前已通过 expand_env_esc 函数展开并存入 NameBuff，其长度受 MAXPATHL 限制，因此不... |
| 557 | vim-9.1.0550 | ff_check_visited | cpp/unbounded-write | 1364 | FP | FP | 目标缓冲区 `vp->ffv_fname` 的大小是动态分配的，其大小为 `STRLEN(ff_expand_buffer) + 1`，与源字符串 `ff_expand_buffer` 的长度完全匹配，因此 `STRCPY`（即 `s... |
| 558 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 801 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过STRLEN检查确保源字符串长度加上分隔符后小于目标缓冲区大小MAXPATHL，因此不存在缓冲区溢出风险。 |
| 559 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 815 | FP | FP | 切片代码中，在调用STRCAT前，已通过条件`STRLEN(file_path) + STRLEN(stackp->ffs_fix_path) + 1 < MAXPATHL`检查了目标缓冲区`file_path`的剩余空间，确保不会发... |
| 560 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 936 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过STRLEN(file_path) + 1 + STRLEN(search_ctx->ffsc_file_to_search) < MAXPATHL进行了明确的长度检查，确保目标缓冲区... |
| 561 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 938 | FP | FP | 代码在调用STRCAT前，已通过条件`STRLEN(file_path) + STRLEN(search_ctx->ffsc_file_to_search) + 1 < MAXPATHL`检查了目标缓冲区`file_path`的剩余空... |
| 562 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 1104 | FP | FP | 代码在调用STRCPY（即strcpy）前，均通过STRLEN检查了源字符串和目标缓冲区的大小，确保不会超过MAXPATHL，因此不存在缓冲区溢出风险。 |
| 563 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 1106 | FP | FP | 代码在调用STRCAT前，已通过STRLEN(file_path) + STRLEN(search_ctx->ffsc_fix_path) < MAXPATHL的条件检查，确保目标缓冲区有足够空间，因此不会发生缓冲区溢出。 |
| 564 | vim-9.1.0550 | <global> | cpp/unbounded-write | 533 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区`ff_expand_buffer`在告警行之前已通过`alloc(MAXPATHL)`分配，其大小固定为MAXPATHL。告警行`STRCPY(ff_expand_buffer, search... |
| 565 | vim-9.1.0550 | <global> | cpp/unbounded-write | 541 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`buf`和`ff_expand_buffer`的大小均通过`alloc`函数分配，且分配时已明确计算了所需长度（`eb_len + STRLEN(search_ctx->ffsc_fix_pat... |
| 566 | vim-9.1.0550 | <global> | cpp/unbounded-write | 544 | FP | FP | 代码中 `ff_expand_buffer` 在函数开头已通过 `alloc(MAXPATHL)` 分配了固定大小的缓冲区（MAXPATHL），且告警处的 `STRCAT` 操作的目标和源字符串长度在之前的逻辑中已通过 `STRLEN... |
| 567 | vim-9.1.0550 | <global> | cpp/unbounded-write | 586 | FP | FP | 切片代码中，STRCPY宏被用于将已知长度的字符串复制到新分配的缓冲区中，目标缓冲区大小已通过alloc确保足够，不存在缓冲区溢出的风险。 |
| 568 | vim-9.1.0550 | <global> | cpp/unbounded-write | 587 | FP | FP | 告警点 `STRCAT(temp, search_ctx->ffsc_wc_path);` 中，目标缓冲区 `temp` 的大小已通过 `alloc` 精确分配，其大小为源字符串 `search_ctx->ffsc_fix_path ... |
| 569 | vim-9.1.0550 | <global> | cpp/unbounded-write | 3793 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够大小的缓冲区，其大小计算包含了源字符串s的长度，因此不会发生缓冲区溢出。 |
| 570 | vim-9.1.0550 | foldDelMarker | cpp/unbounded-write | 1892 | FP | FP | 代码中目标缓冲区 `newline` 的大小通过 `alloc(ml_get_len(lnum) - len + 1)` 精确分配，其长度等于原行长减去被删除标记的长度再加1（用于空字符）。随后使用 `STRCPY` 复制剩余部分，源... |
| 571 | vim-9.1.0550 | foldAddMarker | cpp/unbounded-write | 1810 | FP | FP | 代码中目标缓冲区 `newline` 的大小通过 `alloc(line_len + markerlen + STRLEN(cms) + 1)` 动态分配，其大小足以容纳源字符串 `line` 和 `cms` 的拼接，且分配大小包含了... |
| 572 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2899 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_prolog->title`和`res_prolog->version`的长度在`prt_open_resource`函数中通过`vim_strncpy`进行了限制，确保不会超过... |
| 573 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2901 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_prolog->title`和`res_prolog->version`来自受控的PostScript资源文件，其内容在`prt_open_resource`函数中经过解析和长度... |
| 574 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2905 | FP | FP | 告警点 `STRCPY(buffer, res_cidfont->title);` 中，目标缓冲区 `buffer` 大小为 256 字节，源字符串 `res_cidfont->title` 来自资源文件解析，其长度在 `prt_op... |
| 575 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 切片代码显示，`res_cidfont->title` 和 `res_cidfont->version` 来自外部资源文件，其内容在 `prt_open_resource` 函数中通过解析文件头获得，长度受 `resource->ti... |
| 576 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 告警点 `STRCPY(buffer, res_cmap->title);` 中，`res_cmap->title` 来源于外部资源文件，其内容在 `prt_open_resource` 函数中通过解析文件头获得，长度受 `vim_s... |
| 577 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 切片代码显示，`res_cmap->title` 和 `res_cmap->version` 是从受控的 PostScript 资源文件中解析出的固定字符串，其长度已在 `prt_open_resource` 函数中通过 `vim_s... |
| 578 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2920 | FP | FP | 告警点 `STRCPY(buffer, res_encoding->title);` 中，`res_encoding->title` 来源于受控的资源文件解析（`prt_open_resource` 函数），其长度已在解析时被 `vi... |
| 579 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2922 | FP | FP | 告警涉及的 `buffer` 数组大小为256字节，而 `res_encoding->title` 和 `res_encoding->version` 是从受控的PostScript资源文件中解析出的短字符串，其长度在 `prt_op... |
| 581 | vim-9.1.0550 | do_helptags | cpp/unbounded-write | 1206 | FP | FP | STRCPY 宏的目标缓冲区 NameBuff 在代码中被定义为全局数组，其大小（MAXPATHL）足以容纳典型的文件路径。告警点处的源字符串 `dirname` 是函数参数，其长度受限于文件系统路径的最大长度，且后续操作（如 add... |
| 582 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 971 | FP | FP | NameBuff 缓冲区大小定义为 MAXPATHL（通常为 260 或 4096），而拼接的路径由 dir 和 ext 等参数构成，这些参数来自受控的文档目录和文件扩展名，长度有限，不太可能超过 MAXPATHL。告警点位于构建文件... |
| 583 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 987 | FP | FP | 目标缓冲区 `NameBuff` 在代码中未明确其大小，但根据上下文（如 `MAXPATHL` 的使用）推断，它很可能是一个足够大的固定大小缓冲区（如 `MAXPATHL`）。告警点 `STRCAT(NameBuff, tagfnam... |
| 584 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 1108 | FP | FP | sprintf的目标缓冲区`s`是通过`alloc(p2 - p1 + STRLEN(fname) + 2)`分配的，其大小精确计算为标签字符串长度加文件名长度再加分隔符和终止符，因此不会发生缓冲区溢出。 |
| 585 | vim-9.1.0550 | highlight_set_startstop_termcode | cpp/unbounded-write | 1477 | FP | FP | 代码在调用STRCAT前已通过条件`(int)(STRLEN(buf) + STRLEN(p)) >= 99`检查，确保buf（大小为100）不会溢出，因此是安全的误报。 |
| 586 | vim-9.1.0550 | load_colors | cpp/unbounded-write | 602 | FP | FP | 缓冲区大小已通过 `alloc(STRLEN(name) + 12)` 精确分配，足以容纳格式字符串 `"colors/%s.vim"` 和参数 `name`，因此 `sprintf` 不会发生溢出。 |
| 588 | vim-9.1.0550 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...），并分配了对应大小的内存（buf = alloc(amt)），确保了写入不会越界。 |
| 589 | vim-9.1.0550 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...），并分配了对应大小的内存（buf = alloc(amt)），确保了写入不会溢出。 |
| 592 | vim-9.1.0550 | cs_add_common | cpp/unbounded-write | 604 | FP | FP | 代码在调用 sprintf 前，已通过 alloc 为目标缓冲区 fname2 分配了足够的空间，其大小为 strlen(CSCOPE_DBFILE) + strlen(fname) + 2，这确保了格式化后的字符串不会溢出。 |
| 593 | vim-9.1.0550 | ins_compl_infercase_gettext | cpp/unbounded-write | 658 | FP | FP | 代码中STRCPY的目标缓冲区`gap.ga_data`已通过`ga_grow(&gap, IOSIZE)`分配了至少IOSIZE大小的内存，且源字符串`IObuff`是一个固定大小的数组（IOSIZE），其内容已通过`*p = NU... |
| 594 | vim-9.1.0550 | <global> | cpp/unbounded-write | 3097 | FP | FP | 切片代码显示，在告警的 sprintf 调用附近，存在一个使用 vim_snprintf 的安全函数调用，该函数明确接收了目标缓冲区大小参数（args->os_errbuflen），这表明代码中已存在对缓冲区溢出的防护机制，且该告警点... |
| 595 | vim-9.1.0550 | findswapname | cpp/unbounded-write | 4967 | FP | FP | STRCPY的目标缓冲区fname2是通过alloc(n + 2)分配的，其大小比源字符串fname（长度为n）多2个字节，足以容纳源字符串和可能的修改，不存在缓冲区溢出风险。 |
| 596 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2157 | FP | FP | 目标缓冲区 `s` 的大小通过 `alloc(STRLEN(f) + 1)` 精确分配，其长度等于源字符串 `f` 的长度加1，因此 `STRCPY(s, f)` 不会发生缓冲区溢出。 |
| 597 | vim-9.1.0550 | <global> | cpp/unbounded-write | 811 | FP | FP | 代码中STRCPY宏的目标缓冲区大小通过`alloc(STRLEN(call_data) + 5)`动态分配，长度已包含源字符串长度加额外字符，不存在缓冲区溢出风险。 |
| 598 | vim-9.1.0550 | <global> | cpp/unbounded-write | 815 | FP | FP | 代码中使用了宏 `STRCPY`，其定义为 `strcpy`，但目标缓冲区 `menu->strings[i] + 2` 是通过 `alloc(STRLEN(call_data) + 5)` 分配的，大小足够容纳源字符串 `call_... |
| 599 | vim-9.1.0550 | msg_show_console_dialog | cpp/unbounded-write | 4387 | FP | FP | 告警点 `STRCPY(confirm_msg + 1, message)` 的目标缓冲区 `confirm_msg` 已通过 `alloc(len)` 分配，其大小 `len` 已计算包含源字符串 `message` 的长度（`ST... |
| 600 | vim-9.1.0550 | str2specialbuf | cpp/unbounded-write | 1919 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度小于传入的参数`len`，... |
| 601 | vim-9.1.0550 | get_emsg_source | cpp/unbounded-write | 484 | FP | FP | 代码通过 `alloc(STRLEN(sname) + STRLEN(p))` 为目标缓冲区分配了足够的空间，其大小等于两个字符串长度之和，因此 `sprintf` 不会发生溢出。 |
| 602 | vim-9.1.0550 | may_trigger_modechanged | cpp/unbounded-write | 2821 | FP | FP | STRCPY 的目标缓冲区 `last_mode` 和源缓冲区 `curr_mode` 均为固定大小的字符数组 `char_u curr_mode[MODE_MAX_LENGTH]`，且 `get_mode` 函数内部逻辑确保写入不会... |
| 603 | vim-9.1.0550 | expand_env_esc | cpp/unbounded-write | 1632 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过条件`STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen`检查了目标缓冲区`dst`的剩余空间`dstlen`，确保复制不会发生溢出。 |
| 604 | vim-9.1.0550 | call_shell | cpp/unbounded-write | 1877 | FP | FP | 目标缓冲区 ncmd 的大小通过 alloc(STRLEN(ecmd) + STRLEN(p_sxq) * 2 + 1) 精确分配，足以容纳源字符串 ecmd 和 p_sxq 的两次拼接，因此 strcat 操作不会导致缓冲区溢出。 |
| 605 | vim-9.1.0550 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 切片代码中未发现对strcat的调用，告警消息中提到的所有strcat调用均未在提供的代码片段中出现。因此，该告警在给定上下文中不成立，属于误报。 |
| 606 | vim-9.1.0550 | nb_reply_text | cpp/unbounded-write | 802 | FP | FP | 代码通过 alloc(STRLEN(result) + 32) 为目标缓冲区分配了足够的空间，其中 STRLEN(result) 计算了源字符串长度，加上固定开销 32 字节，确保了 sprintf 写入不会溢出。 |
| 607 | vim-9.1.0550 | push_showcmd | cpp/unbounded-write | 1805 | FP | FP | 告警针对的是宏STRCPY（即strcpy）的使用，但切片显示其目标缓冲区`old_showcmd_buf`和源缓冲区`showcmd_buf`均为全局数组，其大小在代码其他位置定义且相等，不存在缓冲区溢出的风险。该调用仅在条件`p_... |
| 608 | vim-9.1.0550 | add_to_showcmd | cpp/unbounded-write | 1760 | FP | FP | 代码在调用STRCAT前，通过计算`old_len`和`extra_len`，并检查`overflow`，当溢出发生时，会使用`mch_memmove`移动缓冲区内容以腾出空间，从而确保了目标缓冲区`showcmd_buf`不会发生溢出。 |
| 609 | vim-9.1.0550 | op_change | cpp/unbounded-write | 1866 | FP | FP | 切片代码中，STRCPY宏被用于拼接字符串，但目标缓冲区newp的大小已通过alloc(ml_get_len(linenr) + vpos.coladd + ins_len + 1)分配，其中+1确保了NUL终止符的空间，且目标缓冲区... |
| 610 | vim-9.1.0550 | op_replace | cpp/unbounded-write | 1162 | FP | FP | STRCPY宏的目标缓冲区newp是通过alloc(oldlen + 1 + n)分配的，其大小明确为oldlen + 1 + n，而源字符串oldp + bd.textcol + bd.textlen的长度小于oldlen - bd... |
| 611 | vim-9.1.0550 | op_replace | cpp/unbounded-write | 1171 | FP | FP | 代码中STRCPY的目标缓冲区`after_p`是通过`alloc(oldlen + 1 + n - newlen)`分配的，其大小`oldlen + 1 + n - newlen`精确等于源字符串`oldp + bd.textcol... |
| 612 | vim-9.1.0550 | op_delete | cpp/unbounded-write | 825 | FP | FP | STRCPY宏的目标缓冲区newp是通过alloc(ml_get_len(lnum) + 1 - n)分配的，其大小精确计算为原行长减去删除字符数再加1，确保了缓冲区足够容纳源字符串oldp + bd.textcol + bd.tex... |
| 613 | vim-9.1.0550 | block_insert | cpp/unbounded-write | 607 | FP | FP | STRCPY 的目标缓冲区 `newp` 是通过 `alloc` 分配的，其大小为 `ml_get_len(lnum) + spaces + slen + ...`，而源字符串 `oldp` 是来自 `ml_get` 的同一行内容，其... |
| 614 | vim-9.1.0550 | option_value2string | cpp/unbounded-write | 8155 | FP | FP | 切片代码显示，告警涉及的STRCPY宏（即strcpy）的目标缓冲区是NameBuff，但切片中未提供其大小定义，无法判断目标缓冲区大小是否足以容纳源字符串，因此无法评估是否存在缓冲区溢出风险。 |
| 615 | vim-9.1.0550 | option_value2string | cpp/unbounded-write | 8157 | FP | FP | 切片代码显示，告警点 STRCPY 的目标缓冲区 NameBuff 在多个分支中均受到明确的大小限制（如 MAXPATHL 或 MAX_KEY_NAME_LEN），且调用前有长度检查或使用安全函数（如 vim_strncpy），因此不... |
| 616 | vim-9.1.0550 | stropt_expand_envvar | cpp/unbounded-write | 1757 | FP | FP | 目标缓冲区 `newval` 的大小 `newlen` 已通过 `STRLEN(s) + 1` 精确计算并分配，`STRCPY` 复制的源字符串 `s` 长度不会超过分配的大小，因此不存在缓冲区溢出风险。 |
| 618 | vim-9.1.0550 | mch_expand_wildcards | cpp/unbounded-write | 6931 | FP | FP | 代码在调用STRCAT前，已通过alloc(len)为目标缓冲区command分配了精确计算的长度len，该长度已考虑了所有待拼接字符串（包括环境变量、函数名、选项和模式参数）的总和，并预留了必要的分隔符和转义字符空间，因此不存在缓冲... |
| 619 | vim-9.1.0550 | mch_expand_wildcards | cpp/unbounded-write | 7277 | FP | FP | 代码中 STRCPY 的目标缓冲区 `p` 是通过 `alloc(STRLEN((*file)[i]) + 1 + dir)` 分配的，其大小精确计算为源字符串长度加分隔符和终止符，因此不会发生缓冲区溢出。 |
| 620 | vim-9.1.0550 | mch_FullName | cpp/unbounded-write | 2816 | FP | FP | 在调用STRCAT（即strcat）之前，代码已通过条件`(int)(STRLEN(buf) + STRLEN(fname)) >= len`检查了目标缓冲区`buf`的剩余空间是否足以容纳源字符串`fname`，从而防止了缓冲区溢出。 |
| 621 | vim-9.1.0550 | qf_store_title | cpp/unbounded-write | 1932 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc_id为目标缓冲区分配了大小为STRLEN(title) + 2的内存，这确保了缓冲区足以容纳源字符串及额外字符，因此不存在缓冲区溢出风险。 |
| 624 | vim-9.1.0550 | regtilde | cpp/unbounded-write | 1925 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`tmpsublen > MAXCOL`对目标缓冲区大小`tmpsublen`进行了检查，并分配了`tmpsublen + 1`字节的内存，确保了目标缓冲区大小足以容纳... |
| 625 | vim-9.1.0550 | match_with_backref | cpp/unbounded-write | 1600 | FP | FP | 代码在调用STRCPY（即strcpy）前，通过动态内存分配确保了目标缓冲区reg_tofree的大小至少等于源字符串rex.line的长度（len = STRLEN(rex.line)）加上50字节的额外空间，因此不会发生缓冲区溢出。 |
| 626 | vim-9.1.0550 | get_reg_contents | cpp/unbounded-write | 2668 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过循环计算了目标缓冲区retval的总长度（len），并分配了len+1字节的内存，确保缓冲区大小足以容纳所有源字符串及其分隔符，因此不存在缓冲区溢出的风险。 |
| 627 | vim-9.1.0550 | do_put | cpp/unbounded-write | 2094 | FP | FP | 切片代码中未发现对strcpy的直接调用，告警消息中提到的多个strcpy调用源（如环境变量、文件读取）在提供的代码片段中均未出现。该告警可能指向其他未包含在切片中的代码位置，或是对宏（如STRCPY）的误报，但基于当前切片无法确认存... |
| 628 | vim-9.1.0550 | do_put | cpp/unbounded-write | 2095 | FP | FP | 切片代码中未发现任何对strcat函数的调用，告警消息中提到的所有strcat调用在提供的代码片段中均不存在。该告警可能是基于不完整的分析或对宏展开的误判。 |
| 629 | vim-9.1.0550 | op_yank | cpp/unbounded-write | 1278 | FP | FP | 代码中STRCPY宏的目标缓冲区pnew已通过alloc分配了足够大小（两个源字符串长度之和加1），且分配大小计算正确，不存在缓冲区溢出风险。 |
| 630 | vim-9.1.0550 | op_yank | cpp/unbounded-write | 1279 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够容纳两个字符串拼接结果的内存（长度计算为STRLEN(curr->y_array[curr->y_size - 1]) + STRLEN(y_current->y_array[0])... |
| 631 | vim-9.1.0550 | stuff_yank | cpp/unbounded-write | 452 | FP | FP | 代码在调用STRCPY前，已通过alloc为目标缓冲区lp分配了足够的内存，其大小为源字符串(*pp)长度、待拼接字符串(p)长度及终止符之和，确保了缓冲区大小足以容纳源字符串，因此不存在缓冲区溢出风险。 |
| 635 | vim-9.1.0550 | dump_word | cpp/unbounded-write | 4187 | FP | FP | STRCPY的目标缓冲区badword大小为MAXWLEN+10，源字符串p来自cword或word，而cword由make_case_word处理，其目标缓冲区也为MAXWLEN，因此源字符串长度不会超过MAXWLEN，复制到bad... |
| 636 | vim-9.1.0550 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 告警点位于 `make_case_word` 函数，该函数仅在拼写检查时处理内部单词，其输入 `fword` 来自内部缓冲区（如 `goodword`），并非直接来自外部不可信源。函数逻辑表明 `fword` 长度受 `MAXWLEN... |
| 637 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2998 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区p分配了足够空间（ml_get_curline_len() + addlen + 1），且复制的源字符串repl_to的长度repl_to_len已知，复制操作不会导致缓冲区溢出。 |
| 638 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2999 | FP | FP | 目标缓冲区 `p` 的大小已通过 `alloc(ml_get_curline_len() + addlen + 1)` 精确计算，其中 `addlen` 为 `repl_to_len - repl_from_len`，且 `STRCA... |
| 639 | vim-9.1.0550 | count_common_word | cpp/unbounded-write | 1919 | FP | FP | STRCPY的目标缓冲区wc->wc_word的大小为STRLEN(p) + 1，由alloc函数动态分配，其大小精确匹配源字符串p的长度，因此不会发生缓冲区溢出。 |
| 641 | vim-9.1.0550 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(buflen)为目标缓冲区buf分配了足够的内存，其中buflen = len + MAXWLEN + 2，而源字符串line的长度为len，因此拷贝不会导致缓冲区溢出。 |
| 642 | vim-9.1.0550 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数 getroom 已根据源字符串长度 s 分配了 STRLEN(s) + 1 字节的内存，STRCPY 的目标缓冲区 sc 大小与源字符串长度精确匹配，不会发生缓冲区溢出。 |
| 643 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 代码中STRCAT的目标缓冲区p是通过getroom()分配的，其大小已根据items[0]和items[1]的长度计算并预留了额外空间，不存在缓冲区溢出风险。 |
| 644 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 代码中已通过getroom函数为p分配了足够的内存，其大小为spin->si_info的现有长度加上items[0]和items[1]的长度再加3，然后使用STRCAT进行拼接，目标缓冲区大小是经过计算的，不存在溢出风险。 |
| 645 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2464 | FP | FP | STRCPY 的目标缓冲区 p 是通过 getroom(spin, STRLEN(items[1]) + 2, FALSE) 分配的，其大小明确为源字符串长度加 2，足以容纳源字符串和追加的 '+' 字符，因此不会发生缓冲区溢出。 |
| 646 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 代码中目标缓冲区 `p` 的大小是动态计算的（`l = (int)STRLEN(items[1]) + 1;` 加上可能的 `compflags` 长度），并通过 `getroom(spin, l, FALSE)` 分配了足够的内存，... |
| 647 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 代码中使用了安全的字符串复制宏STRCPY，但告警指向的调用是STRCPY(p, spin->si_info)，其中p是通过getroom分配的内存，其大小已通过计算确保足以容纳源字符串spin->si_info和连接的其他字符串，因... |
| 648 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2746 | FP | FP | 代码中使用了安全的 `vim_snprintf` 函数，告警指向的 `sprintf` 调用其目标缓冲区 `buf` 大小为 `MAXLINELEN`，且格式化字符串为静态字符串 `"^%s"` 或 `"%s$"`，其中 `items... |
| 649 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2748 | FP | FP | sprintf 的目标缓冲区 buf 大小为 MAXLINELEN（定义为 1024），而源字符串 items[4] 来自受控的 .aff 文件行解析，其长度受 MAXLINELEN 限制且通常较短，因此缓冲区溢出风险极低。 |
| 650 | vim-9.1.0550 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | 代码中 `STRCPY(sft->sft_word, goodword)` 的目标缓冲区 `sft->sft_word` 是通过 `alloc(offsetof(sftword_T, sft_word) + STRLEN(goodwo... |
| 651 | vim-9.1.0550 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY宏的目标缓冲区fword大小为MAXWLEN，源数据su->su_fbadword是拼写建议模块的内部数据结构，其长度受相同MAXWLEN常量限制，且后续代码有明确的长度检查和截断，因此不会发生缓冲区溢出。 |
| 652 | vim-9.1.0550 | concat_str | cpp/unbounded-write | 768 | FP | FP | 函数内已通过alloc为目标缓冲区分配了精确大小（str1与str2长度之和加1），且STRCPY宏展开为strcpy，其源字符串长度已通过STRLEN计算并包含在分配大小内，因此不会发生缓冲区溢出。 |
| 653 | vim-9.1.0550 | concat_str | cpp/unbounded-write | 770 | FP | FP | 函数通过`alloc`为目标缓冲区分配了精确的、足以容纳源字符串`str1`和`str2`拼接后内容的空间（包括终止符），然后使用`STRCPY`（即`strcpy`）进行复制。由于目标缓冲区大小是计算得出的，且源字符串长度已知，因此... |
| 654 | vim-9.1.0550 | expand_tag_fname | cpp/unbounded-write | 4121 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区retval分配了MAXPATHL大小的内存，且后续的vim_strncpy调用明确限制了拷贝长度，确保不会超出缓冲区边界。因此，该strcpy使用是安全的，属于工具误报。 |
| 655 | vim-9.1.0550 | findtags_add_match | cpp/unbounded-write | 2624 | FP | FP | 代码中 STRCPY 的目标缓冲区 `p` 和 `p + len + 1` 是通过 `alloc` 分配的，其大小已根据源字符串长度（`st->help_lang`）和固定偏移量精确计算（`len + 10 + ML_EXTRA + ... |
| 657 | vim-9.1.0550 | show_one_termcode | cpp/unbounded-write | 7058 | FP | FP | STRCPY的目标缓冲区IObuff+5有足够的空间，因为IObuff是一个全局大数组，且源字符串p来自get_special_key_name，该函数内部使用STRCPY时已通过长度检查确保不会超过MAX_KEY_NAME_LEN，... |
| 658 | vim-9.1.0550 | current_tagblock | cpp/unbounded-write | 1386 | FP | FP | 代码使用`sprintf`格式化字符串时，通过`len`参数限制了写入的字符数量（`%.*s`），且目标缓冲区`spat`和`epat`的大小（`len + 39`和`len + 9`）已根据该长度分配，确保了不会发生缓冲区溢出。 |
| 659 | vim-9.1.0550 | uc_check_code | cpp/unbounded-write | 1691 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，函数已通过STRLEN计算了源字符串长度，且目标缓冲区buf的大小在调用链上层应已根据该长度进行了分配（例如通过result变量），因此不存在无界写入风险。告警为误报。 |
| 661 | vim-9.1.0550 | trans_function_name_ext | cpp/unbounded-write | 4521 | FP | FP | 代码中使用了宏STRCPY，其定义为strcpy，但目标缓冲区`name`的大小已通过`alloc(len + lead + extra + 1)`精确分配，长度计算包含了源字符串长度`len`和必要的额外字符，因此不会发生缓冲区溢出。 |
| 662 | vim-9.1.0550 | fname_trans_sid | cpp/unbounded-write | 2115 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过条件`i + STRLEN(name + llen) < FLEN_FIXED`确保目标缓冲区`fname_buf`有足够空间，防止了缓冲区溢出。 |
| 663 | vim-9.1.0550 | fname_trans_sid | cpp/unbounded-write | 2127 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过条件`i + STRLEN(name + llen) < FLEN_FIXED`或`alloc`分配了足够大小的缓冲区，确保了目标缓冲区大小足以容纳源字符串，因此不存在缓冲区溢出风险。 |
| 665 | vim-9.1.0550 | exec_instructions | cpp/unbounded-write | 3487 | FP | FP | 切片代码中未发现任何对strcpy的调用，告警消息中提到的所有strcpy调用在提供的代码片段中均不存在。该告警可能是工具误报或指向了不相关的代码位置。 |
| 667 | vim-9.1.0550 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | FP | STRCPY的目标缓冲区newsav->sav_key的大小是通过offsetof(sallvar_T, sav_key) + STRLEN(name) + 1精确分配的，其长度足以容纳源字符串name及其终止空字符，因此不会发生缓冲... |
| 668 | vim-9.1.0550 | find_exported | cpp/unbounded-write | 756 | FP | FP | 代码在调用sprintf前已通过动态分配（alloc(len)）或使用固定大小缓冲区（buffer[200]）确保目标缓冲区大小足够，且len的计算已考虑所有拼接字符串的长度，不存在缓冲区溢出风险。 |
| 669 | vim-9.1.0550 | find_exported | cpp/unbounded-write | 763 | FP | FP | sprintf 的目标缓冲区 funcname 的大小已通过 len 计算确保足够，len 的计算考虑了所有拼接部分的最大长度，并据此分配了足够的内存，因此不会发生缓冲区溢出。 |
| 671 | vim-9.1.0550 | ExpandBufnames | cpp/invalid-pointer-deref | 2904 | FP | FP | 告警点 `(*file)[count++] = p;` 的写入操作受 `if (*file == NULL)` 检查保护，当 `*file` 为 NULL 时函数会提前返回 FAIL，不会执行写入。切片中 `*file` 在循环前初始... |
| 672 | vim-9.1.0550 | update_snapshot | cpp/invalid-pointer-deref | 2068 | FP | FP | 切片代码显示，在写入 `p[pos.col + 1]` 之前，已通过条件 `width == 2` 进行了检查，并且 `len` 是列数，`pos.col` 的循环条件为 `pos.col < len`，因此 `pos.col + 1... |
| 695 | vim-9.1.1591 | netbeans_keyname | cpp/unsafe-strcat | 2449 | FP | FP | 代码中`name`变量来源明确且长度有限（最大为3个字符的字符串字面量或2字节的数组），目标缓冲区`buf`虽未在切片中显示大小，但根据函数上下文推断其用于存储按键名称，应有足够空间。`strcat`的使用在可控范围内，未发现明显的缓... |
| 765 | vim-9.1.1591 | cs_make_vim_style_matches | cpp/unbounded-write | 1639 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...）并分配了相应内存（buf = alloc(amt)），确保了目标缓冲区大小足够，不会发生溢出。 |
| 766 | vim-9.1.1591 | cs_make_vim_style_matches | cpp/unbounded-write | 1647 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了该大小的内存，确保了写入不会越界。 |
| 781 | vim-9.1.1591 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 告警指出的strcat调用位于代码切片中，但该调用是使用宏STRCAT实现的，而STRCAT宏在切片中被定义为标准库的strcat。然而，在调用STRCAT之前，代码已经通过alloc分配了足够大的缓冲区（ml_get_len(lnu... |
| 846 | vim-9.1.1040 | <global> | cpp/redundant-null-check-simple | 3502 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 在解引用前已通过 `inc_opt = (*curbuf->b_p_inc == NUL) ? p_inc : curbuf->b_p_in... |
| 847 | vim-9.1.1040 | <global> | cpp/redundant-null-check-simple | 3584 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，指针 `inc_opt` 在解引用前已通过条件 `if (*inc_opt != NUL)` 进行了有效性检查，该检查确保了指针非空，因此后续的 `strstr... |
| 848 | vim-9.1.1040 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | FP | FP | 切片代码显示，在告警点 `linep[pos.col - 1] == '/' && linep[pos.col] == '*'` 之前，存在条件 `(int)pos.col < comment_col` 对 `pos.col` 进行了... |
| 849 | vim-9.1.1040 | common_function | cpp/inconsistent-null-check | 5061 | FP | FP | 代码在调用 vim_strsave 后，对返回的指针 name 进行了后续使用（如传递给 func_ref 或作为返回值），且存在多处对 name 的 vim_free 调用，表明代码已处理了内存分配失败的情况，并非完全忽略空指针检查。 |
| 851 | vim-9.1.1040 | get_isolated_shell_name | cpp/inconsistent-null-check | 2710 | FP | FP | 函数 `gettail` 已对空指针输入进行了检查，返回空字符串而非NULL，因此 `vim_strsave` 的输入是安全的，不会返回NULL。告警点未检查返回值是合理的，因为在此上下文中不会发生分配失败。 |
| 852 | vim-9.1.1040 | get_isolated_shell_name | cpp/inconsistent-null-check | 2721 | FP | FP | 函数 `vim_strnsave` 的返回值被赋值给变量 `p`，而 `p` 在函数末尾被直接返回。调用方（切片中未显示）负责检查返回值是否为 NULL，这是 Vim 代码库中内存分配函数的常见模式。告警点本身没有进行空值检查是符合上... |
| 853 | vim-9.1.1040 | did_set_cryptmethod | cpp/inconsistent-null-check | 1832 | FP | FP | 函数 `vim_strsave` 的返回值被赋值给全局变量 `p_cm`，该变量在后续代码中仅用于字符串比较（`STRCMP`）和作为参数传递给 `ml_set_crypt_key`，这些操作在遇到 NULL 指针时不会导致崩溃或安全... |
| 854 | vim-9.1.1040 | did_set_background | cpp/inconsistent-null-check | 1083 | FP | FP | 告警点 `p_bg = vim_strsave(...)` 的返回值被立即传递给 `check_string_option(&p_bg)`，该函数会检查指针是否为 NULL 并将其设置为 `empty_option`，因此即使 `vi... |
| 855 | vim-9.1.1040 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 在调用 `find_win_by_nr_or_id` 后，代码立即使用 `win_valid_any_tab` 检查返回的窗口指针是否有效，若无效则回退到 `curwin`。这提供了空指针防护，因此告警为误报。 |
| 856 | vim-9.1.1040 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 告警指出的 `regnext` 调用未检查 null，但切片代码显示 `scan` 变量在调用前已通过 `if (got_int ｜｜ scan == NULL)` 检查，且 `regnext` 函数内部有 null 处理逻辑，因此该... |
| 857 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 代码中 `regnode` 的返回值 `br` 被立即用于条件判断 `if (ret == NULL)` 和后续的 `regtail` 调用，其空值检查已通过 `ret` 和 `lastnode` 的判空逻辑间接完成。告警点位于循环内... |
| 858 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 代码中 `regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `JUST_CALC_SIZE`，该返回值在调用点 `br = regnode(NOTHING)` 后仅... |
| 859 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在调用 `regnext(br)` 的上下文中，`br` 变量来自 `ret` 或 `OPERAND(br)`，这些值均由 `regnode` 函数生成，该函数在非 `JUST_CALC_SIZE` 模式下返回非空指针。切片中未显示 ... |
| 860 | vim-9.1.1040 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 函数 `getroom` 在内存分配失败时会返回 NULL，但调用点 `get_wordnode` 在 `spin->si_first_free == NULL` 的分支中，将返回值赋值给 `n` 后，后续的 `#ifdef SPEL... |
| 861 | vim-9.1.1040 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续代码中被立即赋值给 `tofree`，随后 `name` 被重新赋值为 `tag`，原分配的内存指针已通过 `tofree` 保存，并将在函数末尾通过 `vim_... |
| 862 | vim-9.1.1040 | define_function | cpp/inconsistent-null-check | 5403 | FP | FP | 告警指出的 `vim_strchr` 调用结果未检查 NULL，但切片代码显示该调用仅用于检查字符 '(' 是否存在，其返回值直接用于布尔判断，不涉及解引用，因此不存在空指针解引用风险。 |
| 864 | vim-9.1.1040 | exec_instructions | cpp/inconsistent-null-check | 3383 | FP | FP | alloc_clear() 返回的指针被直接赋值给 tv->vval.v_object，后续代码立即访问该对象的成员（如 obj_class、obj_refcount），若 alloc_clear() 返回 NULL 将导致空指针解引... |
| 865 | vim-9.1.1040 | barline_parse | cpp/inconsistent-null-check | 1153 | FP | FP | 代码在调用 vim_strnsave 后，将返回值直接赋值给局部变量 s，而 s 随后被赋值给 value->bv_string。切片显示 value->bv_allocated 被设置为 allocated ｜｜ converted... |
| 866 | vim-9.1.1040 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | 代码中使用了STRCAT宏，但NameBuff是一个固定大小的全局缓冲区（MAXPATHL），且告警点之前的代码已通过STRCPY和STRCAT构建路径，其长度由已知的dir和ext参数控制，未发现明显的缓冲区溢出风险。 |
| 867 | vim-9.1.1040 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 代码中`name`变量来源明确且长度有限（最大为3个字符的字符串字面量或单个字符的数组），目标缓冲区`buf`在切片中虽未显示大小，但根据函数上下文推断其用于存储按键名称，其大小足以容纳拼接后的字符串（如'C-S-F1'），不存在缓冲... |
| 868 | vim-9.1.1040 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为安全内容，并确保其长度不超过MAXWLEN-1。随后拼接的字符串p是原始单词word经过安全截断（chop）后的部分，其长度受... |
| 873 | vim-9.1.1040 | ga_concat_strings | cpp/unbounded-write | 788 | FP | FP | 代码中目标缓冲区 `p` 的大小已通过精确计算分配（`alloc(len + 1)`），且循环中每次复制后都正确更新了指针 `p`，确保了不会发生缓冲区溢出。 |
| 874 | vim-9.1.1040 | maketitle | cpp/unbounded-write | 4147 | FP | FP | STRCPY的目标缓冲区icon_str指向buf，其大小为IOSIZE，而源字符串p是从文件名尾部截取的长度不超过100的字符串，且经过trans_characters处理，长度不会超过IOSIZE，因此不会发生缓冲区溢出。 |
| 875 | vim-9.1.1040 | buf_write | cpp/unbounded-write | 1208 | FP | FP | 代码中STRCPY(IObuff, fname)的源缓冲区fname是函数参数，其长度受调用者控制，但目标缓冲区IObuff是全局数组，其大小在切片中未定义。然而，在典型的Vim代码库中，IObuff通常被定义为足够大的固定大小数组（... |
| 876 | vim-9.1.1040 | buf_write | cpp/unbounded-write | 2566 | FP | FP | 告警指出的strcat调用位于错误消息构建路径中，其目标缓冲区IObuff的大小为IOSIZE（定义为1024），而拼接的字符串长度在切片中可见是受控的（错误消息常量），且拼接前有长度检查（STRLEN(IObuff) + STRLE... |
| 877 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2138 | FP | FP | 切片代码中未发现对 `STRCAT` 宏（即 `strcat`）的调用，告警信息中提到的多个 `strcat` 调用在提供的切片中不可见。因此，基于切片无法确认是否存在缓冲区溢出风险，判定为误报。 |
| 878 | vim-9.1.1040 | transstr | cpp/unbounded-write | 400 | FP | FP | 切片代码显示，目标缓冲区 `res` 的大小是通过 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 精确分配的，其大小足以容纳源字符串 `s` 转换后的结果。`transchar_byte... |
| 879 | vim-9.1.1040 | globpath | cpp/unbounded-write | 3809 | FP | FP | 切片代码显示，在调用STRCAT(buf, file)之前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区`buf`（大小为MAXPATHL）的剩余空间是否足... |
| 880 | vim-9.1.1040 | win_redr_status_matches | cpp/unbounded-write | 640 | FP | FP | 代码中缓冲区大小已根据Columns和字符编码（MB_MAXBYTES）进行分配，且STRCPY的目标缓冲区（buf + len）和源字符串（transchar('｜')或transchar_byte(*s)）均在循环内受控，tran... |
| 881 | vim-9.1.1040 | win_redr_status_matches | cpp/unbounded-write | 659 | FP | FP | STRCPY 的目标缓冲区 `buf + len` 是动态分配的，其大小 `Columns * MB_MAXBYTES + 1` 或 `Columns + 1` 已考虑多字节字符的最大长度，且源字符串 `transchar_byte(... |
| 883 | vim-9.1.1040 | has_profiling | cpp/unbounded-write | 973 | FP | FP | STRCPY的目标缓冲区pe->pen_name的大小为STRLEN(fname) + 1，与源字符串fname的长度精确匹配，且分配了足够空间，因此不会发生缓冲区溢出。 |
| 884 | vim-9.1.1040 | ex_diffpatch | cpp/unbounded-write | 1363 | FP | FP | 告警涉及多个strcpy调用，但切片代码中仅显示对固定长度缓冲区tmp_new的复制，且tmp_new由vim_tempname生成，其长度受TEMPNAMELEN限制，加上固定后缀“.orig”和“.rej”后仍不会超过分配的buf... |
| 885 | vim-9.1.1040 | do_string_sub | cpp/unbounded-write | 7726 | FP | FP | STRCPY宏的目标缓冲区`(char *)ga.ga_data + ga.ga_len`是动态增长的数组`ga`的一部分，其大小已通过`ga_grow`确保有足够空间容纳源字符串`tail`，且`tail`是输入字符串`str`的子... |
| 886 | vim-9.1.1040 | set_var_const | cpp/unbounded-write | 4184 | FP | FP | STRCPY宏的目标缓冲区di->di_key的大小为STRLEN(varname) + 1，与源字符串varname的长度完全匹配，且varname已通过valid_varname()验证，不会导致缓冲区溢出。 |
| 887 | vim-9.1.1040 | cat_prefix_varname | cpp/unbounded-write | 2505 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过动态内存分配确保目标缓冲区varnamebuf的大小（varnamebuflen）大于源字符串name的长度加2，因此不存在缓冲区溢出的风险。 |
| 888 | vim-9.1.1040 | ex_substitute | cpp/unbounded-write | 4883 | FP | FP | 切片代码中未发现对strcat函数的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中不存在。该告警可能是工具对宏展开或代码分析的误判，实际代码中未发现缓冲区溢出风险。 |
| 889 | vim-9.1.1040 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区buf分配了精确计算的长度len，该长度已包含源字符串cmd的长度和必要的额外字符及终止符，因此不会发生缓冲区溢出。 |
| 890 | vim-9.1.1040 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 代码在调用STRCAT（即strcat）前，已通过alloc(len)为目标缓冲区buf分配了精确计算的长度len，该长度已包含所有待拼接字符串及终止符的空间，因此不存在缓冲区溢出的风险。 |
| 891 | vim-9.1.1040 | ex_sort | cpp/unbounded-write | 605 | FP | FP | 代码中 `STRCPY(sortbuf1, s)` 的源字符串 `s` 来自 `ml_get(get_lnum)`，其长度已在循环前通过 `ml_get_len` 获取并用于分配缓冲区 `sortbuf1`（大小为 `maxlen +... |
| 892 | vim-9.1.1040 | expand_sfile | cpp/unbounded-write | 10068 | FP | FP | 代码中目标缓冲区 `newres` 的大小为 `resultlen + 1`，而 `STRCPY` 复制的源字符串 `repl` 长度 `repllen` 已通过 `resultlen += repllen - srclen` 计算并... |
| 893 | vim-9.1.1040 | repl_cmdline | cpp/unbounded-write | 5307 | FP | FP | 代码中目标缓冲区 `new_cmdline` 的大小 `i` 已通过 `alloc(i)` 精确分配，其大小包含了源字符串 `src + srclen` 的长度 `taillen` 和必要的空字符空间，因此 `STRCPY` 操作不会... |
| 894 | vim-9.1.1040 | repl_cmdline | cpp/unbounded-write | 5313 | FP | FP | 代码通过alloc(i)为目标缓冲区new_cmdline分配了内存，其中i已精确计算了所需的总长度（包括源字符串长度、替换字符串长度、尾部长度和额外空间），并在调用STRCPY前通过mch_memmove进行了安全复制，确保了目标缓... |
| 897 | vim-9.1.1040 | do_one_cmd | cpp/unbounded-write | 2678 | FP | FP | 切片代码中未发现对STRCPY宏（即strcpy）的直接调用，告警消息中提到的多个strcpy调用在提供的代码片段中不可见。因此，基于切片内可见的证据，无法确认存在缓冲区溢出漏洞，应视为误报。 |
| 898 | vim-9.1.1040 | discard_exception | cpp/unbounded-write | 646 | FP | FP | STRCPY 的目标缓冲区 IObuff 是全局缓冲区，其大小在代码中定义为 IOSIZE（通常足够大），且源字符串 saved_IObuff 是之前通过 vim_strsave(IObuff) 保存的 IObuff 副本，长度相同，... |
| 899 | vim-9.1.1040 | get_exception_string | cpp/unbounded-write | 473 | FP | FP | 目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度足以容纳前缀字符串和源字符串 `mesg` 或 `p` 的总长度，因此 `strcat` 操作不会导致缓冲区溢出。 |
| 902 | vim-9.1.1040 | cmdline_browse_history | cpp/unbounded-write | 1494 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc_cmdbuff((int)plen)为目标缓冲区ccline.cmdbuff分配了足够容纳源字符串p（长度为plen）的空间，确保了不会发生缓冲区溢出。 |
| 904 | vim-9.1.1040 | vim_settempdir | cpp/unbounded-write | 5286 | FP | FP | 告警点位于 `STRCPY(buf, tempdir)`，但切片显示其仅在 `vim_FullName` 调用失败时执行。`buf` 已通过 `alloc(MAXPATHL + 2)` 分配了固定大小的缓冲区，且 `tempdir` ... |
| 905 | vim-9.1.1040 | vim_rename | cpp/unbounded-write | 3858 | FP | FP | 在调用STRCPY(tempname, from)之前，已有条件判断`if (STRLEN(from) >= MAXPATHL - 5) return -1;`，确保源字符串长度不会导致目标缓冲区tempname（大小为MAXPATH... |
| 906 | vim-9.1.1040 | buf_modname | cpp/unbounded-write | 3636 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区retval分配了足够的内存（fnamelen + extlen + 3），且源字符串fname的长度fnamelen已通过STRLEN获取，因此不会发生缓冲区溢出。 |
| 907 | vim-9.1.1040 | addfile | cpp/unbounded-write | 4202 | FP | FP | 目标缓冲区 `p` 的大小通过 `alloc(STRLEN(f) + 1 + isdir)` 精确分配，其长度等于源字符串 `f` 的长度加上终止符和可能的额外字符，因此 `strcpy` 操作不会导致缓冲区溢出。 |
| 908 | vim-9.1.1040 | unix_expandpath | cpp/unbounded-write | 3837 | FP | FP | 代码中使用了STRCPY宏，但目标缓冲区buf的大小为STRLEN(path) + MAXPATHL，而源字符串是path_end + 1，它是原始路径的一部分，其长度不会超过原始路径长度，因此不会超过目标缓冲区大小。此外，该函数是递... |
| 909 | vim-9.1.1040 | concat_fnames | cpp/unbounded-write | 3127 | FP | FP | 代码在调用strcpy前，已通过alloc为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了缓冲区大小足以容纳拼接后的字符串，因此不存在缓冲区溢出风险。 |
| 910 | vim-9.1.1040 | concat_fnames | cpp/unbounded-write | 3130 | FP | FP | 函数通过alloc为目标缓冲区分配了足够的空间，其大小为两个输入字符串长度之和加3，确保了strcat操作不会导致缓冲区溢出。 |
| 911 | vim-9.1.1040 | uniquefy_paths | cpp/unbounded-write | 2364 | FP | FP | 告警点 `STRCAT(file_pattern, pattern)` 中，`file_pattern` 已通过 `alloc(len + 2)` 分配了足够空间（`len` 为 `pattern` 长度，加2用于存放前缀 '*' 和... |
| 912 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1718 | FP | FP | 代码中STRCPY宏的目标缓冲区NameBuff大小为MAXPATHL，而源字符串长度在复制前已通过STRLEN检查并确保STRLEN(rel_fname) + l < MAXPATHL，因此不会发生缓冲区溢出。 |
| 913 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1719 | FP | FP | 代码中STRCPY宏展开为strcpy，但目标缓冲区NameBuff大小为MAXPATHL，而源字符串*file_to_find或rel_fname的长度在复制前已通过STRLEN检查，确保STRLEN(rel_fname) + l ... |
| 914 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1724 | FP | FP | STRCPY 宏的目标缓冲区 NameBuff 大小为 MAXPATHL，而源字符串 *file_to_find 是经过 expand_env_esc 处理后的环境变量扩展结果，其长度已通过 MAXPATHL 参数限制，因此不会发生缓... |
| 915 | vim-9.1.1040 | ff_check_visited | cpp/unbounded-write | 1370 | FP | FP | STRCPY的目标缓冲区vp->ffv_fname的大小已通过alloc精确分配，其大小为STRLEN(ff_expand_buffer) + 1，与源字符串长度完全匹配，因此不会发生缓冲区溢出。 |
| 916 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 805 | FP | FP | 代码在调用STRCPY前，已通过STRLEN检查确保目标缓冲区大小（MAXPATHL）足够容纳源字符串，并包含终止符，因此不存在缓冲区溢出风险。 |
| 917 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 819 | FP | FP | 代码在调用STRCAT前，已通过STRLEN(file_path) + STRLEN(stackp->ffs_fix_path) + 1 < MAXPATHL检查了目标缓冲区剩余空间，确保不会发生缓冲区溢出。 |
| 918 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 940 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过STRLEN(file_path) + STRLEN(search_ctx->ffsc_file_to_search) + 1 < MAXPATHL进行了明确的长度检查，确保目标缓冲区... |
| 919 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 942 | FP | FP | 代码在每次使用STRCAT前都通过STRLEN(file_path) + STRLEN(source_string) + 1 < MAXPATHL进行了明确的缓冲区长度检查，确保不会发生溢出。告警点位于条件保护块内，是安全的。 |
| 920 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 1110 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过STRLEN检查确保目标缓冲区file_path（大小为MAXPATHL）有足够空间容纳源字符串，防止了缓冲区溢出。 |
| 921 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 1112 | FP | FP | 代码在调用STRCAT前，已通过STRLEN(file_path) + STRLEN(search_ctx->ffsc_fix_path) < MAXPATHL的条件检查，确保目标缓冲区file_path（大小为MAXPATHL）有足... |
| 922 | vim-9.1.1040 | <global> | cpp/unbounded-write | 537 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区ff_expand_buffer已通过alloc(MAXPATHL)分配，其大小固定为MAXPATHL，且所有使用STRCPY的源字符串长度均经过检查（如len + 1 < MAXPATHL），... |
| 923 | vim-9.1.1040 | <global> | cpp/unbounded-write | 545 | FP | FP | 切片代码中所有STRCPY宏的使用，其目标缓冲区（如`buf`、`ff_expand_buffer`）在复制前都经过了明确的长度计算和分配（例如`alloc(eb_len + ... + 1)`），或目标缓冲区是固定大小的全局缓冲区`... |
| 924 | vim-9.1.1040 | <global> | cpp/unbounded-write | 548 | FP | FP | 目标缓冲区 `ff_expand_buffer` 在函数开头已通过 `alloc(MAXPATHL)` 分配，大小为 `MAXPATHL`。告警处的 `STRCAT` 操作拼接的字符串 `search_ctx->ffsc_fix_pa... |
| 925 | vim-9.1.1040 | <global> | cpp/unbounded-write | 590 | FP | FP | 切片代码中，STRCPY 宏被用于将已知长度的字符串复制到新分配的缓冲区中，目标缓冲区大小已通过 alloc 函数确保足够容纳源字符串，不存在缓冲区溢出的风险。 |
| 926 | vim-9.1.1040 | <global> | cpp/unbounded-write | 591 | FP | FP | STRCAT 的目标缓冲区 `temp` 是通过 `alloc` 分配的，其大小为 `STRLEN(search_ctx->ffsc_wc_path) + STRLEN(search_ctx->ffsc_fix_path + len)... |
| 927 | vim-9.1.1040 | <global> | cpp/unbounded-write | 3798 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够大小的缓冲区，其大小计算包含了源字符串s的长度，因此不会发生缓冲区溢出。 |
| 928 | vim-9.1.1040 | foldDelMarker | cpp/unbounded-write | 1897 | FP | FP | 代码中目标缓冲区 `newline` 的大小通过 `alloc(ml_get_len(lnum) - len + 1)` 精确分配，其大小等于原行长减去被删除标记的长度再加1（用于空字符）。随后使用 `STRCPY` 复制剩余部分，源... |
| 929 | vim-9.1.1040 | foldAddMarker | cpp/unbounded-write | 1815 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区newline分配了足够空间（line_len + markerlen + STRLEN(cms) + 1），且分配大小计算包含了源字符串长度，因此不会发生缓冲区溢出。 |
| 930 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2899 | FP | FP | 告警点 `STRCPY(buffer, res_prolog->title);` 中，`buffer` 是大小为256的局部数组，`res_prolog->title` 来源于资源文件头部的 `PRT_DSC_TITLE_TYPE` ... |
| 931 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2901 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_prolog->title`和`res_prolog->version`均来自受控的PostScript资源文件，其内容长度已在`prt_open_resource`函数中通过解... |
| 932 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2905 | FP | FP | 目标缓冲区 `buffer` 大小为256字节，而源字符串 `res_cidfont->title` 的长度已在 `prt_open_resource` 函数中通过 `vim_strncpy` 限制为不超过 `dsc_line.len... |
| 933 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 切片代码显示，`res_cidfont->title` 和 `res_cidfont->version` 来源于外部资源文件，其内容在 `prt_open_resource` 函数中通过解析文件头获得，长度受文件格式和解析逻辑限制。结... |
| 934 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 告警点 `STRCPY(buffer, res_cmap->title);` 中，`res_cmap->title` 来源于外部资源文件，其内容在 `prt_open_resource` 函数中通过解析文件头获得，长度受 `vim_s... |
| 935 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 切片代码显示，`res_cmap->title` 和 `res_cmap->version` 来自受控的资源文件解析（`prt_open_resource`），其长度已在解析时被限制（`vim_strncpy` 确保以空字符结尾且不越... |
| 936 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2920 | FP | FP | 告警点 `STRCPY(buffer, res_encoding->title);` 中，`buffer` 是大小为256的局部数组，`res_encoding->title` 来源于外部资源文件，但其长度已在 `prt_open_r... |
| 937 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2922 | FP | FP | 告警涉及的`buffer`数组大小为256字节，而`res_encoding->title`和`res_encoding->version`均来自受控的PostScript资源文件，其内容在`prt_open_resource`函数中... |
| 938 | vim-9.1.1040 | prt_resource_name | cpp/unbounded-write | 1659 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过`if (STRLEN(filename) >= MAXPATHL)`检查源字符串长度，若过长则将目标缓冲区置空，否则才执行拷贝。这提供了长度保护，防止了缓冲区溢出，因此是误报。 |
| 939 | vim-9.1.1040 | do_helptags | cpp/unbounded-write | 1210 | FP | FP | 告警点 `STRCPY(NameBuff, dirname);` 中，目标缓冲区 `NameBuff` 是一个全局或静态数组，其大小在切片中未明确给出，但根据其在整个代码库中的典型用法（如 `helptags_one` 函数中用于构建... |
| 940 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 975 | FP | FP | 代码中使用了STRCAT宏，其底层是strcat，存在缓冲区溢出风险。但NameBuff是一个全局缓冲区，其大小定义为MAXPATHL（通常足够大，如260或4096）。告警点拼接的字符串由固定字符串'/**/*'和参数ext组成，e... |
| 941 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 991 | FP | FP | 目标缓冲区 `NameBuff` 在代码中未定义其大小，但根据上下文（如 `MAXPATHL` 的使用）推断，它很可能是一个足够大的固定大小缓冲区（如 `MAXPATHL`）。告警点 `STRCAT(NameBuff, tagfnam... |
| 942 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 1112 | FP | FP | sprintf 的目标缓冲区 s 的大小是精确计算的（p2 - p1 + STRLEN(fname) + 2），足以容纳源字符串 p1 和 fname，因此不会发生缓冲区溢出。 |
| 943 | vim-9.1.1040 | highlight_set_startstop_termcode | cpp/unbounded-write | 1481 | FP | FP | 代码在调用STRCAT前已通过条件`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了缓冲区长度，确保拼接后的总长度小于buf的大小（100），因此不会发生缓冲区溢出。 |
| 944 | vim-9.1.1040 | load_colors | cpp/unbounded-write | 602 | FP | FP | 缓冲区 `buf` 的大小通过 `alloc(STRLEN(name) + 12)` 分配，其中 `+12` 足以容纳固定字符串 `"colors/.vim"` 的长度（11个字符）和结尾空字符，因此 `sprintf` 的格式化输出... |
| 946 | vim-9.1.1040 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...），并分配了对应大小的内存（buf = alloc(amt)），确保了目标缓冲区大小足够，不会发生溢出。 |
| 947 | vim-9.1.1040 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了该大小的内存，确保了目标缓冲区大小与格式化字符串长度完全匹配，不存在溢出风险。 |
| 948 | vim-9.1.1040 | <global> | cpp/unbounded-write | 1456 | FP | FP | 目标缓冲区 csinfo[i].fname 的大小通过 alloc(strlen(fname)+1) 精确分配，长度与源字符串 fname 完全匹配，strcpy 操作不会导致缓冲区溢出。 |
| 950 | vim-9.1.1040 | cs_add_common | cpp/unbounded-write | 604 | FP | FP | sprintf 的目标缓冲区 fname2 的大小是动态计算的，为 strlen(CSCOPE_DBFILE) + strlen(fname) + 2，这确保了格式化字符串 "%s/%s" 的结果不会溢出。fname 的长度在之前的循... |
| 951 | vim-9.1.1040 | ins_compl_infercase_gettext | cpp/unbounded-write | 653 | FP | FP | 告警点 `STRCPY(gap.ga_data, IObuff)` 中，目标缓冲区 `gap.ga_data` 的大小已通过 `ga_grow(&gap, IOSIZE)` 确保至少为 `IOSIZE`，而源字符串 `IObuff` ... |
| 953 | vim-9.1.1040 | findswapname | cpp/unbounded-write | 4967 | FP | FP | STRCPY 的目标缓冲区 fname2 是通过 alloc(n + 2) 分配的，其大小 n+2 大于源字符串 fname 的长度 n（n = STRLEN(fname)），因此复制操作不会导致缓冲区溢出。 |
| 954 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2157 | FP | FP | 目标缓冲区 `s` 的大小通过 `alloc(STRLEN(f) + 1)` 分配，其长度精确等于源字符串 `f` 的长度加1，因此 `STRCPY(s, f)` 不会发生缓冲区溢出。告警是基于源数据来自外部这一事实，但分配逻辑确保了... |
| 955 | vim-9.1.1040 | <global> | cpp/unbounded-write | 811 | FP | FP | 代码中STRCPY宏的目标缓冲区大小是动态分配的，通过alloc(STRLEN(call_data) + 5)确保有足够空间容纳源字符串和额外控制字符，不存在缓冲区溢出风险。 |
| 956 | vim-9.1.1040 | <global> | cpp/unbounded-write | 815 | FP | FP | 代码中STRCPY宏的目标缓冲区大小通过alloc(STRLEN(call_data) + 5)动态分配，长度已包含源字符串长度加额外字符，因此不会发生缓冲区溢出。 |
| 957 | vim-9.1.1040 | msg_show_console_dialog | cpp/unbounded-write | 4502 | FP | FP | 告警点 `STRCPY(confirm_msg + 1, message)` 的目标缓冲区 `confirm_msg` 已通过 `alloc(len)` 分配，其大小 `len` 已计算并包含了源字符串 `message` 的长度（`... |
| 958 | vim-9.1.1040 | str2specialbuf | cpp/unbounded-write | 2017 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度小于传入的长度参数`len... |
| 959 | vim-9.1.1040 | get_emsg_source | cpp/unbounded-write | 502 | FP | FP | 代码在调用 sprintf 前，已通过 `alloc(STRLEN(sname) + STRLEN(p))` 为目标缓冲区分配了足够的空间，其大小等于两个字符串长度之和，确保了不会发生缓冲区溢出。 |
| 960 | vim-9.1.1040 | may_trigger_modechanged | cpp/unbounded-write | 2836 | FP | FP | STRCPY宏展开为strcpy，其目标缓冲区last_mode和源缓冲区curr_mode大小均为MODE_MAX_LENGTH，且源字符串curr_mode由get_mode函数生成，该函数内部逻辑确保写入的字符数严格受控，不会超... |
| 961 | vim-9.1.1040 | expand_env_esc | cpp/unbounded-write | 1647 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过条件`(STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen)`明确检查了目标缓冲区`dst`的剩余空间`dstlen`是否足够容纳源字符... |
| 962 | vim-9.1.1040 | call_shell | cpp/unbounded-write | 1877 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够的内存，其大小为STRLEN(ecmd) + STRLEN(p_sxq) * 2 + 1，这确保了目标缓冲区ncmd能够容纳源字符串ecmd和p_sxq的拼接，因此不存在缓冲区溢出风险。 |
| 963 | vim-9.1.1040 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 切片代码中，告警点 `STRCAT(newline, oldline + col);` 的 `newline` 缓冲区大小已通过 `alloc(ml_get_len(lnum) + len + 1)` 分配，其中 `len` 是待插入... |
| 965 | vim-9.1.1040 | push_showcmd | cpp/unbounded-write | 1808 | FP | FP | 切片代码显示，`STRCPY` 的目标缓冲区 `old_showcmd_buf` 和源缓冲区 `showcmd_buf` 均为全局数组，其大小在别处定义且应保持一致。告警基于外部输入可能污染源缓冲区的假设，但切片中未提供任何证据表明 ... |
| 966 | vim-9.1.1040 | add_to_showcmd | cpp/unbounded-write | 1763 | FP | FP | 代码在调用STRCAT前，已通过计算old_len和extra_len检查了缓冲区溢出风险，并在溢出时通过mch_memmove移动了缓冲区内容，确保了拼接操作不会越界。 |
| 967 | vim-9.1.1040 | op_change | cpp/unbounded-write | 2003 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区newp已通过alloc分配了足够大小（ml_get_len(linenr) + vpos.coladd + ins_len + 1），且源缓冲区oldp + bd.textcol的长度不会超过m... |
| 968 | vim-9.1.1040 | op_replace | cpp/unbounded-write | 1299 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`newp`的大小已通过`alloc(oldlen + 1 + n)`精确分配，且源字符串`oldp + bd.textcol + bd.textlen`是已知行内子串，其长度不会超过原始行长度`... |
| 969 | vim-9.1.1040 | op_replace | cpp/unbounded-write | 1308 | FP | FP | 代码中STRCPY的目标缓冲区`after_p`是通过`alloc(oldlen + 1 + n - newlen)`分配的，其大小`oldlen + 1 + n - newlen`明确大于等于源字符串`oldp + bd.textc... |
| 970 | vim-9.1.1040 | op_delete | cpp/unbounded-write | 962 | FP | FP | 切片代码中STRCPY宏的目标缓冲区newp是通过alloc(ml_get_len(lnum) + 1 - n)分配的，其大小精确等于源字符串oldp + bd.textcol + bd.textlen的长度（通过计算得出），因此不会... |
| 971 | vim-9.1.1040 | block_insert | cpp/unbounded-write | 743 | FP | FP | STRCPY 的目标缓冲区 newp 是通过 alloc 分配的，其大小为 ml_get_len(lnum) + spaces + slen + ...，而源字符串 oldp 来自 ml_get(lnum)，其长度不超过 ml_get... |
| 972 | vim-9.1.1040 | option_value2string | cpp/unbounded-write | 8324 | FP | FP | 切片代码显示，告警点 STRCPY 的目标缓冲区是 NameBuff，但切片中未提供其大小定义，无法判断 strcpy 操作是否会导致缓冲区溢出。告警基于外部输入可能过长的假设，但缺乏目标缓冲区大小的关键信息，无法确认漏洞存在。 |
| 973 | vim-9.1.1040 | option_value2string | cpp/unbounded-write | 8326 | FP | FP | 切片代码显示，告警点 STRCPY 的目标缓冲区 NameBuff 在多个代码路径中均受到明确的长度限制（如 MAXPATHL 或 MAXPATHL - 1），且告警点所在分支（wc != 0）的源数据来自受控的内部函数 transc... |
| 974 | vim-9.1.1040 | stropt_expand_envvar | cpp/unbounded-write | 1803 | FP | FP | 目标缓冲区 `newval` 的大小 `newlen` 已通过 `alloc(newlen)` 精确分配，其大小等于源字符串 `s` 的长度加1（以及可能的 `origval` 长度），足以容纳 `STRCPY` 的复制操作，因此不存... |
| 975 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 6989 | FP | FP | 代码在调用strcat前，已通过alloc(len)为目标缓冲区command分配了精确计算的长度len，该长度已考虑了所有待拼接字符串（包括环境变量、函数名、选项和模式参数）的总和，并预留了必要的分隔符和转义字符空间，因此不存在缓冲... |
| 976 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 7029 | FP | FP | 代码在调用strcat前，已通过alloc(len)为目标缓冲区command分配了精确计算的长度len，该长度已考虑了所有待拼接字符串（包括tempname）的总和，因此不会发生缓冲区溢出。 |
| 977 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 7335 | FP | FP | 代码中使用了宏 `STRCPY(p, (*file)[i])`，但目标缓冲区 `p` 的大小是通过 `alloc(STRLEN((*file)[i]) + 1 + dir)` 分配的，长度等于源字符串长度加可能的路径分隔符，因此 `s... |
| 978 | vim-9.1.1040 | mch_FullName | cpp/unbounded-write | 2819 | FP | FP | 代码在调用STRCAT（即strcat）前，已通过条件`(int)(STRLEN(buf) + STRLEN(fname)) >= len`检查了目标缓冲区`buf`的剩余空间是否足以容纳源字符串`fname`，确保了不会发生缓冲区溢出。 |
| 979 | vim-9.1.1040 | qf_store_title | cpp/unbounded-write | 1934 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc_id为目的地缓冲区分配了精确的内存大小（STRLEN(title) + 2），确保了缓冲区足以容纳源字符串及可能的额外字符，因此不存在缓冲区溢出风险。 |
| 982 | vim-9.1.1040 | regtilde | cpp/unbounded-write | 1959 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过`alloc(tmpsublen + 1)`为目标缓冲区`tmpsub`分配了精确大小的内存（`tmpsublen + 1`），且`tmpsublen`已计算了前缀、替换内... |
| 983 | vim-9.1.1040 | match_with_backref | cpp/unbounded-write | 1600 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区reg_tofree分配了足够的内存，其中len的计算基于STRLEN(rex.line) + 50，确保了目标缓冲区大小不小于源字符串长度... |
| 984 | vim-9.1.1040 | get_reg_contents | cpp/unbounded-write | 2733 | FP | FP | 代码中目标缓冲区 `retval` 的大小已通过循环精确计算（`len`），并分配了 `len + 1` 的空间，随后使用 `STRCPY` 进行拷贝，其源字符串 `y_current->y_array[i].string` 的长度 ... |
| 985 | vim-9.1.1040 | do_put | cpp/unbounded-write | 2159 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区newp是通过alloc函数分配的内存，其大小计算为`ml_get_len(lnum) - col + totlen + 1`，其中totlen为源字符串长度，分配大小已包含源字符串长度和NUL终... |
| 986 | vim-9.1.1040 | do_put | cpp/unbounded-write | 2160 | FP | FP | 代码中使用了STRCPY宏，但目标缓冲区newp是通过alloc(totlen + oldlen + 1)或类似方式分配的，其大小明确为源字符串长度加上其他内容的总和加1，足以容纳源字符串和终止符，不存在缓冲区溢出风险。 |
| 987 | vim-9.1.1040 | op_yank | cpp/unbounded-write | 1315 | FP | FP | STRCPY宏用于拼接两个已知长度的字符串，目标缓冲区pnew已通过alloc分配了精确大小（curr->y_array[j].length + y_current->y_array[0].length + 1），且拼接前已确保目标缓... |
| 988 | vim-9.1.1040 | op_yank | cpp/unbounded-write | 1316 | FP | FP | 代码中STRCPY宏的目标缓冲区pnew是通过alloc函数分配的内存，其大小为两个源字符串长度之和加1，确保了缓冲区足够容纳拼接后的字符串，因此不存在缓冲区溢出风险。 |
| 993 | vim-9.1.1040 | dump_word | cpp/unbounded-write | 4187 | FP | FP | STRCPY宏的目标缓冲区badword大小为MAXWLEN+10，源字符串p来自word或cword，而cword和word的最大长度受MAXWLEN限制，因此复制操作不会导致缓冲区溢出。 |
| 994 | vim-9.1.1040 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 函数 `make_case_word` 的调用者 `allcap_copy` 和 `onecap_copy` 内部均包含对目标缓冲区 `cword`（即 `wcopy`）的边界检查，确保写入不会超过 `MAXWLEN`。`STRCPY... |
| 995 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2998 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区p分配了足够的空间（ml_get_curline_len() + addlen + 1），且复制的源字符串repl_to的长度repl_to_len已知，目标偏移curwin-... |
| 996 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2999 | FP | FP | 代码在调用STRCAT前，已为目标缓冲区p分配了足够的空间（ml_get_curline_len() + addlen + 1），且拼接的源字符串长度（line + curwin->w_cursor.col + repl_from_l... |
| 998 | vim-9.1.1040 | spell_load_lang | cpp/unbounded-write | 1632 | FP | FP | STRCPY的目标缓冲区sl.sl_lang的大小未在切片中明确给出，但告警点位于函数开头，且参数lang是函数输入，其长度在调用前未知。然而，该函数是加载拼写文件的内部函数，lang参数通常来自受控的配置或有限集合，并非直接来自不可... |
| 999 | vim-9.1.1040 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过`buflen < len + MAXWLEN + 2`的判断为`buf`分配了足够大的内存（`buflen = len + MAXWLEN + 2`），且`buf`指向新分配的内存。... |
| 1000 | vim-9.1.1040 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数getroom_save通过getroom分配了长度为STRLEN(s)+1的内存，然后使用STRCPY（即strcpy）进行拷贝，目标缓冲区大小与源字符串长度精确匹配，不存在缓冲区溢出的风险。 |
| 1001 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 代码中STRCAT的目标缓冲区p是通过getroom()动态分配的，其大小已根据源字符串长度计算并预留了足够空间（包括分隔符和空字符），因此不会发生缓冲区溢出。 |
| 1002 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 代码中告警点（STRCAT(p, items[1])）的缓冲区p是通过getroom(spin, ...)分配的，其大小已根据items[0]和items[1]的长度精确计算并预留了额外空间，因此不会发生缓冲区溢出。 |
| 1003 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2464 | FP | FP | 代码中STRCPY的目标缓冲区p已通过getroom(spin, STRLEN(items[1]) + 2, FALSE)分配了足够空间（源字符串长度加2），且源字符串items[1]来自受控的aff文件解析，不存在缓冲区溢出风险。 |
| 1004 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 代码中STRCAT的目标缓冲区p是通过getroom()动态分配的，其大小已根据源字符串长度精确计算（STRLEN(items[0]) + STRLEN(items[1]) + 3），因此不会发生缓冲区溢出。 |
| 1005 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 代码中使用了STRCPY宏，但目标缓冲区p是通过getroom(spin, STRLEN(items[1]) + 2, FALSE)分配的，其大小明确为源字符串长度加2，足以容纳源字符串和追加的'+'字符，因此不会发生缓冲区溢出。 |
| 1006 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2746 | FP | FP | sprintf的目标缓冲区buf大小为MAXLINELEN（定义为256），而源字符串items[4]来自受控的.aff文件行解析，其长度受MAXLINELEN限制，且拼接的格式字符串固定为'^%s'或'%s$'，总长度不会超过MAX... |
| 1007 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2748 | FP | FP | 代码中使用了 `sprintf` 构建正则表达式模式，但目标缓冲区 `buf` 的大小为 `MAXLINELEN`（定义为 1024），而源字符串 `items[4]` 来自受控的 .aff 文件行，其长度受 `MAXLINELEN`... |
| 1008 | vim-9.1.1040 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | STRCPY 的目标缓冲区 sft->sft_word 的大小为 STRLEN(goodword) + 1，而源字符串 goodword 的长度恰好等于该缓冲区大小（通过 alloc(offsetof(sftword_T, sft_w... |
| 1009 | vim-9.1.1040 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY 宏的目标缓冲区 fword 的大小为 MAXWLEN，而源字符串 su->su_fbadword 是拼写建议算法内部生成的数据，其长度在算法逻辑中已被确保不会超过 MAXWLEN（例如通过 spell_casefold ... |
| 1010 | vim-9.1.1040 | concat_str | cpp/unbounded-write | 811 | FP | FP | 函数内部通过alloc为目标缓冲区分配了精确的、足以容纳源字符串的长度（包括终止符），然后才调用STRCPY（即strcpy），因此不存在缓冲区溢出的风险。告警是基于对strcpy的通用模式检测，未考虑此处精确的长度计算和分配。 |
| 1011 | vim-9.1.1040 | concat_str | cpp/unbounded-write | 813 | FP | FP | 函数通过`alloc`为目标缓冲区分配了精确的、足以容纳源字符串的长度（`l + STRLEN(str2) + 1`），并使用了正确的偏移量`dest + l`进行拷贝，因此`STRCPY`（即`strcpy`）的使用是安全的，不会发... |
| 1012 | vim-9.1.1040 | expand_tag_fname | cpp/unbounded-write | 4125 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区retval分配了固定大小MAXPATHL，且后续的vim_strncpy调用明确限制了拷贝长度，确保不会超出缓冲区边界。因此，该strcpy使用是安全的，属于工具误报。 |
| 1015 | vim-9.1.1040 | show_one_termcode | cpp/unbounded-write | 7059 | FP | FP | STRCPY的目标缓冲区IObuff+5有足够的空间，因为IObuff是一个大数组（未在切片中显示但根据上下文推断），且源字符串p来自get_special_key_name，该函数内部使用STRCPY时进行了长度检查（len + i... |
| 1016 | vim-9.1.1040 | current_tagblock | cpp/unbounded-write | 1386 | FP | FP | sprintf 使用的格式化字符串包含明确的长度限制符 `%.*s`，其中 `len` 参数控制了从指针 `p` 写入目标缓冲区的最大字节数，且目标缓冲区 `spat` 和 `epat` 的大小（`len + 39` 和 `len +... |
| 1017 | vim-9.1.1040 | uc_check_code | cpp/unbounded-write | 1782 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过STRLEN计算了源字符串长度，且目标缓冲区buf的大小由调用方控制，但告警点处（case ct_ARGS, quote==0）的代码路径中，目标缓冲区大小未在切片内明确验证... |
| 1018 | vim-9.1.1040 | get_scriptlocal_funcname | cpp/unbounded-write | 4705 | FP | FP | 代码通过alloc为newname分配了精确的内存空间，大小为sid_buf长度、p+off长度及终止符之和，确保缓冲区足够容纳拼接后的字符串，因此strcat操作不会导致溢出。 |
| 1019 | vim-9.1.1040 | trans_function_name_ext | cpp/unbounded-write | 4618 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`name`的大小为`len + lead + extra + 1`，由`alloc`分配，而源字符串`sid_buf`的大小由`vim_snprintf`写入，其目标缓冲区大小为`sizeof(... |
| 1020 | vim-9.1.1040 | fname_trans_sid | cpp/unbounded-write | 2212 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过条件`i + STRLEN(name + llen) < FLEN_FIXED`检查了目标缓冲区`fname_buf`的剩余空间是否足够，若不足则分配新缓冲区，因此不存在缓冲区溢出风险。 |
| 1023 | vim-9.1.1040 | exec_instructions | cpp/unbounded-write | 3613 | FP | FP | 切片代码中显示的 STRCPY 宏调用位于 ISN_EXECCONCAT 指令处理中，其中目标缓冲区 'cmd' 已通过 alloc(len + 1) 分配了足够空间（len 已预先计算了所有源字符串的总长度），因此不会发生缓冲区溢出。 |
| 1024 | vim-9.1.1040 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | FP | 代码中目标缓冲区 `funcname` 的大小通过 `alloc(STRLEN(name) + 3)` 分配，其长度已明确为源字符串 `name` 的长度加上前缀 "g:" 的两个字符和结尾空字符，因此 `STRCPY(funcnam... |
| 1025 | vim-9.1.1040 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | FP | STRCPY的目标缓冲区newsav->sav_key的大小是通过offsetof(sallvar_T, sav_key) + STRLEN(name) + 1精确分配的，确保了足够的空间来容纳源字符串name及其终止空字符，因此不会... |
| 1026 | vim-9.1.1040 | find_exported | cpp/unbounded-write | 756 | FP | FP | 代码在调用sprintf前已通过动态分配确保了目标缓冲区大小足够，且对长度进行了计算和检查，不存在缓冲区溢出的风险。 |
| 1027 | vim-9.1.1040 | find_exported | cpp/unbounded-write | 763 | FP | FP | 代码在调用sprintf前已通过动态分配确保目标缓冲区大小足够：当计算出的长度len超过静态缓冲区buffer大小时，会分配一个大小为len的缓冲区funcname，因此不会发生缓冲区溢出。 |
| 1028 | vim-9.1.1040 | xxdline | cpp/unbounded-write | 537 | FP | FP | 目标缓冲区 `z` 是静态数组 `char z[LLEN+1];`，其大小 `LLEN+1` 是编译时常量。告警点 `strcpy(z, l)` 的源 `l` 是函数参数，切片中未显示其来源和长度，但函数 `xxdline` 的上下文... |
| 1029 | vim-9.1.1040 | ExpandBufnames | cpp/invalid-pointer-deref | 2939 | FP | FP | 告警点 `(*file)[count++] = p` 的写入操作受 `round` 循环和 `*file` 分配保护。在 `round == 1` 时，`*file` 为 NULL，代码会提前返回 FAIL，不会执行写入。在 `rou... |
| 1030 | vim-9.1.1040 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | FP | 切片代码显示，在写入 `p[pos.col + 1]` 之前，已通过条件 `width == 2` 确保 `pos.col + 1` 小于分配的 `len`（因为 `width` 是当前单元格的宽度，且循环步进 `pos.col +=... |
| 1031 | vim-9.1.1330 | <global> | cpp/redundant-null-check-simple | 3508 | FP | FP | 告警指出的空指针检查（`inc_opt != NULL`）并非冗余，因为`inc_opt`可能为`p_inc`（全局变量），其值在切片中未定义，无法保证非空。检查是必要的安全防护。 |
| 1032 | vim-9.1.1330 | <global> | cpp/redundant-null-check-simple | 3590 | FP | FP | 告警指出的空指针检查（`inc_opt != NULL`）并非冗余，因为`inc_opt`可能为`p_inc`（全局变量），其值在切片中未定义，无法保证非空。检查是必要的防御性编程。 |
| 1033 | vim-9.1.1330 | findmatchlimit | cpp/offset-use-before-range-check | 2529 | FP | FP | 切片代码显示，在告警点 `linep[pos.col - 1] == '/' && linep[pos.col] == '*'` 之前，存在条件 `(int)pos.col < comment_col` 作为范围检查，确保了 `pos... |
| 1034 | vim-9.1.1330 | common_function | cpp/inconsistent-null-check | 5228 | FP | FP | 代码在调用 `vim_strsave(s)` 后，将返回值赋给变量 `name`，并在后续多个分支中（如 `vim_free(name)`）直接使用 `name` 或将其传递给 `func_ref(name)`。`func_ref` ... |
| 1036 | vim-9.1.1330 | get_isolated_shell_name | cpp/inconsistent-null-check | 2710 | FP | FP | 函数 `gettail` 已对 `NULL` 输入进行了处理，返回空字符串，因此 `vim_strsave` 的参数不会是 `NULL`，其返回值 `p` 在后续路径中会被直接返回，调用方负责检查。切片中未显示调用方对返回值的检查，但... |
| 1037 | vim-9.1.1330 | get_isolated_shell_name | cpp/inconsistent-null-check | 2721 | FP | FP | 函数`get_isolated_shell_name`的返回值`p`被直接返回给调用者，调用者负责检查其是否为NULL。切片代码显示，调用`vim_strnsave`的返回值被赋值给`p`，但函数本身并未使用`p`（例如解引用），因此... |
| 1038 | vim-9.1.1330 | did_set_cryptmethod | cpp/inconsistent-null-check | 1894 | FP | FP | 函数 `vim_strsave` 的返回值被赋值给全局变量 `p_cm`，而 `p_cm` 在后续的 `if (STRCMP(s, p) != 0)` 等条件判断中被使用。这些使用并不依赖于 `p_cm` 是否为 NULL，且切片中未... |
| 1039 | vim-9.1.1330 | did_set_background | cpp/inconsistent-null-check | 1086 | FP | FP | 告警点 `p_bg = vim_strsave(...)` 的返回值被直接赋值给全局变量 `p_bg`，而紧随其后的 `check_string_option(&p_bg)` 函数会检查 `p_bg` 是否为 NULL，若为 NULL... |
| 1040 | vim-9.1.1330 | apply_move_options | cpp/inconsistent-null-check | 531 | FP | FP | 告警点 `find_win_by_nr_or_id` 的返回值被立即用于 `win_valid_any_tab` 函数的条件判断，该函数内部已包含对 `NULL` 指针的检查（`if (win == NULL) return FALS... |
| 1041 | vim-9.1.1330 | <global> | cpp/inconsistent-null-check | 3339 | FP | FP | 告警指出的`regnext`调用未检查null，但切片代码显示`next`变量在后续使用前，其值`scan`已在循环开始处被检查是否为NULL（`if (got_int ｜｜ scan == NULL)`），且`regnext`函数内... |
| 1042 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 代码中 `regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `regcode`（即 `JUST_CALC_SIZE`），该返回值在调用点仅用于指针比较（如 `ret... |
| 1043 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 代码中 `regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `JUST_CALC_SIZE`，而告警点 `br = regnode(NOTHING)` 的返回值仅在... |
| 1044 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 切片代码显示，在调用 `regnext(br)` 之前，已经通过 `if (OP(br) == BRANCH)` 进行了分支判断，并且 `regnext` 函数内部已对 `p == JUST_CALC_SIZE ｜｜ reg_tool... |
| 1045 | vim-9.1.1330 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 告警点位于条件分支 `if (spin->si_first_free == NULL)` 为真的路径中，此时 `getroom` 的返回值被直接赋值给 `n`。后续代码在 `#ifdef SPELL_PRINTTREE` 宏块内对 `... |
| 1046 | vim-9.1.1330 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在赋值给 `tofree` 后，立即被 `name = tag` 覆盖，后续对 `name` 的使用与 `vim_strsave` 的返回值无关，因此该返回值是否为空指... |
| 1047 | vim-9.1.1330 | define_function | cpp/inconsistent-null-check | 5486 | FP | FP | 告警指出的 vim_strchr 调用未检查空指针，但切片代码显示该调用结果仅用于条件判断（!= NULL），并未解引用，因此不存在空指针解引用风险。 |
| 1049 | vim-9.1.1330 | exec_instructions | cpp/inconsistent-null-check | 3666 | FP | FP | 告警点位于 ISN_CONSTRUCT 指令分支，为对象分配内存后立即设置了对象引用计数为1并调用了 object_created()，后续代码中未直接使用该指针进行解引用操作。切片中未显示有对该指针进行解引用或可能导致崩溃的代码路径... |
| 1050 | vim-9.1.1330 | barline_parse | cpp/inconsistent-null-check | 1153 | FP | FP | 告警点 `s = vim_strnsave(s, len);` 的返回值直接赋值给了局部变量 `s`，随后 `value->bv_string = s;`。虽然未显式检查 `vim_strnsave` 是否返回 NULL，但切片代码显... |
| 1051 | vim-9.1.1330 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | 代码中使用了STRCAT宏，但NameBuff缓冲区的大小未在切片中明确给出，且告警点之前的STRCPY操作目标也是NameBuff，表明其大小是预定义的。结合上下文，NameBuff很可能是一个固定大小的全局或静态缓冲区（如MAXP... |
| 1052 | vim-9.1.1330 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 代码中`name`变量来源明确且长度有限（最大为3个字符的字符串字面量或单个字符的数组），`buf`在首次使用前已被初始化为空字符串，连续的`strcat`调用不会导致缓冲区溢出。 |
| 1053 | vim-9.1.1330 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限内容，并确保其以NUL结尾，且后续拼接的源字符串p来自原始单词word，其长度wordlen已通过STRLEN计算并在此前... |
| 1055 | vim-9.1.1330 | highlight_color | cpp/overrunning-write | 3275 | FP | FP | sprintf 格式化字符串为固定的 "#%02x%02x%02x"，输出长度固定为7个字符加上结尾空字符共8字节，目标缓冲区 buf 大小为10字节，不会发生溢出。 |
| 1058 | vim-9.1.1330 | ga_concat_strings | cpp/unbounded-write | 788 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过循环精确计算了目标缓冲区`s`所需的总长度（`len + 1`）并分配了足够空间，且每次复制后指针`p`的移动均基于已复制的字符串长度，因此不会发生缓冲区溢出。 |
| 1059 | vim-9.1.1330 | maketitle | cpp/unbounded-write | 4230 | FP | FP | STRCPY宏调用的目标缓冲区`buf`大小为`IOSIZE`，源字符串`name`是经过`gettail`处理的路径尾部，其长度受原始路径和`namelen`减100操作的限制，且`trans_characters`函数内部有缓冲区... |
| 1060 | vim-9.1.1330 | buf_write | cpp/unbounded-write | 1208 | FP | FP | STRCPY宏用于将已知的本地文件名fname复制到固定大小的缓冲区IObuff中，fname是函数参数，其长度受限于文件系统路径的最大长度（MAXPATHL），且后续使用中通过gettail和sprintf仅追加数字，不会导致缓冲区溢出。 |
| 1061 | vim-9.1.1330 | buf_write | cpp/unbounded-write | 2568 | FP | FP | 告警指出的strcat调用在切片代码中并未出现，切片中仅包含STRCAT宏的定义和使用，但未显示有对用户输入进行未受控拼接的操作。告警可能是基于不完整的数据流分析，实际代码中可能存在边界检查或安全防护。 |
| 1062 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2144 | FP | FP | 告警指向的STRCAT宏调用位于注释处理逻辑中，其目标缓冲区'leader'是通过alloc函数动态分配的，大小计算为'lead_len + lead_repl_len + extra_space + extra_len + (sec... |
| 1063 | vim-9.1.1330 | transstr | cpp/unbounded-write | 400 | FP | FP | 目标缓冲区 `res` 的大小已通过 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 精确分配，其长度足以容纳源字符串 `s` 转换后的所有字符，因此 `strcat` 不会发生溢出。 |
| 1064 | vim-9.1.1330 | globpath | cpp/unbounded-write | 3864 | FP | FP | 切片代码显示，在调用STRCAT(buf, file)之前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区buf的剩余空间，确保拼接后不会溢出。该防护机制使得... |
| 1065 | vim-9.1.1330 | win_redr_status_matches | cpp/unbounded-write | 663 | FP | FP | 目标缓冲区 `buf` 的大小已根据 `Columns` 变量动态分配（`Columns + 1` 或 `Columns * MB_MAXBYTES + 1`），且后续的 `clen` 长度计算和循环条件 `(long)(clen +... |
| 1066 | vim-9.1.1330 | win_redr_status_matches | cpp/unbounded-write | 682 | FP | FP | STRCPY 的目标缓冲区 `buf` 的大小已通过 `alloc(Columns + 1)` 或 `alloc(Columns * MB_MAXBYTES + 1)` 分配，其大小与屏幕列数相关，而源字符串 `transchar_b... |
| 1067 | vim-9.1.1330 | debuggy_find | cpp/unbounded-write | 1067 | FP | FP | 代码中 `STRCPY` 的目标缓冲区 `name` 的大小通过 `alloc(STRLEN(fname) + 3)` 分配，其长度足以容纳源字符串 `fname` 加上额外的前缀，因此不存在缓冲区溢出风险。 |
| 1068 | vim-9.1.1330 | has_profiling | cpp/unbounded-write | 973 | FP | FP | STRCPY的目标缓冲区pe->pen_name的大小为STRLEN(fname) + 1，与源字符串fname的长度完全匹配，且分配了足够空间，因此不会发生缓冲区溢出。 |
| 1069 | vim-9.1.1330 | ex_diffpatch | cpp/unbounded-write | 1390 | FP | FP | 告警指出的strcpy调用目标缓冲区buf是通过alloc(buflen)分配的，其中buflen已通过STRLEN(tmp_orig) + STRLEN(esc_name) + STRLEN(tmp_new) + 16计算，确保有足... |
| 1070 | vim-9.1.1330 | do_string_sub | cpp/unbounded-write | 8014 | FP | FP | 告警点位于 `STRCPY((char *)ga.ga_data + ga.ga_len, tail);`，但切片代码显示，在调用 `STRCPY` 之前，已通过 `ga_grow(&ga, ...)` 确保了目标缓冲区 `ga.ga... |
| 1071 | vim-9.1.1330 | set_var_const | cpp/unbounded-write | 4271 | FP | FP | STRCPY宏的目标缓冲区di->di_key的大小已通过alloc分配，其大小为varname长度加1，确保了缓冲区足够容纳源字符串，因此不会发生溢出。 |
| 1073 | vim-9.1.1330 | ex_substitute | cpp/unbounded-write | 4883 | FP | FP | 告警指出的 `STRCAT` 宏调用位于一个条件分支内，该分支仅在 `new_start != NULL` 时执行。切片代码显示 `new_start` 是通过 `alloc_clear` 分配的缓冲区，其大小 `new_start_... |
| 1074 | vim-9.1.1330 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区分配了精确的长度，该长度已通过计算确保能容纳源字符串cmd及所有附加内容，因此不存在缓冲区溢出的风险。 |
| 1075 | vim-9.1.1330 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 代码在调用STRCAT前，已通过alloc(len)为目标缓冲区分配了精确计算的长度len，该长度已包含所有待拼接字符串的长度和终止符，因此不会发生缓冲区溢出。 |
| 1076 | vim-9.1.1330 | ex_sort | cpp/unbounded-write | 605 | FP | FP | 代码中 `STRCPY(sortbuf1, s)` 的目标缓冲区 `sortbuf1` 已通过 `alloc(maxlen + 1)` 分配，其大小 `maxlen + 1` 是根据待处理行的最大长度 `maxlen` 计算得出的，且... |
| 1077 | vim-9.1.1330 | expand_sfile | cpp/unbounded-write | 10101 | FP | FP | 代码中已为目标缓冲区`newres`分配了`resultlen + 1`的空间，而`STRCPY`复制的字符串`repl`长度`repllen`已通过`resultlen += repllen - srclen`计算并包含在总长度内，... |
| 1079 | vim-9.1.1330 | repl_cmdline | cpp/unbounded-write | 5317 | FP | FP | 代码中`new_cmdline`缓冲区的大小`i`已通过计算`(src - *cmdlinep) + repllen + taillen + 3`并加上`eap->nextcmd`的长度来精确分配，随后使用`STRCPY`（即`str... |
| 1082 | vim-9.1.1330 | do_one_cmd | cpp/unbounded-write | 2678 | FP | FP | 告警指向的STRCPY宏在切片中用于将错误消息复制到固定大小的IObuff缓冲区，但切片显示errormsg来源为静态字符串字面量或已受控的格式化输出（如ex_errmsg），其长度有限且已知，不会导致缓冲区溢出。 |
| 1083 | vim-9.1.1330 | discard_exception | cpp/unbounded-write | 646 | FP | FP | STRCPY(IObuff, saved_IObuff) 的源字符串 saved_IObuff 来自 vim_strsave(IObuff)，而 vim_strsave 会为目标分配足够空间并复制原始 IObuff 的内容，因此源字符... |
| 1084 | vim-9.1.1330 | get_exception_string | cpp/unbounded-write | 473 | FP | FP | 目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度足以容纳源字符串 `mesg` 或 `p` 加上固定的前缀，且源字符串长度在分配时已通过 `STRLEN` 计算，因此 `strcat` 不会导致缓... |
| 1087 | vim-9.1.1330 | cmdline_browse_history | cpp/unbounded-write | 1498 | FP | FP | 代码中在调用STRCPY（即strcpy）前，已通过alloc_cmdbuff((int)plen)为目标缓冲区ccline.cmdbuff分配了足够容纳源字符串p（长度为plen）的空间，并进行了空指针检查，因此不存在缓冲区溢出风险。 |
| 1089 | vim-9.1.1330 | vim_settempdir | cpp/unbounded-write | 5289 | FP | FP | 告警点位于 `STRCPY(buf, tempdir);`，但切片显示 `buf` 已通过 `alloc(MAXPATHL + 2)` 分配了固定大小的缓冲区（MAXPATHL + 2），且 `tempdir` 参数是调用方传入的，其... |
| 1090 | vim-9.1.1330 | vim_rename | cpp/unbounded-write | 3861 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。 |
| 1091 | vim-9.1.1330 | buf_modname | cpp/unbounded-write | 3639 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区retval通过alloc分配了足够的内存，其大小为fnamelen + extlen + 3，其中fnamelen是源字符串fname的长度。由于分配的大小包含了源字符串长度... |
| 1092 | vim-9.1.1330 | addfile | cpp/unbounded-write | 4219 | FP | FP | 代码中目标缓冲区 `p` 的大小通过 `alloc(STRLEN(f) + 1 + isdir)` 动态分配，其长度等于源字符串 `f` 的长度加1（以及可能的目录分隔符），因此 `STRCPY(p, f)` 不会发生缓冲区溢出。 |
| 1093 | vim-9.1.1330 | concat_fnames | cpp/unbounded-write | 3134 | FP | FP | 代码通过alloc为目标缓冲区分配了足够的空间，其大小为STRLEN(fname1) + STRLEN(fname2) + 3，确保了strcpy操作不会发生缓冲区溢出。 |
| 1094 | vim-9.1.1330 | concat_fnames | cpp/unbounded-write | 3137 | FP | FP | 函数通过alloc为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcat操作不会导致缓冲区溢出。 |
| 1095 | vim-9.1.1330 | uniquefy_paths | cpp/unbounded-write | 2569 | FP | FP | STRCPY的目标缓冲区`file_pattern`是通过`alloc(len + 2)`分配的，其大小明确为`pattern`长度加2，而源字符串`pattern`的长度已通过`STRLEN(pattern)`获取，因此拷贝操作不会... |
| 1096 | vim-9.1.1330 | find_file_in_path_option | cpp/unbounded-write | 1912 | FP | FP | STRCPY 的目标缓冲区 NameBuff 大小为 MAXPATHL，而源字符串 *file_to_find 的长度 file_to_findlen 在之前已通过 STRLEN(NameBuff) 获取，且 NameBuff 正是由... |
| 1097 | vim-9.1.1330 | ff_check_visited | cpp/unbounded-write | 1537 | FP | FP | STRCPY的目标缓冲区vp->ffv_fname的大小为ff_expand_buffer.length + 1，而源字符串ff_expand_buffer.string的长度已通过ff_expand_buffer.length记录，... |
| 1098 | vim-9.1.1330 | <global> | cpp/unbounded-write | 3794 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够大小的缓冲区，其大小计算包含了源字符串s的长度，因此不会发生缓冲区溢出。 |
| 1099 | vim-9.1.1330 | foldDelMarker | cpp/unbounded-write | 1897 | FP | FP | 代码中 `STRCPY` 的目标缓冲区 `newline` 是通过 `alloc(ml_get_len(lnum) - len + 1)` 分配的，其大小精确计算为源行长度减去标记长度再加1（用于空终止符），确保了缓冲区足以容纳复制后... |
| 1100 | vim-9.1.1330 | foldAddMarker | cpp/unbounded-write | 1815 | FP | FP | 代码中目标缓冲区 `newline` 的大小通过 `alloc(line_len + markerlen + STRLEN(cms) + 1)` 动态分配，其大小足以容纳源字符串 `line` 和 `cms` 的拼接，且分配大小包含了... |
| 1101 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2899 | FP | FP | 告警点 `STRCPY(buffer, res_prolog->title);` 中，`buffer` 是大小为256的局部数组，`res_prolog->title` 来源于外部资源文件，其内容在 `prt_open_resourc... |
| 1102 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2901 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_prolog->title`和`res_prolog->version`均来自受控的PostScript资源文件，其内容在`prt_open_resource`函数中经过解析和长... |
| 1103 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2905 | FP | FP | 目标缓冲区 `buffer` 在函数开头定义为 `char buffer[256];`，而源字符串 `res_cidfont->title` 是从受控的资源文件中读取的，其长度在 `prt_open_resource` 函数中通过 `... |
| 1104 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_cidfont->title`和`res_cidfont->version`均来自受控的PostScript资源文件，其内容长度在`prt_open_resource`函数中通过... |
| 1105 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 告警点 `STRCPY(buffer, res_cmap->title);` 中，`res_cmap->title` 来源于外部资源文件，但切片代码显示 `prt_open_resource` 函数已通过 `vim_strncpy` ... |
| 1106 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 切片代码显示，`buffer` 数组大小为256字节，而 `STRCAT` 操作拼接的是 `res_cmap->title` 和 `res_cmap->version`，这些字符串来自受控的PostScript资源文件，其长度在 `p... |
| 1107 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2920 | FP | FP | 告警点 `STRCPY(buffer, res_encoding->title);` 中，`buffer` 是大小为256的局部数组，而 `res_encoding->title` 来源于外部资源文件，其长度在 `prt_open_r... |
| 1108 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2922 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_encoding->title`和`res_encoding->version`均来自受控的资源文件解析，其长度在`prt_open_resource`函数中通过`vim_str... |
| 1109 | vim-9.1.1330 | prt_resource_name | cpp/unbounded-write | 1659 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过`if (STRLEN(filename) >= MAXPATHL)`检查了源字符串长度，若长度超过或等于MAXPATHL，则会将目标字符串置空，否则才执行拷贝。这提供了长度... |
| 1110 | vim-9.1.1330 | do_helptags | cpp/unbounded-write | 1210 | FP | FP | STRCPY 宏的目标缓冲区 NameBuff 在代码中未显示其大小，但根据其名称和常见用法推断，它很可能是一个足够大的全局缓冲区（如 MAXPATHL），用于存储文件路径。告警点是将已知的目录名复制到该缓冲区，源字符串 `dirna... |
| 1111 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 975 | FP | FP | NameBuff 是一个全局缓冲区，其大小定义为 MAXPATHL（通常为 260 或更大），而拼接的字符串由固定格式的目录路径、通配符和扩展名组成，长度受限于文件系统路径的最大长度，不会超过缓冲区边界。 |
| 1112 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 991 | FP | FP | NameBuff 是一个全局缓冲区，其大小定义为 MAXPATHL（通常为 260 或更大），而 tagfname 参数来自调用方，其长度在合理的系统路径范围内，不足以导致缓冲区溢出。 |
| 1114 | vim-9.1.1330 | highlight_set_startstop_termcode | cpp/unbounded-write | 1485 | FP | FP | 代码在调用STRCAT前已通过`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查确保缓冲区`buf`（大小为100）不会溢出，存在明确的安全防护。 |
| 1117 | vim-9.1.1330 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...），并分配了相应大小的内存（buf = alloc(amt)），确保了目标缓冲区大小足够，不会发生溢出。 |
| 1118 | vim-9.1.1330 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...），并分配了对应大小的内存（buf = alloc(amt)），因此不会发生缓冲区溢出。 |
| 1119 | vim-9.1.1330 | <global> | cpp/unbounded-write | 1456 | FP | FP | 目标缓冲区 csinfo[i].fname 的大小通过 alloc(strlen(fname)+1) 精确分配，与源字符串 fname 的长度匹配，strcpy 操作不会导致缓冲区溢出。 |
| 1121 | vim-9.1.1330 | cs_add_common | cpp/unbounded-write | 604 | FP | FP | 告警点处的sprintf使用fname和常量字符串CSCOPE_DBFILE拼接，其中fname的长度已通过while循环去除尾部斜杠，且其初始分配大小为MAXPATHL+1，并经过expand_env处理，长度受MAXPATHL限制... |
| 1122 | vim-9.1.1330 | ins_compl_infercase_gettext | cpp/unbounded-write | 688 | FP | FP | STRCPY宏展开为strcpy，其源字符串IObuff和目标缓冲区gap.ga_data均受控于内部逻辑。目标缓冲区已通过ga_grow(&gap, IOSIZE)确保有足够空间（IOSIZE字节），且源字符串IObuff的大小受I... |
| 1123 | vim-9.1.1330 | <global> | cpp/unbounded-write | 3129 | FP | FP | 切片代码显示，在`sprintf`调用前存在对`to`变量的明确赋值检查（`to = NUL`），且`sprintf`仅在`to == NUL`这一特定、受控的分支内执行，其格式化字符串和参数`transchar(from)`均源自内... |
| 1124 | vim-9.1.1330 | findswapname | cpp/unbounded-write | 4967 | FP | FP | STRCPY 的目标缓冲区 fname2 的大小为 n+2，源缓冲区 fname 的大小为 n，且 STRCPY 调用前已确保 fname2 非空，因此复制操作不会导致缓冲区溢出。 |
| 1125 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2157 | FP | FP | 代码通过alloc(STRLEN(f) + 1)为目标缓冲区s分配了精确长度，确保其大小足以容纳源字符串f及其终止空字符，因此strcpy操作不会导致缓冲区溢出。 |
| 1126 | vim-9.1.1330 | <global> | cpp/unbounded-write | 811 | FP | FP | 代码中使用了宏 `STRCPY`，其定义为 `strcpy`，但目标缓冲区 `menu->strings[i]` 的大小是通过 `alloc(STRLEN(call_data) + 5)` 分配的，长度已考虑了源字符串长度并额外增加了... |
| 1127 | vim-9.1.1330 | <global> | cpp/unbounded-write | 815 | FP | FP | 代码中使用了宏 `STRCPY`，其定义为 `strcpy`，但告警点位于 `menu->strings[i]` 的赋值处，该内存是通过 `alloc(STRLEN(call_data) + 5)` 分配的，大小为源字符串长度加5，足... |
| 1128 | vim-9.1.1330 | msg_show_console_dialog | cpp/unbounded-write | 4502 | FP | FP | 告警点 `STRCPY(confirm_msg + 1, message)` 中，目标缓冲区 `confirm_msg` 的大小 `len` 已通过计算 `STRLEN(message) + ...` 确定并分配，源字符串 `mess... |
| 1129 | vim-9.1.1330 | str2specialbuf | cpp/unbounded-write | 2017 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过条件`(int)(STRLEN(s) + STRLEN(buf)) < len`检查了目标缓冲区`buf`的剩余空间，确保拼接后不会溢出。该防护机制使得告警的缓冲区溢出风险... |
| 1130 | vim-9.1.1330 | get_emsg_source | cpp/unbounded-write | 502 | FP | FP | 代码在调用sprintf前，已通过alloc(STRLEN(sname) + STRLEN(p))为目标缓冲区分配了足够的空间，该空间大小等于两个字符串长度之和，足以容纳格式化后的完整字符串，因此不存在缓冲区溢出风险。 |
| 1131 | vim-9.1.1330 | may_trigger_modechanged | cpp/unbounded-write | 2836 | FP | FP | STRCPY 的目标缓冲区 `last_mode` 和源缓冲区 `curr_mode` 大小均为 `MODE_MAX_LENGTH`，且 `get_mode` 函数确保写入的字符数不会超过该长度，因此不存在缓冲区溢出风险。 |
| 1132 | vim-9.1.1330 | expand_env_esc | cpp/unbounded-write | 1647 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过条件`(STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen)`检查了目标缓冲区`dst`的剩余空间，确保不会发生缓冲区溢出。 |
| 1133 | vim-9.1.1330 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 切片代码中，STRCAT宏被用于拼接字符串，但目标缓冲区`newline`是通过`alloc(ml_get_len(lnum) + len + 1)`分配的，其大小等于原行长加上插入文本长度再加1，足以容纳拼接后的字符串，因此不会发生... |
| 1135 | vim-9.1.1330 | push_showcmd | cpp/unbounded-write | 1809 | FP | FP | 切片代码显示，STRCPY宏用于将`showcmd_buf`的内容复制到`old_showcmd_buf`，这是程序内部缓冲区之间的复制，源数据来自程序内部状态而非外部不可控输入。根据常见实现，此类缓冲区通常具有固定且匹配的大小，不存... |
| 1136 | vim-9.1.1330 | add_to_showcmd | cpp/unbounded-write | 1764 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已通过计算`old_len`和`extra_len`检查了缓冲区`showcmd_buf`的剩余空间，并通过`mch_memmove`移动数据来确保拼接后不会溢出`SHOWCMD_... |
| 1137 | vim-9.1.1330 | op_change | cpp/unbounded-write | 2003 | FP | FP | 切片代码中STRCPY宏的目标缓冲区newp是通过alloc分配的大小为(ml_get_len(linenr) + vpos.coladd + ins_len + 1)的缓冲区，且源字符串oldp + bd.textcol的长度不会超... |
| 1138 | vim-9.1.1330 | op_replace | cpp/unbounded-write | 1299 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区newp是通过alloc(oldlen + 1 + n)分配的，其大小明确为oldlen + 1 + n。而源字符串oldp + bd.textcol + bd.textlen的长度不会超过old... |
| 1139 | vim-9.1.1330 | op_replace | cpp/unbounded-write | 1308 | FP | FP | 代码中STRCPY宏的目标缓冲区`after_p`是通过`alloc(oldlen + 1 + n - newlen)`分配的，其大小`oldlen + 1 + n - newlen`明确大于或等于源字符串`oldp + bd.tex... |
| 1140 | vim-9.1.1330 | op_delete | cpp/unbounded-write | 962 | FP | FP | 代码中STRCPY宏的调用目标缓冲区`newp`已通过`alloc(ml_get_len(lnum) + 1 - n)`分配了精确大小，源字符串`oldp + bd.textcol + bd.textlen`是已知行内子串，不会导致缓... |
| 1141 | vim-9.1.1330 | block_insert | cpp/unbounded-write | 743 | FP | FP | STRCPY 的目标缓冲区 newp 是通过 alloc 分配的，其大小为 ml_get_len(lnum) + spaces + slen + ...，而源字符串 oldp 来自 ml_get(lnum)，其长度不超过 ml_get... |
| 1142 | vim-9.1.1330 | option_value2string | cpp/unbounded-write | 8372 | FP | FP | 告警点调用的STRCPY宏目标缓冲区是NameBuff，但切片中未提供其大小定义，无法判断是否存在缓冲区溢出风险。同时，告警涉及的多个数据源（如get_special_key_name）其内部缓冲区大小（MAX_KEY_NAME_LE... |
| 1143 | vim-9.1.1330 | option_value2string | cpp/unbounded-write | 8374 | FP | FP | 目标缓冲区 NameBuff 的大小未在切片中明确给出，但告警点位于处理数值选项（P_NUM）的分支，该分支通过 wc_use_keyname 和 transchar 等函数处理有限范围的整数值，这些值不可能导致 strcpy 溢出。... |
| 1144 | vim-9.1.1330 | stropt_expand_envvar | cpp/unbounded-write | 1803 | FP | FP | 目标缓冲区 `newval` 的大小 `newlen` 是根据源字符串 `s` 的长度精确计算并分配的，`STRCPY` 操作不会导致缓冲区溢出。 |
| 1145 | vim-9.1.1330 | mch_expand_wildcards | cpp/unbounded-write | 7371 | FP | FP | 代码中 `STRCPY(p, (*file)[i])` 的目标缓冲区 `p` 已通过 `alloc(STRLEN((*file)[i]) + 1 + dir)` 分配了足够的空间，其大小等于源字符串长度加1（以及可能的目录分隔符），因... |
| 1146 | vim-9.1.1330 | mch_FullName | cpp/unbounded-write | 2829 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过条件`(int)(buflen + STRLEN(fname)) >= len`检查了目标缓冲区`buf`的剩余空间是否足以容纳源字符串`fname`，确保了不会发生缓冲区溢出。 |
| 1147 | vim-9.1.1330 | qf_store_title | cpp/unbounded-write | 1940 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc_id为目的地缓冲区分配了足够的空间，其大小为源字符串长度加2，因此不会发生缓冲区溢出。 |
| 1148 | vim-9.1.1330 | reg_submatch | cpp/unbounded-write | 2723 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区retval分配了精确的长度len，该长度是根据匹配的起止位置计算得出的，足以容纳待拷贝的字符串。因此，不存在缓冲区溢出的风险。 |
| 1150 | vim-9.1.1330 | regtilde | cpp/unbounded-write | 1959 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`tmpsublen > MAXCOL`检查确保目标缓冲区大小不会超过MAXCOL，并且`tmpsub`是通过`alloc(tmpsublen + 1)`分配，大小为`tmpsubl... |
| 1151 | vim-9.1.1330 | match_with_backref | cpp/unbounded-write | 1600 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区reg_tofree分配了足够的内存，且len的计算基于源字符串rex.line的长度并增加了额外空间，因此不会发生缓冲区溢出。 |
| 1152 | vim-9.1.1330 | get_reg_contents | cpp/unbounded-write | 2741 | FP | FP | 代码中目标缓冲区 `retval` 的大小已通过累加所有源字符串长度精确计算（`len`），并在分配时预留了空字符位置（`alloc(len + 1)`）。STRCPY 宏每次写入的目标地址 `retval + len` 也经过计算，... |
| 1153 | vim-9.1.1330 | do_put | cpp/unbounded-write | 2164 | FP | FP | 切片代码中使用了宏STRCPY，其定义为strcpy，但目标缓冲区newp是通过alloc分配的内存，其大小为(ml_get_len(lnum) - col + totlen + 1)，其中totlen为源字符串y_array[y_s... |
| 1154 | vim-9.1.1330 | do_put | cpp/unbounded-write | 2165 | FP | FP | 切片代码中未发现对STRCPY宏的直接调用，告警消息中提到的所有strcpy调用均未在切片中体现，无法基于现有代码判断是否存在缓冲区溢出风险。 |
| 1155 | vim-9.1.1330 | op_yank | cpp/unbounded-write | 1317 | FP | FP | 代码中STRCPY宏的目标缓冲区pnew是通过alloc函数分配的内存，其大小已精确计算为两个字符串长度之和加1，确保了缓冲区足够容纳拼接后的字符串，因此不存在缓冲区溢出风险。 |
| 1156 | vim-9.1.1330 | op_yank | cpp/unbounded-write | 1318 | FP | FP | 代码中STRCPY宏的目标缓冲区pnew是通过alloc函数分配的内存，其大小为两个字符串长度之和加1，已确保缓冲区足够容纳拼接后的字符串，不存在缓冲区溢出风险。 |
| 1157 | vim-9.1.1330 | stuff_yank | cpp/unbounded-write | 470 | FP | FP | STRCPY的目标缓冲区tmp是通过alloc(tmplen + 1)分配的，其大小tmplen + 1等于源字符串pp->string的长度加上plen再加1，这确保了缓冲区足以容纳拼接后的字符串和终止符，因此不会发生溢出。 |
| 1158 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2838 | FP | FP | 目标缓冲区 `scriptname` 的大小通过 `alloc(STRLEN(name) + 14)` 精确分配，其长度足以容纳固定前缀 "autoload/"、处理后的 `name` 字符串以及后缀 ".vim"，因此 `STRCA... |
| 1161 | vim-9.1.1330 | dump_word | cpp/unbounded-write | 4187 | FP | FP | STRCPY的目标缓冲区badword大小为MAXWLEN+10，源p来自word或cword，而cword和word的最大长度受MAXWLEN限制，且切片中未显示p的长度超过目标缓冲区。因此，该strcpy操作是安全的，不会发生缓冲... |
| 1162 | vim-9.1.1330 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 告警点位于 `make_case_word` 函数中，该函数仅在特定条件下（`flags` 不满足 `WF_ALLCAP` 或 `WF_ONECAP`）才会执行 `STRCPY`。切片代码显示，调用 `onecap_copy` 和 `... |
| 1163 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2998 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区p分配了足够的内存（ml_get_curline_len() + addlen + 1），且复制的源字符串repl_to的长度repl_to_len已知，目标缓冲区大小明确大于... |
| 1164 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2999 | FP | FP | 代码在调用STRCAT前，已为目标缓冲区p分配了精确的大小（ml_get_curline_len() + addlen + 1），其中addlen已考虑了替换字符串的长度差，且STRCAT拼接的源字符串长度（line + curwin... |
| 1165 | vim-9.1.1330 | count_common_word | cpp/unbounded-write | 1919 | FP | FP | STRCPY的目标缓冲区wc->wc_word的大小为STRLEN(p) + 1，是通过alloc精确分配的，与源字符串p的长度完全匹配，因此不会发生缓冲区溢出。 |
| 1166 | vim-9.1.1330 | spell_load_lang | cpp/unbounded-write | 1632 | FP | FP | 告警点 `STRCPY(sl.sl_lang, lang)` 中，目标缓冲区 `sl.sl_lang` 的大小未在切片中明确给出，但源 `lang` 是函数参数，其长度受调用方控制。结合告警描述，工具主要担忧来自环境变量等外部输入，但... |
| 1167 | vim-9.1.1330 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 代码中在调用 STRCPY（即 strcpy）前，已通过 alloc(buflen) 为 buf 分配了足够大的缓冲区，其大小 buflen 被设置为 len + MAXWLEN + 2，其中 len 是当前行的长度。由于 STRCP... |
| 1168 | vim-9.1.1330 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数 getroom 已根据输入字符串长度 s 分配了 STRLEN(s) + 1 字节的内存，STRCPY 的目标缓冲区 sc 大小与源字符串 s 完全匹配，不存在缓冲区溢出风险。 |
| 1169 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 代码中使用了STRCAT宏，但目标缓冲区p是通过getroom()分配的，其大小已根据源字符串长度计算并预留了足够空间（包括分隔符和终止符），因此不会发生缓冲区溢出。 |
| 1170 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 代码中STRCAT的目标缓冲区p是通过getroom()分配的，其大小计算为已有信息长度加上items[0]和items[1]的长度再加3，这确保了缓冲区足够容纳拼接后的字符串，不会发生溢出。 |
| 1171 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2464 | FP | FP | 代码中STRCPY的目标缓冲区p是通过getroom(spin, STRLEN(items[1]) + 2, FALSE)分配的，其大小明确为源字符串长度加2，足以容纳源字符串和追加的'+'字符，因此不会发生缓冲区溢出。 |
| 1172 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 代码中STRCAT的目标缓冲区p是通过getroom(spin, l, FALSE)动态分配的，其大小l已计算为足以容纳源字符串compflags和items[1]加上分隔符'/\0'，因此不会发生缓冲区溢出。 |
| 1173 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 代码中使用了安全的字符串复制宏STRCPY，该宏内部调用标准库的strcpy，但告警点STRCPY(p, spin->si_info)的目标缓冲区p是通过getroom(spin, ...)动态分配的，其大小已根据源字符串长度精确计算... |
| 1174 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2746 | FP | FP | sprintf 的目标缓冲区 buf 大小为 MAXLINELEN（定义为 1024），而源字符串 items[4] 来自受控的 affix 文件行解析，其长度受限于行缓冲区 rline（大小也为 MAXLINELEN）。由于 ite... |
| 1175 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2748 | FP | FP | 切片代码中，sprintf的目标缓冲区buf大小为MAXLINELEN（定义为256），而源字符串items[4]来自受控的affix文件行解析，其长度受MAXLINELEN限制，且拼接模式（如'^%s'或'%s$'）仅增加2个字符，... |
| 1176 | vim-9.1.1330 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | 代码中 `STRCPY(sft->sft_word, goodword)` 的目标缓冲区 `sft->sft_word` 的大小为 `STRLEN(goodword) + 1`，这是通过 `alloc(offsetof(sftword... |
| 1177 | vim-9.1.1330 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY 宏的目标缓冲区 fword 被定义为固定大小的数组 char_u fword[MAXWLEN]，且告警行 STRCPY(fword, su->su_fbadword) 的源 su->su_fbadword 是拼写建议算法... |
| 1178 | vim-9.1.1330 | concat_str | cpp/unbounded-write | 792 | FP | FP | 函数内通过alloc为目标缓冲区分配了精确大小（str1长度+str2长度+1），且STRCPY宏展开为strcpy，其源字符串长度已通过STRLEN计算并包含在分配大小内，因此不会发生缓冲区溢出。 |
| 1179 | vim-9.1.1330 | concat_str | cpp/unbounded-write | 794 | FP | FP | 函数 `concat_str` 通过 `alloc` 为目标缓冲区 `dest` 分配了精确的、足够容纳两个源字符串及其终止符的空间，随后才调用 `STRCPY`（即 `strcpy`）。`strcpy` 的目标地址 `dest + ... |
| 1180 | vim-9.1.1330 | expand_tag_fname | cpp/unbounded-write | 4129 | FP | FP | 代码在调用STRCPY前，已通过alloc(MAXPATHL)为目标缓冲区分配了固定大小MAXPATHL，且后续的vim_strncpy调用也明确限制了拷贝长度，确保了不会发生缓冲区溢出。 |
| 1181 | vim-9.1.1330 | get_tagfname | cpp/unbounded-write | 3435 | FP | FP | 告警点 `STRCPY(buf, fname);` 中，`fname` 来源于 `vim_findfile` 函数，该函数内部使用 `alloc(MAXPATHL)` 分配缓冲区并确保路径长度不超过 `MAXPATHL`，且 `buf... |
| 1182 | vim-9.1.1330 | findtags_add_match | cpp/unbounded-write | 2624 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`p`和`p + len + 1`均通过`alloc`分配了足够大小（`len + 10 + ML_EXTRA + 1`），且源字符串`st->help_lang`和`tagpp->tagname... |
| 1184 | vim-9.1.1330 | show_one_termcode | cpp/unbounded-write | 7050 | FP | FP | STRCPY的目标缓冲区IObuff+5有足够的空间，因为IObuff是一个大数组（在切片外定义），且源字符串p来自get_special_key_name，其内部缓冲区string的大小为MAX_KEY_NAME_LEN+1，而复制... |
| 1185 | vim-9.1.1330 | current_tagblock | cpp/unbounded-write | 1392 | FP | FP | 代码使用 sprintf 格式化字符串时，长度参数 `len` 来源于当前光标位置的标签名长度，该长度受限于当前行的缓冲区内容，且分配的目标缓冲区大小（`len + 39`）已明确考虑了源字符串长度和固定后缀，因此不会发生缓冲区溢出。 |
| 1186 | vim-9.1.1330 | uc_check_code | cpp/unbounded-write | 1782 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过STRLEN计算了源字符串长度，且目标缓冲区buf的大小由调用方控制，但告警点所在的case 0分支中，buf的使用前有非空检查，且上下文表明buf的分配大小可能已考虑了结果... |
| 1187 | vim-9.1.1330 | fname_trans_sid | cpp/unbounded-write | 2259 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过条件`fnamelen < FLEN_FIXED`确保目标缓冲区`fname_buf`（大小为FLEN_FIXED）足以容纳拼接后的字符串，因此不存在缓冲区溢出风险。 |
| 1188 | vim-9.1.1330 | alloc_ufunc | cpp/unbounded-write | 728 | FP | FP | 代码通过 `alloc_clear` 分配了足够的内存，其大小 `len` 已明确包含了目标缓冲区 `uf_name` 的长度 `namelen + 1`，确保了 `strcpy` 的目标缓冲区大小不小于源字符串长度，因此不存在缓冲区... |
| 1189 | vim-9.1.1330 | exec_instructions | cpp/unbounded-write | 3896 | FP | FP | 切片代码中显示的 STRCPY 宏调用位于 ISN_EXECCONCAT 指令处理中，该代码在复制前已通过两轮遍历计算了总长度并分配了足够缓冲区（cmd = alloc(len + 1)），因此不会发生缓冲区溢出。 |
| 1190 | vim-9.1.1330 | generate_PUSHFUNC | cpp/unbounded-write | 1041 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(STRLEN(name) + 3)为目标缓冲区分配了精确长度，确保缓冲区大小足以容纳源字符串'g:'前缀和name内容，因此不存在缓冲区溢出风险。 |
| 1191 | vim-9.1.1330 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | FP | STRCPY宏的目标缓冲区newsav->sav_key的大小是精确分配的，大小为offsetof(sallvar_T, sav_key) + STRLEN(name) + 1，足以容纳源字符串name及其终止空字符，因此不会发生缓冲... |
| 1192 | vim-9.1.1330 | find_exported | cpp/unbounded-write | 756 | FP | FP | 代码在调用sprintf前已通过动态分配确保了目标缓冲区大小足够：当len >= sizeof(buffer)时，会分配len字节的内存，因此不会发生缓冲区溢出。 |
| 1193 | vim-9.1.1330 | find_exported | cpp/unbounded-write | 763 | FP | FP | 代码在调用sprintf前已通过动态分配确保目标缓冲区大小足够：当len >= sizeof(buffer)时，会分配len字节的内存，因此sprintf不会发生缓冲区溢出。 |
| 1194 | vim-9.1.1330 | xxdline | cpp/unbounded-write | 537 | FP | FP | 目标缓冲区 'z' 是静态数组，大小为 LLEN+1，而源 'l' 是同一函数中先前由 fgets 读取的行，其长度受限于相同的 LLEN 缓冲区，因此 strcpy 操作不会导致溢出。 |
| 1195 | vim-9.1.1330 | ExpandBufnames | cpp/invalid-pointer-deref | 2971 | FP | FP | 告警行 `(*file)[count++] = p;` 仅在 `*file` 已成功分配内存后执行，而切片代码显示在 `round == 1` 时，若 `*file == NULL` 会提前返回 `FAIL`，因此写入前 `*file... |
| 1196 | vim-9.1.1330 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | FP | 切片代码显示，在写入 `p[pos.col + 1]` 之前，已通过条件 `if (width == 2)` 确保 `pos.col + 1` 小于分配的数组长度 `len`，因为 `width` 为2表示双宽度字符，且内层循环的终止... |
| 1197 | vim-9.1.0790 | <global> | cpp/redundant-null-check-simple | 3502 | FP | FP | 告警指出的空指针检查是冗余的，因为指针 `inc_opt` 在解引用前已通过 `if (*inc_opt != NUL)` 进行了非空验证，且 `inc_opt` 被赋值为 `p_inc` 或 `curbuf->b_p_inc`，这些... |
| 1198 | vim-9.1.0790 | <global> | cpp/redundant-null-check-simple | 3584 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 指针在解引用前已通过 `if (*inc_opt != NUL)` 进行了有效性检查，该检查确保了指针非空，因此后续的 `strstr((c... |
| 1199 | vim-9.1.0790 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | FP | FP | 告警点位于条件分支 `else if (linep[pos.col - 1] == '/' && linep[pos.col] == '*'` 中，对 `pos.col` 的访问前存在明确的边界检查 `if (pos.col == 0... |
| 1200 | vim-9.1.0790 | common_function | cpp/inconsistent-null-check | 4876 | FP | FP | 代码在调用 `vim_strsave(s)` 后，将返回值赋给 `name` 变量，后续逻辑（如 `vim_free(name)`）会直接使用该变量，并未检查其是否为 NULL。然而，`s` 的来源（如 `tv_get_string`... |
| 1201 | vim-9.1.0790 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | FP | 函数 `vterm_screen_is_eol` 的循环条件 `pos.col < screen->cols` 以及 `getcell` 函数内部的边界检查 `col >= screen->cols` 确保了在调用 `getcell`... |
| 1202 | vim-9.1.0790 | get_isolated_shell_name | cpp/inconsistent-null-check | 2695 | FP | FP | 函数 `get_isolated_shell_name` 的返回值 `p` 被直接返回给调用者，调用者负责检查其是否为 NULL。切片中未显示调用者对返回值的处理，但告警规则仅基于 `vim_strsave` 的调用模式统计，并未证明... |
| 1203 | vim-9.1.0790 | get_isolated_shell_name | cpp/inconsistent-null-check | 2706 | FP | FP | 函数 `vim_strnsave` 的返回值 `p` 被直接返回给调用者，调用者负责检查其是否为 NULL。告警规则要求函数内部检查，但此函数的设计意图是返回分配的内存，由调用者处理分配失败，这是合理的资源管理方式，并非安全漏洞。 |
| 1204 | vim-9.1.0790 | did_set_cryptmethod | cpp/inconsistent-null-check | 1821 | FP | FP | 函数 `vim_strsave` 的返回值被赋值给全局变量 `p_cm`，该变量在后续代码中仅用于字符串比较（`STRCMP`）和作为参数传递，没有进行解引用或可能导致崩溃的操作。即使返回 NULL，代码逻辑也能安全处理，不会导致程序异常。 |
| 1205 | vim-9.1.0790 | did_set_background | cpp/inconsistent-null-check | 1082 | FP | FP | 告警点 `p_bg = vim_strsave(...)` 的返回值被直接赋值给 `p_bg`，而 `p_bg` 在下一行立即作为参数传递给 `check_string_option(&p_bg)`。`check_string_opt... |
| 1206 | vim-9.1.0790 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 代码在调用 find_win_by_nr_or_id 后，立即使用 win_valid_any_tab 检查了返回的窗口指针的有效性，并在无效时回退到 curwin。这构成了有效的空值检查和安全处理，因此告警为误报。 |
| 1207 | vim-9.1.0790 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 告警指出的`regnext`调用未检查null，但切片代码显示其返回值`next`在后续代码中仅作为参数传递给`OP(next)`等宏或函数，这些宏/函数（如`OP`）内部已处理NULL指针（例如`regnext`函数本身在输入为NU... |
| 1208 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 代码中 `regnode` 的返回值 `br` 被立即用于条件判断 `if (ret == NULL)` 和后续的 `regtail` 调用，其值被直接使用而非解引用，且 `regnode` 函数在 `regcode` 不为 `JUS... |
| 1209 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 代码中 `regnode` 的返回值 `br` 被用于 `regtail` 调用，而 `regtail` 函数内部会检查其参数是否为 `JUST_CALC_SIZE` 或 `reg_toolong` 为真，若满足条件则直接返回而不使用... |
| 1210 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在切片代码中，`regnext` 的返回值 `br` 被直接用于循环条件 `br != lastnode`，这是一个指针比较，空指针（NULL）与 `lastnode` 不相等，循环会正常终止，不会导致空指针解引用。代码逻辑安全，告警... |
| 1211 | vim-9.1.0790 | win_redr_custom | cpp/inconsistent-null-check | 1115 | FP | FP | 代码在调用 vim_strsave 后，立即将返回值传递给 vim_free 进行释放，虽然未显式检查 NULL，但 vim_free 内部已处理 NULL 指针（if (x != NULL && !really_exiting)），... |
| 1212 | vim-9.1.0790 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 告警点位于条件分支 `if (spin->si_first_free == NULL)` 内，当条件为真时，`getroom` 的返回值被直接赋值给 `n`。后续代码在 `#ifdef SPELL_PRINTTREE` 块中检查了 `... |
| 1213 | vim-9.1.0790 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 代码在调用 `vim_strsave` 后，立即将返回值赋给 `name`，而 `name` 随后被用于 `vim_free(tofree)` 和 `tofree = name` 的赋值。这表明 `name` 被纳入了资源管理路径（`... |
| 1214 | vim-9.1.0790 | define_function | cpp/inconsistent-null-check | 5356 | FP | FP | 告警指出的 vim_strchr 调用结果未检查 NULL，但代码中该调用仅用于检查字符 '(' 是否存在，其返回值仅用于布尔判断（是否为 NULL），后续逻辑不依赖指针解引用，因此不存在空指针解引用风险。 |
| 1216 | vim-9.1.0790 | exec_instructions | cpp/inconsistent-null-check | 3266 | FP | FP | alloc_clear 返回的指针被直接赋值给 tv->vval.v_object，后续代码立即访问该对象的成员（如 obj_class），若 alloc_clear 返回 NULL 将导致空指针解引用。然而，在 Vim 代码库中，a... |
| 1217 | vim-9.1.0790 | barline_parse | cpp/inconsistent-null-check | 1122 | FP | FP | 切片代码显示，调用 `vim_strsave(s)` 的结果被赋值给局部变量 `s`，随后 `s` 被赋值给 `value->bv_string`。`value->bv_allocated` 被设置为 `allocated ｜｜ co... |
| 1218 | vim-9.1.0790 | ex_history | cpp/unsafe-strcat | 780 | FP | FP | 代码在调用STRCAT前，已通过条件`vim_strsize(hist[i].hisstr) > (int)Columns - 10`检查了源字符串长度，若过长则调用`trunc_string`进行截断处理，确保了目标缓冲区IObuf... |
| 1219 | vim-9.1.0790 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | STRCAT 宏操作的目标缓冲区 NameBuff 在代码中未显示其大小定义，但根据上下文（如用于存储文件路径）和 Vim 项目的惯例，它很可能是一个足够大的固定大小缓冲区（如 MAXPATHL），用于安全地拼接目录和文件扩展名。告警... |
| 1220 | vim-9.1.0790 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 代码中`name`的来源是固定的字符串常量或受控的字符数组`namebuf`，其长度最大为3（如"F12"），而`buf`在拼接前已被初始化为空字符串，且拼接的字符数有限（最多"C"、"S"、"M"、"-"和`name`），总长度远小... |
| 1221 | vim-9.1.0790 | do_put | cpp/unsafe-strcat | 2095 | FP | FP | 告警指向的STRCAT宏调用位于一个已分配固定大小缓冲区的安全上下文中，源字符串y_array[y_size - 1]和目标缓冲区newp的长度均受控，且目标缓冲区大小已通过alloc计算确保足够容纳拼接结果，不存在缓冲区溢出风险。 |
| 1222 | vim-9.1.0790 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限内容，并确保其以NUL结尾，且后续拼接的源字符串p来自原始单词word，其长度受MAXWLEN和条件检查约束，缓冲区溢出风... |
| 1227 | vim-9.1.0790 | ga_concat_strings | cpp/unbounded-write | 788 | FP | FP | 代码中目标缓冲区 `p` 的大小已通过精确计算分配（`alloc(len + 1)`），且 `len` 已包含所有待拼接字符串及分隔符的长度，因此 `STRCPY` 操作不会导致缓冲区溢出。 |
| 1228 | vim-9.1.0790 | maketitle | cpp/unbounded-write | 4145 | FP | FP | STRCPY的目标缓冲区icon_str指向buf（大小为IOSIZE），而源字符串p是经过长度计算和截断的，其长度被限制在100字节以内，且目标缓冲区大小足够，因此不存在缓冲区溢出风险。 |
| 1229 | vim-9.1.0790 | buf_write | cpp/unbounded-write | 1208 | FP | FP | 代码中STRCPY(IObuff, fname)的源缓冲区fname是函数参数，其长度受限于文件系统路径的最大长度（MAXPATHL），且IObuff被定义为全局数组，大小足以容纳最大路径。因此，该strcpy调用不会导致缓冲区溢出。 |
| 1230 | vim-9.1.0790 | buf_write | cpp/unbounded-write | 2566 | FP | FP | 告警指出的strcat调用位于错误消息构建路径，其目标缓冲区IObuff的大小为IOSIZE（切片中可见），且告警点前的代码已通过msg_add_fname等函数确保了IObuff有足够空间，并通过长度检查（STRLEN(IObuff... |
| 1231 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2138 | FP | FP | 代码中使用了宏STRCAT，其定义为strcat，但切片显示目标缓冲区'leader'是通过alloc动态分配的，其大小计算包含了源字符串长度（lead_len + lead_repl_len + extra_space + extr... |
| 1232 | vim-9.1.0790 | transstr | cpp/unbounded-write | 366 | FP | FP | 目标缓冲区 `res` 的大小已通过 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 精确分配，其长度足以容纳源字符串 `s` 转换后的所有字符，因此 `strcat` 操作不会导致缓冲区溢出。 |
| 1233 | vim-9.1.0790 | globpath | cpp/unbounded-write | 3795 | FP | FP | 切片代码显示，在调用STRCAT(buf, file)之前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区buf的剩余空间，确保拼接后的总长度不会超过MAXP... |
| 1234 | vim-9.1.0790 | win_redr_status_matches | cpp/unbounded-write | 639 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为buf分配了足够大小的缓冲区（Columns * MB_MAXBYTES + 1 或 Columns + 1），且后续逻辑通过clen等变量严格控制了写入长度，确保不会超出... |
| 1235 | vim-9.1.0790 | win_redr_status_matches | cpp/unbounded-write | 658 | FP | FP | STRCPY 的目标缓冲区 `buf` 已通过 `alloc(Columns + 1)` 或 `alloc(Columns * MB_MAXBYTES + 1)` 分配了固定大小，且源字符串 `transchar_byte(*s)` ... |
| 1236 | vim-9.1.0790 | debuggy_find | cpp/unbounded-write | 1067 | FP | FP | 代码中 `name` 的分配大小为 `STRLEN(fname) + 3`，而 `STRCPY` 的目标缓冲区 `name` 和 `name + 5` 均指向该分配内存，且复制的源字符串 `fname` 长度已知（通过 `STRLEN... |
| 1237 | vim-9.1.0790 | has_profiling | cpp/unbounded-write | 973 | FP | FP | STRCPY的目标缓冲区pe->pen_name的大小是通过alloc(offsetof(profentry_T, pen_name) + STRLEN(fname) + 1)精确分配的，长度足以容纳源字符串fname及其终止符，因此... |
| 1238 | vim-9.1.0790 | do_string_sub | cpp/unbounded-write | 7697 | FP | FP | 告警点位于 `if (ga.ga_data != NULL) STRCPY(...)` 语句中，`STRCPY` 的目标缓冲区 `(char *)ga.ga_data + ga.ga_len` 是动态增长的数组 `ga.ga_data... |
| 1239 | vim-9.1.0790 | make_expanded_name | cpp/unbounded-write | 6918 | FP | FP | 代码在调用STRCPY前，已通过alloc分配了足够容纳源字符串、前缀和后缀长度的目标缓冲区，缓冲区大小计算正确，不存在缓冲区溢出的风险。 |
| 1240 | vim-9.1.0790 | make_expanded_name | cpp/unbounded-write | 6920 | FP | FP | 代码在调用STRCAT前，已通过alloc为retval分配了足够的内存，其大小为STRLEN(temp_result) + (expr_start - in_start) + (in_end - expr_end) + 1，该大小已... |
| 1241 | vim-9.1.0790 | set_var_const | cpp/unbounded-write | 4183 | FP | FP | STRCPY宏的目标缓冲区di->di_key的大小已通过alloc分配，大小为STRLEN(varname) + 1，与源字符串长度完全匹配，不存在缓冲区溢出风险。 |
| 1242 | vim-9.1.0790 | cat_prefix_varname | cpp/unbounded-write | 2504 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过动态内存分配确保目标缓冲区varnamebuf的大小足以容纳源字符串name（计算了name的长度并额外预留了空间），因此不存在缓冲区溢出的风险。 |
| 1243 | vim-9.1.0790 | ex_substitute | cpp/unbounded-write | 4883 | FP | FP | 切片代码中，STRCAT宏被用于拼接字符串，但目标缓冲区new_start是动态分配的，其大小new_start_len在分配时已考虑了所需长度并留有额外空间，且拼接前有长度检查确保不会溢出。因此不存在缓冲区溢出风险。 |
| 1244 | vim-9.1.0790 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区buf分配了精确的长度len，该长度已通过计算确保能容纳源字符串cmd及所有其他拼接内容，因此不存在缓冲区溢出风险。 |
| 1245 | vim-9.1.0790 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 代码在调用STRCAT前，已通过alloc(len)分配了缓冲区，且len的计算已考虑了cmd、itmp、otmp等所有拼接字符串的长度，并预留了终止符空间。缓冲区大小足够，不存在溢出风险。 |
| 1246 | vim-9.1.0790 | ex_sort | cpp/unbounded-write | 605 | FP | FP | 代码中目标缓冲区 `sortbuf1` 的大小为 `maxlen + 1`，而 `maxlen` 是待排序行中最大行的长度。源字符串 `s` 来自 `ml_get(get_lnum)`，其长度已通过 `ml_get_len` 计算并用... |
| 1247 | vim-9.1.0790 | expand_sfile | cpp/unbounded-write | 9801 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为目标缓冲区newres分配了足够的内存（resultlen + 1），且resultlen已根据源字符串repl的长度和替换长度srclen精确计算，缓冲区大小与要拷贝的字... |
| 1249 | vim-9.1.0790 | repl_cmdline | cpp/unbounded-write | 5308 | FP | FP | 代码中目标缓冲区 `new_cmdline` 的大小 `i` 已通过计算 `(src - *cmdlinep) + repllen + taillen + 3` 并加上 `eap->nextcmd` 的长度（如果存在）来精确分配，其大... |
| 1251 | vim-9.1.0790 | replace_makeprg | cpp/unbounded-write | 5024 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为目标缓冲区分配了足够的内存，大小由源字符串长度计算得出，确保了不会发生缓冲区溢出。 |
| 1252 | vim-9.1.0790 | do_one_cmd | cpp/unbounded-write | 2673 | FP | FP | 切片代码中STRCPY宏用于将静态错误消息字符串复制到IObuff缓冲区，源字符串是编译时常量，长度固定且已知，目标缓冲区IObuff大小在代码中未明确显示，但根据上下文（错误消息处理）和Vim的编码实践，IObuff通常定义为足够大... |
| 1253 | vim-9.1.0790 | discard_exception | cpp/unbounded-write | 642 | FP | FP | 告警点 `STRCPY(IObuff, saved_IObuff)` 中，目标缓冲区 `IObuff` 是全局缓冲区，其大小 `IOSIZE` 在切片中未直接显示，但源数据 `saved_IObuff` 是 `IObuff` 的副本（... |
| 1254 | vim-9.1.0790 | get_exception_string | cpp/unbounded-write | 473 | FP | FP | 切片代码显示，目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度已计算了源字符串 `mesg` 或 `p` 的长度，因此 `strcat` 操作不会导致缓冲区溢出。 |
| 1256 | vim-9.1.0790 | escape_fname | cpp/unbounded-write | 4109 | FP | FP | 目标缓冲区 `p` 的大小通过 `alloc(STRLEN(*pp) + 2)` 分配，其长度精确计算为源字符串长度加2，因此 `STRCPY(p + 1, *pp)` 的写入不会发生溢出。 |
| 1257 | vim-9.1.0790 | cmdline_browse_history | cpp/unbounded-write | 1498 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc_cmdbuff(plen)为目标缓冲区ccline.cmdbuff分配了足够空间，且分配大小plen等于源字符串p的长度，因此不会发生缓冲区溢出。 |
| 1258 | vim-9.1.0790 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 864 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过realloc_cmdbuff(len + 1)为目标缓冲区ccline.cmdbuff重新分配了足够容纳源字符串p（长度为len）及结尾空字符的空间，确保了缓冲区大小足够，不会发生溢出。 |
| 1259 | vim-9.1.0790 | <global> | cpp/unbounded-write | 5375 | FP | FP | 代码中 `sprintf` 的目标缓冲区 `itmp` 大小为 `TEMPNAMELEN`，而源字符串 `vim_tempdir` 是之前通过 `expand_env` 并附加路径分隔符和固定字符串生成的，其长度已通过 `TEMPNA... |
| 1260 | vim-9.1.0790 | vim_settempdir | cpp/unbounded-write | 5235 | FP | FP | 切片代码显示，目标缓冲区 `buf` 的大小为 `MAXPATHL + 2`，而 `vim_FullName` 函数调用时传入的长度参数也是 `MAXPATHL`，且该函数在失败时会安全地截断输入。当 `vim_FullName` 失... |
| 1261 | vim-9.1.0790 | <global> | cpp/unbounded-write | 4352 | FP | FP | 代码在调用 sprintf 前，已通过 alloc(STRLEN(path) + STRLEN(mesg) + STRLEN(mesg2) + 2) 为目标缓冲区 tbuf 分配了足够的空间，其大小是源字符串长度之和加上格式字符串和空... |
| 1262 | vim-9.1.0790 | vim_rename | cpp/unbounded-write | 3839 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。 |
| 1263 | vim-9.1.0790 | buf_modname | cpp/unbounded-write | 3620 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区retval分配了足够空间（fnamelen + extlen + 3），且fnamelen和extlen均来自已知字符串的长度计算，不存在缓冲区溢出的风险。 |
| 1264 | vim-9.1.0790 | addfile | cpp/unbounded-write | 4198 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过`alloc(STRLEN(f) + 1 + isdir)`为目标缓冲区`p`分配了精确的、足以容纳源字符串`f`及其可能添加的路径分隔符的空间，因此不存在缓冲区溢出的风险。 |
| 1265 | vim-9.1.0790 | unix_expandpath | cpp/unbounded-write | 3833 | FP | FP | 代码中使用了STRCPY宏，但目标缓冲区`buf`的大小`buflen`已通过`STRLEN(path) + MAXPATHL`计算并分配，且源字符串`s`指向`buf`内部，`path_end + 1`的长度不会超过`buflen ... |
| 1266 | vim-9.1.0790 | concat_fnames | cpp/unbounded-write | 3123 | FP | FP | 代码通过alloc函数为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcpy操作不会发生缓冲区溢出。 |
| 1267 | vim-9.1.0790 | concat_fnames | cpp/unbounded-write | 3126 | FP | FP | 函数通过alloc为目标缓冲区分配了足够的空间，大小为两个输入字符串长度之和加3，确保了strcat操作不会溢出。代码逻辑保证了安全性。 |
| 1268 | vim-9.1.0790 | uniquefy_paths | cpp/unbounded-write | 2364 | FP | FP | 告警点 `STRCAT(file_pattern, pattern)` 中，`file_pattern` 缓冲区的大小为 `len + 2`，其中 `len` 是 `pattern` 的长度。拼接前已确保 `file_pattern`... |
| 1269 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1718 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区是NameBuff，其大小为MAXPATHL，而源字符串(*file_to_find或rel_fname)在复制前已通过条件`STRLEN(rel_fname) + l < MAXPATHL`或... |
| 1270 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1719 | FP | FP | STRCPY 宏的目标缓冲区 NameBuff 大小为 MAXPATHL，而源字符串长度在复制前已通过 STRLEN 检查，且拼接前验证了 STRLEN(rel_fname) + l < MAXPATHL，因此不会发生缓冲区溢出。 |
| 1271 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1724 | FP | FP | STRCPY 宏的目标缓冲区 NameBuff 大小为 MAXPATHL，而源字符串 *file_to_find 在函数开头已通过 expand_env_esc 处理并存入 NameBuff，其长度受 MAXPATHL 限制，且后续复... |
| 1272 | vim-9.1.0790 | ff_check_visited | cpp/unbounded-write | 1370 | FP | FP | 目标缓冲区 `vp->ffv_fname` 的大小是动态分配的，其大小为 `STRLEN(ff_expand_buffer) + 1`，与源字符串 `ff_expand_buffer` 的长度完全匹配，因此 `STRCPY`（即 `s... |
| 1273 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 805 | FP | FP | 代码在调用STRCPY前，已通过STRLEN检查确保目标缓冲区大小（MAXPATHL）足够容纳源字符串，并包含终止符，因此不会发生缓冲区溢出。 |
| 1274 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 819 | FP | FP | 代码在调用STRCAT前，已通过条件`STRLEN(file_path) + STRLEN(stackp->ffs_fix_path) + 1 < MAXPATHL`检查了目标缓冲区`file_path`的剩余空间，确保不会发生缓冲区溢出。 |
| 1275 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 940 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过STRLEN计算源字符串和目标缓冲区剩余长度，并与MAXPATHL常量进行比较，确认不会发生缓冲区溢出。切片中可见多处长度检查，安全防护机制有效。 |
| 1276 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 942 | FP | FP | 代码在调用STRCAT（即strcat）前，已通过STRLEN(file_path) + STRLEN(search_ctx->ffsc_file_to_search) + 1 < MAXPATHL进行了明确的缓冲区长度检查，确保拼接... |
| 1277 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 1110 | FP | FP | 代码在调用STRCPY前，已通过STRLEN检查确保目标缓冲区大小（MAXPATHL）足以容纳源字符串，从而避免了缓冲区溢出。 |
| 1278 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 1112 | FP | FP | 代码在调用STRCAT前，已通过条件`STRLEN(file_path) + STRLEN(search_ctx->ffsc_fix_path) < MAXPATHL`检查了目标缓冲区`file_path`的剩余空间，确保不会发生缓冲... |
| 1279 | vim-9.1.0790 | <global> | cpp/unbounded-write | 537 | FP | FP | 代码中使用了STRCPY宏，但目标缓冲区ff_expand_buffer的大小为MAXPATHL，而源字符串search_ctx->ffsc_start_dir是通过vim_strsave等函数分配的，其长度受MAXPATHL限制，且... |
| 1280 | vim-9.1.0790 | <global> | cpp/unbounded-write | 545 | FP | FP | 切片代码中所有 STRCPY 宏的使用，其目标缓冲区（如 ff_expand_buffer, buf, temp）的大小均通过 alloc/MAXPATHL 等机制进行了分配或保证，且源字符串长度在复制前已通过 STRLEN 或类似计... |
| 1281 | vim-9.1.0790 | <global> | cpp/unbounded-write | 548 | FP | FP | 代码中 `ff_expand_buffer` 在函数开头已通过 `alloc(MAXPATHL)` 分配了固定大小的缓冲区（MAXPATHL），且告警点 `STRCAT` 拼接的源字符串 `search_ctx->ffsc_fix_p... |
| 1282 | vim-9.1.0790 | <global> | cpp/unbounded-write | 590 | FP | FP | 切片代码中，所有对STRCPY宏的调用，其目标缓冲区（如ff_expand_buffer、buf、temp）的大小均通过alloc或MAXPATHL常量进行分配，且分配大小明确。STRCPY操作前，代码通过长度检查（如len + 1 ... |
| 1283 | vim-9.1.0790 | <global> | cpp/unbounded-write | 591 | FP | FP | 告警点 `STRCAT(temp, search_ctx->ffsc_wc_path);` 中，目标缓冲区 `temp` 的大小已通过 `alloc` 精确分配，其大小为源字符串 `search_ctx->ffsc_fix_path ... |
| 1284 | vim-9.1.0790 | <global> | cpp/unbounded-write | 3798 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够大的缓冲区，其大小计算包含了源字符串s的长度，因此不会发生缓冲区溢出。 |
| 1285 | vim-9.1.0790 | foldDelMarker | cpp/unbounded-write | 1897 | FP | FP | 代码中目标缓冲区 `newline` 的大小通过 `alloc(ml_get_len(lnum) - len + 1)` 精确计算，确保其足以容纳源字符串 `line` 减去被删除标记 `len` 后的内容再加一个空字符。`STRCP... |
| 1286 | vim-9.1.0790 | foldAddMarker | cpp/unbounded-write | 1815 | FP | FP | 代码中目标缓冲区 `newline` 的大小通过 `alloc(line_len + markerlen + STRLEN(cms) + 1)` 动态分配，其大小精确计算了源字符串长度之和并包含终止符，因此 `STRCPY`（即 `s... |
| 1287 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2899 | FP | FP | 告警点 `STRCPY(buffer, res_prolog->title);` 中，`res_prolog->title` 来源于受控的资源文件解析（`prt_open_resource`），其长度已在解析时被 `vim_strnc... |
| 1288 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2901 | FP | FP | 切片代码显示，`res_prolog->title` 和 `res_prolog->version` 是从受控的 PostScript 资源文件中解析出的固定字段，其长度在文件解析阶段已确定，且 `buffer` 大小为 256 字节... |
| 1289 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2905 | FP | FP | 告警点 `STRCPY(buffer, res_cidfont->title);` 中，`res_cidfont->title` 来源于 `prt_open_resource` 函数从资源文件中读取的标题，其长度已在解析时被 `vim... |
| 1290 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 切片代码显示，`res_cidfont->title` 和 `res_cidfont->version` 是从受控的 PostScript 资源文件中解析出的固定字符串，其长度在文件解析阶段（`prt_open_resource`）已... |
| 1291 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 告警点 `STRCPY(buffer, res_cmap->title);` 中，`res_cmap->title` 来源于外部资源文件，其内容在 `prt_open_resource` 函数中通过解析文件头获得，长度受 `vim_s... |
| 1292 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_cmap->title`和`res_cmap->version`均来自受控的PostScript资源文件，其内容长度已在`prt_open_resource`函数中通过解析和验证... |
| 1293 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2920 | FP | FP | 告警点 `STRCPY(buffer, res_encoding->title);` 中，`buffer` 是大小为256的局部数组，而 `res_encoding->title` 的来源已在 `prt_open_resource` ... |
| 1294 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2922 | FP | FP | 告警涉及的`buffer`数组大小为256字节，而`res_encoding->title`和`res_encoding->version`均来自受控的PostScript资源文件，其内容长度已在`prt_open_resource`... |
| 1295 | vim-9.1.0790 | prt_resource_name | cpp/unbounded-write | 1659 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过`if (STRLEN(filename) >= MAXPATHL)`检查了源字符串长度，若长度超过目标缓冲区大小（MAXPATHL），则会将目标字符串置空，从而避免了缓冲区... |
| 1296 | vim-9.1.0790 | do_helptags | cpp/unbounded-write | 1210 | FP | FP | STRCPY 宏的目标缓冲区 NameBuff 在代码中未显示其大小，但根据其名称和常见用法推断，它很可能是一个足够大的全局缓冲区（如 MAXPATHL）。告警点是将已知的目录名复制到该缓冲区，且后续操作（如 add_pathsep）... |
| 1297 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 975 | FP | FP | 告警指向的 `STRCAT(NameBuff, ext);` 行，其目标缓冲区 `NameBuff` 在切片中可见其大小为 `MAXPATHL`（通过 `vim_snprintf` 调用可推断），且 `ext` 参数是函数传入的固定后... |
| 1298 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 991 | FP | FP | NameBuff 是一个全局缓冲区，其大小定义为 MAXPATHL（通常为 260 或 4096），而告警点拼接的 tagfname 是函数参数，其长度受限于文件系统路径长度，且拼接前已确保 NameBuff 末尾有路径分隔符，因此不... |
| 1299 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 1112 | FP | FP | sprintf 的目标缓冲区 s 的大小是精确计算的（p2 - p1 + STRLEN(fname) + 2），足以容纳源字符串 p1 和 fname 以及分隔符和终止符，因此不会发生缓冲区溢出。 |
| 1300 | vim-9.1.0790 | highlight_set_startstop_termcode | cpp/unbounded-write | 1477 | FP | FP | 代码在调用STRCAT前，已通过条件`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了目标缓冲区buf（大小为100）的剩余空间，确保不会发生溢出。 |
| 1303 | vim-9.1.0790 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...），并分配了对应大小的内存（buf = alloc(amt)），因此不会发生缓冲区溢出。 |
| 1304 | vim-9.1.0790 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了相应内存（buf = alloc(amt)），确保了目标缓冲区大小足以容纳格式化后的字符串，因此不存在缓冲区溢出风险。 |
| 1307 | vim-9.1.0790 | cs_add_common | cpp/unbounded-write | 604 | FP | FP | sprintf 的目标缓冲区 fname2 的大小是动态计算的，为 strlen(CSCOPE_DBFILE) + strlen(fname) + 2，这足以容纳拼接后的路径，因此不会发生缓冲区溢出。 |
| 1308 | vim-9.1.0790 | ins_compl_infercase_gettext | cpp/unbounded-write | 653 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`(p - IObuff) + 6 >= IOSIZE`确保目标缓冲区`gap.ga_data`有足够空间，因为`ga_grow(&gap, IOSIZE)`已成功分配... |
| 1310 | vim-9.1.0790 | findswapname | cpp/unbounded-write | 4967 | FP | FP | STRCPY 的目标缓冲区 fname2 是刚通过 alloc(n + 2) 分配的，大小为源字符串 fname 的长度 n 加上 2，因此目标缓冲区足够容纳源字符串，不存在缓冲区溢出风险。 |
| 1311 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2157 | FP | FP | 代码通过 `alloc(STRLEN(f) + 1)` 为目标缓冲区 `s` 分配了精确匹配源字符串 `f` 长度的空间，`STRCPY(s, f)` 的源和目标大小相同，不会发生缓冲区溢出。 |
| 1312 | vim-9.1.0790 | <global> | cpp/unbounded-write | 811 | FP | FP | 代码中 `STRCPY` 的目标缓冲区 `menu->strings[i]` 已通过 `alloc(STRLEN(call_data) + 5)` 分配了足够的空间，其大小明确为源字符串长度加5，因此不会发生缓冲区溢出。 |
| 1313 | vim-9.1.0790 | <global> | cpp/unbounded-write | 815 | FP | FP | 告警点位于 STRCPY(menu->strings[i] + 2, call_data) 调用，其中 call_data 在切片中可见由 vim_strsave(call_data) 复制，其长度已知。目标缓冲区 menu->str... |
| 1315 | vim-9.1.0790 | str2specialbuf | cpp/unbounded-write | 1919 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度小于传入的长度参数`len... |
| 1316 | vim-9.1.0790 | get_emsg_source | cpp/unbounded-write | 484 | FP | FP | 代码通过 `alloc(STRLEN(sname) + STRLEN(p))` 为目标缓冲区分配了足够的空间，该大小是源字符串长度之和，因此 `sprintf` 不会发生缓冲区溢出。 |
| 1317 | vim-9.1.0790 | may_trigger_modechanged | cpp/unbounded-write | 2821 | FP | FP | STRCPY的目标缓冲区`last_mode`和源缓冲区`curr_mode`大小均为`MODE_MAX_LENGTH`，且`get_mode`函数确保写入的字符数严格小于该长度，因此不会发生缓冲区溢出。 |
| 1318 | vim-9.1.0790 | expand_env_esc | cpp/unbounded-write | 1632 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过条件`(STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen)`检查了目标缓冲区`dst`的剩余空间`dstlen`是否足以容纳源字符串`... |
| 1319 | vim-9.1.0790 | call_shell | cpp/unbounded-write | 1877 | FP | FP | 代码在调用STRCAT前，已通过alloc为ncmd分配了足够的内存，其大小为STRLEN(ecmd) + STRLEN(p_sxq) * 2 + 1，足以容纳后续的字符串拼接，因此不存在缓冲区溢出风险。 |
| 1320 | vim-9.1.0790 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中均未出现。该告警可能是工具对宏（如STRCAT）的误识别或代码切片未包含实际调用点。 |
| 1322 | vim-9.1.0790 | push_showcmd | cpp/unbounded-write | 1805 | FP | FP | 切片代码显示，`STRCPY` 的目标缓冲区 `old_showcmd_buf` 和源缓冲区 `showcmd_buf` 均为全局数组，其大小在代码其他位置定义且相等。该函数仅在条件 `p_sc` 为真时执行一个固定大小的缓冲区拷贝，... |
| 1323 | vim-9.1.0790 | add_to_showcmd | cpp/unbounded-write | 1760 | FP | FP | 切片代码显示，在调用STRCAT前，已通过计算`overflow`变量并调用`mch_memmove`来确保目标缓冲区`showcmd_buf`有足够的剩余空间，从而防止了缓冲区溢出。 |
| 1324 | vim-9.1.0790 | op_change | cpp/unbounded-write | 1867 | FP | FP | 切片代码中，STRCPY宏被用于复制已知长度的字符串（ins_len），且目标缓冲区newp已根据源字符串长度（ml_get_len(linenr) + vpos.coladd + ins_len + 1）分配了足够空间，不会发生缓冲... |
| 1325 | vim-9.1.0790 | op_replace | cpp/unbounded-write | 1163 | FP | FP | 代码中STRCPY宏的目标缓冲区newp和after_p均通过alloc分配了足够大小（oldlen + 1 + n），且n已根据替换字符数量精确计算，确保了目标缓冲区大小不小于源字符串长度，因此不存在缓冲区溢出风险。 |
| 1326 | vim-9.1.0790 | op_replace | cpp/unbounded-write | 1172 | FP | FP | 代码中STRCPY宏的目标缓冲区`after_p`是通过`alloc(oldlen + 1 + n - newlen)`分配的，其大小计算包含了源字符串`oldp + bd.textcol + bd.textlen`的长度（通过`ol... |
| 1327 | vim-9.1.0790 | op_delete | cpp/unbounded-write | 826 | FP | FP | 代码中STRCPY宏的目标缓冲区newp是通过alloc(ml_get_len(lnum) + 1 - n)分配的，其大小精确计算为原行长减去删除字符数再加1，确保了足够的空间容纳源字符串oldp + bd.textcol + bd.... |
| 1328 | vim-9.1.0790 | block_insert | cpp/unbounded-write | 607 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区newp是通过alloc函数分配的，其大小计算为ml_get_len(lnum) + spaces + slen + ...，这确保了目标缓冲区足够容纳源字符串oldp（来自ml_get的原始行... |
| 1329 | vim-9.1.0790 | option_value2string | cpp/unbounded-write | 8213 | FP | FP | 代码切片显示，STRCPY宏的目标缓冲区NameBuff是一个全局缓冲区，其大小未在切片中明确给出，但告警点位于option_value2string函数中，该函数在P_STRING分支明确使用了vim_strncpy(NameBuf... |
| 1330 | vim-9.1.0790 | option_value2string | cpp/unbounded-write | 8215 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，函数wc_use_keyname和get_special_key_name内部已对输入进行了处理，且目标缓冲区NameBuff的大小未在切片中明确给出，但告警点位于处理数值选项（... |
| 1331 | vim-9.1.0790 | stropt_expand_envvar | cpp/unbounded-write | 1800 | FP | FP | 目标缓冲区 `newval` 的大小 `newlen` 已通过 `alloc(newlen)` 精确分配，其大小足以容纳源字符串 `s` 及其终止符，因此 `STRCPY` 调用不会导致缓冲区溢出。 |
| 1332 | vim-9.1.0790 | mch_expand_wildcards | cpp/unbounded-write | 6937 | FP | FP | 代码在调用strcat前已通过alloc(len)为目标缓冲区command分配了精确计算的长度len，该长度已考虑了所有待拼接字符串（包括环境变量、静态字符串和用户输入）的总和，因此不存在缓冲区溢出的风险。 |
| 1333 | vim-9.1.0790 | mch_expand_wildcards | cpp/unbounded-write | 7283 | FP | FP | 代码中使用了宏 `STRCPY(p, (*file)[i])`，但目标缓冲区 `p` 的大小为 `STRLEN((*file)[i]) + 1 + dir`，已通过 `alloc` 精确分配，与源字符串长度匹配，因此不会发生缓冲区溢出。 |
| 1334 | vim-9.1.0790 | mch_FullName | cpp/unbounded-write | 2819 | FP | FP | 代码在调用STRCAT（即strcat）前，已通过条件`(int)(STRLEN(buf) + STRLEN(fname)) >= len`检查了目标缓冲区`buf`的剩余空间是否足以容纳源字符串`fname`，确保了不会发生缓冲区溢出。 |
| 1335 | vim-9.1.0790 | qf_store_title | cpp/unbounded-write | 1934 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc_id分配了大小为STRLEN(title) + 2的内存，目标缓冲区大小明确基于源字符串长度计算，确保了足够的空间，因此不存在缓冲区溢出风险。 |
| 1338 | vim-9.1.0790 | regtilde | cpp/unbounded-write | 1959 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过tmpsublen > MAXCOL的检查确保目标缓冲区tmpsub的大小（tmpsublen + 1）足够容纳源字符串postfix，且postfixlen是经过计算得出的安全长度，... |
| 1339 | vim-9.1.0790 | match_with_backref | cpp/unbounded-write | 1600 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区reg_tofree分配了足够的内存，其中len的计算基于STRLEN(rex.line) + 50，确保了缓冲区大小不小于源字符串长度加额外... |
| 1340 | vim-9.1.0790 | get_reg_contents | cpp/unbounded-write | 2668 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len + 1)为目标缓冲区retval分配了精确长度（len为所有源字符串长度及换行符的总和），且循环中每次拷贝后都正确更新了目标偏移量len，因此不会发生缓冲区溢出。 |
| 1341 | vim-9.1.0790 | do_put | cpp/unbounded-write | 2094 | FP | FP | 切片代码中未发现对strcpy的直接调用，告警消息中提到的多个strcpy调用在切片中不存在。切片中使用的字符串复制操作是STRCPY宏，但告警规则检测的是strcpy，可能为工具误报或规则匹配错误。 |
| 1342 | vim-9.1.0790 | do_put | cpp/unbounded-write | 2095 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中不存在。该告警可能是工具对宏展开或代码路径的误判，实际代码中使用了安全的字符串操作宏和函数。 |
| 1343 | vim-9.1.0790 | op_yank | cpp/unbounded-write | 1278 | FP | FP | 代码中STRCPY宏的目标缓冲区pnew是通过alloc(STRLEN(...) + STRLEN(...) + 1)分配的，其大小精确等于源字符串长度之和加1，因此不会发生缓冲区溢出。 |
| 1344 | vim-9.1.0790 | op_yank | cpp/unbounded-write | 1279 | FP | FP | 代码在调用STRCAT前，已通过alloc为目标缓冲区pnew分配了足够的空间，其大小为两个源字符串长度之和加1，因此不会发生缓冲区溢出。 |
| 1345 | vim-9.1.0790 | stuff_yank | cpp/unbounded-write | 452 | FP | FP | 目标缓冲区 `lp` 的大小是通过 `alloc(STRLEN(*pp) + STRLEN(p) + 1)` 精确分配的，其大小足以容纳源字符串 `*pp` 和 `p` 的连接结果。在调用 `STRCPY(lp, *pp)` 之前，`... |
| 1346 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2755 | FP | FP | 目标缓冲区 `scriptname` 的大小通过 `alloc(STRLEN(name) + 14)` 精确分配，足以容纳固定前缀 "autoload/"、处理后的 `name` 字符串以及后缀 ".vim"，且 `STRCAT` 调... |
| 1348 | vim-9.1.0790 | sign_jump | cpp/unbounded-write | 1324 | FP | FP | 代码中通过 `alloc(STRLEN(buf->b_fname) + 25)` 为目标缓冲区分配了足够的空间，其大小为文件名长度加上固定开销，确保 `sprintf` 写入不会溢出。 |
| 1349 | vim-9.1.0790 | dump_word | cpp/unbounded-write | 4187 | FP | FP | 代码中目标缓冲区 `badword` 的大小为 `MAXWLEN + 10`，而源字符串 `p` 是 `word` 或 `cword`，两者大小均受 `MAXWLEN` 限制。`STRCPY` 操作前，源字符串长度不会超过目标缓冲区大... |
| 1350 | vim-9.1.0790 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 告警点位于 `make_case_word` 函数中，该函数仅在 `fword` 和 `cword` 为相同长度或 `cword` 有足够空间时被调用。切片中 `allcap_copy` 和 `onecap_copy` 函数均对目标缓... |
| 1351 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2998 | FP | FP | 代码中目标缓冲区 `p` 的大小是动态计算的（`ml_get_curline_len() + addlen + 1`），其中 `addlen` 是 `repl_to_len - repl_from_len`，且 `STRCPY` 复制... |
| 1352 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2999 | FP | FP | 代码在调用STRCAT前，已为目标缓冲区p分配了足够的空间（ml_get_curline_len() + addlen + 1），且addlen的计算考虑了替换字符串的长度差，确保了缓冲区大小足以容纳拼接后的字符串，因此不存在缓冲区溢... |
| 1353 | vim-9.1.0790 | count_common_word | cpp/unbounded-write | 1919 | FP | FP | STRCPY 的目标缓冲区 wc->wc_word 的大小为 STRLEN(p) + 1，是通过 alloc 函数动态分配的，其大小与源字符串 p 的长度精确匹配，因此不会发生缓冲区溢出。 |
| 1355 | vim-9.1.0790 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 代码在调用 STRCPY（即 strcpy）前，已通过 alloc(buflen) 为 buf 分配了足够的内存，其中 buflen 被设置为 len + MAXWLEN + 2，而 len 是当前行的长度。STRCPY 的目标缓冲区... |
| 1356 | vim-9.1.0790 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数getroom_save通过getroom分配了长度为STRLEN(s)+1的内存，然后使用STRCPY（即strcpy）进行复制，目标缓冲区大小与源字符串长度精确匹配，不存在缓冲区溢出的风险。 |
| 1357 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 代码中使用了安全的字符串拼接模式：先通过getroom分配了足够容纳所有字符串和分隔符的总长度内存，然后使用STRCPY和STRCAT进行拼接。由于目标缓冲区大小是预先计算并分配的，不存在缓冲区溢出的风险。 |
| 1358 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 代码中使用了安全的字符串拼接模式：首先通过计算所需总长度（包括现有字符串长度、分隔符和新增字符串长度）分配足够内存，然后使用STRCPY和STRCAT进行拷贝，这确保了目标缓冲区大小足够，不会发生溢出。 |
| 1359 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2464 | FP | FP | 代码中STRCPY的目标缓冲区p是通过getroom(spin, STRLEN(items[1]) + 2, FALSE)分配的，其大小明确为源字符串长度加2，足以容纳源字符串和追加的'+'字符，因此不会发生缓冲区溢出。 |
| 1360 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 代码中已通过 `getroom(spin, l, FALSE)` 为目标缓冲区 `p` 分配了足够空间，其大小为 `l`（已计算为 `STRLEN(compflags) + STRLEN(items[1]) + 2` 等），然后才调用... |
| 1361 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 代码中使用了 vim_fgets 读取文件行到固定大小的缓冲区 rline[MAXLINELEN]，该函数内部会检查并截断超长行，确保不会发生缓冲区溢出。因此 strcpy 操作是安全的。 |
| 1362 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2746 | FP | FP | 代码中使用了安全的 `vim_snprintf` 函数，而非不安全的 `sprintf`。告警点 `sprintf` 的缓冲区 `buf` 大小为 `MAXLINELEN`（定义为 1024），且格式化字符串 `"^%s"` 或 `"... |
| 1363 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2748 | FP | FP | 切片代码中，sprintf的目标缓冲区buf大小为MAXLINELEN（定义为256），而源字符串items[4]来自受控的affix文件行解析，其长度受限于行缓冲区rline（大小也为MAXLINELEN）。在构造buf时，前缀'^... |
| 1364 | vim-9.1.0790 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | STRCPY的目标缓冲区`sft->sft_word`的大小为`STRLEN(goodword) + 1`，是通过`alloc(offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1)... |
| 1365 | vim-9.1.0790 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY 宏的目标缓冲区 fword 大小为 MAXWLEN，源字符串 su->su_fbadword 是拼写建议算法中的内部字符串，其长度在算法上下文中已被确保不超过 MAXWLEN（例如来自拼写检查的单词），因此不会发生缓冲区溢出。 |
| 1366 | vim-9.1.0790 | concat_str | cpp/unbounded-write | 795 | FP | FP | 函数通过alloc为目标缓冲区分配了精确的、足以容纳源字符串的长度（包括终止符），然后使用STRCPY（即strcpy）进行复制。由于目标缓冲区大小是源字符串长度的精确计算值，因此不存在缓冲区溢出的风险。 |
| 1367 | vim-9.1.0790 | concat_str | cpp/unbounded-write | 797 | FP | FP | 函数内已通过alloc为目标缓冲区分配了精确的、足以容纳源字符串的长度（包括空终止符），STRCPY宏展开为strcpy，但目标缓冲区大小确定，不会发生溢出。 |
| 1368 | vim-9.1.0790 | expand_tag_fname | cpp/unbounded-write | 4125 | FP | FP | 目标缓冲区 `retval` 通过 `alloc(MAXPATHL)` 分配了固定大小 `MAXPATHL`，随后 `STRCPY` 的源 `tag_fname` 是函数参数，其长度未知。然而，紧接着的 `vim_strncpy` 调... |
| 1369 | vim-9.1.0790 | findtags_add_match | cpp/unbounded-write | 2623 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`p`和`p + len + 1`均通过`alloc`分配了足够大小（`len + 10 + ML_EXTRA + 1`），且源字符串`st->help_lang`和`st->tag_fname`... |
| 1371 | vim-9.1.0790 | show_one_termcode | cpp/unbounded-write | 7058 | FP | FP | STRCPY的目标缓冲区IObuff+5的起始位置明确，且源字符串p来自get_special_key_name函数，该函数内部使用STRCPY时已通过长度检查确保不会溢出其本地静态缓冲区string，并最终返回该缓冲区。结合上下文，... |
| 1372 | vim-9.1.0790 | current_tagblock | cpp/unbounded-write | 1386 | FP | FP | 代码使用 `sprintf` 格式化字符串时，长度参数 `len` 来源于当前光标位置的标签名长度，该长度受限于当前行缓冲区内容，且分配的目标缓冲区大小（`len + 39` 和 `len + 9`）已明确预留了额外空间，因此不会发生... |
| 1373 | vim-9.1.0790 | uc_check_code | cpp/unbounded-write | 1778 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过STRLEN计算了源字符串长度，并且从上下文看，目标缓冲区buf的大小分配逻辑（未在切片中完全展示）通常与计算结果result相关，暗示了缓冲区大小可能已匹配。此外，对于... |
| 1374 | vim-9.1.0790 | get_scriptlocal_funcname | cpp/unbounded-write | 4658 | FP | FP | 目标缓冲区 `newname` 的大小通过 `alloc(STRLEN(sid_buf) + STRLEN(p + off) + 1)` 精确分配，足以容纳拼接后的字符串，因此 `STRCAT` 调用不会导致缓冲区溢出。 |
| 1375 | vim-9.1.0790 | trans_function_name_ext | cpp/unbounded-write | 4571 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`name`的大小由`alloc(len + lead + extra + 1)`分配，其长度是计算得出的，且源字符串`sid_buf`是内部生成的固定格式字符串，长度受`sprintf`和缓冲区... |
| 1376 | vim-9.1.0790 | fname_trans_sid | cpp/unbounded-write | 2115 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，存在明确的边界检查 `if (i + STRLEN(name + llen) < FLEN_FIXED)`，确保目标缓冲区 `fname_buf` 有足够空间，因此不会发生缓冲区溢出。 |
| 1377 | vim-9.1.0790 | fname_trans_sid | cpp/unbounded-write | 2127 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过条件`i + STRLEN(name + llen) < FLEN_FIXED`或动态分配`alloc(i + STRLEN(name + llen) + 1)`确保目标缓冲区大小足够... |
| 1378 | vim-9.1.0790 | set_ufunc_name | cpp/unbounded-write | 663 | FP | FP | 告警针对的STRCPY宏调用，其目标缓冲区fp->uf_name的大小未知，但调用者set_ufunc_name的参数name来自函数内部逻辑，并非直接来自外部不可控源（如环境变量、文件读取）。切片显示该函数用于设置内部函数名，通常由... |
| 1379 | vim-9.1.0790 | exec_instructions | cpp/unbounded-write | 3496 | FP | FP | 切片代码中STRCPY宏被用于拼接字符串，但目标缓冲区cmd已通过alloc(len + 1)分配了足够空间，且len在拼接前已精确计算了所有源字符串的总长度，因此不会发生缓冲区溢出。 |
| 1380 | vim-9.1.0790 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | FP | 告警点位于 `STRCPY(funcname + 2, name)`，其中 `funcname` 已通过 `alloc(STRLEN(name) + 3)` 分配了足够容纳前缀 `"g:"` 和 `name` 字符串及终止符的空间，目... |
| 1381 | vim-9.1.0790 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | FP | STRCPY的目标缓冲区newsav->sav_key的大小是精确分配的，大小为offsetof(sallvar_T, sav_key) + STRLEN(name) + 1，足以容纳源字符串name及其终止空字符，因此不存在缓冲区溢... |
| 1382 | vim-9.1.0790 | find_exported | cpp/unbounded-write | 756 | FP | FP | 代码在调用sprintf前已通过动态分配确保目标缓冲区大小足够。当len >= sizeof(buffer)时，funcname指向通过alloc(len)分配的内存，其大小等于计算出的所需长度len，因此sprintf写入不会溢出。 |
| 1383 | vim-9.1.0790 | find_exported | cpp/unbounded-write | 763 | FP | FP | 代码在调用sprintf前已通过动态分配确保了目标缓冲区大小足够：当计算出的长度len大于静态缓冲区buffer大小时，会使用alloc(len)分配恰好大小的内存，因此不会发生缓冲区溢出。 |
| 1384 | vim-9.1.0790 | xxdline | cpp/unbounded-write | 534 | FP | FP | 目标缓冲区 `z` 是静态数组 `char z[LLEN+1]`，其大小固定为 `LLEN+1`。调用 `strcpy(z, l)` 时，虽然 `l` 是外部输入，但函数仅在 `nz` 为假且 `zero_seen == 1` 时执行... |
| 1385 | vim-9.1.0790 | ExpandBufnames | cpp/invalid-pointer-deref | 2937 | FP | FP | 告警行 `(*file)[count++] = p;` 仅在 `*file` 已通过 `*file = alloc(...)` 分配内存后才执行，而切片显示在 `round == 1` 时，若 `*file == NULL` 会提前返... |
| 1386 | vim-9.1.0790 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | FP | 切片代码显示，在写入 `p[pos.col + 1]` 之前，已通过条件 `width == 2` 确保 `pos.col + 1` 小于分配的 `len`（因为 `width` 是当前单元格的宽度，且循环条件为 `pos.col <... |
| 1387 | musl-1.2.3 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 分配的内存大小（sizeof *f + UNGET + BUFSIZ）用于为FILE结构体、反推缓冲区（UNGET）和主缓冲区（BUFSIZ）分配连续内存，这是musl libc中实现FILE流的惯用模式，并非错误的分配大小计算。 |
| 1388 | musl-1.2.3 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat前，代码已通过if (scopeid)确保p非空，且p指向的字符串长度有限（来自itoa或if_indextoname），同时buf的大小为256字节，而inet_ntop的输出和p的拼接长度远小于此限制，不会导致缓... |
| 1389 | musl-1.2.3 | load_library | cpp/unbounded-write | 1162 | FP | FP | 目标缓冲区 `p->name` 的大小为 `alloc_size`，该值等于 `sizeof *p + strlen(pathname) + 1`，而源字符串 `pathname` 的长度已通过 `strlen(pathname)` ... |
| 1390 | musl-1.2.3 | <global> | cpp/unbounded-write | 67 | FP | FP | 代码在调用strcpy前，已通过strlen(canon)计算了所需缓冲区大小，并检查了need > buflen，确保了目标缓冲区buf有足够空间，因此不存在缓冲区溢出风险。 |
| 1391 | musl-1.2.3 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 在调用strcpy前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1392 | musl-1.2.3 | <global> | cpp/unbounded-write | 10 | FP | FP | 函数 `getlogin_r` 在调用 `strcpy` 前，已通过 `if (strlen(logname) >= size) return ERANGE;` 检查了源字符串长度是否小于目标缓冲区大小 `size`，确保了复制操作不... |
| 1393 | musl-1.2.2 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 代码中分配的内存大小（sizeof *f + UNGET + BUFSIZ）用于创建FILE结构体及其缓冲区，该计算方式符合musl库的内部实现逻辑，是正确且安全的，并非可疑的内存分配。 |
| 1394 | musl-1.2.2 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat前，代码已通过if (scopeid)确保p非空，且p指向的字符串长度有限（来自itoa或if_indextoname），同时buf的大小为256，足以容纳inet_ntop的输出和追加的scope标识符，因此不会发... |
| 1395 | musl-1.2.2 | load_library | cpp/unbounded-write | 1161 | FP | FP | 目标缓冲区 `p->name` 的大小为 `alloc_size`，其中 `alloc_size = sizeof *p + strlen(pathname) + 1`，而 `strcpy(p->name, pathname)` 复制... |
| 1396 | musl-1.2.2 | <global> | cpp/unbounded-write | 67 | FP | FP | 代码在调用strcpy前，已通过strlen(canon)计算了所需缓冲区大小，并检查了need > buflen，确保目标缓冲区buf有足够空间容纳canon字符串，因此不存在缓冲区溢出风险。 |
| 1397 | musl-1.2.2 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 代码在调用strcpy前，已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`和`if (strlen(p) >= servlen) return EAI_OVERFLOW;`进行... |
| 1398 | musl-1.2.2 | <global> | cpp/unbounded-write | 10 | FP | FP | 函数 `getlogin_r` 在调用 `strcpy` 前，已通过 `if (strlen(logname) >= size) return ERANGE;` 检查了目标缓冲区 `name` 的大小 `size` 是否足以容纳源字符... |
| 1399 | musl-1.2.1 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 分配的内存大小（sizeof *f + UNGET + BUFSIZ）是结构体FILE、UNGET常量和BUFSIZ常量的总和，这是一个经过设计的、用于分配包含额外缓冲区的FILE对象的内存布局，并非错误的分配大小。 |
| 1400 | musl-1.2.1 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat前，代码已通过if (scopeid)确保p非空，且p指向的缓冲区（tmp或num）大小有限且内容受控。strcat的目标缓冲区buf在拼接前已通过inet_ntop填充了IP地址字符串，其大小（256字节）和拼接后... |
| 1401 | musl-1.2.1 | load_library | cpp/unbounded-write | 1138 | FP | FP | strcpy的目标缓冲区p->name的大小为alloc_size，该值由strlen(pathname) + 1计算得出，并已通过calloc分配，因此复制操作不会导致缓冲区溢出。 |
| 1402 | musl-1.2.1 | <global> | cpp/unbounded-write | 67 | FP | FP | 代码在调用strcpy前已通过strlen(canon)计算了所需缓冲区大小，并检查了need > buflen，确保目标缓冲区buf有足够空间容纳canon字符串，因此不存在缓冲区溢出风险。 |
| 1403 | musl-1.2.1 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 在调用strcpy前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`检查了目标缓冲区大小，确保了不会发生溢出。 |
| 1404 | musl-1.2.1 | <global> | cpp/unbounded-write | 10 | FP | FP | 代码在调用strcpy前，已通过`if (strlen(logname) >= size) return ERANGE;`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1405 | musl-1.1.24 | getname | cpp/offset-use-before-range-check | 89 | FP | FP | 循环条件 `i<TZNAME_MAX` 在访问 `(*p)[i]` 之前进行了检查，确保了索引 `i` 在有效范围内，因此不存在越界访问的风险。 |
| 1406 | musl-1.1.24 | getname | cpp/offset-use-before-range-check | 93 | FP | FP | 循环条件 `i<TZNAME_MAX` 已确保索引 `i` 在访问数组 `d` 和 `(*p)` 前得到范围检查，不会发生越界访问。 |
| 1407 | musl-1.1.24 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 分配的内存大小（sizeof *f + UNGET + BUFSIZ）是结构体FILE、UNGET空间和缓冲区BUFSIZ的精确总和，这是实现中为FILE结构体和其内联缓冲区分配内存的常见且正确的模式，并非可疑的大小不匹配。 |
| 1408 | musl-1.1.24 | getnameinfo | cpp/unsafe-strcat | 178 | FP | FP | 在调用strcat之前，代码已通过`if (scopeid)`确保p非空，且p指向的字符串长度有限（来自itoa或if_indextoname），同时buf的大小为256字节，其当前内容（inet_ntop生成的地址）长度可控，拼接后... |
| 1409 | musl-1.1.24 | load_library | cpp/unbounded-write | 1133 | FP | FP | strcpy的目标缓冲区p->name的大小为alloc_size，该值基于strlen(pathname)+1计算，且pathname在复制前已通过路径搜索和长度检查（如strlen(name) > NAME_MAX），因此复制操作... |
| 1410 | musl-1.1.24 | <global> | cpp/unbounded-write | 67 | FP | FP | 在调用strcpy前，代码已通过strlen(canon)计算了所需缓冲区大小，并检查了need > buflen，确保了目标缓冲区buf有足够空间容纳canon字符串，因此不存在缓冲区溢出风险。 |
| 1411 | musl-1.1.24 | getnameinfo | cpp/unbounded-write | 182 | FP | FP | 在调用strcpy前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`进行了长度检查，确保目标缓冲区node有足够空间，因此不存在缓冲区溢出风险。 |
| 1412 | musl-1.1.24 | <global> | cpp/unbounded-write | 10 | FP | FP | 代码在调用strcpy前，已通过`if (strlen(logname) >= size) return ERANGE;`检查了源字符串长度是否小于目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1413 | musl-1.2.4 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 分配的内存大小（sizeof *f + UNGET + BUFSIZ）用于为FILE结构体、反推缓冲区（UNGET）和主缓冲区（BUFSIZ）分配连续空间，这是musl libc中FILE实现的惯用模式，内存布局经过精确计算，并非错误... |
| 1414 | musl-1.2.4 | getnameinfo | cpp/unsafe-strcat | 180 | FP | FP | 在调用strcat前，代码已通过inet_ntop将IP地址格式化到buf中，其长度受限于IPv6地址的最大长度（INET6_ADDRSTRLEN），且后续拼接的scopeid字符串由itoa生成或来自if_indextoname，长... |
| 1415 | musl-1.2.4 | load_library | cpp/unbounded-write | 1224 | FP | FP | strcpy的目标缓冲区p->name的大小为alloc_size，该值由strlen(pathname) + 1计算得出，且已通过calloc分配，因此复制操作不会导致缓冲区溢出。 |
| 1416 | musl-1.2.4 | <global> | cpp/unbounded-write | 69 | FP | FP | 代码在调用strcpy前已通过need计算确保目标缓冲区大小足够，且canon数组大小固定为256字节，其内容由__lookup_name函数内部安全处理，不会导致缓冲区溢出。 |
| 1417 | musl-1.2.4 | getnameinfo | cpp/unbounded-write | 184 | FP | FP | 在调用strcpy前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1418 | musl-1.2.4 | <global> | cpp/unbounded-write | 10 | FP | FP | 函数 `getlogin_r` 在调用 `strcpy` 前，已通过 `if (strlen(logname) >= size) return ERANGE;` 检查了目标缓冲区 `name` 的大小 `size` 是否足以容纳源字符... |
| 1419 | tmux-3.4 | <global> | cpp/overflow-buffer | 67 | FP | FP | 代码在访问 `place[1]` 之前，已通过条件 `*(place = nargv[BSDoptind]) != '-'` 确保 `place` 指向以 '-' 开头的字符串，且随后检查 `place[1] && *++place ... |
| 1420 | tmux-3.4 | <global> | cpp/overflow-buffer | 68 | FP | FP | 告警点 `place[1]` 的访问是安全的，因为在前一行 `if (place[1] && *++place == '-')` 中已确保 `place[1]` 非空（即不为 '\0'），才进入该代码块。切片内可见的上下文逻辑保证了数... |
| 1421 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 700 | FP | FP | 告警点位于对 `help->org.params` 的赋值语句，但切片代码显示 `help` 指针在函数入口处通过 `help = next++` 被正确初始化，且 `next` 作为参数传入，不存在空指针解引用。工具可能误判了赋值操... |
| 1422 | redis-7.0.11 | breakstat | Dereference of null pointer | 986 | FP | FP | 在调用 `luaK_codeABC` 前，代码已通过 `while` 循环确保 `bl` 指向一个可中断的块（`isbreakable` 为真），因此 `bl` 不可能为空指针，告警为误报。 |
| 1423 | redis-7.0.11 | xgroupCommand | Dereference of null pointer | 2700 | FP | FP | 告警点 `cg->last_id = id;` 位于 `SETID` 子命令分支，该分支仅在 `cg` 指针非空时执行。切片代码显示，`cg` 指针在 `SETID` 分支之前已通过 `streamCreateCG` 创建或通过 `r... |
| 1424 | redis-7.0.11 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1626 | FP | FP | 告警点调用的`sdsfree`函数内部已包含对空指针的检查（`if (s == NULL) return;`），因此即使`state->lines[linenum]`为NULL也不会导致空指针解引用，代码是安全的。 |
| 1425 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在访问 `specs->element[j]->str` 和 `specs->element[j+1]` 之前，已通过 `assert` 语句确保 `specs->type` 为 `REDIS_REPLY_MAP` 或 ... |
| 1427 | redis-7.0.11 | dictGetRandomKey | Dereference of null pointer | 682 | FP | FP | 切片代码显示，在获取`he`指针的循环中，`do...while(he == NULL)`保证了`he`在进入后续链表遍历逻辑前非空。后续的`while(he)`循环也确保了`listlen`至少为1，因此`he = he->next... |
| 1428 | redis-7.0.11 | cliConcatArguments | Dereference of null pointer | 542 | FP | FP | 告警点位于循环条件 `arguments->elements` 的访问，但切片代码显示 `arguments` 指针在 `cliAddArgument` 函数中已通过类型检查（`argMap->type != REDIS_REPLY_... |
| 1429 | redis-7.0.11 | rewriteConfigRewriteLine | Dereference of null pointer | 1236 | FP | FP | 在调用 `sdsfree(state->lines[linenum])` 前，代码已通过 `if (l)` 检查确保 `l` 非空，并通过 `listFirst(l)` 获取 `ln`，且 `linenum` 是从 `ln->valu... |
| 1430 | redis-7.0.11 | sdscat_orempty | Dereference of null pointer | 532 | FP | FP | 告警点检查的是指针`value`指向的字符数组的第一个字符，而非解引用`value`指针本身。`value`作为函数参数传入，在调用前已存在，切片中虽未显示其来源，但函数签名和用法表明它是一个有效的字符串指针，解引用其索引`[0]`是... |
| 1432 | redis-7.0.11 | cliInitGroupHelpEntries | Dereference of null pointer | 771 | FP | FP | 告警点 `helpEntries[pos++] = tmp;` 中，`helpEntries` 数组的声明和初始化未在切片中提供，无法判断其是否为空指针。但结合上下文，`pos` 初始化为 `helpEntriesLen`（全局变量，... |
| 1433 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 688 | FP | FP | 切片代码显示，在访问 `reply->str` 之前，已通过 `assert(reply->type == REDIS_REPLY_STRING)` 断言确保 `reply` 的类型正确，这保证了 `reply->str` 是有效的字... |
| 1435 | redis-7.0.11 | _quicklistListpackMerge | Dereference of null pointer | 813 | FP | FP | 告警点 `if (!a->entry)` 是在 `lpMerge` 函数成功返回后才执行的，`lpMerge` 函数内部已对空指针进行了检查并返回 NULL，因此 `a->entry` 和 `b->entry` 在进入该条件分支时至少... |
| 1436 | redis-7.0.11 | xgroupCommand | Dereference of null pointer | 2696 | FP | FP | 在SETID子命令中，当参数为'$'时，代码`id = s->last_id;`访问`s->last_id`。变量`s`在之前的代码路径中通过`lookupKeyWrite`查找并赋值，如果键不存在则`s`为NULL。但告警所在分支`... |
| 1437 | redis-7.0.11 | cliOldInitHelp | Dereference of null pointer | 455 | FP | FP | 切片代码显示 `zmalloc` 在分配失败时会调用 `zmalloc_oom_handler` 处理内存不足，不会返回空指针给 `tmp.argv`，因此 `tmp.argv[0]` 的赋值是安全的，不存在空指针解引用。 |
| 1438 | redis-7.0.11 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 切片代码显示，在访问 `quicklist->head` 和 `quicklist->tail` 之前，函数已通过 `if (quicklist->len == 0) return;` 确保链表非空，且 `assert` 语句进一步确... |
| 1439 | redis-7.0.11 | getKeySizes | Dereference of null pointer | 8193 | FP | FP | 切片代码显示，在解引用 `types[i]` 之前，已通过条件 `if(!types[i] ｜｜ ...)` 进行了空指针检查，若其为空则跳过后续操作，因此不会发生空指针解引用。 |
| 1440 | redis-7.0.11 | json_next_token | Dereference of null pointer | 1022 | FP | FP | 切片代码显示，在访问 `ch2token[ch]` 之前，`ch` 的值来自 `*(json->ptr)`，而 `json->ptr` 在循环中通过 `json->ptr++` 递增，但始终指向 `json->data` 缓冲区内的有... |
| 1441 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 684 | FP | FP | 切片代码显示，在访问 `help->org.summary` 之前，`help` 指针已在函数开头通过 `help = next++` 明确赋值，且 `next` 作为参数传入，不存在空指针解引用。告警为误报。 |
| 1442 | redis-7.0.11 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 在调用 `forward->next` 之前，代码已通过 `if (forward == reverse ｜｜ forward->next == reverse)` 检查了 `forward->next` 是否等于 `reverse`... |
| 1443 | redis-7.0.11 | _quicklistListpackMerge | Dereference of null pointer | 820 | FP | FP | 在`lpMerge`函数成功返回后，`keep`指针指向的节点（`a`或`b`）的`entry`字段已被确保为非空，因为`lpMerge`仅在两个输入`entry`都非空时才会成功。因此，调用`lpLength(keep->entry... |
| 1444 | redis-7.0.11 | moduleFreeContext | Dereference of null pointer | 748 | FP | FP | 告警点位于 `serverLog` 函数调用处，但该调用仅在 `ctx->postponed_arrays` 非空时执行。切片显示 `zfree` 函数内部已对空指针进行检查（`if (ptr == NULL) return;`），因... |
| 1445 | redis-7.0.11 | extent_try_coalesce_impl | Dereference of null pointer | 1666 | FP | FP | 告警指向的代码行 `*coalesced = false;` 是对一个非空指针的写入操作。`coalesced` 是函数的入参指针，在函数入口处已存在，且切片中未显示其可能为空。该行是安全的赋值语句，不存在空指针解引用。 |
| 1446 | redis-7.0.11 | streamPropagateXCLAIM | Dereference of null pointer | 1564 | FP | FP | 告警点访问 nack->consumer->name，但切片中未提供 nack 或 consumer 的赋值或校验信息，无法确认其是否为 null。然而，考虑到该函数是 Redis 内部传播命令的核心函数，且对 argv[3] 等对象... |
| 1447 | redis-7.0.11 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 告警点 'h->isnull = 1;' 处的指针 'h' 在切片代码中已被检查并重新赋值（例如通过 raxReallocForData 或 raxAddChild 等函数），且其来源（如 'h = child;'）表明它指向有效的内... |
| 1448 | redis-7.0.11 | extent_try_coalesce_impl | Dereference of null pointer | 1636 | FP | FP | 告警点位于对指针 `coalesced` 的赋值语句，该指针作为函数参数传入，在函数内部所有使用路径中，`coalesced` 均被明确赋值（true 或 false），不存在空指针解引用。切片代码已包含所有对 `coalesced`... |
| 1449 | redis-7.0.11 | clusterManagerAddSlots | Dereference of null pointer | 3898 | FP | FP | 告警指向的代码行 `*err = NULL;` 是对指针 `err` 的解引用，但切片显示 `err` 是函数参数，在调用前已被检查（`if (err != NULL)`），且函数 `clusterManagerAddSlots` 的... |
| 1450 | redis-7.0.11 | min_expand | Dereference of null pointer | 322 | FP | FP | 告警行检查了 `s < ms->src_end` 条件，确保指针 `s` 在解引用 `*s` 之前不会越界，因此不会发生空指针解引用。 |
| 1451 | redis-7.0.11 | strbuf_init | Dereference of null pointer | 53 | FP | FP | 代码中`s->buf = NULL;`是对结构体指针`s`的成员进行赋值，并非解引用空指针。该操作是安全的初始化行为，工具报告的逻辑错误不成立。 |
| 1452 | redis-7.0.11 | strbuf_ensure_null | Dereference of null pointer | 142 | FP | FP | 函数 `strbuf_ensure_null` 的目的是在缓冲区末尾写入一个空字符，其逻辑依赖于调用者确保 `s->buf` 和 `s->length` 的有效性。切片代码本身没有显示空指针解引用，该告警可能是工具对缓冲区索引操作 `... |
| 1453 | redis-7.0.11 | checkMultiPartAof | Dereference of null pointer | 474 | FP | FP | 告警点位于条件判断 `if (listLength(am->incr_aof_list))`，但在此之前已存在对 `am->incr_aof_list` 的访问 `if (am->incr_aof_list) total_num +=... |
| 1454 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2541 | FP | FP | 告警点 `dictPauseAutoResize(dstzset->dict)` 中 `dstzset->dict` 不可能为空指针。在 `j == 0` 的分支中，`dstzset->dict` 已通过 `dictAdd` 被使用，... |
| 1455 | redis-7.4.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2891 | FP | FP | 告警点位于条件判断 `if (dstzset->zsl->length)`，但切片代码显示 `dstzset` 变量未定义，其来源和赋值在切片中完全缺失，无法判断其是否为空指针。 |
| 1456 | redis-7.4.2 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 代码中`s->buf = NULL;`是对结构体指针`s`的成员进行赋值，并非解引用空指针。该操作是安全的初始化，工具报告的逻辑错误不成立。 |
| 1457 | redis-7.4.2 | breakstat | Dereference of null pointer | 986 | FP | FP | 告警点位于条件语句 `if (upval)` 内部，`bl` 指针在 while 循环中被赋值，且循环条件 `while (bl && !bl->isbreakable)` 保证了退出循环时 `bl` 非空，因此 `bl->nactv... |
| 1458 | redis-7.4.2 | xgroupCommand | Dereference of null pointer | 2711 | FP | FP | 告警点 `cg->last_id = id;` 位于 `SETID` 子命令分支，该分支仅在 `cg` 指针非空时执行。切片代码显示 `cg` 由 `streamCreateCG` 创建或通过 `raxFind` 查找，在 `SETI... |
| 1459 | redis-7.4.2 | dictGenericDelete | Dereference of null pointer | 628 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，已通过 `dictSize(d) == 0` 检查字典非空，并通过 `idx = h & DICTHT_SIZE_MASK(d->ht_size_exp[... |
| 1460 | redis-7.4.2 | zdiffAlgorithm1 | Dereference of null pointer | 2497 | FP | FP | 告警点位于 `zslInsert` 调用处，该函数内部有 `serverAssert(!isnan(score));` 断言，且 `zval.score` 来源于 `zuiNext` 函数，该函数对有序集合会返回节点的 `score`... |
| 1461 | redis-7.4.2 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1634 | FP | FP | 告警点 `sdsfree(state->lines[linenum])` 中的 `state->lines` 指针在函数入口处未被检查，但 `state` 参数由调用者传入，其有效性是函数契约的一部分。切片中 `state->opti... |
| 1462 | redis-7.4.2 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `*coalesced = false;` 是对布尔指针的赋值操作，`coalesced` 指针作为函数参数传入，在函数内部多个条件分支中已被赋值，其本身不可能为 NULL。该行是安全的指针解引用，工具报告的逻辑错误... |
| 1463 | redis-7.4.2 | clusterSendPing | Dereference of null pointer | 3650 | FP | FP | 告警行 `link->node->ping_sent = mstime();` 位于条件 `if (!link->inbound && type == CLUSTERMSG_TYPE_PING)` 内部，切片代码显示 `link` 是... |
| 1465 | redis-7.4.2 | dictGetVal | Dereference of null pointer | 887 | FP | FP | 函数 `dictGetVal` 接收一个指向 `dictEntry` 的指针 `de`，并直接返回其成员 `v.val`。这是一个简单的访问器函数，其安全性完全依赖于调用方传入的指针 `de` 是否为 NULL。函数本身没有空指针检查... |
| 1466 | redis-7.4.2 | dictFind | Dereference of null pointer | 762 | FP | FP | 在访问 `d->ht_table[table][idx]` 之前，代码已通过 `dictSize(d) == 0` 检查字典非空，并且在循环中 `idx` 的计算和 `table` 的取值均受控，切片内未发现导致空指针解引用的逻辑错误... |
| 1467 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12395 | FP | FP | 告警指向的代码行是对指针 `module` 的成员 `usedby` 的访问，但切片代码显示，在访问 `module->usedby` 之前，已经通过 `if (module == NULL)` 检查并处理了 `module` 为 N... |
| 1468 | redis-7.4.2 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 告警指向的代码行 `*coalesced = true;` 是对非空指针 `coalesced` 的解引用，该指针作为函数参数传入，在切片代码的调用上下文中已被使用且未被置空，不存在空指针解引用风险。 |
| 1470 | redis-7.4.2 | RM_ListInsert | Dereference of null pointer | 4665 | FP | FP | 告警点位于函数调用 `listTypeTryConversionAppend`，其参数 `key->value` 在 `moduleListIteratorSeek` 函数中有明确的非空检查（`if (!key->value ｜｜ k... |
| 1471 | redis-7.4.2 | cliInitGroupHelpEntries | Dereference of null pointer | 728 | FP | FP | 切片代码显示，`helpEntries` 数组的索引 `pos` 初始化为 `helpEntriesLen`，并在循环中递增。虽然切片未显示 `helpEntries` 的声明和大小，但告警点 `helpEntries[pos++] ... |
| 1472 | redis-7.4.2 | cliFillInCommandHelpEntry | Dereference of null pointer | 588 | FP | FP | 切片代码显示，`help->argc` 在传递给 `zmalloc` 前已被明确赋值（1或2），`zmalloc` 函数内部有内存分配失败的处理机制（`zmalloc_oom_handler`），因此不存在对空指针的解引用。告警为逻辑误判。 |
| 1473 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12388 | FP | FP | 代码逻辑正确，当`module`为NULL时，直接返回错误，不会发生空指针解引用。告警点`*errmsg = "no such module..."`是在`module == NULL`的判断分支内执行的，此时`errmsg`指针本身... |
| 1475 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2559 | FP | FP | 告警点位于dictShrinkIfNeeded函数调用，该函数内部已对传入的dstzset->dict指针进行了空指针检查（通过dictIsRehashing等宏），且切片代码显示dstzset在函数开头作为参数传入，并在循环中被di... |
| 1476 | redis-7.4.2 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在解引用 oldlenp 前已检查其是否为 NULL。切片代码显示，在调用 VERIFY_READ 之前，函数已通过 READONLY 宏确保 newp 和 newlen 为 NULL/... |
| 1477 | redis-7.4.2 | xgroupCommand | Dereference of null pointer | 2707 | FP | FP | 在SETID子命令中，对`s->last_id`的访问发生在`s`指针非空的条件下。代码逻辑显示，当`s`为NULL时，会通过`mkstream`选项创建新的流对象，或者命令会提前返回，因此不会发生空指针解引用。 |
| 1478 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12391 | FP | FP | 告警点位于对 `module->types` 的访问，但切片代码显示，在访问 `module->types` 之前，已通过 `if (module == NULL)` 检查了指针 `module` 是否为 NULL。只有当 `modu... |
| 1479 | redis-7.4.2 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 代码在解引用 `quicklist->head` 和 `quicklist->tail` 之前，已通过 `if (quicklist->len == 0) return;` 确保了链表非空，因此 `head` 和 `tail` 指针不... |
| 1480 | redis-7.4.2 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警位于宏 VERIFY_READ 的调用处，该宏检查 oldp 和 oldlenp 是否为 NULL 或长度不匹配，若条件成立则设置错误码并跳转返回，不会发生空指针解引用。代码逻辑确保了安全访问。 |
| 1481 | redis-7.4.2 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 切片代码显示，在访问 `ch2token[ch]` 之前，`ch` 已从 `json->ptr` 解引用赋值，且 `json->ptr` 在循环中通过 `json->ptr++` 递增，确保了指针的有效性。告警点 `ch2token`... |
| 1482 | redis-7.4.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2874 | FP | FP | 切片代码显示，在调用 `dictExpand(dstzset->dict,dictSize(accumulator));` 之前，`dstzset` 已通过 `dstobj = createZsetObject();` 和 `dstz... |
| 1483 | redis-7.4.2 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 在条件 `if (forward == reverse ｜｜ forward->next == reverse)` 中，`forward` 和 `reverse` 指针在循环前已分别初始化为非空的 `quicklist->head` ... |
| 1484 | redis-7.4.2 | _quicklistListpackMerge | Dereference of null pointer | 882 | FP | FP | 告警点 `keep->count = lpLength(keep->entry);` 位于条件分支 `if ((lpMerge(&a->entry, &b->entry)))` 内部，且该分支内已通过 `if (!a->entry)`... |
| 1485 | redis-7.4.2 | moduleFreeContext | Dereference of null pointer | 815 | FP | FP | 在调用 `zfree` 之前，代码通过 `if (ctx->postponed_arrays)` 检查了指针是否为空，而 `zfree` 函数内部也有 `if (ptr == NULL) return;` 的空指针检查，因此不会发生空... |
| 1486 | redis-7.4.2 | rewriteConfigRewriteLine | Dereference of null pointer | 1243 | FP | FP | 在调用 `sdsfree(state->lines[linenum])` 之前，代码已通过 `if (l)` 检查确保 `l` 非空，并通过 `listFirst(l)` 获取了 `ln`，且 `linenum` 是从 `ln->va... |
| 1487 | redis-7.4.2 | raxGenericInsert | Dereference of null pointer | 869 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该分支仅在 `h->size` 为 0 时执行。根据切片代码，`h` 是 `raxReallocForData` 的返回值，该函数在 `data` 不为 NULL 时会... |
| 1488 | redis-7.4.2 | clusterManagerAddSlots | Dereference of null pointer | 4762 | FP | FP | 告警点 `*err = NULL;` 是对指针 `err` 进行赋值，而非解引用。该行代码是安全的初始化操作，不存在空指针解引用问题，属于静态分析工具的逻辑误判。 |
| 1489 | redis-7.4.2 | min_expand | Dereference of null pointer | 322 | FP | FP | 告警行代码 `singlematch(uchar(*s), p, ep)` 中，`s` 在调用前已通过条件 `s<ms->src_end` 检查，确保其指向有效内存，因此解引用 `*s` 不会导致空指针解引用。 |
| 1490 | redis-7.4.2 | usUntilEarliestTimer | Dereference of null pointer | 257 | FP | FP | 函数在循环中明确检查了 `te->id != AE_DELETED_EVENT_ID` 才将 `te` 赋值给 `earliest`，且循环仅在 `te` 非空时执行，因此 `earliest` 在解引用前不可能为 NULL。 |
| 1491 | redis-7.4.2 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | FP | 函数 `strbuf_ensure_null` 是一个内联静态函数，其目的是在字符串缓冲区末尾确保一个空终止符。告警行 `s->buf[s->length] = 0;` 假设 `s->buf` 指向一个至少具有 `s->length ... |
| 1492 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12399 | FP | FP | 告警指向的代码行是字符串字面量赋值给 *errmsg，并非对空指针的解引用。在函数入口处已对 module 指针进行空值检查，并仅在为 NULL 时对 *errmsg 赋值，此时 errmsg 参数本身非空，因此该行不存在空指针解引用风险。 |
| 1493 | redis-7.4.2 | checkMultiPartAof | Dereference of null pointer | 488 | FP | FP | 告警点位于条件判断 `if (listLength(am->incr_aof_list))`，但在此之前已存在对 `am->incr_aof_list` 的访问 `if (am->incr_aof_list) total_num +=... |
| 1494 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12403 | FP | FP | 告警指向的代码行是字符串字面量赋值给 `*errmsg`，并非对空指针的解引用。`errmsg` 作为函数参数传入，在调用 `moduleUnload` 前已被分配有效地址，切片中 `module == NULL` 分支的赋值操作也证... |
| 1495 | redis-7.4.2 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查其是否为NULL，且当条件不满足时通过goto跳转，不会发生空指针解引用。 |
| 1496 | redis-7.4.2 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | 告警指向的宏 `VERIFY_READ` 在 `oldp` 或 `oldlenp` 为空时会通过 `goto label_return` 提前返回，不会发生空指针解引用。切片代码逻辑确保了指针解引用前的安全检查，因此是误报。 |
| 1497 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2537 | FP | FP | 告警指向的代码行 `znode = zslInsert(dstzset->zsl,zval.score,tmp);` 中，`zslInsert` 函数内部已通过 `serverAssert(!isnan(score));` 确保分数有... |
| 1498 | redis-7.4.2 | connClose | Dereference of null pointer | 229 | FP | FP | 切片代码显示 `conn` 指针在解引用前未进行空值检查，但 `connClose` 是一个静态内联函数，通常由调用方保证传入有效连接。函数名 `connClose` 暗示其职责是关闭一个已建立的连接，而非处理空指针。结合告警规则为逻... |
| 1500 | redis-7.2.1 | zunionInterDiffGenericCommand | Dereference of null pointer | 2818 | FP | FP | 告警点位于条件判断 `if (dstzset->zsl->length)` 中，但切片代码显示该行位于 `if (dstkey)` 条件块内，且 `dstzset` 变量未在切片中定义或赋值。结合上下文，`dstkey` 为函数参数，... |
| 1501 | redis-7.2.1 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 代码中`s->buf = NULL;`是对结构体指针`s`的成员进行赋值，并非解引用空指针。该操作是安全的初始化行为，工具报告的逻辑错误不成立。 |
| 1502 | redis-7.2.1 | breakstat | Dereference of null pointer | 986 | FP | FP | 告警点位于条件`if (upval)`内部，`bl`指针在while循环中已被确保为非空（循环条件为`bl && !bl->isbreakable`），因此当执行到`bl->nactvar`时，`bl`不可能为null。 |
| 1503 | redis-7.2.1 | xgroupCommand | Dereference of null pointer | 2697 | FP | FP | 告警点 `cg->last_id = id;` 位于 `SETID` 子命令分支，该分支仅在 `cg` 指针非空时执行。切片代码显示，`cg` 指针来源于 `streamCreateCG` 的返回值或 `raxFind` 查找，在 `... |
| 1504 | redis-7.2.1 | zdiffAlgorithm1 | Dereference of null pointer | 2432 | FP | FP | 切片代码显示，在调用 `zslInsert` 和 `dictAdd` 前，`tmp` 变量由 `zuiNewSdsFromValue` 返回，该函数保证返回有效的 sds 字符串或新分配的 sds，不会返回 NULL。因此，对 `tm... |
| 1505 | redis-7.2.1 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1643 | FP | FP | 在调用 `sdsfree(state->lines[linenum])` 前，代码已通过 `while(listLength(l))` 循环条件确保列表 `l` 非空，且 `listFirst(l)` 能成功获取节点 `ln`，这间接... |
| 1506 | redis-7.2.1 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `*coalesced = false;` 是对布尔指针 `coalesced` 的赋值，该指针作为函数参数传入，在函数内部多个分支已被赋值，因此它不可能是空指针。这是一个明显的工具误判。 |
| 1508 | redis-7.2.1 | dictGetVal | Dereference of null pointer | 805 | FP | FP | 函数 `dictGetVal` 接收一个指向 `dictEntry` 的指针 `de`，并直接返回其成员 `v.val`。这是一个简单的访问器函数，其安全性完全依赖于调用方传入的指针 `de` 是否为 NULL。从切片代码看，函数内部... |
| 1509 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12227 | FP | FP | 代码逻辑显示，在解引用指针 `module->usedby` 之前，已经通过 `if (module == NULL)` 检查了 `module` 是否为 NULL，并提前返回了错误信息。因此，当执行到 `listLength(mod... |
| 1510 | redis-7.2.1 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 告警指向的代码行 `*coalesced = true;` 中，指针 `coalesced` 是函数的传入参数，在切片代码的函数签名中已明确声明为非空指针 `bool *coalesced`，因此不可能为 NULL。这是一个明确的工具误报。 |
| 1512 | redis-7.2.1 | RM_ListInsert | Dereference of null pointer | 4585 | FP | FP | 告警行 `listTypeTryConversionAppend(key->value, ...)` 中，`key` 参数在 `moduleListIteratorSeek` 函数开头有明确的空指针检查 `if (!key) { re... |
| 1513 | redis-7.2.1 | cliInitGroupHelpEntries | Dereference of null pointer | 724 | FP | FP | 告警点 `helpEntries[pos++] = tmp;` 中，`helpEntries` 数组的声明和大小未在切片中给出，无法判断 `pos` 是否越界或 `helpEntries` 是否为 null。但根据告警规则 'Dere... |
| 1514 | redis-7.2.1 | cliFillInCommandHelpEntry | Dereference of null pointer | 584 | FP | FP | 告警点 `help->argc = subcommandname ? 2 : 1;` 是对结构体成员 `argc` 的赋值，并非解引用空指针。`help` 指针的解引用操作（`help->argv = zmalloc(...)`）发生... |
| 1515 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12220 | FP | FP | 告警行 `*errmsg = "no such module with that name";` 仅在 `module == NULL` 的条件下执行，此时对空指针 `errmsg` 的解引用是安全的，因为该指针是函数的输入参数，且在... |
| 1517 | redis-7.2.1 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在解引用 oldlenp 指针前已通过条件 `oldp == NULL ｜｜ oldlenp == NULL ｜｜ *oldlenp != sizeof(t)` 进行了检查，仅当 old... |
| 1518 | redis-7.2.1 | xgroupCommand | Dereference of null pointer | 2693 | FP | FP | 在SETID子命令中，当c->argv[4]为'$'时，访问s->last_id。切片显示，s仅在o存在且为流对象时被赋值，否则为NULL。但SETID子命令仅在c->argc >= 4时执行，且此时s可能为NULL。然而，在SETI... |
| 1519 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12223 | FP | FP | 告警指向的代码行是给指针 `errmsg` 赋值一个字符串常量，这是一个安全的写操作。`errmsg` 是函数的输入参数，其有效性由调用者保证，且切片代码中所有对 `*errmsg` 的赋值都在 `module` 为 NULL 或错误... |
| 1520 | redis-7.2.1 | __quicklistCompress | Dereference of null pointer | 313 | FP | FP | 代码在访问 `quicklist->head` 和 `quicklist->tail` 前，已通过 `if (quicklist->len == 0) return;` 确保链表非空，因此 `head` 和 `tail` 指针非空，`... |
| 1521 | redis-7.2.1 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警指向的宏 VERIFY_READ 在展开后对 oldlenp 进行了空指针解引用检查，但该检查位于条件判断 `oldp == NULL ｜｜ oldlenp == NULL ｜｜ *oldlenp != sizeof(t)` 中，... |
| 1522 | redis-7.2.1 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 代码在访问 `ch2token[ch]` 前，已通过 `ch = (unsigned char)*(json->ptr);` 对 `json->ptr` 进行了解引用，但 `json->ptr` 在循环中会递增，且循环条件 `whil... |
| 1523 | redis-7.2.1 | zunionInterDiffGenericCommand | Dereference of null pointer | 2801 | FP | FP | 切片代码显示，在调用 `dictExpand(dstzset->dict, dictSize(accumulator));` 之前，`dstzset` 已通过 `dstobj = createZsetObject();` 和 `dst... |
| 1524 | redis-7.2.1 | __quicklistCompress | Dereference of null pointer | 366 | FP | FP | 告警行代码 `if (forward == reverse ｜｜ forward->next == reverse)` 在访问 `forward->next` 前，已通过循环条件 `depth++ < quicklist->compr... |
| 1525 | redis-7.2.1 | _quicklistListpackMerge | Dereference of null pointer | 827 | FP | FP | 告警点 `keep->count = lpLength(keep->entry);` 中，`keep` 指针在之前的条件分支中已被明确赋值为 `a` 或 `b`，而 `a` 和 `b` 是函数的非空参数，因此 `keep` 不可能为空... |
| 1526 | redis-7.2.1 | moduleFreeContext | Dereference of null pointer | 816 | FP | FP | 告警指向的代码行是 `serverLog` 函数调用，该行本身不会解引用空指针。对 `ctx->postponed_arrays` 的访问和传递给 `zfree` 的操作，均在 `if (ctx->postponed_arrays)`... |
| 1527 | redis-7.2.1 | rewriteConfigRewriteLine | Dereference of null pointer | 1252 | FP | FP | 在 `if (l)` 条件块内，`ln` 通过 `listFirst(l)` 获取，`l` 非空保证了 `ln` 非空，因此 `ln->value` 的访问是安全的。告警的逻辑前提不成立。 |
| 1528 | redis-7.2.1 | zsetRemoveFromSkiplist | Dereference of null pointer | 1502 | FP | FP | 告警行 `de = dictUnlink(zs->dict,ele);` 的返回值 `de` 在后续条件 `if (de != NULL)` 中被显式检查，仅在非空时才被解引用。代码逻辑正确，不存在空指针解引用。 |
| 1529 | redis-7.2.1 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该分支仅在 `h->size` 为 0 时执行。切片代码显示，在进入此分支前，`h` 已通过 `raxAddChild` 或 `raxCompressNode` 等函数... |
| 1530 | redis-7.2.1 | clusterManagerAddSlots | Dereference of null pointer | 4641 | FP | FP | 告警指向的代码行 `*err = NULL;` 是对指针 `err` 的解引用，但切片代码显示，在函数入口处 `err` 作为参数传入，其值由调用方决定，并非必然为空。此外，后续调用 `clusterManagerCheckRedis... |
| 1531 | redis-7.2.1 | min_expand | Dereference of null pointer | 322 | FP | FP | 告警行代码 `singlematch(uchar(*s), p, ep)` 中，指针 `s` 在解引用前已通过条件 `s<ms->src_end` 进行了边界检查，确保了 `s` 指向有效内存，因此不会发生空指针解引用。 |
| 1532 | redis-7.2.1 | usUntilEarliestTimer | Dereference of null pointer | 276 | FP | FP | 代码逻辑确保了earliest指针在循环后不为空。循环仅在te不为空时执行，且循环内只有当te->id != AE_DELETED_EVENT_ID时才会将earliest赋值为te，如果所有事件都被标记为删除，earliest将保持... |
| 1533 | redis-7.2.1 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | FP | 函数 `strbuf_ensure_null` 是一个内联静态函数，其目的是在缓冲区末尾写入空字符以确保字符串以 null 结尾。调用此函数时，参数 `s` 及其成员 `buf` 和 `length` 应已由调用方正确初始化并确保 `... |
| 1534 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12231 | FP | FP | 切片代码显示，在访问 `module->blocked_clients` 之前，已经通过 `if (module == NULL)` 检查确保了 `module` 指针非空。因此，后续对 `module` 结构体成员的访问是安全的，不... |
| 1535 | redis-7.2.1 | checkMultiPartAof | Dereference of null pointer | 478 | FP | FP | 告警点位于条件判断 `if (listLength(am->incr_aof_list))`，但在此之前已存在 `if (am->incr_aof_list) total_num += listLength(am->incr_aof_... |
| 1536 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12235 | FP | FP | 告警指向的代码行是字符串字面量赋值给 *errmsg，并非对空指针的解引用。函数在 module 为 NULL 时已提前返回，后续对 module 指针的访问（如 module->types）都发生在 module 非空的条件下，切片... |
| 1537 | redis-7.2.1 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在解引用 oldlenp 前已检查 oldp 和 oldlenp 是否为 NULL。若任一为 NULL，宏会设置错误码并跳转返回，不会发生空指针解引用。因此，该告警是误报。 |
| 1538 | redis-7.2.1 | zdiffAlgorithm2 | Dereference of null pointer | 2492 | FP | FP | 告警行 `if (htNeedsResize(dstzset->dict)) dictResize(dstzset->dict);` 中，`dstzset` 及其 `dict` 字段在函数开始时已作为非空参数传入，且在函数内部通过 `... |
| 1539 | redis-7.2.1 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查其不为NULL，且告警点位于宏展开后的条件判断内，该条件已确保指针非空，因此不会发生空指针解引用。 |
| 1540 | redis-7.2.1 | zdiffAlgorithm2 | Dereference of null pointer | 2472 | FP | FP | 告警点位于 `zslInsert(dstzset->zsl,zval.score,tmp)`，但切片代码显示 `dstzset` 是函数参数，其 `zsl` 成员在调用前已由调用方初始化。`zslInsert` 函数内部有 `serv... |
| 1542 | redis-7.2.5 | zunionInterDiffGenericCommand | Dereference of null pointer | 2819 | FP | FP | 告警点位于条件判断 `if (dstzset->zsl->length)` 中，但切片代码显示 `dstzset` 变量未定义，且其来源 `dstobj` 在告警点之前的代码中未出现。然而，告警点位于 `if (dstkey)` 条件... |
| 1543 | redis-7.2.5 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 代码中`s->buf = NULL;`是对结构体指针`s`的成员进行赋值，并非解引用空指针。该操作是安全的初始化，工具报告的逻辑错误不成立。 |
| 1544 | redis-7.2.5 | breakstat | Dereference of null pointer | 986 | FP | FP | 告警点位于条件`if (upval)`内部，`bl`指针已在while循环中被赋值，且循环条件`while (bl && !bl->isbreakable)`确保循环退出时`bl`非空或为NULL。若`bl`为NULL，则`if (u... |
| 1545 | redis-7.2.5 | xgroupCommand | Dereference of null pointer | 2697 | FP | FP | 在SETID子命令分支中，cg指针的使用前有明确的检查：cg = streamCreateCG(...) 或 cg = raxFind(...)，并且只有在cg非空时才会进入该分支。告警行`cg->last_id = id;`位于`e... |
| 1546 | redis-7.2.5 | zdiffAlgorithm1 | Dereference of null pointer | 2433 | FP | FP | 告警点位于 `zslInsert(dstzset->zsl,zval.score,tmp)`，切片代码显示 `dstzset` 是函数参数，`zsl` 是其成员。调用 `zslInsert` 前，`dstzset` 已在函数外部被正确... |
| 1547 | redis-7.2.5 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1643 | FP | FP | 切片代码显示，在调用 `sdsfree(state->lines[linenum])` 之前，`state->lines` 数组的访问索引 `linenum` 的来源和有效性未在切片中提供，但告警点 `sdsfree` 函数内部已包含... |
| 1548 | redis-7.2.5 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `*coalesced = false;` 中，指针 `coalesced` 是函数的传入参数，在函数入口处已被使用（`*coalesced = true;`），表明其非空。切片代码中未发现任何将其置为空的逻辑，因此... |
| 1550 | redis-7.2.5 | dictGetVal | Dereference of null pointer | 805 | FP | FP | 函数 `dictGetVal` 的参数 `de` 是一个指向 `dictEntry` 的指针，其调用方应保证传入非空。该函数本身是简单的取值操作，若调用方传入空指针，则问题根源在调用方而非此函数。静态分析工具将此函数单独切片告警属于误... |
| 1551 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12235 | FP | FP | 告警指向的代码行是对指针 `module` 的成员 `usedby` 的访问，但切片代码显示，在访问 `module->usedby` 之前，已经通过 `if (module == NULL)` 检查了指针为空的情况，并提前返回。因此... |
| 1552 | redis-7.2.5 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 告警点位于对指针 `coalesced` 的赋值语句，切片代码显示 `coalesced` 是函数的传入参数，其来源在切片内不可见，但该行代码是安全的赋值操作，不存在对空指针的解引用。工具可能误判了控制流或指针状态。 |
| 1554 | redis-7.2.5 | RM_ListInsert | Dereference of null pointer | 4585 | FP | FP | 告警行 `listTypeTryConversionAppend(key->value, ...)` 中，`key->value` 的访问发生在 `moduleListIteratorSeek` 函数对 `key` 和 `key->v... |
| 1555 | redis-7.2.5 | cliInitGroupHelpEntries | Dereference of null pointer | 724 | FP | FP | 切片代码显示，`helpEntries` 数组的索引 `pos` 由静态变量 `helpEntriesLen` 初始化，并在循环中递增。切片中未提供 `helpEntries` 数组的定义或大小，无法判断 `pos` 是否会越界或导致... |
| 1556 | redis-7.2.5 | cliFillInCommandHelpEntry | Dereference of null pointer | 584 | FP | FP | 告警点 `help->argc = subcommandname ? 2 : 1;` 是对结构体成员 `argc` 的赋值操作，并非对空指针的解引用。`help` 指针的解引用发生在该赋值语句之前，而切片中未显示 `help` 的来源... |
| 1557 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12228 | FP | FP | 告警指向的代码行 `*errmsg = "no such module with that name";` 仅在 `module == NULL` 时执行，此时对空指针 `errmsg` 的解引用是安全的，因为 `errmsg` 是函... |
| 1559 | redis-7.2.5 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在解引用 oldlenp 前已检查其不为 NULL。切片代码显示，宏 VERIFY_READ 的条件为 `if (oldp == NULL ｜｜ oldlenp == NULL ｜｜ *... |
| 1560 | redis-7.2.5 | xgroupCommand | Dereference of null pointer | 2693 | FP | FP | 告警点 `id = s->last_id;` 位于 `SETID` 子命令分支，该分支仅在 `s` 不为 NULL 时才会执行。切片代码显示，`s` 在 `lookupKeyWrite` 成功或 `mkstream` 为真时会被正确赋... |
| 1561 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12231 | FP | FP | 告警指向的代码行是字符串字面量赋值给指针，并非解引用空指针。`*errmsg = "the module exports one or more module-side data ..."` 中的 `errmsg` 是函数参数，在调用... |
| 1562 | redis-7.2.5 | __quicklistCompress | Dereference of null pointer | 316 | FP | FP | 告警行是一个assert断言语句，用于在调试时验证条件，并非生产代码中的空指针解引用。该语句在发布版本中通常会被禁用，不会导致运行时错误。 |
| 1563 | redis-7.2.5 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在 oldp 或 oldlenp 为 NULL 时会设置错误码并跳转返回，不会发生空指针解引用。代码逻辑确保了在解引用前进行了充分的空指针检查。 |
| 1564 | redis-7.2.5 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 告警行 `token->type = ch2token[ch];` 中，`ch2token` 指针来自 `json->cfg->ch2token`，切片内未显示 `cfg` 或 `ch2token` 的初始化，无法确认其是否为 NUL... |
| 1565 | redis-7.2.5 | zunionInterDiffGenericCommand | Dereference of null pointer | 2802 | FP | FP | 切片代码显示，在调用 `dictExpand(dstzset->dict,dictSize(accumulator));` 之前，`dstzset` 已通过 `dstobj = createZsetObject();` 和 `dstz... |
| 1566 | redis-7.2.5 | __quicklistCompress | Dereference of null pointer | 369 | FP | FP | 告警行代码 `if (forward == reverse ｜｜ forward->next == reverse)` 中，`forward` 和 `reverse` 指针在循环中通过 `forward = forward->next... |
| 1567 | redis-7.2.5 | _quicklistListpackMerge | Dereference of null pointer | 869 | FP | FP | 告警行 `keep->count = lpLength(keep->entry);` 中，`keep` 指针在 `if (!a->entry)` 和 `else if (!b->entry)` 两个分支中被明确赋值，确保非空。切片代码... |
| 1568 | redis-7.2.5 | moduleFreeContext | Dereference of null pointer | 816 | FP | FP | 告警指向的代码行是 `serverLog` 调用，该行本身不会解引用空指针。`ctx` 指针在函数入口处未显式检查，但函数名为 `moduleFreeContext`，其语义是释放上下文，通常由模块系统在确保上下文有效后调用。切片中 ... |
| 1569 | redis-7.2.5 | rewriteConfigRewriteLine | Dereference of null pointer | 1252 | FP | FP | 告警点 `state->lines[linenum]` 的访问发生在 `if (l)` 条件块内，该条件确保 `l` 非空。`linenum` 来自 `ln->value`，而 `ln` 是 `listFirst(l)` 的返回值，由... |
| 1570 | redis-7.2.5 | zsetRemoveFromSkiplist | Dereference of null pointer | 1503 | FP | FP | 告警行 `de = dictUnlink(zs->dict,ele);` 的返回值 `de` 在后续的 `if (de != NULL)` 中被明确检查，仅在非空时才被解引用（`score = *(double*)dictGetVal... |
| 1571 | redis-7.2.5 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该条件仅在 `h->size` 为 0 时执行。切片代码显示，在进入此分支前，`h` 已通过 `h = child;` 赋值，且 `child` 在 `raxAddCh... |
| 1572 | redis-7.2.5 | clusterManagerAddSlots | Dereference of null pointer | 4642 | FP | FP | 告警行 `*err = NULL;` 是对指针 `err` 的解引用，但切片代码显示 `err` 是函数 `clusterManagerAddSlots` 的传入参数，且后续调用 `clusterManagerCheckRedisRe... |
| 1573 | redis-7.2.5 | min_expand | Dereference of null pointer | 322 | FP | FP | 在告警行 `singlematch(uchar(*s), p, ep)` 中，对 `s` 的解引用受前置条件 `s<ms->src_end` 保护，确保了 `s` 指向有效内存，不会解引用空指针。 |
| 1574 | redis-7.2.5 | usUntilEarliestTimer | Dereference of null pointer | 276 | FP | FP | 函数在循环中明确为变量`earliest`赋值，且循环仅在`te`（即`eventLoop->timeEventHead`）非空时执行，因此`earliest`不可能为NULL，对`earliest->when`的访问是安全的。 |
| 1575 | redis-7.2.5 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | FP | 函数 `strbuf_ensure_null` 是一个内联静态函数，其目的是在字符串缓冲区末尾写入空字符以确保以null结尾。切片代码显示，该操作基于结构体指针 `s` 及其成员 `length` 进行索引。在典型的 `strbuf`... |
| 1576 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12239 | FP | FP | 代码逻辑显示，在访问 `module->blocked_clients` 之前，已通过 `if (module == NULL)` 检查确保 `module` 指针非空。因此，后续对 `module` 结构体成员的访问是安全的，不存在... |
| 1577 | redis-7.2.5 | checkMultiPartAof | Dereference of null pointer | 486 | FP | FP | 告警点位于条件判断 `if (listLength(am->incr_aof_list))`，但指针 `am` 已在上一行通过 `aofLoadManifestFromFile` 初始化并直接解引用 `am->incr_aof_lis... |
| 1578 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12243 | FP | FP | 代码逻辑显示，在调用 `moduleHoldsTimer(module)` 之前，`module` 指针已经通过 `if (module == NULL)` 检查，并且后续所有条件分支在 `module` 为 NULL 时均已提前返回... |
| 1579 | redis-7.2.5 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在 oldp 或 oldlenp 为空时会设置错误码并跳转返回，不会发生空指针解引用。代码逻辑确保了在解引用 oldlenp 之前已对其进行了非空检查，因此是误报。 |
| 1580 | redis-7.2.5 | zdiffAlgorithm2 | Dereference of null pointer | 2493 | FP | FP | 告警行 `if (htNeedsResize(dstzset->dict)) dictResize(dstzset->dict);` 中，`dstzset` 及其 `dict` 字段在函数入口处已作为非空参数传入，且函数内部逻辑（如 ... |
| 1581 | redis-7.2.5 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | 告警指向的宏 `VERIFY_READ` 在 `oldp` 或 `oldlenp` 为空时会通过 `goto label_return` 提前返回，避免了后续对空指针的解引用。切片中 `label_return` 标签虽未显示，但宏的... |
| 1582 | redis-7.2.5 | zdiffAlgorithm2 | Dereference of null pointer | 2473 | FP | FP | 告警点位于 `zslInsert(dstzset->zsl,zval.score,tmp)`，该函数内部有 `serverAssert(!isnan(score));` 断言，确保传入的 `zval.score` 有效。`dstzse... |
| 1584 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12586 | FP | FP | 告警指向的代码行是字符串常量赋值语句，不存在对空指针的解引用。该行代码是错误消息字符串的一部分，`errmsg` 指针在函数入口处已通过参数传入，且所有解引用 `*errmsg` 的操作都发生在 `module` 指针非空的条件下，逻... |
| 1585 | redis-8.0.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2871 | FP | FP | 告警点位于条件判断 `if (dstzset->zsl->length)`，但切片代码显示，在进入该分支前，`dstkey` 必须为非空，且 `dstobj` 已成功创建并赋值给 `dstzset`。代码逻辑保证了 `dstzset`... |
| 1588 | redis-8.0.2 | xgroupCommand | Dereference of null pointer | 2730 | FP | FP | 告警点 `cg->last_id = id;` 位于 `SETID` 子命令分支，该分支仅在 `cg` 指针非空时执行。切片代码显示，`cg` 指针来源于 `streamCreateCG` 的返回值或 `raxFind` 查找，在 `... |
| 1589 | redis-8.0.2 | exprTokenToNum | Dereference of null pointer | 688 | FP | FP | 函数入口参数 `exprtoken *t` 在第一个条件分支 `if (t->token_type == EXPR_TOKEN_NUM)` 中被直接解引用，这表明调用方必须保证传入的指针 `t` 非空，否则程序会在更早的访问中崩溃。切... |
| 1590 | redis-8.0.2 | dictGenericDelete | Dereference of null pointer | 661 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，已通过 `dictSize(d) == 0` 检查确保字典非空，并通过 `_dictRehashStepIfNeeded` 处理可能的rehash，且索引... |
| 1591 | redis-8.0.2 | zdiffAlgorithm1 | Dereference of null pointer | 2494 | FP | FP | 告警点位于 `zslInsert` 调用，该函数内部有 `serverAssert(!isnan(score));` 断言，且 `zval.score` 来自 `zuiNext` 的迭代过程，其值由集合或有序集合的数据结构保证，不会是... |
| 1592 | redis-8.0.2 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1645 | FP | FP | 告警点位于 `sdsfree(state->lines[linenum])`，但切片中未定义变量 `linenum`，无法判断其值是否有效或 `state->lines[linenum]` 是否为 null。然而，`sdsfree` ... |
| 1593 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12578 | FP | FP | 告警指向的代码行是给指针 errmsg 赋值字符串常量，这是安全的操作，并非对空指针的解引用。代码逻辑在解引用 errmsg 之前，已通过多个条件分支确保函数提前返回，不会执行到解引用空指针的路径。 |
| 1595 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12571 | FP | FP | 告警指向的代码行 `*errmsg = "the module can't be unloaded";` 位于 `else if (sdslen(module->loadmod->path) == 0)` 条件分支内。切片代码显示，在... |
| 1596 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12568 | FP | FP | 告警点位于对指针 `module` 进行空值检查之后的分支内，代码逻辑确保了在解引用 `module->loadmod->path` 之前，`module` 已被验证为非空。因此，该解引用操作是安全的，属于静态分析工具的逻辑误判。 |
| 1597 | redis-8.0.2 | clusterSendPing | Dereference of null pointer | 3670 | FP | FP | 告警行 `link->node->ping_sent = mstime();` 位于条件 `if (!link->inbound && type == CLUSTERMSG_TYPE_PING)` 内部，该条件已确保 `link->n... |
| 1599 | redis-8.0.2 | dictGetVal | Dereference of null pointer | 937 | FP | FP | 函数 `dictGetVal` 接收一个指向 `dictEntry` 的指针 `de`，并直接返回其成员 `v.val`。这是一个简单的访问器函数，其安全性完全依赖于调用方传入的指针 `de` 是否为 NULL。函数本身没有空指针检查... |
| 1600 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12582 | FP | FP | 告警指向的代码行是字符串字面量赋值给 `*errmsg`，这是一个常量字符串，不存在对空指针的解引用。切片代码显示，在解引用 `errmsg` 之前，函数已通过多个条件检查并可能提前返回，但告警点本身是安全的赋值操作。 |
| 1603 | redis-8.0.2 | RM_ListInsert | Dereference of null pointer | 4704 | FP | FP | 告警点位于函数 `listTypeTryConversionAppend` 的调用处，该函数内部仅调用 `listTypeTryConversionRaw`，不会对指针 `key->value` 进行解引用。关键函数 `moduleL... |
| 1604 | redis-8.0.2 | cliInitGroupHelpEntries | Dereference of null pointer | 729 | FP | FP | 切片代码显示，`helpEntries` 数组的索引 `pos` 由静态变量 `helpEntriesLen` 初始化并递增，但未提供 `helpEntries` 本身的声明或初始化信息，无法判断其大小或是否为 null。告警点 `h... |
| 1605 | redis-8.0.2 | cliFillInCommandHelpEntry | Dereference of null pointer | 589 | FP | FP | 告警点 `help->argc = subcommandname ? 2 : 1;` 是对结构体成员 `argc` 的赋值，并非解引用空指针。`help` 指针的解引用发生在 `help->argv = zmalloc(...);` ... |
| 1607 | redis-8.0.2 | zdiffAlgorithm2 | Dereference of null pointer | 2556 | FP | FP | 告警点位于 `dictShrinkIfNeeded(dstzset->dict)`，该函数内部已对传入的 `dict` 指针进行了空指针检查（`if (dictIsRehashing(d))` 等条件判断），且 `dstzset` 在... |
| 1609 | redis-8.0.2 | xgroupCommand | Dereference of null pointer | 2726 | FP | FP | 在SETID子命令中，对`s->last_id`的访问发生在`s`指针非空的条件下。代码逻辑显示，当`s`为NULL时，会提前返回或进入其他分支，不会执行到该行。因此，该行不存在空指针解引用。 |
| 1610 | redis-8.0.2 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 切片代码显示，在调用 `assert` 之前，函数已通过 `if (quicklist->len == 0) return;` 确保链表非空，因此 `quicklist->head` 和 `quicklist->tail` 不应为空指... |
| 1611 | redis-8.0.2 | exprTokensEqual | Dereference of null pointer | 717 | FP | FP | 函数入口处未对指针a和b进行空指针检查，但告警点位于函数内部，访问成员前已通过条件判断确保指针非空（例如检查token_type），因此不会发生空指针解引用。 |
| 1614 | redis-8.0.2 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 在调用 `forward->next` 之前，代码已通过 `if (forward == reverse ｜｜ forward->next == reverse)` 检查了 `forward->next` 是否等于 `reverse`... |
| 1615 | redis-8.0.2 | _quicklistListpackMerge | Dereference of null pointer | 882 | FP | FP | 告警点 `keep->count = lpLength(keep->entry);` 位于 `if ((lpMerge(&a->entry, &b->entry)))` 条件块内，且前面有明确的逻辑确保 `keep` 指向的节点其 `... |
| 1616 | redis-8.0.2 | moduleFreeContext | Dereference of null pointer | 827 | FP | FP | 代码在调用 `zfree` 前已通过 `if (ctx->postponed_arrays)` 检查了指针非空，且 `zfree` 函数内部也有 `if (ptr == NULL) return;` 的空指针保护，因此不会发生空指针解引用。 |
| 1617 | redis-8.0.2 | rewriteConfigRewriteLine | Dereference of null pointer | 1251 | FP | FP | 在调用 `sdsfree(state->lines[linenum])` 前，代码已通过 `if (l)` 确保 `l` 非空，并通过 `listFirst(l)` 获取 `ln`，且 `linenum` 是从 `ln->value`... |
| 1618 | redis-8.0.2 | raxGenericInsert | Dereference of null pointer | 870 | FP | FP | 告警点 'h->isnull = 1;' 位于条件 'if (h->size == 0)' 内部，该条件由前序代码逻辑保证，当 h->size == 0 时，h 必然是一个有效的节点指针（例如由 raxAddChild 或 raxCo... |
| 1619 | redis-8.0.2 | clusterManagerAddSlots | Dereference of null pointer | 4769 | FP | FP | 在告警行 `*err = NULL;` 之前，指针 `err` 作为函数参数传入，其值由调用方控制。切片代码显示，在后续调用 `clusterManagerCheckRedisReply` 时，`err` 被作为参数传递，而该函数内部... |
| 1621 | redis-8.0.2 | usUntilEarliestTimer | Dereference of null pointer | 275 | FP | FP | 代码逻辑保证了`earliest`指针在循环后不为空。循环仅在`te`不为空时执行，且循环内`if`条件确保至少有一个`te->id != AE_DELETED_EVENT_ID`的有效节点时，`earliest`才会被赋值。由于函数... |
| 1623 | redis-8.0.2 | checkMultiPartAof | Dereference of null pointer | 488 | FP | FP | 告警点位于条件判断 `if (listLength(am->incr_aof_list))`，但在此之前已存在 `if (am->incr_aof_list) total_num += listLength(am->incr_aof_... |
| 1624 | redis-8.0.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2813 | FP | FP | 告警点 `dictExpand(dstzset->dict,zuiLength(&src[setnum-1]));` 仅在 `setnum` 非零且 `!cardinality_only` 时执行，此时 `dstzset` 已在前面通... |
| 1627 | redis-8.0.2 | zdiffAlgorithm2 | Dereference of null pointer | 2534 | FP | FP | 告警点位于 `zslInsert(dstzset->zsl,zval.score,tmp)`，该函数内部有 `serverAssert(!isnan(score));` 断言，且 `zval.score` 来自 `zuiNext` 的... |
| 1628 | redis-8.0.2 | exprTokenToBool | Dereference of null pointer | 703 | FP | FP | 告警指向的代码行 `if (t->token_type == EXPR_TOKEN_NUM)` 在函数入口处，指针 `t` 作为函数参数，其有效性应由调用者保证。切片代码中函数逻辑完整，没有证据表明 `t` 可能为 NULL，且函数体... |
| 1632 | ffmpeg-7.1.1 | finalize_packet | Dereference of null pointer | 678 | FP | FP | 告警指向的代码行`s->st->time_base.den`位于条件`s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->ic->nb_streams > 1`的保护之下，且其上层还有对`s->... |
| 1633 | ffmpeg-7.1.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 413 | FP | FP | 切片代码显示，在访问 `ctx->buffers` 之前，存在 `if (ctx->buffers)` 的检查，且告警行 `avbuf = &ctx->buffers[buf.index];` 仅在成功执行 `ioctl` 调用后才会... |
| 1634 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 299 | FP | FP | 告警指向的代码行 `((uint16_t*)(src + stride*y))[x]` 是对指针 `src` 进行偏移和类型转换后的解引用。切片显示 `src` 是函数参数 `const uint8_t *src`，由调用者传入，在切... |
| 1635 | ffmpeg-7.1.1 | roq_dpcm_encode_frame | Dereference of null pointer | 180 | FP | FP | 告警行访问 `frame->pts` 的条件是 `context->input_frames <= 7`，而在此行之前，`frame` 指针仅在 `in && context->input_frames < 8` 的条件下被使用，且 ... |
| 1636 | ffmpeg-7.1.1 | ebml_read_binary | Dereference of null pointer | 1095 | FP | FP | 告警点 `bin->buf->data` 的访问发生在 `av_buffer_realloc` 成功返回之后，该函数保证在成功时 `*pbuf`（即 `bin->buf`）是一个有效的 `AVBufferRef` 指针，且其 `dat... |
| 1637 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 209 | FP | FP | 告警点位于条件分支 `if (depth == 1) { ... } else { ... }` 的 else 块内，该分支由 `depth` 值控制。切片代码显示 `depth` 来自数据包头部，且已通过 `switch (dept... |
| 1638 | ffmpeg-7.1.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | FP | 指针 `dc_val` 在调用 `ff_vc1_pred_dc` 时通过引用传递，该函数预期会为其分配一个有效的地址。切片代码显示 `dc_val` 被初始化为 NULL，但随后作为输出参数传入函数，函数返回后对其解引用是安全的，因为... |
| 1639 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 切片代码显示，在告警行`uint8_t *val = in->data[plane];`之前，`in`作为函数参数传入且未被修改，其有效性由调用者保证。在`s->filter`为假时，`out`被赋值为`in`，否则会调用`ff_ge... |
| 1641 | ffmpeg-7.1.1 | ebml_parse | Dereference of null pointer | 1363 | FP | FP | 告警行代码 `level->length != EBML_UNKNOWN_LENGTH` 在 `if (matroska->num_levels > 0)` 条件块内，且其上层条件 `if (level && level->lengt... |
| 1642 | ffmpeg-7.1.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警位于宏 UPDATE_CACHE 的调用处，但该宏的定义在切片中已给出，且其展开不涉及对空指针的解引用。代码逻辑显示，指针 'gb' 在宏中仅用于计算索引，没有解引用其内容，因此不存在空指针解引用风险。 |
| 1644 | ffmpeg-7.1.1 | rtp_set_prft | Dereference of null pointer | 646 | FP | FP | 切片代码显示，在调用 `av_rescale_q` 之前，已对 `av_packet_new_side_data` 的返回值 `prft` 进行了空指针检查，若为空则提前返回错误。因此，后续使用 `s->st` 和 `s->last_... |
| 1645 | ffmpeg-7.1.1 | ebml_read_sint | Dereference of null pointer | 1022 | FP | FP | 告警指向的代码行 `*num = sign_extend(avio_r8(pb), 8);` 中，`avio_r8` 函数内部已对 `s->buf_ptr` 进行了空指针检查，并确保在缓冲区耗尽时返回0，因此不会发生空指针解引用。 |
| 1646 | ffmpeg-7.1.1 | safe_filename | Dereference of null pointer | 98 | FP | FP | 代码逻辑正确，指针 `f` 在解引用前已通过循环条件 `*f` 进行了非空检查，确保了其不为空。该告警是静态分析工具对循环条件保护的误判。 |
| 1647 | ffmpeg-7.1.1 | try_push_frame | Dereference of null pointer | 512 | FP | FP | 告警点 `frame->pts = s->input_frames[0]->pts;` 位于 `if (!nb_samples) goto eof;` 之后，而 `nb_samples` 为0的条件会直接跳转到 `eof` 标签，从而... |
| 1648 | ffmpeg-7.1.1 | dump_stream_group | Dereference of null pointer | 788 | FP | FP | 告警点 `printed[st->index] = 1;` 中，`st` 指针来自 `stg->streams[i]`，而 `stg` 来自 `ic->stream_groups[i]`。切片内 `stg` 已在函数开头被赋值且未修改... |
| 1649 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，在告警行使用 `in->linesize[plane]` 之前，`in` 指针作为函数参数传入且未被修改，且函数逻辑中 `out` 可能为 `in` 或新分配的帧，但 `in` 本身始终有效。告警点位于条件 `s->pl... |
| 1650 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 236 | FP | FP | 告警点位于 `av_assert0` 宏内部，该宏用于开发调试，在条件不满足时会调用 `abort()` 终止程序。这属于主动的断言检查，而非意外的空指针解引用，是代码中的安全防护机制。 |
| 1651 | ffmpeg-7.1.1 | ff_encode_encode_cb | Dereference of null pointer | 275 | FP | FP | 告警点位于条件判断 `if (frame->duration)`，但切片代码显示，在进入该分支前，外层已存在 `if (frame && ...)` 的条件检查，且告警所在函数 `ff_encode_encode_cb` 的参数 `f... |
| 1652 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 219 | FP | FP | 告警点位于 `av_assert0` 宏内，该宏在条件为假时会调用 `abort()` 终止程序，属于开发阶段的断言检查，并非运行时可能发生的空指针解引用。切片代码显示 `frame` 指针在解引用前已通过 `if (frame)` ... |
| 1653 | ffmpeg-7.1.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该宏及其相关宏（如 OPEN_READER）均未对指针 's' 或 'gb' 进行解引用操作。宏定义仅涉及参数传递和赋值，没有直接的指针访问，因此不存在空指针解引用。 |
| 1654 | ffmpeg-7.1.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码显示变量 `dpd` 在条件判断 `if (dpd[pos])` 中被解引用，但 `dpd` 本身在切片中未定义或初始化，无法判断其是否为 null。然而，该告警为逻辑错误，且 `dpd` 在同一函数后续的赋值语句 `dpd[... |
| 1655 | ffmpeg-7.1.1 | try_push_frame | Dereference of null pointer | 241 | FP | FP | 告警行 `outbuf->pts = inbuf[0]->pts;` 存在对 `inbuf[0]` 的空指针解引用风险，但切片代码显示，在解引用前，`for` 循环已调用 `ff_inlink_consume_samples` 来填充... |
| 1656 | ffmpeg-7.1.1 | hls_append_segment | Dereference of null pointer | 1185 | FP | FP | 告警行代码 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 位于条件 `if (hls->max_nb_segments &&... |
| 1657 | ffmpeg-7.1.1 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 告警点 `file->user_duration = arg_int[0];` 位于 `case DIR_DURATION:` 分支，该分支仅在 `dir->flags & NEEDS_FILE` 条件满足且 `cat->nb_fil... |
| 1658 | ffmpeg-7.1.1 | dump_argument | Dereference of null pointer | 516 | FP | FP | 函数参数 `a` 是一个 `const char*` 指针，调用方传入空指针的可能性较低，且函数内部通过 `for (p = a; *p; p++)` 循环条件 `*p` 进行空值检查，若 `a` 为空指针，解引用 `*p` 前循环条... |
| 1659 | ffmpeg-7.1.1 | kalman_smoothen | Dereference of null pointer | 585 | FP | FP | 代码逻辑确保了在解引用 best_hist_ptr 之前，它已被有效赋值。当 optimal_gain > 0 时，best_hist_ptr 在循环中被赋值为非空的 ptr；若 optimal_gain <= 0，函数提前返回，不会... |
| 1660 | ffmpeg-7.1.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在访问 `dp1[pos]` 和 `dp2[pos]` 之前，存在条件 `if (dpd[pos])` 进行空指针检查，确保 `dpd` 指针有效。告警点位于该条件保护块内，因此不会发生空指针解引用。 |
| 1661 | ffmpeg-7.1.1 | id3v2_parse | Dereference of null pointer | 1055 | FP | FP | 告警点位于条件分支 `extra_func->read(...)`，但 `extra_func` 仅在 `get_extra_meta_func` 返回非空指针时被赋值。切片代码显示 `get_extra_meta_func` 在未找... |
| 1662 | ffmpeg-7.1.1 | set_bframe_chain_length | Dereference of null pointer | 1596 | FP | FP | 告警指向的代码行 `s->input_picture[i - 1]->f->data[0]` 在切片中受到前置条件 `if (s->input_picture[i] && s->input_picture[i]->b_frame_sc... |
| 1663 | ffmpeg-7.1.1 | split_commandline | Dereference of null pointer | 809 | FP | FP | 告警点 'opt[0] == '-' && opt[1] == '-' && !opt[2]' 在访问 opt[1] 和 opt[2] 之前，已通过 'const char *opt = argv[optindex++], *arg;... |
| 1664 | ffmpeg-7.1.1 | ebml_read_ascii | Dereference of null pointer | 1077 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 1665 | ffmpeg-7.1.1 | output_packet | Dereference of null pointer | 1103 | FP | FP | 告警行访问 `timestamp_packet->unwritten_size`，但切片代码显示 `timestamp_packet` 在访问前已通过 `stream->premux_packet` 赋值，且其上游逻辑（如 `best... |
| 1666 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 286 | FP | FP | 告警点位于 `enc_ctx->width = ost->ist->par->width;`，该赋值发生在 `enc_ctx->codec_type == AVMEDIA_TYPE_SUBTITLE` 且 `!enc_ctx->wid... |
| 1667 | ffmpeg-7.1.1 | ebml_read_uint | Dereference of null pointer | 1002 | FP | FP | 代码中指针 `num` 是函数的传入参数，在函数内部被直接解引用赋值，没有空指针检查。但根据函数签名和上下文，`num` 作为输出参数由调用者传入，其有效性应由调用者保证。切片内没有证据表明调用者会传入空指针，因此告警为误报。 |
| 1668 | ffmpeg-7.1.1 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 告警点 `file->inpoint = arg_int[0];` 位于 `case DIR_INPOINT:` 分支，该分支仅在 `dir->flags & NEEDS_FILE` 条件满足且 `cat->nb_files` 非零时... |
| 1669 | ffmpeg-7.1.1 | sb_decode | Dereference of null pointer | 1348 | FP | FP | 告警点位于条件语句 `if (st->innov_save)` 内部，该条件已确保 `st->innov_save` 非空，进而保证了其派生的 `innov_save` 指针非空，因此对 `innov_save` 的数组访问是安全的。 |
| 1670 | ffmpeg-7.1.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警行 `if ((*child)->state * 2 == -t->state)` 位于 `if (t->state)` 和 `if (!(t->state & 1))` 条件块内，且前文有 `child = &t->child[... |
| 1671 | ffmpeg-7.1.1 | check_header_mismatch | Dereference of null pointer | 519 | FP | FP | 告警指向的代码行 `curr = curr->next;` 位于一个由 `av_assert0(i < FLAC_MAX_SEQUENTIAL_HEADERS);` 保护的循环内，该断言确保了循环变量 `i` 不会越界，从而保证了 `... |
| 1672 | ffmpeg-7.1.1 | get_pict_type | Dereference of null pointer | 136 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效性，确保 `unit->content`... |
| 1674 | ffmpeg-7.1.1 | mpegts_open_filter | Dereference of null pointer | 495 | FP | FP | 告警指向的 `av_log` 调用已被宏定义为空操作 `while(0)`，因此不可能发生空指针解引用。代码逻辑正确，工具报告的是静态分析层面的误判。 |
| 1675 | ffmpeg-7.1.1 | guess_mv | Dereference of null pointer | 432 | FP | FP | 告警行位于条件分支 `else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])` 中，该条件已明确检查了 `s->last_pic.f` 和 `s->last_pic.m... |
| 1676 | ffmpeg-7.1.1 | build_table | Dereference of null pointer | 204 | FP | FP | 告警点 'table[j].len = -subtable_bits;' 处的 table 指针在调用 alloc_table 成功后已通过 'table = &vlc->table[table_index];' 正确初始化，且后续有... |
| 1677 | ffmpeg-7.1.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警位于函数 `ff_vorbiscomment_write` 的第93行，该行是 `AVChapter *chp = chapters[i];`。切片代码显示，在第10行有一个条件判断 `if (chapters && nb_cha... |
| 1678 | ffmpeg-7.1.1 | locate_option | Dereference of null pointer | 495 | FP | FP | 在调用 `po = find_option(options, cur_opt);` 后，`po` 指针不可能为 NULL，因为 `find_option` 函数返回一个指向 `OptionDef` 结构体的指针，该指针来自传入的 `o... |
| 1679 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 78 | FP | FP | 告警位于宏 UPDATE_CACHE 的展开行，该宏及其相关宏（如 GET_CACHE）操作的是结构体内部的位缓存和索引，并非对空指针进行解引用。代码逻辑是标准的位读取操作，不存在空指针解引用风险。 |
| 1680 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警点位于对 `in->data[plane]` 的赋值语句，切片显示 `in` 是函数参数且非空，且 `plane` 在循环内受控，因此不会发生空指针解引用。 |
| 1681 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 333 | FP | FP | 告警行 `new_pts = av_rescale_q(...)` 仅在 `if (s->do_video)` 条件为真时执行，而 `outlink` 在该条件下被赋值为 `ctx->outputs[1]`，是一个有效的非空指针，因此... |
| 1682 | ffmpeg-7.1.1 | av_dump_format | Dereference of null pointer | 898 | FP | FP | 告警点 `printed[program->stream_index[k]] = 1;` 位于 `if (ic->nb_streams && !printed) return;` 之后，该条件已确保当 `ic->nb_streams`... |
| 1683 | ffmpeg-7.1.1 | check_header_mismatch | Dereference of null pointer | 475 | FP | FP | 告警行代码 `curr->link_penalty[i]` 在循环中访问，循环条件 `curr != child` 和 `curr = curr->next` 确保了 `curr` 在链表遍历中有效，且切片内未发现将 `curr` 置... |
| 1684 | ffmpeg-7.1.1 | update_context_from_thread | Dereference of null pointer | 438 | FP | FP | 告警行位于条件判断 `if (hwaccel->priv_data_size)` 内部，该条件已确保 `hwaccel` 非空，且其 `priv_data_size` 大于零。随后对 `hwaccel->update_thread_c... |
| 1685 | ffmpeg-7.1.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 告警指向宏 UPDATE_CACHE_32 的展开，但切片代码显示该宏的参数 `s` 是一个 `GetBitContext *` 指针，在调用函数 `get_bits_long` 时已作为参数传入，且在同一函数内被其他宏（如 OPEN... |
| 1686 | ffmpeg-7.1.1 | activate | Dereference of null pointer | 186 | FP | FP | 告警点位于 `frame->pts = s->pts;`，但在此之前，`frame` 指针已在多个分支中被检查并确保非空（例如 `if (!frame) return AVERROR(ENOMEM);`），且到达该行时 `frame`... |
| 1687 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 200 | FP | FP | 告警点位于一个条件分支 `if (depth == 1)` 内部，该分支仅在 `avctx->pix_fmt == AV_PIX_FMT_PAL8 && depth < 8` 时执行。切片代码显示，当 `depth == 1` 时，`... |
| 1688 | ffmpeg-7.1.1 | check_available | Dereference of null pointer | 616 | FP | FP | 告警行代码中，`TAB_MVF` 宏展开后访问的 `tab_mvf` 数组指针，其有效性由前置的 `is_available(fc, n->x, n->y)` 函数调用保证。`is_available` 函数内部检查了相关数据结构，确... |
| 1689 | ffmpeg-7.1.1 | ff_encode_encode_cb | Dereference of null pointer | 272 | FP | FP | 告警行 `avpkt->pts = frame->pts;` 位于 `if (frame && (codec->caps_internal & FF_CODEC_CAP_EOF_FLUSH))` 条件块内，切片代码显示该行执行前已通过... |
| 1690 | ffmpeg-7.1.1 | rtp_parse_one_packet | Dereference of null pointer | 888 | FP | FP | 告警点 `buf[0]` 的访问发生在 `if (!buf)` 检查之后，且当 `buf` 为 NULL 时，函数已在第 7-9 行通过 `return rtp_parse_queued_packet(s, pkt);` 提前返回，因... |
| 1691 | ffmpeg-7.1.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已通过条件 `if (s->peak[i][j] && ...)` 确保 `s->peak[i][j]` 为真，而 `s->peak[i][j]` 仅在 `dpd[pos]` 非零时被... |
| 1692 | ffmpeg-7.1.1 | ost_add | Dereference of null pointer | 1541 | FP | FP | 告警行 `ms->stream_duration = ist->st->duration;` 位于条件 `if (ost->ist && ost->ist->st->duration > 0)` 内部，已通过前置条件 `ost->is... |
| 1693 | ffmpeg-7.1.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1420 | FP | FP | 切片代码显示 `scale_matrix` 在条件 `sps->scaling_list_enabled && !(transform_skip_flag && log2_trafo_size > 2)` 下被赋值，且在使用点 `sc... |
| 1694 | ffmpeg-7.1.1 | nal_parse_units | Dereference of null pointer | 93 | FP | FP | 告警指向的代码行 `list->nb_nalus >= nalu_limit` 是一个条件判断，用于检查数组索引是否超过安全限制，此处 `list` 指针在函数入口已作为非空参数传入，且切片中未见任何将其置空的操作，因此不会发生空指针... |
| 1695 | ffmpeg-7.1.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1513 | FP | FP | 告警点位于 `ff_get_audio_buffer(link, frame->nb_samples)` 调用处，但在此之前已通过 `if (av_frame_is_writable(frame))` 检查，且 `frame` 参数来... |
| 1696 | ffmpeg-7.1.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 告警点`s->buffer[index >> 3]`的访问基于结构体指针`s`，切片中`s`作为参数传入，其有效性应由调用者保证。函数内部逻辑是安全的位读取操作，没有证据表明`s`或`s->buffer`为NULL，这属于工具对函数内... |
| 1697 | ffmpeg-7.1.1 | asf_parse_packet | Dereference of null pointer | 1307 | FP | FP | 告警点位于一个for循环的条件判断部分，用于检查数据包数据是否全为零。切片代码显示，在访问`asf_st->pkt.data[i]`之前，已经通过`av_new_packet`或`av_packet_unref`等函数确保了`asf_... |
| 1698 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 146 | FP | FP | 告警行 `alpMmxFilter[s*i] = alpSrcPtr[i];` 位于 `if (CONFIG_SWSCALE_ALPHA && hasAlpha)` 条件块内，切片代码显示 `alpSrcPtr` 在该条件块之前被初始... |
| 1699 | ffmpeg-7.1.1 | choose_rct_params | Dereference of null pointer | 1008 | FP | FP | 告警指向的代码行 `r = *((const uint16_t *)(src[2] + x*2 + stride[2]*y));` 位于条件分支 `else if (f->use32bit ｜｜ transparency)` 内，该分... |
| 1700 | ffmpeg-7.1.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 告警点位于条件语句 `if (dpd[pos])` 内部，这表明对指针 `dpd` 的访问是受保护的，只有在 `dpd[pos]` 为真（即非零）时才会解引用。切片代码中 `dpd` 的定义和赋值虽未直接给出，但该保护逻辑足以避免对空... |
| 1702 | ffmpeg-7.1.1 | mov_write_trak_tag | Dereference of null pointer | 4191 | FP | FP | 告警行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 中，`st` 是函数参数，由调用者传入，在切片内未发现其被赋值为 NULL 的路径。函数内多处存在... |
| 1703 | ffmpeg-7.1.1 | ebml_parse | Dereference of null pointer | 1380 | FP | FP | 告警行代码位于条件分支 `else if (level->length != EBML_UNKNOWN_LENGTH)` 中，该分支仅在 `level` 指针非空时才会执行。切片代码显示 `level` 指针在函数开头被赋值，且其来源... |
| 1704 | ffmpeg-7.1.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 代码中dpd指针指向out->data数组中的元素，out指针已在函数参数中传入且被使用，切片内未显示其可能为空。告警点是对dpd数组元素的访问，而非对dpd指针本身的解引用，逻辑检查的是数组元素值是否为0，不会导致空指针解引用。 |
| 1706 | ffmpeg-7.1.1 | ac3_apply_rematrixing | Dereference of null pointer | 598 | FP | FP | 切片代码显示，对指针 `flags` 的访问发生在 `if (!s->rematrixing_enabled)` 返回检查之后，且位于一个循环内部。`flags` 变量在切片中未定义，但其使用点 `flags[bnd]` 表明它很可能... |
| 1707 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 683 | FP | FP | 告警点位于FFSWAP宏调用，用于交换两个指针指向的值。切片代码显示，在调用FFSWAP之前，`ptr1`和`ptr2`均已明确初始化且指向有效缓冲区（`q->decoded_bytes_buffer`及其偏移位置），不存在空指针解引用。 |
| 1708 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 303 | FP | FP | 告警指向的代码行 `sample[0][x] = ((uint16_t*)(src + stride*y))[x] >> (16 - f->bits_per_raw_sample);` 中，`sample[0]` 已在循环前被正确初始... |
| 1709 | ffmpeg-7.1.1 | ff_rdt_parse_header | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在告警行（while循环条件）中访问buf[1]之前，函数参数buf已通过调用方传入，且函数开头没有对buf进行空指针检查。然而，被调用的函数init_get_bits（在后续代码中使用）内部包含对传入buffer指针的... |
| 1710 | ffmpeg-7.1.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 代码在访问 `info->key_ids[i]` 之前，已通过 `if (info)` 检查确保 `info` 指针非空，并且 `for` 循环的条件 `i < info->num_key_ids` 也隐含了对 `info` 的访问，... |
| 1711 | ffmpeg-7.1.1 | shift_frame | Dereference of null pointer | 152 | FP | FP | 告警点所在的 `av_log` 调用已被宏定义为 `while(0)`，该语句在编译后不会产生任何实际代码，因此不可能发生空指针解引用。 |
| 1712 | ffmpeg-7.1.1 | build_table | Dereference of null pointer | 170 | FP | FP | 告警点位于循环内部，`table`指针在函数开头通过`alloc_table`分配并赋值，且循环前已检查`table_index >= 0`，因此`table`非空。循环内`j`的计算受控于`code`和`table_nb_bits`... |
| 1713 | ffmpeg-7.1.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 告警点 `memcpy(info->key_ids[j], side_data, key_id_size);` 中，`info->key_ids[j]` 指针在 `av_encryption_init_info_alloc` 函数中已... |
| 1714 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 293 | FP | FP | 告警指向的代码行 `sample[0][x] = src[x * pixel_stride + stride * y];` 是对数组元素的赋值，并非解引用空指针。切片代码中 `src` 是函数参数，`sample[0]` 已指向有效的... |
| 1715 | ffmpeg-7.1.1 | dump_stream_group | Dereference of null pointer | 715 | FP | FP | 告警行 `printed[st->index] = 1;` 中的指针 `st` 在切片代码中未定义，但根据其所在的循环上下文 `for (int k = 0; channel_count > 0 && k < stg->nb_stre... |
| 1716 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 166 | FP | FP | alpSrcPtr 的赋值在条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 下进行，当条件不满足时其值为 NULL。告警行 `*(const void**)&alpMmxFilter[4*i+0]= a... |
| 1717 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的调用行，但切片代码显示该宏已定义，且其展开 UPDATE_CACHE_LE 在切片中未提供定义。然而，根据函数 get_vlc2 的上下文和宏 GET_VLC 的定义，UPDATE_CACHE ... |
| 1718 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 告警点位于条件表达式 `s->planeheight[plane] > 1 ? in->linesize[plane] / 2 : 0` 中，当条件为假时，`linesize` 被赋值为 0，后续在宏 `CHECK_BIT` 中会使用... |
| 1719 | ffmpeg-7.1.1 | set_bframe_chain_length | Dereference of null pointer | 1611 | FP | FP | 告警点位于循环 `for (i = 0; i < b_frames + 1; i++)` 内部，其中 `b_frames` 由 `b_frames = FFMAX(0, i - 1)` 计算得出，且 `i` 来自前一个循环的终止条件，... |
| 1720 | ffmpeg-7.1.1 | mov_write_trak_tag | Dereference of null pointer | 4196 | FP | FP | 告警指向的代码行 `is_clcp_track(track) && st->sample_aspect_ratio.num` 中，`st` 是函数参数，在调用链中已确保非空。切片内 `mov_write_trak_tag` 函数开头即... |
| 1721 | ffmpeg-7.1.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该宏及其相关宏（如 OPEN_READER）仅对结构体指针 's' 的成员进行操作，并未直接解引用指针 's' 本身。在函数入口处，'s' 作为参数传入，其有效性应由调用者保... |
| 1722 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 472 | FP | FP | 告警指向宏 `DECODE_CODEWORD` 的调用行，但切片代码显示该宏仅进行位操作和变量赋值，并未对任何指针进行解引用。代码逻辑中不存在对空指针的解引用操作，因此是静态分析工具的误报。 |
| 1723 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 687 | FP | FP | 告警指向的代码行 `q->decoded_bytes_buffer[i] = *ptr2--;` 中，`ptr2` 被赋值为 `js_databuf + js_block_align - 1`，而 `js_databuf` 是函数参数... |
| 1724 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 692 | FP | FP | 在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确初始化为 `q->decoded_bytes_buffer`，这是一个有效的数组指针。循环条件 `*ptr1 ==... |
| 1726 | ffmpeg-7.0.1 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 告警指向的代码行 `s->st->time_base.den` 位于条件 `if (s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->ic->nb_streams > 1)` 内部。切片代码显... |
| 1727 | ffmpeg-7.0.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 412 | FP | FP | 告警点 `avbuf = &ctx->buffers[buf.index];` 在访问 `ctx->buffers` 前，切片代码中已存在 `if (ctx->buffers)` 和 `if (!ctx->buffers)` 的检查，... |
| 1728 | ffmpeg-7.0.1 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | FP | 告警行访问的 `frame` 指针在函数入口处已通过三元运算符确保非空时才使用，且告警行位于 `in && context->input_frames < 8` 条件块之后，该条件保证了 `frame` 非空，因此不会发生空指针解引用。 |
| 1729 | ffmpeg-7.0.1 | ebml_read_binary | Dereference of null pointer | 1088 | FP | FP | 告警行访问 `bin->buf->data` 前，`av_buffer_realloc` 已成功返回，这保证了 `bin->buf` 非空且其 `data` 指针有效。切片代码显示了完整的成功路径，不存在空指针解引用。 |
| 1730 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 208 | FP | FP | 告警点位于条件分支 `if (depth == 1) { ... } else { ... }` 的 else 块中，该分支由 `depth < 8` 且 `maplength` 非零的条件触发。切片代码显示 `depth` 在 sw... |
| 1731 | ffmpeg-7.0.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | FP | 切片代码显示，`dc_val` 作为指针参数传入 `ff_vc1_pred_dc` 函数，该函数负责为其赋值，因此在其后的 `*dc_val = dcdiff;` 行解引用时，`dc_val` 不可能为 NULL，告警为误报。 |
| 1732 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 告警点 `uint8_t *val = in->data[plane];` 位于 `if (s->depth <= 8)` 分支内，该分支仅在 `in` 帧有效时执行。`in` 是函数参数，由调用者传入，在切片中未见其为空的赋值或检查... |
| 1734 | ffmpeg-7.0.1 | ebml_parse | Dereference of null pointer | 1354 | FP | FP | 告警行代码 `level->length != EBML_UNKNOWN_LENGTH` 在访问 `level` 指针前已通过条件 `matroska->num_levels > 0` 确保 `level` 非空（`level` 定义... |
| 1735 | ffmpeg-7.0.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警指向的宏 `UPDATE_CACHE` 展开后不涉及指针解引用，且切片代码中 `gb` 参数的使用均通过宏操作，未发现任何直接的指针解引用操作，因此该告警为误报。 |
| 1736 | ffmpeg-7.0.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 告警指向的 `s->bit_buf` 解引用发生在函数起始处，用于读取成员变量，而 `s` 指针在函数调用时已通过 `static inline` 内联机制由调用方传入。切片代码中 `s` 被多次安全使用（如 `s->buf_end`... |
| 1737 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 301 | FP | FP | 告警指向的代码行 `sample[0][x] = ((uint16_t*)(src + stride*y))[x] >> (16 - s->bits_per_raw_sample);` 中，`src` 是函数入参，`stride`、`... |
| 1738 | ffmpeg-7.0.1 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 切片代码显示，在调用 `av_rescale_q` 之前，已对 `av_packet_new_side_data` 的返回值 `prft` 进行了空指针检查，若为空则提前返回错误。因此，后续使用 `s->st` 和 `s->last_... |
| 1739 | ffmpeg-7.0.1 | ebml_read_sint | Dereference of null pointer | 1015 | FP | FP | 切片代码显示，在调用 `avio_r8(pb)` 前，函数 `ebml_read_sint` 并未对指针 `pb` 进行空值检查，这触发了规则。然而，`avio_r8` 函数内部已包含对输入指针 `s` 的访问（`s->buf_ptr... |
| 1740 | ffmpeg-7.0.1 | safe_filename | Dereference of null pointer | 97 | FP | FP | 代码逻辑正确，指针 `f` 在循环条件 `*f` 中作为解引用操作前，已通过函数参数传入且循环条件确保了 `*f` 非空时才进入循环体，不存在对空指针的解引用。 |
| 1741 | ffmpeg-7.0.1 | try_push_frame | Dereference of null pointer | 511 | FP | FP | 告警点 `frame->pts = s->input_frames[0]->pts;` 执行前，代码已通过 `if (!nb_samples) goto eof;` 确保 `nb_samples` 非零，而 `nb_samples` ... |
| 1742 | ffmpeg-7.0.1 | dump_stream_group | Dereference of null pointer | 751 | FP | FP | 告警点位于循环内部，对数组 `printed` 的访问索引 `st->index` 由 `stg->streams[i]` 决定，而 `i` 在循环范围内（0 到 `stg->nb_streams-1`），切片中 `stg` 和 `p... |
| 1743 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 告警行 `const int linesize = s->planeheight[plane] > 1 ? in->linesize[plane] : 0;` 中，当 `s->planeheight[plane] > 1` 为假时，`... |
| 1744 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 225 | FP | FP | 告警点位于av_assert0宏内，该宏用于调试断言，在条件不满足时会调用av_log并abort，但av_log宏在切片中被定义为空操作(while(0))，因此不会发生空指针解引用。这是静态分析工具对宏展开逻辑的误判。 |
| 1745 | ffmpeg-7.0.1 | ff_encode_encode_cb | Dereference of null pointer | 274 | FP | FP | 切片代码显示，在访问 `frame->duration` 之前，外层条件 `if (!ret && *got_packet)` 已经成立，并且内层条件 `if (avpkt->pts == AV_NOPTS_VALUE)` 和 `if... |
| 1746 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 208 | FP | FP | 告警点位于 `av_assert0` 宏内部，该宏用于开发调试断言，在条件不满足时会调用 `abort()` 终止程序，这属于预期的错误处理逻辑，而非空指针解引用漏洞。 |
| 1747 | ffmpeg-7.0.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 告警位于宏 UPDATE_CACHE 的调用处，该宏展开后仅涉及位操作，不会直接解引用指针。切片代码显示 get_sbits 函数是标准的位读取操作，其参数 s 在调用上下文中通常有效，且宏定义中未见对 s 进行空指针解引用。工具可能... |
| 1748 | ffmpeg-7.0.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码显示变量 `dpd` 在条件判断 `if (dpd[pos])` 中被解引用，但在该使用点之前，切片中未包含 `dpd` 的声明、定义或赋值语句，无法判断其是否可能为 null。然而，根据告警规则和上下文，`dpd` 很可能是... |
| 1751 | ffmpeg-7.0.1 | hls_append_segment | Dereference of null pointer | 1171 | FP | FP | 在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 之前，代码已通过 `en = vs->segments;` 赋值，且... |
| 1752 | ffmpeg-7.0.1 | concat_parse_script | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在DIR_DURATION分支中访问file指针前，存在DIR_FILE分支会调用add_file函数来初始化file指针，且代码逻辑确保在DIR_DURATION执行时cat->nb_files>0（由NEEDS_FI... |
| 1753 | ffmpeg-7.0.1 | dump_argument | Dereference of null pointer | 507 | FP | FP | 函数参数 `a` 在循环条件 `for (p = a; *p; p++)` 中被解引用，但 `a` 是函数的 `const char*` 参数，调用方必须保证其非空，否则在解引用 `*p` 前就会发生空指针访问。切片代码显示函数逻辑是... |
| 1754 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 297 | FP | FP | 告警指向的代码行 `((uint16_t*)(src + stride*y))[x]` 是对指针 `src` 的合法解引用。`src` 是函数入参，在切片中未见其被赋值为 NULL 或存在导致其为 NULL 的逻辑。该解引用操作是访问... |
| 1755 | ffmpeg-7.0.1 | kalman_smoothen | Dereference of null pointer | 584 | FP | FP | 代码逻辑确保了`best_hist_ptr`在解引用前不可能为空。在循环中，只有当`optimal_gain > 0`时才会设置`best_hist_ptr`，而后续的解引用操作（如计算点积和赋值`out[n]`）都位于`optima... |
| 1756 | ffmpeg-7.0.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 告警点位于条件语句 `if (dpd[pos])` 内部，这意味着对 `dp1` 和 `dp2` 的赋值仅在 `dpd[pos]` 非零（即非空）时执行，因此不会发生空指针解引用。 |
| 1757 | ffmpeg-7.0.1 | id3v2_parse | Dereference of null pointer | 1054 | FP | FP | 告警点位于条件分支 `extra_func->read(...)`，但切片代码显示 `extra_func` 仅在 `get_extra_meta_func` 返回非空指针时被赋值，且该函数调用前已通过 `extra_func = g... |
| 1758 | ffmpeg-7.0.1 | choose_rct_params | Dereference of null pointer | 983 | FP | FP | 告警点位于条件分支 `else` 块中，该分支仅在 `lbd` 为假时执行。切片代码未显示 `lbd` 变量的值，但 `src` 数组的三个元素（`src[0]`、`src[1]`、`src[2]`）在同一个分支内被同等访问，若 `s... |
| 1759 | ffmpeg-7.0.1 | split_commandline | Dereference of null pointer | 800 | FP | FP | 告警点 'opt[0] == '-' && opt[1] == '-' && !opt[2]' 在访问 opt[1] 和 opt[2] 之前，已通过 'const char *opt = argv[optindex++], *arg;... |
| 1760 | ffmpeg-7.0.1 | ebml_read_ascii | Dereference of null pointer | 1070 | FP | FP | 切片代码显示 `av_free` 被定义为 `while(0)` 宏，这意味着对 `*str` 的解引用操作在编译后不存在，因此不会发生空指针解引用。告警是基于宏展开前的源代码分析产生的误报。 |
| 1761 | ffmpeg-7.0.1 | output_packet | Dereference of null pointer | 1102 | FP | FP | 告警点位于条件判断 `if (timestamp_packet->unwritten_size == timestamp_packet->size)`，但根据切片代码，`timestamp_packet` 被赋值为 `stream->... |
| 1762 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 293 | FP | FP | 切片代码显示，在访问 `ost->ist->par->width` 之前，已通过 `if (e->opened)` 和 `if (ret < 0)` 等条件进行控制，且 `ost` 和 `enc_ctx` 在函数入口处已从有效参数 `... |
| 1763 | ffmpeg-7.0.1 | ebml_read_uint | Dereference of null pointer | 995 | FP | FP | 代码逻辑上，指针 `num` 在函数入口处已被解引用赋值，表明调用方已确保其非空。此外，函数内部对 `num` 的赋值操作是确定性的，不存在导致空指针解引用的条件分支。 |
| 1764 | ffmpeg-7.0.1 | concat_parse_script | Dereference of null pointer | 561 | FP | FP | 告警点位于DIR_INPOINT分支，该分支仅在file指针非空时执行。代码逻辑显示，file指针仅在DIR_FILE分支通过add_file函数成功调用后才被赋值，且该分支有错误检查。此外，NEEDS_FILE标志检查确保在cat-... |
| 1766 | ffmpeg-7.0.1 | ost_add | Dereference of null pointer | 1428 | FP | FP | 告警点 `ms->stream_duration = ist->st->duration;` 在 `if (ost->ist && ost->ist->st->duration > 0)` 条件保护下，`ist` 指针已通过前置条件 ... |
| 1767 | ffmpeg-7.0.1 | sb_decode | Dereference of null pointer | 1347 | FP | FP | 告警点位于 `innov_save[2 * i] = exc[i];`，但该行代码仅在 `if (st->innov_save)` 条件块内执行。切片代码显示，`innov_save` 在该条件块内被初始化为 `st->innov_s... |
| 1768 | ffmpeg-7.0.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警点位于条件 `if ((*child)->state * 2 == -t->state)` 内，该条件仅在 `t->state` 非零且 `t->state` 为偶数（`!(t->state & 1)`）时才会被评估。切片代码显示... |
| 1769 | ffmpeg-7.0.1 | check_header_mismatch | Dereference of null pointer | 520 | FP | FP | 告警位于循环条件 `curr != child` 内，循环体 `curr = curr->next;` 执行前已通过 `curr = header->next;` 初始化，且循环条件 `curr != child` 保证了 `curr... |
| 1770 | ffmpeg-7.0.1 | get_pict_type | Dereference of null pointer | 135 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效性，这确保了 `unit->conten... |
| 1772 | ffmpeg-7.0.1 | mpegts_open_filter | Dereference of null pointer | 497 | FP | FP | 告警指向的 `av_log` 调用已被宏定义为空操作 `while(0)`，因此其第一个参数 `ts->stream` 即使为 null 也不会被解引用，不会导致空指针解引用错误。 |
| 1773 | ffmpeg-7.0.1 | guess_mv | Dereference of null pointer | 428 | FP | FP | 在警告行 `else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])` 之前，已有条件 `if (s->last_pic.f && s->last_pic.f->data... |
| 1774 | ffmpeg-7.0.1 | build_table | Dereference of null pointer | 204 | FP | FP | 告警点位于 `table[j].len = -subtable_bits;`，其中 `j` 的计算基于 `code_prefix` 和 `table_nb_bits`，且 `table_nb_bits` 已通过 `if (table_... |
| 1775 | ffmpeg-7.0.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警位于第93行 `AVChapter *chp = chapters[i];`，但该行代码位于 `if (chapters && nb_chapters)` 和 `if (m)` 两个条件语句的保护范围内。当 `chapters` ... |
| 1776 | ffmpeg-7.0.1 | locate_option | Dereference of null pointer | 486 | FP | FP | 在调用 `po = find_option(options, cur_opt);` 后，`po` 指针不可能为 NULL。`find_option` 函数返回一个指向 `OptionDef` 结构体的指针，该指针在循环中递增，最终会指... |
| 1777 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警指向的代码行 `uint16_t *val = (uint16_t *)in->data[plane];` 中，`in` 是函数参数，在调用前已通过 `filter_frame` 的调用者确保非空，且切片内 `in->data[p... |
| 1778 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 332 | FP | FP | 告警行 `new_pts = av_rescale_q(...)` 仅在 `s->do_video` 为真时执行，而 `outlink` 变量在 `s->do_video` 为真时被赋值为 `ctx->outputs[1]`，为有效指... |
| 1779 | ffmpeg-7.0.1 | av_dump_format | Dereference of null pointer | 834 | FP | FP | 告警点 `printed[program->stream_index[k]] = 1;` 位于 `if (ic->nb_streams && !printed) return;` 之后，该条件保证了当 `ic->nb_streams`... |
| 1780 | ffmpeg-7.0.1 | check_header_mismatch | Dereference of null pointer | 476 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 的循环中，`i` 的值由外层 `for (i = 0; i < FLAC_MAX_SEQUENTIAL_HEADERS; i++)` 严格限定，确保了数组访问在边界... |
| 1781 | ffmpeg-7.0.1 | update_context_from_thread | Dereference of null pointer | 360 | FP | FP | 切片代码显示，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 条件确保 `hwaccel` 不为... |
| 1782 | ffmpeg-7.0.1 | choose_rct_params | Dereference of null pointer | 984 | FP | FP | 切片代码显示，在lbd为假的分支中，对src[0]、src[1]、src[2]进行了指针解引用，但告警点位于src[2]的解引用行。告警规则为'空指针解引用'，而切片中未提供src数组的初始化或有效性检查信息，无法判断src[2]是否... |
| 1783 | ffmpeg-7.0.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 代码中`s`指针在调用宏`OPEN_READER`和`UPDATE_CACHE_32`前未显式判空，但函数`get_bits_long`是静态内联函数，其调用者`get_bits`（在同一切片中）已对同一指针`s`执行了相同的宏操作而... |
| 1784 | ffmpeg-7.0.1 | activate | Dereference of null pointer | 186 | FP | FP | 告警点位于 `frame->pts = s->pts;`，但在此之前，`frame` 指针已在 `if (s->stop_mode == MODE_ADD)` 或 `else if (s->stop_mode == MODE_CLON... |
| 1785 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 199 | FP | FP | 告警点位于一个条件分支 `if (depth == 1)` 内部，该分支仅在 `avctx->pix_fmt == AV_PIX_FMT_PAL8 && depth < 8` 时执行。切片代码显示，当 `depth == 1` 时，`... |
| 1786 | ffmpeg-7.0.1 | ff_encode_encode_cb | Dereference of null pointer | 271 | FP | FP | 告警行 `avpkt->pts = frame->pts;` 位于条件 `if (avpkt->pts == AV_NOPTS_VALUE)` 和 `if (!ret && *got_packet)` 内部，且外层有 `if (fra... |
| 1787 | ffmpeg-7.0.1 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，代码已通过 `if (!buf) { ... }` 和 `if (len < 12) return -1;` 对 `buf` 进... |
| 1788 | ffmpeg-7.0.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已通过条件 `if (dpd[pos])` 进行了非空检查，确保了指针的有效性。后续对 `dpd[pos]` 的赋值操作是在该条件分支内，不会发生空指针解引用。 |
| 1789 | ffmpeg-7.0.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1507 | FP | FP | 告警点位于 `ff_get_audio_buffer(link, frame->nb_samples)` 调用处，工具认为 `frame` 可能为空指针。但在调用此函数前，代码已通过 `if (av_frame_is_writable... |
| 1790 | ffmpeg-7.0.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 代码中`s->buffer`的指针有效性依赖于调用方传入的`GetBitContext *s`结构体的初始化，切片内无证据表明`s`或`s->buffer`为null。该函数为内联工具函数，其安全性由调用上下文保证，告警属于对内部辅助... |
| 1791 | ffmpeg-7.0.1 | asf_parse_packet | Dereference of null pointer | 1306 | FP | FP | 切片代码中，在循环条件 `for (i = 0; i < asf_st->pkt.size && !asf_st->pkt.data[i]; i++)` 之前，已通过 `av_assert0(asf_st);` 断言 `asf_st`... |
| 1792 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 148 | FP | FP | 告警行代码 `*(const void**)&alpMmxFilter[s*i]= alpSrcPtr[i];` 位于 `if (CONFIG_SWSCALE_ALPHA && hasAlpha)` 条件块内，切片代码显示 `alpS... |
| 1795 | ffmpeg-7.0.1 | unsharp_slice_8 | Dereference of null pointer | 142 | FP | FP | 告警指向的宏定义行 `DEF_UNSHARP_SLICE_FUNC(unsharp_slice, 8)` 本身是一个函数模板的声明，其函数体在宏展开后已完整定义，其中不存在对空指针的解引用。切片代码中显示的宏展开内容包含了完整的函数逻... |
| 1796 | ffmpeg-7.0.1 | mov_write_trak_tag | Dereference of null pointer | 3899 | FP | FP | 告警指向的变量 `sample_aspect_ratio` 来自 `st->sample_aspect_ratio`，通过 `av_q2d` 宏安全转换，不存在空指针解引用。切片代码中 `st` 作为函数参数传入，在解引用前无显式判空... |
| 1797 | ffmpeg-7.0.1 | ebml_parse | Dereference of null pointer | 1371 | FP | FP | 切片代码显示，在警告行（`else if (level->length != EBML_UNKNOWN_LENGTH)`）之前，已经存在条件 `if (matroska->num_levels > 0)` 和 `if (length ... |
| 1798 | ffmpeg-7.0.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 代码在访问 `dpd[pos - 1]`、`dpd[pos + 1]`、`dpd[poa]`、`dpd[pob]` 等数组元素前，已通过 `(!j ｜｜ ...)`、`(j == (out->width - 1) ｜｜ ...)`、`... |
| 1800 | ffmpeg-7.0.1 | ac3_apply_rematrixing | Dereference of null pointer | 387 | FP | FP | 告警点 `flags[bnd]` 的指针 `flags` 在切片代码中未定义，但根据其上下文和函数名 `ac3_apply_rematrixing` 推断，`flags` 应为函数参数或结构体成员，且其有效性由前置条件 `s->rem... |
| 1801 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 682 | FP | FP | 告警点位于FFSWAP宏调用，该宏用于交换两个uint8_t指针指向的值。指针ptr1和ptr2在交换前均已明确初始化且指向有效缓冲区（q->decoded_bytes_buffer及其偏移位置），不存在空指针解引用。 |
| 1802 | ffmpeg-7.0.1 | ff_rdt_parse_header | Dereference of null pointer | 201 | FP | FP | 告警指向的代码行是 `while (len >= 5 && buf[1] == 0xFF)`，该行仅读取 `buf[1]` 的值进行条件判断，并未对 `buf` 指针本身进行解引用。函数入口处 `buf` 作为参数传入，切片中未见其被... |
| 1803 | ffmpeg-7.0.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 代码在访问 `info->key_ids[i]` 之前，已通过 `if (info)` 检查确保 `info` 指针非空，并且 `for` 循环的条件 `i < info->num_key_ids` 确保了循环仅在 `num_key_... |
| 1804 | ffmpeg-7.0.1 | shift_frame | Dereference of null pointer | 153 | FP | FP | 切片代码显示，`av_log` 被宏定义为 `while(0)`，这意味着该函数调用在编译时会被完全移除，因此对 `frame->pts` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 1805 | ffmpeg-7.0.1 | build_table | Dereference of null pointer | 170 | FP | FP | 告警点 `table[j].len` 的访问发生在 `j` 由 `code` 移位计算得出的循环内，`j` 的范围由 `table_nb_bits` 和 `code` 位宽决定，且 `table` 指向通过 `alloc_table`... |
| 1806 | ffmpeg-7.0.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], side_data, key_id_size)` 之前，`info->key_ids` 数组及其每个元素 `info->key_ids[j]` 已在 `av_e... |
| 1807 | ffmpeg-7.0.1 | dump_stream_group | Dereference of null pointer | 678 | FP | FP | 告警行 `printed[st->index] = 1;` 中的指针 `st` 在切片代码中未定义，但根据上下文循环 `for (int k = 0; channel_count > 0 && k < stg->nb_streams;... |
| 1808 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 168 | FP | FP | 对alpMmxFilter的赋值操作被严格保护在条件`CONFIG_SWSCALE_ALPHA && hasAlpha`内，当条件不满足时alpMmxFilter为NULL，但告警点代码行处于该条件分支内，不会发生空指针解引用。 |
| 1809 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该宏及其相关宏（如 OPEN_READER, GET_VLC, CLOSE_READER）均未对指针参数进行解引用操作，仅涉及位读取器的索引和缓存更新，不存在对空指针的解引用逻辑。 |
| 1810 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 告警行 `const int linesize = s->planeheight[plane] > 1 ? in->linesize[plane] / 2 : 0;` 中，对 `in->linesize[plane]` 的访问受前置条... |
| 1811 | ffmpeg-7.0.1 | mov_write_trak_tag | Dereference of null pointer | 3904 | FP | FP | 告警点位于条件判断 `is_clcp_track(track) && st->sample_aspect_ratio.num`，其中 `st` 是函数参数，在切片中可见其被调用时传入，且后续代码中 `st` 被直接使用，表明它不为空。... |
| 1812 | ffmpeg-7.0.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警点位于宏 UPDATE_CACHE 的展开处，该宏操作的是传入的 GetBitContext 指针 s。函数 get_bits 是内联静态函数，其调用方必须提供有效的 s 指针。在典型的FFmpeg上下文中，该函数由经过验证的解析... |
| 1814 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 291 | FP | FP | 告警指向的代码行 `sample[0][x] = src[x * pixel_stride + stride * y];` 是对数组元素的赋值，`sample[0]` 指针已在循环前被正确初始化为指向 `s->sample_buffe... |
| 1815 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 686 | FP | FP | 告警行位于一个条件分支（`js_databuf != q->decoded_bytes_buffer`）内，该分支对指针`ptr2`进行递减操作。切片代码显示`ptr2`被初始化为`js_databuf + js_block_alig... |
| 1816 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 691 | FP | FP | 告警指向的指针 `ptr1` 在循环前被明确初始化为 `q->decoded_bytes_buffer`，该缓冲区在代码中已通过 `q->decoded_bytes_buffer[i] = *ptr2--;` 等方式被赋值，因此指针非... |
| 1818 | ffmpeg-6.1.1 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 告警点位于`s->st->time_base.den`的访问，但切片代码显示，在访问该成员之前，已通过`s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->ic->nb_streams > 1`... |
| 1819 | ffmpeg-6.1.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 412 | FP | FP | 切片代码显示，在访问 `ctx->buffers[buf.index]` 之前，`ctx->buffers` 已在多个条件分支中被检查和使用（例如 `if (ctx->buffers)` 和 `ctx->buffers[i].stat... |
| 1820 | ffmpeg-6.1.1 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | FP | 告警行访问的 `frame` 指针在函数入口处已通过三元运算符确保非空时才使用，当 `frame` 为 NULL 时，`in` 也为 NULL，且后续 `if (!in)` 分支会跳过相关逻辑，因此 `frame->pts` 的访问在... |
| 1821 | ffmpeg-6.1.1 | ebml_read_binary | Dereference of null pointer | 1087 | FP | FP | 切片代码显示，在调用`memset`之前，`av_buffer_realloc`的返回值`ret`已被检查，若失败（ret<0）函数会提前返回，因此只有当`av_buffer_realloc`成功时才会执行到告警行。`av_buffe... |
| 1822 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问 `ptr[2*x]` 和 `ptr[2*x+1]` 之前，`ptr` 指向 `p->data[0]`，`ptr2` 指向 `av_malloc_array` 分配的内存，且循环条件 `x < (w + 7 >> ... |
| 1823 | ffmpeg-6.1.1 | vc1_decode_intra_block | Dereference of null pointer | 964 | FP | FP | 在函数ff_vc1_pred_dc中，dc_val被明确赋值为s->dc_val[0] + s->block_index[n]，并通过*dc_val_ptr = &dc_val[0]传递给调用者，因此dc_val指针不可能为空，对*d... |
| 1824 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 告警指向的指针 `in->data[plane]` 在 `filter_frame` 函数入口作为参数 `in` 传入，该参数非空；切片代码中，`in` 在后续使用前未被重新赋值或置空，且其成员 `data` 的访问发生在对 `in`... |
| 1825 | ffmpeg-6.1.1 | unsharp_slice_16 | Dereference of null pointer | 141 | FP | FP | 告警指向的宏定义行 `DEF_UNSHARP_SLICE_FUNC(unsharp_slice, 16)` 本身是一个宏展开，并非实际的空指针解引用。切片代码显示，宏展开后的函数体包含完整的逻辑和空指针检查（如 `if (!amoun... |
| 1826 | ffmpeg-6.1.1 | enc_open | Dereference of null pointer | 271 | FP | FP | 切片代码显示，在访问 `ost->ist->par->width` 之前，`ost->ist` 和 `ost->ist->par` 的指针有效性已在函数 `set_encoder_id` 中通过 `ost->enc_ctx->code... |
| 1827 | ffmpeg-6.1.1 | ebml_parse | Dereference of null pointer | 1353 | FP | FP | 告警行代码 `level->length != EBML_UNKNOWN_LENGTH` 在 `if (matroska->num_levels > 0)` 条件块内，而 `level` 变量在函数开头已定义为 `matroska->... |
| 1828 | ffmpeg-6.1.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警位于宏 UPDATE_CACHE 的调用处，该宏展开后不涉及指针解引用。切片代码中所有对 gb 的使用都是通过宏进行位操作，没有直接的指针解引用操作，因此工具报告的逻辑错误不成立。 |
| 1829 | ffmpeg-6.1.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 告警指向的代码行 `bit_buf = s->bit_buf;` 是对结构体指针 `s` 的成员进行解引用，但切片代码显示 `s` 是函数的传入参数，且函数内部后续多处对 `s` 的成员进行读写，这表明 `s` 在调用时不应为空。工具... |
| 1830 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 301 | FP | FP | 告警指向的代码行 `sample[0][x] = ((uint16_t*)(src + stride*y))[x] >> (16 - s->bits_per_raw_sample);` 中，`sample[0]` 已在循环前被正确初始... |
| 1831 | ffmpeg-6.1.1 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 告警点位于对`s->st->time_base`的访问，但切片代码显示，在访问`s->st`之前，函数已通过`if (!prft) return AVERROR(ENOMEM);`提前返回，因此`s->st`的访问仅在`av_pack... |
| 1832 | ffmpeg-6.1.1 | ebml_read_sint | Dereference of null pointer | 1014 | FP | FP | 告警指向的代码行 `*num = sign_extend(avio_r8(pb), 8);` 中，`avio_r8` 函数内部已对 `s->buf_ptr` 进行了空指针检查，并确保在缓冲区耗尽时返回0，因此不会发生空指针解引用。 |
| 1833 | ffmpeg-6.1.1 | safe_filename | Dereference of null pointer | 97 | FP | FP | 代码逻辑确保了指针 `f` 在解引用前已通过循环条件 `*f` 进行了非空检查，因此不会发生空指针解引用。 |
| 1834 | ffmpeg-6.1.1 | try_push_frame | Dereference of null pointer | 538 | FP | FP | 告警行 `frame->pts = s->input_frames[0]->pts;` 在切片中受 `if (!nb_samples) goto eof;` 保护，当 `nb_samples` 为0时已跳转，此时 `s->input_... |
| 1835 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，在`s->planeheight[plane] > 1`条件不满足时，`linesize`被赋值为0，但后续使用`linesize`的循环`for (y = 0; y < s->planeheight[plane] - ... |
| 1836 | ffmpeg-6.1.1 | ff_encode_encode_cb | Dereference of null pointer | 285 | FP | FP | 告警指向的代码行 `if (frame->duration)` 位于 `if (frame && ...)` 条件块内，切片代码显示外层已通过 `if (frame)` 检查了指针非空，因此对 `frame->duration` 的访... |
| 1837 | ffmpeg-6.1.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 告警位于宏 UPDATE_CACHE 的展开处，该宏操作的对象 `s` 是函数参数，其是否为 null 取决于调用方。切片代码仅包含宏定义和函数框架，未展示任何对 `s` 的显式空指针解引用或调用方信息，无法确认空指针解引用必然发生。... |
| 1838 | ffmpeg-6.1.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码显示变量 `dpd` 在条件判断 `if (dpd[pos])` 中被解引用，但 `dpd` 在函数作用域内未定义，这很可能是一个函数参数或外部变量，其空值检查应在调用此函数前完成。告警点本身不构成空指针解引用，因为 `dpd... |
| 1839 | ffmpeg-6.1.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1476 | FP | FP | 切片代码显示 `scale_matrix` 在解引用前已通过条件 `s->ps.sps->scaling_list_enable_flag && !(transform_skip_flag && log2_trafo_size > 2... |
| 1840 | ffmpeg-6.1.1 | try_push_frame | Dereference of null pointer | 244 | FP | FP | 代码中 `inbuf[0]` 的赋值来自 `ff_inlink_consume_samples` 函数，该函数仅在成功时设置 `*rframe` 为非 NULL 指针，且 `inbuf` 数组已初始化为 NULL。虽然切片未显示循环 ... |
| 1841 | ffmpeg-6.1.1 | hls_read_header | Dereference of null pointer | 2123 | FP | FP | 告警点 `in_fmt->name` 的访问受前置条件 `if (seg && seg->key_type == KEY_SAMPLE_AES)` 保护，且切片代码显示 `in_fmt` 已在之前的 `av_demuxer_itera... |
| 1842 | ffmpeg-6.1.1 | hls_append_segment | Dereference of null pointer | 1173 | FP | FP | 在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 中，`en` 在条件分支 `if (hls->max_nb_segm... |
| 1843 | ffmpeg-6.1.1 | concat_parse_script | Dereference of null pointer | 557 | FP | FP | 在DIR_DURATION分支中，对file指针的访问受到前置条件`(dir->flags & NEEDS_FILE) && !cat->nb_files`的保护，该条件确保只有在cat->nb_files>0（即已存在文件）时才会执... |
| 1844 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 297 | FP | FP | 切片代码显示，在指针解引用前，`src` 作为函数参数传入，其值由调用者控制，切片内无证据表明其为空。告警点 `((uint16_t*)(src + stride*y))[x]` 是常规的数组索引访问，并非对空指针的解引用。该告警是静... |
| 1845 | ffmpeg-6.1.1 | kalman_smoothen | Dereference of null pointer | 584 | FP | FP | 在循环中，`best_hist_ptr` 被初始化为 NULL，但随后在 `dot > optimal_gain` 条件成立时被赋值为 `ptr`。由于 `ptr` 的初始值指向 `in[-FFMAX(...)]`，且循环条件 `--... |
| 1846 | ffmpeg-6.1.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，对指针 `dpd[pos]` 的访问发生在条件 `if (dpd[pos])` 之后，这表明在解引用 `dp1[pos]` 和 `dp2[pos]` 之前，已经检查了 `dpd[pos]` 非零，因此不会发生空指针解引用。 |
| 1847 | ffmpeg-6.1.1 | id3v2_parse | Dereference of null pointer | 1054 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 函数获取的，该函数仅在找到匹配的tag时返回非空指针。调用点位于 `if (extra_m... |
| 1848 | ffmpeg-6.1.1 | choose_rct_params | Dereference of null pointer | 983 | FP | FP | 告警行访问 src[1] 和 src[2] 发生在 lbd 为 false 的 else 分支内，该分支仅在 lbd 为假时执行。切片中未显示 lbd 变量的定义，但告警规则假设指针可能为空。在代码上下文中，src 数组作为函数参数传... |
| 1849 | ffmpeg-6.1.1 | split_commandline | Dereference of null pointer | 731 | FP | FP | 告警点位于检查 `opt[0] == '-' && opt[1] == '-' && !opt[2]` 的条件判断处，其中 `opt` 是 `argv[optindex++]` 的指针，而 `argv` 来自命令行参数。在调用 `sp... |
| 1850 | ffmpeg-6.1.1 | ebml_read_ascii | Dereference of null pointer | 1069 | FP | FP | 切片代码显示 `av_free` 被定义为 `while(0)` 宏，该宏展开为空操作，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 1851 | ffmpeg-6.1.1 | output_packet | Dereference of null pointer | 1102 | FP | FP | 在访问 `timestamp_packet->unwritten_size` 之前，代码已通过 `if (timestamp_packet)` 检查了指针非空，因此不会发生空指针解引用。 |
| 1853 | ffmpeg-6.1.1 | concat_parse_script | Dereference of null pointer | 561 | FP | FP | 告警点位于DIR_INPOINT分支，该分支仅在满足前置条件`(dir->flags & NEEDS_FILE) && !cat->nb_files`为假时才执行。切片代码显示，当`cat->nb_files`为0时，该条件检查会失败... |
| 1854 | ffmpeg-6.1.1 | ost_add | Dereference of null pointer | 1456 | FP | FP | 告警指向的代码行 `ms->stream_duration = ist->st->duration;` 中，变量 `ist` 在切片代码中已通过条件 `if (ost->ist)` 确保非空，且 `ost->ist` 在函数参数中已传... |
| 1855 | ffmpeg-6.1.1 | sb_decode | Dereference of null pointer | 1346 | FP | FP | 告警点位于 `if (st->innov_save)` 条件块内，该条件已确保 `st->innov_save` 非空，进而推导出 `innov_save` 指针非空。切片代码中 `innov_save` 的赋值 `innov_sav... |
| 1856 | ffmpeg-6.1.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警点位于条件 `if ((*child)->state * 2 == -t->state)` 内，该条件仅在 `t->state` 非零且 `t->state` 为偶数（`!(t->state & 1)`）时才会进入。在进入该条件前... |
| 1857 | ffmpeg-6.1.1 | check_header_mismatch | Dereference of null pointer | 520 | FP | FP | 警告指向的代码行 `curr = curr->next;` 位于一个受循环条件 `i < FLAC_MAX_SEQUENTIAL_HEADERS && curr != child` 严格保护的循环体内，循环确保了在 `curr` 变为... |
| 1858 | ffmpeg-6.1.1 | get_pict_type | Dereference of null pointer | 135 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效性，这确保了 `unit->conten... |
| 1860 | ffmpeg-6.1.1 | mpegts_open_filter | Dereference of null pointer | 493 | FP | FP | 告警指向的 `av_log` 调用已被宏定义为空操作 `while(0)`，不会发生空指针解引用。代码逻辑中 `ts->stream` 的取值虽未在切片中直接体现，但告警的核心是 `av_log` 调用，而该调用已被无害化，因此判定为误报。 |
| 1861 | ffmpeg-6.1.1 | guess_mv | Dereference of null pointer | 428 | FP | FP | 在警告所在行 `else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])` 中，对 `s->last_pic.f` 进行了空指针检查，确保其非空后才访问 `data[0]... |
| 1862 | ffmpeg-6.1.1 | fg_output_frame | Dereference of null pointer | 2111 | FP | FP | 告警行代码为三元运算符的条件表达式部分，仅用于计算 `frame->pts` 的值，并未对任何指针进行解引用操作。切片代码中未发现对空指针的解引用，因此该告警为误报。 |
| 1863 | ffmpeg-6.1.1 | build_table | Dereference of null pointer | 204 | FP | FP | 告警点`table[j].len = -subtable_bits;`处的`table`指针在切片代码中已明确赋值（`table = &vlc->table[table_index];`），且`table_index`的有效性已通过`... |
| 1864 | ffmpeg-6.1.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警点位于 `for (int i = 0; i < nb_chapters; i++)` 循环内，该循环仅在 `if (chapters && nb_chapters)` 和 `if (m)` 两个条件同时为真时才执行。在循环内部，... |
| 1865 | ffmpeg-6.1.1 | locate_option | Dereference of null pointer | 424 | FP | FP | 在调用 `po->name` 之前，`po` 已被 `find_option` 函数返回，该函数保证返回一个指向 `OptionDef` 结构体的指针（即使未找到匹配项，也会返回指向数组末尾的指针，而非NULL）。切片代码中 `fin... |
| 1866 | ffmpeg-6.1.1 | guess_status_pts | Dereference of null pointer | 462 | FP | FP | 告警点位于循环条件判断 `ctx->inputs[i]->status_out == status`，该循环遍历 `ctx->inputs` 数组，其长度由 `ctx->nb_inputs` 控制。在FFmpeg的典型上下文中，`ct... |
| 1867 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警点位于对 `in->data[plane]` 的赋值语句，切片代码显示 `in` 是函数参数，在函数开头已存在非空检查（`if (!out)` 分支依赖于 `out` 的赋值，而 `out` 初始化为 `in` 或 `NULL`，... |
| 1868 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 332 | FP | FP | 告警行 `new_pts = av_rescale_q(...)` 仅在 `if (s->do_video)` 条件为真时执行，而 `outlink` 在同一条件下被赋值为 `ctx->outputs[1]`，非空。切片代码显示 `o... |
| 1869 | ffmpeg-6.1.1 | av_dump_format | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `printed` 数组前，已通过条件 `if (ic->nb_streams && !printed) return;` 确保当 `ic->nb_streams` 非零时 `printed` 不为空。后续访问 ... |
| 1870 | ffmpeg-6.1.1 | check_header_mismatch | Dereference of null pointer | 476 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 之前，`i` 变量已在 `for (i = 0; i < FLAC_MAX_SEQUENTIAL_HEADERS; i++)` 循环中明确定义和初始化，且循环条件确... |
| 1871 | ffmpeg-6.1.1 | update_context_from_thread | Dereference of null pointer | 366 | FP | FP | 切片代码显示，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 条件确保 `hwaccel` 指针... |
| 1872 | ffmpeg-6.1.1 | choose_rct_params | Dereference of null pointer | 984 | FP | FP | 告警行代码位于 `lbd` 为 false 的 else 分支中，该分支访问 `src[1]` 和 `src[2]`。切片代码显示 `src` 数组作为函数参数传入，但未提供其调用上下文以确认其是否可能为 NULL。然而，该函数是静态... |
| 1873 | ffmpeg-6.1.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 告警位于宏 UPDATE_CACHE_32 的展开处，该宏的参数 `s` 已在函数入口通过 `av_assert2` 进行了非空断言。在断言开启的构建中，若 `s` 为空程序将提前终止，因此该解引用在实际运行中不会发生。 |
| 1874 | ffmpeg-6.1.1 | activate | Dereference of null pointer | 186 | FP | FP | 告警点 `frame->pts = s->pts;` 位于 `if (s->eof)` 分支内，该分支中 `frame` 的赋值来源（`ff_get_video_buffer` 或 `av_frame_clone`）均进行了空指针检查... |
| 1875 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 199 | FP | FP | 告警指向的代码行 `ptr[8*x] = ptr2[x] >> 7;` 位于一个受 `if (depth == 1)` 条件保护的块内，而 `ptr2` 在之前的逻辑中已通过 `av_malloc_array` 分配，且分配失败时函数... |
| 1876 | ffmpeg-6.1.1 | h264_field_start | Dereference of null pointer | 1426 | FP | FP | 告警点 `sps->log2_max_frame_num` 的指针 `sps` 在切片代码中已通过 `sps = h->ps.sps;` 赋值，且 `h->ps.sps` 在 `h264_init_ps` 函数中被检查并设置，切片内包... |
| 1877 | ffmpeg-6.1.1 | ff_encode_encode_cb | Dereference of null pointer | 282 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，其执行前提是 `frame` 指针非空（由外层 `if (frame && ...)` 和 `if (!ret && *got_pack... |
| 1878 | ffmpeg-6.1.1 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，代码已通过 `if (!buf)` 检查了 `buf` 是否为 NULL，并且当 `buf` 为 NULL 时，函数会提前返回 ... |
| 1879 | ffmpeg-6.1.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已通过条件 `if (s->peak[i][j] && ...)` 确保 `s->peak[i][j]` 为真，而 `s->peak[i][j]` 仅在之前的循环中当 `dpd[pos... |
| 1880 | ffmpeg-6.1.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1442 | FP | FP | 告警点 `frame->nb_samples` 处的 `frame` 指针在函数入口处已通过 `AVFrame *frame = *rframe;` 赋值，且在此之前已调用 `av_frame_is_writable(frame)`，... |
| 1881 | ffmpeg-6.1.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 代码中`s->buffer`是一个结构体成员，其有效性由调用方保证，且函数内部没有空指针检查逻辑，这是典型的低层位操作函数实现。告警是工具对指针解引用模式的误判，并非真实的空指针解引用错误。 |
| 1882 | ffmpeg-6.1.1 | asf_parse_packet | Dereference of null pointer | 1306 | FP | FP | 告警指向的代码行 `for (i = 0; i < asf_st->pkt.size && !asf_st->pkt.data[i]; i++)` 在访问 `asf_st->pkt.data` 前，切片代码已显示 `asf_st->p... |
| 1883 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 148 | FP | FP | 告警行 `alpMmxFilter[s*i] = alpSrcPtr[i];` 仅在条件 `CONFIG_SWSCALE_ALPHA && hasAlpha` 为真时执行，而切片代码显示 `alpSrcPtr` 在该条件下被初始化为 ... |
| 1884 | ffmpeg-6.1.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在告警行 `dp1[pos] = s->tint[0];` 之前，存在条件判断 `if (dpd[pos])`，这表明对指针 `dpd` 的解引用是受保护的，只有在 `dpd[pos]` 为真（非零）时才会执行后续赋值，... |
| 1885 | ffmpeg-6.1.1 | avc_parse_nal_units | Dereference of null pointer | 92 | FP | FP | 告警指向的代码行 `list->nb_nalus >= nalu_limit` 是对 `list->nb_nalus` 的读取，而非解引用。`list` 指针在该分支的进入条件 `else if (list->nb_nalus >= ... |
| 1886 | ffmpeg-6.1.1 | unsharp_slice_8 | Dereference of null pointer | 142 | FP | FP | 切片代码显示，宏展开后的函数中，指针 `sc` 在 `memset` 调用前已从 `fp->sc` 获取，且 `sc` 被用于数组索引 `sc[sc_offset + y]`，这表明 `sc` 本身非空且指向有效数组。告警点 `{ N... |
| 1887 | ffmpeg-6.1.1 | mov_write_trak_tag | Dereference of null pointer | 3818 | FP | FP | 告警指向的变量 `st->sample_aspect_ratio` 在调用 `av_q2d` 前已通过条件 `st->sample_aspect_ratio.num` 进行了检查，确保其分母不为零，因此不会导致空指针解引用。 |
| 1888 | ffmpeg-6.1.1 | ebml_parse | Dereference of null pointer | 1370 | FP | FP | 告警指向的代码行位于一个条件分支内，该分支仅在 `level->length != EBML_UNKNOWN_LENGTH` 且 `length == EBML_UNKNOWN_LENGTH` 时执行，并会立即返回错误码 `AVERR... |
| 1889 | ffmpeg-6.1.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 代码中访问 `dpd[pos - 1]`、`dpd[pos + 1]`、`dpd[poa]`、`dpd[pob]` 等数组元素前，已通过 `(!j ｜｜ ...)`、`(j == (out->width - 1) ｜｜ ...)`、`... |
| 1891 | ffmpeg-6.1.1 | ac3_apply_rematrixing | Dereference of null pointer | 411 | FP | FP | 切片代码显示，对指针 `flags` 的解引用发生在条件判断 `if (flags[bnd])` 中，但 `flags` 变量在切片内未定义或赋值，无法判断其来源和是否可能为空。然而，该告警为逻辑错误（Dereference of n... |
| 1892 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 682 | FP | FP | 告警点位于FFSWAP宏调用，该宏用于交换两个指针指向的uint8_t值。指针ptr1和ptr2在交换前已被正确初始化，且交换操作在循环条件保护下进行，不会导致空指针解引用。 |
| 1893 | ffmpeg-6.1.1 | ff_rdt_parse_header | Dereference of null pointer | 200 | FP | FP | 告警指向的代码行是 `while (len >= 5 && buf[1] == 0xFF)`，该行仅读取 `buf[1]` 的值，而 `buf` 作为函数参数已通过 `len >= 5` 的条件确保了其长度，且切片中未发现任何将 `b... |
| 1894 | ffmpeg-6.1.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 代码在访问 `info->key_ids[i]` 之前，已通过 `if (info)` 检查确保 `info` 指针非空，且 `for` 循环的条件 `i < info->num_key_ids` 确保了循环仅在 `num_key_i... |
| 1895 | ffmpeg-6.1.1 | shift_frame | Dereference of null pointer | 153 | FP | FP | 告警指向的 `frame` 变量在切片中未定义，但关键证据是 `av_log` 宏被定义为 `while(0)`，这意味着该日志调用在编译时会被完全移除，其内部的 `frame->pts` 解引用永远不会执行，因此不存在空指针解引用风险。 |
| 1896 | ffmpeg-6.1.1 | build_table | Dereference of null pointer | 170 | FP | FP | 告警点位于循环内部，`table` 指针在循环开始前已通过 `table = &vlc->table[table_index];` 正确初始化，且 `j` 的值由 `code` 移位计算得到，在 `table_size` 范围内，不会... |
| 1897 | ffmpeg-6.1.1 | ff_inlink_evaluate_timeline_at_frame | Dereference of null pointer | 1485 | FP | FP | 告警点`frame->pts`的指针`frame`是函数参数，由调用者传入。切片代码显示该函数逻辑完整，仅对`frame`进行解引用以获取`pts`值，并未对`frame`本身进行空指针检查。根据函数语义，调用者应确保传入有效的`fr... |
| 1898 | ffmpeg-6.1.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], side_data, key_id_size)` 之前，`info->key_ids` 数组及其每个元素 `info->key_ids[j]` 已在 `av_e... |
| 1899 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 168 | FP | FP | alpSrcPtr 的赋值受条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 保护，当条件不满足时其值为 NULL，但后续对 alpMmxFilter 的赋值仅在相同的条件分支内执行，因此不会发生空指针解引用。 |
| 1900 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的调用，该宏及其展开的宏 UPDATE_CACHE_LE 在切片中均未定义，无法判断其内部是否会导致空指针解引用。切片中缺少评估该逻辑错误所必需的核心代码信息。 |
| 1901 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 告警点位于条件分支 `s->planeheight[plane] > 1 ? in->linesize[plane] / 2 : 0` 中，当条件为假时，`linesize` 被显式赋值为 0，后续在宏 `CHECK_BIT` 中使用... |
| 1902 | ffmpeg-6.1.1 | mov_write_trak_tag | Dereference of null pointer | 3823 | FP | FP | 告警指向的代码行 `is_clcp_track(track) && st->sample_aspect_ratio.num` 中，`st` 是函数参数，在切片内可见其被多处使用且未被置空，没有证据表明它是空指针。工具可能误判了逻辑条件。 |
| 1903 | ffmpeg-6.1.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该函数是内联的比特流读取工具函数，其参数 `s` 在调用时由调用方传入，函数内部无法判断其是否为 null。该告警是静态分析工具对宏展开和函数内联场景的常见误报，代码逻辑本身... |
| 1904 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 471 | FP | FP | 告警指向宏 DECODE_CODEWORD 的调用，但切片代码显示该宏内部包含 UPDATE_CACHE 和 GET_CACHE 操作，这些操作会从 GetBitContext *gb 读取比特流并更新缓存，不会直接导致空指针解引用。... |
| 1905 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 291 | FP | FP | 告警指向的代码行 `sample[0][x] = src[x * pixel_stride + stride * y];` 是对数组元素的赋值，并非指针解引用。切片代码中未发现任何对空指针的解引用操作，因此该告警为误报。 |
| 1906 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 686 | FP | FP | 告警指向的代码行 `q->decoded_bytes_buffer[i] = *ptr2--;` 在 `else` 分支中，该分支仅在 `js_databuf != q->decoded_bytes_buffer` 时执行。此时 `p... |
| 1907 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 691 | FP | FP | 在警告行 `for (i = 4; *ptr1 == 0xF8; i++, ptr1++)` 中，`ptr1` 已通过 `ptr1 = q->decoded_bytes_buffer;` 初始化，指向有效的缓冲区。循环内的边界检查 `... |
| 1909 | ffmpeg-7.1 | finalize_packet | Dereference of null pointer | 678 | FP | FP | 切片代码显示，在调用 `av_rescale` 函数时，其第三个参数 `c` 的值为 `(uint64_t) s->st->time_base.num << 32`。由于 `s->st->time_base.num` 是整数，左移32... |
| 1910 | ffmpeg-7.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 413 | FP | FP | 告警点 `avbuf = &ctx->buffers[buf.index];` 访问 `ctx->buffers` 前，代码已在多个条件分支中检查了 `ctx->buffers` 是否为 NULL，且 `buf.index` 来自受控... |
| 1911 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 299 | FP | FP | 告警指向的代码行 `sample[0][x] = ((uint16_t*)(src + stride*y))[x];` 是对指针 `src` 进行类型转换和索引访问，切片中 `src` 是函数参数且非空，且其偏移计算 `src + s... |
| 1912 | ffmpeg-7.1 | roq_dpcm_encode_frame | Dereference of null pointer | 180 | FP | FP | 告警行 `avpkt->pts = context->input_frames <= 7 ? context->first_pts : frame->pts;` 中，当 `context->input_frames <= 7` 为假时... |
| 1913 | ffmpeg-7.1 | ebml_read_binary | Dereference of null pointer | 1095 | FP | FP | 根据av_buffer_realloc的函数定义，当分配成功时，它确保*pbuf指向一个有效的AVBufferRef，且其buf成员非空。在调用av_buffer_realloc后，仅当返回值ret < 0时才返回，此时不会执行后续的... |
| 1914 | ffmpeg-7.1 | <global> | Dereference of null pointer | 209 | FP | FP | 告警行 `ptr[2*x] = ptr2[x] >> 4;` 位于条件分支 `if (depth == 1) {...} else {...}` 的 else 块中，该分支由 `if (avctx->pix_fmt == AV_PIX... |
| 1915 | ffmpeg-7.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | FP | 告警行 `*dc_val = dcdiff;` 中，`dc_val` 在函数开头被初始化为 `NULL`，但其值作为指针参数 `&dc_val` 传递给 `ff_vc1_pred_dc` 函数。根据常见编码模式，该函数很可能负责为 `... |
| 1916 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 告警点位于对 `in->data[plane]` 的访问，切片代码显示 `in` 是函数参数且非空，且后续循环条件 `s->planeheight[plane] > 1` 和 `s->planeheight[plane] - 1` 已... |
| 1917 | ffmpeg-7.1 | unsharp_slice_16 | Dereference of null pointer | 172 | FP | FP | 告警指向的代码行是宏定义的一部分，实际展开后是一个函数定义，并非空指针解引用。切片代码中未发现任何对空指针的实际解引用操作，因此该告警为误报。 |
| 1918 | ffmpeg-7.1 | ebml_parse | Dereference of null pointer | 1363 | FP | FP | 告警行代码 `level->length != EBML_UNKNOWN_LENGTH` 在 `if (matroska->num_levels > 0)` 条件块内，且其上层条件 `if (level && level->lengt... |
| 1919 | ffmpeg-7.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码显示，宏 `BITS_AVAILABLE` 被定义为常量 1，这导致 `while` 循环条件 `ret<0x8000000U && BITS_AVAILABLE(re, gb)` 恒为真，使得循环可能无限执行并反复调用 `U... |
| 1920 | ffmpeg-7.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 告警指向的 `s->bit_buf` 解引用发生在函数参数 `PutBitContext *s` 的指针上，该指针在函数入口处未被检查。然而，该函数名为 `put_bits_no_assert`，其设计意图是内部辅助函数，通常由调用者... |
| 1921 | ffmpeg-7.1 | rtp_set_prft | Dereference of null pointer | 646 | FP | FP | 切片代码显示，在调用 `av_rescale_q` 之前，`s->st` 指针的取值未被检查，但告警点 `delta_time = av_rescale_q(...)` 本身并不直接解引用空指针。该行代码仅使用 `s->st->tim... |
| 1922 | ffmpeg-7.1 | ebml_read_sint | Dereference of null pointer | 1022 | FP | FP | 告警指向的代码行 `*num = sign_extend(avio_r8(pb), 8);` 中，`avio_r8` 函数内部已对 `s`（即传入的 `pb`）的 `buf_ptr` 进行了空指针检查，并确保在缓冲区耗尽时返回0，因此... |
| 1923 | ffmpeg-7.1 | safe_filename | Dereference of null pointer | 98 | FP | FP | 代码逻辑确保了指针 `f` 在解引用前已通过循环条件 `*f` 进行了非空检查，且函数内部没有导致 `f` 变为空指针的路径，因此不存在空指针解引用风险。 |
| 1924 | ffmpeg-7.1 | try_push_frame | Dereference of null pointer | 512 | FP | FP | 告警点 `frame->pts = s->input_frames[0]->pts;` 位于 `if (!nb_samples) goto eof;` 之后，此时 `nb_samples` 不为0。根据前面的循环逻辑，`nb_samp... |
| 1925 | ffmpeg-7.1 | dump_stream_group | Dereference of null pointer | 788 | FP | FP | 告警点 `printed[st->index] = 1;` 中，`st` 指针来自 `stg->streams[i]`，而 `stg` 来自 `ic->stream_groups[i]`。切片代码显示 `stg` 在循环前已通过 `s... |
| 1926 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 告警行 `const int linesize = s->planeheight[plane] > 1 ? in->linesize[plane] : 0;` 中，`in` 指针在函数入口处作为非空参数传入，且后续代码中 `in->l... |
| 1927 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 236 | FP | FP | 告警点位于 `av_assert0` 宏内部，该宏用于调试断言，在条件为假时会调用 `abort()` 终止程序。此处的断言检查 `frame` 指针非空且其格式、宽高有效，是编码器初始化时的合理性检查，并非对空指针的常规解引用。该断... |
| 1928 | ffmpeg-7.1 | ff_encode_encode_cb | Dereference of null pointer | 275 | FP | FP | 告警点位于条件判断 `if (frame->duration)`，但切片代码显示，在进入该分支前，外层已存在 `if (frame)` 的检查，并且告警所在函数内部对 `frame` 指针的访问（如 `frame->pts`）均发生在... |
| 1929 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 219 | FP | FP | 告警点位于 `av_assert0` 宏内，该宏用于开发调试，在条件不满足时会调用 `abort()` 终止程序，这属于预期的断言检查逻辑，而非空指针解引用漏洞。 |
| 1931 | ffmpeg-7.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码显示，在告警行 `if (dpd[pos])` 之前，`dpd` 指针已在同一函数中被使用（`dpd[pos] = 255;`），这表明 `dpd` 在该函数上下文中已被定义且非空，否则之前的赋值将导致崩溃。因此，对 `dpd... |
| 1932 | ffmpeg-7.1 | try_push_frame | Dereference of null pointer | 241 | FP | FP | 告警点 `outbuf->pts = inbuf[0]->pts;` 存在对 `inbuf[0]` 可能为 NULL 的指针解引用风险。然而，切片代码显示 `inbuf` 数组在循环中被 `ff_inlink_consume_samp... |
| 1933 | ffmpeg-7.1 | hls_append_segment | Dereference of null pointer | 1183 | FP | FP | 告警行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 中，`en` 在条件 `vs->nb_entries >= hls->... |
| 1934 | ffmpeg-7.1 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 告警点位于DIR_DURATION分支，该分支仅在dir->flags & NEEDS_FILE条件满足且cat->nb_files不为0时才会执行。切片代码显示，在进入switch-case前已对NEEDS_FILE标志进行了检查，... |
| 1935 | ffmpeg-7.1 | dump_argument | Dereference of null pointer | 516 | FP | FP | 函数参数 `a` 在循环条件 `for (p = a; *p; p++)` 中被直接解引用，但该参数由调用者传入，切片中未显示其来源。然而，规则检测的是对已知空指针的解引用，而此处是对指针 `a` 指向的字符内容 `*p` 进行非空判... |
| 1936 | ffmpeg-7.1 | kalman_smoothen | Dereference of null pointer | 585 | FP | FP | 在循环中，`best_hist_ptr` 被初始化为 NULL，但只有在 `optimal_gain > 0` 时才会被赋值。随后，代码检查了 `optimal_gain <= 0` 和 `dot <= 0` 两个条件，如果任一条件为... |
| 1937 | ffmpeg-7.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 告警点位于条件语句 `if (dpd[pos])` 内部，对 `dp1` 和 `dp2` 的赋值仅在 `dpd[pos]` 为真（非零）时执行。切片代码显示 `dpd` 数组在之前的循环中已被赋值，且存在检查其值是否为0的逻辑，因此 ... |
| 1938 | ffmpeg-7.1 | id3v2_parse | Dereference of null pointer | 1055 | FP | FP | 告警点位于条件分支 `extra_func->read(...)`，但切片代码显示 `extra_func` 仅在 `get_extra_meta_func` 返回非空指针时被赋值，且该函数调用前已通过 `extra_func = g... |
| 1939 | ffmpeg-7.1 | set_bframe_chain_length | Dereference of null pointer | 1590 | FP | FP | 告警指向的代码行 `s->input_picture[i - 1]->f->data[0]` 在切片中受到前置条件 `if (s->input_picture[i] && s->input_picture[i]->b_frame_sc... |
| 1940 | ffmpeg-7.1 | split_commandline | Dereference of null pointer | 809 | FP | FP | 告警指向的代码行 `if (opt[0] == '-' && opt[1] == '-' && !opt[2])` 在访问 `opt[1]` 和 `opt[2]` 前，`opt` 已被赋值为 `argv[optindex++]`，而 ... |
| 1941 | ffmpeg-7.1 | ebml_read_ascii | Dereference of null pointer | 1077 | FP | FP | 切片代码显示 `av_free` 被定义为 `while(0)` 宏，其展开后为空操作，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 1942 | ffmpeg-7.1 | output_packet | Dereference of null pointer | 1103 | FP | FP | 告警点访问 `timestamp_packet->unwritten_size` 前，代码已通过 `if (timestamp_packet)` 检查了指针非空，因此不会发生空指针解引用。 |
| 1943 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 286 | FP | FP | 告警点位于 `enc_ctx->width = ost->ist->par->width;`，但该赋值仅在 `enc_ctx->codec_type == AVMEDIA_TYPE_SUBTITLE` 且 `!enc_ctx->wid... |
| 1944 | ffmpeg-7.1 | ebml_read_uint | Dereference of null pointer | 1002 | FP | FP | 代码逻辑上，指针 `num` 在函数入口处已被解引用赋值（`*num = default_value;` 或 `*num = 0;`），表明 `num` 本身不为空，否则程序会在更早的语句崩溃。告警点 `*num = 0;` 是对有效... |
| 1945 | ffmpeg-7.1 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 告警点 `file->inpoint = arg_int[0];` 位于 `case DIR_INPOINT:` 分支，该分支仅在 `dir->flags & NEEDS_FILE` 条件满足且 `cat->nb_files` 非零时... |
| 1946 | ffmpeg-7.1 | sb_decode | Dereference of null pointer | 1348 | FP | FP | 告警点位于条件语句 `if (st->innov_save)` 内部，该条件已确保 `st->innov_save` 非空，因此其偏移量 `innov_save` 也非空，不会发生空指针解引用。 |
| 1947 | ffmpeg-7.1 | choose_rct_params | Dereference of null pointer | 990 | FP | FP | 切片代码显示，在访问 src[1] 和 src[2] 之前，程序已通过 lbd 标志位进行了分支判断。当 lbd 为假时，才会执行到告警行，这表明代码逻辑已考虑了不同的数据格式，且 src 数组的索引访问是受控的，不存在对空指针的解引用。 |
| 1948 | ffmpeg-7.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警行 `if ((*child)->state * 2 == -t->state)` 位于 `if (t->state)` 和 `if (!(t->state & 1))` 条件块内，且外层已通过 `if (t)` 确保 `t` 非... |
| 1949 | ffmpeg-7.1 | check_header_mismatch | Dereference of null pointer | 519 | FP | FP | 切片代码显示，在警告行`curr = curr->next;`执行前，循环条件`curr != child`和`i < FLAC_MAX_SEQUENTIAL_HEADERS`已确保`curr`不为空。此外，后续的`av_assert... |
| 1950 | ffmpeg-7.1 | get_pict_type | Dereference of null pointer | 136 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效性，这确保了 `unit->conten... |
| 1952 | ffmpeg-7.1 | mpegts_open_filter | Dereference of null pointer | 495 | FP | FP | 告警指向的 `av_log` 调用被宏定义为 `while(0)`，是一个空操作，不会发生空指针解引用。切片代码中 `ts->stream` 的值虽未知，但宏展开后该表达式不被求值，因此告警为误报。 |
| 1953 | ffmpeg-7.1 | guess_mv | Dereference of null pointer | 432 | FP | FP | 在警告所在行 `else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])` 中，对 `s->last_pic.f` 的访问已由前一个 `if` 条件 `if (s->la... |
| 1954 | ffmpeg-7.1 | build_table | Dereference of null pointer | 204 | FP | FP | 告警点 'table[j].len = -subtable_bits;' 处的 'table' 指针在切片代码中已通过 'table = &vlc->table[table_index];' 初始化，且 'table_index' 在... |
| 1955 | ffmpeg-7.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警指向的代码行 `AVChapter *chp = chapters[i];` 位于 `if (chapters && nb_chapters)` 和 `for (int i = 0; i < nb_chapters; i++)` ... |
| 1956 | ffmpeg-7.1 | locate_option | Dereference of null pointer | 495 | FP | FP | 在调用 `find_option` 后，代码仅在 `po->name` 为假时（即 `find_option` 返回的指针指向一个 `name` 为 NULL 的 `OptionDef` 结构体）才会访问 `po->name` 和 `... |
| 1957 | ffmpeg-7.1 | <global> | Dereference of null pointer | 78 | FP | FP | 告警位于宏 UPDATE_CACHE 的展开行，该宏及其相关宏（如 OPEN_READER）在切片中均有定义，它们操作的是结构体 GetBitContext 的字段，而非空指针。代码逻辑清晰，没有对空指针进行解引用。 |
| 1958 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警点位于对 `in->data[plane]` 的赋值，切片代码显示 `in` 是函数参数，在调用 `filter_frame` 前已分配，且后续代码中 `in->data` 被安全使用。切片内没有证据表明 `in` 或 `in->... |
| 1959 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 333 | FP | FP | 代码在访问 `outlink` 指针前已通过 `if (s->do_video)` 条件进行保护，当 `s->do_video` 为假时 `outlink` 被初始化为 NULL 但不会被使用，因此不会发生空指针解引用。 |
| 1960 | ffmpeg-7.1 | av_dump_format | Dereference of null pointer | 898 | FP | FP | 告警点 `printed[program->stream_index[k]] = 1;` 位于 `if (ic->nb_streams && !printed) return;` 之后，该条件已确保当 `ic->nb_streams`... |
| 1961 | ffmpeg-7.1 | check_header_mismatch | Dereference of null pointer | 475 | FP | FP | 告警点位于一个循环内的条件判断，用于检查 `curr->link_penalty[i]` 的值。`curr` 指针在循环中通过 `curr = curr->next;` 更新，其有效性由循环条件 `while (curr != chi... |
| 1962 | ffmpeg-7.1 | update_context_from_thread | Dereference of null pointer | 438 | FP | FP | 切片代码中，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 条件确保 `hwaccel` 指针有... |
| 1963 | ffmpeg-7.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 告警指向宏 UPDATE_CACHE_32 的展开，但切片代码显示该宏及其依赖的宏（如 OPEN_READER）均未对指针 's' 进行解引用，仅涉及结构体成员的赋值或位操作。代码逻辑本身没有解引用空指针的风险，属于静态分析工具的逻辑误判。 |
| 1964 | ffmpeg-7.1 | activate | Dereference of null pointer | 186 | FP | FP | 告警点位于 `frame->pts = s->pts;`，但在此行之前，`frame` 指针已在 `s->stop_mode == MODE_ADD` 或 `s->stop_mode == MODE_CLONE` 分支中通过 `ff_... |
| 1965 | ffmpeg-7.1 | <global> | Dereference of null pointer | 200 | FP | FP | 告警指向的代码行 `ptr[8*x] = ptr2[x] >> 7;` 中，`ptr2` 已在前面通过 `ptr = ptr2 = av_malloc_array((w + 15), h);` 分配内存，且分配失败时函数已返回，因此 ... |
| 1966 | ffmpeg-7.1 | check_available | Dereference of null pointer | 616 | FP | FP | 代码中`cu`指针来自`lc->cu`，`lc`作为函数参数传入且切片中未显示其来源，但告警点`cu->pred_mode`的使用位于`n->available && is_available(...)`之后，`is_availabl... |
| 1967 | ffmpeg-7.1 | ff_encode_encode_cb | Dereference of null pointer | 272 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，该条件仅在 `avpkt->pts` 等于 `AV_NOPTS_VALUE` 时才会执行对 `frame->pts` 的访问。切片代码显... |
| 1968 | ffmpeg-7.1 | rtp_parse_one_packet | Dereference of null pointer | 888 | FP | FP | 告警点 `buf[0] & 0xc0` 前存在明确的空指针检查 `if (!buf)`，当 `buf` 为 NULL 时会提前返回，因此后续解引用是安全的。 |
| 1969 | ffmpeg-7.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `s->peak[i][j]` 之前，同一循环内已存在 `if (dpd[pos]) s->peak[i][j] = 1;` 的赋值语句，这确保了 `s->peak[i][j]` 在后续被读取时已被初始化为0或1... |
| 1970 | ffmpeg-7.1 | ost_add | Dereference of null pointer | 1541 | FP | FP | 告警行 `ms->stream_duration = ist->st->duration;` 中使用的指针 `ist` 已在函数开头的条件 `if (ist ｜｜ ofilter)` 中进行了非空检查，并且后续代码中 `ist` 仅在... |
| 1971 | ffmpeg-7.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1420 | FP | FP | 切片代码显示 `scale_matrix` 在条件 `sps->scaling_list_enabled && !(transform_skip_flag && log2_trafo_size > 2)` 为真时被赋值，否则保持为 N... |
| 1972 | ffmpeg-7.1 | nal_parse_units | Dereference of null pointer | 93 | FP | FP | 告警指向的代码行是检查 `list->nb_nalus >= nalu_limit`，该行仅对指针 `list` 的成员进行访问。切片代码显示，在进入该分支前，函数已通过 `if (pb)` 和 `else if (list->nb_... |
| 1973 | ffmpeg-7.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1513 | FP | FP | 告警点位于 `ff_get_audio_buffer(link, frame->nb_samples)` 调用，工具可能认为 `frame` 为空指针。但切片代码显示，在调用此函数前，`frame` 已通过 `AVFrame *fra... |
| 1974 | ffmpeg-7.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 代码中`s->buffer`作为结构体成员被访问，其有效性应由调用者保证；函数内部逻辑是安全的位读取操作，未发现明显的空指针解引用错误。告警可能是工具对指针来源的过度推断。 |
| 1975 | ffmpeg-7.1 | asf_parse_packet | Dereference of null pointer | 1307 | FP | FP | 代码中在访问 `asf_st->pkt.data[i]` 之前，已通过 `av_new_packet` 或 `av_buffer_alloc` 等函数为 `asf_st->pkt.data` 分配了内存，且存在对 `asf_st->p... |
| 1976 | ffmpeg-7.1 | <global> | Dereference of null pointer | 146 | FP | FP | 告警行代码位于 `if (CONFIG_SWSCALE_ALPHA && hasAlpha)` 条件块内，切片代码显示 `alpSrcPtr` 在该条件块之前被初始化为 `NULL` 或一个有效的指针数组。当 `CONFIG_SWSC... |
| 1977 | ffmpeg-7.1 | choose_rct_params | Dereference of null pointer | 991 | FP | FP | 告警指向的代码行 `r = *((const uint16_t*)(src[2] + x*2 + stride[2]*y));` 位于 `else` 分支，该分支仅在 `lbd` 为假时执行。切片中未显示 `lbd` 的定义或赋值，无... |
| 1978 | ffmpeg-7.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 告警指向的代码行 `dp1[pos] = s->tint[0];` 位于一个条件判断 `if (dpd[pos])` 内部，该条件确保了在解引用指针 `dp1` 和 `dp2` 之前，`dpd[pos]` 已被验证为非零（在C语言上下... |
| 1979 | ffmpeg-7.1 | unsharp_slice_8 | Dereference of null pointer | 173 | FP | FP | 告警指向的宏定义行 `DEF_UNSHARP_SLICE_FUNC(unsharp_slice, 8)` 本身是函数声明，并非实际的解引用操作。切片代码中未发现任何对空指针的解引用，工具报告的逻辑错误不成立。 |
| 1980 | ffmpeg-7.1 | mov_write_trak_tag | Dereference of null pointer | 4187 | FP | FP | 告警指向的变量 `st->sample_aspect_ratio` 在切片代码中已通过条件 `track->mode == MODE_MOV` 和 `track->par->codec_type == AVMEDIA_TYPE_VID... |
| 1981 | ffmpeg-7.1 | ebml_parse | Dereference of null pointer | 1380 | FP | FP | 告警指向的代码行（1380行）位于条件分支 `else if (level->length != EBML_UNKNOWN_LENGTH)` 中，该分支仅在 `level` 指针非空时才会执行。而 `level` 指针在函数开头已通过... |
| 1982 | ffmpeg-7.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 代码中dpd[pos-1]、dpd[pos+1]、dpd[poa]、dpd[pob]的访问均在检查数组索引边界（如!j、j == (out->width - 1)、!i、i == (out->height - 1)）之后进行，逻辑上保... |
| 1984 | ffmpeg-7.1 | ac3_apply_rematrixing | Dereference of null pointer | 598 | FP | FP | 切片代码显示，变量 `flags` 在循环 `for (bnd = 0; bnd < block->num_rematrixing_bands; bnd++)` 中被使用，但未在切片内定义或赋值。然而，根据其名称 `flags` 和上... |
| 1985 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 683 | FP | FP | 告警点位于宏 `FFSWAP` 内部，该宏用于交换两个变量的值，其参数 `*ptr1` 和 `*ptr2` 在调用前已被明确赋值且指向有效缓冲区（`q->decoded_bytes_buffer` 及其偏移位置），不存在空指针解引用。... |
| 1986 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 303 | FP | FP | 切片代码显示，在调用 encode_line 函数前，已通过循环对 sample[0][x] 进行了明确的赋值，且 sample 数组的指针来源于已初始化的 sc->sample_buffer，不存在空指针解引用。告警点位于对已赋值数... |
| 1987 | ffmpeg-7.1 | ff_rdt_parse_header | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在告警行 `while (len >= 5 && buf[1] == 0xFF)` 中，`buf` 是函数参数，已通过 `init_get_bits` 的检查确保非空（`if (!buffer)` 会置为 NULL 并返... |
| 1988 | ffmpeg-7.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 告警点位于 `if (info)` 条件块内部，已确保 `info` 非空。循环条件 `i < info->num_key_ids` 确保 `info->key_ids` 数组访问有效，且 `av_free` 函数本身可安全处理空指针... |
| 1989 | ffmpeg-7.1 | shift_frame | Dereference of null pointer | 152 | FP | FP | 切片代码显示，`av_log` 被宏定义为 `while(0)`，这意味着该函数调用在编译时会被移除，其参数 `frame->pts` 永远不会被求值，因此不可能发生对空指针 `frame` 的解引用。 |
| 1990 | ffmpeg-7.1 | build_table | Dereference of null pointer | 170 | FP | FP | 告警点 `table[j].len` 的访问发生在 `j` 由 `code` 移位计算得出的循环内，`j` 的范围由 `table_nb_bits` 和 `code` 位宽保证，不会越界。且 `table` 指针指向通过 `alloc... |
| 1991 | ffmpeg-7.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 告警行 `memcpy(info->key_ids[j], side_data, key_id_size);` 中，`info->key_ids[j]` 指针在 `av_encryption_init_info_alloc` 函数中已... |
| 1992 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 293 | FP | FP | 切片代码显示，在调用 `encode_line` 函数前，`sample[0]` 指针已在循环中被明确赋值（例如 `sample[0][x] = src[x * pixel_stride + stride * y];`），且 `sam... |
| 1993 | ffmpeg-7.1 | dump_stream_group | Dereference of null pointer | 715 | FP | FP | 切片代码显示告警行访问的 `st` 指针来自 `stg->streams[k]` 数组，该数组在循环条件 `k < stg->nb_streams` 内被索引，且 `stg` 在函数开头已从有效数组 `ic->stream_group... |
| 1994 | ffmpeg-7.1 | <global> | Dereference of null pointer | 166 | FP | FP | alpSrcPtr 的赋值受条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 保护，当条件不满足时其值为 NULL。告警行 `*(const void**)&alpMmxFilter[4*i+0]= al... |
| 1995 | ffmpeg-7.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的调用，但切片代码显示该宏最终展开为 UPDATE_CACHE_LE，其具体实现未在切片中提供。由于缺少对宏展开后实际操作的可见性，无法判断空指针解引用是否确实会发生。 |
| 1996 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 告警位于条件表达式 `s->planeheight[plane] > 1 ? in->linesize[plane] / 2 : 0` 中，当条件为假时，`linesize` 被赋值为 0，后续对 `linesize` 的算术运算（如... |
| 1997 | ffmpeg-7.1 | set_bframe_chain_length | Dereference of null pointer | 1605 | FP | FP | 切片代码显示，在访问 `s->input_picture[i]->b_frame_score` 的循环 `for (i = 0; i < b_frames + 1; i++)` 之前，`b_frames` 已通过 `b_frames ... |
| 1998 | ffmpeg-7.1 | mov_write_trak_tag | Dereference of null pointer | 4192 | FP | FP | 告警指向的代码行 `is_clcp_track(track) && st->sample_aspect_ratio.num` 中，`st` 指针已在函数入口作为参数传入，且切片内多处代码（如 `mov_write_tkhd_tag` ... |
| 1999 | ffmpeg-7.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该宏及其依赖的宏定义均未对指针 's' 进行解引用。's' 作为参数传递给宏，宏定义中仅涉及结构体成员访问（如 gb->index），这本身是安全的指针使用，并非空指针解引用... |
| 2000 | ffmpeg-7.1 | <global> | Dereference of null pointer | 472 | FP | FP | 告警指向宏 `DECODE_CODEWORD` 的调用，但切片代码显示该宏仅定义了变量和位操作，并未包含任何指针解引用操作。代码逻辑中也没有对空指针进行解引用的直接证据，因此判定为工具误报。 |
| 2001 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 687 | FP | FP | 告警指向的代码行 `q->decoded_bytes_buffer[i] = *ptr2--;` 中，`ptr2` 被正确初始化为 `js_databuf + js_block_align - 1`，且 `js_databuf` 来自... |
| 2002 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 692 | FP | FP | 在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 已被明确赋值为 `q->decoded_bytes_buffer`，这是一个有效的数组指针，因此解引用 `*ptr1` ... |
| 2003 | ffmpeg-6.0 | show_bits | Dereference of null pointer | 366 | FP | FP | 告警位于宏 UPDATE_CACHE 的调用处，但切片代码显示该宏及其相关宏（OPEN_READER_NOSIZE, SHOW_UBITS）仅涉及位缓冲区的索引和缓存操作，并未对指针 s 进行解引用。逻辑错误告警不成立，属于工具误报。 |
| 2004 | ffmpeg-6.0 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 告警指向的代码行 `s->st->time_base.den` 位于条件 `if (s->last_rtcp_ntp_time != AV_NOPTS_VALUE && s->ic->nb_streams > 1)` 内部，且该条件之... |
| 2005 | ffmpeg-6.0 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 408 | FP | FP | 告警点 `avbuf = &ctx->buffers[buf.index];` 中，`buf.index` 来自 `ioctl` 系统调用 `VIDIOC_DQBUF` 的返回值，该操作由内核驱动保证其有效性，且切片内代码在访问前已检... |
| 2006 | ffmpeg-6.0 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | FP | 告警行 `avpkt->pts = context->input_frames <= 7 ? context->first_pts : frame->pts;` 中，当 `context->input_frames <= 7` 为假时... |
| 2007 | ffmpeg-6.0 | ebml_read_binary | Dereference of null pointer | 1073 | FP | FP | 在调用 `memset` 之前，`av_buffer_realloc` 的返回值 `ret` 已被检查，若成功（`ret >= 0`），则 `bin->buf` 及其 `data` 字段已被正确分配或重新分配，不会为 NULL。因此，... |
| 2008 | ffmpeg-6.0 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问 `ptr[2*x]` 和 `ptr[2*x+1]` 之前，`ptr` 指向 `p->data[0]`，而 `p` 通过 `ff_get_buffer` 成功分配了缓冲区，因此 `ptr` 不为空。告警点位于一个循... |
| 2009 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 119 | FP | FP | 告警点 `uint8_t *val = in->data[plane];` 位于 `if (s->depth <= 8)` 分支内，该分支仅在 `s->planeheight[plane] > 1` 时才会访问 `in->linesi... |
| 2010 | ffmpeg-6.0 | unsharp_slice_16 | Dereference of null pointer | 142 | FP | FP | 告警指向的宏定义行 `{ NULL }` 是一个函数体占位符，并非实际的空指针解引用。在宏展开后，该行位于函数定义内部，是合法的语法结构，不会导致运行时解引用空指针。 |
| 2011 | ffmpeg-6.0 | ebml_parse | Dereference of null pointer | 1339 | FP | FP | 切片代码显示，在访问 `level->length` 之前，已通过 `if (matroska->num_levels > 0)` 检查确保 `level` 指针非空。`level` 指针在函数开头被有条件地赋值，但在此处被访问时，其... |
| 2012 | ffmpeg-6.0 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警位于宏 UPDATE_CACHE 的调用处，该宏展开后不直接涉及指针解引用。切片代码中未发现对空指针的显式解引用操作，且关键宏 BITS_AVAILABLE 被定义为常量 1，表明工具可能误判了宏展开或控制流。 |
| 2013 | ffmpeg-6.0 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 告警指向的 `s->bit_buf` 读取操作发生在函数开头，此时 `s` 指针已在函数调用时由调用方传入，切片内虽无直接的空指针检查，但函数名为 `put_bits_no_assert`，且其逻辑是常规的位操作，属于核心工具函数，通... |
| 2014 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码显示，`sample[0]` 在循环开始前已通过 `sample[i] = s->sample_buffer + ...` 明确赋值，指向有效的缓冲区地址。因此，在后续的 `sample[0][x] = ...` 赋值语句中，... |
| 2015 | ffmpeg-6.0 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 332 | FP | FP | 在访问 `ctx->buffers[i]` 之前，代码已通过 `if (ctx->buffers)` 检查了指针非空，且告警行位于该检查之后的循环内，因此不会发生空指针解引用。 |
| 2016 | ffmpeg-6.0 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 切片代码显示，在调用 `av_rescale_q` 之前，已对 `av_packet_new_side_data` 的返回值 `prft` 进行了空指针检查，若为空则提前返回错误。因此，后续使用 `s->st` 和 `s->last_... |
| 2017 | ffmpeg-6.0 | ebml_read_sint | Dereference of null pointer | 1000 | FP | FP | 切片代码显示，在调用 `avio_r8` 函数前，`pb` 指针作为参数传入，其有效性由调用方保证。函数 `avio_r8` 内部有明确的空指针和缓冲区边界检查（`s->buf_ptr >= s->buf_end`），并返回默认值0，... |
| 2018 | ffmpeg-6.0 | safe_filename | Dereference of null pointer | 97 | FP | FP | 代码逻辑确保了指针 `f` 在解引用前已通过循环条件 `*f` 进行了非空检查，因此不会发生空指针解引用。 |
| 2019 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 117 | FP | FP | 告警行代码 `const int linesize = s->planeheight[plane] > 1 ? in->linesize[plane] : 0;` 中，`in` 指针在函数入口处作为参数传入，且后续代码中 `in` 被... |
| 2020 | ffmpeg-6.0 | of_open | Dereference of null pointer | 2303 | FP | FP | 告警行访问 `ost->enc_ctx->codec` 前，切片代码已通过 `if (ost->filter)` 条件保护，确保了 `ost` 非空且 `ost->filter` 有效，从而间接保证了 `ost->enc_ctx` 的... |
| 2021 | ffmpeg-6.0 | ff_encode_encode_cb | Dereference of null pointer | 244 | FP | FP | 告警指向的代码行 `if (frame->duration)` 位于 `if (frame && ...)` 条件块内，切片代码显示外层已通过 `if (frame)` 检查确保 `frame` 指针非空，因此解引用 `frame->... |
| 2022 | ffmpeg-6.0 | get_sbits | Dereference of null pointer | 315 | FP | FP | 告警指向宏 UPDATE_CACHE 的使用，该宏展开后是对结构体指针 `s` 的成员进行访问。切片代码显示 `s` 作为函数参数传入，在函数内部没有显式的空指针检查，但这是FFmpeg内部常用的位读取器操作，其调用约定要求传入的 `... |
| 2023 | ffmpeg-6.0 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已通过 `if (dpd[pos])` 进行了非空检查，确保了指针的有效性，因此不存在空指针解引用。 |
| 2024 | ffmpeg-6.0 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1476 | FP | FP | 切片代码显示，在访问 `scale_matrix[pos]` 之前，存在条件 `if (s->ps.sps->scaling_list_enable_flag && !(transform_skip_flag && log2_traf... |
| 2025 | ffmpeg-6.0 | try_push_frame | Dereference of null pointer | 243 | FP | FP | 切片代码显示，`inbuf[0]` 的赋值来自 `ff_inlink_consume_samples` 函数，该函数仅在成功时设置 `*rframe`（即 `inbuf[i]`），失败时保持其为 NULL。但告警行 `outbuf->... |
| 2026 | ffmpeg-6.0 | hls_read_header | Dereference of null pointer | 2131 | FP | FP | 告警点位于条件判断 `if (strstr(in_fmt->name, "mov"))`，其中 `in_fmt` 可能为空指针。但切片代码显示，在进入该条件分支前，`in_fmt` 已通过 `av_demuxer_iterate` 循... |
| 2027 | ffmpeg-6.0 | hls_append_segment | Dereference of null pointer | 1180 | FP | FP | 在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 之前，代码已通过 `en = vs->segments;` 将 `e... |
| 2028 | ffmpeg-6.0 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 告警点 `file->user_duration = arg_int[0];` 位于 `case DIR_DURATION:` 分支，该分支仅在 `dir->flags & NEEDS_FILE` 条件满足且 `cat->nb_fil... |
| 2029 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 297 | FP | FP | 告警指向的代码行 `((uint16_t*)(src + stride*y))[x]` 是对指针 `src` 进行偏移和类型转换后的解引用。`src` 是函数参数，在切片中未见其来源，但告警规则为'空指针解引用'。切片内代码逻辑显示 ... |
| 2030 | ffmpeg-6.0 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在告警行`dp1[pos] = s->tint[0];`之前，存在条件判断`if (dpd[pos])`，确保了对`dp1`的访问仅在`dpd[pos]`非零时执行。`dpd`是`dst[pd]`的别名，而`dst`来自... |
| 2031 | ffmpeg-6.0 | id3v2_parse | Dereference of null pointer | 1051 | FP | FP | 告警点位于 `extra_func->read(s, pbx, tlen, tag, extra_meta, isv34);`，其中 `extra_func` 由 `get_extra_meta_func` 返回。切片代码显示，只有当... |
| 2032 | ffmpeg-6.0 | choose_rct_params | Dereference of null pointer | 979 | FP | FP | 告警点位于 `lbd` 为 false 的 else 分支，该分支访问 `src[1]` 和 `src[2]`。切片代码显示 `src` 是函数参数，其来源未知，但函数逻辑表明 `src` 是一个指向三个颜色平面数据的指针数组。在典型... |
| 2033 | ffmpeg-6.0 | split_commandline | Dereference of null pointer | 713 | FP | FP | 告警点位于检查字符串是否为双破折号'--'的逻辑中，代码已通过`opt[0] == '-' && opt[1] == '-'`确保指针`opt`至少指向两个字符，且`opt[2]`的访问仅用于检查是否为空字符，不会导致空指针解引用。 |
| 2034 | ffmpeg-6.0 | ebml_read_ascii | Dereference of null pointer | 1055 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 2035 | ffmpeg-6.0 | output_packet | Dereference of null pointer | 1092 | FP | FP | 在访问 `timestamp_packet->unwritten_size` 之前，代码已通过 `if (timestamp_packet)` 检查了指针非空，因此不会发生空指针解引用。告警是误报。 |
| 2036 | ffmpeg-6.0 | ebml_read_uint | Dereference of null pointer | 980 | FP | FP | 告警点 `*num = 0;` 处的指针 `num` 是函数参数，由调用者传入，在函数内部不可能为 NULL，否则在 `size == 0` 分支的 `*num = default_value;` 处已发生解引用。代码逻辑保证了指针的... |
| 2037 | ffmpeg-6.0 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 告警点位于DIR_INPOINT分支，该分支仅在满足前置条件(NEEDS_FILE)且file指针有效时才会执行。切片代码显示，在进入该分支前，程序已通过标志检查确保cat->nb_files > 0，且file指针由add_file... |
| 2038 | ffmpeg-6.0 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警行 `if ((*child)->state * 2 == -t->state)` 位于 `if (t->state)` 和 `if (!(t->state & 1))` 条件块内，且外层已通过 `if (t)` 确保 `t` 非... |
| 2040 | ffmpeg-6.0 | init_output_stream_encode | Dereference of null pointer | 3153 | FP | FP | 切片代码显示，在访问 `ost->ist->par` 之前，已通过 `switch (enc_ctx->codec_type)` 确保当前处理的是 `AVMEDIA_TYPE_SUBTITLE` 类型，且 `ost` 和 `enc_c... |
| 2041 | ffmpeg-6.0 | guess_mv | Dereference of null pointer | 428 | FP | FP | 在告警行 `else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])` 中，对 `s->last_pic.f` 的访问已由前序条件 `if (s->last_pic.f ... |
| 2042 | ffmpeg-6.0 | build_table | Dereference of null pointer | 203 | FP | FP | 告警点 `table[j].len = -subtable_bits;` 处的 `table` 指针在调用 `alloc_table` 成功后已通过 `table = &vlc->table[table_index];` 正确初始化，... |
| 2043 | ffmpeg-6.0 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警点位于 `for (int i = 0; i < nb_chapters; i++)` 循环内，该循环仅在 `if (chapters && nb_chapters)` 条件为真时执行。切片代码显示，在告警行 `AVChapter... |
| 2044 | ffmpeg-6.0 | locate_option | Dereference of null pointer | 424 | FP | FP | 在调用 `po = find_option(options, cur_opt);` 后，`find_option` 函数保证返回一个指向 `OptionDef` 结构体的指针（即使未找到匹配项，也会返回指向数组末尾的指针，该指针的 `... |
| 2045 | ffmpeg-6.0 | guess_status_pts | Dereference of null pointer | 446 | FP | FP | 告警行代码 `ctx->inputs[i]->status_out` 在循环条件 `i < ctx->nb_inputs` 的保护下访问，`ctx->inputs` 数组索引 `i` 是安全的。切片中未发现 `ctx->inputs[... |
| 2046 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 148 | FP | FP | 告警点位于对 `in->data[plane]` 的赋值语句，切片显示 `in` 是函数参数且已在前序逻辑中作为源帧使用，未发现其为空的证据。宏 `CHECK_BIT` 中对 `val` 的访问受 `dst` 判空保护，且 `in` ... |
| 2047 | ffmpeg-6.0 | av_dump_format | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `printed` 数组前，已通过条件 `if (ic->nb_streams && !printed) return;` 确保当 `ic->nb_streams` 非零时 `printed` 指针非空。后续访问... |
| 2048 | ffmpeg-6.0 | choose_rct_params | Dereference of null pointer | 980 | FP | FP | 切片代码显示，在lbd为假的分支中，对src[0]、src[1]、src[2]进行了指针解引用。告警点位于src[2]的解引用行，但src数组作为函数参数传入，其有效性由调用者保证。切片内没有证据表明src[2]为NULL，且代码逻辑... |
| 2049 | ffmpeg-6.0 | activate | Dereference of null pointer | 168 | FP | FP | 告警点位于 `frame->pts = s->pts;`，但在此行之前，`frame` 指针已在多个分支中被分配（通过 `ff_get_video_buffer` 或 `av_frame_clone`）并进行了空指针检查，确保非空后才... |
| 2050 | ffmpeg-6.0 | <global> | Dereference of null pointer | 199 | FP | FP | 告警指向的代码行 `ptr[8*x] = ptr2[x] >> 7;` 位于一个条件分支 `if (depth == 1)` 内部，而 `ptr2` 仅在 `if (maplength && depth < 8)` 分支中被分配内存并... |
| 2051 | ffmpeg-6.0 | ff_encode_encode_cb | Dereference of null pointer | 241 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，该条件确保仅在 `avpkt->pts` 为 `AV_NOPTS_VALUE` 时才执行 `avpkt->pts = frame->pt... |
| 2052 | ffmpeg-6.0 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，代码已通过 `if (!buf)` 和 `if (len < 12)` 进行了检查。当 `buf` 为 NULL 或 `len`... |
| 2053 | ffmpeg-6.0 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 告警行 `dpd[pos] = 255;` 中 `dpd` 指针在函数开头通过三元条件运算符赋值，其来源 `out->data[...]` 由调用方传入，切片中未见其为空的证据。代码逻辑是对帧数据进行处理，`dpd` 在循环前已定义并... |
| 2054 | ffmpeg-6.0 | ff_inlink_make_frame_writable | Dereference of null pointer | 1423 | FP | FP | 告警点位于 `ff_get_audio_buffer(link, frame->nb_samples)` 调用处，工具认为 `frame` 可能为空指针。但在调用此函数前，代码已通过 `if (av_frame_is_writable... |
| 2055 | ffmpeg-6.0 | get_bits1 | Dereference of null pointer | 381 | FP | FP | 代码中`s->buffer`的访问基于`s->index`，而`s`作为函数参数，其有效性应由调用者保证。在典型的比特流读取上下文中，`GetBitContext`结构体及其`buffer`字段在调用`get_bits1`前已被正确初... |
| 2056 | ffmpeg-6.0 | asf_parse_packet | Dereference of null pointer | 1302 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data[i]` 之前，已通过 `av_new_packet` 或 `av_buffer_alloc` 等函数为 `asf_st->pkt.data` 分配了内存，且存在对 `asf_st... |
| 2057 | ffmpeg-6.0 | <global> | Dereference of null pointer | 148 | FP | FP | 告警行代码 `*(const void**)&alpMmxFilter[s*i] = alpSrcPtr[i];` 位于 `if (CONFIG_SWSCALE_ALPHA && hasAlpha)` 条件块内，切片代码显示 `alp... |
| 2058 | ffmpeg-6.0 | add_interval | Dereference of null pointer | 1035 | FP | FP | 告警指向的代码行是条件判断的一部分，用于比较结构体成员，并非解引用空指针。代码逻辑表明，只有在 `ref >= 0` 且 `inter` 非空时才会进入该分支，而 `inter` 作为函数参数，其有效性应由调用者保证。切片中未发现空指... |
| 2059 | ffmpeg-6.0 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 告警点位于条件语句 `if (dpd[pos])` 内部，这表明对指针 `dpd` 的访问是受保护的，只有在 `dpd[pos]` 为真（非零）时才会执行后续的赋值操作，因此不会发生空指针解引用。 |
| 2060 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 335 | FP | FP | 告警行`s->out->pts = in->pts;`位于`s->do_video`条件块内，该条件块仅在`s->out`被成功分配（`ff_get_video_buffer`）或成功获取可写帧（`ff_inlink_make_fra... |
| 2061 | ffmpeg-6.0 | unsharp_slice_8 | Dereference of null pointer | 143 | FP | FP | 告警指向的宏定义行 `DEF_UNSHARP_SLICE_FUNC(unsharp_slice, 8)` 本身是函数声明，不会导致空指针解引用。切片代码中展开的宏函数体包含空指针检查（`if (!amount)`）和安全的数组初始化，... |
| 2062 | ffmpeg-6.0 | ebml_parse | Dereference of null pointer | 1356 | FP | FP | 告警指向的代码行位于一个条件分支内，该分支仅在 `level->length != EBML_UNKNOWN_LENGTH` 且 `length == EBML_UNKNOWN_LENGTH` 时执行，并会立即返回错误码 `AVERR... |
| 2063 | ffmpeg-6.0 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 代码中`dpd`指针指向`out->data`数组的有效元素，且循环内对`dpd`的访问均在数组边界检查（如`!j`、`j == (out->width - 1)`、`!i`、`i == (out->height - 1)`）的保护下... |
| 2064 | ffmpeg-6.0 | get_bits_le | Dereference of null pointer | 351 | FP | FP | 告警指向宏 UPDATE_CACHE_LE 中对指针 gb->buffer 的解引用，但该函数为内联辅助函数，其参数 s (GetBitContext*) 的合法性应由调用者保证。在典型的比特流读取上下文中，s 在进入此类函数前已被有... |
| 2065 | ffmpeg-6.0 | ac3_apply_rematrixing | Dereference of null pointer | 410 | FP | FP | 告警点 `flags[bnd]` 的变量 `flags` 在切片代码中未定义，但根据其上下文（用于判断是否执行重矩阵化）及函数名 `ac3_apply_rematrixing` 推断，`flags` 应为函数内部或结构体中表示频带是否... |
| 2066 | ffmpeg-6.0 | av_encryption_init_info_free | Dereference of null pointer | 219 | FP | FP | 代码在访问 `info->key_ids[i]` 之前，已通过 `if (info)` 检查确保 `info` 指针非空，并且 `for` 循环的条件 `i < info->num_key_ids` 也依赖于 `info`。告警点 `... |
| 2067 | ffmpeg-6.0 | shift_frame | Dereference of null pointer | 150 | FP | FP | 切片代码显示，告警点引用的变量 `frame` 在切片中未定义，无法判断其来源。但关键证据是，宏定义 `av_log` 被展开为 `while(0)`，这意味着该日志调用在实际编译后是空操作，`frame->pts` 的访问不会被执行... |
| 2068 | ffmpeg-6.0 | build_table | Dereference of null pointer | 169 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 2069 | ffmpeg-6.0 | ff_inlink_evaluate_timeline_at_frame | Dereference of null pointer | 1466 | FP | FP | 告警点 `frame->pts` 的访问发生在函数参数 `frame` 非空的上下文中，且切片代码中未发现任何将 `frame` 置为空的逻辑。函数 `ff_inlink_evaluate_timeline_at_frame` 的签名... |
| 2070 | ffmpeg-6.0 | av_encryption_init_info_get_side_data | Dereference of null pointer | 278 | FP | FP | 告警点位于 `memcpy(info->key_ids[j], side_data, key_id_size);`，但切片代码显示，在调用 `av_encryption_init_info_alloc` 时，当 `key_id_siz... |
| 2071 | ffmpeg-6.0 | <global> | Dereference of null pointer | 168 | FP | FP | 对alpMmxFilter的赋值操作受到条件`CONFIG_SWSCALE_ALPHA && hasAlpha`的保护，当条件不满足时alpSrcPtr为NULL，但alpMmxFilter的赋值不会执行，因此不会发生空指针解引用。 |
| 2072 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 146 | FP | FP | 告警位于条件表达式 `s->planeheight[plane] > 1 ? in->linesize[plane] / 2 : 0` 中，当条件为假时，`linesize` 被赋值为 0，后续在宏 `CHECK_BIT` 中使用 `... |
| 2073 | ffmpeg-6.0 | get_bits | Dereference of null pointer | 330 | FP | FP | 告警位于宏 UPDATE_CACHE 的展开处，该宏操作的是传入的 GetBitContext 结构体指针 s。切片代码显示 s 作为函数参数传入，在函数内部被使用，但未显示其来源。然而，函数 get_bits 是内联工具函数，其调用... |
| 2074 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 291 | FP | FP | 切片代码显示，告警行 `sample[0][x] = src[x * pixel_stride + stride * y];` 中 `src` 是函数参数，`sample[0]` 已正确指向 `s->sample_buffer` 分配... |
| 2075 | ffmpeg-6.0 | bits_priv_refill_32_be | Dereference of null pointer | 85 | FP | FP | 在 `UNCHECKED_BITSTREAM_READER` 未定义的情况下，代码在调用 `AV_RB32(bc->ptr)` 前已通过 `if (bc->ptr >= bc->buffer_end) return -1;` 检查了指... |
| 2076 | git-2.46.0 | add_parents_only | Dereference of null pointer | 1929 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且仅在 `it` 非空时才继续执行。因此，对 `it->t... |
| 2077 | git-2.46.0 | get_mode | Dereference of null pointer | 63 | FP | FP | 告警点 `*special = SPECIAL_STDIN;` 位于 `if (path == file_from_standard_input)` 分支内，该分支仅在 `path` 指向静态常量字符串 `"-"` 时执行。由于 `p... |
| 2078 | git-2.46.0 | sync_submodule | Dereference of null pointer | 1273 | FP | FP | 告警行 `sub->name` 的指针 `sub` 由 `submodule_from_path` 函数返回，该函数在切片中已定义，其返回值可能为 NULL，但调用前有 `if (!is_submodule_active(the_re... |
| 2079 | git-2.46.0 | crlf_to_git | Dereference of null pointer | 573 | FP | FP | 告警点位于循环内，对指针 `src` 进行解引用。切片代码显示，在进入该循环前，函数已通过条件 `if (!buf && !src) return 1;` 和 `if (!buf) return 1;` 对 `src` 和 `buf`... |
| 2080 | git-2.46.0 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码显示，在警告行 `d = delta[c = (end += d)[-1]];` 之前，变量 `d` 已在循环条件 `while (lim - end >= d)` 中被使用，这表明 `d` 在进入循环时已被初始化且不为零，因... |
| 2081 | git-2.46.0 | diffcore_merge_broken | Dereference of null pointer | 295 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环已通过 `struct diff_filepair *pp = q->queue[j];` 获取了 `pp` 指针，且外层循环已明确处理了 `q->queue[i]` 为 NU... |
| 2082 | git-2.46.0 | parse_options_step | Dereference of null pointer | 900 | FP | FP | 告警点 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 在进入该分支前已被赋值为 `arg + 1`（第45行），且 `arg` 是 `ctx->argv[0]`，保证非空。... |
| 2083 | git-2.46.0 | rstrip_ref_components | Dereference of null pointer | 2117 | FP | FP | 切片代码显示，在 for 循环条件 `p[i] == '/' ? i++ : *p++` 中，对指针 `p` 的递增操作 `*p++` 是合法的，它先解引用 `p` 再递增指针，而 `p` 指向字符串 `refname` 且已通过 `... |
| 2084 | git-2.46.0 | parse_options | Dereference of null pointer | 1046 | FP | FP | 告警点位于 `isascii(*ctx.opt)`，但在进入该分支前，`parse_options_step` 函数已明确将 `ctx->opt` 重置为 NULL，且当 `ctx->opt` 为 NULL 时，`ctx->argv[... |
| 2085 | git-2.46.0 | process_entry | Dereference of null pointer | 3413 | FP | FP | 告警行位于 `RENAME_ONE_FILE_TO_TWO` 分支内，该分支仅在 `ci->ren2` 非空时才会执行。切片代码显示，在进入此分支前有 `if (ci->ren2)` 断言，确保了 `ci->ren2` 的有效性，因此... |
| 2086 | git-2.46.0 | verify_absent | Dereference of null pointer | 2526 | FP | FP | 告警点 `ce` 是函数的输入参数，调用方必须提供非空指针，否则在访问 `ce->ce_flags` 前程序已崩溃。静态分析工具未能识别这一前置的调用约定，属于典型的误报。 |
| 2087 | git-2.46.0 | show_pack_info | Dereference of null pointer | 1688 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，随后在循环中访问该数组。访问发生在 `if (deepest_delta)` 条件块之... |
| 2088 | git-2.46.0 | output | Dereference of null pointer | 548 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util->matching` 的值已在 `while (j < b->nr && b_util->matching < 0)` 循... |
| 2089 | git-2.46.0 | limit_list | Dereference of null pointer | 1492 | FP | FP | 告警指向的代码行 `if (obj->flags & UNINTERESTING)` 中，`obj` 是从 `commit->object` 获取的，而 `commit` 来自 `pop_commit` 函数，该函数在栈非空时返回有效... |
| 2090 | git-2.46.0 | add_lines_to_move_detection | Dereference of null pointer | 1055 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`l->id` 的值已通过 `ALLOC_GROW_BY(entry_list, id, 1, entry_list_alloc)` 确保 `entry_list` ... |
| 2091 | git-2.46.0 | limit_list | Dereference of null pointer | 1488 | FP | FP | 告警指向的代码行 `if (revs->max_age != -1 && (commit->date < revs->max_age))` 中，`commit` 变量来自 `pop_commit` 函数，该函数在栈非空时返回有效指针，... |
| 2092 | git-2.46.0 | lstrip_ref_components | Dereference of null pointer | 2079 | FP | FP | 代码中 `p` 被赋值为 `refname`，而 `refname` 是函数参数，在切片中未显示为空。警告行 `p[i] == '/' ? i++ : *p++` 中的 `*p` 解引用发生在 `p` 指向 `refname` 字符串... |
| 2093 | git-2.46.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当`strmap_get_entry`返回NULL时，函数直接返回`map->default_value`，并未对空指针进行解引用。告警是对控制流逻辑的误判。 |
| 2094 | git-2.46.0 | coalesce_lines | Dereference of null pointer | 264 | FP | FP | 在告警行 `newend = newend->prev;` 之前，`newend` 仅在 `directions[i][j] == MATCH` 分支内被赋值，而该分支仅在 `i` 和 `j` 均不为零时进入。由于外层循环 `whil... |
| 2095 | git-2.46.0 | merge_ort_internal | Dereference of null pointer | 5217 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--` 之前，`opt->priv->call_depth++` 已确保 `opt->priv` 不为空，且递归调用 `merge_ort_internal` 后未修改... |
| 2096 | git-2.46.0 | process_parents | Dereference of null pointer | 1175 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，且 `repo_parse_commit_gently` 调用失败时会 `continue`，不会执行到该行。切片内逻辑保证了空指针解引用... |
| 2097 | git-2.46.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1364 | FP | FP | 告警指向的代码行 `write_message(msg->buf, msg->len, name, 0)` 中，`msg` 是函数参数且已在调用前被初始化，`name` 由 `git_path_commit_editmsg()` 返回... |
| 2098 | git-2.46.0 | gather_stats | Dereference of null pointer | 51 | FP | FP | 切片代码显示函数参数 `buf` 和 `size` 在循环前未进行空指针检查，但循环条件 `i < size` 确保了当 `size` 为0时循环不会执行，因此不会发生对 `buf` 的无效解引用。告警为逻辑误判。 |
| 2099 | git-2.46.0 | append_strategy | Dereference of null pointer | 229 | FP | FP | 切片代码显示，函数`append_strategy`仅将指针`s`存入数组`use_strategies`，并未对`s`进行解引用操作。告警消息‘Dereference of null pointer’与切片中的实际代码行为不符，属于... |
| 2100 | git-2.46.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码显示函数直接对数组指针进行赋值和递增操作，未涉及空指针解引用。告警的逻辑错误不成立，因为 `array->v` 和 `value` 的使用本身不会导致空指针解引用，除非调用方传入的 `array` 为 NULL，但这不是本行代... |
| 2101 | git-2.46.0 | add_lines_to_move_detection | Dereference of null pointer | 1058 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，其范围与数组... |
| 2102 | git-2.46.0 | coalesce_lines | Dereference of null pointer | 272 | FP | FP | 告警点位于条件判断 `if (lline->prev)` 中，但根据切片代码，`lline` 被赋值为 `newend`，而 `newend` 在循环中通过 `newend = newend->prev` 或 `newend = ll... |
| 2103 | git-2.46.0 | apply_one_fragment | Dereference of null pointer | 3025 | FP | FP | 切片代码显示告警行位于一个条件块内，该条件块检查 `inaccurate_eof` 等多个前置条件，且对 `postimage.line_allocated` 的访问是在 `preimage.nr - 1` 索引上，而 `add_li... |
| 2104 | git-2.46.0 | try_to_commit | Dereference of null pointer | 1698 | FP | FP | 告警指向的 `commit_tree_extended` 函数调用行，其参数 `parents` 在切片代码的所有可达路径中均被正确初始化（可能为 `NULL` 或有效链表），且该函数内部会处理 `parents` 为 `NULL` ... |
| 2105 | git-2.46.0 | prepare_attr_stack | Dereference of null pointer | 1013 | FP | FP | 告警行 `*stack = info->prev;` 之前已调用 `bootstrap_attr_stack` 确保 `*stack` 非空，且 `info` 被赋值为 `*stack`，因此 `info` 非空，解引用 `info-... |
| 2106 | git-2.46.0 | split_graph_merge_strategy | Dereference of null pointer | 2269 | FP | FP | 告警点位于条件分支 `if (ctx->num_commit_graphs_after == 2)` 内部，而在此分支之前，变量 `g` 已在循环中被更新，且循环条件 `while (g && ...)` 保证了只有当 `g` 非空时... |
| 2107 | git-2.46.0 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 函数逻辑清晰，通过条件判断 `if (line == 0)` 确保了当 `line` 不为0时才会访问 `ends[line]`。切片中 `ends` 作为参数传入，其有效性由调用方保证，且函数内部没有引入空指针解引用。告警为工具的逻... |
| 2108 | git-2.46.0 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对参数 `ref_iterator` 进行任何解引用操作，因此不存在空指针解引用问题。 |
| 2109 | git-2.46.0 | find_bisection | Dereference of null pointer | 439 | FP | FP | 在告警行 `list->item = best->item;` 之前，`best` 指针已通过 `if (best) {` 检查非空，且 `list` 在函数开头通过 `list = last;` 赋值，而 `last` 在循环中被初... |
| 2110 | git-2.46.0 | verify_absent_1 | Dereference of null pointer | 2485 | FP | FP | 告警点 `ce->name` 的指针 `ce` 由函数参数传入，切片代码中所有对 `ce` 的使用（如 `ce_namelen(ce)`、`ce_to_dtype(ce)`）均未进行空指针检查，表明函数设计上假定 `ce` 非空。调用... |
| 2111 | git-2.46.0 | merge_ref_iterator_advance | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 已在 `if (!iter->current)` 分支中被检查，且 `while` 循环仅在 `selection & ITER_YIEL... |
| 2112 | git-2.46.0 | try_to_commit | Dereference of null pointer | 1582 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，工具认为 `current_head` 可能为空导致空指针解引用。但在切片代码中，该行位于 `if (flags &... |
| 2113 | git-2.46.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点是对函数`match_pathspec`的调用，其参数`ce`和`pathspec`由上层函数传入，切片中未显示其来源。但函数`ce_path_match`是静态内联的辅助函数，其设计目的是安全地封装对`match_pathsp... |
| 2114 | git-2.46.0 | cmp_local_packs | Dereference of null pointer | 481 | FP | FP | 告警点检查 `pl->next` 前，`pl` 已从全局变量 `local_packs` 初始化。`local_packs` 在文件作用域初始化为 NULL，但在调用 `cmp_local_packs` 前，必然有其他函数（如 `ad... |
| 2115 | git-2.46.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 677 | FP | FP | 在函数入口处，指针 `tws` 被解引用以访问 `tws->next`，但该指针在调用前已被检查非空。切片代码显示 `tws` 是函数参数，其有效性应由调用者保证，且函数内部逻辑仅在 `n`（即 `tws->next`）非空时才进行后... |
| 2116 | git-2.46.0 | unload_one_branch | Dereference of null pointer | 2049 | FP | FP | 在进入while循环前，条件`cur_active_branches && cur_active_branches >= max_active_branches`确保了`cur_active_branches`大于0，这意味着`act... |
| 2117 | git-2.46.0 | process_entries | Dereference of null pointer | 4451 | FP | FP | 告警点位于一个BUG断言检查的printf语句中，该代码路径仅在内部一致性检查失败时触发，用于打印调试信息并主动终止程序。这属于防御性编程的错误处理逻辑，而非对空指针的实际解引用。 |
| 2118 | git-2.46.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已在循环中被填充，且 `remotes->nr == 1` 的条件保证了列表至少有一个... |
| 2119 | git-2.46.0 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警点位于循环条件 `curr = kwset->trie->next`，但切片代码显示，在进入该循环前，`kwset->trie` 已在 `for (curr = last = kwset->trie; curr; curr = c... |
| 2120 | git-2.46.0 | cmd_merge | Dereference of null pointer | 1529 | FP | FP | 告警点位于检查 `use_strategies[i]->attr` 属性的条件判断中，切片代码显示 `use_strategies` 数组在循环前已正确初始化，且循环变量 `i` 在有效范围内，不存在空指针解引用。 |
| 2121 | git-2.46.0 | get_ref_map | Dereference of null pointer | 545 | FP | FP | 告警点位于 `for (i = 0; i < fetch_refspec->nr; i++)` 循环中，`fetch_refspec` 指针在之前的条件判断中已被明确赋值：若 `refmap.nr` 非零则指向 `&refmap`，否... |
| 2122 | git-2.46.0 | setup_scoreboard | Dereference of null pointer | 2841 | FP | FP | 告警点位于 while 循环条件 `c->parents` 的检查，但切片代码显示，在进入该循环前，变量 `c` 被赋值为 `final_commit`，而 `final_commit` 仅在 `sb->reverse && sb->... |
| 2123 | git-2.46.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 代码逻辑确保了在访问 `sb->buf[len]` 之前，已通过条件 `sb->buf != strbuf_slopbuf` 检查了 `sb->buf` 不为空指针（`strbuf_slopbuf` 是一个静态分配的缓冲区，非空）。因... |
| 2124 | git-2.46.0 | prepare_attr_stack | Dereference of null pointer | 1021 | FP | FP | 告警行 `while ((*stack)->origin)` 在进入循环前，`*stack` 已通过 `*stack = info->prev;` 被赋值为 `info->prev`。`info` 来自 `info = *stack;... |
| 2125 | git-2.46.0 | assert_sane_strbuf | Dereference of null pointer | 36 | FP | FP | 告警点位于宏 `check_char` 内部，该宏用于单元测试断言，其逻辑是检查条件并报告失败，而非正常的程序执行路径。即使 `buf->buf` 为 NULL，也属于测试用例要捕获的错误情况，不会导致程序产生空指针解引用漏洞。 |
| 2126 | git-2.46.0 | show_pack_info | Dereference of null pointer | 1710 | FP | FP | 切片代码显示，在循环访问 `chain_histogram[i]` 之前，已通过条件 `if (deepest_delta)` 和 `CALLOC_ARRAY` 宏确保当 `deepest_delta` 非零时，`chain_hist... |
| 2127 | git-2.49.0 | image_remove_last_line | Dereference of null pointer | 363 | FP | FP | 代码在访问 `img->line[img->line_nr - 1]` 前，虽然切片未显示对 `img->line_nr` 的校验，但根据函数名 `image_remove_last_line` 和上下文推断，该函数应在 `img->... |
| 2128 | git-2.49.0 | add_parents_only | Dereference of null pointer | 1941 | FP | FP | 在调用 `get_reference` 后，如果 `it` 为 NULL 且 `revs->ignore_missing` 为真，函数会提前返回 0，避免了后续的空指针解引用。告警点 `if (it->type != OBJ_TAG)... |
| 2129 | git-2.49.0 | get_mode | Dereference of null pointer | 65 | FP | FP | 告警点位于 `*special = SPECIAL_STDIN;`，但切片代码显示，该行仅在 `path == file_from_standard_input` 时执行，此时 `special` 参数由调用者传入，在切片中无法确认其... |
| 2130 | git-2.49.0 | sync_submodule | Dereference of null pointer | 1288 | FP | FP | 在调用 `submodule_from_path` 后，未检查返回值 `sub` 是否为 NULL 便直接解引用 `sub->name`，这确实存在空指针解引用的风险。然而，切片代码显示，在调用 `submodule_from_pat... |
| 2131 | git-2.49.0 | <global> | Dereference of null pointer | 88 | FP | FP | 告警点位于单元测试代码中，`check_str(out[0], "a")` 在调用前已通过 `check(out != NULL)` 确保了 `out` 非空，且 `parse_names` 函数在成功时返回以 NULL 结尾的有效字... |
| 2132 | git-2.49.0 | crlf_to_git | Dereference of null pointer | 583 | FP | FP | 告警指向的代码行 `unsigned char c = *src++;` 位于 `do...while` 循环内，循环条件 `while (--len);` 保证了在进入循环体前 `len` 大于0，因此 `src` 指针在解引用前已... |
| 2133 | git-2.49.0 | cwexec | Dereference of null pointer | 675 | FP | FP | 切片代码显示，在访问 `trie->accepting` 和 `trie->shift` 之前，`trie` 变量是通过 `next[c]` 赋值的，而 `next` 数组来自 `kwset->next`。虽然切片未显示 `next`... |
| 2134 | git-2.49.0 | diffcore_merge_broken | Dereference of null pointer | 291 | FP | FP | 在访问 `pp->one` 和 `pp->two` 之前，外层循环已通过 `if (pp->broken_pair)` 检查了 `pp` 的有效性，且 `pp` 是从 `q->queue[j]` 直接赋值而来，该数组在循环中被遍历，`... |
| 2135 | git-2.49.0 | parse_options_step | Dereference of null pointer | 906 | FP | FP | 告警点 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 在进入该分支前已被赋值为 `arg + 1`（第49行），且 `arg` 是 `ctx->argv[0]` 非空字符串... |
| 2136 | git-2.49.0 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | FP | 代码逻辑中，`p` 指针在循环条件 `p[i]` 中被解引用，但 `p` 被初始化为 `refname`，而 `refname` 是函数参数，由调用方传入且未被切片显示为 null。在 `for` 循环的条件判断中，`p[i]` 等价... |
| 2137 | git-2.49.0 | clar_summary_init | Dereference of null pointer | 76 | FP | FP | 在调用 `summary->filename = filename` 之前，`summary` 指针的初始化或分配未包含在切片中，但告警点位于 `fopen` 失败检查之后。如果 `fopen` 失败，`clar_abort` 函数将... |
| 2138 | git-2.49.0 | parse_options | Dereference of null pointer | 1052 | FP | FP | 告警点 `*ctx.opt` 在 `parse_options_step` 函数中已被显式初始化为 `NULL`，并且在 `PARSE_OPT_UNKNOWN` 分支的 `unknown:` 标签处，`ctx->opt` 被再次赋值为... |
| 2139 | git-2.49.0 | <global> | Dereference of null pointer | 82 | FP | FP | 告警点位于单元测试代码中，对 `out[0]` 的访问发生在 `check(out != NULL)` 之后，已确保指针非空。测试逻辑清晰，不存在空指针解引用。 |
| 2141 | git-2.49.0 | verify_absent | Dereference of null pointer | 2537 | FP | FP | 告警点位于条件判断 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))`，其中 `ce` 作为函数参数被解引用。该函数为静态辅助函数，其调用方... |
| 2142 | git-2.49.0 | show_pack_info | Dereference of null pointer | 1776 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，而在使用前通过 `if (is_delta_type(obj->type))` 条件保... |
| 2143 | git-2.49.0 | output | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `j < b->nr` 条件确保非空，且 `b_util->matching` 在 `while (j < b-... |
| 2144 | git-2.49.0 | clar__fail | Dereference of null pointer | 698 | FP | FP | 切片代码显示对指针 `error` 进行解引用，但 `error` 变量本身未在切片中定义或初始化。根据函数名 `clar__fail` 及其参数推断，这很可能是一个全局或静态的错误处理结构体指针，在程序上下文中已被正确初始化，工具误... |
| 2145 | git-2.49.0 | limit_list | Dereference of null pointer | 1499 | FP | FP | 告警指向的代码行 `if (obj->flags & UNINTERESTING)` 中，`obj` 是从 `commit` 结构体中的 `&commit->object` 获取的，而 `commit` 是从 `pop_commit`... |
| 2146 | git-2.49.0 | add_lines_to_move_detection | Dereference of null pointer | 1060 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，确保了访问的... |
| 2147 | git-2.49.0 | limit_list | Dereference of null pointer | 1495 | FP | FP | 切片代码显示，在告警行 `if (revs->max_age != -1 && (commit->date < revs->max_age))` 中，`commit` 变量来自 `pop_commit(&original_list)`... |
| 2148 | git-2.49.0 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | FP | 代码逻辑中，指针 `p` 在循环条件 `p[i]` 中用于索引访问，其本身在循环前被赋值为 `refname` 且未被修改，因此不可能为 NULL。警告所指的 `p[i]` 解引用是安全的，属于静态分析工具的逻辑误判。 |
| 2149 | git-2.49.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当 `strmap_get_entry` 返回 NULL 时，函数返回 `map->default_value`，这是对空指针的合理处理，并未发生解引用空指针的操作。 |
| 2150 | git-2.49.0 | coalesce_lines | Dereference of null pointer | 251 | FP | FP | 在告警行 `newend = newend->prev;` 之前，`newend` 变量已在循环 `for (j = 1, newend = newline; ...)` 中被初始化为 `newline`，且后续通过 `if (new... |
| 2151 | git-2.49.0 | merge_ort_internal | Dereference of null pointer | 5219 | FP | FP | 告警点 `opt->priv->call_depth--;` 位于 `opt->priv->call_depth++` 之后，且处于同一代码块内。`opt->priv` 在函数入口处未被检查，但切片中 `opt` 作为函数参数传入，且... |
| 2152 | git-2.49.0 | assert_sane_strbuf | Dereference of null pointer | 35 | FP | FP | cl_assert 是一个单元测试断言宏，其目的是在测试失败时终止程序，而非在生产逻辑中执行。对 `buf->buf` 的访问发生在断言表达式中，用于验证字符串缓冲区是否以空字符结尾，这属于测试框架的正常使用模式，并非逻辑错误或空指针... |
| 2153 | git-2.49.0 | process_parents | Dereference of null pointer | 1182 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，并且 `repo_parse_commit_gently` 函数调用后也使用了 `continue` 处理错误，因此 `p` 在访问其 `... |
| 2154 | git-2.49.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1366 | FP | FP | 告警点 `msg->buf` 的指针 `msg` 是函数参数，由调用者传入，在切片内未发现其为空的赋值或检查。但函数 `write_message` 内部会检查 `buf` 参数，若 `msg->buf` 为空，`len` 为0，写入... |
| 2155 | git-2.49.0 | gather_stats | Dereference of null pointer | 52 | FP | FP | 切片代码显示告警行 `unsigned char c = buf[i];` 位于一个有效的循环内，`buf` 指针作为函数参数传入，循环条件 `i < size` 确保了访问不会越界。没有证据表明 `buf` 在该上下文中为 null... |
| 2156 | git-2.49.0 | clar_parse_args | Dereference of null pointer | 496 | FP | FP | 告警点位于 `explicit->suite_idx = j;`，其中 `j` 是循环变量，其值由 `for (j = 0; j < _clar_suite_count; ++j)` 控制，确保 `j` 在有效范围内，不会为 NULL... |
| 2157 | git-2.49.0 | append_strategy | Dereference of null pointer | 234 | FP | FP | 切片代码显示，函数将指针 s 存入数组 use_strategies，并未对其进行解引用操作。告警消息提及的'解引用空指针'逻辑错误在此代码片段中并未发生，属于工具误报。 |
| 2158 | git-2.49.0 | merge_ref_iterator_advance | Dereference of null pointer | 205 | FP | FP | 告警点 `iter->current` 的指针解引用发生在 `selection & ITER_YIELD_CURRENT` 条件分支内，而该分支仅在 `iter->select` 函数返回包含 `ITER_YIELD_CURRENT... |
| 2159 | git-2.49.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 函数 `strvec_push_nodup` 的入参 `array` 和 `value` 在切片中未显示其来源，但函数内部逻辑是标准的数组元素赋值操作，其安全性完全依赖于调用方确保 `array` 指针有效且 `array->v` 有... |
| 2160 | git-2.49.0 | add_lines_to_move_detection | Dereference of null pointer | 1063 | FP | FP | 切片代码显示，`entry_list` 通过 `ALLOC_GROW_BY` 宏进行动态分配和增长，该宏会确保分配内存并初始化为零。在访问 `entry_list[l->id]` 之前，`l->id` 的值要么来自已存在的 `s->e... |
| 2161 | git-2.49.0 | image_remove_first_line | Dereference of null pointer | 355 | FP | FP | 告警点是对 `strbuf_remove` 函数的调用，该函数内部实现稳健，即使传入空指针或零长度也会安全处理。切片中未显示 `img`、`img->buf` 或 `img->line` 为空指针的证据，且函数调用本身不会导致空指针解引用。 |
| 2162 | git-2.49.0 | coalesce_lines | Dereference of null pointer | 259 | FP | FP | 告警点位于条件判断 `if (lline->prev)` 中，但根据切片代码，`lline` 被赋值为 `newend`，而 `newend` 在循环中通过 `newend = newend->prev` 或 `newend = ll... |
| 2163 | git-2.49.0 | write_table | Dereference of null pointer | 65 | FP | FP | 告警指向的代码行 `refs[i].refname = (*names)[i] = xstrfmt(...);` 中，`xstrfmt` 函数返回动态分配的内存指针，不会返回 NULL，因此不存在对空指针的解引用。该告警是静态分析工具... |
| 2164 | git-2.49.0 | strvec_splice | Dereference of null pointer | 69 | FP | FP | 切片代码显示，在调用ALLOC_GROW宏之前，如果`array->v == empty_strvec`，会将其显式设置为NULL。ALLOC_GROW宏内部包含REALLOC_ARRAY，当`x`（即`array->v`）为NULL... |
| 2166 | git-2.49.0 | try_to_commit | Dereference of null pointer | 1700 | FP | FP | 告警指向的 `commit_tree_extended` 函数调用行，其参数 `parents` 在切片中所有代码路径下均被正确初始化（可能为 `NULL` 或有效链表），且该函数内部会处理 `parents` 为 `NULL` 的情... |
| 2167 | git-2.49.0 | prepare_attr_stack | Dereference of null pointer | 978 | FP | FP | 告警行 `*stack = info->prev;` 之前，`info` 被赋值为 `*stack`，而 `*stack` 在 `bootstrap_attr_stack` 中被确保非空（若为空则初始化）。因此 `info` 非空，解... |
| 2168 | git-2.49.0 | split_graph_merge_strategy | Dereference of null pointer | 2281 | FP | FP | 告警点位于条件分支 `if (ctx->num_commit_graphs_after == 2)` 内部，该条件确保进入分支时 `ctx->num_commit_graphs_after` 为 2。根据前面的逻辑，当 `flags`... |
| 2169 | git-2.49.0 | get_nth_line | Dereference of null pointer | 879 | FP | FP | 函数逻辑清晰，通过条件判断 `if (line == 0)` 确保了当 `line` 不为0时才会访问 `ends[line]`。切片中 `ends` 作为参数传入，其有效性由调用方保证，且函数内部没有引入空指针解引用路径。告警为逻辑误判。 |
| 2170 | git-2.49.0 | <global> | Dereference of null pointer | 15 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对参数 `ref_iterator` 进行任何解引用操作，因此不存在空指针解引用问题。 |
| 2171 | git-2.49.0 | find_bisection | Dereference of null pointer | 440 | FP | FP | 在 `if (best)` 条件块内访问 `list->item`，而 `list` 在函数开头被赋值为 `last`，`last` 在循环中被初始化为 `NULL` 但随后在循环中被更新为 `p`，因此当 `best` 非空时，`l... |
| 2172 | git-2.49.0 | <global> | Dereference of null pointer | 1541 | FP | FP | 告警点 'use_strategies[i]->attr & NO_FAST_FORWARD' 位于循环中，且切片代码显示 use_strategies 数组是通过 add_strategies 函数填充的，该函数确保添加的策略指针有... |
| 2173 | git-2.49.0 | verify_absent_1 | Dereference of null pointer | 2496 | FP | FP | 告警点 `ce->name` 的指针 `ce` 由函数参数传入，调用方必须提供非空指针，否则在调用 `ce_namelen(ce)` 宏时已发生解引用。切片内逻辑表明 `ce` 在告警点前已被安全使用，不存在空指针解引用。 |
| 2174 | git-2.49.0 | <global> | Dereference of null pointer | 182 | FP | FP | 告警位于单元测试代码中，`arr[0] = 42;` 行之前已通过 `REFTABLE_ALLOC_GROW_OR_NULL` 宏检查并确保 `arr != NULL`，且测试逻辑明确验证了分配成功，因此不会发生空指针解引用。 |
| 2175 | git-2.49.0 | try_to_commit | Dereference of null pointer | 1584 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，但切片代码显示在调用此语句前，`current_head` 已通过 `parse_head` 函数获取，且当 `pa... |
| 2176 | git-2.49.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点调用的函数参数 `ce` 来自函数入参，在切片代码中未发现任何对 `ce` 的显式空值检查或赋值，但函数 `ce_path_match` 是一个静态辅助函数，其调用方应保证传入有效的 `ce` 指针。直接解引用 `ce->nam... |
| 2177 | git-2.49.0 | cmp_local_packs | Dereference of null pointer | 509 | FP | FP | 告警点 `if (!pl->next)` 处的 `pl` 由 `local_packs` 初始化，而 `local_packs` 是一个全局变量，在函数调用前可能已被正确赋值。切片中虽未显示其赋值点，但函数逻辑表明它旨在处理一个链表，... |
| 2178 | git-2.49.0 | t_log_write_read | Dereference of null pointer | 224 | FP | FP | 告警指向 `names[i] = xstrdup(name);` 行，但切片中 `names` 数组未定义，推测为测试代码中已定义且不为空。`xstrdup` 函数内部会检查 `strdup` 返回值，失败时会调用 `die` 终止程... |
| 2179 | git-2.49.0 | reftable_stack_reload_once | Dereference of null pointer | 351 | FP | FP | 告警点 `new_readers[new_readers_len] = rd;` 处，`new_readers` 已在 `names_len` 非零时通过 `reftable_calloc` 分配内存，且 `new_readers_l... |
| 2180 | git-2.49.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 678 | FP | FP | 代码在解引用指针 `n` 之前，已通过 `if (n)` 进行了空指针检查，确保了 `n` 非空时才执行后续操作，因此不存在空指针解引用风险。 |
| 2181 | git-2.49.0 | unload_one_branch | Dereference of null pointer | 2065 | FP | FP | 在进入while循环前，条件`cur_active_branches && cur_active_branches >= max_active_branches`确保了`cur_active_branches`大于0，因此`activ... |
| 2182 | git-2.49.0 | cmd_add | Dereference of null pointer | 431 | FP | FP | 函数参数 `struct repository *repo` 在函数入口处未被检查，但根据函数签名和常见编程惯例，`cmd_add` 作为命令处理函数，其 `repo` 参数由调用者传入且不应为空。切片代码中仅包含对 `repo` 成... |
| 2183 | git-2.49.0 | apply_one_fragment | Dereference of null pointer | 2991 | FP | FP | 切片代码显示，在访问 `postimage.line[postimage.line_nr - 1]` 之前，`postimage.line_nr` 已通过 `image_add_line` 函数递增，确保了数组索引有效。此外，`ina... |
| 2184 | git-2.49.0 | process_entries | Dereference of null pointer | 4453 | FP | FP | 告警指向的代码行位于一个条件检查分支内，该分支仅在数据结构状态异常时触发，并通过BUG宏主动终止程序。这是预期的错误处理逻辑，而非对空指针的意外解引用。 |
| 2185 | git-2.49.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 告警指向的代码行 `friendly_ref_names.items[0].string` 仅在 `remotes->nr == 1` 的条件下执行，而切片代码显示 `friendly_ref_names` 列表在此条件下已通过循环添... |
| 2186 | git-2.49.0 | clar_run_suite | Dereference of null pointer | 399 | FP | FP | 告警点 `report->suite = _clar.active_suite;` 中，`report` 指针由 `calloc` 分配并已检查是否为 NULL，分配失败会调用 `clar_abort` 退出程序，因此 `report... |
| 2187 | git-2.49.0 | kwsprep | Dereference of null pointer | 504 | FP | FP | 告警点位于循环 `for (curr = kwset->trie->next; curr; curr = curr->next)`，其中 `curr` 由 `kwset->trie->next` 初始化。切片代码显示，`kwset->... |
| 2188 | git-2.49.0 | <global> | Dereference of null pointer | 188 | FP | FP | 告警指向的代码行 `arr[alloc - 1] = 42;` 位于单元测试中，其上下文明确显示 `arr` 在赋值前已通过 `REFTABLE_ALLOC_GROW_OR_NULL` 宏确保非空且 `alloc` 已增长，不会发生空... |
| 2189 | git-2.49.0 | get_ref_map | Dereference of null pointer | 545 | FP | FP | 告警指向的代码行 `for (i = 0; i < fetch_refspec->nr; i++)` 中，`fetch_refspec` 指针在切片代码中已明确被赋值：它要么指向 `&refmap`（当 `refmap.nr` 非零时... |
| 2190 | git-2.49.0 | setup_scoreboard | Dereference of null pointer | 2842 | FP | FP | 告警点位于 while 循环条件 `c->parents` 的检查，但切片显示 `c` 由 `final_commit` 赋值，而 `final_commit` 在 `sb->reverse && sb->revs->first_pa... |
| 2191 | git-2.49.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 代码在访问 `sb->buf[len]` 前已通过 `if (sb->buf != strbuf_slopbuf)` 检查，确保 `sb->buf` 不为空指针或指向特殊缓冲区。当 `sb->buf` 等于 `strbuf_slopb... |
| 2192 | git-2.49.0 | t_table_refs_for | Dereference of null pointer | 577 | FP | FP | 变量 `want_names` 在切片代码中未声明和初始化，无法判断其是否为NULL。但告警点位于循环内，且循环后调用了 `free_names(want_names)`，该函数明确检查NULL指针。结合代码逻辑和参考标签，推断 `w... |
| 2193 | git-2.49.0 | prepare_attr_stack | Dereference of null pointer | 986 | FP | FP | 在进入while循环前，*stack已被赋值为info->prev，而info来自*stack，这表明*stack在循环前已被更新，且循环条件检查(*stack)->origin，这隐含了*stack不为空的假设。结合函数逻辑，该循环... |
| 2194 | git-2.49.0 | show_pack_info | Dereference of null pointer | 1798 | FP | FP | 切片代码显示，在访问 `chain_histogram[i]` 之前，存在条件 `if (deepest_delta)` 保护，当该条件为真时，会通过 `CALLOC_ARRAY` 为指针分配内存，因此指针不会为 null；当条件为假... |
| 2195 | git-2.44.0 | add_parents_only | Dereference of null pointer | 1898 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且当 `revs->ignore_missing` 为真时... |
| 2196 | git-2.44.0 | table_iter_next_block | Dereference of null pointer | 327 | FP | FP | 在告警行 `src->bi.br->full_block_size` 中，`src->bi.br` 在切片内没有直接的赋值，但通过分析 `block_reader_start` 函数可知，`it->br` 被赋值为传入的 `br` 参... |
| 2197 | git-2.44.0 | get_mode | Dereference of null pointer | 63 | FP | FP | 告警点 `*special = SPECIAL_STDIN;` 位于 `if (path == file_from_standard_input)` 分支内，该分支仅在 `path` 指向静态常量字符串 `"-"` 时执行，`spec... |
| 2198 | git-2.44.0 | sync_submodule | Dereference of null pointer | 1267 | FP | FP | 告警行 `sub->name` 的指针 `sub` 来自 `submodule_from_path` 函数，该函数在切片中被调用两次且其返回值被直接使用。在 `submodule_to_gitdir` 的函数定义中，当 `submod... |
| 2199 | git-2.44.0 | crlf_to_git | Dereference of null pointer | 569 | FP | FP | 告警点位于循环内部，对指针 `src` 进行解引用。在进入该循环前，代码已通过条件 `if (!buf && !src)` 和 `if (!buf)` 对 `src` 和 `buf` 的组合状态进行了检查，并且 `src` 作为函数参... |
| 2200 | git-2.44.0 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码显示，在访问 `trie->shift` 和 `trie->accepting` 之前，`trie` 变量是通过 `next[c]` 赋值的，而 `next` 数组来自 `kwset->next`。虽然切片未显示 `kwset... |
| 2201 | git-2.44.0 | diffcore_merge_broken | Dereference of null pointer | 292 | FP | FP | 告警点 `pp->broken_pair` 位于内层循环，其外层循环已确保 `pp`（即 `q->queue[j]`）不为 NULL，因为外层循环条件 `j < q->nr` 且 `q->queue` 数组在初始化后未被置空（除了显式... |
| 2202 | git-2.44.0 | parse_options_step | Dereference of null pointer | 891 | FP | FP | 告警点 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 在进入该分支前已通过 `ctx->opt = arg + 1;` 被赋值为非空指针（`arg` 是 `ctx->arg... |
| 2203 | git-2.44.0 | rstrip_ref_components | Dereference of null pointer | 2113 | FP | FP | 切片代码显示，在 for 循环的条件判断 `p[i]` 之前，指针 `p` 已被初始化为 `refname`，而 `refname` 是函数的非空参数，因此 `p` 不可能为空。循环条件 `p[i]` 是安全的，不会发生空指针解引用。 |
| 2204 | git-2.44.0 | parse_options | Dereference of null pointer | 1037 | FP | FP | 告警点 `*ctx.opt` 在 `parse_options_step` 函数中已被显式初始化为 `NULL`，并且在 `PARSE_OPT_UNKNOWN` 分支的 `unknown:` 标签处，当 `ctx->opt` 不为空时... |
| 2205 | git-2.44.0 | process_entry | Dereference of null pointer | 3357 | FP | FP | 告警点位于switch-case语句的RENAME_ONE_FILE_TO_TWO分支内，该分支仅在ci->ren2不为NULL时才会执行。切片代码显示，在进入此分支前有一个条件判断`if (ci->ren2)`，并且紧随其后有一个`... |
| 2206 | git-2.44.0 | verify_absent | Dereference of null pointer | 2523 | FP | FP | 告警点检查的是指针 `o` 是否为 null，但在函数 `verify_absent_1` 中，`o` 被直接使用前，其上层调用函数 `verify_absent` 已先检查了 `o->skip_sparse_checkout`，这隐... |
| 2207 | git-2.44.0 | show_pack_info | Dereference of null pointer | 1698 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，随后在循环中访问 `chain_histogram` 前，已通过 `if (is_de... |
| 2208 | git-2.44.0 | output | Dereference of null pointer | 546 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `j < b->nr` 条件确保非空，且 `b_util->matching` 在 `while (j < b-... |
| 2209 | git-2.44.0 | limit_list | Dereference of null pointer | 1460 | FP | FP | 切片代码显示，在告警行 `if (obj->flags & UNINTERESTING)` 中，`obj` 指针来自 `&commit->object`，而 `commit` 在循环中通过 `pop_commit(&original_... |
| 2210 | git-2.44.0 | add_lines_to_move_detection | Dereference of null pointer | 1034 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，确保了访问的... |
| 2211 | git-2.44.0 | limit_list | Dereference of null pointer | 1456 | FP | FP | 告警指向的代码行 `if (revs->max_age != -1 && (commit->date < revs->max_age))` 中，`commit` 变量来自 `pop_commit` 函数，该函数在输入非空时返回有效指针... |
| 2212 | git-2.44.0 | lstrip_ref_components | Dereference of null pointer | 2075 | FP | FP | 代码中 `p` 指针指向 `refname` 字符串，循环条件 `p[i]` 在 `p` 非空时是安全的。`refname` 作为函数参数，在调用 `xstrdup` 时已被验证非空，且循环逻辑正确，不存在空指针解引用。 |
| 2213 | git-2.44.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当 `strmap_get_entry` 返回 NULL 时，函数直接返回 `map->default_value`，并未对空指针进行解引用。告警是对控制流逻辑的误判。 |
| 2214 | git-2.44.0 | coalesce_lines | Dereference of null pointer | 262 | FP | FP | 告警点位于 `directions[i][j] == MATCH` 分支内，该分支仅在 `i != 0 ｜｜ j != 0` 时进入。由于循环前 `i` 和 `j` 已递减（`i--; j--;`），且外层循环确保了 `i` 和 `j... |
| 2215 | git-2.44.0 | process_parents | Dereference of null pointer | 1143 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，且 `repo_parse_commit_gently` 调用失败时会 `continue`，不会执行到告警行。切片内逻辑保证了 `p` ... |
| 2216 | git-2.44.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1282 | FP | FP | 告警指向的 `write_message` 调用中，`msg->buf` 的指针 `msg` 由函数参数传入，切片内无任何证据表明 `msg` 可能为空。函数逻辑在调用 `write_message` 前未对 `msg` 进行空指针检... |
| 2217 | git-2.44.0 | gather_stats | Dereference of null pointer | 49 | FP | FP | 代码中`buf`指针作为函数参数传入，在循环前未进行空指针检查，但循环条件`i < size`在`size`为0时会直接跳过循环，且后续对`buf[size-1]`的访问也有`size >= 1`的保护，因此不会发生空指针解引用。 |
| 2218 | git-2.44.0 | append_strategy | Dereference of null pointer | 227 | FP | FP | 切片代码显示，函数`append_strategy`仅将指针`s`存入数组`use_strategies`，并未对`s`进行解引用操作。告警消息‘解引用空指针’与代码逻辑不符，属于工具误判。 |
| 2219 | git-2.44.0 | add_lines_to_move_detection | Dereference of null pointer | 1037 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，并与数组大小... |
| 2220 | git-2.44.0 | coalesce_lines | Dereference of null pointer | 270 | FP | FP | 告警指向的代码行 `if (lline->prev)` 在 `directions[i][j] == NEW` 分支内，此时 `lline` 被赋值为 `newend`。在进入此分支前，`newend` 已在循环中通过 `if (ne... |
| 2221 | git-2.44.0 | apply_one_fragment | Dereference of null pointer | 2990 | FP | FP | 切片代码显示，在告警行（postimage.line_allocated[postimage.nr - 1].len--）之前，已通过条件 `if (inaccurate_eof && old > oldlines && old[-1... |
| 2222 | git-2.44.0 | try_to_commit | Dereference of null pointer | 1615 | FP | FP | 告警指向的代码行 `commit_tree_extended(msg->buf, msg->len, ...)` 中，`msg` 参数在函数内部已通过条件分支确保非空（例如第31行 `msg = &commit_msg;`），且 `c... |
| 2223 | git-2.44.0 | prepare_attr_stack | Dereference of null pointer | 1011 | FP | FP | 告警行 `*stack = info->prev;` 在 `bootstrap_attr_stack` 调用之后执行，该函数确保 `*stack` 不为空（若为空则进行初始化），因此 `info` 指针非空，解引用 `info->pr... |
| 2224 | git-2.44.0 | split_graph_merge_strategy | Dereference of null pointer | 2239 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，代码已通过 `while (g && ...)` 循环确保 `g` 不为空，且进入 `if (ctx->num_commit_graphs_afte... |
| 2225 | git-2.44.0 | read_cached_dir | Dereference of null pointer | 2515 | FP | FP | 切片代码显示，在访问 `cdir->untracked` 之前，函数 `read_cached_dir` 已被调用，这表明 `cdir` 及其 `untracked` 成员很可能已在外部被正确初始化并传递进来。告警点 `cdir->u... |
| 2226 | git-2.44.0 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 函数逻辑通过条件判断 `if (line == 0)` 将输入 `line` 分为两种情况处理。当 `line` 不为0时，才执行 `ends[line]` 的数组访问。切片中虽未显示 `ends` 数组的边界信息，但函数设计表明 `... |
| 2227 | git-2.44.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码显示函数`strvec_push_nodup`仅执行数组赋值操作，未涉及任何指针解引用。告警消息‘Dereference of null pointer’与代码逻辑不符，属于工具误报。 |
| 2228 | git-2.44.0 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对参数 `ref_iterator` 进行任何解引用操作，因此不存在空指针解引用问题。 |
| 2229 | git-2.44.0 | find_bisection | Dereference of null pointer | 437 | FP | FP | 告警点位于条件分支 `if (best) {` 内部，该分支仅在 `best` 非空时执行。`best` 是 `do_find_bisection` 的返回值，切片中 `do_find_bisection` 函数有明确的返回逻辑，可能... |
| 2230 | git-2.44.0 | verify_absent_1 | Dereference of null pointer | 2482 | FP | FP | 告警点位于函数调用 `check_leading_path(ce->name, ce_namelen(ce), 0)` 中，工具可能认为 `ce` 指针为空。但在函数入口，`ce` 作为参数传入，且切片代码中多处（如 `ce->nam... |
| 2231 | git-2.44.0 | merge_ref_iterator_advance | Dereference of null pointer | 161 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 的赋值逻辑位于 `iter->select` 函数中，该函数未被包含在切片内，因此无法判断其返回值是否可能为 NULL。然而，告警规则为‘... |
| 2232 | git-2.44.0 | try_to_commit | Dereference of null pointer | 1499 | FP | FP | 告警点 `parents = copy_commit_list(current_head->parents);` 位于 `if (flags & AMEND_MSG)` 分支内，该分支仅在 `current_head` 非空时才会进入... |
| 2233 | git-2.44.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点是对函数`match_pathspec`的调用，其参数`ce`来自函数入参且被标记为`const`，调用前无任何解引用或可能导致其为空的检查。切片代码显示`ce`仅用于获取其成员（`ce->name`, `ce->ce_mode... |
| 2234 | git-2.44.0 | cmp_local_packs | Dereference of null pointer | 479 | FP | FP | 函数入口处 `pl` 被赋值为全局变量 `local_packs`，该变量在切片中初始化为 NULL，但函数 `cmp_local_packs` 被调用时，`local_packs` 很可能已被正确初始化（例如在其他函数中分配），否则... |
| 2235 | git-2.44.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 673 | FP | FP | 告警行 `struct tree_write_stack *n = tws->next;` 在解引用 `tws` 前已通过函数参数传入，调用方需保证 `tws` 非空。切片内函数逻辑在访问 `n` 前已检查 `if (n)`，且后续对... |
| 2236 | git-2.44.0 | unload_one_branch | Dereference of null pointer | 2052 | FP | FP | 在while循环条件`cur_active_branches && cur_active_branches >= max_active_branches`中，`cur_active_branches`为真值是进入循环体的前提，这保证了... |
| 2237 | git-2.44.0 | process_entries | Dereference of null pointer | 4329 | FP | FP | 告警点位于一个BUG断言宏内部，该宏仅在内部一致性检查失败时触发，用于打印调试信息并终止程序。代码逻辑表明，只有当`dir_metadata.offsets.nr != 1`或其首项`util`不为0时才会执行到该行，此时程序已确定进... |
| 2238 | git-2.44.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 169 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已在循环中被填充，且 `remotes->nr == 1` 的条件保证了列表至少有一个... |
| 2239 | git-2.44.0 | merge_ort_internal | Dereference of null pointer | 5056 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--` 之前，已经执行了 `opt->priv->call_depth++`，确保了指针 `opt->priv` 的有效性。该操作位于递归调用 `merge_ort_i... |
| 2240 | git-2.44.0 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警点位于 `for (curr = kwset->trie->next; curr; curr = curr->next)` 循环中，该循环仅在 `kwset->trie` 非空时才会进入。在前面的代码中，`curr = last ... |
| 2241 | git-2.44.0 | cmd_merge | Dereference of null pointer | 1509 | FP | FP | 告警点位于检查策略属性的条件判断语句中，`use_strategies[i]` 指针在循环前已通过 `use_strategies_nr` 控制访问范围，且切片中未见其有被赋值为 NULL 的可能。该指针解引用是安全的，属于静态分析工... |
| 2242 | git-2.44.0 | get_ref_map | Dereference of null pointer | 544 | FP | FP | 告警指向的代码行 `for (i = 0; i < fetch_refspec->nr; i++)` 中，`fetch_refspec` 已在前面通过条件判断被明确赋值（指向 `&refmap` 或 `&remote->fetch`）... |
| 2243 | git-2.44.0 | setup_scoreboard | Dereference of null pointer | 2839 | FP | FP | 告警点位于 while 循环条件 `c->parents` 的检查，但切片显示 `c` 由 `final_commit` 赋值，而 `final_commit` 仅在 `sb->reverse && sb->revs->first_p... |
| 2244 | git-2.44.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 代码逻辑确保了只有在 `sb->buf` 不为 `strbuf_slopbuf` 时才会进行解引用操作，此时 `sb->buf` 非空；而当 `sb->buf` 等于 `strbuf_slopbuf` 时，执行的是断言语句，不会解引用... |
| 2245 | git-2.44.0 | prepare_attr_stack | Dereference of null pointer | 1019 | FP | FP | 在循环条件 `while ((*stack)->origin)` 之前，代码已执行 `*stack = info->prev;`，其中 `info` 来自 `info = *stack;`，这表明 `*stack` 在进入循环前已被更... |
| 2246 | git-2.44.0 | assert_sane_strbuf | Dereference of null pointer | 34 | FP | FP | 告警点位于宏展开后的检查函数内部，其参数 `buf->buf` 已在上一行通过 `check(!!buf->buf)` 进行了非空断言。该检查确保了在调用 `check_char` 时 `buf->buf` 不为空，因此对 `buf-... |
| 2247 | git-2.44.0 | show_pack_info | Dereference of null pointer | 1720 | FP | FP | 代码逻辑保证了`chain_histogram`在循环访问前已被正确分配。`if (deepest_delta)`条件为真时，`CALLOC_ARRAY`会分配内存；若条件为假，则`deepest_delta`为0，循环`for (i... |
| 2248 | git-2.50.1 | image_remove_last_line | Dereference of null pointer | 363 | FP | FP | 切片代码显示，在访问 `img->line[img->line_nr - 1]` 之前，虽然没有显式的空指针检查，但函数 `image_remove_last_line` 被调用时，其参数 `img` 应处于有效状态，且 `img->... |
| 2249 | git-2.50.1 | add_parents_only | Dereference of null pointer | 1933 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且仅在非 NULL 时才执行后续解引用。因此，解引用空指针... |
| 2250 | git-2.50.1 | reftable_stack_reload_once | Dereference of null pointer | 380 | FP | FP | 告警点 `new_tables[new_tables_len] = table;` 中，`new_tables` 已在 `names_len` 非零时通过 `reftable_calloc` 分配，且 `new_tables_len`... |
| 2251 | git-2.50.1 | get_mode | Dereference of null pointer | 65 | FP | FP | 告警点位于 `*special = SPECIAL_STDIN;`，但切片代码显示，在解引用 `special` 指针之前，函数已通过 `if (special && ...)` 检查了该指针的有效性。在 `path == file_... |
| 2252 | git-2.50.1 | sync_submodule | Dereference of null pointer | 1288 | FP | FP | 告警点 `sub->name` 的指针 `sub` 由 `submodule_from_path` 函数返回，该函数在切片中定义，其返回值可能为 NULL，但调用点前有 `is_submodule_active` 检查，若检查失败函数... |
| 2254 | git-2.50.1 | crlf_to_git | Dereference of null pointer | 583 | FP | FP | 告警点位于循环内部，对指针 `src` 进行解引用。切片代码显示，在进入该循环前，函数已通过条件 `if (!buf && !src) return 1;` 对 `src` 为 NULL 的情况进行了处理并提前返回，因此当执行到解引用... |
| 2255 | git-2.50.1 | cwexec | Dereference of null pointer | 679 | FP | FP | 切片代码显示，在访问 `trie->accepting` 和 `trie->shift` 之前，`trie` 变量是通过 `next[c]` 赋值的，而 `next` 数组来自 `kwset->next`。虽然切片未显示 `kwset... |
| 2256 | git-2.50.1 | diffcore_merge_broken | Dereference of null pointer | 291 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环已确保 `pp = q->queue[j]` 被赋值，且外层循环已对 `q->queue[i]` 进行了空指针检查，代码逻辑保证了 `pp` 不为空。告警点位于 `if (pp... |
| 2257 | git-2.50.1 | parse_options_step | Dereference of null pointer | 958 | FP | FP | 告警点 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 在进入该分支前已被赋值为 `arg + 1`（第58行），且 `arg` 是 `ctx->argv[0]`，保证非空。... |
| 2258 | git-2.50.1 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | FP | 切片代码显示，在 for 循环条件 `p[i] == '/' ? i++ : *p++` 中，对指针 `p` 的递增操作 `*p++` 是合法的，它先解引用 `p`（该操作本身不会导致空指针解引用错误），然后对指针 `p` 进行后置递... |
| 2259 | git-2.50.1 | clar_summary_init | Dereference of null pointer | 76 | FP | FP | 在调用 `summary->filename = filename` 之前，`fopen` 失败会触发 `clar_abort` 函数，该函数调用 `exit(-1)` 终止程序，因此 `summary` 指针不可能为 NULL 时被... |
| 2260 | git-2.50.1 | parse_options | Dereference of null pointer | 1104 | FP | FP | 告警点 `*ctx.opt` 在 `parse_options_step` 函数中已被显式初始化为 `NULL`，并且在 `isascii(*ctx.opt)` 所在的 `case PARSE_OPT_UNKNOWN:` 分支中，`c... |
| 2261 | git-2.50.1 | allocate_snapshot_buffer | Dereference of null pointer | 533 | FP | FP | 告警点位于die_errno函数调用处，该函数用于错误处理并终止程序，不会对空指针进行解引用。切片代码中snapshot->buf由xmalloc分配，若分配失败会调用die终止程序，因此snapshot->buf在read_in_f... |
| 2263 | git-2.50.1 | verify_absent | Dereference of null pointer | 2537 | FP | FP | 告警行代码 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))` 中，`ce` 作为函数参数，其来源由调用方保证非空；且根据上下文，`ce` ... |
| 2264 | git-2.50.1 | show_pack_info | Dereference of null pointer | 1784 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，随后在循环中访问 `chain_histogram` 的代码被包裹在 `if (is_... |
| 2265 | git-2.50.1 | output | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `j < b->nr` 条件确保非空，且 `b_util->matching` 在 `while (j < b-... |
| 2267 | git-2.50.1 | limit_list | Dereference of null pointer | 1491 | FP | FP | 告警点位于检查 `obj->flags & UNINTERESTING` 的条件语句中，`obj` 由 `&commit->object` 赋值，`commit` 从 `pop_commit` 返回，该函数在输入非空时保证返回有效指针... |
| 2268 | git-2.50.1 | add_lines_to_move_detection | Dereference of null pointer | 1060 | FP | FP | 告警点 `entry_list[l->id].add` 访问前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量赋值，该变量在循环中递增，其值始终小于 `... |
| 2269 | git-2.50.1 | limit_list | Dereference of null pointer | 1487 | FP | FP | 切片代码显示，在访问 `commit->date` 之前，`commit` 变量由 `pop_commit(&original_list)` 返回，而 `pop_commit` 函数在输入列表非空时返回有效的 `item`，在列表为空... |
| 2270 | git-2.50.1 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | FP | 代码逻辑中，指针 `p` 在循环条件 `p[i]` 中用于索引访问，但 `p` 指向的字符串 `refname` 由 `xstrdup` 保证非空，且循环条件 `p[i]` 在 `p[i]` 为 '\0' 时终止，不会发生对空指针的解引用。 |
| 2271 | git-2.50.1 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当 `strmap_get_entry` 返回 NULL 时，函数直接返回 `map->default_value`，并未对空指针进行解引用。告警是对控制流逻辑的误判。 |
| 2272 | git-2.50.1 | coalesce_lines | Dereference of null pointer | 251 | FP | FP | 在告警行 `newend = newend->prev;` 之前，`newend` 仅在 `directions[i][j] == MATCH` 分支内被赋值，而该分支仅在 `i` 和 `j` 均不为零时进入。由于外层循环 `whil... |
| 2273 | git-2.50.1 | merge_ort_internal | Dereference of null pointer | 5277 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--` 之前，已经执行了 `opt->priv->call_depth++`，且该操作位于一个循环内，每次迭代都会成对地增加和减少。代码逻辑保证了 `call_dept... |
| 2274 | git-2.50.1 | assert_sane_strbuf | Dereference of null pointer | 35 | FP | FP | `cl_assert` 是一个单元测试断言宏，其目的是在测试失败时中止程序，而非在生产逻辑中执行。告警所指的指针 `buf` 在测试上下文（由函数名 `assert_sane_strbuf` 暗示）中应被视为有效，且该行代码的目的是验... |
| 2275 | git-2.50.1 | process_parents | Dereference of null pointer | 1174 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，因此对 `p->parents` 的访问是安全的，不会发生空指针解引用。 |
| 2276 | git-2.50.1 | run_prepare_commit_msg_hook | Dereference of null pointer | 1352 | FP | FP | 告警点 `msg->buf` 的指针 `msg` 由函数参数传入，切片中未显示其来源，但调用 `write_message` 前未对 `msg` 进行空指针检查。然而，该函数是 `run_prepare_commit_msg_hook... |
| 2277 | git-2.50.1 | gather_stats | Dereference of null pointer | 52 | FP | FP | 切片代码显示，函数参数 `buf` 在循环中被直接索引访问，但函数入口处没有对 `buf` 进行空指针检查。然而，该告警指向的是 `unsigned char c = buf[i];` 这一行，其前提是 `buf` 为空。在给定的循环... |
| 2278 | git-2.50.1 | clar_parse_args | Dereference of null pointer | 496 | FP | FP | 告警点位于 `explicit->suite_idx = j;`，该指针 `explicit` 由 `calloc` 分配，`calloc` 成功返回非空指针，失败则调用 `clar_abort` 退出程序，因此 `explicit`... |
| 2279 | git-2.50.1 | append_strategy | Dereference of null pointer | 233 | FP | FP | 切片代码显示，函数将指针 s 存入数组 use_strategies，并未对其进行解引用操作。告警消息描述的'解引用空指针'逻辑错误在此代码片段中并未发生，属于工具误报。 |
| 2280 | git-2.50.1 | merge_ref_iterator_advance | Dereference of null pointer | 214 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 已在 `if (!iter->current)` 分支中被检查为非空，且 `ITER_YIELD_CURRENT` 分支仅在 `selec... |
| 2281 | git-2.50.1 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码显示函数`strvec_push_nodup`直接对`array`指针进行解引用，但该函数是内部辅助函数，其调用方应确保传入的`array`指针非空。告警规则未考虑函数调用契约，属于典型的工具误报。 |
| 2282 | git-2.50.1 | add_lines_to_move_detection | Dereference of null pointer | 1063 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏根据 `id` 的值进行了动态扩容和初始化，确保了数组访问的有效性，不存在空指针解引用。 |
| 2283 | git-2.50.1 | image_remove_first_line | Dereference of null pointer | 355 | FP | FP | 告警点是对 `strbuf_remove` 函数的正常调用，该函数内部实现安全。切片代码中未显示 `img`、`img->buf` 或 `img->line[0]` 为空指针的任何证据或可能导致其为空的逻辑，因此该解引用是安全的。 |
| 2284 | git-2.50.1 | coalesce_lines | Dereference of null pointer | 259 | FP | FP | 告警点位于条件判断 `if (lline->prev)` 中，该判断旨在安全地访问指针成员。在切片代码的上下文中，`lline` 被赋值为 `newend`，而 `newend` 在循环中通过 `newend = newend->pr... |
| 2286 | git-2.50.1 | strvec_splice | Dereference of null pointer | 69 | FP | FP | 在调用ALLOC_GROW宏之前，代码已通过条件判断确保array->v不为NULL（若等于empty_strvec则显式设为NULL），且该宏内部会调用REALLOC_ARRAY进行内存分配，因此对array->v的索引访问是安全的... |
| 2288 | git-2.50.1 | prepare_attr_stack | Dereference of null pointer | 978 | FP | FP | 在调用 `bootstrap_attr_stack` 后，`*stack` 保证非空，且 `info = *stack` 赋值成功，因此 `info->prev` 的访问是安全的。告警点 `*stack = info->prev;` ... |
| 2289 | git-2.50.1 | split_graph_merge_strategy | Dereference of null pointer | 2284 | FP | FP | 告警点位于条件分支 `if (ctx->num_commit_graphs_after == 2)` 内部，而在此条件之前，`g` 变量已在 while 循环中被更新，且循环条件 `while (g && ...)` 确保了进入循环体... |
| 2290 | git-2.50.1 | get_nth_line | Dereference of null pointer | 879 | FP | FP | 函数逻辑清晰，当line为0时直接返回data，否则通过ends数组偏移计算地址。切片中未显示ends或data为空的证据，且函数体本身没有空指针解引用。告警可能是工具对指针运算的误判。 |
| 2291 | git-2.50.1 | <global> | Dereference of null pointer | 15 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对指针 `ref_iterator` 进行解引用操作，因此不存在空指针解引用问题。 |
| 2292 | git-2.50.1 | find_bisection | Dereference of null pointer | 440 | FP | FP | 告警点 `list->item = best->item;` 位于 `if (best)` 条件块内，`best` 是 `do_find_bisection` 的返回值，切片代码显示该函数在多种条件下（如 `approx_halfwa... |
| 2293 | git-2.50.1 | try_to_commit | Dereference of null pointer | 1570 | FP | FP | 告警点 `parents = copy_commit_list(current_head->parents);` 位于 `if (flags & AMEND_MSG)` 分支内，该分支仅在 `current_head` 非空时进入（因... |
| 2294 | git-2.50.1 | <global> | Dereference of null pointer | 1546 | FP | FP | 告警点位于条件判断 `if (use_strategies[i]->attr & NO_FAST_FORWARD)`，切片代码显示 `use_strategies` 数组在循环前已通过 `for (i = 0; i < use_str... |
| 2295 | git-2.50.1 | verify_absent_1 | Dereference of null pointer | 2496 | FP | FP | 告警行 `len = check_leading_path(ce->name, ce_namelen(ce), 0);` 中，`ce` 是函数参数，由调用方传入，在切片代码中未发现其被赋值为 NULL 的路径。函数入口处有 `if (... |
| 2296 | git-2.50.1 | try_to_commit | Dereference of null pointer | 1686 | FP | FP | 告警指向的 `commit_tree_extended` 函数调用行，其参数 `parents` 在切片代码的所有可达路径中均被正确初始化（可能为 NULL 或非空链表），且该函数内部已通过 `commit_list_count` 和... |
| 2298 | git-2.50.1 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点是对函数`match_pathspec`的调用，其参数`ce`来自函数入参，调用者应保证其非空。切片代码中未显示`ce`有显式的空值检查，但函数`ce_path_match`是静态内联的辅助函数，其调用上下文（未在切片中完全展示... |
| 2299 | git-2.50.1 | cmp_local_packs | Dereference of null pointer | 509 | FP | FP | 告警点检查 `pl->next` 前，`pl` 被赋值为 `local_packs`，而 `local_packs` 是一个静态变量，在文件作用域被初始化为 NULL。在 `cmp_local_packs` 被首次调用时，`pl` 为... |
| 2301 | git-2.50.1 | tree_write_stack_finish_subtree | Dereference of null pointer | 679 | FP | FP | 告警行 `struct tree_write_stack *n = tws->next;` 在后续的 `if (n)` 条件中被明确检查，只有在 `n` 非空时才会解引用。代码逻辑确保了不会对空指针进行解引用，因此是误报。 |
| 2302 | git-2.50.1 | unload_one_branch | Dereference of null pointer | 2066 | FP | FP | 切片代码显示，在解引用指针 `e` 之前，`e` 被明确赋值为 `active_branches`，而 `active_branches` 仅在 `cur_active_branches` 为真时才会进入循环，且 `e` 在循环中作为... |
| 2303 | git-2.50.1 | apply_one_fragment | Dereference of null pointer | 2991 | FP | FP | 告警指向的代码行 `postimage.line[postimage.line_nr - 1].len--;` 在切片中受到前置条件 `inaccurate_eof && old > oldlines && old[-1] == '\... |
| 2304 | git-2.50.1 | process_entries | Dereference of null pointer | 4486 | FP | FP | 告警点位于一个BUG断言宏内部，该宏仅在内部一致性检查失败时触发，用于打印调试信息并终止程序。这属于防御性编程的错误处理路径，而非正常的程序逻辑，因此不存在对空指针的实际解引用风险。 |
| 2305 | git-2.50.1 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已在循环中被填充，且 `remotes->nr == 1` 的条件保证了列表至少有一个... |
| 2306 | git-2.50.1 | clar_run_suite | Dereference of null pointer | 399 | FP | FP | 切片代码显示，在报告行`report->suite = _clar.active_suite;`之前，`report`指针已通过`calloc`分配并检查了是否为NULL，若分配失败程序会调用`clar_abort`退出，因此后续对`... |
| 2307 | git-2.50.1 | kwsprep | Dereference of null pointer | 507 | FP | FP | 告警点位于 `for (curr = kwset->trie->next; curr; curr = curr->next)` 循环中，该循环仅在 `kwset->trie` 非空时才会进入。根据切片代码，`kwset->trie` ... |
| 2309 | git-2.50.1 | get_ref_map | Dereference of null pointer | 544 | FP | FP | 切片代码显示，在警告行`for (i = 0; i < fetch_refspec->nr; i++)`之前，`fetch_refspec`指针已被明确赋值，要么指向`&refmap`（如果`refmap.nr`非零），要么指向`&r... |
| 2310 | git-2.50.1 | setup_scoreboard | Dereference of null pointer | 2842 | FP | FP | 告警指向的代码行 `while (c->parents &&` 位于条件 `if (sb->reverse && sb->revs->first_parent_only)` 内部，且 `c` 被赋值为 `final_commit`，而... |
| 2311 | git-2.50.1 | clear_snapshot_buffer | Dereference of null pointer | 185 | FP | FP | 告警点位于die_errno函数调用内部，该函数仅在munmap调用失败时才会被触发。在munmap失败的情况下，snapshot->buf指针本身是有效的（因为它是munmap的参数），不存在对空指针的解引用。该告警是工具的逻辑误判。 |
| 2312 | git-2.50.1 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 代码在访问 `sb->buf[len]` 前已通过 `if (sb->buf != strbuf_slopbuf)` 检查，确保 `sb->buf` 不为空指针或指向特殊缓冲区，因此不会发生空指针解引用。 |
| 2314 | git-2.50.1 | prepare_attr_stack | Dereference of null pointer | 986 | FP | FP | 在进入while循环前，代码执行了`*stack = info->prev;`，其中`info`来自`info = *stack;`，这表明`*stack`在循环前已被更新为其前驱节点。虽然切片未显示`info->prev`的赋值来源... |
| 2315 | git-2.50.1 | show_pack_info | Dereference of null pointer | 1806 | FP | FP | 代码逻辑保证了指针的有效性。`chain_histogram` 仅在 `deepest_delta` 为真时通过 `CALLOC_ARRAY` 分配内存，该宏会调用 `xcalloc` 确保返回有效指针或退出程序。后续循环访问 `ch... |
| 2316 | git-2.47.1 | image_remove_last_line | Dereference of null pointer | 362 | FP | FP | 代码在访问 `img->line[img->line_nr - 1]` 前，切片中未显示对 `img->line` 或 `img->line_nr` 的校验，但函数 `image_remove_last_line` 的语义和名称表明它... |
| 2317 | git-2.47.1 | add_parents_only | Dereference of null pointer | 1934 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且仅在 `it` 非 NULL 时才执行后续解引用。因此，... |
| 2318 | git-2.47.1 | get_mode | Dereference of null pointer | 63 | FP | FP | 告警点 `*special = SPECIAL_STDIN;` 位于 `if (path == file_from_standard_input)` 分支内，`special` 指针作为函数参数传入，在调用前已通过 `if (spec... |
| 2319 | git-2.47.1 | sync_submodule | Dereference of null pointer | 1283 | FP | FP | 告警点`sub->name`的指针`sub`由`submodule_from_path`函数返回，该函数在切片中定义，其返回值可能为NULL，但调用前已通过`is_submodule_active`检查，且`submodule_to_... |
| 2320 | git-2.47.1 | crlf_to_git | Dereference of null pointer | 582 | FP | FP | 告警指向的代码行 `unsigned char c = *src++;` 位于一个 `do...while` 循环内，该循环的条件是 `while (--len);`。在进入此循环前，函数开头有检查 `if (src && !len)... |
| 2321 | git-2.47.1 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码显示，在访问 `trie->shift` 和 `trie->accepting` 之前，`trie` 变量已通过 `trie = next[c]` 赋值，其中 `next` 是 `kwset->next` 的别名，且 `kws... |
| 2322 | git-2.47.1 | diffcore_merge_broken | Dereference of null pointer | 295 | FP | FP | 在访问 `pp->broken_pair` 之前，内层循环已确保 `pp = q->queue[j]` 赋值，且外层循环已处理 `q->queue[i]` 为 NULL 的情况并跳过。代码逻辑保证了 `pp` 指针非空，因此对 `pp... |
| 2323 | git-2.47.1 | parse_options_step | Dereference of null pointer | 906 | FP | FP | 告警点 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 在进入该分支前已通过 `ctx->opt = arg + 1;` 被赋值为非空指针，且后续有 `if (ctx->op... |
| 2324 | git-2.47.1 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | FP | 告警指向的代码行 `p[i] == '/' ? i++ : *p++` 是一个循环条件表达式，其目的是遍历字符串并计数。表达式 `*p++` 仅在 `p[i] != '/'` 时执行，用于递增指针 `p`，而 `p` 指向的是有效的字... |
| 2325 | git-2.47.1 | parse_options | Dereference of null pointer | 1052 | FP | FP | 在告警行 `isascii(*ctx.opt)` 之前，`ctx->opt` 已在 `parse_options_step` 函数中被显式重置为 `NULL`，并且当代码流程到达 `PARSE_OPT_UNKNOWN` 分支时，`ct... |
| 2326 | git-2.47.1 | process_entry | Dereference of null pointer | 3413 | FP | FP | 告警点位于 `RENAME_ONE_FILE_TO_TWO` 分支内，该分支仅在 `ci->ren2` 非空时执行。切片代码显示，在进入此分支前有 `if (ci->ren2)` 断言，确保了 `ci->ren2` 的有效性，因此 `... |
| 2327 | git-2.47.1 | verify_absent | Dereference of null pointer | 2534 | FP | FP | 告警行代码 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))` 中，`ce` 作为函数参数，其指针有效性由调用者保证，且切片内无任何证据表明... |
| 2328 | git-2.47.1 | show_pack_info | Dereference of null pointer | 1689 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，随后在循环中访问。访问发生在 `if (is_delta_type(obj->type... |
| 2329 | git-2.47.1 | output | Dereference of null pointer | 550 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `j < b->nr` 条件确保非空，且 `b_util->matching` 在 `while (j < b-... |
| 2330 | git-2.47.1 | limit_list | Dereference of null pointer | 1497 | FP | FP | 告警指向的代码行 `if (obj->flags & UNINTERESTING)` 中，`obj` 指针来自 `&commit->object`，而 `commit` 在循环中由 `pop_commit(&original_list... |
| 2331 | git-2.47.1 | add_lines_to_move_detection | Dereference of null pointer | 1059 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，确保了数组访... |
| 2332 | git-2.47.1 | limit_list | Dereference of null pointer | 1493 | FP | FP | 告警指向的代码行 `if (revs->max_age != -1 && (commit->date < revs->max_age))` 中，`commit` 变量来自 `pop_commit(&original_list)`，该函... |
| 2333 | git-2.47.1 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | FP | 代码逻辑中，`p` 指针初始化为 `refname` 且 `refname` 来自函数参数，不会为 NULL。循环条件 `p[i]` 在 `p` 非空字符串时安全，且 `xstrdup` 保证返回非空或终止程序，因此不存在空指针解引用。 |
| 2334 | git-2.47.1 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 告警逻辑错误。代码在检查指针`result`为空后，直接返回`map->default_value`，并未对空指针进行解引用操作，因此不存在空指针解引用问题。 |
| 2335 | git-2.47.1 | coalesce_lines | Dereference of null pointer | 264 | FP | FP | 告警点位于 `directions[i][j] == MATCH` 分支内，该分支仅在 `i != 0 ｜｜ j != 0` 时进入。循环初始化 `i` 和 `j` 为 `origbaselen` 和 `lennew`，且每次迭代递减... |
| 2336 | git-2.47.1 | merge_ort_internal | Dereference of null pointer | 5218 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--;` 之前，`opt->priv->call_depth` 已通过 `opt->priv->call_depth++;` 进行了递增，确保了指针 `opt->pri... |
| 2337 | git-2.47.1 | process_parents | Dereference of null pointer | 1180 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，因此对 `p->parents` 的解引用是安全的，不会导致空指针解引用。 |
| 2338 | git-2.47.1 | run_prepare_commit_msg_hook | Dereference of null pointer | 1365 | FP | FP | 告警点位于 `write_message(msg->buf, msg->len, name, 0)`，其中 `msg` 是函数参数 `struct strbuf *msg`，由调用者传入。切片代码中，在调用 `write_messag... |
| 2339 | git-2.47.1 | gather_stats | Dereference of null pointer | 51 | FP | FP | 代码逻辑中已通过循环条件 `i < size` 确保对 `buf[i]` 的访问在有效范围内，不存在对空指针的解引用。告警可能是工具对循环边界或指针状态的分析误判。 |
| 2340 | git-2.47.1 | append_strategy | Dereference of null pointer | 231 | FP | FP | 切片代码显示，函数将指针 s 存入数组，并未对其进行解引用操作。告警消息描述的'解引用空指针'逻辑错误在此代码片段中并未发生，属于工具误报。 |
| 2341 | git-2.47.1 | merge_ref_iterator_advance | Dereference of null pointer | 203 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 已在 `ITER_YIELD_CURRENT` 分支中被检查，该分支仅在 `selection & ITER_YIELD_CURRENT`... |
| 2342 | git-2.47.1 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码显示函数`strvec_push_nodup`直接对`array`指针进行解引用，但该函数是内部辅助函数，其调用方应确保传入的`array`指针非空。告警规则未考虑函数调用契约，直接报告空指针解引用属于典型的误报。 |
| 2343 | git-2.47.1 | add_lines_to_move_detection | Dereference of null pointer | 1062 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行分配和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，确保了索引在... |
| 2345 | git-2.47.1 | coalesce_lines | Dereference of null pointer | 272 | FP | FP | 告警指向的代码行 `if (lline->prev)` 位于 `if (directions[i][j] == NEW)` 分支内，该分支仅在 `directions[i][j]` 等于 `NEW` 时执行。根据切片中 `direct... |
| 2346 | git-2.47.1 | try_to_commit | Dereference of null pointer | 1699 | FP | FP | 告警指向的代码行 `commit_tree_extended(msg->buf, msg->len, &tree, parents, oid, author, committer, opts->gpg_sign, extra)` 中，... |
| 2347 | git-2.47.1 | prepare_attr_stack | Dereference of null pointer | 1013 | FP | FP | 告警行 `*stack = info->prev;` 前已通过 `bootstrap_attr_stack` 确保 `*stack` 非空，且 `info` 被赋值为 `*stack`，因此 `info` 非空，解引用 `info->... |
| 2348 | git-2.47.1 | split_graph_merge_strategy | Dereference of null pointer | 2269 | FP | FP | 告警行`get_commit_graph_filename(g->odb)`中，变量`g`在进入该代码块前已通过`while (g && ...)`循环和`if (ctx->num_commit_graphs_after == 2)`... |
| 2349 | git-2.47.1 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 函数逻辑清晰，当line为0时直接返回data，否则通过ends数组偏移计算地址。切片中未显示ends或data为空的证据，且函数为static，调用方应确保参数有效，因此告警为误报。 |
| 2350 | git-2.47.1 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对指针 `ref_iterator` 进行解引用操作，因此不存在空指针解引用问题。 |
| 2351 | git-2.47.1 | find_bisection | Dereference of null pointer | 439 | FP | FP | 告警点 `list->item = best->item;` 处，`list` 在函数开头已通过 `list = last;` 被明确赋值，且 `last` 在循环中被正确初始化，不可能为 NULL。因此，对 `list` 的访问是安... |
| 2352 | git-2.47.1 | <global> | Dereference of null pointer | 1537 | FP | FP | 告警点位于检查 `use_strategies[i]->attr & NO_FAST_FORWARD` 的条件判断中，切片代码显示 `use_strategies` 数组在循环前已通过 `add_strategies` 等函数正确初始... |
| 2353 | git-2.47.1 | verify_absent_1 | Dereference of null pointer | 2493 | FP | FP | 告警点 `ce->name` 的指针 `ce` 由函数参数传入，在切片代码中，`ce` 在调用 `ce_namelen` 和 `submodule_from_ce` 等函数时已被安全解引用，表明其不为空。工具可能未能正确推断函数调用上... |
| 2354 | git-2.47.1 | try_to_commit | Dereference of null pointer | 1583 | FP | FP | 告警点 `parents = copy_commit_list(current_head->parents);` 位于 `if (flags & AMEND_MSG)` 分支内，该分支仅在 `current_head` 非空时进入（因... |
| 2355 | git-2.47.1 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 告警点是对函数`ce_path_match`参数`ce`的成员访问，该参数由调用方传入且未被修改。切片代码显示`ce`作为函数参数，其有效性应由调用者保证，且函数内部无任何可能导致其为空的逻辑。因此，在函数内部`ce`不可能为NULL... |
| 2356 | git-2.47.1 | cmp_local_packs | Dereference of null pointer | 482 | FP | FP | 告警点检查 `pl->next` 前，`pl` 已从全局变量 `local_packs` 初始化，而 `local_packs` 在文件作用域被显式初始化为 NULL。因此，当 `local_packs` 为 NULL 时，`pl` ... |
| 2357 | git-2.47.1 | tree_write_stack_finish_subtree | Dereference of null pointer | 677 | FP | FP | 告警行 `struct tree_write_stack *n = tws->next;` 在后续的 `if (n)` 条件中已对指针 `n` 进行了空值检查，只有在非空时才会解引用，因此不存在对空指针的解引用逻辑错误。 |
| 2358 | git-2.47.1 | unload_one_branch | Dereference of null pointer | 2049 | FP | FP | 在进入while循环前，条件`cur_active_branches && cur_active_branches >= max_active_branches`确保了`cur_active_branches`大于0，这意味着`act... |
| 2359 | git-2.47.1 | apply_one_fragment | Dereference of null pointer | 2987 | FP | FP | 告警指向的代码行 `postimage.line[postimage.line_nr - 1].len--;` 在切片中受 `if (inaccurate_eof && old > oldlines && ...)` 条件保护，且 `... |
| 2360 | git-2.47.1 | process_entries | Dereference of null pointer | 4452 | FP | FP | 告警点位于一个BUG宏调用前的调试打印语句中，该条件分支仅在内部一致性检查失败时触发，用于报告错误并终止程序，不会导致正常的空指针解引用。切片代码显示对`dir_metadata.offsets.items[0].util`的访问发生... |
| 2361 | git-2.47.1 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 告警点访问 `friendly_ref_names.items[0].string` 前，切片代码显示 `friendly_ref_names` 列表已通过循环添加了元素，且 `remotes->nr == 1` 的条件保证了列表至少... |
| 2362 | git-2.47.1 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警点位于循环 `for (curr = kwset->trie->next; curr; curr = curr->next)`，该循环仅在 `kwset->trie` 非空时才会进入，且 `curr` 在循环中通过 `curr->... |
| 2363 | git-2.47.1 | get_ref_map | Dereference of null pointer | 546 | FP | FP | 告警指向的代码行 `for (i = 0; i < fetch_refspec->nr; i++)` 中，`fetch_refspec` 指针在切片代码中已被明确赋值：它要么指向 `&refmap`（当 `refmap.nr` 非零时... |
| 2364 | git-2.47.1 | setup_scoreboard | Dereference of null pointer | 2841 | FP | FP | 告警指向的 while 循环条件 `c->parents` 在循环前已通过 `if (sb->reverse && sb->revs->first_parent_only)` 和 `final_commit = find_single... |
| 2365 | git-2.47.1 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 代码在访问 `sb->buf[len]` 前已通过 `if (sb->buf != strbuf_slopbuf)` 检查，确保 `sb->buf` 不为空指针（`strbuf_slopbuf` 是一个静态缓冲区，非空），因此不会发生... |
| 2366 | git-2.47.1 | prepare_attr_stack | Dereference of null pointer | 1021 | FP | FP | 告警行 `while ((*stack)->origin)` 在循环前已执行 `*stack = info->prev;`，但切片中未显示 `info` 或 `*stack` 的初始赋值，无法确认 `info->prev` 或 `*s... |
| 2368 | git-2.47.1 | show_pack_info | Dereference of null pointer | 1711 | FP | FP | 切片代码显示，在访问 `chain_histogram[i]` 之前，已通过 `if (deepest_delta)` 条件判断，并调用了 `CALLOC_ARRAY(chain_histogram, deepest_delta)` ... |
| 2369 | musl-1.2.1 | iconv | Dereference of null pointer | 373 | FP | FP | 代码中 `scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。在 `ISO2022_JP` 的 `case 'J': scd->state=1;` 行，只有当 `scd` 非空时才会解... |
| 2370 | musl-1.2.1 | load_direct_deps | Dereference of null pointer | 1194 | FP | FP | 在 `p->deps` 为空的错误处理分支中，程序已通过 `error` 函数报告错误，并在 `runtime` 为真时通过 `longjmp` 跳转退出，因此后续对 `p->deps[cnt++]` 的访问在实际执行中不可达，属于误报。 |
| 2371 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警行 `so = pmatch[bt].rm_so;` 中，`pmatch` 指针在 `tnfa->num_submatches` 非零时已通过 `xmalloc` 分配，且 `bt` 是来自 `trans_i->u.backref... |
| 2372 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 告警点 `tags[*next_tags] = pos;` 中，`next_tags` 指针在循环条件 `*next_tags >= 0` 的保护下被解引用，该条件确保了指针非空且指向的值有效，因此不会发生空指针解引用。 |
| 2373 | musl-1.2.1 | do_relocs | Dereference of null pointer | 435 | FP | FP | 告警指向的 `memcpy` 调用位于 `case REL_COPY:` 分支，其源地址 `(void *)sym_val` 和目标地址 `reloc_addr` 均通过 `laddr` 函数计算得到，该函数确保返回非空指针。切片中未... |
| 2374 | musl-1.2.1 | iconv | Dereference of null pointer | 380 | FP | FP | 告警点位于 `switch (scd->state)` 语句，但切片代码显示 `scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。当 `scd` 为0时，解引用 `scd->stat... |
| 2375 | musl-1.2.1 | iconv | Dereference of null pointer | 372 | FP | FP | 代码中 `scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。在 `case ISO2022_JP:` 分支中，对 `scd->state` 的访问被包裹在 `if (c == '\0... |
| 2376 | musl-1.2.1 | load_direct_deps | Dereference of null pointer | 1206 | FP | FP | 切片代码显示，在访问 `p->deps[cnt]` 之前，已通过 `if (p->deps) return;` 进行了空指针检查，因此当程序执行到告警行时，`p->deps` 必然不为空，不会发生空指针解引用。 |
| 2377 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 告警点位于宏展开后的代码行，该行在`next_tags`非空时才会执行解引用。切片代码显示，`next_tags`仅在`state`非空且存在匹配的转换时被赋值，且其来源（如`trans_i->tags`）可能为空。然而，在解引用前存... |
| 2378 | musl-1.2.1 | iconv | Dereference of null pointer | 374 | FP | FP | 告警指向的代码行 `case 'I': scd->state=4; continue;` 是对 `scd->state` 的赋值，而 `scd` 指针在函数开头已通过条件 `if (!((size_t)cd & 1)) { scd =... |
| 2379 | musl-1.2.1 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `if (match_eo >= 0 && !(cflags & REG_NOSUB))` 条件确保 `match_eo` 非负，且 `tags` 数组的索引 `submatch_d... |
| 2380 | musl-1.2.1 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，变量 `max` 已在 `else if` 分支中被赋值为 `-1`，因此 `max` 的值是确定的，不会导致空指针解引用。告警是误报。 |
| 2381 | musl-1.2.1 | iconv | Dereference of null pointer | 375 | FP | FP | 告警点位于switch-case语句中，`scd->state`的赋值操作受控于前置条件`if (!scd->state)`，且`scd`指针在函数入口处已通过`if (!((size_t)cd & 1))`检查并赋值，不会为null... |
| 2382 | musl-1.2.1 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点 `if (!scd->state)` 位于 `scd` 指针被显式初始化为 `0` 之后，且仅在 `!((size_t)cd & 1)` 为真时才会被赋值为非空指针。当 `scd` 为 `0` 时，代码不会进入该分支，因此不会... |
| 2383 | musl-1.2.1 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，存在对 `submatch_data` 指针的赋值 `submatch_data = tnfa->submatch_data;`，且该指针在循... |
| 2384 | musl-1.2.1 | queue_ctors | Dereference of null pointer | 1452 | FP | FP | 告警行 `p->deps[p->next_dep]->mark` 中，`p->deps` 的访问受 `p->next_dep < p->ndeps_direct` 条件保护，确保了索引在有效范围内；且切片中未发现 `p->deps` ... |
| 2385 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 在调用 `states_seen[stack->item.state_id] = 0;` 之前，代码已通过 `if (stack->prev)` 检查确保 `stack` 不为空，且 `stack->prev` 的存在意味着 `sta... |
| 2386 | musl-1.2.1 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于switch-case语句的一个分支标签处（case 128+'B':），该行本身不包含任何指针解引用操作。指针解引用发生在其他逻辑分支中，且切片代码显示对scd指针的访问（如scd->state）均有条件保护（s... |
| 2387 | musl-1.2.1 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警行代码 `regset = xmalloc(sizeof(*regset) * ((tnfa->num_submatches + 1) * 2));` 中，`tnfa` 指针在函数入口处通过 `first_pass = (mem ... |
| 2388 | musl-1.2.4 | iconv | Dereference of null pointer | 373 | FP | FP | 告警指向的代码行 `case 'J': scd->state=1; continue;` 是对状态变量 `scd->state` 的赋值，`scd` 指针在函数入口处已通过条件 `if (!((size_t)cd & 1)) { sc... |
| 2390 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警点 `so = pmatch[bt].rm_so;` 访问的 `pmatch` 数组指针在函数前部已通过条件 `if (tnfa->num_submatches)` 检查并分配内存，且 `bt` 是来自 `trans_i->u.b... |
| 2391 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 告警点位于条件判断 `if (next_tags)` 之后，该条件已确保 `next_tags` 不为空。在循环 `for (; *next_tags >= 0; next_tags++)` 中，对 `next_tags` 的递增操作... |
| 2392 | musl-1.2.4 | do_relocs | Dereference of null pointer | 484 | FP | FP | 告警位于 `case REL_COPY:` 分支的 `memcpy` 调用处，但切片代码显示，在该分支执行前，`sym_val` 和 `sym->st_size` 已通过 `def.sym` 和 `sym` 的有效性检查。`def.s... |
| 2393 | musl-1.2.4 | iconv | Dereference of null pointer | 380 | FP | FP | 告警指向的代码行位于 `switch (scd->state)` 语句，但切片代码显示，在进入该switch语句前，`scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。然而，在 `s... |
| 2394 | musl-1.2.4 | iconv | Dereference of null pointer | 372 | FP | FP | 告警点位于switch-case语句的标签行，该行是控制流跳转目标，不会对空指针进行解引用。代码逻辑表明，只有当`scd`指针非空时才会进入相关分支，且切片中未发现对空指针`scd`的直接解引用操作。 |
| 2395 | musl-1.2.4 | do_relocs | Dereference of null pointer | 519 | FP | FP | 告警点位于条件判断 `if (def.dso->tls_id > static_tls_cnt)` 中，是对指针 `def.dso` 的成员访问。根据切片代码，`def` 结构体在 `sym_index` 非零和为零的两种情况下都被明... |
| 2396 | musl-1.2.4 | do_relocs | Dereference of null pointer | 458 | FP | FP | 告警指向的代码行位于一个条件判断块内，该条件为 `(type == REL_TPOFF ｜｜ type == REL_TPOFF_NEG) && def.dso->tls_id > static_tls_cnt`。当此条件为真时，代码... |
| 2397 | musl-1.2.4 | load_direct_deps | Dereference of null pointer | 1292 | FP | FP | 切片代码显示，在访问 `p->deps[cnt]` 之前，已通过 `if (p->deps) return;` 检查了 `p->deps` 指针，若其为空则直接返回，因此不会发生空指针解引用。 |
| 2398 | musl-1.2.4 | do_relocs | Dereference of null pointer | 500 | FP | FP | 在 `case REL_DTPMOD:` 分支中，`def.dso` 被赋值为 `dso`（见第38行 `def.dso = dso;`），因此 `def.dso` 不可能为空。对 `def.dso->tls_id` 的访问是安全的，... |
| 2399 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `tags[*next_tags++] = pos;` 中，`next_tags` 指针在循环前已通过 `if (next_tags)` 检查非空，且循环条件 `*next_tags >= 0` 确保解引用前指针指向... |
| 2400 | musl-1.2.4 | iconv | Dereference of null pointer | 374 | FP | FP | 代码中 `scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。在 `case ISO2022_JP:` 分支中，对 `scd->state` 的访问（第374行）受控于 `if (c ... |
| 2401 | musl-1.2.4 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 代码在访问 `tags` 数组前，已通过 `if (match_eo >= 0 && !(cflags & REG_NOSUB))` 条件确保 `match_eo` 非负，且 `tags` 数组索引 `submatch_data[i]... |
| 2402 | musl-1.2.4 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 告警行 `tag_directions[max] = TRE_TAG_MAXIMIZE;` 中，变量 `max` 在切片中已明确赋值为 `-1`（见 `max = pos = -1;`），因此 `tag_directions[-1]`... |
| 2403 | musl-1.2.4 | iconv | Dereference of null pointer | 375 | FP | FP | 告警点位于switch-case语句的case标签行，该行本身不包含任何指针解引用操作。代码逻辑表明，只有当`scd`指针非空且其`state`字段为0时，才会在后续代码中访问`scd->state`，而在此之前`scd`已被有条件地... |
| 2404 | musl-1.2.4 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点 `if (!scd->state)` 位于 `scd` 指针被初始化为 `0` 之后，但在执行到该行之前，代码逻辑（`if (!((size_t)cd & 1))`）确保了当 `cd` 为偶数时 `scd` 会被赋值为非空指针... |
| 2405 | musl-1.2.4 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 在访问 `tags[submatch_data[i].eo_tag]` 前，代码已通过 `while (i < tnfa->num_submatches && i < nmatch)` 循环条件确保 `i` 在有效范围内，且 `sub... |
| 2406 | musl-1.2.4 | queue_ctors | Dereference of null pointer | 1553 | FP | FP | 在告警行 `p->deps[p->next_dep]->mark` 处，`p->deps` 数组的访问受 `p->next_dep < p->ndeps_direct` 循环条件保护，确保了索引在有效范围内；同时，`p->deps[p... |
| 2407 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 在 `backtrack` 标签处，对 `stack->prev` 的检查确保了 `stack` 不为空，因此 `stack->item.state` 和 `stack->item.state_id` 的访问是安全的。切片代码中未发现... |
| 2408 | musl-1.2.4 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于switch-case语句的标签处（case 128+'B':），该行是控制流跳转目标，不涉及指针解引用操作。静态分析工具可能误将标签识别为可执行代码。 |
| 2409 | musl-1.2.4 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警行代码 `regset = xmalloc(sizeof(*regset) * ((tnfa->num_submatches + 1) * 2));` 中，`tnfa` 指针在函数开头通过 `first_pass = (mem =... |
| 2410 | musl-1.1.24 | iconv | Dereference of null pointer | 373 | FP | FP | 告警指向的代码行 `case 'J': scd->state=1; continue;` 是对 `scd->state` 的赋值操作，并非解引用。`scd` 指针在函数入口处已通过条件 `if (!((size_t)cd & 1)) ... |
| 2411 | musl-1.1.24 | load_direct_deps | Dereference of null pointer | 1189 | FP | FP | 切片代码显示，在警告行 `p->deps[cnt++] = q;` 之前，`p->deps` 已被明确赋值（例如 `p->deps = (p==head && cnt<2) ? builtin_deps : ...`），并且紧接着有 ... |
| 2412 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警行 `so = pmatch[bt].rm_so;` 中，`pmatch` 指针在 `tnfa->num_submatches` 非零时已通过 `xmalloc` 分配，且 `bt` 是 `trans_i->u.backref`，... |
| 2413 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 告警指向的代码行 `tags[*next_tags] = pos;` 位于 `if (next_tags)` 条件保护之后，且 `next_tags` 在循环条件 `*next_tags >= 0` 中已确保其指向的整数值非负，同时 ... |
| 2414 | musl-1.1.24 | do_relocs | Dereference of null pointer | 430 | FP | FP | 告警指向的代码行位于 `case REL_COPY:` 分支，该分支仅在 `sym` 和 `sym_val` 有效时执行。根据切片代码，`sym_val` 由 `def.sym ? (size_t)laddr(def.dso, def... |
| 2415 | musl-1.1.24 | iconv | Dereference of null pointer | 380 | FP | FP | 告警位于switch语句中对`scd->state`的访问，但切片代码显示，在进入该switch前，`scd`仅在`cd`为偶数时被赋值，且`ISO2022_JP`编码处理分支仅在`scd->state`被显式赋值（如`scd->st... |
| 2416 | musl-1.1.24 | iconv | Dereference of null pointer | 372 | FP | FP | 告警指向的代码行 `case 'B': scd->state=0; continue;` 位于 ISO2022_JP 编码处理分支中，该分支仅在 `scd` 指针非空时才会进入。函数开头已通过 `if (!((size_t)cd & ... |
| 2417 | musl-1.1.24 | load_direct_deps | Dereference of null pointer | 1201 | FP | FP | 切片代码显示，在访问 `p->deps[cnt]` 之前，已通过 `if (p->deps) return;` 检查了 `p->deps` 指针的有效性，若为空则直接返回，因此不会发生空指针解引用。 |
| 2418 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 告警点位于宏展开后的代码行，该行在`next_tags`非空时才会执行解引用。切片代码显示，`next_tags`仅在`trans_i->tags`非空时被赋值，且`trans_i`来自`state`的遍历，`state`在进入循环前... |
| 2419 | musl-1.1.24 | iconv | Dereference of null pointer | 374 | FP | FP | 告警指向的代码行 `case 'I': scd->state=4; continue;` 是对 `scd->state` 的赋值，而 `scd` 在函数开头已通过条件 `if (!((size_t)cd & 1)) { scd = (... |
| 2420 | musl-1.1.24 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].so_tag]` 之前，`tags` 指针已在函数参数中传入，且其有效性由调用者保证。告警行位于一个受 `if (match_eo >= 0 && !(cflags ... |
| 2421 | musl-1.1.24 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 告警行 `tag_directions[max] = TRE_TAG_MAXIMIZE;` 中，变量 `max` 在切片中已明确赋值为 `-1`（见 `max = pos = -1;`），因此 `tag_directions[-1]`... |
| 2422 | musl-1.1.24 | iconv | Dereference of null pointer | 375 | FP | FP | 告警指向的代码行 `case 128+'@': scd->state=2; continue;` 位于一个switch语句的分支中，该分支仅在变量 `scd` 非空时才会执行。函数开头已通过条件 `if (!((size_t)cd &... |
| 2423 | musl-1.1.24 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点 `if (!scd->state)` 位于 `scd` 指针被显式初始化为 `0` 的代码块之后，且该指针仅在 `if (!((size_t)cd & 1))` 条件为真时才被重新赋值。当条件为假时，`scd` 保持为 `0`... |
| 2424 | musl-1.1.24 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 告警行代码 `pmatch[i].rm_eo = tags[submatch_data[i].eo_tag];` 中，对 `tags` 数组的索引 `submatch_data[i].eo_tag` 的值已通过 `if (submat... |
| 2425 | musl-1.1.24 | queue_ctors | Dereference of null pointer | 1447 | FP | FP | 在告警行访问 `p->deps[p->next_dep]` 前，循环条件 `while (p->next_dep < p->ndeps_direct)` 已确保 `p->next_dep` 是有效索引，且 `p->deps` 数组在切... |
| 2426 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 在 `states_seen[stack->item.state_id] = 0;` 这行代码之前，存在 `if (stack->prev)` 的条件检查，确保了 `stack` 不为空。同时，`states_seen` 数组在函数开... |
| 2427 | musl-1.1.24 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于一个switch-case语句的分支标签处（case 128+'B':），该行本身不包含任何指针解引用操作。切片代码显示，变量`scd`在函数入口处被有条件地赋值，但在该case分支被使用前，其值已通过`scd->... |
| 2428 | musl-1.1.24 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警行代码 `regset = xmalloc(sizeof(*regset) * ((tnfa->num_submatches + 1) * 2));` 中，`tnfa` 指针在函数入口处通过 `first_pass = (mem ... |
| 2429 | musl-1.2.3 | iconv | Dereference of null pointer | 373 | FP | FP | 告警指向的代码行 `case 'J': scd->state=1; continue;` 是对 `scd->state` 的赋值操作，并非解引用。`scd` 指针在函数入口处已通过条件 `if (!((size_t)cd & 1)) ... |
| 2430 | musl-1.2.3 | load_direct_deps | Dereference of null pointer | 1218 | FP | FP | 在警告行之前，代码通过条件赋值 `p->deps = (p==head && cnt<2) ? builtin_deps :` 为 `p->deps` 赋值，并且紧接着有 `if (!p->deps)` 的检查，如果为空则会调用 `e... |
| 2431 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警点 `so = pmatch[bt].rm_so;` 中，`pmatch` 指针在 `tnfa->num_submatches` 非零时已通过 `xmalloc` 分配，且 `bt` 是 `trans_i->u.backref`，... |
| 2432 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 告警点 `tags[*next_tags] = pos;` 中，`next_tags` 指针在循环条件 `*next_tags >= 0` 的保护下被解引用，切片代码显示 `next_tags` 来源于 `trans_i->tags`... |
| 2433 | musl-1.2.3 | do_relocs | Dereference of null pointer | 440 | FP | FP | 告警行位于switch-case的REL_COPY分支内，该分支仅在`sym`和`sym_val`有效时执行`memcpy`。切片代码显示，进入此分支前`sym_val`的计算为`def.sym ? (size_t)laddr(def... |
| 2434 | musl-1.2.3 | iconv | Dereference of null pointer | 380 | FP | FP | 告警点位于switch语句中对scd->state的访问，但切片代码显示，在进入该switch前，scd仅在特定条件（(size_t)cd & 1为假）下被赋值为非空指针。对于ISO2022_JP等需要状态的处理，代码逻辑确保了在访问... |
| 2435 | musl-1.2.3 | iconv | Dereference of null pointer | 372 | FP | FP | 告警指向的代码行 `case 'B': scd->state=0; continue;` 是对 `scd->state` 的赋值，而非解引用。`scd` 指针在函数入口处已通过条件 `if (!((size_t)cd & 1)) { ... |
| 2436 | musl-1.2.3 | load_direct_deps | Dereference of null pointer | 1230 | FP | FP | 切片代码显示，在访问 `p->deps[cnt]` 之前，已通过 `if (p->deps) return;` 检查了指针 `p->deps` 是否为空，若为空则函数直接返回，因此后续的指针解引用是安全的。 |
| 2437 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `tags[*next_tags++] = pos;` 在切片中受到 `while (*next_tags >= 0)` 的保护，确保了 `next_tags` 指针非空且指向有效索引。切片内未发现会导致 `next... |
| 2438 | musl-1.2.3 | iconv | Dereference of null pointer | 374 | FP | FP | 告警点位于switch语句的case标签行，该行仅用于设置状态变量，不涉及任何指针解引用操作。代码逻辑清晰，不存在空指针解引用。 |
| 2439 | musl-1.2.3 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 告警行访问的 `tags` 数组指针由函数参数传入，切片中未见其可能为空的证据。代码逻辑在访问前已通过 `match_eo >= 0 && !(cflags & REG_NOSUB)` 条件保护，且后续对 `tags` 的索引 `su... |
| 2440 | musl-1.2.3 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，对数组 `tag_directions` 的索引 `max` 在访问前已被赋值为 -1（`max = pos = -1;`），这发生在 `(flags & COPY_REMOVE_TAGS)` 为真的分支中。虽然存在另一... |
| 2441 | musl-1.2.3 | iconv | Dereference of null pointer | 375 | FP | FP | 告警点位于switch-case语句的case标签行，该行仅用于设置状态变量，不涉及任何指针解引用操作。工具可能误将标签行识别为可执行代码。 |
| 2442 | musl-1.2.3 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点 `if (!scd->state)` 位于 `scd` 指针被显式初始化为 `0` 之后，且仅在 `if (!((size_t)cd & 1))` 条件为真时才会被赋值为非空指针。当 `scd` 为 `0` 时，代码不会进入 ... |
| 2443 | musl-1.2.3 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，`submatch_data` 已从 `tnfa->submatch_data` 获取，且循环条件 `i < tnfa->num_submat... |
| 2444 | musl-1.2.3 | queue_ctors | Dereference of null pointer | 1487 | FP | FP | 在访问 `p->deps[p->next_dep]` 之前，循环条件 `while (p->next_dep < p->ndeps_direct)` 确保了 `p->next_dep` 是 `p->deps` 数组的有效索引，因此不会... |
| 2445 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 在访问 `states_seen[stack->item.state_id]` 之前，代码已通过 `if (stack->prev)` 检查确保 `stack` 不为空，且 `states_seen` 数组在 `tnfa->num_s... |
| 2446 | musl-1.2.3 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于一个switch-case语句的case标签处（case 128+'B':），该行本身不包含任何指针解引用操作。切片代码显示，变量`scd`在函数入口处被有条件地赋值，但在该case分支中仅用于赋值`scd->st... |
| 2447 | musl-1.2.3 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警行代码 `regset = xmalloc(...)` 在调用前已通过 `if (regset == NULL)` 检查了返回值，后续所有对 `regset` 的访问（如 `regset[0] = -1`）都发生在该空指针检查之后... |
| 2448 | musl-1.2.2 | iconv | Dereference of null pointer | 373 | FP | FP | 告警指向的代码行 `case 'J': scd->state=1; continue;` 是对 `scd->state` 的赋值，而非解引用。`scd` 指针在函数开头已通过条件 `if (!((size_t)cd & 1)) { s... |
| 2449 | musl-1.2.2 | load_direct_deps | Dereference of null pointer | 1217 | FP | FP | 在 `p->deps` 被解引用前，代码已通过条件 `if (!p->deps)` 进行检查，若为空则会调用 `error` 并 `longjmp` 跳出函数，因此后续的 `p->deps[cnt++] = q` 解引用不会在 `p-... |
| 2450 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警行 `so = pmatch[bt].rm_so;` 中，`pmatch` 指针在 `tnfa->num_submatches` 非零时已通过 `xmalloc` 分配，且 `bt` 是来自 `trans_i->u.backref... |
| 2451 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 告警点位于条件判断 `if (next_tags)` 之后，该条件确保了 `next_tags` 非空才进入循环。在循环内部，`*next_tags >= 0` 是循环条件，`next_tags` 指针在循环体内递增。切片代码显示 `... |
| 2452 | musl-1.2.2 | do_relocs | Dereference of null pointer | 440 | FP | FP | 告警指向的代码行位于switch-case的REL_COPY分支，该分支仅在sym_val和sym指针有效时执行memcpy。切片代码显示，sym_val由def.sym决定，而def.sym在sym_index为0时被显式设为0，在... |
| 2453 | musl-1.2.2 | iconv | Dereference of null pointer | 380 | FP | FP | 告警指向的代码行 `switch (scd->state)` 位于 `if (!scd->state) { ... }` 条件块之后，该条件块已确保当执行到该行时 `scd->state` 已被赋值（非零），因此不会发生空指针解引用。 |
| 2454 | musl-1.2.2 | iconv | Dereference of null pointer | 372 | FP | FP | 代码中 `scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。在 `case ISO2022_JP` 分支中，对 `scd->state` 的访问发生在 `if (c == '\033... |
| 2455 | musl-1.2.2 | load_direct_deps | Dereference of null pointer | 1229 | FP | FP | 切片代码显示，在访问 `p->deps[cnt]` 之前，已通过 `if (p->deps) return;` 检查了 `p->deps` 指针，确保其非空后才进行解引用，因此不存在空指针解引用风险。 |
| 2456 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `tags[*next_tags++] = pos;` 在 `next_tags` 不为 NULL 且 `*next_tags >= 0` 的循环条件下执行。切片代码显示 `next_tags` 来源于 `trans... |
| 2457 | musl-1.2.2 | iconv | Dereference of null pointer | 374 | FP | FP | 告警指向的代码行 `case 'I': scd->state=4; continue;` 是对 `scd->state` 的赋值，而 `scd` 在函数开头已通过条件 `if (!((size_t)cd & 1)) { scd = (... |
| 2458 | musl-1.2.2 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，对 `tags` 数组的访问索引 `submatch_data[i].so_tag` 和 `submatch_data[i].eo_tag` 由库内部数据结构 `tnfa` 控制，并非外部输入，且循环条件 `i < tn... |
| 2459 | musl-1.2.2 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，`max` 变量已在 `else if (IS_TAG(lit) && (flags & COPY_REMOVE_TAGS))` 分支中被赋值为 `-1`，这确保... |
| 2460 | musl-1.2.2 | iconv | Dereference of null pointer | 375 | FP | FP | 告警指向的代码行 `case 128+'@': scd->state=2; continue;` 是switch语句中的一个分支，`scd`指针在函数入口处已通过条件 `if (!((size_t)cd & 1)) { scd = (... |
| 2461 | musl-1.2.2 | iconv | Dereference of null pointer | 300 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查，确保 `scd` 非空时才进行解引用。在 `case UCS2:` 和 `case UTF_16:` 分支中，`scd` 仅在... |
| 2462 | musl-1.2.2 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags[submatch_data[i].eo_tag]` 之前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 进行了条件判断，仅在 `eo_tag`... |
| 2463 | musl-1.2.2 | queue_ctors | Dereference of null pointer | 1486 | FP | FP | 在警告行 `p->deps[p->next_dep]` 访问前，代码逻辑 `while (p->next_dep < p->ndeps_direct)` 确保了 `p->next_dep` 索引在 `p->deps` 数组的有效范围内... |
| 2464 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 在`backtrack`标签处，对`stack->prev`的检查确保了`stack`不为空，因此`stack->item.state_id`是有效的索引。`states_seen`数组在函数开头已根据`tnfa->num_state... |
| 2465 | musl-1.2.2 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行 `case 128+'B': scd->state=3; continue;` 是对 `scd->state` 的赋值，而非解引用。`scd` 指针在函数入口处已通过 `if (!((size_t)cd & 1)) ... |
| 2466 | musl-1.2.2 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警行代码 `regset = xmalloc(sizeof(*regset) * ((tnfa->num_submatches + 1) * 2));` 中，`tnfa` 指针在函数开头已通过 `first_pass = (mem ... |
| 2467 | tmux-3.3 | recalculate_sizes_now | Dereference of null pointer | 458 | FP | FP | 在访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已检查 `c->session` 是否为空，若为空则提前返回，确保了后续 `s`（即 `c->session`）不为空。切片代码中的逻... |
| 2468 | tmux-3.3 | mode_tree_draw | Dereference of null pointer | 750 | FP | FP | 告警指向的 `xasprintf` 调用中，`mti->name` 和 `mtd->sort_list[mtd->sort_crit.field]` 均来自结构体成员，切片内未发现它们可能为 NULL 的证据。`mti` 在循环中通过... |
| 2469 | tmux-3.3 | window_copy_search | Dereference of null pointer | 3674 | FP | FP | 在访问 `data->searchmark[at]` 之前，代码已通过 `window_copy_search_mark_at(data, fx, fy, &at) == 0` 检查了 `at` 的有效性，并且 `data->sear... |
| 2470 | tmux-3.3 | grid_string_cells | Dereference of null pointer | 1013 | FP | FP | 告警点位于 `grid_string_cells_code(*lastgc, &gc, code, sizeof code, escape_c0);` 调用处，工具认为 `*lastgc` 可能为空指针。但在函数开头，当 `lastg... |
| 2471 | tmux-3.3 | mode_tree_draw | Dereference of null pointer | 754 | FP | FP | 告警点位于 `xasprintf(&text, " %s", mti->name);`，其中 `mti` 指针在切片代码中已通过 `mti = line->item;` 和 `if (mti->draw_as_parent) mti ... |
| 2472 | tmux-3.3 | grid_reflow_join | Dereference of null pointer | 1212 | FP | FP | 切片代码显示，在访问 `from` 指针前，`from = &gd->linedata[line];` 已对其进行了明确的非空赋值，该赋值发生在循环内部且条件可达，因此不会发生空指针解引用。 |
| 2473 | tmux-3.3 | spawn_window | Dereference of null pointer | 180 | FP | FP | 告警点 `free(w->name);` 位于 `if (~sc->flags & SPAWN_RESPAWN)` 条件块内，而在此条件块之前，存在 `if (~sc->flags & SPAWN_RESPAWN) { ... } e... |
| 2474 | tmux-3.3 | server_client_reset_state | Dereference of null pointer | 2340 | FP | FP | 告警行访问的指针 s 在切片代码中已被明确赋值，要么来自 c->overlay_mode 的调用结果（若不为NULL），要么直接赋值为 wp->screen（wp 来自 server_client_get_pane，可能返回NULL，... |
| 2475 | tmux-3.3 | input_parse | Dereference of null pointer | 907 | FP | FP | 在切片代码中，`ictx->state` 在告警行 `itr = ictx->state->transitions;` 之前已被使用（例如在条件 `ictx->state != state` 中），这表明 `ictx->state` ... |
| 2476 | tmux-3.2 | recalculate_sizes_now | Dereference of null pointer | 367 | FP | FP | 在访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已检查 `c->session` 是否为 NULL，若为 NULL 则函数返回 1，循环会跳过当前迭代，因此 `s` 指针在解引用时不... |
| 2477 | tmux-3.2 | mode_tree_draw | Dereference of null pointer | 753 | FP | FP | 告警点位于xasprintf调用，其参数mti->name和mtd->sort_list[mtd->sort_crit.field]在切片中均有明确的非空来源和赋值路径，且存在前置条件检查mtd->sort_list != NULL，... |
| 2478 | tmux-3.2 | window_copy_search | Dereference of null pointer | 3183 | FP | FP | 在访问 `data->searchmark[at]` 之前，代码已通过 `window_copy_search_mark_at(data, fx, fy, &at) == 0` 检查了索引 `at` 的有效性，并且 `searchma... |
| 2479 | tmux-3.2 | spawn_window | Dereference of null pointer | 181 | FP | FP | 告警指向的代码行 `w->name = format_single(...)` 中，变量 `w` 在切片中已被多处使用（如 `w->panes`、`w->sx`），表明其已在前文被正确初始化或赋值，并非空指针。切片内未发现将 `w` ... |
| 2480 | tmux-3.2 | grid_string_cells | Dereference of null pointer | 983 | FP | FP | 告警点位于函数调用 `grid_string_cells_code(*lastgc, ...)`，但切片代码显示，在调用前已通过条件 `if (lastgc != NULL && *lastgc == NULL)` 将 `*lastg... |
| 2481 | tmux-3.2 | mode_tree_draw | Dereference of null pointer | 757 | FP | FP | 告警点位于 `xasprintf(&text, " %s", mti->name);`，其中 `mti` 指针在切片代码中已通过 `mti = line->item;` 和 `if (mti->draw_as_parent) mti ... |
| 2482 | tmux-3.2 | spawn_window | Dereference of null pointer | 185 | FP | FP | 告警指向 `w->name = default_window_name(w);` 行，认为可能对空指针 `w` 解引用。但切片代码显示，在该行执行前，`w` 已在 `if (~sc->flags & SPAWN_RESPAWN)` 分... |
| 2483 | tmux-3.2 | grid_reflow_join | Dereference of null pointer | 1182 | FP | FP | 告警行 `left = from->cellused - want;` 中，变量 `from` 已在循环 `for (want = 1; want < from->cellused; want++)` 中被明确赋值（`from = &... |
| 2484 | tmux-3.2 | server_client_reset_state | Dereference of null pointer | 1672 | FP | FP | 告警行代码 `wp->xoff + s->cx >= ox` 中，变量 `s` 在告警前已通过条件分支被明确赋值（`s = wp->screen` 或 `s = c->overlay_mode(...)`），不会为 NULL。切片代码... |
| 2485 | tmux-3.2 | input_parse | Dereference of null pointer | 902 | FP | FP | 在访问 `ictx->state->transitions` 之前，代码逻辑已通过 `if` 条件确保 `ictx->state` 不为 NULL，且 `state` 变量被初始化为 NULL 并与 `ictx->state` 进行比... |
| 2486 | tmux-3.1 | spawn_window | Dereference of null pointer | 185 | FP | FP | 告警指向的代码行 `w->name = format_single(...)` 中，变量 `w` 在切片代码中未显示其初始化或赋值来源，无法判断其是否为 NULL。但结合上下文逻辑（如 `w->latest = sc->c;` 等对 ... |
| 2487 | tmux-3.1 | grid_string_cells | Dereference of null pointer | 927 | FP | FP | 告警点位于函数调用 `grid_string_cells_code(*lastgc, ...)`，其中 `*lastgc` 被解引用。切片代码显示，在函数入口处有明确的检查 `if (lastgc != NULL && *lastgc... |
| 2489 | tmux-3.1 | grid_reflow_join | Dereference of null pointer | 1126 | FP | FP | 切片代码显示，在访问 `from` 指针前，`from` 已在循环中被赋值为 `&gd->linedata[line]`，且该循环在 `lines == 0` 时提前返回，因此 `from` 在 `left = from->cellu... |
| 2490 | tmux-3.1 | mode_tree_build | Dereference of null pointer | 407 | FP | FP | 在告警行之前，代码已通过条件 `if (mtd->line_list != NULL)` 检查了 `mtd->line_list` 的合法性，并在其为 NULL 时将 `tag` 设为 `UINT64_MAX`。告警行位于 `if (... |
| 2491 | tmux-3.1 | spawn_window | Dereference of null pointer | 189 | FP | FP | 告警点位于 `w->name = xstrdup(default_window_name(w));`，其中 `w` 指针在 `if (~sc->flags & SPAWN_RESPAWN)` 分支中已通过 `w = sc->wl->w... |
| 2492 | tmux-3.1 | cmdq_get_command | Dereference of null pointer | 248 | FP | FP | 在TAILQ_FOREACH循环中，当cmd->group != group条件首次为真时，shared会被xcalloc分配内存并初始化，随后shared->references被递增。由于xcalloc在失败时会调用fatalx终... |
| 2493 | tmux-3.1 | recalculate_sizes | Dereference of null pointer | 387 | FP | FP | 在访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已检查 `c->session` 是否为 NULL，若为 NULL 则直接 `continue`，确保了 `s`（即 `c->sess... |
| 2494 | tmux-3.0 | grid_string_cells | Dereference of null pointer | 918 | FP | FP | 告警点位于 `grid_string_cells_code(*lastgc, ...)` 调用处，工具认为 `*lastgc` 可能为空指针。但在调用前，代码已通过 `if (lastgc != NULL && *lastgc == ... |
| 2495 | tmux-3.0 | spawn_window | Dereference of null pointer | 183 | FP | FP | 告警指向 `w->name = xstrdup(sc->name);` 行，认为 `w` 可能为空指针。切片代码显示，在告警行之前，`w` 已在多个分支中被赋值（如 `w = sc->wl->window;` 或通过 `spawn_p... |
| 2496 | tmux-3.0 | grid_reflow_join | Dereference of null pointer | 1117 | FP | FP | 切片代码显示，在解引用 `from` 指针前，`from` 已在循环中被赋值为 `&gd->linedata[line]`，且该循环仅在 `gd->linedata[line].cellused != 0` 时才会进入，确保了 `fr... |
| 2497 | tmux-3.0 | mode_tree_build | Dereference of null pointer | 407 | FP | FP | 在告警行之前，代码已通过条件 `if (tag == UINT64_MAX)` 进行保护，仅当 `tag` 不等于 `UINT64_MAX` 时才会执行对 `mtd->line_list` 的访问。而 `tag` 被赋值为 `UINT... |
| 2498 | tmux-3.0 | spawn_window | Dereference of null pointer | 186 | FP | FP | 告警指向 `w->name = xstrdup(default_window_name(w));` 行，认为 `w` 可能为空指针。分析代码逻辑，当 `(~sc->flags & SPAWN_RESPAWN)` 为真时，`w` 在 `... |
| 2499 | tmux-3.0 | cmdq_get_command | Dereference of null pointer | 233 | FP | FP | 在TAILQ_FOREACH循环中，当cmd->group != group条件首次为真时，shared会被xcalloc分配内存并初始化；在后续迭代中，只要group未改变，shared将保持非空，因此shared->referen... |
| 2500 | tmux-3.0 | options_array_set | Dereference of null pointer | 368 | FP | FP | 告警指向的代码行 `*cause = xstrdup("empty command");` 位于 `if (cause != NULL)` 条件块内部，因此对 `cause` 指针的解引用是安全的，不会发生空指针解引用。 |
| 2501 | tmux-3.4 | recalculate_sizes_now | Dereference of null pointer | 458 | FP | FP | 在访问 s->statuslines 之前，代码通过 TAILQ_FOREACH 遍历 clients，并通过 ignore_client_size(c) 函数检查 c->session 是否为 NULL。该函数明确检查了 c->se... |
| 2502 | tmux-3.4 | mode_tree_draw | Dereference of null pointer | 750 | FP | FP | 告警指向的代码行 `xasprintf(&text, " %s (sort: %s%s)", mti->name, mtd->sort_list[mtd->sort_crit.field], ...);` 中，`mtd->sort_l... |
| 2503 | tmux-3.4 | mode_tree_get_tag | Dereference of null pointer | 309 | FP | FP | 告警点位于循环内的条件判断，用于比较 `mtd->line_list[i].item->tag` 与 `tag` 参数。切片代码显示，在访问 `item` 指针前，循环条件 `i < mtd->line_size` 确保了索引 `i`... |
| 2504 | tmux-3.4 | mode_tree_draw | Dereference of null pointer | 754 | FP | FP | 告警指向的代码行 `xasprintf(&text, " %s", mti->name);` 中，`mti` 指针在之前的逻辑中已通过 `mti = line->item;` 和 `if (mti->draw_as_parent) m... |
| 2505 | tmux-3.4 | grid_reflow_join | Dereference of null pointer | 1286 | FP | FP | 切片代码显示，在访问`from`指针前，`from = &gd->linedata[line];`已对其进行了明确的赋值，且`line`变量在循环中受控，因此不会出现空指针解引用。 |
| 2506 | tmux-3.4 | spawn_window | Dereference of null pointer | 181 | FP | FP | 告警行 `free(w->name);` 位于条件 `if (~sc->flags & SPAWN_RESPAWN)` 块内，而在此条件块之前，存在 `if (~sc->flags & SPAWN_RESPAWN) ... else ... |
| 2507 | tmux-3.4 | grid_string_cells | Dereference of null pointer | 1073 | FP | FP | 告警点位于 `grid_string_cells_code(*lastgc, ...)` 调用处，工具认为 `*lastgc` 可能为空指针。但在调用前，代码已通过 `if (lastgc != NULL && *lastgc == ... |
| 2508 | tmux-3.4 | server_client_reset_state | Dereference of null pointer | 2394 | FP | FP | 告警行代码 `s->cx` 中，变量 `s` 在切片代码的所有可达路径中均被明确赋值，不会为 NULL。在 `if (c->overlay_draw != NULL)` 分支中，`s` 被赋值为 `c->overlay_mode(..... |
| 2509 | tmux-3.4 | window_copy_move_after_search_mark | Dereference of null pointer | 3691 | FP | FP | 在调用 `window_copy_search_mark_at` 并返回0后，才访问 `data->searchmark[start]`，此时 `start` 已被有效赋值，且 `searchmark` 数组的索引 `start` 已... |
| 2510 | tmux-3.4 | input_parse | Dereference of null pointer | 912 | FP | FP | 代码在访问 `ictx->state->transitions` 前，已通过 `if` 条件确保 `ictx->state` 不为 NULL（因为 `ictx->state` 与 `state` 比较，而 `state` 初始化为 N... |

### 5.3 不一致：算法=TP，LLM=FP（共 74 条）

> 算法认为是真实漏洞（TP），但 LLM 认为是误报（FP）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 276 | git-2.47.1 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，其中 `string` 是字符串字面量 `DIGIT "abcdefABCDEF"`。`ARRAY_SI... |
| 277 | git-2.47.1 | test_ctype__ispunct | cpp/overflow-buffer | 91 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，其中 `string` 是宏参数 `PUNCT`。`PUNCT` 是一个预定义的字符串字面量，其大小在编... |
| 278 | git-2.47.1 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | TP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为0时结果为-1，但宏内已通过 `BUILD_ASSERT_OR_ZERO(ARRAY_S... |
| 279 | git-2.47.1 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但传入的 `string` 是一个字符串字面量，其 `ARRAY_SIZE` 结果大于0，因此 `ARRA... |
| 280 | git-2.47.1 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | TP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但宏内已通过 `BUILD_ASSERT_OR_ZERO(ARRA... |
| 281 | git-2.47.1 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | TP | FP | 宏 `TEST_CHAR_CLASS` 中 `ARRAY_SIZE(string) - 1` 的计算对象是字符串字面量 `"*?[\\"`，其大小在编译时已知且大于0，因此 `len` 的计算结果非负，不会导致负索引访问。告警是对宏展... |
| 282 | git-2.47.1 | test_ctype__isalnum | cpp/overflow-buffer | 51 | TP | FP | 宏 `TEST_CHAR_CLASS` 中的 `len` 计算为 `ARRAY_SIZE(string) - 1`，当 `string` 为 `LOWER UPPER DIGIT` 时，其 `ARRAY_SIZE` 大于0，因此 `l... |
| 283 | git-2.47.1 | test_ctype__isalpha | cpp/overflow-buffer | 46 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是宏参数，实际传入的是字面量字符串 `"LOWER UPPER"`，其 `ARRAY... |
| 284 | git-2.47.1 | test_ctype__isdigit | cpp/overflow-buffer | 41 | TP | FP | 宏 `TEST_CHAR_CLASS` 中 `len` 的计算 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但宏内包含 `BUILD_ASSERT_OR_Z... |
| 285 | git-2.47.1 | <global> | cpp/overflow-buffer | 36 | TP | FP | 切片代码显示函数体为空，不存在任何数组索引操作，因此告警所描述的访问负索引-1的情况不可能发生，属于工具误报。 |
| 403 | git-2.46.0 | get_rev | cpp/inconsistent-null-check | 189 | TP | FP | 函数 `prio_queue_get` 在队列为空时返回 NULL，但调用前已通过 `if (data->rev_list.nr == 0 ｜｜ data->non_common_revs == 0)` 检查了队列状态，确保了 `pr... |
| 406 | git-2.46.0 | fill_bitmap_commit | cpp/inconsistent-null-check | 493 | TP | FP | 代码在调用 `prio_queue_get` 前已通过 `while (queue->nr)` 检查队列非空，且 `prio_queue_get` 函数内部在 `queue->nr` 为0时返回NULL，因此该调用点不会返回NULL，... |
| 413 | git-2.46.0 | <global> | cpp/overflow-buffer | 40 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，其中 `string` 是字符串字面量。`ARRAY_SIZE` 宏返回数组大小（包含空终止符），因此 `... |
| 414 | git-2.46.0 | <global> | cpp/overflow-buffer | 41 | TP | FP | 告警指向宏 `TEST_CHAR_CLASS` 的调用，该宏内部使用 `ARRAY_SIZE(string) - 1` 计算长度。`ARRAY_SIZE` 宏作用于字符串字面量，其大小在编译时确定且大于0，因此 `ARRAY_SIZE... |
| 415 | git-2.46.0 | <global> | cpp/overflow-buffer | 42 | TP | FP | 告警指出的数组索引操作发生在宏 `TEST_CHAR_CLASS` 内部，用于计算字符串字面量的长度。`ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但宏中已通... |
| 416 | git-2.46.0 | <global> | cpp/overflow-buffer | 43 | TP | FP | 告警源于宏 `TEST_CHAR_CLASS` 的展开，其中 `ARRAY_SIZE(string) - 1` 在 `string` 为空字符串字面量 `""` 时可能产生 -1 的索引。但宏内包含 `BUILD_ASSERT_OR_... |
| 417 | git-2.46.0 | <global> | cpp/overflow-buffer | 47 | TP | FP | 宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但宏内已通过 `BUILD_ASSERT_OR_ZERO(ARRA... |
| 418 | git-2.46.0 | <global> | cpp/overflow-buffer | 48 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是字符串字面量，其 `ARRAY_SIZE` 至少为1（包含终止符），因此 `len... |
| 419 | git-2.46.0 | <global> | cpp/overflow-buffer | 49 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是字符串字面量，其 `ARRAY_SIZE` 至少为1（包含终止符），因此 `ARR... |
| 470 | curl-8_9_1 | Curl_splayremove | cpp/inconsistent-null-check | 270 | TP | FP | 在调用 `Curl_splay` 的代码路径中，`t->smaller` 已被显式检查为非空（`if(!t->smaller)`），因此传入的 `t->smaller` 参数是有效的，且被调用函数 `Curl_splay` 内部已处理... |
| 673 | vim-9.1.1591 | <global> | cpp/redundant-null-check-simple | 3506 | TP | FP | 告警指出的空指针检查（`inc_opt != NULL`）并非冗余，因为`inc_opt`可能为`NULL`（当`*curbuf->b_p_inc == NUL`且`p_inc`也为空时），且后续的`strstr`调用在`inc_op... |
| 674 | vim-9.1.1591 | <global> | cpp/redundant-null-check-simple | 3588 | TP | FP | 告警指出的空指针检查（`inc_opt != NULL`）并非冗余，因为`inc_opt`可能为`NULL`（当`*curbuf->b_p_inc == NUL`且`p_inc`也为空时）。切片代码显示`inc_opt`被赋值后，其值... |
| 675 | vim-9.1.1591 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | TP | FP | 切片代码显示，在访问 `linep[pos.col]` 和 `linep[pos.col + 1]` 之前，存在对 `pos.col` 的边界检查和调整逻辑（例如 `if (linep[pos.col] == NUL && pos.c... |
| 676 | vim-9.1.1591 | common_function | cpp/inconsistent-null-check | 5253 | TP | FP | 代码在调用 `vim_strsave` 后，将返回值赋给变量 `name`，并在后续多个分支中检查 `name` 是否为 NULL，若为 NULL 则调用 `vim_free(name)`（`vim_free` 内部会检查 NULL）... |
| 677 | vim-9.1.1591 | common_function | cpp/inconsistent-null-check | 5366 | TP | FP | 告警行 `pt->pt_func = find_func(trans_name, is_global);` 的返回值被直接赋值给 `pt->pt_func`，但切片代码显示，在调用 `find_func` 之前，`trans_name... |
| 679 | vim-9.1.1591 | get_isolated_shell_name | cpp/inconsistent-null-check | 2743 | TP | FP | 函数 `get_isolated_shell_name` 的返回值 `p` 被直接返回给调用者，调用者负责检查其是否为 NULL。告警点 `vim_strsave` 的返回值被赋值给 `p`，但 `p` 在另一个分支中也可能由 `vi... |
| 681 | vim-9.1.1591 | did_set_cryptmethod | cpp/inconsistent-null-check | 1923 | TP | FP | 代码中 `p_cm` 被赋值为 `vim_strsave((char_u *)"zip")`，其参数是常量字符串 "zip"，而非用户输入或动态内容，因此 `vim_strsave` 不会返回 NULL，无需检查。 |
| 682 | vim-9.1.1591 | did_set_background | cpp/inconsistent-null-check | 1098 | TP | FP | 告警点 `p_bg = vim_strsave(...)` 的返回值被立即传递给 `check_string_option(&p_bg)` 函数，该函数明确检查指针是否为 NULL 并在为 NULL 时将其赋值为 `empty_opt... |
| 683 | vim-9.1.1591 | apply_move_options | cpp/inconsistent-null-check | 531 | TP | FP | 调用 find_win_by_nr_or_id 的返回值在下一行立即被 win_valid_any_tab 函数检查，该函数内部已包含对 NULL 指针的显式检查（if (win == NULL) return FALSE;），因此代... |
| 684 | vim-9.1.1591 | <global> | cpp/inconsistent-null-check | 3339 | TP | FP | 告警指出的 `regnext` 调用未检查空指针，但切片代码显示该函数内部已处理空指针情况（返回 NULL 时直接处理为失败状态），且调用后 `next` 变量在后续逻辑中未解引用，因此不存在空指针解引用风险。 |
| 685 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1541 | TP | FP | 代码中 `regnode` 的返回值 `br` 被立即用于条件判断 `if (ret == NULL)` 和后续的 `regtail` 调用，其空值检查已通过 `ret` 和 `lastnode` 的判空逻辑间接完成，且切片中 `re... |
| 686 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1562 | TP | FP | 告警点 `br = regnode(NOTHING);` 的返回值未被检查，但切片代码显示 `regnode` 函数在 `regcode == JUST_CALC_SIZE` 模式下仅增加 `regsize` 并返回一个非空指针（`r... |
| 687 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1579 | TP | FP | 代码中调用 `regnext` 的返回值 `br` 在循环中仅用于迭代遍历链表，其是否为 NULL 由循环条件 `br != lastnode` 控制，且 `regnext` 函数内部已处理 NULL 返回（如 `reg_toolon... |
| 688 | vim-9.1.1591 | get_wordnode | cpp/inconsistent-null-check | 4636 | TP | FP | 函数 `getroom` 在内存分配失败时会返回 NULL，但调用点 `get_wordnode` 在 `spin->si_first_free == NULL` 的分支中，将 `getroom` 的返回值直接赋值给 `n`，随后在 ... |
| 689 | vim-9.1.1591 | do_tag | cpp/inconsistent-null-check | 638 | TP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续代码中被立即传递给 `vim_free(tofree)`，而 `tofree` 被赋值为 `name`，这表明内存管理是受控的。此外，`name` 变量在后续逻辑... |
| 691 | vim-9.1.1591 | exec_instructions | cpp/inconsistent-null-check | 3699 | TP | FP | alloc_clear 返回的指针被直接赋值给 tv->vval.v_object，后续代码立即对该对象进行成员访问（obj_class、obj_refcount 等），若 alloc_clear 返回 NULL 将导致空指针解引用。... |
| 692 | vim-9.1.1591 | barline_parse | cpp/inconsistent-null-check | 1158 | TP | FP | 代码中 `vim_strnsave` 的返回值被直接赋值给 `s`，而 `s` 随后被赋值给 `value->bv_string`。切片显示 `value->bv_allocated` 被设置为 `allocated ｜｜ conve... |
| 694 | vim-9.1.1591 | helptags_one | cpp/unsafe-strcat | 975 | TP | FP | 代码中使用了宏STRCAT，其底层调用标准库strcat，但目标缓冲区NameBuff在切片中未显示其大小定义，无法判断是否存在缓冲区溢出风险。然而，该告警点用于拼接目录路径和文件扩展名以生成通配符模式，输入的`dir`和`ext`参... |
| 710 | vim-9.1.1591 | win_redr_status_matches | cpp/unbounded-write | 717 | TP | FP | STRCPY 的目标缓冲区 `buf + len` 和源字符串 `transchar_byte(*s)` 均在受控范围内。`transchar_byte` 返回一个静态字符串，长度有限（通常为几个字符），而 `buf` 的大小为 `C... |
| 737 | vim-9.1.1591 | vim_rename | cpp/unbounded-write | 3865 | TP | FP | 在调用STRCPY(tempname, from)之前，已有条件判断`if (STRLEN(from) >= MAXPATHL - 5) return -1;`，确保源字符串`from`的长度小于`MAXPATHL - 5`，而目标缓... |
| 739 | vim-9.1.1591 | addfile | cpp/unbounded-write | 4219 | TP | FP | 代码在调用STRCPY（即strcpy）前，已使用STRLEN(f)计算了源字符串长度，并分配了恰好足够的空间（STRLEN(f) + 1 + isdir），因此不会发生缓冲区溢出。 |
| 762 | vim-9.1.1591 | highlight_set_startstop_termcode | cpp/unbounded-write | 1488 | TP | FP | 切片代码中，在调用STRCAT(buf, p)之前，已通过条件`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`进行了明确的长度检查，确保拼接后的总长度不会超过缓冲区buf的大小（100字节），因此... |
| 773 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2157 | TP | FP | 代码通过 `alloc(STRLEN(f) + 1)` 为目标缓冲区 `s` 分配了精确匹配源字符串 `f` 长度的空间，然后执行 `STRCPY(s, f)`，这确保了不会发生缓冲区溢出。告警是基于对 `strcpy` 的通用检测，... |
| 779 | vim-9.1.1591 | may_trigger_modechanged | cpp/unbounded-write | 2869 | TP | FP | STRCPY的目标缓冲区`last_mode`和源缓冲区`curr_mode`大小均为`MODE_MAX_LENGTH`，且`get_mode`函数确保写入`curr_mode`的字符数不会超过该大小，因此不存在缓冲区溢出风险。 |
| 784 | vim-9.1.1591 | add_to_showcmd | cpp/unbounded-write | 1764 | TP | FP | 切片代码显示，在调用STRCAT(showcmd_buf, p)前，已通过计算old_len和extra_len检查了缓冲区溢出风险，并在overflow > 0时使用mch_memmove移除了部分内容以确保拼接后长度不超过SHOW... |
| 816 | vim-9.1.1591 | getroom_save | cpp/unbounded-write | 4341 | TP | FP | 函数 getroom 已根据源字符串长度 s 分配了 STRLEN(s) + 1 字节的内存，目标缓冲区 sc 大小足够，strcpy 操作不会导致缓冲区溢出。 |
| 826 | vim-9.1.1591 | concat_str | cpp/unbounded-write | 792 | TP | FP | 函数内已通过alloc为目标缓冲区分配了精确的、足以容纳源字符串的长度（包括终止符），STRCPY（即strcpy）的调用不会导致缓冲区溢出。 |
| 827 | vim-9.1.1591 | concat_str | cpp/unbounded-write | 794 | TP | FP | 函数内通过alloc为目标缓冲区分配了精确大小（str1长度+str2长度+1），且STRCPY宏展开为strcpy，但源字符串长度已通过STRLEN计算并用于分配，因此不会发生缓冲区溢出。 |
| 828 | vim-9.1.1591 | strlow_save | cpp/unbounded-write | 463 | TP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(STRLEN(res) + 1 + newl - l)为目标缓冲区s分配了精确大小，确保目标缓冲区足以容纳源字符串（包括空终止符），因此不会发生缓冲区溢出。 |
| 837 | vim-9.1.1591 | alloc_ufunc | cpp/unbounded-write | 728 | TP | FP | 函数 `alloc_ufunc` 中，目标缓冲区 `fp->uf_name` 的大小是动态计算并分配的（`len = offsetof(ufunc_T, uf_name) + namelen + 1`），且分配时确保至少能容纳 `na... |
| 1586 | redis-8.0.2 | strbuf_init | Dereference of null pointer | 55 | TP | FP | 代码中`s->buf = NULL;`是对结构体指针`s`的成员进行赋值，并非解引用空指针。该操作是安全的初始化，不构成空指针解引用错误。 |
| 1587 | redis-8.0.2 | breakstat | Dereference of null pointer | 986 | TP | FP | 在while循环中，如果`bl`不为NULL，会持续遍历直到找到`isbreakable`为真的块或`bl`变为NULL。告警行`luaK_codeABC(fs, OP_CLOSE, bl->nactvar, 0, 0);`仅在`up... |
| 1594 | redis-8.0.2 | extent_try_coalesce_impl | Dereference of null pointer | 869 | TP | FP | 告警指向的代码行 `*coalesced = false;` 是对一个布尔指针的赋值，该指针 `coalesced` 是函数的传入参数，在函数内部已被检查和使用，其有效性由调用方保证。切片中未发现 `coalesced` 为 NULL... |
| 1601 | redis-8.0.2 | extent_try_coalesce_impl | Dereference of null pointer | 844 | TP | FP | 告警指向的代码行 `*coalesced = true;` 是对非空指针 `coalesced` 的赋值，该指针作为函数参数传入，在切片中可见其被多处使用且未被置空，不存在空指针解引用。 |
| 1608 | redis-8.0.2 | tcache_create_ctl | Dereference of null pointer | 2467 | TP | FP | 告警指向的宏 `VERIFY_READ` 在展开后，其条件判断 `if (oldp == NULL ｜｜ oldlenp == NULL ｜｜ *oldlenp != sizeof(t))` 中，对 `oldlenp` 的解引用 `*... |
| 1612 | redis-8.0.2 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | TP | FP | 告警位于宏 VERIFY_READ 内部，该宏在解引用 oldlenp 前已检查 oldp 和 oldlenp 是否为 NULL，因此不会发生空指针解引用。代码逻辑保证了安全性。 |
| 1613 | redis-8.0.2 | json_next_token | Dereference of null pointer | 1024 | TP | FP | 切片代码显示，在解引用 `ch2token[ch]` 之前，`ch2token` 指针已从 `json->cfg->ch2token` 获取，且 `json->cfg` 在函数调用前应已有效初始化。告警点位于循环内，`ch` 的值来自... |
| 1620 | redis-8.0.2 | min_expand | Dereference of null pointer | 322 | TP | FP | 在告警行 `singlematch(uchar(*s), p, ep)` 中，指针 `s` 在调用前已通过条件 `s<ms->src_end` 检查，确保其指向有效内存，因此解引用 `*s` 是安全的，不会发生空指针解引用。 |
| 1625 | redis-8.0.2 | arenas_create_ctl | Dereference of null pointer | 3101 | TP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在 oldp 或 oldlenp 为空时会设置 ret = EINVAL 并跳转到 label_return，从而避免了对空指针的后续解引用。切片代码中包含了完整的宏定义，显示存在明确的... |
| 1626 | redis-8.0.2 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | TP | FP | 告警指向宏 `VERIFY_READ` 中对 `oldlenp` 的空指针解引用。该宏在解引用 `*oldlenp` 前已通过 `oldp == NULL ｜｜ oldlenp == NULL` 的条件检查，若 `oldlenp` 为... |
| 1749 | ffmpeg-7.0.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1428 | TP | FP | 切片代码显示 `scale_matrix` 在条件 `s->ps.sps->scaling_list_enable_flag && !(transform_skip_flag && log2_trafo_size > 2)` 为真时被... |
| 1765 | ffmpeg-7.0.1 | check_available | Dereference of null pointer | 608 | TP | FP | 代码中`TAB_MVF`宏访问的`tab_mvf`数组索引由`n->x`和`n->y`计算得出，而`n`是函数参数，其可用性已在`n->available`赋值逻辑中通过`sps`和`cu`等上下文进行了严格的条件判断，`n->che... |
| 1794 | ffmpeg-7.0.1 | avc_parse_nal_units | Dereference of null pointer | 92 | TP | FP | 告警指向的代码行 `list->nb_nalus >= nalu_limit` 是对 `list->nb_nalus` 的读取，而非解引用。`list` 指针在函数入口作为参数传入，切片中未显示其可能为空，且后续代码逻辑（如 `lis... |
| 1813 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 471 | TP | FP | 告警指向宏 `DECODE_CODEWORD` 的调用，该宏展开后包含对指针 `gb` 的解引用。切片代码显示 `gb` 是函数参数，在函数内部被使用，但没有任何证据表明 `gb` 在调用此函数前为空。该告警是基于对函数内部逻辑的假设... |
| 2140 | git-2.49.0 | process_entry | Dereference of null pointer | 3413 | TP | FP | 告警点位于RENAME_ONE_FILE_TO_TWO分支的赋值语句，该分支仅在ci->ren2非空时执行，而切片代码中第15行已通过`if (ci->ren2)`进行了显式保护，确保了ci->ren2的有效性，因此不会发生空指针解引用。 |
| 2253 | git-2.50.1 | <global> | Dereference of null pointer | 88 | TP | FP | 告警位于单元测试代码中，`out` 指针在 `check(out != NULL)` 后使用，测试逻辑确保了 `out` 非空，不会发生空指针解引用。 |
| 2262 | git-2.50.1 | <global> | Dereference of null pointer | 82 | TP | FP | 告警点位于单元测试代码中，`check_str(out[0], "line");` 前已通过 `check(out != NULL);` 确保 `out` 非空，且 `parse_names` 函数在成功时返回以NULL结尾的字符串数... |
| 2285 | git-2.50.1 | write_table | Dereference of null pointer | 65 | TP | FP | 告警指向的代码行 `refs[i].refname = (*names)[i] = xstrfmt(...);` 中，`xstrfmt` 是分配内存并返回字符串指针的函数，不会返回 NULL。切片中 `(*names)[i]` 的赋值... |
| 2297 | git-2.50.1 | <global> | Dereference of null pointer | 200 | TP | FP | 告警位于单元测试代码中，`arr[0] = 42;` 行之前已通过 `REFTABLE_ALLOC_GROW_OR_NULL` 宏检查并确保 `arr != NULL`，切片内可见的测试逻辑保证了指针的有效性，因此是误报。 |
| 2300 | git-2.50.1 | t_log_write_read | Dereference of null pointer | 224 | TP | FP | 告警指向 `names[i] = xstrdup(name);` 行，但切片中未定义 `names` 数组，且 `xstrdup` 函数在内存分配失败时会调用 `die` 终止程序，因此不会返回空指针。告警基于不完整的上下文（缺少 `... |
| 2308 | git-2.50.1 | <global> | Dereference of null pointer | 206 | TP | FP | 告警位于单元测试代码中，`arr[alloc - 1] = 42;` 这行代码前已通过 `check(arr != NULL);` 确保了 `arr` 非空，且 `alloc` 已增长，因此不会发生空指针解引用。这是测试逻辑的一部分，... |
| 2313 | git-2.50.1 | t_table_refs_for | Dereference of null pointer | 577 | TP | FP | 告警点位于循环内部，`want_names` 数组在循环前未初始化，但循环内 `want_names_len` 从0开始递增，`want_names[want_names_len++]` 的访问依赖于 `want_names` 的初始... |
| 2367 | git-2.47.1 | assert_sane_strbuf | Dereference of null pointer | 36 | TP | FP | 告警点位于宏展开后的检查函数内部，其目的是验证传入的指针 `buf->buf` 不为空。在调用 `check_char` 之前，代码已通过 `check(!!buf->buf)` 对指针进行了非空断言，因此后续的 `buf->buf[... |
| 2488 | tmux-3.1 | <global> | Dereference of null pointer | 74 | TP | FP | 告警点位于条件判断 `if (wme == NULL ｜｜ wme->mode->key_table == NULL)` 之后，该条件已确保 `wme` 非空且 `wme->mode` 非空，因此对 `wme->mode->key_t... |

### 5.4 不一致：算法=FP，LLM=TP（共 110 条）

> 算法认为是误报（FP），但 LLM 认为是真实漏洞（TP）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 44 | ffmpeg-7.0.1 | get_frag_time | cpp/inconsistent-null-check | 1541 | FP | TP | 函数 get_frag_stream_info 可能返回 NULL，但调用后未检查返回值就直接解引用访问其成员（如 frag_stream_info->sidx_pts），存在空指针解引用风险。 |
| 60 | ffmpeg-7.1 | get_frag_time | cpp/inconsistent-null-check | 1630 | FP | TP | 函数 get_frag_stream_info 可能返回 NULL，但调用后未检查返回值就直接解引用其成员（如 frag_stream_info->sidx_pts），存在空指针解引用风险。 |
| 351 | git-2.49.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1932 | FP | TP | 代码在调用 submodule_from_path 后未检查返回值 sub 是否为 NULL，随后直接解引用 sub->name，存在空指针解引用风险。切片中未见任何前置校验或防护机制。 |
| 376 | git-2.49.0 | add_patterns | cpp/invalid-pointer-deref | 1152 | FP | TP | 代码在分配大小为 `size` 的缓冲区 `buf` 后，执行了 `buf[size++] = '\n';`，这明显是对缓冲区末尾之后一个字节的越界写入，存在内存损坏风险。 |
| 393 | git-2.46.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1900 | FP | TP | 代码在调用submodule_from_path后未检查返回值sub是否为NULL，随后直接解引用sub->name，存在空指针解引用风险。切片中未见任何防护机制确保sub非空。 |
| 420 | git-2.46.0 | add_patterns | cpp/invalid-pointer-deref | 1150 | FP | TP | 代码在分配大小为 `size` 的缓冲区后，执行 `buf[size++] = '\n';`，这明显是对缓冲区末尾之后一个字节的越界写入，属于典型的缓冲区溢出漏洞。 |
| 507 | vim-9.1.0550 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 '%6ld' 写入最多6位数字、一个符号位和字符串终止符，在最坏情况下（如 lnum 为 -100000）需要至少8个字符，而目标缓冲区 tbuf 仅20字节，足够容纳，但告警提示需要21字节，这表明格... |
| 508 | vim-9.1.0550 | highlight_color | cpp/overrunning-write | 3254 | FP | TP | sprintf 目标缓冲区 'buf' 大小为10字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少10字节，当三个颜色分量均为最大值（0xff）时，生成的字符串 "#ffffffff" 恰好为10字节（含终止符... |
| 509 | vim-9.1.0550 | msg_outnum | cpp/overrunning-write | 1555 | FP | TP | 函数`sprintf`的目标缓冲区`buf`大小为20字节，但格式化长整数`%ld`的最大长度（如-9223372036854775808）为20个字符加1个空终止符，共21字节，存在缓冲区溢出风险。切片代码中未见任何输入验证或缓冲区... |
| 510 | vim-9.1.0550 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf函数将格式化的字符串写入大小为32字节的固定数组reply，当cmdno和result的值组合超过31个字符（加上空终止符）时，会导致缓冲区溢出。切片代码中未显示任何对输入长度的校验或使用安全函数（如snprintf）的... |
| 511 | vim-9.1.0550 | uc_check_code | cpp/overrunning-write | 1764 | FP | TP | 代码中`sprintf`的目标缓冲区`num_buf`大小为20字节，而格式化长整型数值`%ld`在极端情况下（如-9223372036854775808）需要21字节，存在缓冲区溢出风险。切片中未见任何输入验证或大小限制来防止此情况。 |
| 521 | vim-9.1.0550 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串fname复制到新分配的内存name中，未检查目标缓冲区大小，而fname是函数参数，其长度可能超过分配的内存（STRLEN(fname) + 3），存在缓冲区溢出风险。 |
| 527 | vim-9.1.0550 | cat_prefix_varname | cpp/unbounded-write | 2504 | FP | TP | 代码使用STRCPY（即strcpy）将外部传入的`name`字符串复制到缓冲区`varnamebuf + 2`处，虽然缓冲区大小`varnamebuflen`根据`STRLEN(name) + 3 + 10`分配，但分配后未检查`a... |
| 535 | vim-9.1.0550 | replace_makeprg | cpp/unbounded-write | 5039 | FP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串p复制到固定大小的缓冲区ptr中，存在缓冲区溢出的风险。虽然p的来源在切片中未完全展示，但告警明确指出其可能来自环境变量、文件读取等外部输入，且代码中未见任何长度检查或安全... |
| 536 | vim-9.1.0550 | replace_makeprg | cpp/unbounded-write | 5054 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串'program'和'p'复制到固定大小的缓冲区'new_cmdline'中，而'new_cmdline'的大小是基于这些字符串的长度计算分配的，但分配后存在多个连续的STR... |
| 540 | vim-9.1.0550 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 代码使用`sprintf`将`&mesg[1]`的内容格式化写入`val`缓冲区，`mesg`来源于用户输入或外部数据，其长度未受限制，而目标缓冲区`val`的大小是预先根据`mesg`长度计算的，但`sprintf`添加了额外的格式... |
| 543 | vim-9.1.0550 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 861 | FP | TP | 代码使用STRCPY（即strcpy）将动态长度的字符串p复制到固定大小的缓冲区ccline.cmdbuff，虽然之前调用了realloc_cmdbuff(len + 1)来确保缓冲区大小足够，但该函数内部仅当len小于当前缓冲区长度... |
| 555 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1721 | FP | TP | 代码中直接使用STRCPY（即strcpy）宏将`rel_fname`或`*file_to_find`复制到固定大小的`NameBuff`缓冲区，未检查源字符串长度是否超过`MAXPATHL`，存在缓冲区溢出风险。 |
| 580 | vim-9.1.0550 | prt_resource_name | cpp/unbounded-write | 1659 | FP | TP | 代码使用strcpy将filename复制到resource_filename，虽然对filename长度进行了检查，但resource_filename缓冲区的大小未知，若其大小小于MAXPATHL，则存在缓冲区溢出风险。 |
| 587 | vim-9.1.0550 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | 代码使用`sprintf`将变量`csinfo[i].ppath`和`name`拼接到固定大小的缓冲区`fullname`中，而`fullname`的大小`len`由这两个字符串的长度计算得出，未包含分隔符`/`和终止符`\0`的空间... |
| 590 | vim-9.1.0550 | <global> | cpp/unbounded-write | 1456 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，虽然分配的大小为strlen(fname)+1，但fname是外部传入的文件名，其长度可能超过目标缓冲区大小（如果分配失败或后续修改了缓冲区大小）。strcpy本身不检查边界，存在... |
| 591 | vim-9.1.0550 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是函数参数，其长度未经验证，而strcpy不检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 617 | vim-9.1.0550 | set_init_default_backupskip | cpp/unbounded-write | 169 | FP | TP | 代码使用STRCPY（即strcpy）将环境变量内容复制到固定大小的缓冲区`item`，而`item`的大小`len`仅基于环境变量字符串长度计算，未考虑目标缓冲区大小限制，存在缓冲区溢出风险。 |
| 622 | vim-9.1.0550 | reg_submatch | cpp/unbounded-write | 2689 | FP | TP | 代码在循环中使用 STRCPY（即 strcpy）将 reg_getline_submatch 返回的字符串复制到固定大小的缓冲区 retval 中，但 retval 的大小仅由 alloc(len) 分配，而 len 的计算依赖于匹... |
| 623 | vim-9.1.0550 | reg_submatch | cpp/unbounded-write | 2698 | FP | TP | 代码在循环中使用STRCPY（即strcpy）将reg_getline_submatch返回的字符串复制到固定大小的缓冲区retval中，而retval的大小仅由alloc(len)分配，len的计算依赖于外部匹配位置，若源字符串长度... |
| 632 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2755 | FP | TP | 函数为输入字符串`name`分配了固定长度（STRLEN(name) + 14）的缓冲区`scriptname`，随后使用STRCAT（即strcat）向其追加内容。strcat会从目标缓冲区的当前末尾开始写入，如果之前已写入的内容加... |
| 633 | vim-9.1.0550 | ExpandPackAddDir | cpp/unbounded-write | 1226 | FP | TP | sprintf 使用未限制长度的用户输入 pat 作为格式化字符串的一部分，目标缓冲区 s 的大小为 pat_len + 26，若 pat 长度足够大，拼接后的字符串可能超过缓冲区大小，存在缓冲区溢出风险。 |
| 634 | vim-9.1.0550 | sign_jump | cpp/unbounded-write | 1324 | FP | TP | sprintf 使用未限制长度的缓冲区 buf->b_fname 作为格式化字符串的一部分，且目标缓冲区 cmd 的大小仅基于 STRLEN(buf->b_fname) + 25 分配，无法防止当 buf->b_fname 长度接近或... |
| 640 | vim-9.1.0550 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）将参数lang复制到固定大小的数组sl.sl_lang中，但切片未显示对lang的长度有任何校验或限制，存在缓冲区溢出风险。 |
| 656 | vim-9.1.0550 | findtags_add_match | cpp/unbounded-write | 2703 | FP | TP | 代码中直接使用 STRCPY（即 strcpy）宏将 st->tag_fname、st->ebuf 和 st->lbuf 等字符串复制到固定大小的缓冲区 mfp 中，而 mfp 的大小由 alloc 分配，其长度计算依赖于这些源字符串... |
| 660 | vim-9.1.0550 | get_scriptlocal_funcname | cpp/unbounded-write | 4608 | FP | TP | 代码使用 `STRCAT(newname, p + off)` 向动态分配的缓冲区 `newname` 追加字符串，但 `newname` 的大小仅根据 `sid_buf` 和 `p + off` 的长度之和分配，未考虑 `strca... |
| 664 | vim-9.1.0550 | set_ufunc_name | cpp/unbounded-write | 663 | FP | TP | 代码直接使用STRCPY（即strcpy）将外部传入的字符串name复制到固定大小的缓冲区fp->uf_name中，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 666 | vim-9.1.0550 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到固定大小的缓冲区`funcname`中，而`funcname`的大小仅为`STRLEN(name) + 3`，未考虑目标缓冲区大小，存在缓冲区溢出风险。 |
| 670 | vim-9.1.0550 | xxdline | cpp/unbounded-write | 533 | FP | TP | 函数`xxdline`中的`strcpy(z, l)`将外部输入`l`复制到固定大小的静态缓冲区`z`（大小为`LLEN+1`），且切片中未显示对`l`的长度有任何校验或限制，存在缓冲区溢出风险。 |
| 700 | vim-9.1.1591 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 写入的目标缓冲区 `reply` 大小为 32 字节，但格式化字符串 `"%d %ld\n"` 在最坏情况下（如 `cmdno` 为负的 10 位数，`result` 为负的 10 位数）所需空间超过 32 字节，存在... |
| 764 | vim-9.1.1591 | cs_resolve_file | cpp/unbounded-write | 2438 | FP | TP | 代码使用`sprintf`将`csinfo[i].ppath`和`name`拼接至`fullname`，`fullname`的分配长度`len`计算了`strlen(name) + 2`及可能的路径长度，但`sprintf`格式字符串... |
| 767 | vim-9.1.1591 | <global> | cpp/unbounded-write | 1454 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是函数参数，其长度未经验证，而目标缓冲区大小仅为strlen(fname)+1，strcpy本身存在缓冲区溢出风险，因为strcpy不检查目标缓冲区大小，若fname在调... |
| 768 | vim-9.1.1591 | <global> | cpp/unbounded-write | 1463 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是外部传入的文件名字符串，其长度未经验证。虽然分配了strlen(fname)+1的空间，但若fname在分配后、复制前被恶意修改或并发篡改，仍可能导致缓冲区溢出。切片中... |
| 769 | vim-9.1.1591 | cs_add_common | cpp/unbounded-write | 603 | FP | TP | 代码使用`sprintf`拼接`fname`和`CSCOPE_DBFILE`，其中`fname`来自用户输入（可能包含环境变量），且未对拼接后的总长度进行限制，存在缓冲区溢出风险。 |
| 782 | vim-9.1.1591 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf 使用未受控的 `result` 作为格式化字符串的一部分，目标缓冲区 `reply` 的大小为 `STRLEN(result) + 32`，但 sprintf 的输出长度可能超过此值，因为 `cmdno` 的字符串表示... |
| 850 | vim-9.1.1040 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数 `getcell` 可能返回 NULL，但调用后未检查返回值就直接解引用 `cell->chars[0]`，存在空指针解引用风险。 |
| 869 | vim-9.1.1040 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 '%6ld' 将长整型 lnum 写入大小为 20 字节的 tbuf 数组。当 lnum 为 6 位数字时，格式化的字符串包含 6 个数字字符，但 sprintf 还会添加一个终止空字符 '\0'，总共... |
| 870 | vim-9.1.1040 | highlight_color | cpp/overrunning-write | 3259 | FP | TP | sprintf 目标缓冲区 'buf' 大小为 10 字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少 8 个字符（# + 6个十六进制数字 + '\0'），计算出的实际需求为 8 字节，小于缓冲区大小，因此告... |
| 871 | vim-9.1.1040 | msg_outnum | cpp/overrunning-write | 1653 | FP | TP | 函数 `msg_outnum` 使用 `sprintf` 将长整型 `n` 格式化到大小为20字节的缓冲区 `buf` 中。对于某些负数值（例如 -9223372036854775808），格式化后的字符串长度可能达到21字节（包括负... |
| 872 | vim-9.1.1040 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 写入的目标缓冲区 `reply` 大小为 32 字节，但格式化字符串 `"%d %ld\n"` 在最坏情况下（如 cmdno 为负长整数）可能超过 32 字节，导致缓冲区溢出。 |
| 882 | vim-9.1.1040 | debuggy_find | cpp/unbounded-write | 1067 | FP | TP | 代码中 `STRCPY` 宏展开为 `strcpy`，将 `fname + 3` 复制到 `name + 5`，目标缓冲区 `name` 的大小为 `STRLEN(fname) + 3`，但源字符串 `fname + 3` 的长度可能... |
| 895 | vim-9.1.1040 | replace_makeprg | cpp/unbounded-write | 5014 | FP | TP | 代码使用STRCPY（即strcpy）将用户控制的参数p复制到固定大小的缓冲区ptr中，而ptr指向的缓冲区new_cmdline大小是基于program长度和p长度计算的，但STRCPY调用本身没有边界检查，存在缓冲区溢出风险。 |
| 896 | vim-9.1.1040 | replace_makeprg | cpp/unbounded-write | 5029 | FP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串program和p复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小是基于STRLEN(program)和STRLEN(p)计算的，但strcpy... |
| 900 | vim-9.1.1040 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 代码使用`sprintf`将`&mesg[1]`的内容格式化写入`val`缓冲区，`mesg`来源于用户输入或外部数据，且切片中未显示对`mesg`长度进行任何校验或限制，存在缓冲区溢出风险。 |
| 901 | vim-9.1.1040 | escape_fname | cpp/unbounded-write | 4105 | FP | TP | 代码使用`strcpy`将源字符串`*pp`复制到目标缓冲区`p+1`，目标缓冲区大小仅为`STRLEN(*pp) + 2`，恰好等于源字符串长度加2（用于前缀'\\'和结尾空字符），因此不会发生缓冲区溢出。但告警指出源可能来自环境变... |
| 903 | vim-9.1.1040 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 860 | FP | TP | 代码使用STRCPY（即strcpy）将动态长度的字符串p复制到固定大小的缓冲区ccline.cmdbuff中，虽然之前调用了realloc_cmdbuff(len + 1)来调整缓冲区大小，但该函数内部使用alloc_cmdbuff... |
| 945 | vim-9.1.1040 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | sprintf 使用未经验证的字符串拼接，目标缓冲区 `fullname` 的大小 `len` 可能不足以容纳拼接后的完整路径，存在缓冲区溢出风险。 |
| 949 | vim-9.1.1040 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是外部传入的文件名参数，其长度未经验证。虽然分配了strlen(fname)+1的空间，但strcpy本身不检查边界，若fname在调用cs_insert_filelis... |
| 952 | vim-9.1.1040 | <global> | cpp/unbounded-write | 3129 | FP | TP | 代码中直接使用`sprintf`将格式化字符串和变量`transchar(from)`写入固定缓冲区`args->os_errbuf`，未检查缓冲区大小，存在缓冲区溢出风险。切片中未显示对`args->os_errbuf`长度的限制或验证。 |
| 964 | vim-9.1.1040 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | sprintf 使用未受控的外部输入 result 作为格式化字符串的一部分，且目标缓冲区 reply 的大小仅基于 result 的当前长度分配，未考虑格式化添加的额外字符（如 cmdno 和换行符），存在缓冲区溢出的风险。 |
| 980 | vim-9.1.1040 | reg_submatch | cpp/unbounded-write | 2723 | FP | TP | 代码在多个路径中直接使用STRCPY宏（即strcpy）复制未知长度的字符串到固定大小的缓冲区，且切片中未显示对源字符串长度进行任何检查或限制，存在缓冲区溢出风险。 |
| 981 | vim-9.1.1040 | reg_submatch | cpp/unbounded-write | 2732 | FP | TP | 代码在循环中使用 STRCPY（即 strcpy）向固定大小的缓冲区 retval 写入内容，而 retval 的大小由 alloc(len) 分配，len 的计算依赖于外部输入（如匹配位置和行长度），若计算出的 len 不足以容纳所... |
| 989 | vim-9.1.1040 | stuff_yank | cpp/unbounded-write | 470 | FP | TP | 代码使用STRCPY（即strcpy）将源字符串复制到固定大小的缓冲区tmp中，而tmp的大小由tmplen决定，但源字符串pp->string的长度未知且未在切片中显示有任何边界检查，存在缓冲区溢出的风险。 |
| 990 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2838 | FP | TP | 函数`autoload_name`中，`scriptname`缓冲区的大小基于输入`name`的长度分配，但后续`STRCAT`操作可能将`name`（或其子串）追加到已包含固定前缀"autoload/"的同一缓冲区中，若`name`... |
| 991 | vim-9.1.1040 | ExpandPackAddDir | cpp/unbounded-write | 1309 | FP | TP | sprintf 使用未限制长度的用户输入 pat 作为格式化字符串的一部分，目标缓冲区 s 的大小为 pat_len + 26，若 pat 长度被精心构造，可能导致缓冲区溢出。切片中未见对 pat 长度的任何验证或使用更安全的函数。 |
| 992 | vim-9.1.1040 | sign_jump | cpp/unbounded-write | 1313 | FP | TP | sprintf 使用未受控的缓冲区指针 buf->b_fname 作为格式化字符串的一部分，且目标缓冲区 cmd 的大小仅基于 b_fname 的长度计算，未考虑格式化字符串 'e +%ld ' 和长整型变量 lnum 的潜在长度，存... |
| 997 | vim-9.1.1040 | count_common_word | cpp/unbounded-write | 1919 | FP | TP | 代码使用 STRCPY（即 strcpy）将长度未知的字符串 p 复制到新分配的内存 wc->wc_word 中，而分配的大小仅基于 STRLEN(p) + 1，未对源字符串长度进行限制，存在缓冲区溢出的风险。 |
| 1013 | vim-9.1.1040 | findtags_add_match | cpp/unbounded-write | 2623 | FP | TP | 代码中直接使用 STRCPY（即 strcpy）将 st->help_lang 复制到固定大小的缓冲区 p 中，而 st->help_lang 是环境变量，其长度未经验证，可能导致缓冲区溢出。切片中未见任何长度检查或安全复制机制。 |
| 1014 | vim-9.1.1040 | findtags_add_match | cpp/unbounded-write | 2702 | FP | TP | 代码中多次使用STRCPY（即strcpy）宏，将长度未知的源字符串（如st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1021 | vim-9.1.1040 | fname_trans_sid | cpp/unbounded-write | 2224 | FP | TP | 代码在分配动态缓冲区后，使用STRCPY（即strcpy）进行字符串复制，未检查源字符串长度是否超过目标缓冲区大小。虽然存在长度计算，但未在复制前进行边界检查，存在缓冲区溢出风险。 |
| 1035 | vim-9.1.1330 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | TP | 函数 `getcell` 可能返回 NULL，但调用点 `vterm_screen_is_eol` 未检查返回值便直接解引用 `cell->chars[0]`，存在空指针解引用风险。 |
| 1054 | vim-9.1.1330 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 的目标缓冲区 tbuf 大小为 20 字节，但格式化字符串 '%6ld' 最多可产生 6 位数字加一个符号位和终止符，共 8 字节，不会溢出。然而，告警指出需要 21 字节，这暗示 lnum 可能为 long 类型，其... |
| 1056 | vim-9.1.1330 | msg_outnum | cpp/overrunning-write | 1653 | FP | TP | 函数 `msg_outnum` 使用 `sprintf` 将长整型 `n` 写入大小为20字节的栈数组 `buf`，当 `n` 为最小值（如-9223372036854775808）时，格式化字符串长度（包括负号和终止空字符）可能达到... |
| 1057 | vim-9.1.1330 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 的目标缓冲区 `reply` 大小为 32 字节，但格式化字符串 "%d %ld\n" 在最坏情况下（如 cmdno 为负长整数，result 为长整数最小值）可能产生超过 32 字节的输出，存在缓冲区溢出的风险。 |
| 1072 | vim-9.1.1330 | cat_prefix_varname | cpp/unbounded-write | 2576 | FP | TP | 代码使用strcpy复制外部传入的字符串'name'到缓冲区'varnamebuf'，虽然缓冲区大小'len'根据'name'的长度计算并分配，但分配后立即将'varnamebuf'的前两个字节用于存储前缀和冒号，导致STRCPY的目... |
| 1078 | vim-9.1.1330 | repl_cmdline | cpp/unbounded-write | 5311 | FP | TP | 代码使用STRCPY（即strcpy）将未限制长度的源字符串复制到固定大小的缓冲区new_cmdline中，而new_cmdline的大小由变量i决定，i的计算包含了多个未经验证其长度的字符串，存在缓冲区溢出的实际风险。 |
| 1080 | vim-9.1.1330 | replace_makeprg | cpp/unbounded-write | 5018 | FP | TP | 代码使用STRCPY（即strcpy）将未限制长度的字符串p复制到目标缓冲区ptr，而p是用户提供的命令行参数，其长度可能超过目标缓冲区剩余空间，存在缓冲区溢出风险。切片中未见对p的长度进行检查或限制。 |
| 1081 | vim-9.1.1330 | replace_makeprg | cpp/unbounded-write | 5033 | FP | TP | 代码使用STRCPY（即strcpy）将外部来源的字符串（如环境变量、文件读取内容）复制到固定大小的缓冲区，且切片中未显示对源字符串长度进行任何检查或限制，存在缓冲区溢出风险。 |
| 1085 | vim-9.1.1330 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 代码使用`sprintf`将`&mesg[1]`的内容格式化写入缓冲区`val`，而`mesg`来源于用户输入或外部数据，其长度未受限制，可能导致缓冲区溢出。切片中未见对`mesg`长度的验证或使用安全函数。 |
| 1086 | vim-9.1.1330 | escape_fname | cpp/unbounded-write | 4116 | FP | TP | 代码使用 STRCPY（即 strcpy）将源字符串 *pp 复制到目标缓冲区 p+1，目标缓冲区大小仅为 STRLEN(*pp) + 2，但源字符串 *pp 可能包含空字符，导致 strcpy 在遇到空字符前复制过多字符，从而溢出目... |
| 1088 | vim-9.1.1330 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 860 | FP | TP | 代码使用STRCPY（即strcpy）将动态长度的字符串p复制到固定大小的缓冲区ccline.cmdbuff中，虽然之前调用了realloc_cmdbuff(len + 1)来调整缓冲区大小，但该函数内部使用alloc_cmdbuff... |
| 1113 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 1112 | FP | TP | 代码使用`sprintf`将动态内容（`p1`和`fname`）写入固定大小的缓冲区`s`，而`s`的大小计算为`p2 - p1 + STRLEN(fname) + 2`，未考虑`sprintf`格式字符串`"%s\t%s"`本身可能... |
| 1115 | vim-9.1.1330 | load_colors | cpp/unbounded-write | 606 | FP | TP | sprintf 使用未经验证的用户输入 `name` 拼接字符串，目标缓冲区 `buf` 的大小仅为 `STRLEN(name) + 12`，若 `name` 长度过长，拼接后的字符串 'colors/%s.vim' 可能超过缓冲区大... |
| 1116 | vim-9.1.1330 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | 代码使用`sprintf`将`csinfo[i].ppath`和`name`拼接到`fullname`缓冲区，`fullname`的大小由`len`决定。`len`的计算包含了`strlen(name)`和`strlen(csinfo... |
| 1120 | vim-9.1.1330 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是函数参数，其长度未在切片内进行任何检查或限制，存在缓冲区溢出风险。 |
| 1134 | vim-9.1.1330 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | 代码使用`sprintf`将变量`cmdno`和`result`格式化写入固定大小的缓冲区`reply`，而`reply`的大小仅基于`result`的长度计算，未考虑`cmdno`的格式化长度和固定字符串的开销，存在缓冲区溢出的风险。 |
| 1149 | vim-9.1.1330 | reg_submatch | cpp/unbounded-write | 2732 | FP | TP | 代码在round==2时，使用STRCPY（即strcpy）将未经验证长度的源字符串`s`复制到固定大小的目标缓冲区`retval`中，而`retval`的大小`len`是在第一轮计算得出的，但复制操作发生在`len`递增之前，存在缓... |
| 1159 | vim-9.1.1330 | ExpandPackAddDir | cpp/unbounded-write | 1309 | FP | TP | sprintf 使用未经验证的用户输入 `pat` 拼接格式字符串，目标缓冲区 `s` 的大小为 `pat_len + 26`，但格式字符串 `"pack/*/opt/%s*"` 在拼接后可能超过该大小，存在缓冲区溢出风险。 |
| 1160 | vim-9.1.1330 | sign_jump | cpp/unbounded-write | 1313 | FP | TP | sprintf 使用未限制长度的外部输入 buf->b_fname 和变量 lnum 格式化字符串，目标缓冲区 cmd 的大小仅基于 b_fname 的当前长度计算，未考虑格式化后字符串的总长度，存在缓冲区溢出风险。 |
| 1183 | vim-9.1.1330 | findtags_add_match | cpp/unbounded-write | 2703 | FP | TP | 代码中多次使用 STRCPY（即 strcpy）宏将未知长度的源字符串（如 st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区 mfp 中，而 mfp 的大小由 alloc 分配，其长度计算依赖... |
| 1223 | vim-9.1.0790 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 目标缓冲区 tbuf 大小为 20 字节，但格式化字符串 '%6ld' 在 lnums 为某些值时（如 1000000）会产生 7 个数字字符加一个空终止符，共 8 字节，不会溢出。然而，当 lnum 为负数时，格式化... |
| 1224 | vim-9.1.0790 | highlight_color | cpp/overrunning-write | 3254 | FP | TP | sprintf 目标缓冲区 `buf` 大小为10字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少10字节（# + 6个十六进制字符 + '\0'），计算表明需要10字节，但告警提示需要14字节，可能涉及宽字符... |
| 1225 | vim-9.1.0790 | msg_outnum | cpp/overrunning-write | 1555 | FP | TP | 函数 `msg_outnum` 使用 `sprintf` 将长整型 `n` 格式化到大小为20字节的缓冲区 `buf` 中。对于某些负数值（例如 -9223372036854775808），格式化后的字符串长度可能达到21字节（包括负... |
| 1226 | vim-9.1.0790 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf 函数将格式化的字符串写入大小为 32 字节的栈数组 reply，当 cmdno 和 result 的值组合超过 31 个字符（加上结尾空字符）时，会发生缓冲区溢出。切片代码中未见任何输入验证或长度检查来防止此情况。 |
| 1248 | vim-9.1.0790 | repl_cmdline | cpp/unbounded-write | 5302 | FP | TP | 代码使用STRCPY（即strcpy）将未限制长度的源字符串复制到固定大小的缓冲区new_cmdline中，且切片内未见对源字符串长度进行校验或使用安全函数，存在缓冲区溢出风险。 |
| 1250 | vim-9.1.0790 | replace_makeprg | cpp/unbounded-write | 5009 | FP | TP | 代码使用STRCPY（即strcpy）将用户输入或环境变量等外部数据复制到固定大小的缓冲区，未进行边界检查，存在缓冲区溢出风险。切片中未显示对源字符串长度的限制或目标缓冲区大小的验证。 |
| 1255 | vim-9.1.0790 | get_exception_string | cpp/unbounded-write | 484 | FP | TP | 代码使用`sprintf`将`&mesg[1]`的内容格式化写入`val`缓冲区，`mesg`来源于用户输入或外部数据（`throw_msg`），且切片中未显示对`mesg`长度的验证或对目标缓冲区`val`大小的检查，存在缓冲区溢出风险。 |
| 1301 | vim-9.1.0790 | load_colors | cpp/unbounded-write | 602 | FP | TP | sprintf 使用未经验证的用户输入 `name` 拼接字符串，目标缓冲区 `buf` 的大小为 `STRLEN(name) + 12`，但格式化字符串 `"colors/%s.vim"` 的长度加上 `name` 的长度可能超过缓... |
| 1302 | vim-9.1.0790 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | TP | 代码使用`sprintf`将`csinfo[i].ppath`和`name`拼接到`fullname`缓冲区，缓冲区大小`len`由`strlen(name) + 2`加上`strlen(csinfo[i].ppath)`计算得出，但... |
| 1305 | vim-9.1.0790 | <global> | cpp/unbounded-write | 1456 | FP | TP | 代码使用strcpy将fname复制到新分配的内存中，fname是函数参数，其长度未经验证，而分配的大小仅为strlen(fname)+1，strcpy本身不检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 1306 | vim-9.1.0790 | <global> | cpp/unbounded-write | 1465 | FP | TP | 代码使用 `strcpy` 将 `fname` 复制到新分配的缓冲区，`fname` 是函数参数，其长度未经验证，而 `alloc` 仅分配 `strlen(fname)+1` 字节，`strcpy` 调用本身存在缓冲区溢出的风险。切... |
| 1309 | vim-9.1.0790 | <global> | cpp/unbounded-write | 3119 | FP | TP | 代码使用`sprintf`将`transchar(from)`的结果格式化到固定缓冲区`args->os_errbuf`中，但`transchar`函数返回的字符串长度未受限制，且缓冲区大小未知，存在缓冲区溢出风险。 |
| 1314 | vim-9.1.0790 | msg_show_console_dialog | cpp/unbounded-write | 4387 | FP | TP | 代码中 `STRCPY(confirm_msg + 1, message)` 宏展开为 `strcpy`，目标缓冲区 `confirm_msg` 的大小为 `len`，而 `len` 的计算包含了 `STRLEN(message)`，... |
| 1321 | vim-9.1.0790 | nb_reply_text | cpp/unbounded-write | 802 | FP | TP | 代码使用`sprintf`将外部输入`result`和整数`cmdno`写入固定大小的缓冲区`reply`，而`reply`的大小仅基于`result`的长度分配，未考虑格式化字符串`"%d %s\n"`中整数和额外字符的固定开销，存... |
| 1336 | vim-9.1.0790 | reg_submatch | cpp/unbounded-write | 2723 | FP | TP | 代码在round==2时，使用STRCPY（即strcpy）将源字符串`s`复制到目标缓冲区`retval`，而`s`来自`reg_getline_submatch`函数，其内容不受控。目标缓冲区`retval`由`alloc(len... |
| 1337 | vim-9.1.0790 | reg_submatch | cpp/unbounded-write | 2732 | FP | TP | 代码在循环中使用STRCPY（即strcpy）将reg_getline_submatch返回的字符串复制到固定大小的缓冲区retval中，而retval的大小仅由len确定，但len的计算依赖于外部数据（匹配位置），无法保证源字符串长... |
| 1347 | vim-9.1.0790 | ExpandPackAddDir | cpp/unbounded-write | 1226 | FP | TP | 代码使用`sprintf`将外部输入`pat`拼接到固定格式字符串中，目标缓冲区`s`的大小为`pat_len + 26`，但格式字符串`"pack/*/opt/%s*"`本身包含固定字符，加上`pat`的长度后可能超过`s`的大小，... |
| 1354 | vim-9.1.0790 | spell_load_lang | cpp/unbounded-write | 1632 | FP | TP | 代码使用STRCPY（即strcpy）将参数lang直接复制到固定大小的数组sl.sl_lang中，但切片中未显示sl.sl_lang的大小定义，也未对lang的长度进行任何校验，存在缓冲区溢出风险。 |
| 1370 | vim-9.1.0790 | findtags_add_match | cpp/unbounded-write | 2702 | FP | TP | 切片代码中多次使用 STRCPY（即 strcpy）宏，将来源未知的字符串（如 st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区 mfp 中，而 mfp 的大小由 alloc 分配，其长度计算... |
| 1499 | redis-7.4.2 | auxHumanNodenameSetter | Dereference of null pointer | 233 | FP | TP | 在 `if (n)` 为 false 的分支中，代码直接解引用了空指针 `n` 来访问 `n->human_nodename`，这是一个明确的空指针解引用逻辑错误。 |
| 1541 | redis-7.2.1 | auxHumanNodenameSetter | Dereference of null pointer | 267 | FP | TP | 当指针 n 为 NULL 时，代码在 else if 条件中直接解引用 n->human_nodename 作为参数传递给 sdslen 函数，这构成了对空指针的明确解引用，存在逻辑错误和崩溃风险。 |
| 1630 | redis-8.0.2 | auxHumanNodenameSetter | Dereference of null pointer | 234 | FP | TP | 当指针 n 为 NULL 时，代码进入 `else if (sdslen(n->human_nodename) != 0)` 分支，此时对 `n->human_nodename` 的解引用（作为参数传递给 sdslen）会导致空指针解... |
| 1750 | ffmpeg-7.0.1 | try_push_frame | Dereference of null pointer | 241 | FP | TP | 代码在访问 `inbuf[0]->pts` 前，未检查 `inbuf[0]` 是否为 NULL。`inbuf` 数组初始化为 NULL，且 `ff_inlink_consume_samples` 的返回值可能为 0，此时 `inbuf... |
| 1852 | ffmpeg-6.1.1 | ebml_read_uint | Dereference of null pointer | 994 | FP | TP | 在 `size == 0` 的分支中，`num` 指针被解引用赋值，但调用方可能传入空指针，且切片代码中未显示对 `num` 进行空值检查，存在解引用空指针的逻辑错误风险。 |
| 2266 | git-2.50.1 | clar__fail | Dereference of null pointer | 698 | FP | TP | 切片代码显示直接对指针 `error` 进行解引用（`error->file = file;`），但未提供 `error` 指针的初始化或空值检查，存在解引用空指针的风险。 |

### 5.5 Unknown：算法=TP，LLM=Unknown（共 11 条）

> 算法判定为 TP，LLM 无法判定。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 410 | git-2.46.0 | <global> | cpp/overflow-buffer | 37 | TP | Unknown | 切片代码仅包含空函数定义，完全缺失与数组索引操作相关的任何代码上下文，无法判断告警所描述的访问负索引-1的情况是否存在。 |
| 411 | git-2.46.0 | <global> | cpp/overflow-buffer | 38 | TP | Unknown | 切片代码仅包含空函数定义，完全缺失与数组索引操作相关的任何代码上下文，无法判断告警所描述的负索引访问是否真实存在。 |
| 412 | git-2.46.0 | <global> | cpp/overflow-buffer | 39 | TP | Unknown | 切片代码仅包含空函数定义，完全缺失与数组索引操作相关的任何代码上下文，无法判断告警所描述的负索引访问是否真实存在。 |
| 690 | vim-9.1.1591 | is_duplicate_variable | cpp/inconsistent-null-check | 1044 | TP | Unknown | 提供的切片代码仅包含函数签名和空函数体，缺少对 `vim_strnsave` 函数调用的具体代码，无法判断其返回值是否被检查或使用，因此无法评估告警的真实性。 |
| 1426 | redis-7.0.11 | rb_gen | Dereference of null pointer | 273 | TP | Unknown | 切片代码仅包含宏调用和类型定义，未展示任何指针变量的赋值、传递或解引用操作，无法判断是否存在空指针解引用逻辑。 |
| 1431 | redis-7.0.11 | <global> | Dereference of null pointer | 307 | TP | Unknown | 提供的切片代码 `prof_tdata_comp)` 仅为片段，无法识别其所属的完整语句或上下文，缺少判断空指针解引用所必需的关键变量定义、赋值或控制流信息。 |
| 1434 | redis-7.0.11 | <global> | Dereference of null pointer | 288 | TP | Unknown | 提供的切片代码 `prof_gctx_comp)` 仅为片段，无法构成有效的代码上下文，缺少判断空指针解引用所必需的关键变量定义、赋值或控制流信息。 |
| 1598 | redis-8.0.2 | rb_gen | Dereference of null pointer | 88 | TP | Unknown | 提供的切片代码仅为宏或函数调用声明，未包含任何实际的数据流或控制流逻辑，无法判断是否存在空指针解引用。 |
| 1602 | redis-8.0.2 | <global> | Dereference of null pointer | 122 | TP | Unknown | 提供的切片代码 `prof_tdata_comp)` 仅为片段，无法识别任何变量、赋值、控制流或函数调用逻辑，缺少判断空指针解引用所必需的核心代码上下文。 |
| 1606 | redis-8.0.2 | <global> | Dereference of null pointer | 103 | TP | Unknown | 提供的切片代码 `prof_gctx_comp)` 仅为片段，无法构成有效语句，缺少判断空指针解引用所必需的关键变量定义、赋值及使用上下文。 |
| 1622 | redis-8.0.2 | strbuf_ensure_null | Dereference of null pointer | 134 | TP | Unknown | 切片代码仅包含函数定义和告警行，缺少对关键参数 `s` 及其成员 `buf` 和 `length` 的来源、赋值或有效性检查的任何信息，无法判断 `s` 是否为 NULL 或 `buf` 是否已分配足够内存，因此无法确定是否存在空指针... |

### 5.6 Unknown：算法=FP，LLM=Unknown（共 38 条）

> 算法判定为 FP，LLM 无法判定。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 498 | vim-9.1.0550 | is_duplicate_variable | cpp/inconsistent-null-check | 909 | FP | Unknown | 提供的切片代码仅为函数签名和空函数体，缺少对 `vim_strnsave` 函数调用的具体实现和上下文，无法判断其返回值是否被检查以及是否存在空指针解引用风险。 |
| 863 | vim-9.1.1040 | is_duplicate_variable | cpp/inconsistent-null-check | 991 | FP | Unknown | 提供的切片代码仅为函数签名和空函数体，缺少对 `vim_strnsave` 函数调用的具体代码，无法判断其返回值是否被检查以及告警是否成立。 |
| 1022 | vim-9.1.1040 | set_ufunc_name | cpp/unbounded-write | 664 | FP | Unknown | 切片代码中未提供关键信息：`fp->uf_name` 缓冲区的大小以及 `name` 参数的长度或来源，无法判断 `strcpy` 操作是否会导致缓冲区溢出。 |
| 1048 | vim-9.1.1330 | is_duplicate_variable | cpp/inconsistent-null-check | 1011 | FP | Unknown | 提供的切片代码仅包含函数签名和空函数体，完全缺失对 `vim_strnsave` 函数的调用以及其返回值的处理逻辑，无法判断是否存在空指针检查或评估告警的有效性。 |
| 1215 | vim-9.1.0790 | is_duplicate_variable | cpp/inconsistent-null-check | 909 | FP | Unknown | 提供的切片代码仅包含函数签名和空函数体，缺少对 `vim_strnsave` 函数调用的具体代码，无法判断其返回值是否被检查或使用，因此无法评估告警的有效性。 |
| 1464 | redis-7.4.2 | rb_gen | Dereference of null pointer | 88 | FP | Unknown | 切片代码仅包含宏调用，未展示任何指针操作或变量赋值的具体逻辑，无法判断是否存在空指针解引用。 |
| 1469 | redis-7.4.2 | <global> | Dereference of null pointer | 122 | FP | Unknown | 提供的切片代码仅为字符串 'prof_tdata_comp)\n'，完全缺失与空指针解引用相关的变量定义、赋值或使用上下文，无法进行任何有意义的分析。 |
| 1474 | redis-7.4.2 | <global> | Dereference of null pointer | 103 | FP | Unknown | 提供的切片代码仅为字符串 'prof_gctx_comp)\n'，完全缺失与空指针解引用相关的变量定义、赋值或控制流等关键上下文，无法进行任何有意义的分析。 |
| 1507 | redis-7.2.1 | rb_gen | Dereference of null pointer | 88 | FP | Unknown | 切片代码仅包含宏调用，未展示任何具体的指针操作或赋值逻辑，无法判断是否存在空指针解引用。缺少做出判断所必需的核心代码上下文。 |
| 1511 | redis-7.2.1 | <global> | Dereference of null pointer | 122 | FP | Unknown | 提供的切片代码 `prof_tdata_comp)` 仅为片段，无法识别其所属的完整语句、上下文或关键变量的来源，缺少判断空指针解引用所必需的数据流和控制流信息。 |
| 1516 | redis-7.2.1 | <global> | Dereference of null pointer | 103 | FP | Unknown | 提供的切片代码仅为字符串 'prof_gctx_comp)\n'，完全缺失与空指针解引用相关的变量定义、赋值或使用等关键上下文，无法进行任何有意义的分析。 |
| 1549 | redis-7.2.5 | rb_gen | Dereference of null pointer | 88 | FP | Unknown | 提供的切片代码仅为宏调用，未展示任何指针操作或变量赋值的具体逻辑，无法判断是否存在空指针解引用。缺少做出判断所必需的核心代码上下文。 |
| 1553 | redis-7.2.5 | <global> | Dereference of null pointer | 122 | FP | Unknown | 提供的切片代码仅为字符串 'prof_tdata_comp)\n'，完全缺失与空指针解引用相关的变量定义、赋值或使用等关键上下文，无法进行任何有意义的分析。 |
| 1558 | redis-7.2.5 | <global> | Dereference of null pointer | 103 | FP | Unknown | 提供的切片代码仅为字符串 'prof_gctx_comp)\n'，完全缺失与空指针解引用相关的变量定义、赋值或控制流等关键上下文，无法进行任何有意义的分析。 |
| 1629 | redis-8.0.2 | connClose | Dereference of null pointer | 235 | FP | Unknown | 切片代码仅展示了函数调用 `conn->type->close(conn)`，但未提供 `conn` 或 `conn->type` 是否为空的任何前置检查或赋值信息，无法判断空指针解引用是否必然发生。 |
| 1631 | ffmpeg-7.1.1 | show_bits | Dereference of null pointer | 376 | FP | Unknown | 切片代码仅展示了宏展开，未提供 `GetBitContext *s` 指针的来源、初始化或空值检查，无法判断在调用 `UPDATE_CACHE` 时 `s` 是否可能为空。 |
| 1640 | ffmpeg-7.1.1 | unsharp_slice_16 | Dereference of null pointer | 172 | FP | Unknown | 切片代码仅包含宏定义和部分函数体，告警点位于宏展开后的函数定义行，但切片中未提供调用该函数的上下文，无法判断传入的 `arg` 或 `ctx` 等关键参数是否可能为空，因此无法确定空指针解引用是否会发生。 |
| 1643 | ffmpeg-7.1.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | Unknown | 切片代码中，告警行 `bit_buf = s->bit_buf;` 引用的指针 `s` 的来源和有效性完全缺失，无法判断其是否可能为 NULL，因此无法确定是否存在空指针解引用。 |
| 1673 | ffmpeg-7.1.1 | ogg_write_header | Dereference of null pointer | 629 | FP | Unknown | 切片代码仅显示对结构体成员 `page.start_granule` 的赋值，未提供 `oggstream` 指针的来源或初始化信息，无法判断其是否为 NULL，缺少做出判断所必需的核心上下文。 |
| 1701 | ffmpeg-7.1.1 | unsharp_slice_8 | Dereference of null pointer | 173 | FP | Unknown | 切片代码仅展示了宏定义和函数框架，未包含触发空指针解引用的具体执行路径或变量赋值，无法判断在何种条件下会解引用空指针。 |
| 1705 | ffmpeg-7.1.1 | get_bits_le | Dereference of null pointer | 361 | FP | Unknown | 切片代码仅展示了宏展开，未提供 `GetBitContext *s` 参数的具体来源、初始化状态或调用上下文，无法判断其是否可能为空指针。 |
| 1725 | ffmpeg-7.0.1 | show_bits | Dereference of null pointer | 376 | FP | Unknown | 切片代码仅展示了宏展开后的形式，未提供 `UPDATE_CACHE_LE` 宏或 `GetBitContext *s` 指针的具体定义和初始化路径，无法判断指针 `s` 是否可能为空，缺少做出判断所必需的核心信息。 |
| 1733 | ffmpeg-7.0.1 | unsharp_slice_16 | Dereference of null pointer | 141 | FP | Unknown | 切片代码仅展示了宏定义和函数框架，未包含对指针 `sc` 或 `sr` 进行解引用的具体代码行，无法判断空指针解引用是否实际发生。 |
| 1771 | ffmpeg-7.0.1 | ogg_write_header | Dereference of null pointer | 628 | FP | Unknown | 切片代码仅显示对结构体成员 `page.start_granule` 的赋值，未提供 `oggstream` 指针的定义、初始化或空值检查上下文，无法判断其是否为 null，因此无法确定是否存在空指针解引用。 |
| 1793 | ffmpeg-7.0.1 | vectorscope8 | Dereference of null pointer | 775 | FP | Unknown | 切片代码中缺少对关键指针 `dpd` 和 `dp1`、`dp2` 的定义、赋值或来源说明，无法判断 `dpd[pos]` 是否可能为空，因此无法确定空指针解引用是否会发生。 |
| 1799 | ffmpeg-7.0.1 | get_bits_le | Dereference of null pointer | 361 | FP | Unknown | 切片代码仅展示了宏定义和函数框架，未提供关键参数 `s`（GetBitContext *）的来源、初始化状态或调用上下文，无法判断其是否可能为NULL，因此无法确定空指针解引用是否会发生。 |
| 1817 | ffmpeg-6.1.1 | show_bits | Dereference of null pointer | 376 | FP | Unknown | 切片代码仅包含宏定义和函数框架，未提供 `GetBitContext *s` 指针的来源、初始化或空值检查信息，无法判断在调用 `UPDATE_CACHE(re, s)` 时 `s` 是否可能为空。 |
| 1859 | ffmpeg-6.1.1 | ogg_write_header | Dereference of null pointer | 628 | FP | Unknown | 切片代码中变量 `oggstream` 的来源和初始化状态完全缺失，无法判断其是否为 null，因此无法确定解引用是否安全。 |
| 1890 | ffmpeg-6.1.1 | get_bits_le | Dereference of null pointer | 361 | FP | Unknown | 切片代码仅展示了宏定义和函数框架，缺少对关键参数 `s`（GetBitContext *）是否为空的任何检查或赋值信息，无法判断其是否可能为空指针。 |
| 1908 | ffmpeg-7.1 | show_bits | Dereference of null pointer | 376 | FP | Unknown | 切片代码仅展示了宏定义和函数框架，缺少对关键参数 `s`（GetBitContext *）是否为空的判断逻辑。无法从提供的切片中追踪 `s` 的来源或验证其非空性，因此无法确定空指针解引用是否会发生。 |
| 1930 | ffmpeg-7.1 | get_sbits | Dereference of null pointer | 325 | FP | Unknown | 切片代码仅展示了宏展开后的函数框架，缺少对关键参数 `s`（GetBitContext *）是否为空的任何检查或赋值信息，无法判断其来源和有效性，因此无法评估空指针解引用风险。 |
| 1951 | ffmpeg-7.1 | ogg_write_header | Dereference of null pointer | 629 | FP | Unknown | 切片代码仅显示对结构体成员 `page.start_granule` 的赋值，未提供 `oggstream` 指针的定义、初始化或空值检查上下文，无法判断该指针在解引用前是否为空。 |
| 1983 | ffmpeg-7.1 | get_bits_le | Dereference of null pointer | 361 | FP | Unknown | 切片代码仅展示了宏定义和函数框架，未提供 `GetBitContext *s` 参数的具体来源、初始化状态或调用上下文，无法判断其是否可能为 NULL，因此无法评估空指针解引用风险。 |
| 2039 | ffmpeg-6.0 | ogg_write_header | Dereference of null pointer | 628 | FP | Unknown | 切片代码仅显示对结构体成员 `page.start_granule` 的赋值，未提供 `oggstream` 指针的定义、初始化或空值检查上下文，无法判断该指针在解引用时是否可能为 null。 |
| 2165 | git-2.49.0 | <global> | Dereference of null pointer | 30 | FP | Unknown | 切片代码仅包含函数声明和空函数体，未提供任何关于指针解引用或变量赋值的实际代码逻辑，无法判断是否存在空指针解引用问题。 |
| 2287 | git-2.50.1 | <global> | Dereference of null pointer | 30 | FP | Unknown | 切片代码仅包含函数签名和空函数体，无法判断是否存在空指针解引用或相关数据流，缺少做出判断所必需的核心代码逻辑。 |
| 2344 | git-2.47.1 | image_remove_first_line | Dereference of null pointer | 354 | FP | Unknown | 切片代码中未提供 `img` 指针的来源、初始化状态或调用 `image_remove_first_line` 前的任何检查，无法判断 `img` 或 `img->line` 是否为 NULL，因此无法确定是否存在空指针解引用。 |
| 2389 | musl-1.2.4 | load_direct_deps | Dereference of null pointer | 1280 | FP | Unknown | 切片代码中，变量 `cnt` 在 `p->deps[cnt++] = q;` 这一告警行之前的赋值逻辑不完整且存在矛盾（例如在条件 `p==head` 下 `cnt` 可能未初始化），无法确定其初始值或是否会导致对空指针 `p->de... |

## 6. 按 (tool_name, project_name_without_version, rule_id) 联合分组统计

> 共 **43** 种不同组合（种类），按条目数降序排列。

| # | tool_name | project_name_without_version | rule_id | 总计 | TP | FP | Unknown |
|---|---|---|---|---|---|---|---|
| 1 | codeql | vim | cpp/unbounded-write | 753 | 202 | 550 | 1 |
| 2 | csa | ffmpeg | Dereference of null pointer | 445 | 2 | 424 | 19 |
| 3 | csa | git | Dereference of null pointer | 293 | 1 | 289 | 3 |
| 4 | csa | redis | Dereference of null pointer | 210 | 4 | 189 | 17 |
| 5 | codeql | git | cpp/inconsistent-null-check | 129 | 2 | 127 | 0 |
| 6 | csa | musl | Dereference of null pointer | 98 | 0 | 97 | 1 |
| 7 | codeql | vim | cpp/inconsistent-null-check | 87 | 4 | 78 | 5 |
| 8 | codeql | git | cpp/overflow-buffer | 50 | 0 | 47 | 3 |
| 9 | codeql | openssl-openssl | cpp/unterminated-variadic-call | 45 | 0 | 45 | 0 |
| 10 | csa | tmux | Dereference of null pointer | 44 | 0 | 44 | 0 |
| 11 | codeql | openssl-openssl | cpp/use-after-free | 40 | 0 | 40 | 0 |
| 12 | codeql | ffmpeg | cpp/inconsistent-null-check | 35 | 2 | 33 | 0 |
| 13 | codeql | ffmpeg | cpp/offset-use-before-range-check | 33 | 0 | 33 | 0 |
| 14 | codeql | openssl-openssl | cpp/invalid-pointer-deref | 25 | 0 | 25 | 0 |
| 15 | codeql | openssl-openssl | cpp/unbounded-write | 24 | 0 | 24 | 0 |
| 16 | codeql | vim | cpp/overrunning-write | 21 | 20 | 1 | 0 |
| 17 | codeql | vim | cpp/unsafe-strcat | 21 | 2 | 19 | 0 |
| 18 | codeql | git | cpp/offset-use-before-range-check | 20 | 0 | 20 | 0 |
| 19 | codeql | musl | cpp/unbounded-write | 20 | 0 | 20 | 0 |
| 20 | codeql | openssl-openssl | cpp/inconsistent-null-check | 19 | 0 | 19 | 0 |
| 21 | codeql | git | cpp/invalid-pointer-deref | 15 | 2 | 13 | 0 |
| 22 | codeql | vim | cpp/invalid-pointer-deref | 10 | 2 | 8 | 0 |
| 23 | codeql | vim | cpp/redundant-null-check-simple | 10 | 0 | 10 | 0 |
| 24 | codeql | openssl-openssl | cpp/offset-use-before-range-check | 8 | 0 | 8 | 0 |
| 25 | codeql | ffmpeg | cpp/unbounded-write | 5 | 0 | 5 | 0 |
| 26 | codeql | git | cpp/no-space-for-terminator | 5 | 0 | 5 | 0 |
| 27 | codeql | musl | cpp/suspicious-allocation-size | 5 | 0 | 5 | 0 |
| 28 | codeql | musl | cpp/unsafe-strcat | 5 | 0 | 5 | 0 |
| 29 | codeql | nginx | cpp/inconsistent-null-check | 5 | 0 | 5 | 0 |
| 30 | codeql | openssl-openssl | cpp/unsafe-strcat | 5 | 0 | 5 | 0 |
| 31 | codeql | vim | cpp/offset-use-before-range-check | 5 | 0 | 5 | 0 |
| 32 | codeql | git | cpp/redundant-null-check-simple | 4 | 0 | 4 | 0 |
| 33 | codeql | openssl-openssl | cpp/redundant-null-check-simple | 3 | 0 | 3 | 0 |
| 34 | codeql | ffmpeg | cpp/overflow-buffer | 2 | 0 | 2 | 0 |
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

*报告由 `analyze_results.py` 自动生成，生成时间：2026-03-05 23:16:20*
