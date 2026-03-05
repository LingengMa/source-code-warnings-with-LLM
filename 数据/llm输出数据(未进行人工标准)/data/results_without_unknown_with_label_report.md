# LLM 分类结果分析报告

- **分析文件**：`results_without_unknown_with_label.json`
- **完整路径**：`/home/lg/Documents/projects/毕设/大仓/匹配/llm-match/output/results_without_unknown_with_label.json`
- **生成时间**：2026-03-05 23:16:29

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
| 判定一致数 | 2399 |
| 判定不一致数 | 111 |

## 2. 算法标注（label）分布

| label | 数量 | 占比 |
|---|---|---|
| TP | 218 | 8.7% |
| FP | 2292 | 91.3% |

## 3. label × llm_label 交叉矩阵

| label \ llm_label | TP | FP | Unknown | **合计** |
|---|---|---|---|---|
| **TP** | 119 | 99 | 0 | **218** |
| **FP** | 12 | 2280 | 0 | **2292** |
| **合计** | 131 | 2379 | 0 | **2510** |

## 4. 汇总指标

> 以下指标仅基于**已判定（非 Unknown）**条目计算。

| 指标 | 数值 |
|---|---|
| 准确率（Accuracy） | 95.6% |
| 精确率（Precision，以 TP 为正类） | 90.8% |
| 召回率（Recall，以 TP 为正类） | 54.6% |
| F1 分数（以 TP 为正类） | 68.2% |

## 5. 各分类条目详情

### 5.1 一致：算法=TP，LLM=TP（共 119 条）

> 算法与 LLM 均判定为真阳性（True Positive）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 678 | vim-9.1.1591 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | TP | TP | 函数 `getcell` 可能返回 NULL，但调用后未进行空指针检查就直接解引用 `cell->chars[0]`，存在空指针解引用风险。算法标签 `TP` 与此分析一致。 |
| 680 | vim-9.1.1591 | get_isolated_shell_name | cpp/inconsistent-null-check | 2754 | TP | TP | 函数 `vim_strnsave` 的返回值 `p` 被直接返回给调用者，切片代码中未对 `p` 进行空指针检查。由于 `vim_strnsave` 在内存分配失败时会返回 NULL，这可能导致调用者使用空指针，存在潜在风险。 |
| 697 | vim-9.1.1591 | prt_line_number | cpp/overrunning-write | 387 | TP | TP | sprintf 使用格式字符串 "%6ld" 写入最多6位数字加一个符号位，共7个字符，但目标缓冲区 tbuf 仅20字节，足够容纳。然而，告警指出需要21字节，可能考虑了字符串终止符 '\0' 导致溢出。切片中未见对 lnum 的范... |
| 698 | vim-9.1.1591 | highlight_color | cpp/overrunning-write | 3278 | TP | TP | sprintf 目标缓冲区 `buf` 大小为 10 字节，但格式化字符串 "#%02x%02x%02x" 加上终止符需要至少 8 个字符（# + 6 个十六进制数字 + '\0'），计算为 8 字节，看似安全。然而，规则告警提示需要... |
| 699 | vim-9.1.1591 | msg_outnum | cpp/overrunning-write | 1651 | TP | TP | 目标缓冲区 `buf` 大小为20字节，但 `sprintf` 格式化长整型 `%ld` 最多可能写入21字节（包括负号和终止空字符），存在缓冲区溢出风险，切片中未见任何防护措施。 |
| 701 | vim-9.1.1591 | ga_concat_strings | cpp/unbounded-write | 788 | TP | TP | 代码使用宏STRCPY（即strcpy）将动态长度的字符串复制到固定大小的缓冲区中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何边界检查或安全复制机制。 |
| 702 | vim-9.1.1591 | maketitle | cpp/unbounded-write | 4239 | TP | TP | 代码使用 STRCPY（即 strcpy）将 `name` 复制到固定大小的缓冲区 `buf` 中，而 `name` 是从 `gettail` 或 `buf_spname` 获取的路径尾部，其长度未经验证，存在缓冲区溢出风险。切片中未... |
| 703 | vim-9.1.1591 | buf_write | cpp/unbounded-write | 1208 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将fname复制到固定大小的IObuff缓冲区，未检查fname长度是否超过IObuff大小，存在缓冲区溢出风险。切片中未见任何长度校验或安全防护。 |
| 705 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2150 | TP | TP | 代码中直接使用宏 `STRCAT(d, s)`（即 `strcat`）将 `p_extra` 的内容拼接到 `leader` 缓冲区末尾，而 `leader` 缓冲区的大小是动态计算的 `lead_len + lead_repl_le... |
| 706 | vim-9.1.1591 | transstr | cpp/unbounded-write | 400 | TP | TP | 切片代码显示，`res` 缓冲区通过 `alloc(len + 1)` 分配，其大小 `len` 是计算出的字符显示宽度，而非字节长度。随后循环中使用 `STRCAT(res, transchar_byte(*p++))` 拼接字符串... |
| 707 | vim-9.1.1591 | globpath | cpp/unbounded-write | 4180 | TP | TP | 代码使用STRCPY（即strcpy）将外部输入`file`复制到固定大小的缓冲区`buf`中，虽然存在`pathlen + seplen + filelen + 1 <= MAXPATHL`的长度检查，但`filelen`是基于`f... |
| 708 | vim-9.1.1591 | expand_shellcmd | cpp/unbounded-write | 3902 | TP | TP | 代码在拼接路径时使用STRCPY（即strcpy）将pat复制到buf+pathlen处，未检查目标缓冲区buf的剩余空间是否足够容纳源字符串pat，存在缓冲区溢出风险。切片中未见对pat长度的前置校验，且算法标签为TP，倾向于判定为... |
| 709 | vim-9.1.1591 | win_redr_status_matches | cpp/unbounded-write | 698 | TP | TP | 代码使用STRCPY（即strcpy）宏将字符串复制到固定大小的缓冲区buf中，而源字符串s来自外部输入（如环境变量、文件读取等），其长度未经验证，存在缓冲区溢出风险。切片中未见对源字符串长度的检查或使用安全复制函数。 |
| 710 | vim-9.1.1591 | win_redr_status_matches | cpp/unbounded-write | 717 | TP | TP | 代码使用 STRCPY（即 strcpy）将 transchar_byte 函数的返回值复制到缓冲区，该返回值长度未知，而目标缓冲区大小固定（Columns+1 或 Columns*MB_MAXBYTES+1），存在缓冲区溢出风险。切... |
| 711 | vim-9.1.1591 | debuggy_find | cpp/unbounded-write | 1067 | TP | TP | 代码使用STRCPY宏（即strcpy）将fname+3复制到name+5，未检查目标缓冲区大小，而name的大小仅基于STRLEN(fname)+3分配，存在缓冲区溢出风险。 |
| 712 | vim-9.1.1591 | has_profiling | cpp/unbounded-write | 973 | TP | TP | 代码使用STRCPY（即strcpy）将源字符串fname复制到新分配的目标缓冲区pe->pen_name，目标缓冲区大小仅为strlen(fname)+1，与源长度相同，没有额外空间。如果fname在分配后、复制前被并发修改变长，或... |
| 713 | vim-9.1.1591 | ex_diffpatch | cpp/unbounded-write | 1512 | TP | TP | 代码中多次使用不安全的 STRCPY（即 strcpy）将字符串复制到固定大小的缓冲区 buf 中，而 buf 的大小是根据多个字符串长度计算分配的，但后续的 STRCPY 操作可能写入超过 buf 分配大小的数据，存在缓冲区溢出风险。 |
| 714 | vim-9.1.1591 | do_string_sub | cpp/unbounded-write | 8057 | TP | TP | 代码在告警行使用STRCPY（即strcpy）将`tail`指向的字符串复制到动态数组`ga.ga_data`的尾部，但未检查目标缓冲区剩余空间是否足够容纳源字符串。虽然前面有`ga_grow`调用，但它仅确保数组能容纳计算出的固定长... |
| 715 | vim-9.1.1591 | set_var_const | cpp/unbounded-write | 4300 | TP | TP | 代码使用宏 STRCPY（即 strcpy）将 varname 复制到 di->di_key，而 varname 的长度可能超过 di->di_key 的分配大小（STRLEN(varname) + 1），存在缓冲区溢出风险。切片中未... |
| 716 | vim-9.1.1591 | cat_prefix_varname | cpp/unbounded-write | 2578 | TP | TP | 代码使用STRCPY（即strcpy）将外部输入`name`复制到缓冲区`varnamebuf+2`，虽然缓冲区大小`len`根据`name`的长度计算并分配，但分配后立即将`varnamebuf[1]`和`*varnamebuf`赋... |
| 718 | vim-9.1.1591 | make_filter_cmd | cpp/unbounded-write | 1854 | TP | TP | 代码在多个分支中直接使用不安全的 STRCPY（即 strcpy）宏将外部命令字符串复制到固定大小的缓冲区，未对源字符串长度进行校验，存在缓冲区溢出风险。 |
| 720 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 795 | TP | TP | 代码使用STRCPY（即strcpy）将长度不确定的字符串&s[start_col]复制到固定大小的缓冲区sortbuf1中，而sortbuf1的大小由maxlen+1分配，但&s[start_col]的长度可能超过maxlen，存在... |
| 721 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 815 | TP | TP | 代码使用STRCPY宏（即strcpy）将长度不确定的字符串&s[start_col]复制到固定大小的缓冲区sortbuf1中，而sortbuf1的大小由maxlen+1分配，但maxlen是之前遍历行计算出的最大长度，不能保证&s[... |
| 722 | vim-9.1.1591 | ex_uniq | cpp/unbounded-write | 833 | TP | TP | 代码使用STRCPY宏（即strcpy）将长度不确定的字符串`s[start_col]`复制到固定大小的缓冲区`sortbuf1`中，而`sortbuf1`的大小仅根据`maxlen`分配，无法保证源字符串长度不超过目标缓冲区大小，存... |
| 723 | vim-9.1.1591 | ex_sort | cpp/unbounded-write | 605 | TP | TP | 代码使用STRCPY宏（即strcpy）将长度未知的字符串`s`复制到固定大小的缓冲区`sortbuf1`中，而`sortbuf1`的大小仅基于`maxlen`分配，未考虑空字符或确保源字符串长度不超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 724 | vim-9.1.1591 | expand_sfile | cpp/unbounded-write | 10143 | TP | TP | 代码使用STRCPY宏（即strcpy）将可变长度的字符串`repl`复制到固定大小的缓冲区`newres`中，而`newres`的大小是根据`resultlen`计算的，但`repl`的长度可能超过目标缓冲区剩余空间，存在缓冲区溢出... |
| 725 | vim-9.1.1591 | repl_cmdline | cpp/unbounded-write | 5330 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的字符串（src + srclen）复制到固定大小的缓冲区new_cmdline中，存在缓冲区溢出风险。切片中未见对目标缓冲区大小或源字符串长度的前置检查。 |
| 726 | vim-9.1.1591 | repl_cmdline | cpp/unbounded-write | 5336 | TP | TP | 代码使用不安全的STRCPY（即strcpy）宏，将eap->nextcmd复制到目标缓冲区new_cmdline + new_cmdlinelen，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对eap->nextcmd长度的... |
| 727 | vim-9.1.1591 | replace_makeprg | cpp/unbounded-write | 5037 | TP | TP | 代码使用STRCPY宏（即strcpy）将用户控制的参数p复制到新分配的缓冲区ptr中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对p的长度进行限制或使用安全复制函数。 |
| 728 | vim-9.1.1591 | replace_makeprg | cpp/unbounded-write | 5052 | TP | TP | 代码使用STRCPY（即strcpy）宏将未经验证长度的字符串（如程序变量program和参数p）复制到固定大小的缓冲区new_cmdline中，存在缓冲区溢出风险。切片中未见对源字符串长度的限制或检查，且目标缓冲区大小仅通过allo... |
| 729 | vim-9.1.1591 | do_one_cmd | cpp/unbounded-write | 2686 | TP | TP | 代码中直接使用STRCPY宏（即strcpy）将未知长度的字符串复制到固定大小的IObuff缓冲区，存在缓冲区溢出风险。切片中未见对源字符串长度的检查或使用安全函数。 |
| 731 | vim-9.1.1591 | get_exception_string | cpp/unbounded-write | 473 | TP | TP | 代码使用`strcat`向缓冲区`val`追加内容，而`val`指向的缓冲区大小由`vim_strnsave`分配，其大小计算依赖于`STRLEN(mesg)`等变量。若`mesg`内容被外部输入（如环境变量、文件读取）控制，且长度超... |
| 732 | vim-9.1.1591 | get_exception_string | cpp/unbounded-write | 484 | TP | TP | 代码使用`sprintf`将`&mesg[1]`的内容格式化写入`val`缓冲区，而`val`指向的缓冲区大小由`vim_strnsave`分配，其大小基于`mesg`的长度计算。但`mesg[1]`可能是一个未经验证的用户输入或错误... |
| 733 | vim-9.1.1591 | escape_fname | cpp/unbounded-write | 4193 | TP | TP | 代码使用STRCPY（即strcpy）将源字符串复制到新分配的内存中，虽然目标缓冲区大小通过alloc(STRLEN(*pp) + 2)分配，但strcpy本身不检查边界，若源字符串未以空字符结尾或分配计算有误，仍可能导致缓冲区溢出。... |
| 734 | vim-9.1.1591 | cmdline_browse_history | cpp/unbounded-write | 1528 | TP | TP | 代码使用宏STRCPY（即strcpy）将历史记录字符串p复制到固定大小的缓冲区ccline.cmdbuff中，而p的长度plen可能超过alloc_cmdbuff分配的缓冲区大小，存在缓冲区溢出风险。切片中未见对plen与目标缓冲区... |
| 735 | vim-9.1.1591 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 879 | TP | TP | 代码使用不安全的 STRCPY（即 strcpy）宏将动态长度的字符串 p 复制到固定大小的缓冲区 ccline.cmdbuff 中，虽然前面调用了 realloc_cmdbuff 来确保缓冲区大小足够，但该函数内部仅当 len < ... |
| 736 | vim-9.1.1591 | vim_settempdir | cpp/unbounded-write | 5293 | TP | TP | 代码使用STRCPY（即strcpy）将参数tempdir直接复制到固定大小的缓冲区buf中，而tempdir是外部传入的路径，其长度未在切片内进行验证。缓冲区buf的大小为MAXPATHL+2，但无法保证tempdir的长度小于此值... |
| 737 | vim-9.1.1591 | vim_rename | cpp/unbounded-write | 3865 | TP | TP | 代码使用STRCPY（即strcpy）将'from'复制到固定大小的缓冲区'tempname'，虽然前面有长度检查'if (STRLEN(from) >= MAXPATHL - 5)'，但该检查仅确保'from'长度小于MAXPATH... |
| 738 | vim-9.1.1591 | buf_modname | cpp/unbounded-write | 3643 | TP | TP | 代码使用STRCPY（即strcpy）将未经验证长度的fname复制到新分配的缓冲区retval，而retval的大小仅基于fnamelen + extlen + 3计算，未对源字符串fname的长度进行限制，存在缓冲区溢出风险。切片... |
| 741 | vim-9.1.1591 | concat_fnames | cpp/unbounded-write | 3137 | TP | TP | 函数使用strcat拼接两个输入字符串，虽然为目标缓冲区分配了基于两个输入字符串长度计算的空间，但未对输入字符串fname1和fname2的长度进行验证或限制，若调用者传入的字符串长度与STRLEN计算不符（如包含空字符），仍可能导致... |
| 742 | vim-9.1.1591 | uniquefy_paths | cpp/unbounded-write | 2568 | TP | TP | 代码使用STRCPY（即strcpy）将用户提供的pattern字符串复制到新分配的缓冲区file_pattern+1位置，但file_pattern的大小仅根据pattern长度+2分配，未考虑源字符串长度可能超过目标缓冲区剩余容量... |
| 743 | vim-9.1.1591 | uniquefy_paths | cpp/unbounded-write | 2685 | TP | TP | 代码在告警行 `STRCPY(fnames[i], short_name);` 处使用 `STRCPY`（即 `strcpy`）宏，将 `short_name` 复制到 `fnames[i]` 指向的缓冲区。`short_name` ... |
| 744 | vim-9.1.1591 | find_file_in_path_option | cpp/unbounded-write | 1911 | TP | TP | 代码中直接使用 STRCPY（即 strcpy）将 *file_to_find 复制到 NameBuff，而 NameBuff 的大小为 MAXPATHL，但 *file_to_find 的长度 file_to_findlen 可能超... |
| 745 | vim-9.1.1591 | ff_check_visited | cpp/unbounded-write | 1537 | TP | TP | 代码使用STRCPY（即strcpy）将ff_expand_buffer.string复制到vp->ffv_fname，目标缓冲区大小由alloc分配，其大小为ff_expand_buffer.length + 1，而源字符串长度恰好... |
| 746 | vim-9.1.1591 | <global> | cpp/unbounded-write | 3794 | TP | TP | 代码使用 `sprintf` 和 `STRCAT`（即 `strcat`）将未经验证长度的字符串 `s` 拼接到固定大小的缓冲区 `r` 中，而 `r` 的分配大小仅通过 `STRLEN` 估算，未考虑 `s` 可能被后续 `fold... |
| 747 | vim-9.1.1591 | foldDelMarker | cpp/unbounded-write | 1897 | TP | TP | 代码使用宏STRCPY（即strcpy）将源字符串`p + len`复制到目标缓冲区`newline + (p - line)`，目标缓冲区大小`alloc(ml_get_len(lnum) - len + 1)`仅确保能容纳原始行删... |
| 748 | vim-9.1.1591 | foldAddMarker | cpp/unbounded-write | 1815 | TP | TP | 代码使用STRCPY（即strcpy）宏将`line`复制到新分配的`newline`缓冲区，而`line`是从文件内容中读取的任意长度字符串。虽然`newline`的大小已根据`line_len`、`markerlen`和`STRL... |
| 749 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2899 | TP | TP | 代码使用STRCPY宏（即strcpy）将长度未知的字符串res_prolog->title复制到固定大小的缓冲区buffer（256字节）中，存在缓冲区溢出风险。切片中未显示对res_prolog->title长度的检查或限制。 |
| 751 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2905 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_cidfont->title复制到固定大小的buffer[256]中，而title的来源是外部资源文件，其长度未在切片内进行验证，存在缓冲区溢出风险。 |
| 752 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2907 | TP | TP | 代码使用STRCAT宏（即strcat）向固定大小的缓冲区buffer追加内容，而buffer的大小为256字节。切片中未显示对res_cidfont->title和res_cidfont->version的长度有任何校验或限制，存在... |
| 753 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2912 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_cmap->title复制到固定大小的buffer[256]中，而title来自外部资源文件，其长度未经验证，存在缓冲区溢出风险。 |
| 754 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2914 | TP | TP | 代码使用STRCAT宏（即strcat）将字符串拼接到固定大小的缓冲区buffer中，而buffer的大小为256字节。告警点处拼接的源字符串（如res_cmap->title和res_cmap->version）长度未知，且切片中未... |
| 755 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2920 | TP | TP | 代码使用STRCPY宏（即strcpy）将res_encoding->title复制到固定大小的buffer[256]中，但切片内未显示对res_encoding->title长度的任何验证或限制，存在缓冲区溢出风险。 |
| 757 | vim-9.1.1591 | prt_resource_name | cpp/unbounded-write | 1659 | TP | TP | 代码使用STRCPY（即strcpy）将`filename`复制到`resource_filename`，虽然存在长度检查，但检查条件是`STRLEN(filename) >= MAXPATHL`时清空目标，否则直接复制。这未能防止`... |
| 758 | vim-9.1.1591 | do_helptags | cpp/unbounded-write | 1210 | TP | TP | 代码中直接使用STRCPY（即strcpy）将参数dirname复制到固定大小的NameBuff缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。告警规则正确识别了此不安全操作。 |
| 759 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 975 | TP | TP | 代码使用STRCAT宏（即strcat）向NameBuff缓冲区拼接未经验证长度的字符串ext和tagfname，存在缓冲区溢出风险。切片中未见对NameBuff大小（MAXPATHL）的边界检查，且label为TP，倾向于判定为真实问题。 |
| 760 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 991 | TP | TP | 代码使用STRCAT宏（即strcat）将参数tagfname拼接到NameBuff缓冲区，而NameBuff的大小（MAXPATHL）未在切片中明确验证。由于tagfname是函数参数，其长度可能超过NameBuff的剩余空间，导致... |
| 761 | vim-9.1.1591 | helptags_one | cpp/unbounded-write | 1112 | TP | TP | 代码使用 sprintf 将可变长度的字符串 p1 和 fname 写入固定大小的缓冲区 s，其中 p1 来自用户控制的帮助文件内容，fname 是文件名，缓冲区大小计算为 (p2 - p1 + STRLEN(fname) + 2)，... |
| 762 | vim-9.1.1591 | highlight_set_startstop_termcode | cpp/unbounded-write | 1488 | TP | TP | 代码在调用STRCAT（即strcat）前，虽然检查了目标缓冲区buf的当前长度与待追加字符串p的长度之和是否超过99，但buf的大小为100字节，且strcat依赖空字符定位结尾，若缓冲区已满或接近满，strcat可能写入超出边界。... |
| 763 | vim-9.1.1591 | load_colors | cpp/unbounded-write | 609 | TP | TP | sprintf 使用未经验证的用户输入 `name` 拼接字符串，目标缓冲区 `buf` 的大小仅为 `STRLEN(name) + 12`，当 `name` 长度足够长时，拼接后的字符串 'colors/%s.vim' 可能超过缓冲... |
| 771 | vim-9.1.1591 | <global> | cpp/unbounded-write | 3140 | TP | TP | 代码使用`sprintf`将变量`transchar(from)`的结果写入固定大小的缓冲区`args->os_errbuf`，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对`transchar`返回字符串长度的限制或对目标缓... |
| 774 | vim-9.1.1591 | <global> | cpp/unbounded-write | 811 | TP | TP | 代码中直接使用宏 STRCPY（即 strcpy）将 call_data 复制到新分配的缓冲区，未检查源字符串长度是否超过目标缓冲区大小。分配的缓冲区大小为 STRLEN(call_data) + 5，但若 call_data 在复制... |
| 775 | vim-9.1.1591 | <global> | cpp/unbounded-write | 815 | TP | TP | 代码中多处使用宏 STRCPY（即 strcpy）将长度未知的源字符串（如 call_data、tearpath 等）复制到固定大小的目标缓冲区，且切片中未见对源字符串长度的检查或使用安全函数（如 strncpy），存在缓冲区溢出风险。 |
| 776 | vim-9.1.1591 | msg_show_console_dialog | cpp/unbounded-write | 4505 | TP | TP | 代码使用宏STRCPY（即strcpy）将message字符串复制到confirm_msg缓冲区，而confirm_msg的大小len由STRLEN(message)等计算得出，但复制目标confirm_msg + 1的偏移计算可能导... |
| 778 | vim-9.1.1591 | get_emsg_source | cpp/unbounded-write | 500 | TP | TP | 代码使用`sprintf`将可变字符串`sname`格式化到固定大小的缓冲区`Buf`中，缓冲区大小由`STRLEN(sname) + STRLEN(p)`计算，但`sprintf`的格式字符串`p`包含一个`%s`占位符，这使得写入... |
| 780 | vim-9.1.1591 | expand_env_esc | cpp/unbounded-write | 1678 | TP | TP | 代码在调用STRCPY（即strcpy）前，仅通过比较源字符串长度与目标缓冲区剩余空间（dstlen）来判断是否安全，但未考虑目标缓冲区dst的原始大小，存在缓冲区溢出风险。算法标签TP与此判断一致。 |
| 783 | vim-9.1.1591 | push_showcmd | cpp/unbounded-write | 1809 | TP | TP | 代码使用宏STRCPY（即strcpy）将showcmd_buf复制到old_showcmd_buf，未对源缓冲区showcmd_buf的大小进行任何检查。strcpy函数在源缓冲区大小未知或超过目标缓冲区大小时会导致缓冲区溢出，切片... |
| 785 | vim-9.1.1591 | op_change | cpp/unbounded-write | 2003 | TP | TP | 代码中直接使用 STRCPY 宏（即 strcpy）将源字符串 oldp + bd.textcol 复制到目标缓冲区 newp + newlen + ins_len，未检查目标缓冲区大小，存在缓冲区溢出风险。 |
| 786 | vim-9.1.1591 | op_replace | cpp/unbounded-write | 1299 | TP | TP | 代码中直接使用不安全的STRCPY（即strcpy）宏，将源字符串复制到目标缓冲区，未检查目标缓冲区大小。切片中未显示对源字符串长度的限制或对目标缓冲区的边界检查，存在缓冲区溢出风险。 |
| 787 | vim-9.1.1591 | op_replace | cpp/unbounded-write | 1308 | TP | TP | 代码中直接使用 STRCPY（即 strcpy）宏将未知长度的源字符串复制到固定大小的目标缓冲区，且切片中未见任何对源字符串长度的检查或限制，存在缓冲区溢出风险。 |
| 788 | vim-9.1.1591 | op_delete | cpp/unbounded-write | 962 | TP | TP | 代码中直接使用不安全的STRCPY（即strcpy）宏，将源字符串`oldp + bd.textcol + bd.textlen`复制到目标缓冲区`newp + bd.textcol + bd.startspaces + bd.end... |
| 789 | vim-9.1.1591 | block_insert | cpp/unbounded-write | 743 | TP | TP | 代码使用STRCPY（即strcpy）将字符串oldp复制到newp + offset处，未检查目标缓冲区newp的大小，而newp是通过alloc动态分配的，其大小由ml_get_len(lnum) + spaces + slen ... |
| 791 | vim-9.1.1591 | option_value2string | cpp/unbounded-write | 8461 | TP | TP | 代码在多个分支中直接使用不安全的STRCPY（即strcpy）宏将数据复制到固定大小的NameBuff缓冲区，未检查源字符串长度，存在缓冲区溢出风险。切片中未见对源数据长度的限制或验证。 |
| 792 | vim-9.1.1591 | stropt_expand_envvar | cpp/unbounded-write | 1803 | TP | TP | 代码使用STRCPY（即strcpy）将源字符串`s`复制到新分配的目标缓冲区`newval`中，但未检查源字符串长度是否超过目标缓冲区大小。虽然`newlen`是根据`s`的长度计算并分配的，但`s`来自`option_expand... |
| 793 | vim-9.1.1591 | mch_expand_wildcards | cpp/unbounded-write | 7445 | TP | TP | 代码在行 `STRCPY(p, (*file)[i]);` 处使用宏 `STRCPY`（即 `strcpy`）复制字符串，目标缓冲区 `p` 的大小为 `STRLEN((*file)[i]) + 1 + dir`，而源字符串 `(*f... |
| 794 | vim-9.1.1591 | mch_FullName | cpp/unbounded-write | 2846 | TP | TP | 代码在告警行使用STRCPY（即strcpy）将fname复制到buf+buflen位置，虽然前面有长度检查`(int)(buflen + STRLEN(fname)) >= len`，但该检查仅在retval为FAIL或长度不足时提... |
| 796 | vim-9.1.1591 | reg_submatch | cpp/unbounded-write | 2723 | TP | TP | 代码在循环中使用STRCPY（即strcpy）将未知长度的字符串`s`复制到固定大小的缓冲区`retval`中，而`retval`的大小`len`是在复制过程中动态计算的，存在写入时目标缓冲区大小可能不足的风险，符合无界写入漏洞特征。 |
| 797 | vim-9.1.1591 | reg_submatch | cpp/unbounded-write | 2732 | TP | TP | 代码在多个位置使用STRCPY（即strcpy）宏，将长度未知的源字符串（如从reg_getline_submatch获取的行内容）复制到固定大小的缓冲区retval中，而retval的大小仅由alloc(len)分配，但复制操作前未... |
| 798 | vim-9.1.1591 | regtilde | cpp/unbounded-write | 1959 | TP | TP | STRCPY宏直接展开为strcpy，目标缓冲区tmpsub的大小为tmpsublen+1，源字符串postfix的长度未在切片中验证，存在缓冲区溢出的风险。算法标签TP与此判断一致。 |
| 799 | vim-9.1.1591 | match_with_backref | cpp/unbounded-write | 1600 | TP | TP | 代码使用STRCPY（即strcpy）将长度未知的rex.line复制到固定大小的缓冲区reg_tofree中，虽然reg_tofree的大小会根据rex.line的长度动态分配，但分配后若rex.line内容被外部修改（如环境变量、... |
| 800 | vim-9.1.1591 | get_reg_contents | cpp/unbounded-write | 2743 | TP | TP | 代码使用宏 STRCPY（即 strcpy）将 y_current->y_array[i].string 复制到目标缓冲区 retval + len，未检查源字符串长度是否超过目标缓冲区剩余空间。目标缓冲区 retval 的大小由 a... |
| 801 | vim-9.1.1591 | do_put | cpp/unbounded-write | 2166 | TP | TP | 代码中直接使用 STRCPY 宏（即 strcpy）将 y_array[y_size - 1].string 复制到固定大小的缓冲区 newp，未检查源字符串长度是否超过目标缓冲区大小，存在缓冲区溢出风险。 |
| 802 | vim-9.1.1591 | do_put | cpp/unbounded-write | 2167 | TP | TP | 代码中直接使用 STRCPY 宏（即 strcpy）将 y_array[i].string 复制到缓冲区，未检查目标缓冲区大小，存在缓冲区溢出风险。告警消息指出输入可能来自环境变量、文件读取等外部源，切片中未见长度校验或安全复制机制。 |
| 803 | vim-9.1.1591 | op_yank | cpp/unbounded-write | 1318 | TP | TP | 代码使用STRCPY宏（即strcpy）拼接两个字符串，目标缓冲区pnew的大小是两者长度之和加1，但strcpy不检查边界，若源字符串未正确以空字符结尾，可能导致缓冲区溢出。切片中未见对源字符串内容的边界或终止符验证。 |
| 804 | vim-9.1.1591 | op_yank | cpp/unbounded-write | 1319 | TP | TP | 代码使用STRCPY宏（即strcpy）拼接两个字符串，目标缓冲区pnew的大小是两者长度之和加1，但strcpy不检查边界，若源字符串长度计算错误或未以空字符结尾，可能导致缓冲区溢出。切片中未见边界检查或使用安全函数。 |
| 805 | vim-9.1.1591 | stuff_yank | cpp/unbounded-write | 471 | TP | TP | 代码使用STRCPY（即strcpy）宏将源字符串复制到目标缓冲区，目标缓冲区大小由tmplen+1分配，但源字符串pp->string的长度未知，可能超过分配的大小，存在缓冲区溢出风险。切片中未见对源字符串长度的校验。 |
| 806 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2850 | TP | TP | 代码使用`strcat`向固定大小的缓冲区`scriptname`追加内容，而`name`参数长度未经验证，可能导致缓冲区溢出。切片中未见对`name`长度的前置检查或使用安全函数，存在真实风险。 |
| 807 | vim-9.1.1591 | ExpandPackAddDir | cpp/unbounded-write | 1321 | TP | TP | sprintf 使用未经验证的用户输入 `pat` 作为格式化字符串的一部分，目标缓冲区 `s` 的大小为 `pat_len + 26`，但格式化字符串 `"pack/*/opt/%s*"` 在拼接 `pat` 后可能超过该大小，存在... |
| 808 | vim-9.1.1591 | sign_jump | cpp/unbounded-write | 1313 | TP | TP | 代码使用`sprintf`将缓冲区文件名和行号格式化到固定大小的缓冲区`cmd`中，缓冲区大小仅基于文件名长度计算，未考虑格式化字符串`"e +%ld %s"`中行号的最大长度，存在缓冲区溢出风险。 |
| 809 | vim-9.1.1591 | dump_word | cpp/unbounded-write | 4187 | TP | TP | 代码使用STRCPY宏（即strcpy）将变量p的内容复制到固定大小的数组badword中，而p可能指向用户输入或外部数据（如cword或word），且切片中未见对p长度的前置检查，存在缓冲区溢出风险。 |
| 811 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2998 | TP | TP | 代码使用不安全的 STRCPY（即 strcpy）宏将 repl_to 复制到新分配的缓冲区 p 中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见对 repl_to 长度或目标缓冲区 p 大小的校验。 |
| 812 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2999 | TP | TP | 代码使用STRCAT宏（即strcat）将源字符串拼接到目标缓冲区p中，但p的大小是基于ml_get_curline_len() + addlen + 1分配的，而addlen可能为负数（当repl_to_len < repl_fro... |
| 813 | vim-9.1.1591 | count_common_word | cpp/unbounded-write | 1919 | TP | TP | 代码使用STRCPY（即strcpy）将字符串p复制到wc->wc_word，而p的来源（word或buf）长度未在切片中显示有明确的上限约束，且目标缓冲区wc->wc_word的大小为STRLEN(p) + 1，虽然动态分配了足够空... |
| 814 | vim-9.1.1591 | spell_load_lang | cpp/unbounded-write | 1632 | TP | TP | 代码使用STRCPY（即strcpy）将参数lang直接复制到结构体成员sl.sl_lang中，未对源字符串长度进行任何检查。目标缓冲区sl.sl_lang的大小在切片中未定义，但strcpy本身是不安全的，存在缓冲区溢出风险。 |
| 815 | vim-9.1.1591 | spell_move_to | cpp/unbounded-write | 1420 | TP | TP | 代码使用STRCPY宏（即strcpy）将长度不确定的line字符串复制到固定大小的buf缓冲区，且buf的大小仅根据len + MAXWLEN + 2分配，未对源字符串长度进行限制，存在缓冲区溢出风险。 |
| 817 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2369 | TP | TP | 代码中使用STRCAT宏（即strcat）将items[0]和items[1]拼接到缓冲区p中，而p的大小仅根据spin->si_info、items[0]和items[1]的长度计算，未考虑strcat可能导致的缓冲区溢出风险。切片... |
| 818 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2371 | TP | TP | 代码中使用STRCAT宏（即strcat）将items[1]拼接到缓冲区p中，而p的大小是根据多个字符串长度动态计算的，未在切片中看到对目标缓冲区p的边界检查，存在缓冲区溢出的风险。 |
| 819 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2464 | TP | TP | 代码中使用STRCPY(p, items[1])将items[1]（来自fgets读取的输入行）复制到缓冲区p，而p的大小仅为STRLEN(items[1]) + 2，未对源字符串长度进行验证，存在缓冲区溢出风险。 |
| 820 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2495 | TP | TP | 代码在拼接字符串时使用STRCAT宏（即strcat），目标缓冲区大小未知，且输入来自fgets读取的字符串，存在缓冲区溢出风险。切片中未见对目标缓冲区大小或输入长度的检查。 |
| 821 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2644 | TP | TP | 代码中使用 `STRCPY(p, items[1])` 将 `fgets` 读取的字符串 `items[1]` 复制到固定大小的缓冲区 `p` 中，而 `p` 的大小仅通过 `STRLEN(items[1]) + 2` 分配，未检查目... |
| 822 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2746 | TP | TP | 代码中直接使用 sprintf 将 items[4] 拼接到 buf 中，buf 大小为 MAXLINELEN，但 items[4] 来自外部文件行，长度未经验证，可能导致缓冲区溢出。 |
| 823 | vim-9.1.1591 | spell_read_aff | cpp/unbounded-write | 2748 | TP | TP | 代码中使用了 sprintf 将 items[4] 拼接到 buf 中，而 buf 的大小为 MAXLINELEN（定义为 256），但 items[4] 来自外部文件行解析，长度未受限制，可能导致缓冲区溢出。切片中未见对 items... |
| 824 | vim-9.1.1591 | add_sound_suggest | cpp/unbounded-write | 3243 | TP | TP | 代码使用STRCPY宏（即strcpy）将goodword复制到新分配的内存sft->sft_word中，目标缓冲区大小由STRLEN(goodword)+1确定，但goodword作为函数参数来源未知，切片中未见对其长度的验证或边界... |
| 828 | vim-9.1.1591 | strlow_save | cpp/unbounded-write | 463 | TP | TP | 代码在重新分配内存后，使用STRCPY（即strcpy）复制字符串，目标缓冲区大小`s`是根据`STRLEN(res) + 1 + newl - l`计算分配的，但源字符串`p + l`的长度可能超过目标缓冲区剩余空间，存在缓冲区溢出... |
| 829 | vim-9.1.1591 | expand_tag_fname | cpp/unbounded-write | 4141 | TP | TP | 代码使用不安全的STRCPY（即strcpy）将tag_fname复制到固定大小的缓冲区retval中，未检查源字符串长度是否超过目标缓冲区大小MAXPATHL，存在缓冲区溢出风险。切片中未见任何长度校验或安全防护。 |
| 830 | vim-9.1.1591 | get_tagfname | cpp/unbounded-write | 3436 | TP | TP | 代码在行 `STRCPY(buf, fname);` 处使用 `strcpy` 将 `fname`（由 `vim_findfile` 返回）复制到固定大小的缓冲区 `buf` 中，而 `vim_findfile` 可能返回长度超过 `... |
| 831 | vim-9.1.1591 | findtags_add_match | cpp/unbounded-write | 2625 | TP | TP | 代码中直接使用 STRCPY（即 strcpy）宏将来源未知的字符串（如 st->help_lang）复制到固定大小的缓冲区中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何长度校验或安全复制机制。 |
| 832 | vim-9.1.1591 | findtags_add_match | cpp/unbounded-write | 2704 | TP | TP | 代码中多次使用不安全的 STRCPY（即 strcpy）宏，将长度未知的源字符串（如 st->tag_fname, st->ebuf, st->lbuf）复制到固定大小的缓冲区，且切片中未见对源字符串长度的前置检查或使用安全函数，存在... |
| 833 | vim-9.1.1591 | show_one_termcode | cpp/unbounded-write | 7054 | TP | TP | 代码使用STRCPY（即strcpy）将get_special_key_name返回的字符串复制到IObuff+5位置，但未检查源字符串长度是否超过目标缓冲区剩余空间。IObuff大小未知，且源字符串来自外部输入（如环境变量、文件读取... |
| 834 | vim-9.1.1591 | current_tagblock | cpp/unbounded-write | 1392 | TP | TP | 代码使用 sprintf 将用户控制的字符串 p 和长度 len 写入固定大小的缓冲区 spat 和 epat，缓冲区大小由 alloc(len + 39) 和 alloc(len + 9) 分配，但 sprintf 的格式字符串包含... |
| 835 | vim-9.1.1591 | uc_check_code | cpp/unbounded-write | 1810 | TP | TP | 代码在多个分支中直接使用STRCPY（即strcpy）将外部输入（如eap->arg、*split_buf）复制到固定大小的缓冲区buf中，未检查目标缓冲区大小，存在缓冲区溢出风险。切片中未见任何长度校验或安全复制机制。 |
| 836 | vim-9.1.1591 | fname_trans_sid | cpp/unbounded-write | 2278 | TP | TP | 代码在条件 `fnamelen < FLEN_FIXED` 下，使用 `STRCPY`（即 `strcpy`）将 `script_name` 复制到固定大小的缓冲区 `fname_buf` 中。虽然存在长度检查，但 `fname_bu... |
| 839 | vim-9.1.1591 | generate_PUSHFUNC | cpp/unbounded-write | 1042 | TP | TP | 代码使用STRCPY（即strcpy）将变量`name`的内容复制到新分配的缓冲区`funcname`中，虽然分配的大小为`STRLEN(name) + 3`，但`name`的来源在切片中未显示有长度限制或验证，存在缓冲区溢出的潜在风... |
| 840 | vim-9.1.1591 | update_vim9_script_var | cpp/unbounded-write | 947 | TP | TP | 代码使用STRCPY（即strcpy）将变量`name`复制到新分配的内存`newsav->sav_key`中，目标缓冲区大小仅为`STRLEN(name) + 1`，与源字符串长度相同，没有预留额外空间。若`name`未以空字符结尾... |
| 842 | vim-9.1.1591 | find_exported | cpp/unbounded-write | 763 | TP | TP | 代码使用`sprintf`将变量`sid`和`name`拼接到缓冲区`funcname`中，`sid`为整数，`name`为外部输入的函数名，其长度未在切片内进行限制，存在缓冲区溢出风险。算法标签TP与此判断一致。 |
| 843 | vim-9.1.1591 | xxdline | cpp/unbounded-write | 600 | TP | TP | 代码中 `strcpy(z, l)` 将外部输入 `l` 复制到固定大小的缓冲区 `z`，而 `z` 的大小为 `LLEN_NO_COLOR+1`，但未对 `l` 的长度进行校验，存在缓冲区溢出风险。切片中未见任何对 `l` 的长度检... |
| 844 | vim-9.1.1591 | ExpandBufnames | cpp/invalid-pointer-deref | 2980 | TP | TP | 切片代码显示，在 `round == 1` 且 `*file == NULL` 时，`(*file)[count++] = p` 这行代码会向未分配内存的指针 `*file` 写入数据。`*file` 仅在 `round == 2` ... |
| 1583 | redis-7.2.5 | auxHumanNodenameSetter | Dereference of null pointer | 281 | TP | TP | 在 `else if (sdslen(n->human_nodename) != 0)` 这一行，当 `n` 为 `NULL` 时，代码会解引用空指针 `n` 以访问其成员 `human_nodename` 并传递给 `sdslen`... |
| 1622 | redis-8.0.2 | strbuf_ensure_null | Dereference of null pointer | 134 | TP | TP | 代码直接对指针`s`进行解引用访问其成员`buf`和`length`，但切片中未显示对`s`进行空指针检查。如果传入的`s`为NULL，则解引用空指针会导致程序崩溃，这是一个明确的逻辑错误。 |

### 5.2 一致：算法=FP，LLM=FP（共 2280 条）

> 算法与 LLM 均判定为假阳性（False Positive）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 1 | ffmpeg-6.1.1 | upcase_string | cpp/offset-use-before-range-check | 1053 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了在访问 `src[i]` 和 `dst[i]` 之前，索引 `i` 已通过 `i < dst_size-1` 进行了范围检查，因此不存在偏移量在范围检查前使用的问题。 |
| 2 | ffmpeg-6.1.1 | capture_screen | cpp/offset-use-before-range-check | 479 | FP | FP | 在告警行 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 中，变量 `j` 的使用已通过条件 `j < tab` 进行了范围检查，确保了... |
| 3 | ffmpeg-6.1.1 | capture_screen | cpp/offset-use-before-range-check | 479 | FP | FP | 在告警行 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 中，变量 `j` 的使用已通过条件 `j < tab` 进行了范围检查，确保了... |
| 4 | ffmpeg-6.1.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 告警所在行的循环条件 `i<w_r` 已对索引 `i` 进行了范围检查，确保 `dst[i]` 的访问在有效范围内。切片代码中未发现明显的越界访问风险。 |
| 5 | ffmpeg-6.1.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 告警指向的循环条件 `i<w_r` 已对变量 `i` 进行了范围检查，确保其不会越界访问数组 `temp`。切片代码中的逻辑表明该告警是安全的。 |
| 6 | ffmpeg-6.1.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | FP | 切片代码中，while循环条件 `m < b && m < nb_entries - 1` 已经对变量 `m` 进行了范围检查，确保其不会越界访问 `entries` 数组。因此，该告警是误报。 |
| 7 | ffmpeg-6.1.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 215 | FP | FP | 切片代码显示，在访问 `q->subs[i + 1]` 之前，已经通过条件 `i < q->nb_subs - 1` 进行了范围检查，确保了 `i+1` 是有效索引，因此不存在越界访问风险。 |
| 8 | ffmpeg-6.1.1 | choose_out_timebase | cpp/inconsistent-null-check | 1850 | FP | FP | 切片代码显示，`frame_data`函数内部已对`av_buffer_allocz`的失败情况返回NULL，但调用点`choose_out_timebase`函数后续逻辑并未直接解引用`fd`指针，而是通过`fd->dec.tb`访... |
| 9 | ffmpeg-6.1.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | 函数 `skip_space` 内部实现仅跳过空格字符，不会返回 NULL，因此调用处无需检查其返回值是否为 NULL。告警是基于调用模式统计的误报。 |
| 10 | ffmpeg-6.1.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | FP | 函数 `ff_iir_filter_init_state` 的返回值直接返回给调用者，由调用者负责检查内存分配是否成功。切片代码中 `av_mallocz` 的定义也显示其返回 `NULL` 表示分配失败，符合标准的内存分配模式，因此... |
| 11 | ffmpeg-6.1.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1392 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已检查队列中有可用帧，且 `ff_framequeue_peek` 内部有断言确保索引有效，因此返回的指... |
| 12 | ffmpeg-6.1.1 | intercept_id3 | cpp/inconsistent-null-check | 1185 | FP | FP | 函数 `current_segment` 的返回值 `seg` 在后续代码中被直接传递给 `read_from_url` 和用于访问 `seg->size`，但切片中未包含对 `seg` 为 NULL 时的显式检查或防护。然而，`la... |
| 13 | ffmpeg-6.1.1 | get_frag_time | cpp/inconsistent-null-check | 1383 | FP | FP | 告警点位于条件分支 `if (sc->has_sidx)` 内部，该分支仅在 `sc->has_sidx` 为真时执行。切片中未提供 `sc` 的定义，无法确认其值，因此该代码路径可能不会被执行。此外，参考标签 `label` 为 F... |
| 14 | ffmpeg-6.1.1 | init_muxer | cpp/inconsistent-null-check | 189 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，仅对已知的 `s->oformat` 指针进行转换，不会返回空指针。后续代码对 `of` 指针的访问（如 `of->p.flags`、`of->interleave_packet`... |
| 15 | ffmpeg-6.1.1 | url_alloc_for_protocol | cpp/unbounded-write | 101 | FP | FP | 目标缓冲区 `uc->filename` 的大小通过 `strlen(filename) + 1` 精确分配，与源字符串 `filename` 长度匹配，`strcpy` 操作不会导致缓冲区溢出。 |
| 16 | ffmpeg-7.1.1 | upcase_string | cpp/offset-use-before-range-check | 1109 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了只有当 `i` 在有效范围内（`i < dst_size-1`）且源字符串未结束时，才会进入循环体访问 `src[i]`。循环结束后，`i` 的值要么等于 `dst... |
| 17 | ffmpeg-7.1.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警行 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 中，变量 `j` 的使用已包含范围检查 `j < tab`，且 `tab` 值... |
| 18 | ffmpeg-7.1.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 切片代码显示，在告警点所在的while循环条件中，变量`j`的使用已包含范围检查`j < tab`，这确保了`j`不会超出`tab`的边界。因此，该告警是误报。 |
| 19 | ffmpeg-7.1.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码中，在警告所在行的循环条件 `i<w_r` 已经对索引 `i` 进行了范围检查，确保 `i` 不会超出 `w_r` 的边界。该检查先于对 `dst[i]` 的访问，因此不存在越界访问风险，属于工具误报。 |
| 20 | ffmpeg-7.1.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警所在的循环 `for(; (((x86_reg)&temp[i]) & 0x1F) && i<w_r; i++)` 中，变量 `i` 的使用（如 `temp[i]`）之前已经通过条件 `i<w_r` 进行了范围检查... |
| 21 | ffmpeg-7.1.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 148 | FP | FP | 切片代码中，`m` 在 `while` 循环条件 `m < b && m < nb_entries - 1` 和后续的 `if (m == b ...)` 逻辑中受到严格约束，确保其不会越界访问 `entries` 数组。算法标签 `... |
| 22 | ffmpeg-7.1.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 223 | FP | FP | 在切片代码的for循环条件 `i < q->nb_subs` 中，变量 `i` 的使用已受到范围检查的保护。告警所指的 `i` 在数组访问 `q->subs[i]` 和 `q->subs[i + 1]` 之前，已通过循环条件和额外的 ... |
| 23 | ffmpeg-7.1.1 | enc_open | cpp/inconsistent-null-check | 189 | FP | FP | 告警点对 `av_frame_side_data_desc` 的返回值进行了间接的空指针检查。代码在访问 `desc->props` 前，先检查了 `desc->props & AV_SIDE_DATA_PROP_GLOBAL`，这在... |
| 24 | ffmpeg-7.1.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | 函数 `skip_space` 内部实现仅跳过空格字符，不会返回空指针，其返回值始终是有效的字符串指针。告警所提示的 `null` 检查在此上下文中不适用，属于工具误报。 |
| 25 | ffmpeg-7.1.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | FP | 函数 `ff_iir_filter_init_state` 的职责是分配并初始化状态结构体，其返回值由调用者检查和处理。切片代码显示该函数是内存分配器的一个简单封装，遵循了库的常见模式，将空指针检查的责任交给了上层调用者，因此工具报告... |
| 26 | ffmpeg-7.1.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1461 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 27 | ffmpeg-7.1.1 | hls_read_header | cpp/inconsistent-null-check | 2158 | FP | FP | 代码中 `av_find_input_format` 的返回值 `in_fmt` 在后续使用前（如 `strstr(in_fmt->name, "mov")`）已通过条件分支确保其非空，因为只有在 `seg && seg->key_t... |
| 28 | ffmpeg-7.1.1 | intercept_id3 | cpp/inconsistent-null-check | 1240 | FP | FP | 函数 `current_segment` 的返回值 `seg` 在后续代码中被直接传递给 `read_from_url` 和用于访问 `seg->size`，但切片中未包含对 `seg` 为 NULL 时的显式检查。然而，`read_... |
| 29 | ffmpeg-7.1.1 | init_muxer | cpp/inconsistent-null-check | 190 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，它直接返回转换后的指针，不会返回 NULL。因此，调用它的结果不需要进行空指针检查，工具的告警属于误报。 |
| 30 | ffmpeg-7.1.1 | cmp_dm_level0 | cpp/overflow-buffer | 294 | FP | FP | 代码使用 `sizeof(AVDOVIColorMetadata) - offsetof(AVDOVIColorMetadata, signal_eotf)` 计算 `memcmp` 的长度，这是从结构体成员 `signal_eotf... |
| 31 | ffmpeg-7.1.1 | url_alloc_for_protocol | cpp/unbounded-write | 146 | FP | FP | 目标缓冲区 `uc->filename` 的大小通过 `av_mallocz(sizeof(URLContext) + strlen(filename) + 1)` 精确分配，其长度足以容纳源字符串 `filename` 及其终止符，... |
| 32 | ffmpeg-7.0.1 | upcase_string | cpp/offset-use-before-range-check | 1108 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了只有当 `i` 在有效范围内（小于 `dst_size-1`）且源字符串未结束时，才会进入循环体。循环结束后，`i` 的值要么等于 `dst_size-1`（缓冲区... |
| 33 | ffmpeg-7.0.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警行所在的while循环条件中，已经包含了 `j < tab` 的范围检查，确保 `j` 不会越界访问数组。切片代码显示该访问是安全的。 |
| 34 | ffmpeg-7.0.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警行 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 中，变量 `j` 的使用已包含范围检查 `j < tab`，且 `tab` 的... |
| 35 | ffmpeg-7.0.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码中，在警告所在行的循环条件 `i<w_r` 已经对索引 `i` 进行了范围检查，确保 `i` 不会超出 `w_r` 边界，因此不存在越界访问的风险。 |
| 36 | ffmpeg-7.0.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警行使用变量 `i` 的循环条件 `i<w_r` 中，`i` 已与 `w_r` 进行了范围检查，确保了访问的安全性。该告警是工具对循环条件逻辑的误判。 |
| 37 | ffmpeg-7.0.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | FP | 切片代码中，`m` 在 `while` 循环条件 `m < b && m < nb_entries - 1` 中已受到范围检查的保护，确保其递增不会越界。循环条件 `m < nb_entries - 1` 直接保证了 `m` 在访问 ... |
| 38 | ffmpeg-7.0.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 215 | FP | FP | 切片代码显示，在访问 `q->subs[i+1]` 之前，已经通过条件 `i < q->nb_subs - 1` 进行了明确的数组下标范围检查，确保了 `i+1` 不会越界。因此，该告警是误报。 |
| 39 | ffmpeg-7.0.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | 函数 `skip_space` 内部实现仅跳过空格字符，不会返回空指针，其返回值始终是有效的字符串指针。告警提示的“未检查空值”在此上下文中是安全的，属于工具误报。 |
| 40 | ffmpeg-7.0.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | FP | 函数 `ff_iir_filter_init_state` 的职责是分配并初始化状态，其返回值由调用者检查是更合理的模式。切片中 `av_mallocz` 内部已调用 `av_malloc`，其失败时返回 NULL 并会由调用者处理，... |
| 41 | ffmpeg-7.0.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1455 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有 `av_assert1` 断言来... |
| 42 | ffmpeg-7.0.1 | hls_read_header | cpp/inconsistent-null-check | 2107 | FP | FP | 代码中 `in_fmt` 变量在后续的 `avformat_open_input` 调用中被直接使用，但切片显示该调用会检查返回值，且 `in_fmt` 仅在特定条件分支（`seg && seg->key_type == KEY_SA... |
| 43 | ffmpeg-7.0.1 | intercept_id3 | cpp/inconsistent-null-check | 1190 | FP | FP | 代码切片显示，`seg` 指针在后续使用前（如 `seg->size`）未进行空指针检查，这确实存在潜在风险。然而，`current_segment` 函数在索引越界时返回 NULL，但调用上下文 `intercept_id3` 是一... |
| 44 | ffmpeg-7.0.1 | get_frag_time | cpp/inconsistent-null-check | 1541 | FP | FP | 在调用 `get_frag_stream_info` 后，代码立即访问了其返回的指针成员（如 `sidx_pts`），这表明代码逻辑假设该指针非空。结合被调用函数 `get_frag_stream_info` 的定义，其仅在索引越界或... |
| 45 | ffmpeg-7.0.1 | init_muxer | cpp/inconsistent-null-check | 189 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，它直接返回转换后的指针，不会返回 NULL。代码中多处直接使用其返回值访问成员，表明它被设计为总是返回有效指针，无需空值检查。 |
| 46 | ffmpeg-7.0.1 | url_alloc_for_protocol | cpp/unbounded-write | 145 | FP | FP | 目标缓冲区 `uc->filename` 的大小通过 `av_mallocz(sizeof(URLContext) + strlen(filename) + 1)` 精确分配，其长度为 `strlen(filename) + 1`，随... |
| 47 | ffmpeg-7.1 | upcase_string | cpp/offset-use-before-range-check | 1109 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了在访问 `src[i]` 和 `dst[i]` 之前，索引 `i` 已通过 `i < dst_size-1` 的范围检查，因此不存在越界访问风险。 |
| 48 | ffmpeg-7.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警行 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 中，变量 `j` 的使用已通过 `j < tab` 条件进行了范围检查，确保了... |
| 49 | ffmpeg-7.1 | capture_screen | cpp/offset-use-before-range-check | 495 | FP | FP | 在告警所在行，while循环的条件中已经包含了`j < tab`的范围检查，这确保了`j`在访问数组`row`和`charset`之前不会超出`tab`的界限，因此不存在越界访问风险。 |
| 50 | ffmpeg-7.1 | <global> | cpp/offset-use-before-range-check | 80 | FP | FP | 切片代码中，在警告所在行的循环条件 `i<w_r` 已经对索引 `i` 进行了范围检查，确保了 `dst[i]` 的访问不会越界。该告警是工具对复杂循环边界条件的误判。 |
| 51 | ffmpeg-7.1 | <global> | cpp/offset-use-before-range-check | 153 | FP | FP | 切片代码显示，在告警行使用变量 `i` 之前，循环条件 `i<w_r` 已经对其进行了范围检查，确保了 `i` 在有效范围内。代码逻辑是安全的，属于工具误报。 |
| 52 | ffmpeg-7.1 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 148 | FP | FP | 切片代码显示，在访问 `entries[m]` 之前，循环条件 `m < b && m < nb_entries - 1` 已经对 `m` 进行了范围检查，确保其不会越界访问数组。因此，该告警为误报。 |
| 53 | ffmpeg-7.1 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 223 | FP | FP | 切片代码中，在访问 `q->subs[i + 1]` 之前，已经通过条件 `i < q->nb_subs - 1` 进行了明确的数组边界检查，确保了 `i+1` 是有效索引，因此不存在越界访问风险。 |
| 54 | ffmpeg-7.1 | enc_open | cpp/inconsistent-null-check | 189 | FP | FP | 告警点对 `av_frame_side_data_desc` 的返回值进行了间接的空指针检查。代码在访问 `desc->props` 前，先检查了 `desc` 是否为空（`if (!(desc->props & AV_SIDE_DA... |
| 55 | ffmpeg-7.1 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | 函数 `skip_space` 内部实现仅进行简单的空格遍历，不会返回空指针，其返回值始终是有效的字符串指针。告警所提示的“未检查空值”在此上下文中不构成安全问题，属于静态分析工具的误报。 |
| 56 | ffmpeg-7.1 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 207 | FP | FP | 函数 `ff_iir_filter_init_state` 直接返回了 `av_mallocz` 的分配结果，调用者负责检查返回值。切片代码中 `av_mallocz` 的定义也显示其内部已对 `av_malloc` 的返回值进行了检... |
| 57 | ffmpeg-7.1 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1461 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 58 | ffmpeg-7.1 | hls_read_header | cpp/inconsistent-null-check | 2109 | FP | FP | 代码中 `in_fmt` 变量在后续使用前（`avformat_open_input`）已通过 `av_probe_input_buffer` 或条件分支进行了有效赋值或检查，且告警点位于条件分支内，上下文表明即使 `av_find_... |
| 59 | ffmpeg-7.1 | intercept_id3 | cpp/inconsistent-null-check | 1191 | FP | FP | 在切片代码中，`seg` 指针在后续使用前（如 `seg->size`）未进行空指针检查，这确实存在潜在风险。然而，`current_segment` 函数仅在索引越界时返回 NULL，而 `pls->cur_seq_no` 和 `p... |
| 60 | ffmpeg-7.1 | get_frag_time | cpp/inconsistent-null-check | 1630 | FP | FP | 在调用 `get_frag_stream_info` 后，代码立即访问了其返回的指针成员（如 `sidx_pts`），这表明代码逻辑假设指针非空。结合被调用函数 `get_frag_stream_info` 在索引无效时返回 NULL... |
| 61 | ffmpeg-7.1 | init_muxer | cpp/inconsistent-null-check | 190 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，它直接返回转换后的指针，不会返回 NULL。因此，调用它的结果不需要进行空指针检查，工具的告警属于误报。 |
| 62 | ffmpeg-7.1 | cmp_dm_level0 | cpp/overflow-buffer | 294 | FP | FP | 切片代码显示，memcmp操作的大小是通过结构体总大小减去成员偏移量计算得出的，这是访问结构体尾部剩余字段的常见且安全的模式，旨在比较从'signal_eotf'到结构体末尾的所有成员，并非硬编码的24字节。 |
| 63 | ffmpeg-7.1 | url_alloc_for_protocol | cpp/unbounded-write | 146 | FP | FP | 目标缓冲区 uc->filename 的大小为 strlen(filename) + 1，与源字符串 filename 的长度精确匹配，strcpy 操作不会导致缓冲区溢出。代码逻辑确保了缓冲区大小足够。 |
| 64 | ffmpeg-6.0 | upcase_string | cpp/offset-use-before-range-check | 1044 | FP | FP | 循环条件 `src[i] && i < dst_size-1` 确保了只有当 `i` 小于 `dst_size-1` 时才会进入循环体并访问 `src[i]` 和 `dst[i]`，因此循环内的数组访问是安全的。循环结束后，`i` 的... |
| 65 | ffmpeg-6.0 | capture_screen | cpp/offset-use-before-range-check | 485 | FP | FP | 在警告所在行，变量 `j` 的使用已在其循环条件 `j < tab` 中进行了范围检查，确保了 `j` 不会超出 `tab` 的界限，因此不存在越界访问的风险。 |
| 66 | ffmpeg-6.0 | capture_screen | cpp/offset-use-before-range-check | 485 | FP | FP | 在告警行 `while (row[j] == ' ' && charset[j] == CCSET_BASIC_AMERICAN && j < tab)` 中，变量 `j` 的使用已通过条件 `j < tab` 进行了范围检查，确保了... |
| 67 | ffmpeg-6.0 | ff_index_search_timestamp | cpp/offset-use-before-range-check | 147 | FP | FP | 循环条件 `m < b && m < nb_entries - 1` 确保了 `m` 在递增时不会超过 `nb_entries - 1`，从而防止了数组越界访问。切片代码中可见有效的范围检查，因此告警为误报。 |
| 68 | ffmpeg-6.0 | ff_subtitles_queue_finalize | cpp/offset-use-before-range-check | 207 | FP | FP | 切片代码中，在访问 `q->subs[i + 1]` 之前，已通过条件 `i < q->nb_subs - 1` 进行了明确的数组边界检查，确保了 `i+1` 是有效索引，因此不存在越界访问风险。 |
| 69 | ffmpeg-6.0 | ff_ass_split_dialog | cpp/inconsistent-null-check | 457 | FP | FP | 函数 `skip_space` 内部实现仅进行简单的空格遍历，不涉及内存分配或可能返回NULL的复杂操作，其返回值始终是有效的指针（指向输入字符串或字符串末尾的'\0'），因此无需进行NULL检查。告警是基于调用模式统计的误报。 |
| 70 | ffmpeg-6.0 | ff_iir_filter_init_state | cpp/inconsistent-null-check | 203 | FP | FP | 函数 `ff_iir_filter_init_state` 的返回值直接返回给调用者，由调用者负责检查内存分配是否成功。切片代码中 `av_mallocz` 的定义显示其内部调用了 `av_malloc`，而 `av_malloc` ... |
| 71 | ffmpeg-6.0 | ff_inlink_consume_frame | cpp/inconsistent-null-check | 1373 | FP | FP | 在调用 `ff_framequeue_peek` 之前，函数 `ff_inlink_check_available_frame` 已确保队列中有帧，且 `ff_framequeue_peek` 内部有断言 `av_assert1(id... |
| 72 | ffmpeg-6.0 | intercept_id3 | cpp/inconsistent-null-check | 1184 | FP | FP | 函数 `current_segment` 可能返回 NULL，但切片代码中后续对 `seg` 的使用（如 `seg->size`）均发生在 `seg` 被传递给 `read_from_url` 函数之后，而 `read_from_ur... |
| 73 | ffmpeg-6.0 | get_frag_time | cpp/inconsistent-null-check | 1286 | FP | FP | 告警点位于 `if (sc->has_sidx)` 条件分支内，该分支仅在 `sc->has_sidx` 为真时执行。切片中未提供 `sc` 的定义，无法确认其值，但被调用的 `get_frag_stream_info` 函数在索引无... |
| 74 | ffmpeg-6.0 | init_muxer | cpp/inconsistent-null-check | 185 | FP | FP | 函数 `ffofmt` 是一个简单的内联类型转换函数，仅执行指针转换，不会返回空指针。告警点后续的代码多处安全地使用了 `of` 指针，未出现空指针解引用。因此，不检查其返回值是安全的，属于误报。 |
| 75 | ffmpeg-6.0 | url_alloc_for_protocol | cpp/unbounded-write | 102 | FP | FP | 切片代码显示，目标缓冲区 `uc->filename` 的大小是通过 `strlen(filename) + 1` 精确分配的，随后使用 `strcpy` 进行复制，不会发生缓冲区溢出。告警是基于环境变量作为输入来源的推测，但代码逻辑... |
| 76 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1194 | FP | FP | 代码在分配新内存前，已通过 `OPENSSL_free` 释放了旧指针，并将指针置为 NULL。随后检查 `OPENSSL_malloc` 的返回值，仅在分配成功后才进行后续操作。该逻辑正确，不存在 use-after-free 问题。 |
| 77 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1195 | FP | FP | 代码中 `sc->ext.session_ticket->data` 被赋值为 `sc->ext.session_ticket + 1`，这是一个指向新分配内存块内部的指针，并非指向已释放的内存。`OPENSSL_free` 释放的是... |
| 78 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1196 | FP | FP | 代码在分配新内存前，通过OPENSSL_free释放了旧指针，并将指针置为NULL，然后检查新分配的内存是否成功。在ext_data不为NULL的分支中，对sc->ext.session_ticket的访问是在成功分配和检查之后，不存... |
| 79 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1196 | FP | FP | 切片代码显示，在调用 `memcpy` 之前，已通过 `OPENSSL_malloc` 为新分配的 `sc->ext.session_ticket` 分配了内存，并检查了分配结果是否为 NULL。`memcpy` 使用的目标地址 `s... |
| 80 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1198 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。后续的 `OPENSSL_malloc` 分配了新内存，对 `sc->... |
| 81 | openssl-openssl-3.5.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1199 | FP | FP | 切片代码显示，在将 `sc->ext.session_ticket->data` 赋值为 NULL 之前，已经通过 `OPENSSL_free` 释放了旧指针并分配了新内存，不存在对已释放内存的访问。告警点是对新分配结构体成员的初始化... |
| 82 | openssl-openssl-3.5.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1729 | FP | FP | 切片代码显示，在调用memcmp比较s->session->ext.alpn_selected和s->s3.alpn_selected之前，s->s3.alpn_selected已通过OPENSSL_malloc分配内存，且分配失败时... |
| 83 | openssl-openssl-3.5.1 | tls_parse_stoc_npn | cpp/use-after-free | 1660 | FP | FP | 切片代码显示，在调用memcpy之前，已通过OPENSSL_free释放了s->ext.npn，并立即通过OPENSSL_malloc重新分配了内存。这是对同一指针的安全释放与重新分配，并非对已释放内存的非法使用。告警工具可能误判了这... |
| 84 | openssl-openssl-3.5.1 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 告警指出的空指针检查 `if (keySpec != NULL)` 是冗余的，因为在其之前，代码已经通过 `sk_OSSL_CMP_ATAV_pop_free(*keySpec, OSSL_CMP_ATAV_free);` 对 `*k... |
| 85 | openssl-openssl-3.5.1 | <global> | cpp/offset-use-before-range-check | 266 | FP | FP | 切片代码显示，for循环的条件 `src[i] != '\0' && i < len` 已经对偏移量 `i` 进行了范围检查（`i < len`），确保了访问 `src[i]` 和 `tgt[i]` 时 `i` 不会越界，因此告警是误报。 |
| 86 | openssl-openssl-3.5.1 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 告警指向的循环条件 `DB[i] == 0 && i < (maskedDBLen - 1)` 已包含对 `i` 的范围检查，确保 `i` 不会越界访问 `DB` 数组。代码逻辑是安全的，属于工具误报。 |
| 87 | openssl-openssl-3.5.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 345 | FP | FP | 切片代码中，在调用 `CRYPTO_THREAD_get_local` 获取 `data` 后，立即使用 `assert(data != NULL)` 进行断言检查。这表明开发者预期并强制要求 `data` 不为空，若为空则程序会终止... |
| 88 | openssl-openssl-3.5.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `enc_level` 参数无效时会返回 NULL，但调用方 `ossl_qrl_enc_level_set_has_keyslot` 已通过 `ossl_asser... |
| 89 | openssl-openssl-3.5.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在切片代码中显示，其返回 `NULL` 的唯一条件是 `enc_level` 参数无效或 `require_prov` 为真且状态不满足要求。在调用点，`requ... |
| 90 | openssl-openssl-3.5.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 并将结果赋值给 `f` 后，代码立即在 `if (start <= f->range.start && end >= z->range.end)` 中解引用了 `f->... |
| 91 | openssl-openssl-3.5.1 | ts_check_status_info | cpp/unsafe-strcat | 385 | FP | FP | 代码中`failure_text`数组的大小由常量`TS_STATUS_BUF_SIZE`定义，且循环拼接的源字符串`ts_failure_info[i].text`是静态常量数组的元素，其长度在编译时已知。通过循环条件`i < (i... |
| 92 | openssl-openssl-3.5.1 | <global> | cpp/unbounded-write | 30 | FP | FP | 函数 CRYPTO_strdup 在调用 strcpy 前，已通过 CRYPTO_malloc(strlen(str) + 1, ...) 为目标缓冲区分配了精确的、足以容纳源字符串（包括终止符）的空间，因此不存在缓冲区溢出的风险。 |
| 93 | openssl-openssl-3.5.1 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的长度检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而避免了缓冲区溢出。因此该告警为误报。 |
| 94 | openssl-openssl-3.5.1 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码中，在调用strcpy之前，已通过条件`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`对目标缓冲区大小进行了严格检查，确保不会发生溢出。因此该告警为误报。 |
| 95 | openssl-openssl-3.5.1 | main | cpp/unbounded-write | 82 | FP | FP | 代码在调用strcpy前，已为pathname分配了PATH_MAX大小的缓冲区，而argv[n]是目录名，其长度通常远小于PATH_MAX，且后续操作确保了路径拼接不会溢出。结合label为FP，判断为误报。 |
| 96 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3468 | FP | FP | 告警提示可变参数调用未正确终止，但切片代码显示 `QUIC_RAISE_NON_NORMAL_ERROR` 是一个已定义的宏，其参数数量固定，并非真正的可变参数函数调用。这是工具对宏展开的误判，代码本身是安全的。 |
| 97 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3477 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确传递了三个参数（ctx, reason, msg），与宏定义匹配，未发现参数缺失或终止符使用错误的问题。代码逻辑清晰，属于工具误报。 |
| 98 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3487 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 宏调用已正确提供了 `reason` 和 `msg` 两个参数，与宏定义 `(ctx), (reason), (msg)` 的参数数量一致，不存在未终止的可变参数... |
| 99 | openssl-openssl-3.5.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3493 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已正确使用了两个参数（reason 和 msg），符合其定义，未见未终止的可变参数问题。参考标签 FP 也支持此为误报的结论。 |
| 100 | openssl-openssl-3.5.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3409 | FP | FP | 告警提示可变参数调用未正确终止，但切片代码中 `QUIC_RAISE_NON_NORMAL_ERROR` 宏的展开显示其参数列表是固定的（包含 ctx, reason, msg），并非可变参数函数调用。这是一个宏定义，其最终调用的 `... |
| 101 | openssl-openssl-3.5.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3421 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确传递了所有参数，包括 `ERR_R_PASSED_INVALID_ARGUMENT` 和字符串字面量，切片中未见可变参数列表使用不当的证据。该告警可能... |
| 102 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1846 | FP | FP | 告警指出的宏 `QUIC_RAISE_NON_NORMAL_ERROR` 展开后调用的 `quic_raise_non_normal_error` 函数，其参数列表在切片中未完整显示，无法确认是否为可变参数函数及是否缺少终止符。结合告... |
| 103 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1853 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已明确定义为 `quic_raise_non_normal_error` 的包装，其参数列表是固定的，不存在未终止的可变参数调用风险。代码逻辑正... |
| 104 | openssl-openssl-3.5.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1861 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 宏调用符合其定义，该宏接受固定数量的参数，并非一个需要显式终止符的可变参数函数。代码逻辑正确，工具规则在此上下文中不适用。 |
| 105 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 代码在循环中使用掩码（mask）和常量时间操作来安全地复制数据，并通过检查 `flen` 来控制指针移动，防止了越界访问。告警点 `*--em = *from & mask;` 的逻辑确保了当 `flen` 耗尽时，`from` 指针... |
| 106 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中，`em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，并在循环中从 `em + num` ... |
| 107 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用了恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来控制内存访问，确保指针运算不会越界。循环条件 `i < num` 和 `em` 的分配大小 `... |
| 108 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 `em[0]` 的访问是安全的。指针 `em` 指向由 `OPENSSL_malloc(num)` 分配的内存块起始位置，且循环 `for (from += flen, em += num, i = 0; i < num; i... |
| 109 | openssl-openssl-3.5.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的。指针 `em` 指向大小为 `num` 的已分配内存，且循环 `for (from += flen, em += num, i = 0; i < num; i++)` 将 `em` 递减回有效内... |
| 110 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1171 | FP | FP | 切片代码显示，在重新分配内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后，`OPENSSL_malloc` 的返回值被赋给同一个指针，这... |
| 111 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1172 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后分配新内存，并将 `data` 指针指向新分配内存块内的偏移位置（... |
| 112 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1173 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且已为新分配的sc->ext.session_ticket分配了足够的内存（sizeof(TLS_SESSION_TICKET_EXT) + ext... |
| 113 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1173 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且已为新分配的sc->ext.session_ticket分配了足够的内存（sizeof(TLS_SESSION_TICKET_EXT) + ext... |
| 114 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1175 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后对新分配的内存进行了空指针检查，并在 `ext_data` 为 ... |
| 115 | openssl-openssl-3.3.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1176 | FP | FP | 代码在分配新内存前已调用OPENSSL_free释放旧指针，并检查了分配结果，逻辑正确。告警点`sc->ext.session_ticket->data = NULL;`是安全的初始化操作，不存在对已释放内存的访问。 |
| 116 | openssl-openssl-3.3.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1626 | FP | FP | 切片代码显示，在调用memcmp比较s->session->ext.alpn_selected之前，已经通过条件`s->session->ext.alpn_selected == NULL`进行了检查，并且后续的ossl_assert... |
| 117 | openssl-openssl-3.3.1 | tls_parse_stoc_npn | cpp/use-after-free | 1581 | FP | FP | 切片代码显示，在调用memcpy之前，已通过OPENSSL_free释放了s->ext.npn，并立即通过OPENSSL_malloc重新分配了内存。这是一个典型的先释放旧指针再分配新指针的模式，不存在对已释放内存的访问。告警是工具对... |
| 118 | openssl-openssl-3.3.1 | RSA_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 109 | FP | FP | 切片代码显示，变量'i'在for循环中作为索引使用，其初始化和递增均在循环条件'DB[i] == 0 && i < (maskedDBLen - 1)'的检查范围内，该条件确保了'i'在访问DB[i]之前不会超过'maskedDBLe... |
| 119 | openssl-openssl-3.3.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 447 | FP | FP | 切片代码显示函数 `ossl_rcu_read_unlock` 为空实现，未调用 `CRYPTO_THREAD_get_local`，因此工具报告的未检查空指针问题不成立，属于误报。 |
| 120 | openssl-openssl-3.3.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 越界时返回 NULL，而调用前 `enc_level` 由上层逻辑控制，且后续函数 `os... |
| 121 | openssl-openssl-3.3.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在切片中可见，其内部已通过 `ossl_assert` 对 `enc_level` 参数进行了边界检查，并在特定条件下返回 NULL。调用方 `ossl_qrl_... |
| 122 | openssl-openssl-3.3.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 获取 `f` 后，代码立即在 `if (start <= f->range.start && end >= z->range.end)` 中解引用 `f->range.... |
| 123 | openssl-openssl-3.3.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | 代码中`failure_text`数组大小由`TS_STATUS_BUF_SIZE`宏定义，且循环拼接的源字符串`ts_failure_info[i].text`是静态常量数组元素，其长度在编译时已知。切片内未显示有动态或不受控的输入... |
| 124 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 2582 | FP | FP | 切片代码显示，目标缓冲区 `evp_hmac_name` 是通过 `app_malloc` 动态分配的，其大小为固定字符串 "hmac()" 的长度加上变量 `evp_mac_mdname` 的长度，这确保了缓冲区大小足以容纳 `sp... |
| 125 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 2860 | FP | FP | 代码通过 `app_malloc` 为 `evp_cmac_name` 分配了足够的内存，其大小为字符串字面量 "cmac()" 的长度加上 `evp_mac_ciphername` 的长度，确保了 `sprintf` 的目标缓冲区大... |
| 126 | openssl-openssl-3.3.1 | <global> | cpp/unbounded-write | 29 | FP | FP | 函数 `CRYPTO_strdup` 在调用 `strcpy` 前，已通过 `CRYPTO_malloc(strlen(str) + 1, ...)` 为目标缓冲区分配了精确匹配源字符串长度的内存，因此 `strcpy` 操作是安全的... |
| 127 | openssl-openssl-3.3.1 | RAND_file_name | cpp/unbounded-write | 309 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的长度检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而避免了缓冲区溢出。 |
| 128 | openssl-openssl-3.3.1 | RAND_file_name | cpp/unbounded-write | 313 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的大小检查（`if (len + 1 >= size)` 或 `if (len + 1 + strlen(RFILE) + 1 >= size)`），若缓冲区大小不足则提前返回NULL，这有... |
| 129 | openssl-openssl-3.3.1 | main | cpp/unbounded-write | 82 | FP | FP | 切片代码显示，在调用strcpy前，已为pathname分配了大小为PATH_MAX的缓冲区，该大小通常足以容纳系统最大路径长度。同时，代码逻辑确保dirname_len在拼接前不会超过PATH_MAX，且目标缓冲区大小固定，因此不存... |
| 130 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3131 | FP | FP | 代码中 `QUIC_RAISE_NON_NORMAL_ERROR` 宏的调用符合其定义，参数数量正确，且 `label` 为 FP 表明该告警在后续版本中未被修复，属于工具误报。 |
| 131 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3140 | FP | FP | 告警提示调用 `quic_raise_non_normal_error` 应使用 0 作为终止符，但切片代码中 `QUIC_RAISE_NON_NORMAL_ERROR` 宏的定义显示其参数列表是固定的，且调用时传递的参数数量与宏定义... |
| 132 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3150 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 调用在切片中提供了三个参数（ctx, reason, msg），符合其宏定义，未发现参数缺失或终止符使用错误。代码逻辑完整，且参考标签为FP，表明开发者未将其视为... |
| 133 | openssl-openssl-3.3.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3156 | FP | FP | 告警指出的未终止可变参数调用是针对宏 `QUIC_RAISE_NON_NORMAL_ERROR` 的使用，但切片代码中该宏的定义明确包含 `(msg)` 参数，且调用时提供了字符串字面量参数，语法正确。该告警可能是工具对宏展开的误判，... |
| 134 | openssl-openssl-3.3.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3072 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确展开为 `quic_raise_non_normal_error` 函数，其参数列表在切片中可见且完整，未发现未终止的可变参数调用问题。代码逻辑是正常... |
| 135 | openssl-openssl-3.3.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3084 | FP | FP | 告警指出的函数调用 `QUIC_RAISE_NON_NORMAL_ERROR` 是一个宏，其展开为 `quic_raise_non_normal_error` 并传递了固定数量的参数（包括 `OPENSSL_FILE`, `OPENS... |
| 136 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1544 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 宏调用在切片代码中格式正确，其参数 `ERR_R_INTERNAL_ERROR` 和字符串字面量均非可变参数，且宏定义明确，不存在未终止的可变参数调用问题。该告警... |
| 137 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1551 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 调用是一个宏，其展开为 `quic_raise_non_normal_error` 函数。切片代码中该宏的调用格式与定义完全一致，传递了正确的参数数量（包括文件、... |
| 138 | openssl-openssl-3.3.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1561 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 调用是一个宏，其展开为 `quic_raise_non_normal_error` 函数。切片代码中该宏的调用参数数量与宏定义匹配，且告警信息本身提示90次调用中... |
| 139 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 221 | FP | FP | 切片代码显示，在循环读取数据前，通过 `mask = ~constant_time_is_zero(flen)` 和 `flen -= 1 & mask` 等操作，确保了指针 `from` 的递减和访问仅在 `flen > 0` 时发... |
| 140 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 229 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中，`em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，并在循环中从 `em + num` ... |
| 141 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用了恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来控制循环和内存访问，确保指针运算不会越界。告警点 `*--em = *from & mask;... |
| 142 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 切片代码显示，指针 `em` 在循环后指向分配内存的起始位置，访问 `em[0]` 是安全的。告警所担心的越界读取场景（指针等于 `CRYPTO_malloc` + `num`）在代码逻辑中不会发生，因为循环操作确保了 `em` 被正... |
| 143 | openssl-openssl-3.3.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的，因为 `em` 指向 `OPENSSL_malloc(num)` 分配的内存块起始位置，且循环 `for (from += flen, em += num, i = 0; i < num; i+... |
| 144 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1182 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。后续对 `sc->ext.session_ticket` 的访问（如设... |
| 145 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1183 | FP | FP | 切片代码显示，在重新分配内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后，`OPENSSL_malloc` 分配了新内存并赋值给同一指针... |
| 146 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件`if (ext_data != NULL)`进行了检查，并且`sc->ext.session_ticket`指针在分配后也进行了非空校验，没有明显的释放后使用路径。算法参考标签也为FP... |
| 147 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且已为新分配的sc->ext.session_ticket检查了NULL。代码逻辑在切片内是安全的，不存在对已释放内存的访问。 |
| 148 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1186 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后分配新内存并检查成功后才访问其成员，不存在对已释放内存的解引用。告... |
| 149 | openssl-openssl-3.4.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1187 | FP | FP | 代码在设置 `sc->ext.session_ticket->data` 为 NULL 之前，已经通过 `OPENSSL_malloc` 为新结构体分配了内存，并检查了分配结果。`data` 字段被设置为 NULL 是处理 `ext_... |
| 150 | openssl-openssl-3.4.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1689 | FP | FP | 切片代码显示，在调用 `memcmp` 比较 `s->session->ext.alpn_selected` 和 `s->s3.alpn_selected` 之前，`s->s3.alpn_selected` 已通过 `OPENSSL_... |
| 151 | openssl-openssl-3.4.1 | tls_parse_stoc_npn | cpp/use-after-free | 1620 | FP | FP | 切片代码显示，在调用memcpy之前，已通过OPENSSL_free释放了s->ext.npn，并立即通过OPENSSL_malloc重新分配了内存。这是一个典型的先释放旧指针再分配新指针的合法操作，不存在对已释放内存的访问。 |
| 152 | openssl-openssl-3.4.1 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 告警所指的 `if (keySpec != NULL)` 检查并非冗余。在它之前，`*keySpec` 可能已被 `sk_OSSL_CMP_ATAV_pop_free(*keySpec, ...)` 释放并置为悬空指针，此检查用于安全... |
| 153 | openssl-openssl-3.4.1 | <global> | cpp/offset-use-before-range-check | 246 | FP | FP | 循环条件 `src[i] != '\0' && i < len` 已确保索引 `i` 在访问 `src[i]` 和 `tgt[i]` 前进行了范围检查，代码逻辑安全。 |
| 154 | openssl-openssl-3.4.1 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 告警指向的循环条件 `DB[i] == 0 && i < (maskedDBLen - 1)` 中，变量 `i` 的访问 `DB[i]` 发生在范围检查 `i < (maskedDBLen - 1)` 之前，这符合规则检测的模式。然而... |
| 155 | openssl-openssl-3.4.1 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 489 | FP | FP | 切片代码中，在调用 `CRYPTO_THREAD_get_local` 获取 `data` 后，立即使用 `assert(data != NULL)` 进行断言检查，这明确表明代码假设并强制要求 `data` 非空。虽然断言在发布版本... |
| 156 | openssl-openssl-3.4.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 无效时返回 NULL，而调用前 `enc_level` 由上层逻辑控制，且在切片中 `os... |
| 157 | openssl-openssl-3.4.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在切片中显示，当 `enc_level` 参数有效且 `require_prov` 为0时，函数保证返回一个指向有效结构体成员的指针，不会返回NULL。调用时 `... |
| 158 | openssl-openssl-3.4.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 获取 `f` 后，代码立即在 `if (start <= f->range.start ...)` 中解引用了 `f->range.start`，这表明 `f` 被假定... |
| 159 | openssl-openssl-3.4.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | 代码中 `failure_text` 数组大小由 `TS_STATUS_BUF_SIZE` 宏定义，且循环拼接的源字符串 `ts_failure_info[i].text` 是静态常量数组元素，其长度可控。结合 `OSSL_NELEM... |
| 160 | openssl-openssl-3.4.1 | <global> | cpp/unbounded-write | 30 | FP | FP | 函数 `CRYPTO_strdup` 在调用 `strcpy` 前，已通过 `CRYPTO_malloc(strlen(str) + 1, ...)` 为目标缓冲区分配了精确匹配源字符串长度的空间，确保了目标缓冲区大小足够，因此不存在... |
| 161 | openssl-openssl-3.4.1 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的长度检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而避免了缓冲区溢出。 |
| 162 | openssl-openssl-3.4.1 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的长度检查（`if (len + 1 >= size)` 或 `if (len + 1 + strlen(RFILE) + 1 >= size)`），若长度不足则提前返回NULL，这有效防止... |
| 163 | openssl-openssl-3.4.1 | main | cpp/unbounded-write | 82 | FP | FP | 代码在调用strcpy前，已为pathname分配了PATH_MAX大小的缓冲区，该常量通常定义了系统路径的最大长度，足以容纳拼接后的路径。同时，代码通过dirname_len跟踪写入位置，并在拼接前添加路径分隔符，有效控制了写入边界... |
| 164 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3149 | FP | FP | 切片代码显示，宏 QUIC_RAISE_NON_NORMAL_ERROR 的调用格式正确，其最后一个参数 'msg' 是一个字符串字面量，并非可变参数列表的一部分。该告警误将固定参数函数调用识别为未正确终止的可变参数调用。 |
| 165 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3158 | FP | FP | 告警提示调用 `quic_raise_non_normal_error` 应使用 0 作为终止符，但切片代码中该函数是通过宏 `QUIC_RAISE_NON_NORMAL_ERROR` 调用的，其定义明确传递了固定数量的参数（`(ct... |
| 166 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3168 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 调用在切片中提供了三个参数（ctx, reason, msg），符合宏定义要求，未发现参数缺失或终止符问题。代码逻辑清晰，且参考标签为FP，表明此模式在代码库中被... |
| 167 | openssl-openssl-3.4.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3174 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已正确使用了两个参数（reason 和 msg），符合其定义。该告警可能是工具对可变参数宏的误判，且参考标签 `label` 为 FP，表明该问... |
| 168 | openssl-openssl-3.4.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3090 | FP | FP | 告警指出的函数调用 `QUIC_RAISE_NON_NORMAL_ERROR` 是一个宏，其展开后调用的 `quic_raise_non_normal_error` 函数参数列表在切片中未完整给出，无法确认其是否为可变参数函数以及是否... |
| 169 | openssl-openssl-3.4.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3102 | FP | FP | 告警指出的函数调用已通过宏 QUIC_RAISE_NON_NORMAL_ERROR 正确展开，该宏已包含所有必需的参数（包括文件、行号、函数名等），符合函数签名要求，不存在未终止的可变参数调用问题。参考标签 FP 与代码分析结论一致。 |
| 170 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1546 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已正确使用了两个参数（reason 和 msg），符合其定义。该规则检查可变参数调用是否以0终止，但此处调用的参数数量固定且与宏定义匹配，属于工... |
| 171 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1553 | FP | FP | 切片代码显示 QUIC_RAISE_NON_NORMAL_ERROR 是一个宏，其展开为对 `quic_raise_non_normal_error` 的调用，但切片中未提供该函数的可变参数列表定义，无法确认是否存在未终止的可变参数调... |
| 172 | openssl-openssl-3.4.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1563 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 宏调用在切片中已正确展开为 `quic_raise_non_normal_error` 函数，且该宏定义明确，不存在未终止的可变参数问题。代码逻辑清晰，属于工具误报。 |
| 173 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 代码中使用了恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来控制循环和内存访问，这确保了即使指针计算可能接近边界，实际的读写操作也会被安全地屏蔽，从而防... |
| 174 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 切片代码显示告警点 `good = constant_time_is_zero(em[0]);` 中的 `em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，并在循环中从 `em ... |
| 175 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用常量时间操作和掩码（mask）来安全地处理边界条件，循环中的指针运算 `*--em = *from & mask;` 受 `flen` 和 `mask` 控制，确保不会越界访问。算法标签也为 FP，增强了误报的倾向性。 |
| 176 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 `em[0]` 的访问是安全的。指针 `em` 通过 `OPENSSL_malloc(num)` 分配了 `num` 字节内存，随后在循环 `for (from += flen, em += num, i = 0; i < n... |
| 177 | openssl-openssl-3.4.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的，因为 `em` 指向由 `OPENSSL_malloc(num)` 分配的内存块，且 `num` 作为参数传入，在循环 `for (i = 0; i < num; i++)` 中确保了 `em`... |
| 178 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1138 | FP | FP | 切片代码显示，在重新分配内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后，`OPENSSL_malloc` 的返回值被赋给同一个指针，并... |
| 179 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1139 | FP | FP | 代码在分配新内存前已正确释放旧指针（OPENSSL_free），并将指针置为NULL，然后检查新分配的内存是否成功。数据指针被设置为紧邻结构体之后的内存地址，这是有效的指针运算，不存在对已释放内存的访问。 |
| 180 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1140 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保sc->ext.session_ticket不为NULL，且数据指针sc->ext.session_ticket->data被正确指向分配的内存区域（sc->ext.sessio... |
| 181 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1140 | FP | FP | 代码在分配新内存前已正确释放了旧指针（OPENSSL_free），并检查了新分配的内存是否为空。memcpy操作的目标地址是从新分配的结构体计算得出，不存在对已释放内存的访问。 |
| 182 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1142 | FP | FP | 代码逻辑显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。后续的 `memcpy` 操作仅在 `ext_data != NULL... |
| 183 | openssl-openssl-3.2.1 | SSL_set_session_ticket_ext | cpp/use-after-free | 1143 | FP | FP | 代码在分配新内存前已调用OPENSSL_free释放旧指针，并检查了分配结果，这是正确的资源管理。告警点`sc->ext.session_ticket->data = NULL;`是对新分配结构体成员的初始化，不存在对已释放内存的访问。 |
| 184 | openssl-openssl-3.2.1 | tls_parse_stoc_alpn | cpp/use-after-free | 1626 | FP | FP | 切片代码显示，在调用 `memcmp` 比较 `s->session->ext.alpn_selected` 之前，该指针仅在条件 `!s->hit` 分支中被赋值，且赋值前有断言确保其为 NULL。在 `s->hit` 为真的情况下... |
| 185 | openssl-openssl-3.2.1 | tls_parse_stoc_npn | cpp/use-after-free | 1581 | FP | FP | 切片代码显示，在调用 `memcpy` 之前，已通过 `OPENSSL_free` 释放了 `s->ext.npn`，但随后立即通过 `OPENSSL_malloc` 为其分配了新内存。`memcpy` 操作的目标是新分配的内存，而非... |
| 186 | openssl-openssl-3.2.1 | RSA_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 109 | FP | FP | 变量'i'在循环'for (i = 0; DB[i] == 0 && i < (maskedDBLen - 1); i++) ;'中作为索引使用，其范围检查'i < (maskedDBLen - 1)'与使用'DB[i]'是同步进行的... |
| 187 | openssl-openssl-3.2.1 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 越界时可能返回 NULL，而调用前有 `ossl_qrl_enc_level_set_ha... |
| 188 | openssl-openssl-3.2.1 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在切片中可见，其逻辑保证了在给定有效 `enc_level` 和 `require_prov=0` 的条件下，返回值 `el` 指向结构体数组的有效成员，不会为 ... |
| 189 | openssl-openssl-3.2.1 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 获取 `f` 后，代码立即在 `if (start <= f->range.start && end >= z->range.end)` 中解引用了 `f->range... |
| 190 | openssl-openssl-3.2.1 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | 代码中 `failure_text` 缓冲区大小由 `TS_STATUS_BUF_SIZE` 宏定义，且循环拼接的源字符串 `ts_failure_info[i].text` 是静态常量数组中的短字符串，拼接操作在已知的、有限的常量字... |
| 191 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 2530 | FP | FP | 切片代码显示，目标缓冲区 `evp_hmac_name` 是通过 `app_malloc` 动态分配的，其大小为固定字符串 "hmac()" 的长度加上 `evp_mac_mdname` 的长度，这确保了 `sprintf` 写入的内... |
| 192 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 2826 | FP | FP | 切片代码显示，目标缓冲区 `evp_cmac_name` 是通过 `app_malloc` 动态分配的，其大小精确计算为 `sizeof("cmac()") + strlen(evp_mac_ciphername)`，足以容纳格式化字... |
| 193 | openssl-openssl-3.2.1 | <global> | cpp/unbounded-write | 29 | FP | FP | 函数 `CRYPTO_strdup` 在调用 `strcpy` 前，已通过 `CRYPTO_malloc(strlen(str) + 1, ...)` 为目标缓冲区分配了精确匹配源字符串长度的内存，确保了缓冲区大小足够，因此不存在缓冲... |
| 194 | openssl-openssl-3.2.1 | RAND_file_name | cpp/unbounded-write | 309 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的长度检查（`if (len + 1 >= size)`），当环境变量字符串长度超过目标缓冲区大小时，函数会提前返回NULL，从而避免了缓冲区溢出。因此该告警为误报。 |
| 195 | openssl-openssl-3.2.1 | RAND_file_name | cpp/unbounded-write | 313 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的长度检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而避免了缓冲区溢出。因此该告警为误报。 |
| 196 | openssl-openssl-3.2.1 | main | cpp/unbounded-write | 82 | FP | FP | 代码为路径拼接操作，`pathname` 已分配 `PATH_MAX` 固定大小缓冲区，且 `dirname_len` 和 `filename` 均来自文件系统目录读取，长度可控，不存在来自外部攻击者的任意长输入导致溢出的风险。 |
| 197 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3054 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确使用了 `NULL` 作为可变参数的终止符，这与宏定义和函数 `expect_quic_conn_only` 中的用法一致，符合代码规范，属于静态分析... |
| 198 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3063 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片中已明确定义为接收两个固定参数和一个可变参数 `(msg)`，而调用处的 `msg` 参数是一个字符串字面量，并非未终止的可变参数列表。代码逻辑清晰，... |
| 199 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3073 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中传递了三个参数（ctx, reason, msg），符合其定义，未发现参数缺失或终止符使用错误的问题。该告警可能是工具对宏展开或可变参数函数模式... |
| 200 | openssl-openssl-3.2.1 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3079 | FP | FP | 告警指出的未终止可变参数调用在切片代码中未体现，且被调用的宏 `QUIC_RAISE_NON_NORMAL_ERROR` 已明确定义为固定参数格式。代码逻辑是正常的错误处理流程，未发现实际的可变参数使用错误。参考标签 `FP` 与此分... |
| 201 | openssl-openssl-3.2.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 2995 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确展开为 `quic_raise_non_normal_error` 函数，其参数列表在宏定义中明确，不存在未终止的可变参数问题。代码逻辑是安全的，属于... |
| 202 | openssl-openssl-3.2.1 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3007 | FP | FP | 告警指出的函数调用 `QUIC_RAISE_NON_NORMAL_ERROR` 是一个宏，其展开后调用的 `quic_raise_non_normal_error` 函数参数列表是固定的（包含 `ctx`, `file`, `line... |
| 203 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1520 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 宏调用已正确使用了两个参数（reason 和 msg），符合其宏定义 `quic_raise_non_normal_error(ctx, OPENSSL_FILE... |
| 204 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1527 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 宏调用符合其定义，该宏接受三个参数，切片中所有调用均提供了三个参数，未见未终止的可变参数调用问题。参考标签 `label` 为 FP，与代码分析结论一致。 |
| 205 | openssl-openssl-3.2.1 | ensure_channel_started | cpp/unterminated-variadic-call | 1537 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 宏调用在切片中已正确终止，其展开为 `quic_raise_non_normal_error` 函数调用，参数列表完整且格式正确，不存在未终止的可变参数问题。代码... |
| 206 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 221 | FP | FP | 切片代码显示，在循环 `for (from += flen, em += num, i = 0; i < num; i++)` 中，指针 `from` 和 `em` 的移动以及访问操作 `*--em = *from & mask;` ... |
| 207 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 229 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中，`em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，并在循环中从 `em + num` ... |
| 208 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用了恒定时间操作（如 constant_time_is_zero, constant_time_select_8）和掩码（mask）来控制循环和内存访问，确保指针运算在边界内。告警点 `*--em = *from & mask;... |
| 209 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 切片代码显示，在访问 `em[0]` 之前，`em` 指针已通过 `em += num` 调整，随后在循环中执行 `*--em` 操作，这确保了 `em` 指针在循环结束后指向有效分配内存的起始位置。因此，对 `em[0]` 的访问是... |
| 210 | openssl-openssl-3.2.1 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的。指针 `em` 指向通过 `OPENSSL_malloc(num)` 分配的大小为 `num` 的内存块，且循环 `for (i = 0; i < num; i++)` 确保了 `em` 数组的... |
| 211 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1182 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后对新分配的内存进行了空指针检查，访问 `sc->ext.sessi... |
| 212 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1183 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将指针置为 NULL。随后分配新内存并检查成功后才进行赋值和访问，不存在对已释放内存的访问... |
| 213 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用memcpy之前，已通过条件判断确保ext_data不为NULL，且已为新分配的sc->ext.session_ticket检查了非空，不存在对已释放内存的访问。告警可能是工具对指针运算 `sc->ext.sess... |
| 214 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1184 | FP | FP | 切片代码显示，在调用 `memcpy` 之前，已通过 `OPENSSL_malloc` 为新指针 `sc->ext.session_ticket` 分配了内存，并检查了分配结果。`memcpy` 使用的目标地址 `sc->ext.se... |
| 215 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1186 | FP | FP | 切片代码显示，在分配新内存给 `sc->ext.session_ticket` 之前，已通过 `OPENSSL_free` 释放了旧指针，并立即将其置为 NULL。随后分配新内存，并根据 `ext_data` 是否为 NULL 进行安... |
| 216 | openssl-openssl-3.4.0 | SSL_set_session_ticket_ext | cpp/use-after-free | 1187 | FP | FP | 代码在分配内存后立即检查了指针是否为NULL，并在分配失败时提前返回，确保了后续对 `sc->ext.session_ticket` 的访问是安全的。告警点 `sc->ext.session_ticket->data = NULL;`... |
| 217 | openssl-openssl-3.4.0 | tls_parse_stoc_alpn | cpp/use-after-free | 1688 | FP | FP | 切片代码显示，在调用 `memcmp` 比较 `s->session->ext.alpn_selected` 和 `s->s3.alpn_selected` 之前，`s->s3.alpn_selected` 已通过 `OPENSSL_... |
| 218 | openssl-openssl-3.4.0 | tls_parse_stoc_npn | cpp/use-after-free | 1619 | FP | FP | 切片代码显示，在调用 `memcpy` 之前，`s->ext.npn` 已被 `OPENSSL_free` 释放，但随后立即通过 `OPENSSL_malloc` 重新分配了内存。这是一个典型的释放后立即重新分配的模式，用于复用同一指... |
| 219 | openssl-openssl-3.4.0 | OSSL_CMP_ITAV_get1_certReqTemplate | cpp/redundant-null-check-simple | 471 | FP | FP | 告警指出的空指针检查（`if (keySpec != NULL)`）是冗余的，因为在其之前的代码行 `sk_OSSL_CMP_ATAV_pop_free(*keySpec, OSSL_CMP_ATAV_free);` 已经对 `*ke... |
| 220 | openssl-openssl-3.4.0 | <global> | cpp/offset-use-before-range-check | 246 | FP | FP | 循环条件 `src[i] != '\0' && i < len` 确保了在访问 `src[i]` 之前，索引 `i` 已通过 `i < len` 检查，防止了越界访问。代码逻辑安全，属于误报。 |
| 221 | openssl-openssl-3.4.0 | ossl_rsa_verify_PKCS1_PSS_mgf1 | cpp/offset-use-before-range-check | 117 | FP | FP | 告警指向的代码行 `for (i = 0; DB[i] == 0 && i < (maskedDBLen - 1); i++) ;` 是一个用于跳过前导零的循环，其循环条件 `i < (maskedDBLen - 1)` 已经对 `i... |
| 222 | openssl-openssl-3.4.0 | ossl_rcu_read_unlock | cpp/inconsistent-null-check | 470 | FP | FP | 切片代码中，在调用 `CRYPTO_THREAD_get_local` 获取 `data` 后，立即使用 `assert(data != NULL);` 进行断言检查，这明确表明代码假设并强制要求 `data` 非空。虽然断言在发布版... |
| 223 | openssl-openssl-3.4.0 | el_teardown_keyslot | cpp/inconsistent-null-check | 88 | FP | FP | 函数 `ossl_qrl_enc_level_set_get` 在 `enc_level` 无效或 `require_prov` 条件不满足时会返回 NULL，但调用方 `ossl_qrl_enc_level_set_has_keys... |
| 224 | openssl-openssl-3.4.0 | ossl_qrl_enc_level_set_have_el | cpp/inconsistent-null-check | 47 | FP | FP | 被调用的函数 `ossl_qrl_enc_level_set_get` 在 `require_prov` 参数为 0 时，仅在 `enc_level` 无效时返回 NULL，而调用时 `require_prov` 明确为 0，且 `e... |
| 225 | openssl-openssl-3.4.0 | ossl_uint_set_insert | cpp/inconsistent-null-check | 163 | FP | FP | 在调用 `ossl_list_uint_set_head(s)` 获取 `f` 后，代码立即在 `if (start <= f->range.start && end >= z->range.end)` 中解引用了 `f->range... |
| 226 | openssl-openssl-3.4.0 | ts_check_status_info | cpp/unsafe-strcat | 383 | FP | FP | 代码中 `failure_text` 数组大小为 `TS_STATUS_BUF_SIZE`，且循环拼接的源字符串 `ts_failure_info[i].text` 是静态常量数组元素，其长度可控。结合 `OSSL_NELEM` 宏限... |
| 227 | openssl-openssl-3.4.0 | <global> | cpp/unbounded-write | 30 | FP | FP | 函数 `CRYPTO_malloc` 已为 `strlen(str) + 1` 分配了足够的内存，`strcpy` 的目标缓冲区大小与源字符串长度精确匹配，不会发生缓冲区溢出。 |
| 228 | openssl-openssl-3.4.0 | RAND_file_name | cpp/unbounded-write | 318 | FP | FP | 切片代码中，在调用strcpy之前，存在明确的长度检查（len + 1 >= size），如果环境变量字符串长度超过目标缓冲区大小，函数会提前返回NULL，从而避免了缓冲区溢出。因此该告警为误报。 |
| 229 | openssl-openssl-3.4.0 | RAND_file_name | cpp/unbounded-write | 322 | FP | FP | 切片代码中，在调用strcpy之前，已通过条件`len + 1 >= size`或`len + 1 + strlen(RFILE) + 1 >= size`对目标缓冲区大小进行了严格检查，确保不会发生溢出。因此该告警为误报。 |
| 230 | openssl-openssl-3.4.0 | main | cpp/unbounded-write | 82 | FP | FP | 代码在调用strcpy前，已为pathname分配了大小为PATH_MAX的缓冲区，该常量通常定义了系统路径的最大长度，足以容纳拼接后的完整路径名，因此不存在缓冲区溢出风险。 |
| 231 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3136 | FP | FP | 告警指出的函数调用使用了宏 `QUIC_RAISE_NON_NORMAL_ERROR`，该宏已正确展开为 `quic_raise_non_normal_error` 函数，并传递了所有必需的参数（包括 `ctx`, `reason`,... |
| 232 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3145 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已正确使用了两个参数（reason 和 msg），符合其定义 `quic_raise_non_normal_error(ctx, ..., re... |
| 233 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3155 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR(&ctx, ERR_R_INTERNAL_ERROR, "ref")` 提供了三个参数，与宏定义 `(ctx, reason, msg)` 的参数数量一致，切... |
| 234 | openssl-openssl-3.4.0 | ossl_quic_attach_stream | cpp/unterminated-variadic-call | 3161 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已正确使用了两个参数（reason 和 msg），符合其定义 `quic_raise_non_normal_error(ctx, ..., re... |
| 235 | openssl-openssl-3.4.0 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3077 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已正确展开为 `quic_raise_non_normal_error` 函数，其参数列表在切片中可见是完整的，且该调用位于明确的错误处理路径中，代码逻辑清... |
| 236 | openssl-openssl-3.4.0 | ossl_quic_set_default_stream_mode | cpp/unterminated-variadic-call | 3089 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 已明确定义为 `quic_raise_non_normal_error` 函数，其参数列表在宏定义中已完整给出，不存在未终止的可变参数调用问题。代码逻辑正确... |
| 237 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1546 | FP | FP | 告警指出的宏调用 `QUIC_RAISE_NON_NORMAL_ERROR` 在切片代码中已正确提供了所有必需的参数（ctx, reason, msg），没有证据表明存在未终止的可变参数调用问题。参考标签为FP，与代码分析一致，判定为误报。 |
| 238 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1553 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 调用是宏展开，其参数列表在宏定义中已明确包含终止符 `(msg)`，符合可变参数函数调用规范。切片代码中未发现参数缺失或格式错误，属于工具误判。 |
| 239 | openssl-openssl-3.4.0 | ensure_channel_started | cpp/unterminated-variadic-call | 1563 | FP | FP | 告警指出的 `QUIC_RAISE_NON_NORMAL_ERROR` 调用在切片代码中是一个宏展开，其参数数量与宏定义匹配，且上下文显示该调用是错误处理流程的一部分，未发现明显的可变参数使用错误。结合参考标签为FP，判断为误报。 |
| 240 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 245 | FP | FP | 代码在循环中使用了掩码（mask）和常量时间操作来安全地复制数据，并通过检查flen来防止越界访问。告警点`*--em = *from & mask;`的逻辑确保了当flen耗尽时，from指针不会递减，且读取的值被掩码清零，因此不会... |
| 241 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_OAEP_mgf1 | cpp/invalid-pointer-deref | 253 | FP | FP | 告警点 `good = constant_time_is_zero(em[0]);` 中，`em` 指针已通过 `em = OPENSSL_malloc(num);` 分配了 `num` 字节内存，且后续循环 `for (i = 0;... |
| 242 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 207 | FP | FP | 代码使用常量时间操作和掩码（mask）来安全地处理边界条件，循环中的 `flen` 递减和指针移动受 `mask` 保护，当 `flen` 耗尽后，`mask` 变为0，后续读取操作被安全地屏蔽，不会发生越界访问。 |
| 243 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 210 | FP | FP | 告警点 `em[0]` 的访问是安全的，因为 `em` 指针指向 `OPENSSL_malloc(num)` 分配的内存块起始位置，且循环 `for (from += flen, em += num, i = 0; i < num; ... |
| 244 | openssl-openssl-3.4.0 | RSA_padding_check_PKCS1_type_2 | cpp/invalid-pointer-deref | 211 | FP | FP | 告警点 `em[1]` 的访问是安全的。指针 `em` 指向大小为 `num` 的动态分配内存，而循环 `for (i = 0; i < num; i++)` 确保了 `em` 被初始化为指向有效内存区域的末尾，后续的 `*--em`... |
| 245 | git-2.47.1 | is_command | cpp/redundant-null-check-simple | 2602 | FP | FP | 代码逻辑中，`nick` 变量在 `(nick && *p++ == nick)` 表达式中被检查非空后才进行解引用，因此告警点之前的空值检查是必要的，并非冗余。静态分析工具未能正确理解短路求值逻辑，导致误报。 |
| 246 | git-2.47.1 | refname_is_safe | cpp/no-space-for-terminator | 350 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，这是字符串 `rest` 的长度，而 `rest` 来自 `skip_prefix` 且已通过非空检查。`normalize_path_copy` 函数要求目标缓冲区足够容... |
| 247 | git-2.47.1 | fill_es_indent_data | cpp/offset-use-before-range-check | 894 | FP | FP | 在第一个while循环的条件中，访问`s[off]`之前已经通过`off < len - 1`检查了偏移量`off`的范围，确保了它不会越界访问数组`s`。代码逻辑是安全的。 |
| 248 | git-2.47.1 | ce_write_entry | cpp/offset-use-before-range-check | 2687 | FP | FP | 变量 `common` 在 for 循环的条件中已通过 `common < previous_name->len` 进行了范围检查，确保其不会超过 `previous_name->len`。后续使用 `ce->name + commo... |
| 249 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 757 | FP | FP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，对变量 `pos` 的访问 `s1[pos]` 和 `s2[pos]` 发生在范围检查 `pos < len` 之前，这违反了先检查后使用的安全... |
| 250 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 757 | FP | FP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，对 `pos` 的访问 `s1[pos]` 和 `s2[pos]` 发生在 `pos < len` 的范围检查之前，这触发了规则告警。然而，该循... |
| 251 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 792 | FP | FP | 在循环条件 `wcs1[pos] == wcs2[pos] && pos < len` 中，对 `pos` 的访问 `wcs1[pos]` 和 `wcs2[pos]` 发生在范围检查 `pos < len` 之前，这触发了规则告警。然... |
| 252 | git-2.47.1 | clar__assert_equal | cpp/offset-use-before-range-check | 792 | FP | FP | 在for循环条件 `wcs1[pos] == wcs2[pos] && pos < len` 中，对 `pos` 的访问 `wcs1[pos]` 和 `wcs2[pos]` 发生在范围检查 `pos < len` 之前，这违反了先检查... |
| 253 | git-2.47.1 | setup_scoreboard | cpp/inconsistent-null-check | 2857 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，此时 `sb->final` 非空且其 OID 为空。`get_blame_suspects` 函数定义明确返回 `NULL` ... |
| 254 | git-2.47.1 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的函数 `branch_get` 在输入为 `NULL` 或空字符串时会返回 `the_repository->remote_state->current_branch`，该返回值可能为 `NULL`，但告警点后的代码立即访问 ... |
| 255 | git-2.47.1 | bisect_successful | cpp/inconsistent-null-check | 646 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `refs_read_ref` 检查了 `bad_ref` 引用的存在性并获取了其 OID，这确保了后续查找的引用是有效的，因此空指针检查在... |
| 256 | git-2.47.1 | update_head | cpp/inconsistent-null-check | 685 | FP | FP | 代码中 `refs_update_ref` 调用时指定了 `UPDATE_REFS_DIE_ON_ERR` 错误处理模式，若 `lookup_commit_reference` 返回 NULL 导致后续 `&c->object.oid... |
| 257 | git-2.47.1 | describe_commit | cpp/inconsistent-null-check | 324 | FP | FP | 函数 `lookup_commit_reference` 在失败时会返回 NULL，但切片代码显示，在后续的 `if (!max_candidates)` 分支中，当 `cmit` 为 NULL 时，代码会通过 `die` 函数终止程... |
| 258 | git-2.47.1 | do_fetch | cpp/inconsistent-null-check | 1628 | FP | FP | 代码在调用 `branch_get(NULL)` 后，其返回值 `branch` 仅在 `branch_has_merge_config(branch)` 中被使用，而该函数内部已包含对 `branch` 是否为 NULL 的检查（`... |
| 259 | git-2.47.1 | get_ref_map | cpp/inconsistent-null-check | 552 | FP | FP | 代码中 `branch_get(NULL)` 的返回值 `branch` 在后续使用前，已通过 `branch_has_merge_config(branch)` 函数进行安全检查，该函数内部会检查 `branch` 是否为 NULL... |
| 260 | git-2.47.1 | refspec_append_mapped | cpp/inconsistent-null-check | 90 | FP | FP | 被调用的 `branch_get` 函数内部已对 `name` 参数进行了空指针和空字符串检查，并返回一个有效的 `struct branch` 指针（例如 `current_branch` 或 `make_branch` 的结果），... |
| 261 | git-2.47.1 | do_create_stash | cpp/inconsistent-null-check | 1390 | FP | FP | 告警点 `head_commit = lookup_commit(...)` 的返回值在后续代码中被直接使用（如 `head_commit->object.oid`），但切片中未显示对 `info->b_commit` 来源的验证。然... |
| 262 | git-2.47.1 | reset_tree | cpp/inconsistent-null-check | 285 | FP | FP | 告警指出未检查 parse_tree_indirect 的返回值是否为 NULL，但切片代码显示其返回值 `tree` 立即作为参数传递给 `parse_tree(tree)`，后者会检查其有效性并返回错误。代码逻辑在切片内保证了错误... |
| 263 | git-2.47.1 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1924 | FP | FP | 告警点后的代码直接解引用 `sub->name`，表明 `sub` 指针被假定为非空。结合 `submodule_from_path` 函数定义，它返回一个指向 `const struct submodule` 的指针，在给定的上下文... |
| 264 | git-2.47.1 | write_bundle_refs | cpp/inconsistent-null-check | 435 | FP | FP | 在调用 `lookup_commit_reference` 后，代码立即通过 `e->item == &(one->object)` 访问了 `one->object` 成员，这隐含地假设了 `one` 不为空。结合 `label` ... |
| 265 | git-2.47.1 | update_one | cpp/inconsistent-null-check | 328 | FP | FP | 在调用 `find_subtree` 时，参数 `create` 被设置为 1，这确保了函数在子树不存在时会创建并返回一个非空指针。切片代码中后续对 `sub->cache_tree` 的直接解引用也证实了这一点，因此不存在空指针解引... |
| 266 | git-2.47.1 | verify_one_commit_graph | cpp/inconsistent-null-check | 2774 | FP | FP | 代码中 `lookup_commit` 的返回值 `graph_commit` 在后续使用前，已通过 `parse_commit_in_graph_one` 或 `repo_parse_commit_internal` 等函数进行有效... |
| 267 | git-2.47.1 | unparse_commit | cpp/inconsistent-null-check | 188 | FP | FP | 切片代码显示，函数 `lookup_commit` 在内部已处理了 `obj` 为 NULL 的情况，会调用 `create_object` 返回一个对象，因此其返回值 `c` 不太可能为 NULL。后续代码 `if (!c->obj... |
| 268 | git-2.47.1 | clear_common_flag | cpp/inconsistent-null-check | 2132 | FP | FP | 告警点位于一个迭代循环中，该循环条件 `while ((oid = oidset_iter_next(&iter)))` 确保了 `oid` 非空。`lookup_object` 函数在哈希表中查找此 `oid` 对应的对象，若未找到... |
| 269 | git-2.47.1 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 143 | FP | FP | 告警点位于 `if (*type == OBJ_TAG)` 分支内，该分支仅在 `oid_object_info_extended` 调用成功（返回0）且对象类型为标签时进入。随后对 `tag->tagged` 的访问隐式检查了 `t... |
| 270 | git-2.47.1 | find_merge_parents | cpp/inconsistent-null-check | 616 | FP | FP | 告警点 `obj = parse_object(...)` 的返回值 `obj` 在后续代码中仅用于 `add_merge_parent(result, &obj->oid, ...)`，而该函数内部仅对 `obj->oid` 进行复... |
| 271 | git-2.47.1 | get_parent | cpp/inconsistent-null-check | 1107 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将其返回值 `commit` 传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 函数会检查 `commit` 的有... |
| 272 | git-2.47.1 | show_ambiguous_object | cpp/inconsistent-null-check | 442 | FP | FP | 代码中 `lookup_tag` 的返回值 `tag` 在 `if (!parse_tag(tag) && tag->tag)` 条件中被直接使用，但 `parse_tag` 函数内部会处理 `tag` 为 NULL 或无效的情况并返... |
| 273 | git-2.47.1 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3344 | FP | FP | 函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到项（`!ref->base`）的情况进行了处理并返回 NULL，调用方 `leave_one_treesame_to_parent` 虽未显... |
| 274 | git-2.47.1 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 701 | FP | FP | 切片代码显示，`lookup_commit` 函数内部已处理空对象指针情况（若 `obj` 为空则创建新对象），因此调用点不检查返回值是安全的。算法标签 FP 与此分析一致。 |
| 275 | git-2.47.1 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在内部已处理空对象情况，若 `obj` 为空会调用 `create_object` 创建新对象并返回，因此调用者无需额外进行空值检查。该告警属于工具对代码模式的误判。 |
| 286 | git-2.47.1 | add_patterns | cpp/invalid-pointer-deref | 1151 | FP | FP | 代码在分配缓冲区时使用 `xmallocz(size)`，该函数分配了 `size+1` 字节并清零，因此 `buf[size] = '\n'` 的写入操作是在分配的缓冲区末尾（索引 `size` 处），是安全的，不会导致越界写入。 |
| 287 | git-2.47.1 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1660 | FP | FP | 代码中 `buffer = xmallocz_gently(size);` 分配了 `size` 字节的内存，但随后 `stream.avail_out = size + 1;` 和循环中的解压逻辑确保了写入不会超过 `size` 字... |
| 288 | git-2.47.1 | should_prune_worktree | cpp/invalid-pointer-deref | 788 | FP | FP | 代码在写入 path[len] = '\0' 前，通过 while 循环确保了 len 已递减至去除尾部换行符后的有效长度，因此该写入操作在已分配的缓冲区边界内，不会发生越界。 |
| 289 | git-2.50.1 | refname_is_safe | cpp/no-space-for-terminator | 353 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，这是字符串 `rest` 的长度，而 `rest` 是 `refname` 去掉前缀 `"refs/"` 后的部分。`restlen` 来自 `strlen(rest)`，... |
| 290 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，对`s1[pos]`和`s2[pos]`的访问与对`pos`的范围检查`pos < len`是同时进行的，逻辑上确保了访问不会越界。该告警是工具... |
| 291 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，对`s1[pos]`和`s2[pos]`的访问与对`pos`的范围检查`pos < len`是同时进行的，逻辑上确保了访问不会越界。这是一个典型... |
| 292 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 在for循环条件 `wcs1[pos] == wcs2[pos] && pos < len` 中，对 `pos` 的访问 `wcs1[pos]` 和 `wcs2[pos]` 发生在范围检查 `pos < len` 之前，这违反了规则。... |
| 293 | git-2.50.1 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 在for循环条件 `pos < len` 中，变量 `pos` 的使用（`wcs1[pos] == wcs2[pos]`）发生在与 `len` 的范围检查之后，逻辑上确保了访问不会越界。告警所提示的'使用前应进行范围检查'的条件已满足。 |
| 294 | git-2.50.1 | setup_scoreboard | cpp/inconsistent-null-check | 2858 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，此时 `sb->final` 非空且其 OID 为空。`get_blame_suspects` 函数定义明确返回 `NULL` ... |
| 295 | git-2.50.1 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的 `branch_get` 函数内部已对空指针输入进行了处理，并始终返回一个有效的 `struct branch` 指针（可能指向 `current_branch` 或新创建的对象），因此调用后无需进行空指针检查。 |
| 296 | git-2.50.1 | write_index_patch | cpp/inconsistent-null-check | 1435 | FP | FP | 告警点调用 `lookup_tree` 时传入的是 `the_repository->hash_algo->empty_tree`，这是一个已知的、有效的空树对象ID，函数内部会成功返回一个有效的 `tree` 对象，不会返回 NUL... |
| 297 | git-2.50.1 | bisect_successful | cpp/inconsistent-null-check | 648 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `refs_read_ref` 读取了引用并获取了对象ID (`oid`)，这表明引用 `bad_ref` 很可能存在。后续 `commit... |
| 298 | git-2.50.1 | describe_commit | cpp/inconsistent-null-check | 326 | FP | FP | 在切片代码中，`cmit` 指针在解引用前（如 `cmit->object.oid`）已被用于 `die` 函数调用，这表明代码逻辑假设 `lookup_commit_reference` 调用成功，且上下文未提供该调用可能失败的场景... |
| 299 | git-2.50.1 | <global> | cpp/inconsistent-null-check | 547 | FP | FP | 告警点调用 `lookup_tree(the_repository, the_repository->hash_algo->empty_tree)`，其中 `empty_tree` 是一个已知的、有效的内部对象标识符，不可能返回 NU... |
| 300 | git-2.50.1 | get_ref_map | cpp/inconsistent-null-check | 550 | FP | FP | 代码中调用 branch_get(NULL) 后，其返回值 branch 被立即传递给 branch_has_merge_config(branch) 函数，该函数内部已包含对 branch 指针的 NULL 检查（`return b... |
| 301 | git-2.50.1 | refspec_append_mapped | cpp/inconsistent-null-check | 92 | FP | FP | 被调用的函数 `branch_get` 在切片中可见其内部逻辑，它总是返回一个有效的 `struct branch` 指针（要么是 `current_branch`，要么是 `make_branch` 的结果），不会返回 NULL。因... |
| 302 | git-2.50.1 | do_create_stash | cpp/inconsistent-null-check | 1397 | FP | FP | 告警点 `head_commit = lookup_commit(...)` 的返回值在后续代码中被直接用于 `head_commit->object.oid` 和 `commit_list_insert`，未进行空指针检查。然而，`... |
| 303 | git-2.50.1 | reset_tree | cpp/inconsistent-null-check | 286 | FP | FP | 告警指出未检查 parse_tree_indirect 的返回值是否为 NULL，但切片代码显示其返回值 `tree` 立即被传递给 `parse_tree` 函数，后者会检查其有效性并返回错误。这表明代码逻辑通过后续调用间接处理了可... |
| 304 | git-2.50.1 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1932 | FP | FP | 告警点调用的 `submodule_from_path` 函数返回的指针 `sub` 在后续代码中被直接解引用（`sub->name`），这表明代码逻辑假设该指针非空。结合告警描述，此模式属于少数未检查空值的情况，但切片中未显示有前置... |
| 305 | git-2.50.1 | update_one | cpp/inconsistent-null-check | 333 | FP | FP | 在调用 `find_subtree` 时，参数 `create` 被设置为 1，根据 `find_subtree` 函数的定义，当 `create` 为真时，函数会分配并返回一个新的子树节点，不会返回 NULL。因此，此处无需进行 N... |
| 306 | git-2.50.1 | verify_one_commit_graph | cpp/inconsistent-null-check | 2798 | FP | FP | 函数 `lookup_commit` 在切片中显示，当对象不存在时会调用 `create_object` 创建一个新的提交对象并返回，因此它不会返回 NULL。代码逻辑保证了指针的有效性，无需进行空指针检查。 |
| 307 | git-2.50.1 | unparse_commit | cpp/inconsistent-null-check | 189 | FP | FP | 切片代码显示，函数 `unparse_commit` 在调用 `lookup_commit` 后，直接访问 `c->object.parsed` 成员。根据 `lookup_commit` 的定义，它要么返回一个有效的 `struct... |
| 308 | git-2.50.1 | clear_common_flag | cpp/inconsistent-null-check | 2146 | FP | FP | 代码逻辑保证了 `lookup_object` 的返回值非空。`oid` 来源于 `oidset_iter_next`，该函数仅在集合中存在有效元素时才返回一个有效的 `oid`。`lookup_object` 函数在哈希表中查找该 ... |
| 309 | git-2.50.1 | deref_without_lazy_fetch | cpp/inconsistent-null-check | 156 | FP | FP | 告警点位于一个循环和条件分支内，其返回值被立即用于访问结构体成员（tag->tagged），这隐含了对指针非空的假设。结合上下文，该函数在调用 parse_object 前已通过 oid_object_info_extended 检查... |
| 310 | git-2.50.1 | find_merge_parents | cpp/inconsistent-null-check | 617 | FP | FP | `parse_object` 的返回值被立即传递给 `repo_peel_to_type`，后者在其内部循环中会检查 `parse_object` 的返回值是否为 NULL，并据此返回 NULL。随后，调用方代码检查 `parent`... |
| 311 | git-2.50.1 | get_parent | cpp/inconsistent-null-check | 1110 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将其返回值 `commit` 传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 函数会检查 `commit` 的有... |
| 312 | git-2.50.1 | show_ambiguous_object | cpp/inconsistent-null-check | 443 | FP | FP | 代码在调用 `lookup_tag` 后，立即将其结果 `tag` 传递给 `parse_tag(tag)` 进行解析和错误检查。`parse_tag` 函数内部会处理空指针或无效对象的情况并返回错误，因此即使 `lookup_tag... |
| 313 | git-2.50.1 | setup_pending_objects | cpp/inconsistent-null-check | 333 | FP | FP | 切片代码显示，在调用 `strmap_get` 获取 `root_tree_list` 后，后续代码（`oid_array_append(&root_tree_list->oids, &obj->oid)`）仅在 `root_tree... |
| 314 | git-2.50.1 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3351 | FP | FP | 被调用的函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到对象（`!ref->base`）的情况进行了处理，并明确返回 `NULL`。调用方未检查返回值，是因为后续逻辑（如循环遍历 `com... |
| 315 | git-2.50.1 | add_cache_tree | cpp/inconsistent-null-check | 1775 | FP | FP | 函数 `lookup_tree` 内部已处理空指针情况，当 `obj` 为空时会调用 `create_object` 返回一个有效的 `tree` 对象，因此调用后无需额外检查 `tree` 是否为 null。 |
| 316 | git-2.50.1 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 706 | FP | FP | 告警指出的 `lookup_commit` 调用未检查空值，但根据提供的 `lookup_commit` 函数定义，当对象不存在时会调用 `create_object` 创建并返回一个有效的 `commit` 对象，因此该函数本身设计... |
| 317 | git-2.50.1 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在内部已处理空对象指针，若 `obj` 为空则创建新对象并返回，因此调用者无需进行空指针检查。代码逻辑在切片内是安全的，属于工具误报。 |
| 318 | git-2.50.1 | has_uncommitted_changes | cpp/inconsistent-null-check | 2642 | FP | FP | `lookup_tree` 被调用时传入的是 `the_hash_algo->empty_tree`，这是一个已知的、有效的内置对象标识符，不可能返回 NULL。因此，此处不检查返回值是安全的，属于工具误报。 |
| 319 | git-2.50.1 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是字符串字面量 `DIGIT "abcdefABCDEF"`，其大小在编译时确定且大... |
| 320 | git-2.50.1 | test_ctype__ispunct | cpp/overflow-buffer | 91 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `len` 计算包含了 `ARRAY_SIZE(string) - 1`，但 `string` 是宏参数 `PUNCT`，其具体内容未知。然而，宏内使用了 `BUILD_AS... |
| 321 | git-2.50.1 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，但该表达式受 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)... |
| 322 | git-2.50.1 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏的调用参数 `string` 是一个字符串字面量，其 `ARRAY_SIZE` 结果大于0，因此 `... |
| 323 | git-2.50.1 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被调用时传入的字符串字面量 `"$()*+.?[\\^{｜"` 长度明确大于0，因此 `ARRAY_... |
| 324 | git-2.50.1 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但传入的字符串字面量 `"*?[\\"` 长度大于0，因此 `ARRAY_SIZE(string) - 1... |
| 325 | git-2.50.1 | test_ctype__isalnum | cpp/overflow-buffer | 51 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被 `TEST_CHAR_CLASS(isalnum, LOWER UPPER DIGIT)` 调用... |
| 326 | git-2.50.1 | test_ctype__isalpha | cpp/overflow-buffer | 46 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是宏参数 `LOWER UPPER`，它由字符字面量组成，`ARRAY_SIZE` ... |
| 327 | git-2.50.1 | test_ctype__isdigit | cpp/overflow-buffer | 41 | FP | FP | 宏定义 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在数组大小为0时可能产生负索引，但宏内包含 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0... |
| 328 | git-2.50.1 | <global> | cpp/overflow-buffer | 36 | FP | FP | 切片代码中仅包含一个空的函数定义，没有任何数组访问操作，因此告警所描述的访问负索引-1的情况在可见上下文中不存在。结合参考标签为FP，判断为误报。 |
| 329 | git-2.50.1 | add_patterns | cpp/invalid-pointer-deref | 1152 | FP | FP | 代码在分配内存时使用 `xmallocz(size)`，该函数分配 `size+1` 字节并清零，因此 `buf[size++] = '\n';` 的写入操作在分配的缓冲区范围内，是安全的。 |
| 330 | git-2.50.1 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1684 | FP | FP | 代码中 `buffer = xmallocz_gently(size)` 分配了 `size` 字节的内存，但随后 `stream.avail_out = size + 1` 和循环条件 `if (!stream.avail_out)... |
| 331 | git-2.50.1 | should_prune_worktree | cpp/invalid-pointer-deref | 965 | FP | FP | 切片代码显示，在写入 `path[len] = '\0';` 之前，存在一个 while 循环用于递减 `len` 以去除尾部的换行符。只要 `len` 在递减前大于 0（即文件大小大于 0），递减后的 `len` 将小于分配的缓冲区... |
| 332 | git-2.49.0 | is_command | cpp/redundant-null-check-simple | 2614 | FP | FP | 告警指出的空指针检查冗余，是针对变量 `nick` 的检查。在切片代码中，`nick` 是从结构体数组 `todo_command_info[command].c` 直接获取的字符，并非指针，因此工具将其误判为指针解引用。代码逻辑正确... |
| 333 | git-2.49.0 | refname_is_safe | cpp/no-space-for-terminator | 353 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，这是字符串 `rest` 的长度。根据 `strlen` 的语义，`restlen` 不包含字符串的终止空字符。然而，被调用的 `normalize_path_copy` ... |
| 334 | git-2.49.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 895 | FP | FP | 切片代码显示，在第一个while循环中，条件 `off < len - 1` 已对 `off` 进行了范围检查，确保在访问 `s[off]` 时 `off` 不会超过 `len` 的有效范围，因此不存在越界访问风险。 |
| 335 | git-2.49.0 | ce_write_entry | cpp/offset-use-before-range-check | 2689 | FP | FP | 变量 `common` 在 for 循环条件中已通过 `common < previous_name->len` 进行了范围检查，确保其不会超过 `previous_name->len`。后续使用 `ce->name + common... |
| 336 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在for循环条件 `s1[pos] == s2[pos] && pos < len` 中，对 `pos` 的访问 `s1[pos]` 和 `s2[pos]` 发生在 `pos < len` 的范围检查之前，这触发了规则告警。然而，该循... |
| 337 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 770 | FP | FP | 在切片代码的for循环条件中，'pos'的递增和边界检查's1[pos] == s2[pos] && pos < len'是同时进行的，这确保了在访问's1[pos]'和's2[pos]'之前，'pos'已经通过了'pos < len... |
| 338 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 在for循环条件 `pos < len` 中，变量 `pos` 的使用（`wcs1[pos] == wcs2[pos]`）发生在与 `len` 的范围检查之后，符合正确的顺序，因此不存在范围检查前使用的问题。 |
| 339 | git-2.49.0 | clar__assert_equal | cpp/offset-use-before-range-check | 806 | FP | FP | 在for循环条件`wcs1[pos] == wcs2[pos] && pos < len`中，对`pos`的访问`wcs1[pos]`和`wcs2[pos]`发生在范围检查`pos < len`之前，这违反了先检查后使用的安全原则。然... |
| 340 | git-2.49.0 | setup_scoreboard | cpp/inconsistent-null-check | 2858 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件为真的分支内，此时 `sb->final` 非空且其对象ID为空，`get_blame_suspects` 函数返回的指针 `o` 被直接解引... |
| 341 | git-2.49.0 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 告警点位于对 `branch_get` 返回值的空指针检查之后，代码在解引用 `branch->remote_name` 前已隐式假设 `branch` 非空。分析 `branch_get` 函数，当 `name` 为 NULL、空字... |
| 342 | git-2.49.0 | write_index_patch | cpp/inconsistent-null-check | 1433 | FP | FP | lookup_tree函数被调用时传入的是已知的、有效的空树对象ID（the_repository->hash_algo->empty_tree），该调用预期不会返回NULL。切片代码中后续对tree指针的使用（如add_pendin... |
| 343 | git-2.49.0 | bisect_successful | cpp/inconsistent-null-check | 648 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `refs_read_ref` 读取了引用并获取了对象ID，且后续使用 `commit->object.oid` 时未进行空指针检查，这表明... |
| 344 | git-2.49.0 | describe_commit | cpp/inconsistent-null-check | 326 | FP | FP | 切片代码显示，在调用 `lookup_commit_reference` 后，其返回值 `cmit` 被直接解引用（`&cmit->object.oid`），这通常需要空值检查。然而，`lookup_commit_reference`... |
| 345 | git-2.49.0 | <global> | cpp/inconsistent-null-check | 546 | FP | FP | 告警指出的 `lookup_tree` 调用位于 `add_head_to_pending` 失败后的回退路径中，其参数是已知的、固定的空树哈希值（`the_repository->hash_algo->empty_tree`），不可... |
| 346 | git-2.49.0 | do_fetch | cpp/inconsistent-null-check | 1756 | FP | FP | 切片代码中，`branch_get(NULL)` 的返回值 `branch` 在后续使用前，已通过 `branch_has_merge_config(branch)` 函数进行检查，该函数内部会验证 `branch` 是否为 NULL... |
| 347 | git-2.49.0 | get_ref_map | cpp/inconsistent-null-check | 551 | FP | FP | 代码中调用 branch_get(NULL) 后，其返回值 branch 被立即传递给 branch_has_merge_config 函数，该函数内部已包含对 branch 指针的 NULL 检查（`return branch &&... |
| 348 | git-2.49.0 | refspec_append_mapped | cpp/inconsistent-null-check | 92 | FP | FP | 告警点位于条件分支 `if (branch->merge_nr == 1 && branch->merge[0]->src)` 中，直接解引用 `branch->merge_nr` 和 `branch->merge[0]->src`。... |
| 349 | git-2.49.0 | do_create_stash | cpp/inconsistent-null-check | 1398 | FP | FP | 函数 `lookup_commit` 在失败时会返回一个新建的 `commit` 对象（见其定义），不会返回 NULL。因此，对它的返回值进行 NULL 检查是多余的，告警属于误报。 |
| 350 | git-2.49.0 | reset_tree | cpp/inconsistent-null-check | 287 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将返回值传递给 parse_tree 函数进行检查，如果解析失败会返回 -1，这相当于对返回的指针进行了有效性检查。因此，该告警是误报。 |
| 351 | git-2.49.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1932 | FP | FP | 告警点后代码立即使用 `sub->name`，若 `sub` 为 NULL 将导致段错误，但函数上下文（如 `die_message` 和 `BUG` 宏）表明程序在错误条件下会终止，且 `submodule_from_path` 内... |
| 352 | git-2.49.0 | update_one | cpp/inconsistent-null-check | 329 | FP | FP | 在调用 `find_subtree` 时，`create` 参数为 1，根据 `find_subtree` 函数的定义，当 `create` 为真时，函数会分配并返回一个新的 `cache_tree_sub` 结构体，不会返回 NUL... |
| 353 | git-2.49.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2788 | FP | FP | 函数 `lookup_commit` 在告警行被调用，其返回值 `graph_commit` 在后续代码中被直接使用（例如访问 `graph_commit->parents` 和传递给 `commit_graph_generation... |
| 354 | git-2.49.0 | unparse_commit | cpp/inconsistent-null-check | 188 | FP | FP | 切片代码显示，函数 `lookup_commit` 在内部已处理了空对象指针的情况（若 `obj` 为空则创建新对象），因此其返回值不会为空。调用方 `unparse_commit` 直接使用 `c->object.parsed` 是... |
| 355 | git-2.49.0 | clear_common_flag | cpp/inconsistent-null-check | 2147 | FP | FP | 代码逻辑保证了 `lookup_object` 的返回值非空。`oid` 来源于 `oidset_iter_next`，该函数仅在集合中存在有效条目时才返回一个有效的 `oid`。`lookup_object` 函数在哈希表中查找该 ... |
| 356 | git-2.49.0 | deref_without_lazy_fetch | cpp/inconsistent-null-check | 156 | FP | FP | 在调用 parse_object 之前，代码已通过 oid_object_info_extended 检查了对象类型，并确认其为 OBJ_TAG。对于标签对象，parse_object 预期返回有效指针，且后续代码直接访问 tag->... |
| 357 | git-2.49.0 | find_merge_parents | cpp/inconsistent-null-check | 617 | FP | FP | 切片代码显示，`parse_object` 返回的 `obj` 指针在后续被传递给 `add_merge_parent` 函数，该函数内部仅使用 `obj->oid` 字段。`parse_object` 函数定义表明它不会返回空指针，... |
| 358 | git-2.49.0 | get_parent | cpp/inconsistent-null-check | 1108 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将其返回值 `commit` 传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 函数会检查 `commit` 的有... |
| 359 | git-2.49.0 | show_ambiguous_object | cpp/inconsistent-null-check | 443 | FP | FP | 代码在调用 `lookup_tag` 后，立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析和验证。`parse_tag` 函数内部会检查 `tag` 的有效性（例如读取对象文件、验证类型），如果失败会返回... |
| 360 | git-2.49.0 | setup_pending_objects | cpp/inconsistent-null-check | 333 | FP | FP | 切片代码显示，在后续使用 `root_tree_list` 的 `else` 分支中，存在 `oid_array_append(&root_tree_list->oids, &obj->oid);` 调用，这要求 `root_tree... |
| 361 | git-2.49.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3357 | FP | FP | 被调用的函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到对象（`!ref->base`）的情况进行了处理并返回 NULL，调用方后续未使用其返回值进行关键操作（仅赋值给局部变量 `ts` ... |
| 362 | git-2.49.0 | add_cache_tree | cpp/inconsistent-null-check | 1783 | FP | FP | 被调用的 `lookup_tree` 函数内部已对空指针进行了检查，若 `obj` 为空会调用 `create_object` 返回一个有效的对象，因此调用方无需再次检查其返回值是否为空。 |
| 363 | git-2.49.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 703 | FP | FP | 根据提供的lookup_commit函数定义，当查找对象不存在时，函数会调用create_object创建一个新的对象并返回，因此该函数不会返回NULL。告警所提示的null检查缺失在此上下文中不构成问题。 |
| 364 | git-2.49.0 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在切片中显示，当 `lookup_object` 返回 NULL 时，它会调用 `create_object` 来分配并返回一个新的 commit 对象，因此该函数本身设计为永不返回 NULL。后... |
| 365 | git-2.49.0 | has_uncommitted_changes | cpp/inconsistent-null-check | 2642 | FP | FP | 告警点调用 `lookup_tree(r, the_hash_algo->empty_tree)` 获取空树对象，`the_hash_algo->empty_tree` 是预定义的常量 OID，不可能返回 NULL。切片中 `add_... |
| 366 | git-2.49.0 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是字符串字面量 `DIGIT "abcdefABCDEF"`，其大小固定且大于0，因... |
| 367 | git-2.49.0 | test_ctype__ispunct | cpp/overflow-buffer | 91 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)` 保... |
| 368 | git-2.49.0 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，但该表达式受 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)... |
| 369 | git-2.49.0 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被调用时的实参 `string` 是一个字符串字面量，其 `ARRAY_SIZE` 结果大于0，因此... |
| 370 | git-2.49.0 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被调用时传入的 `string` 是一个非空的字符串字面量 `"$()*+.?[\\^{｜"`，其 ... |
| 371 | git-2.49.0 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但传入的字符串字面量 `"*?[\\"` 长度大于0，因此 `ARRAY_SIZE(string) - 1... |
| 372 | git-2.49.0 | test_ctype__isalnum | cpp/overflow-buffer | 51 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，但该表达式受 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)... |
| 373 | git-2.49.0 | test_ctype__isalpha | cpp/overflow-buffer | 46 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏的调用参数 `string` 为 `LOWER UPPER`，这是一个字符串字面量，其 `ARRAY... |
| 374 | git-2.49.0 | test_ctype__isdigit | cpp/overflow-buffer | 41 | FP | FP | 切片代码显示，宏 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string) > 0` 时才会执行，且 `BUILD_ASSERT_OR_ZERO` 宏在数... |
| 375 | git-2.49.0 | <global> | cpp/overflow-buffer | 36 | FP | FP | 切片代码中仅包含一个空的函数定义，没有任何数组访问或可能导致负索引的操作，因此告警所描述的问题在可见代码中不存在。 |
| 376 | git-2.49.0 | add_patterns | cpp/invalid-pointer-deref | 1152 | FP | FP | 代码在分配缓冲区时使用 `xmallocz(size)`，该函数分配 `size+1` 字节并清零，因此 `buf[size] = '\n'` 的写入操作在分配的空间内，是安全的。告警误判了缓冲区边界。 |
| 377 | git-2.49.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1677 | FP | FP | 代码中 `buffer = xmallocz_gently(size)` 分配了 `size` 字节，随后 `stream.avail_out = size + 1` 和 `buffer[size] = '\0'` 表明分配时已为末尾... |
| 378 | git-2.49.0 | should_prune_worktree | cpp/invalid-pointer-deref | 960 | FP | FP | 指针 'path' 通过 xmallocz(len) 分配，大小为 len 字节，而写入操作 path[len] = '\0' 是在 while 循环将 len 递减至最后一个非换行符字符之后执行的，因此写入位置始终在分配的内存边界内... |
| 379 | git-2.46.0 | is_command | cpp/redundant-null-check-simple | 2601 | FP | FP | 告警指出的空指针检查冗余，但代码中变量 `nick` 是字符类型而非指针，其值 `todo_command_info[command].c` 可能为 `'\0'`，逻辑表达式 `(nick && *p++ == nick)` 中的 `... |
| 380 | git-2.46.0 | refname_is_safe | cpp/no-space-for-terminator | 345 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，而 `restlen` 是 `strlen(rest)` 的结果，不包含终止符的长度。但 `normalize_path_copy` 函数要求目标缓冲区足够容纳源字符串及其... |
| 381 | git-2.46.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 890 | FP | FP | 切片代码显示，在第一个while循环中，条件 `off < len - 1` 已对 `off` 进行了范围检查，确保在访问 `s[off]` 时不会越界。因此，该告警为误报。 |
| 382 | git-2.46.0 | ce_write_entry | cpp/offset-use-before-range-check | 2685 | FP | FP | 变量 `common` 在 for 循环条件中已通过 `common < previous_name->len` 进行了范围检查，确保其不会超过 `previous_name->len`。后续使用 `ce->name + common... |
| 383 | git-2.46.0 | setup_scoreboard | cpp/inconsistent-null-check | 2857 | FP | FP | 告警点位于 `is_null_oid(&sb->final->object.oid)` 条件分支内，该条件已确保 `sb->final` 非空且其 OID 为空，此时调用 `get_blame_suspects` 返回 NULL 是预... |
| 384 | git-2.46.0 | inherit_tracking | cpp/inconsistent-null-check | 226 | FP | FP | 被调用的函数 `branch_get` 在传入空名或 "HEAD" 时会返回 `the_repository->remote_state->current_branch`，否则会调用 `make_branch` 创建或查找分支，但该函... |
| 385 | git-2.46.0 | bisect_successful | cpp/inconsistent-null-check | 644 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `refs_read_ref` 检查了 `bad_ref` 是否存在，这确保了后续查找的引用是有效的。切片代码中可见的防护逻辑表明，即使 `... |
| 386 | git-2.46.0 | update_head | cpp/inconsistent-null-check | 684 | FP | FP | 代码中 `refs_update_ref` 调用时指定了 `UPDATE_REFS_DIE_ON_ERR` 标志，若 `lookup_commit_reference` 返回 NULL 导致后续 `c->object.oid` 解引用... |
| 387 | git-2.46.0 | describe_commit | cpp/inconsistent-null-check | 323 | FP | FP | 在切片代码中，`lookup_commit_reference` 返回的指针 `cmit` 在后续代码中被直接解引用（如 `cmit->object.oid`），但该函数在给定无效对象ID时会返回NULL。然而，调用函数 `descr... |
| 388 | git-2.46.0 | do_fetch | cpp/inconsistent-null-check | 1626 | FP | FP | 代码在调用 `branch_has_merge_config(branch)` 前已对 `branch` 指针进行了隐式检查，该函数内部也包含空指针检查（`return branch && !!branch->merge;`），因此即... |
| 389 | git-2.46.0 | get_ref_map | cpp/inconsistent-null-check | 551 | FP | FP | 代码中调用 `branch_get(NULL)` 后，其返回值 `branch` 被直接传递给 `branch_has_merge_config` 函数。该函数内部已包含对 `branch` 指针的显式空值检查（`return bra... |
| 390 | git-2.46.0 | refspec_append_mapped | cpp/inconsistent-null-check | 88 | FP | FP | 被调用的 `branch_get` 函数在输入为 NULL 或空字符串时会返回 `the_repository->remote_state->current_branch`，该指针在代码上下文中应为有效值，且后续访问 `branch-... |
| 391 | git-2.46.0 | do_create_stash | cpp/inconsistent-null-check | 1388 | FP | FP | 切片代码显示 `head_commit` 在后续多处被直接使用（如 `head_commit->object.oid`），未进行空指针检查，这可能导致程序崩溃。然而，参考标签 `label` 为 FP，表明该问题在后续版本中未被修复，... |
| 392 | git-2.46.0 | reset_tree | cpp/inconsistent-null-check | 283 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将结果传递给 parse_tree 函数进行检查，该检查会处理可能的错误（如返回 -1），这相当于对返回的指针进行了间接验证。因此，告警指出的空指针检查缺失是误报。 |
| 393 | git-2.46.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1900 | FP | FP | 告警点后的代码直接使用了 `sub->name`，这表明 `sub` 指针被假定为非空。结合 `submodule_from_path` 的函数定义，它返回一个指向 `const struct submodule` 的指针，且没有显式... |
| 394 | git-2.46.0 | write_bundle_refs | cpp/inconsistent-null-check | 430 | FP | FP | 在调用 `lookup_commit_reference` 后，代码立即通过 `e->item == &(one->object)` 访问了 `one->object` 成员，这隐含地假设了 `one` 非空。结合 `label` 为... |
| 395 | git-2.46.0 | update_one | cpp/inconsistent-null-check | 327 | FP | FP | 在调用 `find_subtree` 时，`create` 参数为 1，根据函数定义，当 `create` 为真时，函数会分配并返回一个新的子树节点，不会返回 NULL。因此，此处无需进行 NULL 检查，告警为误报。 |
| 396 | git-2.46.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2774 | FP | FP | 函数 `lookup_commit` 在切片中被调用两次，其返回值 `graph_commit` 在后续代码中直接用于指针解引用（如 `graph_commit->parents`），这表明代码逻辑假设该调用总是返回有效的非空指针。结... |
| 397 | git-2.46.0 | ahead_behind | cpp/inconsistent-null-check | 1069 | FP | FP | 函数 `prio_queue_get` 在队列为空时返回 NULL，但调用点位于 `while (queue_has_nonstale(&queue))` 循环内，该循环条件已确保队列中存在非 STALE 的提交，因此 `prio_q... |
| 398 | git-2.46.0 | paint_down_to_common | cpp/inconsistent-null-check | 81 | FP | FP | 函数 `queue_has_nonstale` 确保队列非空时才进入循环，且 `prio_queue_get` 内部在 `queue->nr` 为0时返回NULL，但调用点 `commit = prio_queue_get(&queu... |
| 399 | git-2.46.0 | unparse_commit | cpp/inconsistent-null-check | 182 | FP | FP | 函数 `lookup_commit` 内部已处理了 `lookup_object` 返回 `NULL` 的情况，会创建新对象并返回，因此其返回值不会为 `NULL`。调用后直接使用 `c->object.parsed` 是安全的，无需... |
| 400 | git-2.46.0 | clear_common_flag | cpp/inconsistent-null-check | 2130 | FP | FP | 代码逻辑保证了 `lookup_object` 的输入 `oid` 来自 `oidset_iter_next`，该迭代器仅在集合中存在有效对象ID时才返回非空指针。因此，在循环体内 `oid` 非空，`lookup_object` 返... |
| 401 | git-2.46.0 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 143 | FP | FP | 告警点位于一个无限循环中，其前置条件 `if (*type == OBJ_TAG)` 已确保 `parse_object` 的返回值 `tag` 在后续 `if (!tag->tagged)` 中被检查和使用。代码逻辑表明，如果 `p... |
| 402 | git-2.46.0 | find_merge_parents | cpp/inconsistent-null-check | 616 | FP | FP | 告警点 `obj = parse_object(...)` 的返回值 `obj` 在后续代码中直接传递给 `add_merge_parent` 函数使用其 `obj->oid` 成员，这表明 `obj` 被假定为非空。切片中 `par... |
| 404 | git-2.46.0 | get_parent | cpp/inconsistent-null-check | 1098 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将其返回值 `commit` 传递给 `repo_parse_commit` 进行解析。`repo_parse_commit` 函数会检查 `commit` 的有... |
| 405 | git-2.46.0 | show_ambiguous_object | cpp/inconsistent-null-check | 436 | FP | FP | 代码在调用 `lookup_tag` 后，立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析和校验。`parse_tag` 函数内部会检查 `tag` 的有效性（例如读取对象文件、验证类型），如果 `tag... |
| 407 | git-2.46.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3339 | FP | FP | 被调用的函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到项（`!ref->base`）的情况进行了处理并返回 NULL，调用方后续未使用其返回值进行关键操作（如解引用），因此该告警为误报。 |
| 408 | git-2.46.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 690 | FP | FP | 切片代码显示，`lookup_commit` 函数内部已处理空对象指针的情况（若 `obj` 为空则创建新对象），因此调用处不检查空指针是安全的。该告警属于工具对代码模式的误判。 |
| 409 | git-2.46.0 | <global> | cpp/inconsistent-null-check | 29 | FP | FP | 函数 `lookup_commit` 在内部已处理空对象指针，若 `lookup_object` 返回 NULL，会调用 `create_object` 创建新对象，因此调用者无需额外检查 NULL。代码逻辑在切片内是安全的。 |
| 420 | git-2.46.0 | add_patterns | cpp/invalid-pointer-deref | 1150 | FP | FP | 代码在分配内存时使用 `xmallocz(size)`，该函数分配 `size+1` 字节并清零，因此 `buf[size] = '\n'` 的写入操作在分配的内存边界内，是安全的。告警源于工具未识别 `xmallocz` 的语义。 |
| 421 | git-2.46.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1649 | FP | FP | 代码中 `buffer = xmallocz_gently(size);` 分配了 `size+1` 字节的内存，而 `stream.avail_out = size + 1;` 确保了 `git_inflate` 最多写入 `siz... |
| 422 | git-2.46.0 | should_prune_worktree | cpp/invalid-pointer-deref | 788 | FP | FP | 代码在写入 `path[len] = '\0';` 前，通过 `while` 循环确保了 `len` 已递减至最后一个非换行符字符的位置，因此写入操作在已分配的缓冲区 `path` 范围内，不会发生越界。算法标签 `FP` 与此分析一致。 |
| 423 | git-2.44.0 | is_command | cpp/redundant-null-check-simple | 2522 | FP | FP | 告警指出的冗余空值检查是针对变量 `nick`，该变量是从结构体数组 `todo_command_info` 中直接读取的字符成员，并非指针，因此对其进行的空值检查 `(nick && ...)` 在逻辑上是有效的，并非冗余。工具可能... |
| 424 | git-2.44.0 | refname_is_safe | cpp/no-space-for-terminator | 342 | FP | FP | 函数 `xmallocz` 的调用参数为 `restlen`，即字符串 `rest` 的长度。根据 `normalize_path_copy` 函数的语义，它要求目标缓冲区足够容纳源字符串及其空终止符。由于 `rest` 是一个以空字... |
| 425 | git-2.44.0 | fill_es_indent_data | cpp/offset-use-before-range-check | 869 | FP | FP | 在第一个while循环的条件中，访问`s[off]`之前已经通过`off < len - 1`检查了偏移量`off`的范围，确保了访问不会越界。切片代码中可见的防护逻辑表明该告警为误报。 |
| 426 | git-2.44.0 | ce_write_entry | cpp/offset-use-before-range-check | 2713 | FP | FP | 变量 `common` 在 for 循环条件中已通过 `common < previous_name->len` 进行了范围检查，确保其不会超过 `previous_name->len`。后续使用 `ce->name + common... |
| 427 | git-2.44.0 | setup_scoreboard | cpp/inconsistent-null-check | 2855 | FP | FP | 函数 get_blame_suspects 的定义显示它可能返回 NULL，但调用点位于 `if (is_null_oid(&sb->final->object.oid))` 条件块内，该条件确保 `sb->final` 是一个有效的... |
| 428 | git-2.44.0 | inherit_tracking | cpp/inconsistent-null-check | 224 | FP | FP | 被调用的函数 `branch_get` 在传入空名或 "HEAD" 时返回 `the_repository->remote_state->current_branch`，否则通过 `make_branch` 创建新分支结构体，两种路径... |
| 429 | git-2.44.0 | bisect_successful | cpp/inconsistent-null-check | 640 | FP | FP | 在调用 `lookup_commit_reference_by_name` 之前，代码已通过 `read_ref(bad_ref, &oid)` 读取了引用，如果引用不存在，`read_ref` 会失败并导致 `oid` 无效，但后续... |
| 430 | git-2.44.0 | update_head | cpp/inconsistent-null-check | 648 | FP | FP | 告警点调用的 `lookup_commit_reference` 返回的指针 `c` 被直接传递给 `update_ref` 函数，而 `update_ref` 的 `onerr` 参数为 `UPDATE_REFS_DIE_ON_ER... |
| 431 | git-2.44.0 | describe_commit | cpp/inconsistent-null-check | 320 | FP | FP | 函数 `lookup_commit_reference` 在内部调用 `lookup_commit_reference_gently`，后者在对象不存在时返回 NULL。然而，在切片代码中，`describe_commit` 函数的参... |
| 432 | git-2.44.0 | do_fetch | cpp/inconsistent-null-check | 1611 | FP | FP | 代码在调用 `branch_get(NULL)` 后，立即在 `if (branch_has_merge_config(branch) && ...)` 条件中使用了 `branch` 指针。`branch_has_merge_con... |
| 433 | git-2.44.0 | get_ref_map | cpp/inconsistent-null-check | 550 | FP | FP | 告警点调用 `branch_get(NULL)`，其返回值 `branch` 在后续使用前，已通过 `branch_has_merge_config(branch)` 函数进行显式检查，该函数内部会验证 `branch` 是否为 NU... |
| 434 | git-2.44.0 | cmd_merge | cpp/inconsistent-null-check | 1638 | FP | FP | 切片代码显示，在调用 `repo_get_merge_bases` 后，其返回值 `common_one` 被直接用于访问 `common_one->item`，但在此之前，代码逻辑（如 `if (!remoteheads->next... |
| 435 | git-2.44.0 | refspec_append_mapped | cpp/inconsistent-null-check | 88 | FP | FP | 被调用的函数 `branch_get` 在输入为 NULL 或空字符串时会返回 `the_repository->remote_state->current_branch`，该返回值是一个有效的结构体指针，并非 NULL。因此，在调用... |
| 436 | git-2.44.0 | do_create_stash | cpp/inconsistent-null-check | 1378 | FP | FP | 切片代码显示 `lookup_commit` 返回的 `head_commit` 指针在后续被直接解引用（如 `head_commit->object.oid`），这表明代码逻辑假设该调用不会返回 NULL。结合告警规则是关于不一致的... |
| 437 | git-2.44.0 | reset_tree | cpp/inconsistent-null-check | 283 | FP | FP | 代码在调用 parse_tree_indirect 后，立即将结果传递给 parse_tree 函数进行检查，如果 parse_tree 失败会返回 -1，这间接验证了 tree 指针的有效性。此外，后续代码 tree->buffer... |
| 438 | git-2.44.0 | determine_submodule_update_strategy | cpp/inconsistent-null-check | 1838 | FP | FP | 切片代码中，在调用 `submodule_from_path` 获取 `sub` 后，立即使用 `sub->name` 进行字符串格式化，这表明代码逻辑假设 `sub` 非空。结合告警描述，该检查缺失属于代码风格或特定上下文下的安全假... |
| 439 | git-2.44.0 | write_bundle_refs | cpp/inconsistent-null-check | 428 | FP | FP | 在调用 `lookup_commit_reference` 后，其返回值 `one` 被直接用于 `e->item == &(one->object)` 的比较。如果 `lookup_commit_reference` 返回 NULL... |
| 440 | git-2.44.0 | update_one | cpp/inconsistent-null-check | 325 | FP | FP | 在调用 `find_subtree` 时，`create` 参数为 1，根据函数定义，当 `create` 为真时，函数会分配并返回一个新的 `cache_tree_sub` 结构体，不会返回 NULL。因此，此处无需进行空指针检查，... |
| 441 | git-2.44.0 | verify_one_commit_graph | cpp/inconsistent-null-check | 2722 | FP | FP | 代码中 `lookup_commit` 的返回值 `graph_commit` 在后续使用前，已通过 `parse_commit_in_graph_one` 或 `repo_parse_commit_internal` 等函数进行了解... |
| 442 | git-2.44.0 | ahead_behind | cpp/inconsistent-null-check | 1010 | FP | FP | 函数 `queue_has_nonstale` 在循环前已检查队列中是否存在非 STALE 的提交，确保 `prio_queue_get` 被调用时队列非空。`prio_queue_get` 函数内部也有 `if (!queue->n... |
| 443 | git-2.44.0 | paint_down_to_common | cpp/inconsistent-null-check | 78 | FP | FP | 函数 `prio_queue_get` 在队列为空时返回 NULL，但调用点位于 `while (queue_has_nonstale(&queue))` 循环内，该循环条件已确保队列中至少存在一个非 STALE 的提交，因此 `pr... |
| 444 | git-2.44.0 | unparse_commit | cpp/inconsistent-null-check | 179 | FP | FP | 切片代码显示，函数 `lookup_commit` 在未找到对象时会调用 `create_object` 创建一个新的对象并返回，因此它不会返回 NULL。后续代码直接访问 `c->object.parsed` 是安全的，告警为误报。 |
| 445 | git-2.44.0 | clear_common_flag | cpp/inconsistent-null-check | 2124 | FP | FP | 代码逻辑保证了 `lookup_object` 的返回值非空。`oid` 来源于 `oidset_iter_next`，该迭代器仅在集合中存在有效元素时才返回一个 `object_id` 指针，且 `lookup_object` 函数... |
| 446 | git-2.44.0 | deref_without_lazy_fetch_extended | cpp/inconsistent-null-check | 141 | FP | FP | 告警点 `parse_object` 的返回值被赋值给 `tag` 指针，随后代码立即检查 `tag->tagged` 是否为 NULL，这隐含了对 `tag` 指针非空的假设。虽然未显式检查 `parse_object` 是否返回 ... |
| 447 | git-2.44.0 | find_merge_parents | cpp/inconsistent-null-check | 614 | FP | FP | 切片代码显示，`parse_object` 返回的 `obj` 指针在后续被传递给 `add_merge_parent` 函数，该函数内部仅使用 `obj->oid` 字段。`parse_object` 函数定义表明它可能返回 NUL... |
| 448 | git-2.44.0 | get_rev | cpp/inconsistent-null-check | 187 | FP | FP | 在调用 `prio_queue_get` 后，代码立即通过 `entry->commit` 访问其成员，这隐含了对 `entry` 非空的假设。结合 `prio_queue_get` 的实现，当队列为空时返回 NULL，但调用点前的 ... |
| 449 | git-2.44.0 | get_parent | cpp/inconsistent-null-check | 1063 | FP | FP | 代码在调用 `lookup_commit_reference` 后，立即将其结果 `commit` 传递给 `repo_parse_commit` 进行校验；若 `commit` 为 NULL，`repo_parse_commit` ... |
| 450 | git-2.44.0 | show_ambiguous_object | cpp/inconsistent-null-check | 422 | FP | FP | 代码在调用 `lookup_tag` 后，立即将其返回值 `tag` 传递给 `parse_tag(tag)` 进行解析和检查。`parse_tag` 函数内部会处理 `tag` 为 NULL 或无效的情况并返回错误，且后续的 `if... |
| 451 | git-2.44.0 | fill_bitmap_commit | cpp/inconsistent-null-check | 416 | FP | FP | 代码中while循环的条件是`queue->nr`（元素数量），`prio_queue_get`函数内部已检查此条件并在队列为空时返回NULL。因此，在循环内部调用`prio_queue_get`时，`queue->nr`保证大于0，... |
| 452 | git-2.44.0 | leave_one_treesame_to_parent | cpp/inconsistent-null-check | 3256 | FP | FP | 被调用的函数 `lookup_decoration` 在内部已对空指针（`!n->size`）和未找到项（`!ref->base`）的情况进行了处理并返回 NULL，调用方未检查返回值是合理的，因为后续循环逻辑不依赖该指针。 |
| 453 | git-2.44.0 | assign_shallow_commits_to_refs | cpp/inconsistent-null-check | 686 | FP | FP | 切片代码显示，`lookup_commit`函数内部已对`lookup_object`的返回值进行了空指针检查，若为空则创建新对象，因此函数本身保证了不会返回空指针给调用者。告警所提示的调用点无需额外检查。 |
| 454 | git-2.44.0 | <global> | cpp/inconsistent-null-check | 27 | FP | FP | 该告警针对的是未对 `lookup_commit` 的返回值进行空指针检查。然而，在切片代码中，`c` 被直接用于访问 `c->date` 和 `c->parents`，这表明代码逻辑假设 `lookup_commit` 总是成功。结... |
| 455 | git-2.44.0 | test_ctype_isxdigit | cpp/overflow-buffer | 59 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 的循环中，该循环明确限定 `i` 的范围为 `0` 到 `255`，因此不会访问索引 `-1`。对 `EOF` 的调用是函数调用，不是数组索引，不构成缓冲区溢出。切片代... |
| 456 | git-2.44.0 | test_ctype_ispunct | cpp/overflow-buffer | 58 | FP | FP | 切片代码显示，循环索引 i 的范围是 0 到 255，用于测试字符分类函数。对 EOF（值为 -1）的调用是函数 `func(EOF)` 的参数，并非数组索引操作。告警误将函数参数识别为数组负索引。 |
| 457 | git-2.44.0 | test_ctype_iscntrl | cpp/overflow-buffer | 57 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 的循环中，循环变量 `i` 的范围是 0 到 255，因此不会出现负索引。对 `EOF` 的调用是 `func(EOF)`，并非数组索引操作，是安全的。代码逻辑本身无误... |
| 458 | git-2.44.0 | test_ctype_is_pathspec_magic | cpp/overflow-buffer | 53 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 的 `func(EOF)` 调用中，其中 `EOF` 为 -1。该宏是测试框架的一部分，用于验证函数 `func` 对边界输入 `EOF` 的处理，属于受控的测试逻辑，... |
| 459 | git-2.44.0 | test_ctype_is_regex_special | cpp/overflow-buffer | 52 | FP | FP | 切片代码显示，宏 `TEST_CTYPE_FUNC` 中的循环索引 `i` 范围是 0 到 255，且对 `EOF` 的调用 `func(EOF)` 有显式检查 `!func(EOF)`，这确保了函数 `func` 在参数为 `EOF... |
| 460 | git-2.44.0 | test_ctype_is_glob_special | cpp/overflow-buffer | 51 | FP | FP | 切片代码显示，宏 `TEST_CTYPE_FUNC` 中的循环索引 `i` 范围固定为 0 到 255，且对 `EOF` 的调用是显式检查 `func(EOF)`，并非通过数组索引访问。告警所指的负索引 -1 可能源于工具对 `EOF... |
| 461 | git-2.44.0 | test_ctype_isalnum | cpp/overflow-buffer | 50 | FP | FP | 代码切片显示告警位于宏定义 `TEST_CTYPE_FUNC(isalnum, LOWER UPPER DIGIT)` 的展开处，该宏内部循环索引 `i` 的范围为 0 到 255，并专门处理了 `EOF`（通常为 -1）作为边界情况... |
| 462 | git-2.44.0 | test_ctype_isalpha | cpp/overflow-buffer | 49 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 的展开中，用于检查 `func(EOF)`，其中 `EOF` 通常定义为 -1。这是对字符分类函数（如 `isalpha`）输入边界值的合法测试，旨在验证函数对无效输入... |
| 463 | git-2.44.0 | test_ctype_isspace | cpp/overflow-buffer | 48 | FP | FP | 告警指出的负索引访问发生在宏 `TEST_CTYPE_FUNC` 对 `func(EOF)` 的调用中，其中 `EOF` 通常定义为 -1。然而，`func` 参数（如 `isspace`）是字符分类函数，其标准定义明确接受 `int... |
| 464 | git-2.44.0 | test_ctype_isdigit | cpp/overflow-buffer | 47 | FP | FP | 切片代码显示，宏 `TEST_CTYPE_FUNC` 中的循环索引 `i` 范围是 0 到 255，且对 `EOF` 的调用是 `func(EOF)` 而非数组索引。告警所指的负索引 `-1` 可能源于工具对 `EOF` 值（通常为 ... |
| 465 | git-2.44.0 | add_patterns | cpp/invalid-pointer-deref | 1117 | FP | FP | 代码在分配缓冲区时使用了 `xmallocz(size)`，该函数分配了 `size+1` 字节并清零，为追加的换行符预留了空间。因此，`buf[size++] = '\n';` 的写入操作在分配的内存边界内，是安全的。 |
| 466 | git-2.44.0 | unpack_compressed_entry | cpp/invalid-pointer-deref | 1647 | FP | FP | 代码中 `buffer = xmallocz_gently(size);` 分配了 `size+1` 字节的内存，而 `stream.avail_out = size + 1;` 确保了 `git_inflate` 最多写入 `siz... |
| 467 | git-2.44.0 | should_prune_worktree | cpp/invalid-pointer-deref | 791 | FP | FP | 代码在写入 `path[len] = '\0';` 前，通过 `while` 循环确保了 `len` 大于0且 `path[len - 1]` 是有效字符，因此 `len` 是缓冲区 `path` 内的有效索引，不会发生越界写入。 |
| 468 | curl-8_13_0 | <global> | cpp/invalid-pointer-deref | 89 | FP | FP | 代码在写入 `newname[len]` 前已通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen = len + 13`，确保了 `len` 索引位置在分配的内存范围内，因此该写入操作是安全的。 |
| 469 | curl-8_15_0 | <global> | cpp/invalid-pointer-deref | 85 | FP | FP | 代码在 `newname[len] = '.';` 处写入点号，`newname` 已通过 `malloc(newlen)` 分配，其中 `newlen = len + 13`，因此 `newname[len]` 是分配内存内的有效位... |
| 471 | curl-8_9_1 | <global> | cpp/invalid-pointer-deref | 96 | FP | FP | 代码在 `newname[len] = '.';` 处写入前，已通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen` 的计算为 `len + 13`，确保了写入位置 `len` 在分配的内存边界 `newl... |
| 472 | curl-8_7_1 | Curl_splayremove | cpp/inconsistent-null-check | 270 | FP | FP | 在切片代码中，调用 `Curl_splay` 的结果被赋值给变量 `x` 并随后被用作新的根节点，但此处的 `x` 在赋值前已通过条件分支确保其不为空（例如，当 `t->smaller` 为空时，`x` 被赋值为 `t->larger... |
| 473 | curl-8_7_1 | <global> | cpp/invalid-pointer-deref | 96 | FP | FP | 代码在写入 `newname[len]` 前已通过 `malloc(newlen)` 分配了足够的内存，其中 `newlen = len + 13`，确保了 `len` 索引位置在分配的内存范围内，因此该写入操作是安全的。 |
| 474 | curl-8_11_1 | <global> | cpp/invalid-pointer-deref | 91 | FP | FP | 代码中 `newname[len] = '.';` 的写入操作是安全的。`newname` 通过 `malloc(newlen)` 分配，其中 `newlen = len + 13`，确保了 `newname` 的有效索引范围是 `[... |
| 475 | nginx-1.27.2 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 切片代码中明确包含注释说明'/* the array has 4 empty preallocated elements, so push cannot fail */'，表明在调用ngx_array_push时，数组有预分配的空元素... |
| 476 | nginx-1.29.0 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3565 | FP | FP | 切片代码中的注释明确指出，数组有4个预分配的空元素，因此push操作不会失败，无需检查NULL。代码逻辑保证了安全性，属于工具误报。 |
| 477 | nginx-1.27.4 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3521 | FP | FP | 切片代码中包含明确的注释和逻辑表明，在调用 ngx_array_push 时，数组 conf->server_names 已预分配了4个空元素且当前元素数量为0，因此该次调用不会失败，无需检查返回值。这与工具报告的“不一致的空指针检查... |
| 478 | nginx-1.25.4 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 切片代码中的注释明确指出数组有4个预分配的空元素，因此push操作不会失败，无需检查null。代码逻辑保证了安全性，属于工具误报。 |
| 479 | nginx-1.27.0 | ngx_http_core_merge_srv_conf | cpp/inconsistent-null-check | 3514 | FP | FP | 切片代码中明确注释说明数组有4个预分配的空元素，因此ngx_array_push调用不会失败，无需进行空指针检查。代码逻辑保证了安全性，属于工具误报。 |
| 480 | vim-9.1.0550 | <global> | cpp/redundant-null-check-simple | 3494 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 指针在解引用前已通过 `if (*inc_opt != NUL)` 进行了有效性检查，这确保了指针非空。因此，后续的 `strstr((ch... |
| 481 | vim-9.1.0550 | <global> | cpp/redundant-null-check-simple | 3576 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，解引用发生在条件分支内（如 `if (inc_opt != NULL && strstr(...) != NULL)`），而空指针检查（`if (inc_opt... |
| 482 | vim-9.1.0550 | findmatchlimit | cpp/offset-use-before-range-check | 2522 | FP | FP | 告警点位于 `linep[pos.col] == '*' && linep[pos.col + 1] == '/'` 条件判断中，访问 `linep[pos.col + 1]`。切片代码显示，在进入该条件分支前，存在对 `pos.co... |
| 483 | vim-9.1.0550 | common_function | cpp/inconsistent-null-check | 4856 | FP | FP | 代码在调用 `vim_strsave` 后，其返回值 `name` 被立即用于 `func_ref(name)` 或作为返回值的一部分，而 `func_ref` 函数内部已包含对 `name` 为 NULL 的检查（`if (name... |
| 484 | vim-9.1.0550 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | FP | 函数 `vterm_screen_is_eol` 的循环条件 `pos.col < screen->cols` 确保了 `pos.col` 在有效列范围内，结合 `getcell` 函数内部对行列的边界检查，可以推断在循环内调用 `g... |
| 485 | vim-9.1.0550 | get_isolated_shell_name | cpp/inconsistent-null-check | 2695 | FP | FP | 函数 `vim_strsave` 内部已对 `alloc` 的返回值进行了 `NULL` 检查，若分配失败则返回 `NULL`，调用者 `get_isolated_shell_name` 直接返回该值，由上层调用者负责处理。告警是工具... |
| 486 | vim-9.1.0550 | get_isolated_shell_name | cpp/inconsistent-null-check | 2706 | FP | FP | 函数 `vim_strnsave` 和 `vim_strsave` 在分配内存失败时返回 NULL，但调用函数 `get_isolated_shell_name` 的返回值被上层调用者使用，切片中未显示上层有 NULL 检查。然而，该... |
| 487 | vim-9.1.0550 | did_set_cryptmethod | cpp/inconsistent-null-check | 1766 | FP | FP | 函数 `vim_strsave` 内部已调用 `alloc` 并检查返回值，若分配失败则返回 NULL。调用方 `did_set_cryptmethod` 将返回值赋给全局变量 `p_cm`，后续使用前有检查 `*p_cm == NU... |
| 488 | vim-9.1.0550 | did_set_background | cpp/inconsistent-null-check | 1079 | FP | FP | 告警点位于条件分支内，且紧随其后调用了 `check_string_option(&p_bg);`，该函数明确处理了 `p_bg` 为 NULL 的情况（将其设置为 `empty_option`），因此存在有效的空指针防护机制，使得告... |
| 489 | vim-9.1.0550 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 告警点`find_win_by_nr_or_id`的返回值在下一行立即被`win_valid_any_tab`函数检查，该函数内部已包含对NULL指针的校验，因此存在有效的空值防护，属于工具误报。 |
| 490 | vim-9.1.0550 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 告警指出对regnext的调用未检查null，但切片代码显示在多个地方（如regnext函数定义和调用上下文）已通过条件判断确保scan不为NULL，且该函数在scan为NULL时返回NULL，调用后未立即使用其结果，后续逻辑会处理N... |
| 491 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 告警点 `br = regnode(BRANCH);` 的返回值 `br` 在后续代码中仅用于赋值和条件判断，并未解引用或用于可能导致崩溃的操作。切片中未显示对 `regnode` 返回值的空指针有安全性依赖，且 `label` 为 ... |
| 492 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 代码中 `regnode` 的返回值 `br` 被用于 `regtail` 调用，但 `regtail` 函数内部会检查其第一个参数是否为 `JUST_CALC_SIZE`，如果是则直接返回，不会解引用。切片中 `ret != JUS... |
| 493 | vim-9.1.0550 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在切片代码中，对 `regnext` 的调用位于一个循环内，该循环在 `ret != JUST_CALC_SIZE` 的条件下执行，并且循环体内部有 `if (reg_toolong) return NULL;` 的检查。`regne... |
| 494 | vim-9.1.0550 | win_redr_custom | cpp/inconsistent-null-check | 1115 | FP | FP | 代码在调用 vim_strsave 后立即将返回值传递给 vim_free 进行释放，表明内存管理是正确且完整的，不存在空指针解引用风险。告警仅基于统计模式（85%的调用检查空值），但当前上下文显示返回值被安全处理。 |
| 495 | vim-9.1.0550 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 在告警行之后，代码在 `#ifdef SPELL_PRINTTREE` 块中检查了 `n != NULL`，这表明代码逻辑已考虑空指针情况。此外，`getroom` 函数在内存分配失败时会返回 NULL，但调用点 `spin->si_... |
| 496 | vim-9.1.0550 | do_tag | cpp/inconsistent-null-check | 639 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 被立即赋值给 `tofree`，随后 `tofree` 在函数末尾通过 `vim_free(tofree)` 被释放。这表明代码逻辑已妥善处理了潜在的 NULL 返回值... |
| 497 | vim-9.1.0550 | define_function | cpp/inconsistent-null-check | 5306 | FP | FP | 代码中 `vim_strchr(p, '(')` 的返回值仅用于条件判断 `!= NULL`，未直接解引用，因此空指针检查缺失不构成安全风险。该告警属于编码风格不一致的误报。 |
| 498 | vim-9.1.0550 | is_duplicate_variable | cpp/inconsistent-null-check | 909 | FP | FP | 提供的切片代码中，函数 `is_duplicate_variable` 的函数体为空，未包含对 `vim_strnsave` 的调用，因此无法确认存在未检查返回值的空指针风险。结合参考标签为 FP，倾向于判定为误报。 |
| 499 | vim-9.1.0550 | exec_instructions | cpp/inconsistent-null-check | 3257 | FP | FP | alloc_clear 函数内部已调用 lalloc 并检查返回值是否为 NULL，若为 NULL 则返回 NULL，后续代码中 tv->vval.v_object 的访问均通过指针判断进行防护，例如在 ISN_GET_OBJ_MEM... |
| 500 | vim-9.1.0550 | barline_parse | cpp/inconsistent-null-check | 1122 | FP | FP | 告警点 `s = vim_strsave(s);` 的返回值被赋值给 `value->bv_string`，但切片代码显示，当 `s != buf && allocated && !converted` 条件成立时，`value->b... |
| 501 | vim-9.1.0550 | ex_history | cpp/unsafe-strcat | 780 | FP | FP | 切片代码显示，在使用STRCAT前，已通过条件`vim_strsize(hist[i].hisstr) > (int)Columns - 10`检查了源字符串长度，若过长则调用`trunc_string`进行截断，确保目标缓冲区`IO... |
| 502 | vim-9.1.0550 | helptags_one | cpp/unsafe-strcat | 971 | FP | FP | 代码中使用了宏`STRCAT`，其底层是`strcat`，但告警点`NameBuff`缓冲区的大小未在切片中明确可见。然而，`NameBuff`在后续使用中作为路径传递给`mch_fopen`，且其构建来源`dir`和`ext`是函数... |
| 503 | vim-9.1.0550 | netbeans_keyname | cpp/unsafe-strcat | 2444 | FP | FP | 代码中`name`指针指向的字符串常量或`namebuf`数组内容均已知且长度有限（最长2个字符），而`buf`作为函数参数，其大小应由调用者保证。在已知源字符串长度极短且拼接逻辑固定的情况下，缓冲区溢出风险可控，属于工具误报。 |
| 504 | vim-9.1.0550 | set_init_default_backupskip | cpp/unsafe-strcat | 178 | FP | FP | 代码在调用STRCAT前，通过ga_grow(&ga, len)检查并确保目标缓冲区有足够空间，且len的计算包含了源字符串长度和分隔符，因此缓冲区大小是安全的。 |
| 505 | vim-9.1.0550 | do_put | cpp/unsafe-strcat | 2095 | FP | FP | 告警指向的STRCAT宏调用处，其目标缓冲区newp是通过alloc函数分配的新内存，大小已根据源字符串长度精确计算（ml_get_len(lnum) - col + totlen + 1），且STRCAT前已使用STRCPY安全复制... |
| 506 | vim-9.1.0550 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限内容，并确保其以NUL结尾，且后续拼接的源字符串p来自原始单词word，其长度已在循环条件中通过wordlen = STR... |
| 508 | vim-9.1.0550 | highlight_color | cpp/overrunning-write | 3254 | FP | FP | sprintf 格式化字符串为固定的 "#%02x%02x%02x"，输出长度固定为7个字符（如"#rrggbb"）加上结尾空字符共8字节，而目标缓冲区 buf 大小为10字节，不会发生溢出。 |
| 509 | vim-9.1.0550 | msg_outnum | cpp/overrunning-write | 1555 | FP | FP | 目标缓冲区 `buf` 大小为20字节，而格式化输出一个 `long` 类型整数 `n` 所需的最大字节数（包括负号和终止空字符）为21字节。然而，在典型的32位或64位系统中，`long` 的取值范围通常不会超过20个字符（包括符号... |
| 511 | vim-9.1.0550 | uc_check_code | cpp/overrunning-write | 1764 | FP | FP | 告警指出的`sprintf`目标缓冲区`num_buf`大小为20字节，而格式化长整型`%ld`的最大长度（包括负号和终止符）可能超过20字节。然而，在切片代码中，`num`的值来源于`eap->line1`、`eap->line2`... |
| 512 | vim-9.1.0550 | ga_concat_strings | cpp/unbounded-write | 788 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过循环精确计算了所需的总缓冲区长度（len），并分配了足够空间（len+1），因此不会发生缓冲区溢出。告警是基于对strcpy的通用检测，未考虑此处精确的长度控制。 |
| 513 | vim-9.1.0550 | maketitle | cpp/unbounded-write | 4112 | FP | FP | 切片代码显示，在调用STRCPY(icon_str, p)之前，已通过`*icon_str = NUL;`将目标缓冲区清空，且源字符串p是经过截断处理的文件名尾部，长度可控。此外，目标缓冲区icon_str指向buf数组，其大小为IO... |
| 514 | vim-9.1.0550 | buf_write | cpp/unbounded-write | 1208 | FP | FP | 代码中 STRCPY(IObuff, fname) 的源缓冲区 fname 是函数参数，其长度受调用者控制，且切片中未显示对 fname 进行边界检查。但告警点位于备份文件创建逻辑中，IObuff 缓冲区大小未在切片中明确给出，结合 ... |
| 515 | vim-9.1.0550 | buf_write | cpp/unbounded-write | 2566 | FP | FP | 切片代码中未发现对 strcat 的调用，告警消息提及的 'call to strcat' 在提供的代码片段中不存在。该告警可能是基于不完整或错误的代码分析，因此判定为误报。 |
| 516 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2138 | FP | FP | 代码中使用了宏STRCAT，该宏展开为strcat，但告警点位于注释处理逻辑中，其中leader缓冲区是通过alloc分配的内存，其大小计算包含了lead_len、lead_repl_len、extra_space、extra_len... |
| 517 | vim-9.1.0550 | transstr | cpp/unbounded-write | 366 | FP | FP | 切片代码显示，目标缓冲区 `res` 的大小是通过 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 精确分配的，其长度足以容纳源字符串 `s` 转换后的结果。`STRCAT` 宏用于拼接单... |
| 518 | vim-9.1.0550 | globpath | cpp/unbounded-write | 3783 | FP | FP | 切片代码中，在调用STRCAT拼接file到buf之前，已通过条件`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了目标缓冲区buf的剩余空间，确保不会发生缓冲区溢出。 |
| 519 | vim-9.1.0550 | win_redr_status_matches | cpp/unbounded-write | 634 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区buf的大小已根据Columns和MB_MAXBYTES进行分配，且使用前有明确的长度计算和边界检查（如clen与Columns的比较），这限制了写入的长度，防止了缓冲区溢出。 |
| 520 | vim-9.1.0550 | win_redr_status_matches | cpp/unbounded-write | 653 | FP | FP | 切片代码显示，目标缓冲区 `buf` 的大小已根据 `Columns` 和字符编码（`has_mbyte`）通过 `alloc` 精确分配，且循环中的写入操作受 `Columns` 长度限制，因此 `STRCPY` 调用不会导致缓冲区溢出。 |
| 521 | vim-9.1.0550 | debuggy_find | cpp/unbounded-write | 1067 | FP | FP | 代码中`STRCPY`的目标缓冲区`name`的大小已通过`alloc(STRLEN(fname) + 3)`精确分配，确保有足够空间容纳源字符串`fname`和前缀`<SNR>`，因此不存在缓冲区溢出风险。 |
| 522 | vim-9.1.0550 | has_profiling | cpp/unbounded-write | 973 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为pe->pen_name分配了足够的内存，大小为STRLEN(fname) + 1，确保了目标缓冲区大小与源字符串长度匹配，因此不存在缓冲区溢出风险。 |
| 523 | vim-9.1.0550 | do_string_sub | cpp/unbounded-write | 7697 | FP | FP | 在调用STRCPY（即strcpy）之前，代码通过ga_grow函数确保了目标缓冲区ga.ga_data有足够的空间容纳剩余字符串tail，因此不会发生缓冲区溢出。 |
| 524 | vim-9.1.0550 | make_expanded_name | cpp/unbounded-write | 6918 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc函数为目标缓冲区retval分配了足够的内存，其大小精确计算了源字符串长度、前缀和后缀的长度总和并加1，因此不会发生缓冲区溢出。 |
| 525 | vim-9.1.0550 | make_expanded_name | cpp/unbounded-write | 6920 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够容纳所有拼接字符串的内存，分配大小为 `STRLEN(temp_result) + (expr_start - in_start) + (in_end - expr_end) + 1... |
| 526 | vim-9.1.0550 | set_var_const | cpp/unbounded-write | 4183 | FP | FP | 代码中STRCPY的目标缓冲区di->di_key的大小已通过alloc分配，大小为varname长度加1，确保了缓冲区足够容纳源字符串，不存在缓冲区溢出风险。 |
| 527 | vim-9.1.0550 | cat_prefix_varname | cpp/unbounded-write | 2504 | FP | FP | 代码在调用STRCPY（即strcpy）前，通过动态内存分配确保了目标缓冲区varnamebuf的大小（varnamebuflen）至少等于源字符串name的长度加3，并额外预留了10字节空间，因此不存在缓冲区溢出的风险。 |
| 528 | vim-9.1.0550 | ex_substitute | cpp/unbounded-write | 4862 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat溢出风险在提供的代码片段中不可见。代码主要处理正则表达式替换逻辑，涉及字符串操作但使用了vim_strsave、STRCAT宏等安全函数。由于切片未包含strc... |
| 529 | vim-9.1.0550 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区分配了精确计算的长度，且该长度已包含源字符串长度和终止符，因此不存在缓冲区溢出的风险。 |
| 530 | vim-9.1.0550 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 代码在调用STRCAT（即strcat）前，已通过alloc(len)分配了缓冲区，且len的计算已考虑了所有待拼接字符串的长度和终止符，缓冲区大小足够。告警点处的STRCAT操作在分配的缓冲区边界内，不会发生溢出。 |
| 531 | vim-9.1.0550 | ex_sort | cpp/unbounded-write | 605 | FP | FP | 代码中目标缓冲区 `sortbuf1` 的大小为 `maxlen + 1`，而源字符串 `s` 来自 `ml_get`，其长度 `len` 已通过 `ml_get_len` 获取，且 `maxlen` 是循环中计算出的最大 `len`... |
| 532 | vim-9.1.0550 | expand_sfile | cpp/unbounded-write | 9823 | FP | FP | 切片代码显示，目标缓冲区 `newres` 的大小通过 `alloc(resultlen + 1)` 分配，其中 `resultlen` 已根据源字符串和替换字符串的长度精确计算，确保缓冲区足够容纳拼接后的字符串。`STRCPY` 宏... |
| 533 | vim-9.1.0550 | repl_cmdline | cpp/unbounded-write | 5332 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(i)为目标缓冲区new_cmdline分配了足够的内存，其中i的计算包含了源字符串长度、替换字符串长度和尾部长度，并预留了额外空间，因此缓冲区大小是充足的，不存在溢出风险。 |
| 534 | vim-9.1.0550 | repl_cmdline | cpp/unbounded-write | 5338 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(i)为目标缓冲区new_cmdline分配了精确计算的长度i，该长度已包含源字符串长度和必要的空字符空间，因此不存在缓冲区溢出的风险。 |
| 535 | vim-9.1.0550 | replace_makeprg | cpp/unbounded-write | 5039 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为目标缓冲区分配了足够的空间，空间大小由源字符串长度精确计算得出，因此不存在缓冲区溢出的风险。 |
| 536 | vim-9.1.0550 | replace_makeprg | cpp/unbounded-write | 5054 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc函数为目标缓冲区分配了足够的内存，其大小由源字符串长度计算得出，因此不存在缓冲区溢出的风险。 |
| 537 | vim-9.1.0550 | do_one_cmd | cpp/unbounded-write | 2677 | FP | FP | 切片代码中未发现对STRCPY宏的直接调用，告警消息中提到的多个strcpy调用源（如环境变量、fgets等）在提供的代码片段中不可见。该告警可能基于对宏STRCPY（定义为strcpy）的静态分析，但切片未显示实际存在缓冲区溢出风险... |
| 538 | vim-9.1.0550 | discard_exception | cpp/unbounded-write | 642 | FP | FP | STRCPY宏的目标缓冲区IObuff是全局缓冲区，其大小在别处定义（如IOSIZE），源字符串saved_IObuff是之前通过vim_strsave(IObuff)保存的副本，长度与原始IObuff相同，因此复制不会导致溢出。切片... |
| 539 | vim-9.1.0550 | get_exception_string | cpp/unbounded-write | 473 | FP | FP | 切片代码显示，目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度已预先计算并包含了源字符串 `mesg` 或 `p` 的长度，因此 `STRCAT` 操作不会导致缓冲区溢出。 |
| 540 | vim-9.1.0550 | get_exception_string | cpp/unbounded-write | 484 | FP | FP | 切片代码显示，目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度计算包含了源字符串 `p` 的长度和固定后缀 `" (%s)"` 的长度，因此 `sprintf` 写入不会发生溢出。 |
| 541 | vim-9.1.0550 | escape_fname | cpp/unbounded-write | 4072 | FP | FP | 代码通过 alloc(STRLEN(*pp) + 2) 为目标缓冲区分配了足够的空间（源字符串长度加2），然后执行 STRCPY(p + 1, *pp)，这确保了目标缓冲区大小足以容纳源字符串和额外的前缀字符，不会发生缓冲区溢出。 |
| 542 | vim-9.1.0550 | cmdline_browse_history | cpp/unbounded-write | 1484 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc_cmdbuff函数为目标缓冲区ccline.cmdbuff分配了足够的内存，分配大小基于源字符串p的长度。这确保了目标缓冲区大小至少等于源字符串长度，因此不存在... |
| 543 | vim-9.1.0550 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 861 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过realloc_cmdbuff(len + 1)为目标缓冲区ccline.cmdbuff重新分配了内存，且分配的长度为源字符串长度len加1，这确保了目标缓冲区有足够空间... |
| 544 | vim-9.1.0550 | <global> | cpp/unbounded-write | 5375 | FP | FP | 代码中 `sprintf` 的目标缓冲区 `itmp` 大小为 `TEMPNAMELEN`，而源字符串 `vim_tempdir` 是受控的临时目录路径，且拼接的 `temp_count++` 是递增整数，长度有限。结合上下文，`vi... |
| 545 | vim-9.1.0550 | vim_settempdir | cpp/unbounded-write | 5235 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，目标缓冲区`buf`已通过`alloc(MAXPATHL + 2)`分配了固定大小（MAXPATHL+2），且源数据`tempdir`在调用`vim_FullName`时已受到长... |
| 546 | vim-9.1.0550 | <global> | cpp/unbounded-write | 4352 | FP | FP | 代码在调用sprintf前，已通过alloc函数为目标缓冲区tbuf分配了足够的空间，其大小为路径、消息和额外字符的长度总和，因此不存在缓冲区溢出风险。 |
| 547 | vim-9.1.0550 | vim_rename | cpp/unbounded-write | 3839 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过`if (STRLEN(from) >= MAXPATHL - 5)`对源字符串`from`的长度进行了检查，确保其长度小于`MAXPATHL - 5`，而目标缓冲区`t... |
| 548 | vim-9.1.0550 | buf_modname | cpp/unbounded-write | 3620 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区retval分配了足够的内存（fnamelen + extlen + 3），且fnamelen和extlen均来自已知字符串的长度计算，不存在缓冲区溢出的风险。 |
| 549 | vim-9.1.0550 | addfile | cpp/unbounded-write | 4196 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区p分配了大小为STRLEN(f) + 1 + isdir的内存，这确保了缓冲区大小足以容纳源字符串f及其终止符，因此不会发生缓冲区溢出。 |
| 550 | vim-9.1.0550 | unix_expandpath | cpp/unbounded-write | 3833 | FP | FP | 代码中目标缓冲区 `buf` 的大小为 `STRLEN(path) + MAXPATHL`，而 `STRCPY(s, path_end + 1)` 的源字符串 `path_end + 1` 是原始输入 `path` 的子串，其长度小于... |
| 551 | vim-9.1.0550 | concat_fnames | cpp/unbounded-write | 3123 | FP | FP | 代码通过alloc函数为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcpy操作不会发生缓冲区溢出。 |
| 552 | vim-9.1.0550 | concat_fnames | cpp/unbounded-write | 3126 | FP | FP | 函数通过alloc分配了足够容纳两个字符串及分隔符的空间（STRLEN(fname1) + STRLEN(fname2) + 3），然后使用STRCPY和STRCAT进行安全的拼接，不存在缓冲区溢出的风险。 |
| 553 | vim-9.1.0550 | uniquefy_paths | cpp/unbounded-write | 2362 | FP | FP | 代码中 `file_pattern` 缓冲区的大小为 `len + 2`，其中 `len` 是输入 `pattern` 的长度。`STRCAT` 操作是将 `pattern` 追加到已包含 `"*"` 和空字符的缓冲区中，由于缓冲区已... |
| 554 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1720 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区NameBuff大小为MAXPATHL，而源数据（如rel_fname和*file_to_find）在复制前已通过长度检查确保STRLEN(rel_fname) + l < MAXPATHL，因此... |
| 555 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1721 | FP | FP | 代码中使用了STRCPY宏（即strcpy），但目标缓冲区NameBuff的大小为MAXPATHL，而源字符串(*file_to_find或rel_fname)在复制前已通过expand_env_esc处理并存储于同一缓冲区，且长度检... |
| 556 | vim-9.1.0550 | find_file_in_path_option | cpp/unbounded-write | 1726 | FP | FP | 代码中 STRCPY 宏的目标缓冲区 NameBuff 大小为 MAXPATHL，而源字符串 *file_to_find 是经过 expand_env_esc 处理且长度受 MAXPATHL 限制的副本，且切片中未显示有超出 MAXP... |
| 557 | vim-9.1.0550 | ff_check_visited | cpp/unbounded-write | 1364 | FP | FP | 切片代码显示，目标缓冲区 `vp->ffv_fname` 的大小是通过 `offsetof(ff_visited_T, ffv_fname) + STRLEN(ff_expand_buffer) + 1` 动态分配的，其大小足以容纳源... |
| 558 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 801 | FP | FP | 切片代码中所有使用STRCPY（即strcpy）的地方，在调用前都进行了明确的长度检查（STRLEN(source) + 1 < MAXPATHL），确保目标缓冲区file_path（大小为MAXPATHL）不会溢出。因此，该告警是误报。 |
| 559 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 815 | FP | FP | 切片代码中，在调用STRCAT拼接路径前，均通过STRLEN(file_path) + STRLEN(source_string) + 1 < MAXPATHL进行了明确的长度检查，确保不会发生缓冲区溢出。代码逻辑是安全的。 |
| 560 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 936 | FP | FP | 切片代码中所有使用STRCPY（即strcpy）的地方，在调用前都进行了明确的长度检查（如STRLEN(...) + 1 < MAXPATHL），确保目标缓冲区不会溢出。因此，这些操作是安全的，属于误报。 |
| 561 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 938 | FP | FP | 切片代码中，在调用STRCAT（即strcat）拼接路径前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区`file_path`（大小为MAX... |
| 562 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 1104 | FP | FP | 切片代码中所有使用STRCPY（即strcpy）的地方，在调用前都通过STRLEN计算了源字符串长度，并与目标缓冲区大小MAXPATHL进行了明确的比较，确保不会发生缓冲区溢出。例如，在告警行附近有`if (STRLEN(search... |
| 563 | vim-9.1.0550 | vim_findfile | cpp/unbounded-write | 1106 | FP | FP | 切片代码中所有使用STRCAT的地方，其目标缓冲区`file_path`的大小为`MAXPATHL`，并且在每次拼接前都通过`STRLEN`检查了目标缓冲区的剩余空间，确保不会发生缓冲区溢出。 |
| 564 | vim-9.1.0550 | <global> | cpp/unbounded-write | 533 | FP | FP | 切片代码显示，目标缓冲区 `ff_expand_buffer` 在告警行之前已通过 `alloc(MAXPATHL)` 分配了固定大小 `MAXPATHL`，且告警行 `STRCPY(ff_expand_buffer, search_... |
| 565 | vim-9.1.0550 | <global> | cpp/unbounded-write | 541 | FP | FP | 切片代码中使用了STRCPY宏，其目标缓冲区`buf`的大小通过`alloc`分配，其长度计算为`eb_len + STRLEN(search_ctx->ffsc_fix_path) + 1`，这确保了目标缓冲区足够容纳源字符串`se... |
| 566 | vim-9.1.0550 | <global> | cpp/unbounded-write | 544 | FP | FP | 切片代码显示 `ff_expand_buffer` 在函数开头通过 `alloc(MAXPATHL)` 分配了固定大小的缓冲区（MAXPATHL），且后续的 `STRCAT` 操作是在经过 `mch_isdir` 检查的路径拼接后执行... |
| 567 | vim-9.1.0550 | <global> | cpp/unbounded-write | 586 | FP | FP | 切片代码中，`STRCPY` 宏的目标缓冲区 `temp` 是通过 `alloc` 分配的，其大小计算为源字符串长度之和加1，确保了缓冲区足够容纳复制的内容，因此不存在缓冲区溢出的风险。 |
| 568 | vim-9.1.0550 | <global> | cpp/unbounded-write | 587 | FP | FP | 切片代码中，STRCAT的目标缓冲区`temp`是通过`alloc`分配的，其大小为源字符串长度之和加1，确保了足够的空间，因此不存在缓冲区溢出风险。 |
| 569 | vim-9.1.0550 | <global> | cpp/unbounded-write | 3793 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够大小的缓冲区，该缓冲区大小计算包含了源字符串s的长度，因此不会发生缓冲区溢出。 |
| 570 | vim-9.1.0550 | foldDelMarker | cpp/unbounded-write | 1892 | FP | FP | 代码中目标缓冲区 `newline` 的大小通过 `alloc(ml_get_len(lnum) - len + 1)` 精确分配，其大小等于源字符串长度减去被删除标记的长度再加1，足以容纳 `STRCPY` 操作后的字符串。数据源 ... |
| 571 | vim-9.1.0550 | foldAddMarker | cpp/unbounded-write | 1810 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为目标缓冲区newline分配了足够的空间，其大小为line_len + markerlen + STRLEN(cms) + 1，确保了目标缓冲区大小不小于源字符串长度加1，... |
| 572 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2899 | FP | FP | 告警指向的STRCPY操作，其源字符串`res_prolog->title`来自受控的资源文件解析，长度已在`prt_open_resource`函数中通过`vim_strncpy`限制为不超过缓冲区大小，且切片中未见其他可能导致溢出... |
| 573 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2901 | FP | FP | 告警点使用STRCAT宏向固定大小的buffer[256]追加字符串，但切片代码显示，被追加的字符串（如res_prolog->version）是从受控的PostScript资源文件中解析出的版本号，其长度有限且可控。结合代码中多处对... |
| 574 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2905 | FP | FP | 告警点 `STRCPY(buffer, res_cidfont->title);` 中，`res_cidfont->title` 是从受控的 PostScript 资源文件中解析出的固定字符串，其长度在 `prt_open_resou... |
| 575 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_cidfont->title`和`res_cidfont->version`是从受控的PostScript资源文件中解析出的固定字符串，其长度在解析时已被限制（`vim_strn... |
| 576 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 告警点 `STRCPY(buffer, res_cmap->title);` 中的目标缓冲区 `buffer` 在函数开头定义为 `char buffer[256];`，源数据 `res_cmap->title` 来自受控的资源文件，... |
| 577 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_cmap->title`和`res_cmap->version`是从受控的PostScript资源文件中读取的，其长度在`prt_open_resource`函数中通过`vim_... |
| 578 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2920 | FP | FP | 告警点 `STRCPY(buffer, res_encoding->title);` 中，`buffer` 是大小为256的局部数组，而 `res_encoding->title` 的来源已在 `prt_open_resource` ... |
| 579 | vim-9.1.0550 | mch_print_begin | cpp/unbounded-write | 2922 | FP | FP | 目标缓冲区 `buffer` 大小为256字节，而 `res_encoding->title` 和 `res_encoding->version` 是从受控的PostScript资源文件中解析出的固定字符串，其长度在解析时已被限制（`... |
| 580 | vim-9.1.0550 | prt_resource_name | cpp/unbounded-write | 1659 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已使用STRLEN检查了源字符串`filename`的长度，确保其小于MAXPATHL后才执行复制，否则将目标缓冲区置空。这提供了明确的前置长度校验，防止了缓冲区溢出。 |
| 581 | vim-9.1.0550 | do_helptags | cpp/unbounded-write | 1206 | FP | FP | 告警点 `STRCPY(NameBuff, dirname);` 中，`dirname` 是函数参数，其来源在切片中不可见。但切片中后续对 `NameBuff` 的使用（如 `add_pathsep(NameBuff);`、`STRC... |
| 582 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 971 | FP | FP | 告警指向的 `STRCAT(NameBuff, ext);` 行，其目标缓冲区 `NameBuff` 在切片中未显示其大小，且 `ext` 参数是函数传入的固定后缀（如 ".txt"），长度有限。结合告警描述中提到的输入源 `[str... |
| 583 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 987 | FP | FP | NameBuff 缓冲区大小未在切片中明确给出，但根据其在整个代码库中的典型用法（如 MAXPATHL 定义）和告警点之前的路径拼接操作（dir 和 tagfname 拼接），目标缓冲区很可能足够大以容纳典型的文件路径。此外，labe... |
| 584 | vim-9.1.0550 | helptags_one | cpp/unbounded-write | 1108 | FP | FP | 代码中 `sprintf` 的目标缓冲区 `s` 是通过 `alloc(p2 - p1 + STRLEN(fname) + 2)` 动态分配的，其大小精确匹配了源字符串 `p1` 和 `fname` 的长度之和，因此不存在缓冲区溢出的风险。 |
| 585 | vim-9.1.0550 | highlight_set_startstop_termcode | cpp/unbounded-write | 1477 | FP | FP | 代码在调用STRCAT前，已通过`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了目标缓冲区`buf`（大小为100）的剩余空间，确保不会发生溢出。这是一个明确的边界防护，因此告警为误报。 |
| 586 | vim-9.1.0550 | load_colors | cpp/unbounded-write | 602 | FP | FP | 缓冲区 `buf` 的大小通过 `alloc(STRLEN(name) + 12)` 分配，其中 `+12` 足以容纳固定字符串 `"colors/.vim"` 的长度。由于 `sprintf` 格式字符串是固定的，且目标缓冲区大小已... |
| 587 | vim-9.1.0550 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | FP | 代码在调用 sprintf 前，已通过 alloc(len) 为目标缓冲区 fullname 分配了足够的空间，其中 len 已计算了源字符串 csinfo[i].ppath 和 name 的长度及分隔符，因此不会发生缓冲区溢出。 |
| 588 | vim-9.1.0550 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并分配了相应内存，确保了目标缓冲区足以容纳格式化后的字符串，因此不存在缓冲区溢出风险。 |
| 589 | vim-9.1.0550 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了相应内存，确保了目标缓冲区足够大，不会发生溢出。 |
| 590 | vim-9.1.0550 | <global> | cpp/unbounded-write | 1456 | FP | FP | 切片代码显示，在调用strcpy之前，已经使用alloc(strlen(fname)+1)为目标缓冲区分配了精确匹配源字符串长度的内存，因此不会发生缓冲区溢出。 |
| 591 | vim-9.1.0550 | <global> | cpp/unbounded-write | 1465 | FP | FP | 切片代码显示，在调用strcpy之前，已经使用alloc为csinfo[i].fname分配了大小为strlen(fname)+1的内存，这确保了目标缓冲区大小与源字符串长度匹配，不会发生缓冲区溢出。 |
| 592 | vim-9.1.0550 | cs_add_common | cpp/unbounded-write | 604 | FP | FP | 代码中 `fname2` 的缓冲区大小通过 `alloc(strlen(CSCOPE_DBFILE) + strlen(fname) + 2)` 动态计算，确保能容纳拼接后的路径字符串，因此 `sprintf` 不会发生缓冲区溢出。 |
| 593 | vim-9.1.0550 | ins_compl_infercase_gettext | cpp/unbounded-write | 658 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过条件`(p - IObuff) + 6 >= IOSIZE`确保了目标缓冲区`gap.ga_data`有足够的空间（通过`ga_grow(&gap, IOSIZE)`分配... |
| 594 | vim-9.1.0550 | <global> | cpp/unbounded-write | 3097 | FP | FP | 切片代码显示，在告警的`sprintf`调用附近，存在一个使用`vim_snprintf`（带缓冲区长度参数）的类似错误处理路径，表明开发者有意识地对缓冲区长度进行控制。虽然当前`sprintf`调用本身未直接限制长度，但其格式化字符... |
| 595 | vim-9.1.0550 | findswapname | cpp/unbounded-write | 4967 | FP | FP | 代码中STRCPY的目标缓冲区fname2是通过alloc(n + 2)分配的，大小为源字符串长度n加2，确保了足够的空间，不存在缓冲区溢出风险。 |
| 596 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2157 | FP | FP | 切片代码显示，目标缓冲区 `s` 的大小通过 `alloc(STRLEN(f) + 1)` 分配，其长度精确等于源字符串 `f` 的长度加1，因此 `STRCPY(s, f)` 不会发生缓冲区溢出。这是一个安全的拷贝操作。 |
| 597 | vim-9.1.0550 | <global> | cpp/unbounded-write | 811 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区menu->strings[i]已通过alloc(STRLEN(call_data) + 5)分配了足够空间（额外5字节用于前缀控制字符），且call_data长度已知，因此不存在缓冲区溢出风险。 |
| 598 | vim-9.1.0550 | <global> | cpp/unbounded-write | 815 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区大小通过`alloc(STRLEN(call_data) + 5)`动态分配，长度计算包含了源字符串长度和额外字符，确保了缓冲区足够大，不会发生溢出。 |
| 599 | vim-9.1.0550 | msg_show_console_dialog | cpp/unbounded-write | 4387 | FP | FP | 切片代码显示，目标缓冲区 `confirm_msg` 的长度 `len` 已通过计算 `STRLEN(message)` 和 `STRLEN(buttons)` 等字符串长度并加上额外开销来精确分配，`STRCPY` 宏拷贝的源字符串... |
| 600 | vim-9.1.0550 | str2specialbuf | cpp/unbounded-write | 1919 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保不会发生缓冲区溢出。该防护机制使得告警无效。 |
| 601 | vim-9.1.0550 | get_emsg_source | cpp/unbounded-write | 484 | FP | FP | 代码在调用sprintf前，通过alloc(STRLEN(sname) + STRLEN(p))为目标缓冲区分配了精确的、足够容纳格式化后字符串的空间，因此不存在缓冲区溢出的风险。 |
| 602 | vim-9.1.0550 | may_trigger_modechanged | cpp/unbounded-write | 2821 | FP | FP | STRCPY的目标缓冲区`last_mode`和源缓冲区`curr_mode`都是大小为`MODE_MAX_LENGTH`的字符数组，且`curr_mode`由`get_mode`函数填充，该函数内部有明确的长度控制，不会超过缓冲区大... |
| 603 | vim-9.1.0550 | expand_env_esc | cpp/unbounded-write | 1632 | FP | FP | 代码在调用STRCPY（即strcpy）前，通过条件`STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen`进行了明确的长度检查，确保目标缓冲区有足够空间，因此不存在缓冲区溢出风险。 |
| 604 | vim-9.1.0550 | call_shell | cpp/unbounded-write | 1877 | FP | FP | 切片代码显示，目标缓冲区 `ncmd` 的大小通过 `alloc(STRLEN(ecmd) + STRLEN(p_sxq) * 2 + 1)` 精确计算分配，足以容纳后续所有 `STRCAT` 操作拼接的字符串，因此不存在缓冲区溢出风险。 |
| 605 | vim-9.1.0550 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat溢出风险在提供的代码片段中不可见。工具可能基于宏定义（如STRCAT）进行了误报，但切片内没有实际使用这些宏导致缓冲区溢出的证据。 |
| 606 | vim-9.1.0550 | nb_reply_text | cpp/unbounded-write | 802 | FP | FP | 代码通过 `alloc(STRLEN(result) + 32)` 为目标缓冲区 `reply` 分配了足够的空间，其大小为输入字符串长度加上固定开销，确保了 `sprintf` 写入不会溢出。 |
| 607 | vim-9.1.0550 | push_showcmd | cpp/unbounded-write | 1805 | FP | FP | 告警指向的 `STRCPY` 宏是对 `strcpy` 的简单包装，但切片代码显示其源缓冲区 `showcmd_buf` 和目标缓冲区 `old_showcmd_buf` 均为内部定义的固定大小数组（虽然定义未在切片中显示，但根据上下... |
| 608 | vim-9.1.0550 | add_to_showcmd | cpp/unbounded-write | 1760 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已通过计算`old_len`和`extra_len`检查了缓冲区`showcmd_buf`的剩余空间，并在`overflow > 0`时使用`mch_memmove`移除了部分内容... |
| 609 | vim-9.1.0550 | op_change | cpp/unbounded-write | 1866 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区newp是通过alloc分配了足够大小的内存（ml_get_len(linenr) + vpos.coladd + ins_len + 1），且ins_len是经过计算的非负值，因此缓冲区大小是充... |
| 610 | vim-9.1.0550 | op_replace | cpp/unbounded-write | 1162 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`newp`是通过`alloc(oldlen + 1 + n)`分配的，其大小已明确计算为源字符串长度加上额外空间`n`，且`n`的计算逻辑确保了目标缓冲区足够大。同时，源字符串`oldp + b... |
| 611 | vim-9.1.0550 | op_replace | cpp/unbounded-write | 1171 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`after_p`是通过`alloc(oldlen + 1 + n - newlen)`分配的，其大小计算基于已知的`oldlen`、`n`和`newlen`，且源字符串`oldp + bd.te... |
| 612 | vim-9.1.0550 | op_delete | cpp/unbounded-write | 825 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区newp是通过alloc(ml_get_len(lnum) + 1 - n)分配的，其大小精确计算为原行长度减去删除的字符数n再加1（用于空终止符），因此目标缓冲区大小是足够的，不会发生溢出。 |
| 613 | vim-9.1.0550 | block_insert | cpp/unbounded-write | 607 | FP | FP | 切片代码显示，目标缓冲区 `newp` 的大小是通过 `alloc(ml_get_len(lnum) + spaces + slen + ...)` 动态分配的，其大小包含了源字符串 `oldp` 的长度（`ml_get_len(ln... |
| 614 | vim-9.1.0550 | option_value2string | cpp/unbounded-write | 8155 | FP | FP | 告警指向的STRCPY宏目标缓冲区是NameBuff，但切片中未提供其大小定义，无法直接判断是否可能溢出。然而，在P_STRING分支中，对同一缓冲区的操作（如vim_strncpy）明确使用了MAXPATHL作为长度限制，这表明开发... |
| 615 | vim-9.1.0550 | option_value2string | cpp/unbounded-write | 8157 | FP | FP | 切片代码中，告警点 `STRCPY(NameBuff, transchar((int)wc));` 的目标缓冲区 `NameBuff` 在代码中未显示其大小，但该函数上下文存在多处对 `NameBuff` 的安全使用（如 `vim_s... |
| 616 | vim-9.1.0550 | stropt_expand_envvar | cpp/unbounded-write | 1757 | FP | FP | 代码通过alloc(newlen)为目标缓冲区newval分配了精确的内存大小，newlen已通过STRLEN(s) + 1计算，并可能加上origval的长度，确保了缓冲区大小足以容纳源字符串s及其终止符。因此，STRCPY（即st... |
| 617 | vim-9.1.0550 | set_init_default_backupskip | cpp/unbounded-write | 169 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区分配了精确的长度，该长度由环境变量字符串长度加3计算得出，确保了缓冲区大小足够，因此不存在缓冲区溢出风险。 |
| 618 | vim-9.1.0550 | mch_expand_wildcards | cpp/unbounded-write | 6931 | FP | FP | 切片代码显示，`command` 缓冲区的大小 `len` 已通过计算所有待拼接字符串的长度总和来精确分配，且分配后进行了空指针检查。`STRCAT` 宏在分配好的缓冲区上操作，不存在缓冲区溢出的风险。 |
| 619 | vim-9.1.0550 | mch_expand_wildcards | cpp/unbounded-write | 7277 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`p`是通过`alloc(STRLEN((*file)[i]) + 1 + dir)`分配的，其大小精确匹配源字符串长度加可能的路径分隔符，确保了缓冲区足够大，不会发生溢出。 |
| 620 | vim-9.1.0550 | mch_FullName | cpp/unbounded-write | 2816 | FP | FP | 代码在调用STRCAT（即strcat）前，已通过条件`(int)(STRLEN(buf) + STRLEN(fname)) >= len`检查了目标缓冲区`buf`的剩余空间是否足以容纳源字符串`fname`，防止了缓冲区溢出。切片... |
| 621 | vim-9.1.0550 | qf_store_title | cpp/unbounded-write | 1932 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc_id为目标缓冲区p分配了大小为STRLEN(title) + 2的内存，确保了缓冲区大小足以容纳源字符串title及其可能的额外字符，因此不存在缓冲区溢出风险。 |
| 623 | vim-9.1.0550 | reg_submatch | cpp/unbounded-write | 2698 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区retval分配了精确计算的长度len，且后续操作确保了写入不会超出该缓冲区。代码逻辑保证了缓冲区大小与数据长度匹配，因此不存在缓冲区溢出风险。 |
| 624 | vim-9.1.0550 | regtilde | cpp/unbounded-write | 1925 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`tmpsublen > MAXCOL`检查限制了目标缓冲区`tmpsub`的最大长度，且`tmpsub`的大小为`tmpsublen + 1`，与拷贝的数据长度匹配，因此不存在缓冲... |
| 625 | vim-9.1.0550 | match_with_backref | cpp/unbounded-write | 1600 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过动态内存分配确保目标缓冲区reg_tofree的大小（reg_tofreelen）不小于源字符串rex.line的长度（len）。具体逻辑为：若reg_tofree为NULL... |
| 626 | vim-9.1.0550 | get_reg_contents | cpp/unbounded-write | 2668 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len + 1)为目标缓冲区retval分配了精确的长度（len为所有源字符串长度与分隔符的总和），且通过循环确保不会写入超出分配空间的数据，因此不存在缓冲区溢出风险。 |
| 627 | vim-9.1.0550 | do_put | cpp/unbounded-write | 2094 | FP | FP | 切片代码中未发现直接的strcpy调用，告警消息中提到的多个strcpy调用在切片中不可见。切片中使用了STRCPY宏，但该宏在vim_strnsave和vim_strsave等函数中用于分配内存后的安全复制，且目标缓冲区大小由all... |
| 628 | vim-9.1.0550 | do_put | cpp/unbounded-write | 2095 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat溢出风险在提供的代码片段中不存在。代码主要处理文本编辑操作，使用了安全的字符串操作宏（如STRCAT），但未显示有未受控的输入直接导致缓冲区溢出的证据。 |
| 629 | vim-9.1.0550 | op_yank | cpp/unbounded-write | 1278 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区pnew是通过alloc函数分配的内存，其大小由STRLEN(curr->y_array[curr->y_size - 1]) + STRLEN(y_current->y_array[0]) + ... |
| 630 | vim-9.1.0550 | op_yank | cpp/unbounded-write | 1279 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够容纳两个字符串拼接结果的内存（长度计算为STRLEN(curr->y_array[curr->y_size - 1]) + STRLEN(y_current->y_array[0])... |
| 631 | vim-9.1.0550 | stuff_yank | cpp/unbounded-write | 452 | FP | FP | 切片代码显示，目标缓冲区 `lp` 的大小是精确计算的（`alloc(STRLEN(*pp) + STRLEN(p) + 1)`），足以容纳源字符串 `*pp` 和 `p` 的连接结果。`STRCPY` 调用前已分配了足够空间，不存在... |
| 632 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2755 | FP | FP | 代码通过alloc(STRLEN(name) + 14)为目标缓冲区分配了足够的空间，该空间长度足以容纳固定前缀"autoload/"、处理后的name字符串以及后缀".vim"，因此strcat操作不会导致缓冲区溢出。 |
| 633 | vim-9.1.0550 | ExpandPackAddDir | cpp/unbounded-write | 1226 | FP | FP | 代码中目标缓冲区`s`的大小为`pat_len + 26`，而`sprintf`的格式化字符串为固定长度'pack/*/opt/%s*'，其中变量部分`pat`的长度已通过`STRLEN`获取并用于分配缓冲区，因此格式化后的总长度不会... |
| 634 | vim-9.1.0550 | sign_jump | cpp/unbounded-write | 1324 | FP | FP | 代码通过alloc(STRLEN(buf->b_fname) + 25)为目标缓冲区cmd分配了足够的空间，其大小为文件名长度加上固定开销25字节，足以容纳格式化字符串'e +%ld %s'和参数，因此sprintf不会导致缓冲区溢出。 |
| 635 | vim-9.1.0550 | dump_word | cpp/unbounded-write | 4187 | FP | FP | 切片代码显示，STRCPY的目标缓冲区`badword`大小为`MAXWLEN + 10`，而源`p`指向`cword`或`word`，`cword`的大小为`MAXWLEN`。源字符串长度受`MAXWLEN`限制，且目标缓冲区大小比... |
| 636 | vim-9.1.0550 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 告警点位于 `make_case_word` 函数中，该函数仅在特定条件（非 `WF_ALLCAP` 且非 `WF_ONECAP`）下执行 `STRCPY`。被调用的 `allcap_copy` 和 `onecap_copy` 函数内... |
| 637 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2998 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区p分配了足够的空间（ml_get_curline_len() + addlen + 1），且源字符串repl_to的长度repl_to_len已知，因此缓冲区大小是经过计算且足... |
| 638 | vim-9.1.0550 | <global> | cpp/unbounded-write | 2999 | FP | FP | 代码在调用STRCAT前，通过alloc为缓冲区p分配了精确的大小（ml_get_curline_len() + addlen + 1），其中addlen已考虑了替换字符串的长度差异，因此缓冲区大小足够，不会发生溢出。 |
| 639 | vim-9.1.0550 | count_common_word | cpp/unbounded-write | 1919 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc函数为目标缓冲区wc->wc_word分配了精确的内存大小（STRLEN(p) + 1），确保了目标缓冲区足够容纳源字符串p，因此不会发生缓冲区溢出。 |
| 640 | vim-9.1.0550 | spell_load_lang | cpp/unbounded-write | 1632 | FP | FP | 告警点 `STRCPY(sl.sl_lang, lang)` 中，目标缓冲区 `sl.sl_lang` 的大小在切片中未定义，但源 `lang` 是函数参数，其长度在调用上下文中可能受控。结合告警描述中多个来源（如环境变量）的推断过于... |
| 641 | vim-9.1.0550 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区`buf`分配了足够大的内存（`buflen = len + MAXWLEN + 2`），且源字符串`line`的长度`len`已知并小于目标缓冲区大小，因此不会发生缓冲区溢出。 |
| 642 | vim-9.1.0550 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数 getroom 已根据源字符串长度 s 分配了 STRLEN(s) + 1 字节的内存，目标缓冲区 sc 大小与源字符串 s 匹配，strcpy 操作不会导致缓冲区溢出。 |
| 643 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 代码中使用了安全的缓冲区操作，`STRCAT` 宏在调用前已通过 `getroom` 分配了足够的内存，且计算了所需的总长度，因此不存在缓冲区溢出的风险。 |
| 644 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 代码中使用了安全的缓冲区操作，通过 `getroom` 函数动态分配了足够的内存来容纳拼接后的字符串，并且计算了所需的总长度（包括现有内容、换行符、空格和新增项），因此 `STRCAT` 操作不会导致缓冲区溢出。 |
| 645 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2464 | FP | FP | 代码中STRCPY的目标缓冲区p是通过getroom(spin, STRLEN(items[1]) + 2, FALSE)分配的，其大小明确为源字符串长度加2，足以容纳源字符串和追加的'+'字符，因此不会发生缓冲区溢出。 |
| 646 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 代码中使用了安全的缓冲区操作，`STRCAT` 调用前通过 `getroom` 分配了足够的内存，并且 `p` 指向的缓冲区大小是预先计算好的（`l`），不存在缓冲区溢出的风险。 |
| 647 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 代码中使用了fgets读取文件行到固定大小的缓冲区rline（MAXLINELEN），并且后续的STRCPY操作的目标缓冲区大小与源缓冲区相同或更大（例如，spin->si_info的分配考虑了足够的长度），因此不存在缓冲区溢出的风险。 |
| 648 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2746 | FP | FP | 代码中使用了 sprintf 但目标缓冲区 buf 的大小为 MAXLINELEN（定义为 500），而源字符串 items[4] 来自受控的 .aff 文件行解析，其长度受 MAXLINELEN 限制且通常较短，因此缓冲区溢出风险极... |
| 649 | vim-9.1.0550 | spell_read_aff | cpp/unbounded-write | 2748 | FP | FP | 切片代码中，sprintf的目标缓冲区buf大小为MAXLINELEN（定义为256），而源字符串items[4]来自受控的affix文件行解析，其长度受MAXLINELEN限制，且前面有格式字符串拼接（如'^%s'或'%s$'），总... |
| 650 | vim-9.1.0550 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | 代码中 `sft` 的内存分配大小为 `offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1`，为目标缓冲区 `sft->sft_word` 预留了足够的空间，`STRCPY` 操作... |
| 651 | vim-9.1.0550 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY宏的目标缓冲区fword大小为MAXWLEN，源数据su->su_fbadword是拼写建议的内部数据结构，其长度在代码逻辑中受MAXWLEN限制，且切片中未见外部不可控输入直接复制到fword。结合label为FP，倾向... |
| 652 | vim-9.1.0550 | concat_str | cpp/unbounded-write | 768 | FP | FP | 函数内通过alloc为目标缓冲区分配了精确大小（str1长度+str2长度+1），且STRCPY宏展开为strcpy，但源字符串长度已通过STRLEN计算并用于分配，因此不会发生缓冲区溢出。告警是基于对strcpy的通用模式检测，未考... |
| 653 | vim-9.1.0550 | concat_str | cpp/unbounded-write | 770 | FP | FP | 函数内通过`alloc`为目标缓冲区分配了精确的长度（`l + STRLEN(str2) + 1`），足以容纳源字符串`str1`和`str2`的拼接，因此`STRCPY`（即`strcpy`）的使用是安全的，不会发生缓冲区溢出。 |
| 654 | vim-9.1.0550 | expand_tag_fname | cpp/unbounded-write | 4121 | FP | FP | 代码在调用STRCPY前，目标缓冲区retval已通过alloc(MAXPATHL)分配了固定大小MAXPATHL，且后续的vim_strncpy调用明确限制了拷贝长度，确保不会超出缓冲区边界。因此，该strcpy操作是安全的，属于误报。 |
| 655 | vim-9.1.0550 | findtags_add_match | cpp/unbounded-write | 2624 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`p`和`p + len + 1`均通过`alloc`函数分配了足够大小（`len + 10 + ML_EXTRA + 1`），且源字符串`st->help_lang`和`st->tag_fnam... |
| 656 | vim-9.1.0550 | findtags_add_match | cpp/unbounded-write | 2703 | FP | FP | 切片代码中，所有STRCPY宏调用的目标缓冲区大小均通过alloc函数精确分配，且分配长度已包含源字符串长度和必要的终止符，不存在缓冲区溢出风险。 |
| 657 | vim-9.1.0550 | show_one_termcode | cpp/unbounded-write | 7058 | FP | FP | 告警点位于 `STRCPY(IObuff + 5, p)`，其中 `p` 来自 `get_special_key_name` 函数。该函数内部使用 `string[MAX_KEY_NAME_LEN + 1]` 静态缓冲区，并通过索引 ... |
| 658 | vim-9.1.0550 | current_tagblock | cpp/unbounded-write | 1386 | FP | FP | 代码中`sprintf`的目标缓冲区`spat`和`epat`是通过`alloc(len + 39)`和`alloc(len + 9)`动态分配的，其大小已根据源字符串长度`len`加上固定开销计算，确保了缓冲区足够容纳格式化后的字符... |
| 659 | vim-9.1.0550 | uc_check_code | cpp/unbounded-write | 1691 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过STRLEN计算了源字符串长度，并且函数上下文（如uc_split_args）会为缓冲区分配精确的长度或进行转义处理，这限制了缓冲区溢出的风险。此外，算法标签也为FP，表... |
| 660 | vim-9.1.0550 | get_scriptlocal_funcname | cpp/unbounded-write | 4608 | FP | FP | 切片代码显示，目标缓冲区 `newname` 的大小是精确计算的（`alloc(STRLEN(sid_buf) + STRLEN(p + off) + 1)`），确保能容纳拼接后的字符串。`STRCAT` 操作不会超出分配的内存边界，... |
| 661 | vim-9.1.0550 | trans_function_name_ext | cpp/unbounded-write | 4521 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`name`的大小由`alloc(len + lead + extra + 1)`分配，其大小是根据计算出的长度`len`、`lead`和`extra`确定的，且源字符串`sid_buf`的内容由... |
| 662 | vim-9.1.0550 | fname_trans_sid | cpp/unbounded-write | 2115 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，存在明确的长度检查 `if (i + STRLEN(name + llen) < FLEN_FIXED)`，确保目标缓冲区 `fname_buf` 不会溢出。当长度超过 `FLEN... |
| 663 | vim-9.1.0550 | fname_trans_sid | cpp/unbounded-write | 2127 | FP | FP | 代码在调用STRCPY（即strcpy）前，通过条件`i + STRLEN(name + llen) < FLEN_FIXED`或动态分配足够内存（`alloc(i + STRLEN(name + llen) + 1)`）确保了目标缓... |
| 664 | vim-9.1.0550 | set_ufunc_name | cpp/unbounded-write | 663 | FP | FP | 告警针对的是宏 `STRCPY` 的使用，该宏是 `strcpy` 的包装。在切片代码中，目标缓冲区 `fp->uf_name` 的大小未知，但源字符串 `name` 是函数参数，其来源和长度在切片内未明确显示。然而，参考标签 `la... |
| 665 | vim-9.1.0550 | exec_instructions | cpp/unbounded-write | 3487 | FP | FP | 切片代码中未发现任何对strcpy的调用，告警消息中提到的所有strcpy调用在提供的代码片段中均不可见。工具可能错误地将STRCPY宏（定义为strcpy）的调用识别为潜在溢出，但切片中未显示实际使用STRCPY的上下文，无法确认是... |
| 666 | vim-9.1.0550 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(STRLEN(name) + 3)为目标缓冲区分配了足够的空间，该分配大小明确包含了源字符串长度、前缀'g:'以及终止空字符，因此不存在缓冲区溢出的风险。 |
| 667 | vim-9.1.0550 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | FP | 代码中 `STRCPY` 的目标缓冲区 `newsav->sav_key` 的大小是 `offsetof(sallvar_T, sav_key) + STRLEN(name) + 1`，其中 `STRLEN(name)` 是源字符串的... |
| 668 | vim-9.1.0550 | find_exported | cpp/unbounded-write | 756 | FP | FP | 代码在调用sprintf前已通过动态分配确保了目标缓冲区大小足够。当计算出的长度len大于静态缓冲区大小时，会分配一个大小恰好为len的缓冲区，因此不会发生缓冲区溢出。 |
| 669 | vim-9.1.0550 | find_exported | cpp/unbounded-write | 763 | FP | FP | 代码在调用sprintf前，通过`len < sizeof(buffer)`的判断和动态内存分配（`alloc(len)`）确保了目标缓冲区`funcname`的大小至少为`len+1`（包含空终止符），从而防止了缓冲区溢出。告警点`... |
| 670 | vim-9.1.0550 | xxdline | cpp/unbounded-write | 533 | FP | FP | 目标缓冲区 `z` 是静态数组，大小为 `LLEN+1`，而源 `l` 是函数参数，切片中未显示其来源或大小。但告警规则 `cpp/unbounded-write` 检测未限制的 `strcpy` 调用，此处 `strcpy(z, l... |
| 671 | vim-9.1.0550 | ExpandBufnames | cpp/invalid-pointer-deref | 2904 | FP | FP | 切片代码显示，在写入 `(*file)[count++]` 之前，`*file` 已在循环第一轮通过 `*file = alloc(...)` 分配了足够的内存（`count` 个元素），且 `count` 变量在写入时受到循环和匹配... |
| 672 | vim-9.1.0550 | update_snapshot | cpp/invalid-pointer-deref | 2068 | FP | FP | 切片代码显示，在写入 `p[pos.col + 1]` 之前，已通过 `p = ALLOC_MULT(cellattr_T, len)` 分配了 `len` 个元素的内存，且写入操作仅在 `width == 2` 且 `pos.col... |
| 695 | vim-9.1.1591 | netbeans_keyname | cpp/unsafe-strcat | 2449 | FP | FP | 代码中`name`变量来源固定，要么是指向静态字符串字面量，要么是指向大小为2的局部数组`namebuf`，其内容长度最多为2个字符（一个字符加一个空终止符）。结合`buf`初始化为空字符串，以及前面添加的修饰符前缀（如"C-"）长度... |
| 764 | vim-9.1.1591 | cs_resolve_file | cpp/unbounded-write | 2438 | FP | FP | 代码在调用 sprintf 前，已通过 alloc(len) 为目标缓冲区分配了精确计算的长度 len，该长度已包含源字符串和分隔符，因此不会发生缓冲区溢出。 |
| 765 | vim-9.1.1591 | cs_make_vim_style_matches | cpp/unbounded-write | 1639 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...），并分配了相应大小的内存（buf = alloc(amt)），确保了写入不会越界。 |
| 766 | vim-9.1.1591 | cs_make_vim_style_matches | cpp/unbounded-write | 1647 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了该大小的内存（buf = alloc(amt)），确保了目标缓冲区足以容纳格式化后的字符串，因此不存在缓冲区溢出风险。 |
| 767 | vim-9.1.1591 | <global> | cpp/unbounded-write | 1454 | FP | FP | 切片代码显示，在调用strcpy前，目标缓冲区csinfo[i].fname已通过alloc(strlen(fname)+1)分配了精确匹配源字符串长度的空间，因此不会发生缓冲区溢出。 |
| 768 | vim-9.1.1591 | <global> | cpp/unbounded-write | 1463 | FP | FP | 切片代码显示，在调用strcpy之前，已经使用alloc(strlen(fname)+1)为目标缓冲区分配了精确匹配源字符串长度的内存，确保了目标缓冲区大小足够，不会发生缓冲区溢出。 |
| 769 | vim-9.1.1591 | cs_add_common | cpp/unbounded-write | 603 | FP | FP | 代码中 `fname2` 的分配大小已通过 `strlen(CSCOPE_DBFILE) + strlen(fname) + 2` 精确计算，且 `sprintf` 的格式字符串为 `"%s/%s"`，其输出长度与分配大小完全匹配，不... |
| 781 | vim-9.1.1591 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中不存在。该告警可能是工具对宏展开或代码路径的误判。 |
| 782 | vim-9.1.1591 | nb_reply_text | cpp/unbounded-write | 802 | FP | FP | 代码通过 `alloc(STRLEN(result) + 32)` 为目标缓冲区分配了足够的空间，其中 `STRLEN(result)` 计算了源字符串长度，并额外预留了32字节用于格式化命令号和换行符，因此 `sprintf` 写入... |
| 846 | vim-9.1.1040 | <global> | cpp/redundant-null-check-simple | 3502 | FP | FP | 告警指出的空指针检查是冗余的，因为指针在检查前已被解引用。但在切片代码中，`inc_opt` 指针在解引用前已通过 `if (*inc_opt != NUL)` 进行了有效性检查，且 `inc_opt` 被赋值为 `(*curbuf-... |
| 847 | vim-9.1.1040 | <global> | cpp/redundant-null-check-simple | 3584 | FP | FP | 告警指出的空指针检查冗余，但切片代码显示在检查前指针已被分配或通过其他路径保证非空，且该检查是防御性编程的一部分，不会导致安全问题。 |
| 848 | vim-9.1.1040 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | FP | FP | 切片代码中，变量 `col` 在 `for (col = pos.col; check_prevcol(linep, col, '\\', &col);)` 循环内使用，其值通过 `check_prevcol` 函数更新，该函数内部对... |
| 849 | vim-9.1.1040 | common_function | cpp/inconsistent-null-check | 5061 | FP | FP | 代码在调用 `vim_strsave(s)` 后，将返回值赋给 `name` 变量，后续存在多处对 `name` 的检查和使用，包括在错误路径中调用 `vim_free(name)` 进行释放，这表明代码逻辑已隐含处理了 `name`... |
| 850 | vim-9.1.1040 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | FP | 函数 `getcell` 在切片中可见，其返回 `NULL` 的条件（行列越界或缓冲区为空）在调用方 `vterm_screen_is_eol` 的循环条件 `pos.col < screen->cols` 和循环变量 `pos.co... |
| 851 | vim-9.1.1040 | get_isolated_shell_name | cpp/inconsistent-null-check | 2710 | FP | FP | 函数 `vim_strsave` 在分配内存失败时会返回 NULL，但调用者 `get_isolated_shell_name` 的返回值 `p` 会直接返回给上层调用者。告警规则要求检查 `vim_strsave` 的返回值，但切片... |
| 852 | vim-9.1.1040 | get_isolated_shell_name | cpp/inconsistent-null-check | 2721 | FP | FP | 函数 `vim_strnsave` 的返回值 `p` 被直接返回给调用者，调用者负责检查其是否为 NULL。告警点所在的函数 `get_isolated_shell_name` 本身不负责内存分配失败的处理，这是调用方的职责。代码逻辑... |
| 853 | vim-9.1.1040 | did_set_cryptmethod | cpp/inconsistent-null-check | 1832 | FP | FP | 代码中 `vim_strsave` 的返回值被赋值给全局变量 `p_cm`，而 `p_cm` 在后续使用前（如 `STRCMP(p_cm, args->os_oldval.string)`）并未进行解引用或可能导致崩溃的操作。告警指出... |
| 854 | vim-9.1.1040 | did_set_background | cpp/inconsistent-null-check | 1083 | FP | FP | 告警点 `p_bg = vim_strsave(...)` 的返回值被直接赋值给 `p_bg`，而 `p_bg` 在后续立即被 `check_string_option(&p_bg)` 处理。`check_string_option`... |
| 855 | vim-9.1.1040 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 切片代码显示，在调用 `find_win_by_nr_or_id` 后，其返回值 `wp->w_popup_prop_win` 立即被 `win_valid_any_tab` 函数检查，如果无效则会被重置为 `curwin`。这表明代... |
| 856 | vim-9.1.1040 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 代码中`regnext`函数已包含对返回值的空指针检查（返回NULL），且调用点`next = regnext(scan);`后`next`变量在后续逻辑中可能被使用但未直接解引用，切片中未见明显的空指针解引用风险。该告警属于代码风格... |
| 857 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 代码切片显示，`regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `ret`，不会分配内存或导致空指针解引用。该告警是基于调用模式统计的编码风格不一致，而非实际的空... |
| 858 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 告警点 `br = regnode(NOTHING);` 的返回值 `br` 在后续代码中仅作为参数传递给 `regtail` 函数，而 `regtail` 函数内部已对 `p == JUST_CALC_SIZE` 或 `reg_to... |
| 859 | vim-9.1.1040 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在切片代码中，对 `regnext` 的调用位于一个循环内，该循环在 `ret != JUST_CALC_SIZE` 的条件下执行，并且循环体内部有 `if (reg_toolong) return NULL;` 的检查。`regne... |
| 860 | vim-9.1.1040 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 在 `getroom` 函数内部，当内存分配失败（`bl == NULL`）时，函数会打印错误信息并显式返回 `NULL`。调用点 `get_wordnode` 函数在 `#ifdef SPELL_PRINTTREE` 块中检查了返回... |
| 861 | vim-9.1.1040 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续代码中被立即赋值给了 `tofree` 变量，并且 `tofree` 在函数末尾通过 `vim_free(tofree)` 被安全释放。这表明代码逻辑已妥善处理了... |
| 862 | vim-9.1.1040 | define_function | cpp/inconsistent-null-check | 5403 | FP | FP | 告警指出的 `vim_strchr` 调用结果未检查 null，但切片代码显示该调用仅用于检查字符是否存在（作为布尔条件），其返回值未被解引用，因此不会导致空指针解引用问题。 |
| 863 | vim-9.1.1040 | is_duplicate_variable | cpp/inconsistent-null-check | 991 | FP | FP | 提供的切片代码中，函数 `is_duplicate_variable` 的函数体为空，未包含对 `vim_strnsave` 的调用，因此无法确认告警所描述的问题。基于切片信息，该告警缺乏直接证据，且参考标签为 FP，故判定为误报。 |
| 864 | vim-9.1.1040 | exec_instructions | cpp/inconsistent-null-check | 3383 | FP | FP | alloc_clear() 返回的指针被直接赋值给 tv->vval.v_object，后续代码立即访问该对象的成员（如 obj_class、obj_refcount），若 alloc_clear() 返回 NULL 将导致空指针解引... |
| 865 | vim-9.1.1040 | barline_parse | cpp/inconsistent-null-check | 1153 | FP | FP | 在调用 `vim_strnsave` 之前，切片代码已通过 `if (s != buf && allocated && !converted)` 条件确保 `s` 不是指向已分配的 `buf` 且 `allocated` 为真，这表明... |
| 866 | vim-9.1.1040 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | 代码中使用了STRCAT宏，但NameBuff是一个固定大小的全局缓冲区，且告警点之前的操作（STRCPY和STRLEN）以及后续的路径拼接逻辑表明，拼接的字符串长度受限于已知的目录名和固定后缀，在切片可见范围内未发现明显的缓冲区溢出风险。 |
| 867 | vim-9.1.1040 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 代码中`name`的来源是有限的静态字符串或受控的字符数组`namebuf`，其长度最大为3（如"F12"），而`buf`在拼接前已被初始化为空字符串。虽然未明确检查`buf`的剩余大小，但根据上下文，拼接的字符串总长度极短，缓冲区溢... |
| 868 | vim-9.1.1040 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏前，已通过vim_strncpy将目标缓冲区newword初始化为安全长度（MAXWLEN-1），并确保源字符串p来自受控的word变量，且其长度已通过wordlen和chop字符串长度检查，缓冲区溢出风险已被... |
| 870 | vim-9.1.1040 | highlight_color | cpp/overrunning-write | 3259 | FP | FP | sprintf 格式化字符串为固定的 "#%02x%02x%02x"，输出长度固定为7个字符（'#' + 6个十六进制数字），目标缓冲区 buf 大小为10字节，足够容纳，不存在缓冲区溢出风险。 |
| 871 | vim-9.1.1040 | msg_outnum | cpp/overrunning-write | 1653 | FP | FP | 目标缓冲区 `buf` 大小为20字节，而格式化输出一个 `long` 类型整数 `n` 所需的最大字节数（包括负号和终止符）为21字节，存在缓冲区溢出的理论风险。但结合 `label` 为 FP（算法推测为误报）以及该函数在后续版本... |
| 873 | vim-9.1.1040 | ga_concat_strings | cpp/unbounded-write | 788 | FP | FP | 代码中已通过循环预先计算了目标缓冲区 `s` 的总长度 `len` 并分配了 `len + 1` 的空间，随后使用 `STRCPY`（即 `strcpy`）进行复制，缓冲区大小是足够的，不存在溢出风险。 |
| 874 | vim-9.1.1040 | maketitle | cpp/unbounded-write | 4147 | FP | FP | 切片代码显示，在调用STRCPY(icon_str, p)之前，已通过`len = (int)STRLEN(p);`和后续的截断逻辑（如`if (len > 100) len -= 100;`）限制了源字符串p的长度，且目标缓冲区ic... |
| 875 | vim-9.1.1040 | buf_write | cpp/unbounded-write | 1208 | FP | FP | 代码中使用了STRCPY宏（即strcpy），但目标缓冲区IObuff的大小未在切片中明确给出，且告警点位于一个循环中用于生成临时文件名，源字符串fname是函数参数（文件名）。在上下文中，fname通常来自用户输入或文件系统，长度可... |
| 876 | vim-9.1.1040 | buf_write | cpp/unbounded-write | 2566 | FP | FP | 切片代码中未发现对 strcat 的调用，告警消息提及的 'call to strcat' 在提供的代码片段中不存在。该告警可能是基于不完整或过时的分析，且参考标签为 FP，表明在后续版本中该告警未被修复，倾向于误报。 |
| 877 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2138 | FP | FP | 代码中使用了宏STRCAT，该宏展开为strcat，但目标缓冲区'leader'的大小是通过alloc动态分配的，其大小计算包含了lead_len、lead_repl_len、extra_space、extra_len和second_... |
| 878 | vim-9.1.1040 | transstr | cpp/unbounded-write | 400 | FP | FP | 切片代码显示，目标缓冲区 `res` 的大小已通过 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 精确分配，足以容纳源字符串 `s` 转换后的结果。`STRCAT` 宏用于拼接 `tra... |
| 879 | vim-9.1.1040 | globpath | cpp/unbounded-write | 3809 | FP | FP | 切片代码中，在调用STRCAT之前，存在明确的长度检查 `if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`，确保拼接后的字符串不会超过目标缓冲区buf的大小（MAXPATHL）。因此，该告... |
| 880 | vim-9.1.1040 | win_redr_status_matches | cpp/unbounded-write | 640 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为buf分配了足够的内存（Columns * MB_MAXBYTES + 1 或 Columns + 1），并且后续逻辑严格控制了写入长度不超过Columns，因此不存在缓冲... |
| 881 | vim-9.1.1040 | win_redr_status_matches | cpp/unbounded-write | 659 | FP | FP | 切片代码显示，目标缓冲区 `buf` 的大小已通过 `alloc(Columns + 1)` 或 `alloc(Columns * MB_MAXBYTES + 1)` 根据屏幕列数安全分配，且写入操作在循环中受 `(long)(cle... |
| 882 | vim-9.1.1040 | debuggy_find | cpp/unbounded-write | 1067 | FP | FP | 代码中 `STRCPY` 的目标缓冲区 `name` 已通过 `alloc(STRLEN(fname) + 3)` 分配了足够空间（源字符串长度加3），且分配大小计算正确，不存在缓冲区溢出风险。 |
| 883 | vim-9.1.1040 | has_profiling | cpp/unbounded-write | 973 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为pe->pen_name分配了足够的内存，大小为STRLEN(fname) + 1，确保了目标缓冲区大小与源字符串长度匹配，因此不会发生缓冲区溢出。 |
| 884 | vim-9.1.1040 | ex_diffpatch | cpp/unbounded-write | 1363 | FP | FP | 告警针对的 STRCPY(buf, tmp_new) 调用中，buf 的大小 buflen 已通过 alloc(buflen) 分配，且 buflen 的计算包含了 tmp_new 的长度加上额外字节，确保目标缓冲区足够容纳源字符串。... |
| 885 | vim-9.1.1040 | do_string_sub | cpp/unbounded-write | 7726 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过ga_grow函数确保了目标缓冲区ga.ga_data有足够的空间容纳源字符串tail，因此不会发生缓冲区溢出。 |
| 886 | vim-9.1.1040 | set_var_const | cpp/unbounded-write | 4184 | FP | FP | 代码中STRCPY宏的目标缓冲区di->di_key的大小已通过alloc分配，大小为STRLEN(varname) + 1，与源字符串长度精确匹配，不存在缓冲区溢出风险。 |
| 887 | vim-9.1.1040 | cat_prefix_varname | cpp/unbounded-write | 2505 | FP | FP | 代码在调用STRCPY（即strcpy）前，通过动态内存分配确保了目标缓冲区varnamebuf的大小足以容纳源字符串name（长度计算为STRLEN(name)+3，并额外预留了10字节空间），因此不存在缓冲区溢出的风险。 |
| 888 | vim-9.1.1040 | ex_substitute | cpp/unbounded-write | 4883 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的strcat溢出风险在提供的代码片段中不存在。代码主要处理正则表达式替换逻辑，使用vim_strsave、STRCAT宏等安全的内存操作。因此判定为工具误报。 |
| 889 | vim-9.1.1040 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区分配了精确计算的长度，且该长度包含了源字符串长度和终止符，因此不会发生缓冲区溢出。告警是基于对strcpy的通用检测，未考虑此处精确的长度控制。 |
| 890 | vim-9.1.1040 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 代码在调用STRCAT（即strcat）前，已通过alloc(len)分配了缓冲区，且长度len已通过计算包含了所有待拼接字符串的长度和终止符，因此缓冲区大小是充足的，不存在溢出风险。 |
| 891 | vim-9.1.1040 | ex_sort | cpp/unbounded-write | 605 | FP | FP | 代码中目标缓冲区 `sortbuf1` 的大小为 `maxlen + 1`，而源字符串 `s` 的长度 `len` 已通过 `ml_get_len` 获取，且 `maxlen` 是循环中计算出的最大 `len` 值。因此 `STRCP... |
| 892 | vim-9.1.1040 | expand_sfile | cpp/unbounded-write | 10068 | FP | FP | 切片代码显示，目标缓冲区 `newres` 的大小通过 `alloc(resultlen + 1)` 分配，其中 `resultlen` 已根据源字符串 `repl` 的长度 `repllen` 和待替换部分长度 `srclen` 精... |
| 893 | vim-9.1.1040 | repl_cmdline | cpp/unbounded-write | 5307 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(i)为目标缓冲区new_cmdline分配了足够的内存，其中i的计算包含了源字符串长度、替换字符串长度和尾部长度，并额外预留了空间，因此缓冲区大小是充足的，不存在溢出风险。 |
| 894 | vim-9.1.1040 | repl_cmdline | cpp/unbounded-write | 5313 | FP | FP | 代码通过alloc(i)为目标缓冲区new_cmdline分配了精确计算的长度i，该长度已包含源字符串长度、替换长度、尾部长度及终止符空间，因此后续使用STRCPY（即strcpy）是安全的，不会发生缓冲区溢出。 |
| 895 | vim-9.1.1040 | replace_makeprg | cpp/unbounded-write | 5014 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为目标缓冲区分配了足够的空间，空间大小由源字符串长度精确计算得出，因此不存在缓冲区溢出的风险。 |
| 896 | vim-9.1.1040 | replace_makeprg | cpp/unbounded-write | 5029 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc函数为目标缓冲区分配了足够的内存，分配的大小为program_len + STRLEN(p) + 2，这确保了目标缓冲区能够容纳源字符串。因此，不存在缓冲区溢出的风险。 |
| 897 | vim-9.1.1040 | do_one_cmd | cpp/unbounded-write | 2678 | FP | FP | 切片代码中未发现对STRCPY宏的直接调用，该宏被定义为strcpy。告警指向的代码行（2678）在do_one_cmd函数中，但切片内该行附近没有STRCPY的使用。告警可能基于数据流分析，但切片中缺乏具体证据表明存在未受保护的st... |
| 898 | vim-9.1.1040 | discard_exception | cpp/unbounded-write | 646 | FP | FP | 告警点 `STRCPY(IObuff, saved_IObuff)` 中，目标缓冲区 `IObuff` 是全局缓冲区，其大小 `IOSIZE` 在代码中未直接给出但应是固定的；源字符串 `saved_IObuff` 是之前通过 `vi... |
| 899 | vim-9.1.1040 | get_exception_string | cpp/unbounded-write | 473 | FP | FP | 切片代码显示，目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度已计算了源字符串 `mesg` 或 `p` 的长度，并预留了空字符。`STRCAT` 宏在此上下文中不会导致缓冲区溢出，因为目标缓冲区... |
| 900 | vim-9.1.1040 | get_exception_string | cpp/unbounded-write | 484 | FP | FP | 代码通过`vim_strnsave`为目标缓冲区`ret`分配了精确的长度（4 + cmdlen + 2 + STRLEN(mesg) 或 4 + STRLEN(mesg)），确保缓冲区大小足以容纳`sprintf`写入的格式化字符串... |
| 901 | vim-9.1.1040 | escape_fname | cpp/unbounded-write | 4105 | FP | FP | 代码在调用STRCPY（即strcpy）前，为目标缓冲区p分配了精确的内存大小（STRLEN(*pp) + 2），确保了缓冲区足以容纳源字符串和额外的字符，因此不存在缓冲区溢出的风险。 |
| 902 | vim-9.1.1040 | cmdline_browse_history | cpp/unbounded-write | 1494 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc_cmdbuff函数为目标缓冲区ccline.cmdbuff分配了足够空间，且分配的长度plen等于源字符串的长度，因此不会发生缓冲区溢出。 |
| 903 | vim-9.1.1040 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 860 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过realloc_cmdbuff(len + 1)为目标缓冲区ccline.cmdbuff重新分配了足够的内存（len + 1字节），其中len是源字符串p的长度。这确保了... |
| 904 | vim-9.1.1040 | vim_settempdir | cpp/unbounded-write | 5286 | FP | FP | 告警点位于 `STRCPY(buf, tempdir)`，但切片显示 `buf` 已通过 `alloc(MAXPATHL + 2)` 分配了固定大小的缓冲区（MAXPATHL + 2），且 `tempdir` 参数是函数传入的路径，其... |
| 905 | vim-9.1.1040 | vim_rename | cpp/unbounded-write | 3858 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。切片中可见明确... |
| 906 | vim-9.1.1040 | buf_modname | cpp/unbounded-write | 3636 | FP | FP | 代码中通过 alloc 为目标缓冲区分配了精确大小（fnamelen + extlen + 3），且 STRCPY 复制的源字符串 fname 长度已通过 STRLEN 获取并用于分配，因此不会发生缓冲区溢出。 |
| 907 | vim-9.1.1040 | addfile | cpp/unbounded-write | 4202 | FP | FP | 代码在调用STRCPY（即strcpy）前，已使用alloc(STRLEN(f) + 1 + isdir)为目标缓冲区p分配了精确的内存空间，大小为源字符串f的长度加1（以及可能的目录分隔符）。这确保了目标缓冲区足够容纳源字符串，因此... |
| 908 | vim-9.1.1040 | unix_expandpath | cpp/unbounded-write | 3837 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`buf`在调用前已通过`alloc(buflen)`分配，其中`buflen = STRLEN(path) + MAXPATHL`，且源字符串`s`是`buf`的一部分，`path_end + ... |
| 909 | vim-9.1.1040 | concat_fnames | cpp/unbounded-write | 3127 | FP | FP | 代码通过alloc函数为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcpy操作不会发生缓冲区溢出。 |
| 910 | vim-9.1.1040 | concat_fnames | cpp/unbounded-write | 3130 | FP | FP | 代码通过alloc函数为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcat操作不会发生缓冲区溢出。 |
| 911 | vim-9.1.1040 | uniquefy_paths | cpp/unbounded-write | 2364 | FP | FP | 切片代码显示，`file_pattern` 缓冲区是通过 `alloc(len + 2)` 分配的，其中 `len` 是输入 `pattern` 的长度。`STRCAT` 操作是将 `pattern` 追加到已初始化为 `"*"` 的... |
| 912 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1718 | FP | FP | 切片代码中 STRCPY 宏的目标缓冲区 NameBuff 大小为 MAXPATHL，且调用前通过 STRLEN(rel_fname) + l < MAXPATHL 进行了长度校验，确保不会发生缓冲区溢出。 |
| 913 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1719 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区NameBuff大小为MAXPATHL，而源字符串*file_to_find或rel_fname在复制前已通过expand_env_esc处理并存入NameBuff，且后续有长度检查确保STRLE... |
| 914 | vim-9.1.1040 | find_file_in_path_option | cpp/unbounded-write | 1724 | FP | FP | 代码中 STRCPY 的目标缓冲区 NameBuff 大小为 MAXPATHL，而源字符串 *file_to_find 在复制前已通过 expand_env_esc 处理并限制在 MAXPATHL 内，且后续有长度检查确保不会溢出。 |
| 915 | vim-9.1.1040 | ff_check_visited | cpp/unbounded-write | 1370 | FP | FP | 告警点 `STRCPY(vp->ffv_fname, ff_expand_buffer)` 的目标缓冲区 `vp->ffv_fname` 的大小已通过 `alloc(offsetof(ff_visited_T, ffv_fname) ... |
| 916 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 805 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，均存在明确的长度检查（例如`if (STRLEN(search_ctx->ffsc_start_dir) + 1 < MAXPATHL)`），确保目标缓冲区`file_path`（... |
| 917 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 819 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，明确进行了长度检查（STRLEN(file_path) + STRLEN(stackp->ffs_fix_path) + 1 < MAXPATHL），确保目标缓冲区不会溢出。因此该... |
| 918 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 940 | FP | FP | 代码在调用STRCPY（即strcpy）前，通过STRLEN计算了源字符串和目标缓冲区的总长度，并与MAXPATHL常量进行了明确的边界检查，确认不会发生缓冲区溢出后才执行拷贝操作。切片中可见的防护逻辑使得告警无效。 |
| 919 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 942 | FP | FP | 切片代码中所有使用STRCAT（即strcat）的地方，在拼接前都通过STRLEN计算了目标缓冲区剩余空间并与MAXPATHL常量进行了比较，确认不会发生缓冲区溢出。例如，在告警行号附近，代码有`if (STRLEN(file_pat... |
| 920 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 1110 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，均存在明确的长度检查（例如使用STRLEN计算长度并与MAXPATHL比较），确保目标缓冲区不会溢出。因此，该告警为误报。 |
| 921 | vim-9.1.1040 | vim_findfile | cpp/unbounded-write | 1112 | FP | FP | 切片代码中所有对STRCAT的调用前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区不会溢出。因此，该告警为误报。 |
| 922 | vim-9.1.1040 | <global> | cpp/unbounded-write | 537 | FP | FP | 切片代码中，`ff_expand_buffer` 在告警行（`STRCPY(ff_expand_buffer, search_ctx->ffsc_start_dir);`）之前已通过 `ff_expand_buffer = alloc... |
| 923 | vim-9.1.1040 | <global> | cpp/unbounded-write | 545 | FP | FP | 切片代码中所有STRCPY宏的使用，其目标缓冲区（如`ff_expand_buffer`、`buf`）均经过`alloc`分配，且分配大小（如`MAXPATHL`或计算出的`eb_len + ...`）是明确的，源字符串长度在切片内未... |
| 924 | vim-9.1.1040 | <global> | cpp/unbounded-write | 548 | FP | FP | 切片代码显示，`ff_expand_buffer` 在函数开头通过 `alloc(MAXPATHL)` 分配了固定大小的缓冲区（MAXPATHL），且告警处的 `STRCAT` 操作是在经过 `mch_isdir` 检查、路径拼接长度... |
| 925 | vim-9.1.1040 | <global> | cpp/unbounded-write | 590 | FP | FP | 切片代码中，`STRCPY` 宏的目标缓冲区 `temp` 是通过 `alloc` 分配的，其大小计算为源字符串长度之和加1，确保了缓冲区足够容纳复制的内容，因此不存在缓冲区溢出的风险。 |
| 926 | vim-9.1.1040 | <global> | cpp/unbounded-write | 591 | FP | FP | 切片代码中，STRCAT 的目标缓冲区 `temp` 是通过 `alloc` 分配的，其大小为源字符串长度之和加1，确保了缓冲区足够容纳拼接后的字符串，因此不存在缓冲区溢出风险。 |
| 927 | vim-9.1.1040 | <global> | cpp/unbounded-write | 3798 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够大小的缓冲区，该缓冲区大小计算包含了源字符串s的长度，因此不会发生缓冲区溢出。 |
| 928 | vim-9.1.1040 | foldDelMarker | cpp/unbounded-write | 1897 | FP | FP | 代码中`newline`缓冲区的大小通过`alloc(ml_get_len(lnum) - len + 1)`精确计算，其长度等于原行长减去被删除标记的长度再加1（用于空字符）。随后使用`STRCPY`（即`strcpy`）将剩余字符... |
| 929 | vim-9.1.1040 | foldAddMarker | cpp/unbounded-write | 1815 | FP | FP | 切片代码显示，目标缓冲区 `newline` 的大小通过 `alloc(line_len + markerlen + STRLEN(cms) + 1)` 动态分配，其大小足以容纳源字符串 `line` 加上一个终止符。`STRCPY`... |
| 930 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2899 | FP | FP | 告警点 `STRCPY(buffer, res_prolog->title);` 中，`buffer` 是大小为256的局部数组，而 `res_prolog->title` 来自受控的PostScript资源文件，其长度在 `prt_... |
| 931 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2901 | FP | FP | 告警点 `STRCAT(buffer, res_prolog->version);` 中，`buffer` 是大小为 256 的局部数组，其内容由 `STRCPY(buffer, res_prolog->title);` 初始化。`r... |
| 932 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2905 | FP | FP | 告警指向的 `STRCPY(buffer, res_cidfont->title);` 操作中，`res_cidfont->title` 来源于受控的资源文件解析，其长度在 `prt_open_resource` 函数中已被限制为不超... |
| 933 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_cidfont->title`和`res_cidfont->version`来自受控的PostScript资源文件，其内容在`prt_open_resource`中经过解析和长度... |
| 934 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 告警指向的 `STRCPY(buffer, res_cmap->title);` 操作中，`buffer` 是局部数组 `char buffer[256];`，而 `res_cmap->title` 的来源已在 `prt_open_r... |
| 935 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 切片代码显示，`res_cmap->title` 和 `res_cmap->version` 是从受控的 PostScript 资源文件中解析出来的，其长度在 `prt_open_resource` 函数中通过 `vim_strncp... |
| 936 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2920 | FP | FP | 告警点 `STRCPY(buffer, res_encoding->title);` 的目标缓冲区 `buffer` 大小为256字节，而源数据 `res_encoding->title` 来自受控的资源文件，其长度在 `prt_op... |
| 937 | vim-9.1.1040 | mch_print_begin | cpp/unbounded-write | 2922 | FP | FP | 切片代码显示，`buffer` 数组大小为256字节，而 `res_encoding->title` 和 `res_encoding->version` 是从受控的PostScript资源文件中解析出的固定字符串，其长度在解析时已被限... |
| 938 | vim-9.1.1040 | prt_resource_name | cpp/unbounded-write | 1659 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，已通过STRLEN检查了源字符串`filename`的长度是否小于MAXPATHL，若长度超过或等于MAXPATHL，则会将目标缓冲区首字节置为NUL，从而避免了缓冲区溢出。该前置... |
| 939 | vim-9.1.1040 | do_helptags | cpp/unbounded-write | 1210 | FP | FP | 代码中使用了STRCPY宏，但目标缓冲区NameBuff是一个全局或静态缓冲区，其大小在切片中未定义，但根据上下文（用于构建文件路径）和Vim项目的惯例，它通常被定义为足够大（如MAXPATHL）以容纳典型路径。此外，告警点STRCP... |
| 940 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 975 | FP | FP | 告警指向的 `STRCAT(NameBuff, ext);` 语句中，`ext` 参数是函数传入的常量字符串（如 ".txt"），其长度固定且很短，而 `NameBuff` 是一个大小为 `MAXPATHL` 的缓冲区，在切片中未见其... |
| 941 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 991 | FP | FP | 代码中使用了`NameBuff`缓冲区，但切片中未提供其大小定义，无法确认`STRCAT`操作是否会导致溢出。结合告警描述和参考标签`FP`，倾向于认为缓冲区大小足够或存在其他防护机制，判定为误报。 |
| 942 | vim-9.1.1040 | helptags_one | cpp/unbounded-write | 1112 | FP | FP | 代码中 `sprintf` 的目标缓冲区 `s` 是通过 `alloc(p2 - p1 + STRLEN(fname) + 2)` 动态分配的，其大小精确计算为标签字符串长度加文件名长度再加分隔符和终止符，因此不会发生缓冲区溢出。 |
| 943 | vim-9.1.1040 | highlight_set_startstop_termcode | cpp/unbounded-write | 1481 | FP | FP | 代码在调用STRCAT前，通过`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了目标缓冲区buf（大小为100）的剩余空间，确保不会发生缓冲区溢出。这是一个有效的防护机制。 |
| 944 | vim-9.1.1040 | load_colors | cpp/unbounded-write | 602 | FP | FP | 缓冲区 `buf` 的大小通过 `alloc(STRLEN(name) + 12)` 分配，其中 `+12` 对应了固定字符串 `"colors/.vim"` 的长度（包含终止符）。`sprintf` 写入的格式字符串长度正好是 `S... |
| 945 | vim-9.1.1040 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | FP | 代码在调用 sprintf 前，已通过 alloc(len) 为目标缓冲区分配了精确计算的长度 len，该长度已包含源字符串和分隔符，因此不会发生缓冲区溢出。 |
| 946 | vim-9.1.1040 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了该大小的内存，确保了目标缓冲区足以容纳格式化后的字符串，因此不存在缓冲区溢出风险。 |
| 947 | vim-9.1.1040 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt = strlen(...) + ...），并动态分配了该大小的内存（buf = alloc(amt)），确保了目标缓冲区足够大，不会发生溢出。 |
| 948 | vim-9.1.1040 | <global> | cpp/unbounded-write | 1456 | FP | FP | 目标缓冲区 csinfo[i].fname 的大小通过 alloc(strlen(fname)+1) 精确分配，与源字符串 fname 的长度匹配，strcpy 操作不会导致缓冲区溢出。 |
| 949 | vim-9.1.1040 | <global> | cpp/unbounded-write | 1465 | FP | FP | 切片代码显示，在调用strcpy之前，已经使用alloc(strlen(fname)+1)为目标缓冲区分配了精确匹配源字符串长度的内存，因此不会发生缓冲区溢出。 |
| 950 | vim-9.1.1040 | cs_add_common | cpp/unbounded-write | 604 | FP | FP | 代码中 `fname2` 的缓冲区大小通过 `alloc(strlen(CSCOPE_DBFILE) + strlen(fname) + 2)` 精确计算，与后续 `sprintf` 的格式字符串 `"%s/%s"` 完全匹配，不会发... |
| 951 | vim-9.1.1040 | ins_compl_infercase_gettext | cpp/unbounded-write | 653 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，程序已通过条件`(p - IObuff) + 6 >= IOSIZE`确保目标缓冲区`gap.ga_data`有足够空间（通过`ga_grow(&gap, IOSIZE)`分配）... |
| 952 | vim-9.1.1040 | <global> | cpp/unbounded-write | 3129 | FP | FP | 切片代码显示，在告警的`sprintf`调用附近，存在使用安全的`vim_snprintf`函数进行缓冲区长度控制的模式，且`args->os_errbuf`缓冲区大小在上下文中可能已受约束。结合算法标签为FP，倾向于判定为误报。 |
| 953 | vim-9.1.1040 | findswapname | cpp/unbounded-write | 4967 | FP | FP | 代码中STRCPY的目标缓冲区fname2是通过alloc(n + 2)分配的，其中n是源字符串fname的长度，分配大小比源字符串多2个字节，确保了足够的空间，不会发生缓冲区溢出。 |
| 954 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2157 | FP | FP | 代码通过 `alloc(STRLEN(f) + 1)` 为目标缓冲区 `s` 分配了精确匹配源字符串 `f` 长度的空间，然后执行 `STRCPY(s, f)`，这确保了不会发生缓冲区溢出。告警是基于对 `strcpy` 的通用检测，... |
| 955 | vim-9.1.1040 | <global> | cpp/unbounded-write | 811 | FP | FP | 代码中使用了宏STRCPY，但目标缓冲区menu->strings[i]是通过alloc(STRLEN(call_data) + 5)分配的，大小明确为源字符串长度加5，确保了足够的空间，因此不会发生缓冲区溢出。 |
| 956 | vim-9.1.1040 | <global> | cpp/unbounded-write | 815 | FP | FP | 切片代码中，STRCPY宏被用于将已知长度的字符串（call_data）复制到新分配的内存（menu->strings[i]）中，该内存大小已通过alloc(STRLEN(call_data) + 5)精确分配，确保了目标缓冲区足够大... |
| 957 | vim-9.1.1040 | msg_show_console_dialog | cpp/unbounded-write | 4502 | FP | FP | 切片代码显示，目标缓冲区 `confirm_msg` 的长度 `len` 已通过计算 `STRLEN(message)` 等字符串长度并加上额外开销来精确分配，`STRCPY` 操作的目标地址 `confirm_msg + 1` 和源... |
| 958 | vim-9.1.1040 | str2specialbuf | cpp/unbounded-write | 2017 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度小于传入的长度参数`len`... |
| 959 | vim-9.1.1040 | get_emsg_source | cpp/unbounded-write | 502 | FP | FP | 代码在调用sprintf前，使用alloc(STRLEN(sname) + STRLEN(p))为目标缓冲区分配了足够的空间，其大小等于两个字符串长度之和，这确保了格式化后的字符串不会溢出。 |
| 960 | vim-9.1.1040 | may_trigger_modechanged | cpp/unbounded-write | 2836 | FP | FP | STRCPY的目标缓冲区`last_mode`和源缓冲区`curr_mode`大小均为`MODE_MAX_LENGTH`，且`curr_mode`由`get_mode`函数内部填充，其长度受该函数逻辑严格控制，不会超过`MODE_MA... |
| 961 | vim-9.1.1040 | expand_env_esc | cpp/unbounded-write | 1647 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，已通过条件`(STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen)`检查了目标缓冲区`dst`的剩余空间`dstlen`，确保不会发... |
| 962 | vim-9.1.1040 | call_shell | cpp/unbounded-write | 1877 | FP | FP | 切片代码显示，在调用STRCAT前，已通过alloc为ncmd分配了足够的内存，其大小为STRLEN(ecmd) + STRLEN(p_sxq) * 2 + 1，这包含了源字符串和两个目标字符串的长度及终止符，因此缓冲区大小是经过计算... |
| 963 | vim-9.1.1040 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中不可见。该告警可能是基于对宏（如STRCAT）的静态分析，但切片中未显示具体的易受攻击的代码路径。结合参考标签FP，判定为误报。 |
| 964 | vim-9.1.1040 | nb_reply_text | cpp/unbounded-write | 802 | FP | FP | 代码通过alloc(STRLEN(result) + 32)为目标缓冲区分配了足够的空间，其中32字节用于存放格式化字符串的固定部分，因此sprintf不会导致缓冲区溢出。 |
| 965 | vim-9.1.1040 | push_showcmd | cpp/unbounded-write | 1808 | FP | FP | 告警针对的是宏STRCPY（即strcpy）的使用，但切片代码显示源缓冲区（showcmd_buf）和目标缓冲区（old_showcmd_buf）是固定大小的内部缓冲区，且没有证据表明源数据来自外部不可控输入。在给定的切片上下文中，这... |
| 966 | vim-9.1.1040 | add_to_showcmd | cpp/unbounded-write | 1763 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已计算了目标缓冲区showcmd_buf的当前长度old_len和待追加字符串p的长度extra_len，并检查了溢出（overflow）。如果溢出，会通过mch_memmove移... |
| 967 | vim-9.1.1040 | op_change | cpp/unbounded-write | 2003 | FP | FP | 切片代码中，STRCPY宏被用于将`oldp + bd.textcol`复制到`newp + newlen + ins_len`处，其中`newp`已通过`alloc`分配了足够大小（`ml_get_len(linenr) + vpo... |
| 968 | vim-9.1.1040 | op_replace | cpp/unbounded-write | 1299 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`newp`是通过`alloc(oldlen + 1 + n)`分配的，其大小`oldlen + 1 + n`已明确计算并包含了源字符串`oldp + bd.textcol + bd.textle... |
| 969 | vim-9.1.1040 | op_replace | cpp/unbounded-write | 1308 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区after_p是通过alloc(oldlen + 1 + n - newlen)动态分配的，其大小计算基于已知的oldlen、n和newlen，且newlen在之前已精确计算。目标缓冲区大小足够容... |
| 970 | vim-9.1.1040 | op_delete | cpp/unbounded-write | 962 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`newp`是使用`alloc(ml_get_len(lnum) + 1 - n)`分配的，其大小已根据源字符串长度和删除的字符数`n`精确计算，确保了目标缓冲区足够容纳源字符串，因此不存在缓冲区... |
| 971 | vim-9.1.1040 | block_insert | cpp/unbounded-write | 743 | FP | FP | 切片代码显示，目标缓冲区 `newp` 的大小是通过 `alloc` 动态分配的，其大小计算包含了源字符串长度 `ml_get_len(lnum)`、插入内容长度 `slen` 以及必要的空格填充，确保了缓冲区足够容纳 `STRCPY... |
| 972 | vim-9.1.1040 | option_value2string | cpp/unbounded-write | 8324 | FP | FP | 切片代码显示，告警点 STRCPY 的目标缓冲区是 NameBuff，但切片中未提供其大小定义。然而，在 P_STRING 分支中，后续对 NameBuff 的操作（如 vim_strncpy）明确使用了 MAXPATHL 作为长度限... |
| 973 | vim-9.1.1040 | option_value2string | cpp/unbounded-write | 8326 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区NameBuff大小未知，但告警点位于处理数值选项（P_NUM）的分支，其输入来自内部函数get_special_key_name或transchar，这些函数返回内部静态缓冲区或受控字符串，并非... |
| 974 | vim-9.1.1040 | stropt_expand_envvar | cpp/unbounded-write | 1803 | FP | FP | 代码通过alloc(newlen)为目标缓冲区newval分配了精确的内存大小，newlen已通过STRLEN(s) + 1计算并可能加上origval的长度，因此STRCPY（即strcpy）的写入不会超出分配的空间。切片中可见充分... |
| 975 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 6989 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过alloc(len)为目标缓冲区command分配了精确计算的长度len，该长度已考虑了所有待拼接字符串（包括环境变量、函数名等）的总和，因此不存在缓冲区溢出的风险。 |
| 976 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 7029 | FP | FP | 代码在调用STRCAT前，通过alloc(len)为目标缓冲区command分配了精确计算的长度len，该长度已考虑了所有待拼接字符串（包括tempname）的总和，因此不存在缓冲区溢出的风险。 |
| 977 | vim-9.1.1040 | mch_expand_wildcards | cpp/unbounded-write | 7335 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`p`是通过`alloc(STRLEN((*file)[i]) + 1 + dir)`分配的，其大小精确匹配源字符串长度加可能的路径分隔符，确保了缓冲区足够大，不会发生溢出。 |
| 978 | vim-9.1.1040 | mch_FullName | cpp/unbounded-write | 2819 | FP | FP | 切片代码在调用STRCAT（即strcat）前，已通过条件`(int)(STRLEN(buf) + STRLEN(fname)) >= len`检查了目标缓冲区`buf`的剩余空间是否足以容纳源字符串`fname`，该检查能有效防止缓... |
| 979 | vim-9.1.1040 | qf_store_title | cpp/unbounded-write | 1934 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc_id分配了大小为STRLEN(title) + 2的内存，目标缓冲区大小明确基于源字符串长度计算，因此不会发生缓冲区溢出。 |
| 980 | vim-9.1.1040 | reg_submatch | cpp/unbounded-write | 2723 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区retval分配了精确的长度len，该长度是根据匹配的起始和结束位置计算得出的。这确保了目标缓冲区大小足以容纳源字符串，因此不存在缓冲区溢出... |
| 981 | vim-9.1.1040 | reg_submatch | cpp/unbounded-write | 2732 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区分配了精确的长度len，该长度是根据匹配的起始和结束位置计算得出的，确保了缓冲区大小足以容纳要复制的数据，因此不存在缓冲区溢出的风险。 |
| 982 | vim-9.1.1040 | regtilde | cpp/unbounded-write | 1959 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过`tmpsublen > MAXCOL`的检查限制了目标缓冲区`tmpsub`的最大长度，且`tmpsub`的大小为`tmpsublen + 1`，与拷贝的数据长度`pos... |
| 983 | vim-9.1.1040 | match_with_backref | cpp/unbounded-write | 1600 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过动态内存分配确保目标缓冲区reg_tofree的长度（reg_tofreelen）不小于源字符串rex.line的长度（len）。该分配策略（len = STRLEN(re... |
| 984 | vim-9.1.1040 | get_reg_contents | cpp/unbounded-write | 2733 | FP | FP | 切片代码显示，目标缓冲区 `retval` 的大小已通过精确计算（`len`）并分配了 `len + 1` 字节，随后使用 `STRCPY`（即 `strcpy`）进行复制。由于源字符串 `y_current->y_array[i].... |
| 985 | vim-9.1.1040 | do_put | cpp/unbounded-write | 2159 | FP | FP | 切片代码中使用了STRCPY宏，但目标缓冲区newp是通过alloc函数分配的内存，其大小计算为(ml_get_len(lnum) - col + totlen + 1)，其中totlen为源字符串长度，这确保了目标缓冲区足够容纳源字... |
| 986 | vim-9.1.1040 | do_put | cpp/unbounded-write | 2160 | FP | FP | 切片代码中使用了STRCPY宏，但目标缓冲区newp是通过alloc(totlen + oldlen + 1)分配的，其大小明确为源字符串长度加上目标字符串长度再加1，确保了缓冲区足够大，不会发生溢出。 |
| 987 | vim-9.1.1040 | op_yank | cpp/unbounded-write | 1315 | FP | FP | 代码中STRCPY宏的目标缓冲区pnew是通过alloc函数分配的内存，其大小已精确计算为两个字符串长度之和加1，确保了缓冲区足够容纳拼接后的字符串，因此不存在缓冲区溢出风险。 |
| 988 | vim-9.1.1040 | op_yank | cpp/unbounded-write | 1316 | FP | FP | 代码中STRCPY宏的目标缓冲区pnew是通过alloc函数精确分配了足够大小的内存，其大小为两个源字符串长度之和加1，因此不会发生缓冲区溢出。 |
| 989 | vim-9.1.1040 | stuff_yank | cpp/unbounded-write | 470 | FP | FP | 切片代码显示，目标缓冲区 `tmp` 的大小是 `tmplen + 1`，而 `tmplen` 是源字符串 `pp->string` 的长度 `pp->length` 与 `p` 的长度 `plen` 之和。`STRCPY` 宏展开为... |
| 990 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2838 | FP | FP | 目标缓冲区 `scriptname` 的大小通过 `alloc(STRLEN(name) + 14)` 分配，其长度足以容纳固定前缀 "autoload/"、处理后的 `name` 字符串以及后缀 ".vim"。在切片可见范围内，`S... |
| 991 | vim-9.1.1040 | ExpandPackAddDir | cpp/unbounded-write | 1309 | FP | FP | 代码中目标缓冲区`s`的大小为`pat_len + 26`，而`sprintf`的格式化字符串为固定长度'pack/*/opt/%s*'，其中变量部分`pat`的长度已通过`STRLEN`获取并计入缓冲区大小计算，因此格式化后的总长度... |
| 992 | vim-9.1.1040 | sign_jump | cpp/unbounded-write | 1313 | FP | FP | 代码通过 `alloc(STRLEN(buf->b_fname) + 25)` 为目标缓冲区分配了足够的空间，其大小为文件名长度加上固定开销，因此 `sprintf` 不会发生缓冲区溢出。 |
| 993 | vim-9.1.1040 | dump_word | cpp/unbounded-write | 4187 | FP | FP | STRCPY宏的目标缓冲区badword大小为MAXWLEN+10，源p来自word或cword，而cword大小为MAXWLEN，且切片中未显示word长度超过MAXWLEN+10的证据。结合label为FP，倾向于判定为误报。 |
| 994 | vim-9.1.1040 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 告警点位于 `make_case_word` 函数中，该函数仅在特定条件下（非 `WF_ALLCAP` 且非 `WF_ONECAP`）才会调用 `STRCPY`（即 `strcpy`）。调用 `STRCPY` 的两个参数 `cword... |
| 995 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2998 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区p分配了足够的内存（ml_get_curline_len() + addlen + 1），且源字符串repl_to的长度repl_to_len在分配时已考虑，因此缓冲区大小是安... |
| 996 | vim-9.1.1040 | <global> | cpp/unbounded-write | 2999 | FP | FP | 代码在调用STRCAT前，已为目标缓冲区p分配了足够的内存（ml_get_curline_len() + addlen + 1），其中addlen已考虑了替换字符串的长度差，因此缓冲区大小是经过计算且足够的，不存在缓冲区溢出的风险。 |
| 997 | vim-9.1.1040 | count_common_word | cpp/unbounded-write | 1919 | FP | FP | 切片代码显示，目标缓冲区 `wc->wc_word` 的大小是动态分配的，其大小为 `STRLEN(p) + 1`，与源字符串 `p` 的长度精确匹配。`STRCPY` 宏展开为 `strcpy`，由于目标缓冲区大小与源字符串长度一致... |
| 998 | vim-9.1.1040 | spell_load_lang | cpp/unbounded-write | 1632 | FP | FP | 告警点 `STRCPY(sl.sl_lang, lang)` 中，目标缓冲区 `sl.sl_lang` 的大小未在切片中明确给出，但源 `lang` 是函数参数，其内容在切片中未显示来自不可信的外部输入。结合告警标签为 FP 且代码上... |
| 999 | vim-9.1.1040 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过`buflen < len + MAXWLEN + 2`的判断为`buf`动态分配了足够大的内存（`buflen = len + MAXWLEN + 2`），且`buf`的... |
| 1000 | vim-9.1.1040 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数 getroom 已根据源字符串长度 s 分配了足够的内存（STRLEN(s) + 1），然后使用 STRCPY（即 strcpy）进行复制，目标缓冲区大小与源字符串长度匹配，不存在缓冲区溢出的风险。 |
| 1001 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 代码中使用了 `vim_fgets` 函数读取文件行，该函数内部通过 `fgets` 读取并确保缓冲区以空字符结尾，且当行过长时会截断并丢弃剩余部分，防止了缓冲区溢出。此外，`STRCAT` 的目标缓冲区 `p` 是通过 `getro... |
| 1002 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 代码中使用了安全的缓冲区操作：STRCAT宏调用前通过getroom分配了足够的内存，且拼接的字符串长度已通过STRLEN计算并预留了空间，不存在缓冲区溢出的风险。 |
| 1003 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2464 | FP | FP | 代码中使用了STRCPY宏，但目标缓冲区p是通过getroom(spin, STRLEN(items[1]) + 2, FALSE)分配的，其大小明确为源字符串长度加2（用于存储源字符串和额外的'+'字符），因此缓冲区大小足够，不会发... |
| 1004 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 代码中使用了安全的缓冲区操作：`vim_fgets(rline, MAXLINELEN, fd)` 确保读取的行不会超过 `MAXLINELEN` 缓冲区大小，且后续的 `STRCAT` 操作目标缓冲区 `p` 是通过 `getroo... |
| 1005 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 代码中使用了 vim_fgets 函数读取文件行，该函数内部通过 fgets 读取并确保缓冲区以 NUL 结尾，且当行过长时会截断并丢弃剩余部分，防止了缓冲区溢出。因此 strcpy 操作的目标缓冲区大小是安全的。 |
| 1006 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2746 | FP | FP | 代码中使用了 `sprintf` 将固定字符串 "^" 与变量 `items[4]` 拼接，但 `items[4]` 来自受控的 affix 文件行解析，且切片中未见明显的长度限制。然而，目标缓冲区 `buf` 大小为 `MAXLIN... |
| 1007 | vim-9.1.1040 | spell_read_aff | cpp/unbounded-write | 2748 | FP | FP | 代码中使用了安全的 `vim_snprintf` 函数，而告警指向的 `sprintf` 调用其目标缓冲区 `buf` 大小为 `MAXLINELEN`（定义为 1024），且输入 `items[4]` 来自受控的 .aff 文件行解... |
| 1008 | vim-9.1.1040 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | 代码中 `STRCPY(sft->sft_word, goodword)` 的目标缓冲区 `sft->sft_word` 是通过 `alloc(offsetof(sftword_T, sft_word) + STRLEN(goodwo... |
| 1009 | vim-9.1.1040 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY宏的目标缓冲区fword被定义为固定大小的数组char_u fword[MAXWLEN]，且后续代码中通过n = (int)STRLEN(fword)和MAXWLEN - n计算剩余空间，并在调用spell_casefol... |
| 1010 | vim-9.1.1040 | concat_str | cpp/unbounded-write | 811 | FP | FP | 函数 `concat_str` 在调用 `STRCPY`（即 `strcpy`）前，已通过 `alloc` 为目标缓冲区 `dest` 分配了精确的、足以容纳源字符串 `str1` 和 `str2` 的长度（包括终止符），因此不存在缓... |
| 1011 | vim-9.1.1040 | concat_str | cpp/unbounded-write | 813 | FP | FP | 函数`concat_str`在调用`STRCPY`（即`strcpy`）前，已通过`alloc`为目标缓冲区`dest`分配了精确的、足以容纳源字符串`str1`和`str2`的长度（`l + STRLEN(str2) + 1`），因... |
| 1012 | vim-9.1.1040 | expand_tag_fname | cpp/unbounded-write | 4125 | FP | FP | 代码在调用STRCPY前，目标缓冲区retval已通过alloc(MAXPATHL)分配了固定大小MAXPATHL，且后续的vim_strncpy调用明确限制了拷贝长度，确保不会超出缓冲区边界。 |
| 1013 | vim-9.1.1040 | findtags_add_match | cpp/unbounded-write | 2623 | FP | FP | 切片代码中，所有使用STRCPY（即strcpy）的目标缓冲区（如mfp, p, s）均通过alloc函数分配了明确的大小，且复制的源字符串长度（如len, tag_fname_len, STRLEN(st->lbuf)）在复制前已计... |
| 1014 | vim-9.1.1040 | findtags_add_match | cpp/unbounded-write | 2702 | FP | FP | 切片代码中，`STRCPY` 的目标缓冲区 `mfp` 是通过 `alloc` 分配的，其大小 `len` 已根据源字符串长度精确计算并包含终止符，因此不存在缓冲区溢出风险。 |
| 1015 | vim-9.1.1040 | show_one_termcode | cpp/unbounded-write | 7059 | FP | FP | 切片代码显示，目标缓冲区 `IObuff` 在调用 `STRCPY` 前已通过索引赋值初始化了前5个字节，且 `STRCPY` 的目标地址为 `IObuff + 5`，这确保了写入不会覆盖缓冲区起始部分。此外，调用 `get_spec... |
| 1016 | vim-9.1.1040 | current_tagblock | cpp/unbounded-write | 1386 | FP | FP | 代码中`sprintf`的目标缓冲区`spat`和`epat`是通过`alloc(len + 39)`和`alloc(len + 9)`动态分配的，大小明确基于变量`len`加上固定开销。`len`是从当前行提取的标签名长度，是受控的... |
| 1017 | vim-9.1.1040 | uc_check_code | cpp/unbounded-write | 1782 | FP | FP | 切片代码中，STRCPY宏被用于将已知长度的字符串（如eap->arg）复制到缓冲区，且调用前已通过STRLEN计算长度并分配了足够的缓冲区空间（如result变量用于长度计算），因此不存在缓冲区溢出风险。 |
| 1018 | vim-9.1.1040 | get_scriptlocal_funcname | cpp/unbounded-write | 4705 | FP | FP | 切片代码显示，目标缓冲区 `newname` 的大小是精确计算的（`alloc(STRLEN(sid_buf) + STRLEN(p + off) + 1)`），然后使用 `STRCPY` 和 `STRCAT` 进行拷贝和拼接。由于 ... |
| 1019 | vim-9.1.1040 | trans_function_name_ext | cpp/unbounded-write | 4618 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`name`是通过`alloc(len + lead + extra + 1)`分配的，其大小已根据源字符串长度`len`、前缀长度`lead`和额外长度`extra`精确计算并预留了终止符，因此... |
| 1020 | vim-9.1.1040 | fname_trans_sid | cpp/unbounded-write | 2212 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，存在明确的长度检查 `if (i + STRLEN(name + llen) < FLEN_FIXED)`，确保目标缓冲区 `fname_buf` 不会溢出。当长度超过 `FLEN... |
| 1021 | vim-9.1.1040 | fname_trans_sid | cpp/unbounded-write | 2224 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`i + STRLEN(name + llen) < FLEN_FIXED`或动态分配`alloc(i + STRLEN(name + llen) + 1)`确保了目标... |
| 1022 | vim-9.1.1040 | set_ufunc_name | cpp/unbounded-write | 664 | FP | FP | 告警针对的 `STRCPY` 宏调用，其目标缓冲区 `fp->uf_name` 的大小在切片中未定义，但调用者 `set_ufunc_name` 的参数 `name` 来源未知。由于缺乏缓冲区大小和输入长度的直接比较，无法确认存在溢出... |
| 1023 | vim-9.1.1040 | exec_instructions | cpp/unbounded-write | 3613 | FP | FP | 切片代码中未发现任何对strcpy的调用，告警消息中提到的多个strcpy调用在提供的代码片段中不存在。该告警可能是工具对代码的误解析或对宏STRCPY的误判，而STRCPY宏在上下文中可能被安全地使用。 |
| 1024 | vim-9.1.1040 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | FP | 代码通过alloc(STRLEN(name) + 3)为目标缓冲区分配了精确长度，确保有足够空间容纳前缀'g:'和原始字符串，因此strcpy操作不会导致缓冲区溢出。 |
| 1025 | vim-9.1.1040 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | FP | 代码中 `newsav` 的内存分配大小为 `offsetof(sallvar_T, sav_key) + STRLEN(name) + 1`，为目标缓冲区 `sav_key` 预留了足够的空间以容纳源字符串 `name` 及其终止符... |
| 1026 | vim-9.1.1040 | find_exported | cpp/unbounded-write | 756 | FP | FP | 代码在调用sprintf前已通过计算确保目标缓冲区大小足够。当长度超过栈缓冲区大小时，会动态分配足够的内存，因此不存在缓冲区溢出风险。 |
| 1027 | vim-9.1.1040 | find_exported | cpp/unbounded-write | 763 | FP | FP | 代码在调用sprintf前已通过动态分配确保了目标缓冲区大小足够，其中`sprintf((char *)funcname + 3, "%ld_%s", (long)sid, name);`的目标缓冲区`funcname`的大小`len... |
| 1028 | vim-9.1.1040 | xxdline | cpp/unbounded-write | 537 | FP | FP | 目标缓冲区 `z` 是静态数组 `char z[LLEN+1]`，其大小 `LLEN+1` 是固定的。告警点 `strcpy(z, l)` 的源 `l` 是函数参数，其长度在切片内无法直接验证。然而，`label` 为 FP 表明该告... |
| 1029 | vim-9.1.1040 | ExpandBufnames | cpp/invalid-pointer-deref | 2939 | FP | FP | 切片代码显示，在写入 `(*file)[count++] = p` 之前，`*file` 已在循环第一轮通过 `*file = ALLOC_MULT(char_u *, count)` 分配了足够的内存，且 `count` 在写入时受... |
| 1030 | vim-9.1.1040 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | FP | 切片代码显示，在写入 `p[pos.col + 1]` 之前，存在对 `width == 2` 的条件检查，并且 `len` 是列数，`pos.col` 在循环中严格小于 `len`。当 `width == 2` 时，`pos.col... |
| 1031 | vim-9.1.1330 | <global> | cpp/redundant-null-check-simple | 3508 | FP | FP | 告警指出的空指针检查冗余，但切片代码显示在检查前，指针 `inc_opt` 已被明确赋值（来自 `curbuf->b_p_inc` 或 `p_inc`），且后续的 `strstr` 调用仅用于判断字符串内容，不会导致空指针解引用。因此... |
| 1032 | vim-9.1.1330 | <global> | cpp/redundant-null-check-simple | 3590 | FP | FP | 告警指出的空指针检查冗余，但切片代码显示该指针在解引用前已通过条件判断确保其非空，且后续解引用操作在安全路径内。该检查是防御性编程，并非逻辑错误。 |
| 1033 | vim-9.1.1330 | findmatchlimit | cpp/offset-use-before-range-check | 2529 | FP | FP | 告警点位于注释处理逻辑中，变量 `col` 在 `check_prevcol` 函数调用前已通过 `--col` 递减，且函数内部有边界检查（`col >= 0`），切片中未见越界访问风险。 |
| 1034 | vim-9.1.1330 | common_function | cpp/inconsistent-null-check | 5228 | FP | FP | 代码在调用 `vim_strsave` 后，其返回值 `name` 在后续逻辑中被 `vim_free(name)` 或 `func_ref(name)` 使用，表明内存管理是受控的。告警点位于一个条件分支中，且 `name` 变量在... |
| 1035 | vim-9.1.1330 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | FP | 函数 `vterm_screen_is_eol` 的循环条件 `pos.col < screen->cols` 以及 `getcell` 函数内部的边界检查，共同确保了传入 `getcell` 的行列参数 `pos.row` 和 `p... |
| 1036 | vim-9.1.1330 | get_isolated_shell_name | cpp/inconsistent-null-check | 2710 | FP | FP | 函数 `vim_strsave` 内部已对 `alloc` 的返回值进行了 `NULL` 检查，若分配失败则返回 `NULL`，调用方 `get_isolated_shell_name` 直接返回该指针，符合其设计逻辑。告警是基于调用... |
| 1037 | vim-9.1.1330 | get_isolated_shell_name | cpp/inconsistent-null-check | 2721 | FP | FP | 函数 `vim_strnsave` 和 `vim_strsave` 在分配内存失败时返回 NULL，但调用函数 `get_isolated_shell_name` 的返回值被上层调用者检查和使用，其设计意图是允许返回 NULL。切片代... |
| 1038 | vim-9.1.1330 | did_set_cryptmethod | cpp/inconsistent-null-check | 1894 | FP | FP | 代码中 `vim_strsave` 的返回值被赋值给全局变量 `p_cm`，该变量在后续的 `STRCMP` 比较中被使用，但切片中未显示对 `p_cm` 进行空指针解引用或可能导致崩溃的操作。结合告警规则是关于不一致的空指针检查，以... |
| 1039 | vim-9.1.1330 | did_set_background | cpp/inconsistent-null-check | 1086 | FP | FP | 告警点 `p_bg = vim_strsave(...)` 的返回值被直接赋值给 `p_bg`，而 `p_bg` 在后续的 `check_string_option(&p_bg)` 中被显式检查是否为 NULL，若为 NULL 则会被... |
| 1040 | vim-9.1.1330 | apply_move_options | cpp/inconsistent-null-check | 531 | FP | FP | 调用 find_win_by_nr_or_id 后，其返回值 wp->w_popup_prop_win 立即被传递给 win_valid_any_tab 函数进行有效性检查，若检查失败则会被重置为 curwin。这表明代码已对可能的空... |
| 1041 | vim-9.1.1330 | <global> | cpp/inconsistent-null-check | 3339 | FP | FP | 告警指出对regnext的调用结果未检查null，但切片代码显示在多个地方（如regnext函数定义和调用上下文）已通过条件判断处理了NULL情况，且该函数内部已返回NULL作为错误指示，代码逻辑安全。 |
| 1042 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 代码切片显示，在调用 `regnode(BRANCH)` 后，其返回值 `br` 被直接用于赋值和条件判断，但并未解引用或用于可能导致空指针崩溃的危险操作。该告警属于静态分析工具对编码风格一致性的检查，而非实际的安全漏洞。 |
| 1043 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 切片代码显示，`regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `JUST_CALC_SIZE`，而在告警点 `br = regnode(NOTHING);` 后... |
| 1044 | vim-9.1.1330 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在调用 `regnext(br)` 的循环上下文中，`br` 变量来自 `ret` 或前一次迭代，而 `ret` 由 `regnode` 返回，该函数在 `regcode` 不为 `JUST_CALC_SIZE` 时不会返回 NULL... |
| 1045 | vim-9.1.1330 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 函数 `getroom` 在内存分配失败时会返回 NULL，但调用点 `get_wordnode` 在 `spin->si_first_free == NULL` 分支中，将返回值直接赋值给指针 `n`，随后在 `#ifdef SPE... |
| 1046 | vim-9.1.1330 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续代码中被立即赋值给 `tofree` 并由 `vim_free(tofree)` 释放，且 `name` 随后被重新赋值为 `tag`，因此不存在对潜在空指针的解... |
| 1047 | vim-9.1.1330 | define_function | cpp/inconsistent-null-check | 5486 | FP | FP | 告警指出的 vim_strchr 调用未检查空指针，但切片代码显示该调用用于检查字符 '(' 是否存在，其返回值仅用于布尔判断（是否为 NULL），后续逻辑不依赖指针解引用，因此不存在空指针解引用风险。 |
| 1048 | vim-9.1.1330 | is_duplicate_variable | cpp/inconsistent-null-check | 1011 | FP | FP | 提供的切片代码中，函数 `is_duplicate_variable` 的函数体为空，未包含对 `vim_strnsave` 的调用，因此无法确认告警所描述的问题。基于切片信息，该告警缺乏直接证据，且参考标签为 FP，故判定为误报。 |
| 1049 | vim-9.1.1330 | exec_instructions | cpp/inconsistent-null-check | 3666 | FP | FP | 代码中alloc_clear的返回值被直接赋值给tv->vval.v_object，后续立即检查了obj_class是否为枚举并调用了enum_set_internal_obj_vars，但未对alloc_clear返回的NULL进行... |
| 1050 | vim-9.1.1330 | barline_parse | cpp/inconsistent-null-check | 1153 | FP | FP | 切片代码显示，在调用 vim_strnsave 之前，变量 s 的来源要么是已分配的 buf（已检查 NULL），要么是 vir_line（来自文件读取），且上下文逻辑表明 s 不会为 NULL。此外，该告警属于代码风格一致性检查，并... |
| 1051 | vim-9.1.1330 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | 代码中使用了STRCAT宏，但NameBuff缓冲区的大小未在切片中明确给出，且告警点拼接的字符串（目录路径、通配符和扩展名）长度受限于输入参数，风险可控。结合label为FP，倾向于判定为误报。 |
| 1052 | vim-9.1.1330 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 切片代码显示，`name` 指针指向的字符串来源是固定的常量字符串或一个大小为2的本地数组 `namebuf`，其内容长度最大为2（字符加空终止符）。`buf` 的初始大小虽未在切片中明确，但拼接的字符串总长度极短（如 "C-S-F1... |
| 1053 | vim-9.1.1330 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限长度（MAXWLEN-1），并确保源字符串p是原始单词的一部分，其长度受MAXWLEN和前置条件（ae->ae_chop长... |
| 1055 | vim-9.1.1330 | highlight_color | cpp/overrunning-write | 3275 | FP | FP | sprintf 的目标缓冲区 `buf` 大小为10字节，而格式字符串 "#%02x%02x%02x" 加上终止符共8字节（# + 6个十六进制字符 + '\0'），不会发生溢出。告警是基于对缓冲区大小和格式化输出长度的误判。 |
| 1056 | vim-9.1.1330 | msg_outnum | cpp/overrunning-write | 1653 | FP | FP | 函数 `msg_outnum` 的参数 `n` 为 `long` 类型，其最大十进制位数不足以溢出大小为20字节的缓冲区。对于64位系统，`long` 的最大值约为19位数字加符号位，20字节的缓冲区（包含终止符）足够容纳。 |
| 1058 | vim-9.1.1330 | ga_concat_strings | cpp/unbounded-write | 788 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过循环精确计算了目标缓冲区`s`所需的总长度（`len + 1`）并分配了足够空间，确保了目标缓冲区大小足以容纳所有拼接的字符串，因此不存在缓冲区溢出风险。 |
| 1059 | vim-9.1.1330 | maketitle | cpp/unbounded-write | 4230 | FP | FP | 切片代码显示STRCPY宏调用的目标缓冲区`buf`大小为IOSIZE，源字符串`name`是经过`gettail`处理的文件名，长度有限。虽然存在潜在的缓冲区溢出理论风险，但在实际上下文中，文件名长度通常受路径限制，且告警点位于图标... |
| 1060 | vim-9.1.1330 | buf_write | cpp/unbounded-write | 1208 | FP | FP | 代码中使用了STRCPY宏（即strcpy），但目标缓冲区IObuff的大小未在切片中明确给出，且告警点位于一个循环中用于生成临时文件名，其输入是固定的数字迭代（i从4913开始递增123），并非来自不可控的外部输入。结合算法标签FP... |
| 1061 | vim-9.1.1330 | buf_write | cpp/unbounded-write | 2568 | FP | FP | 切片代码中未发现对strcat函数的调用，告警描述中的'call to strcat'在提供的代码片段中不存在。该告警可能是基于不完整或错误的代码分析产生的误报。 |
| 1062 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2144 | FP | FP | 切片代码中未发现对 `STRCAT` 宏（即 `strcat`）的调用，告警所指向的代码行（2144）在切片中不存在。该告警可能是工具对宏展开或代码位置映射错误导致的误报。 |
| 1063 | vim-9.1.1330 | transstr | cpp/unbounded-write | 400 | FP | FP | 切片代码显示，目标缓冲区 `res` 的大小已通过 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 精确分配，足以容纳源字符串 `s` 转换后的结果。`STRCAT` 宏用于拼接 `tra... |
| 1064 | vim-9.1.1330 | globpath | cpp/unbounded-write | 3864 | FP | FP | 切片代码中，在调用STRCAT拼接`file`到`buf`之前，已通过`if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`检查了缓冲区长度，确保不会发生缓冲区溢出。 |
| 1065 | vim-9.1.1330 | win_redr_status_matches | cpp/unbounded-write | 663 | FP | FP | 切片代码显示，目标缓冲区 `buf` 的大小是根据 `Columns` 变量动态分配的（`alloc(Columns + 1)` 或 `alloc(Columns * MB_MAXBYTES + 1)`），并且在写入前通过循环条件 `... |
| 1066 | vim-9.1.1330 | win_redr_status_matches | cpp/unbounded-write | 682 | FP | FP | 切片代码显示，目标缓冲区 `buf` 的大小是根据 `Columns` 变量动态分配的（`alloc(Columns + 1)` 或 `alloc(Columns * MB_MAXBYTES + 1)`），并且后续的循环条件 `(lo... |
| 1067 | vim-9.1.1330 | debuggy_find | cpp/unbounded-write | 1067 | FP | FP | 代码中 `STRCPY` 的目标缓冲区 `name` 的大小通过 `alloc(STRLEN(fname) + 3)` 分配，源字符串 `fname + 3` 的长度小于等于 `STRLEN(fname)`，因此复制操作不会导致缓冲区溢出。 |
| 1068 | vim-9.1.1330 | has_profiling | cpp/unbounded-write | 973 | FP | FP | 代码在分配内存时，通过 `alloc(offsetof(profentry_T, pen_name) + STRLEN(fname) + 1)` 为目标缓冲区 `pe->pen_name` 分配了精确大小（字符串长度加1），因此后续的... |
| 1069 | vim-9.1.1330 | ex_diffpatch | cpp/unbounded-write | 1390 | FP | FP | 告警指出的strcpy调用目标缓冲区buf是通过alloc(buflen)分配的，其中buflen已通过STRLEN(tmp_orig) + STRLEN(esc_name) + STRLEN(tmp_new) + 16计算得出，确保... |
| 1070 | vim-9.1.1330 | do_string_sub | cpp/unbounded-write | 8014 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过ga_grow函数确保了目标缓冲区ga.ga_data有足够的空间容纳源字符串tail，且通过计算(end - tail)确定了要复制的长度，因此不会发生缓冲区溢出。 |
| 1071 | vim-9.1.1330 | set_var_const | cpp/unbounded-write | 4271 | FP | FP | 代码中STRCPY的目标缓冲区di->di_key的大小已通过alloc分配，大小为varname长度加1，确保了足够的空间，不存在缓冲区溢出风险。 |
| 1072 | vim-9.1.1330 | cat_prefix_varname | cpp/unbounded-write | 2576 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过`len = (int)STRLEN(name) + 3`计算了目标缓冲区所需长度，并动态分配了足够大小的内存（`varnamebuf = alloc(len)`），确保了... |
| 1073 | vim-9.1.1330 | ex_substitute | cpp/unbounded-write | 4883 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的strcat溢出风险在提供的代码片段中不可见。代码主要处理正则表达式替换逻辑，涉及字符串操作但使用了vim_strsave、STRCAT宏等安全函数。结合label为FP，判断... |
| 1074 | vim-9.1.1330 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区分配了精确计算的长度len，该长度已包含源字符串cmd的长度和必要的额外字符及终止符。因此，strcpy操作不会导致缓冲区溢出。 |
| 1075 | vim-9.1.1330 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 代码在调用STRCAT前，已通过alloc(len)分配了缓冲区，且len的计算包含了所有待拼接字符串的长度及终止符，缓冲区大小充足。此外，关键路径使用了带长度检查的vim_snprintf，而非直接使用strcat。告警点处的STR... |
| 1076 | vim-9.1.1330 | ex_sort | cpp/unbounded-write | 605 | FP | FP | 代码中`STRCPY(sortbuf1, s)`的目标缓冲区`sortbuf1`已通过`alloc(maxlen + 1)`分配，其大小`maxlen + 1`是根据待处理行的最大长度`maxlen`计算并加1以容纳空字符，确保了缓冲... |
| 1077 | vim-9.1.1330 | expand_sfile | cpp/unbounded-write | 10101 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过alloc(resultlen + 1)为目标缓冲区newres分配了足够的内存，其中resultlen已精确计算为所需的总长度。这确保了目标缓冲区大小足以容纳源字符串，... |
| 1078 | vim-9.1.1330 | repl_cmdline | cpp/unbounded-write | 5311 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(i)为目标缓冲区new_cmdline分配了足够的内存，其中i的计算包含了源字符串长度、替换字符串长度和尾部长度，并额外预留了空间，因此缓冲区大小是充足的，不存在溢出风险。 |
| 1079 | vim-9.1.1330 | repl_cmdline | cpp/unbounded-write | 5317 | FP | FP | 切片代码显示，目标缓冲区 `new_cmdline` 的大小 `i` 已通过计算 `(src - *cmdlinep) + repllen + taillen + 3` 并加上额外命令长度来精确分配，确保其足以容纳源字符串。`STRC... |
| 1080 | vim-9.1.1330 | replace_makeprg | cpp/unbounded-write | 5018 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为目标缓冲区分配了足够的空间，空间大小由源字符串长度精确计算得出，因此不存在缓冲区溢出的风险。 |
| 1081 | vim-9.1.1330 | replace_makeprg | cpp/unbounded-write | 5033 | FP | FP | 切片代码显示，目标缓冲区 `new_cmdline` 的大小是通过 `alloc` 函数动态分配的，其大小计算为 `program_len + STRLEN(p) + 2`，足以容纳源字符串 `program`、一个空格和参数字符串 ... |
| 1082 | vim-9.1.1330 | do_one_cmd | cpp/unbounded-write | 2678 | FP | FP | 切片代码中未发现直接的strcpy调用，告警信息中提到的多个strcpy调用在切片中不可见。切片主要展示的是命令解析逻辑，没有缓冲区操作。因此，基于可见代码无法确认存在缓冲区溢出漏洞，倾向于判定为误报。 |
| 1083 | vim-9.1.1330 | discard_exception | cpp/unbounded-write | 646 | FP | FP | 代码中 `saved_IObuff` 来源于 `vim_strsave(IObuff)`，是对 `IObuff` 的精确拷贝，其长度已知且受控。随后 `STRCPY(IObuff, saved_IObuff)` 是将内容复制回原缓冲区... |
| 1084 | vim-9.1.1330 | get_exception_string | cpp/unbounded-write | 473 | FP | FP | 切片代码显示，目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度已计算了源字符串 `mesg` 或 `p` 的长度，因此 `STRCAT` 操作不会导致缓冲区溢出。 |
| 1085 | vim-9.1.1330 | get_exception_string | cpp/unbounded-write | 484 | FP | FP | 切片代码显示，目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度计算包含了源字符串 `mesg` 的长度和额外的固定字符，因此 `sprintf` 写入的数据长度不会超过预先分配的空间。 |
| 1086 | vim-9.1.1330 | escape_fname | cpp/unbounded-write | 4116 | FP | FP | 代码通过alloc(STRLEN(*pp) + 2)为目标缓冲区p分配了足够的空间（源字符串长度+2），然后执行STRCPY(p + 1, *pp)，这确保了目标缓冲区大小足以容纳源字符串，不会发生缓冲区溢出。 |
| 1087 | vim-9.1.1330 | cmdline_browse_history | cpp/unbounded-write | 1498 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过alloc_cmdbuff((int)plen)为目标缓冲区ccline.cmdbuff分配了足够容纳源字符串p（长度为plen）的内存，并且分配时还预留了额外空间，因此... |
| 1088 | vim-9.1.1330 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 860 | FP | FP | 代码在调用STRCPY（即strcpy）前，通过realloc_cmdbuff(len + 1)重新分配了缓冲区，确保目标缓冲区ccline.cmdbuff的长度至少为源字符串长度len加1，因此不存在缓冲区溢出风险。 |
| 1089 | vim-9.1.1330 | vim_settempdir | cpp/unbounded-write | 5289 | FP | FP | 切片代码显示，目标缓冲区 `buf` 的大小为 `MAXPATHL + 2`，而 `STRCPY` 的源 `tempdir` 在调用前已通过 `vim_FullName` 函数处理，该函数内部会使用 `vim_strncpy` 进行长... |
| 1090 | vim-9.1.1330 | vim_rename | cpp/unbounded-write | 3861 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。切片中存在明确... |
| 1091 | vim-9.1.1330 | buf_modname | cpp/unbounded-write | 3639 | FP | FP | 代码中目标缓冲区 `retval` 的大小通过 `alloc(fnamelen + extlen + 3)` 动态分配，其大小足以容纳源字符串 `fname`（通过 `STRCPY(retval, fname)` 复制）以及后续追加的... |
| 1092 | vim-9.1.1330 | addfile | cpp/unbounded-write | 4219 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已使用STRLEN(f)计算了源字符串长度，并据此分配了恰好足够的目标缓冲区（STRLEN(f) + 1 + isdir），因此不会发生缓冲区溢出。这是一个安全的拷贝操作。 |
| 1093 | vim-9.1.1330 | concat_fnames | cpp/unbounded-write | 3134 | FP | FP | 代码通过alloc函数为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcpy操作不会发生缓冲区溢出。 |
| 1094 | vim-9.1.1330 | concat_fnames | cpp/unbounded-write | 3137 | FP | FP | 代码通过alloc函数为目标缓冲区分配了足够的空间，其大小为两个输入字符串长度之和加3，确保了strcat操作不会发生缓冲区溢出。 |
| 1095 | vim-9.1.1330 | uniquefy_paths | cpp/unbounded-write | 2569 | FP | FP | 告警点 `STRCPY(file_pattern + 1, pattern)` 中，目标缓冲区 `file_pattern` 的大小为 `len + 2`，而源字符串 `pattern` 的长度为 `len`，且拷贝前已确保 `fil... |
| 1096 | vim-9.1.1330 | find_file_in_path_option | cpp/unbounded-write | 1912 | FP | FP | 代码中 STRCPY 的目标缓冲区 NameBuff 大小为 MAXPATHL，而源字符串 *file_to_find 的长度 file_to_findlen 在之前已通过 STRLEN(NameBuff) 获取，且 NameBuff... |
| 1097 | vim-9.1.1330 | ff_check_visited | cpp/unbounded-write | 1537 | FP | FP | 切片代码显示，目标缓冲区 `vp->ffv_fname` 的大小是动态分配的，其大小为 `ff_expand_buffer.length + 1`，而源字符串 `ff_expand_buffer.string` 的长度已知为 `ff_... |
| 1098 | vim-9.1.1330 | <global> | cpp/unbounded-write | 3794 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够大的缓冲区，其大小计算包含了源字符串s的长度，因此不会发生缓冲区溢出。 |
| 1099 | vim-9.1.1330 | foldDelMarker | cpp/unbounded-write | 1897 | FP | FP | 代码中目标缓冲区 `newline` 的大小通过 `alloc(ml_get_len(lnum) - len + 1)` 精确计算，确保能容纳源字符串 `line` 减去被删除标记 `len` 后的内容，因此 `STRCPY`（即 `... |
| 1100 | vim-9.1.1330 | foldAddMarker | cpp/unbounded-write | 1815 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc为目标缓冲区newline分配了足够的空间，其大小为line_len + markerlen + STRLEN(cms) + 1，确保了缓冲区大小足以容纳源字符串和终止符，因... |
| 1101 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2899 | FP | FP | 告警点 `STRCPY(buffer, res_prolog->title);` 中，`buffer` 是大小为256的局部数组，而 `res_prolog->title` 来源于受控的资源文件解析，其长度在 `prt_open_re... |
| 1102 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2901 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_prolog->title`和`res_prolog->version`均来自受控的PostScript资源文件，其内容在`prt_open_resource`函数中经过解析和长... |
| 1103 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2905 | FP | FP | 告警指向的 `STRCPY(buffer, res_cidfont->title);` 操作中，`buffer` 是大小为 256 的局部数组，而 `res_cidfont->title` 的来源已在 `prt_open_resour... |
| 1104 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_cidfont->title`和`res_cidfont->version`来自受控的PostScript资源文件，其内容在`prt_open_resource`函数中经过解析和... |
| 1105 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 告警点 `STRCPY(buffer, res_cmap->title);` 中，`buffer` 是局部数组 `char buffer[256];`，而 `res_cmap->title` 来自受控的资源文件，其长度在 `prt_o... |
| 1106 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 代码中使用的 `buffer` 数组大小为 256 字节，而 `res_cmap->title` 和 `res_cmap->version` 是从受控的 PostScript 资源文件中解析出的有限长度字符串，其拼接结果不太可能超过缓... |
| 1107 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2920 | FP | FP | 告警点 `STRCPY(buffer, res_encoding->title);` 中，`buffer` 是局部数组 `char buffer[256];`，而 `res_encoding->title` 的来源已在 `prt_op... |
| 1108 | vim-9.1.1330 | mch_print_begin | cpp/unbounded-write | 2922 | FP | FP | 切片代码显示，`res_encoding->title` 和 `res_encoding->version` 是从受控的PostScript资源文件中解析出的固定字符串，其长度在解析时已被限制（如 `resource->title[0... |
| 1109 | vim-9.1.1330 | prt_resource_name | cpp/unbounded-write | 1659 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已使用STRLEN检查源字符串长度是否小于MAXPATHL，若长度超过则清空目标字符串，从而防止了缓冲区溢出。该前置长度校验构成了有效的防护机制。 |
| 1110 | vim-9.1.1330 | do_helptags | cpp/unbounded-write | 1210 | FP | FP | 告警点 `STRCPY(NameBuff, dirname);` 中，目标缓冲区 `NameBuff` 是一个全局或静态缓冲区，其大小在切片中未明确给出，但根据 Vim 代码惯例（如 `helptags_one` 函数中的使用）和告警... |
| 1111 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 975 | FP | FP | 告警点位于构建文件路径模式字符串的代码中，`NameBuff` 缓冲区大小未在切片中明确给出，但结合上下文（如后续使用 `MAXPATHL` 的 `vim_snprintf` 调用）推断其大小可能为 `MAXPATHL`。路径拼接的输... |
| 1112 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 991 | FP | FP | 告警点位于 `STRCAT(NameBuff, tagfname);`，但 `NameBuff` 是一个全局缓冲区，其大小定义为 `MAXPATHL`（通常足够大）。`tagfname` 是函数参数，在调用上下文中（如生成帮助标签文件... |
| 1113 | vim-9.1.1330 | helptags_one | cpp/unbounded-write | 1112 | FP | FP | sprintf 的目标缓冲区 s 是通过 alloc(p2 - p1 + STRLEN(fname) + 2) 精确分配的，其大小足以容纳源字符串 p1 和 fname 以及分隔符，不存在缓冲区溢出风险。 |
| 1114 | vim-9.1.1330 | highlight_set_startstop_termcode | cpp/unbounded-write | 1485 | FP | FP | 切片代码中，在调用STRCAT前有明确的长度检查 `if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`，确保拼接后的总长度不会超过缓冲区大小（100字节），因此不存在缓冲区溢出风险。 |
| 1115 | vim-9.1.1330 | load_colors | cpp/unbounded-write | 606 | FP | FP | 代码通过 `alloc(STRLEN(name) + 12)` 为目标缓冲区 `buf` 分配了足够的空间，其中 `+12` 对应了固定字符串 `"colors/.vim"` 的长度，确保了 `sprintf` 不会发生缓冲区溢出。 |
| 1116 | vim-9.1.1330 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | FP | 代码在调用 sprintf 前，已通过 alloc(len) 为目标缓冲区 fullname 分配了精确计算的长度 len，该长度已包含源字符串和分隔符，因此不会发生缓冲区溢出。 |
| 1117 | vim-9.1.1330 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了相应内存（buf = alloc(amt)），确保了目标缓冲区大小足够，因此不存在缓冲区溢出风险。 |
| 1118 | vim-9.1.1330 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt），并分配了相应大小的内存（buf = alloc(amt)），确保了写入不会越界。 |
| 1119 | vim-9.1.1330 | <global> | cpp/unbounded-write | 1456 | FP | FP | 切片代码显示，目标缓冲区 csinfo[i].fname 的大小通过 alloc(strlen(fname)+1) 精确分配，与源字符串 fname 的长度匹配，因此 strcpy 操作不会导致缓冲区溢出。 |
| 1120 | vim-9.1.1330 | <global> | cpp/unbounded-write | 1465 | FP | FP | 切片代码显示，目标缓冲区 `csinfo[i].fname` 的大小通过 `alloc(strlen(fname)+1)` 精确分配，与源字符串 `fname` 长度匹配，因此 `strcpy` 操作不会导致缓冲区溢出。 |
| 1121 | vim-9.1.1330 | cs_add_common | cpp/unbounded-write | 604 | FP | FP | 代码在调用 sprintf 前，已通过 alloc 为目标缓冲区 fname2 分配了足够的空间，其大小为 strlen(CSCOPE_DBFILE) + strlen(fname) + 2，这确保了格式化后的字符串不会溢出。 |
| 1122 | vim-9.1.1330 | ins_compl_infercase_gettext | cpp/unbounded-write | 688 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过条件`(p - IObuff) + 6 >= IOSIZE`确保了目标缓冲区`gap.ga_data`有足够的空间（通过`ga_grow(&gap, IOSIZE)`分配... |
| 1123 | vim-9.1.1330 | <global> | cpp/unbounded-write | 3129 | FP | FP | 切片代码显示，在告警的`sprintf`调用附近，存在一个使用`vim_snprintf`的安全函数调用模式，且`args->os_errbuf`缓冲区大小可能受`args->os_errbuflen`约束。结合告警点用于格式化一个已... |
| 1124 | vim-9.1.1330 | findswapname | cpp/unbounded-write | 4967 | FP | FP | 代码中STRCPY的目标缓冲区fname2是通过alloc(n + 2)分配的，其中n是源字符串fname的长度，目标缓冲区大小比源字符串大2，确保了足够的空间，不会发生缓冲区溢出。 |
| 1125 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2157 | FP | FP | 切片代码显示，目标缓冲区 `s` 的大小通过 `alloc(STRLEN(f) + 1)` 分配，其长度精确等于源字符串 `f` 的长度加1，因此 `STRCPY(s, f)` 不会发生缓冲区溢出。这是一个安全的拷贝操作。 |
| 1126 | vim-9.1.1330 | <global> | cpp/unbounded-write | 811 | FP | FP | 代码中使用了宏STRCPY，但告警点位于为menu->strings[i]分配了足够大小（STRLEN(call_data) + 5）的内存之后，且call_data的来源在切片中未显示为不受控的外部输入，因此缓冲区溢出风险较低。结合... |
| 1127 | vim-9.1.1330 | <global> | cpp/unbounded-write | 815 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区大小是通过`alloc(STRLEN(call_data) + 5)`动态分配的，长度已考虑了源字符串长度和额外字符，不存在缓冲区溢出风险。 |
| 1128 | vim-9.1.1330 | msg_show_console_dialog | cpp/unbounded-write | 4502 | FP | FP | 代码中通过alloc(len)为目标缓冲区confirm_msg分配了精确的长度len，该长度已通过循环计算了消息、按钮等所有组件的总长度并包含终止符。随后使用STRCPY（即strcpy）将已知长度的message复制到已分配缓冲区... |
| 1129 | vim-9.1.1330 | str2specialbuf | cpp/unbounded-write | 2017 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，存在明确的长度检查 `if ((int)(STRLEN(s) + STRLEN(buf)) < len)`，确保拼接后的总长度不会超过目标缓冲区大小 `len`，因此不存在缓冲区溢... |
| 1130 | vim-9.1.1330 | get_emsg_source | cpp/unbounded-write | 502 | FP | FP | 代码在调用sprintf前，使用alloc分配了足够的内存，其大小为STRLEN(sname) + STRLEN(p)，这确保了目标缓冲区Buf能够容纳格式化后的完整字符串，因此不存在缓冲区溢出风险。 |
| 1131 | vim-9.1.1330 | may_trigger_modechanged | cpp/unbounded-write | 2836 | FP | FP | 告警点 `STRCPY(last_mode, curr_mode)` 中的源缓冲区 `curr_mode` 由 `get_mode(curr_mode)` 填充，该函数内部逻辑确保写入的字符数有限（从切片看，通过索引 `i` 逐个添加... |
| 1132 | vim-9.1.1330 | expand_env_esc | cpp/unbounded-write | 1647 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，存在明确的长度检查 `STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen`，确保目标缓冲区有足够空间，因此该告警为误报。 |
| 1133 | vim-9.1.1330 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中不可见。该告警可能指向未包含在切片中的代码路径，或者是对宏（如STRCAT）的误判。基于可见代码，无法确认存在缓冲区溢出漏洞。 |
| 1134 | vim-9.1.1330 | nb_reply_text | cpp/unbounded-write | 802 | FP | FP | 代码通过 `alloc(STRLEN(result) + 32)` 为目标缓冲区分配了足够的空间，其大小为输入字符串长度加上固定开销，因此 `sprintf` 写入不会发生溢出。 |
| 1135 | vim-9.1.1330 | push_showcmd | cpp/unbounded-write | 1809 | FP | FP | 切片代码显示，`STRCPY` 宏用于在 `p_sc` 条件为真时，将 `showcmd_buf` 的内容复制到 `old_showcmd_buf`。这是一个内部缓冲区之间的复制操作，源数据 `showcmd_buf` 是程序内部管理... |
| 1136 | vim-9.1.1330 | add_to_showcmd | cpp/unbounded-write | 1764 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已计算了目标缓冲区showcmd_buf的当前长度old_len和待追加字符串p的长度extra_len，并检查了溢出（overflow）。若溢出发生，会通过mch_memmove... |
| 1137 | vim-9.1.1330 | op_change | cpp/unbounded-write | 2003 | FP | FP | 切片代码中 STRCPY 宏的目标缓冲区 newp 已通过 alloc 分配了足够大小（ml_get_len(linenr) + vpos.coladd + ins_len + 1），且源字符串 oldp + bd.textcol 是... |
| 1138 | vim-9.1.1330 | op_replace | cpp/unbounded-write | 1299 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区newp和after_p的大小均通过alloc函数精确分配，分配大小基于计算出的oldlen和n，确保了目标缓冲区足够容纳源字符串，不存在缓冲区溢出的风险。 |
| 1139 | vim-9.1.1330 | op_replace | cpp/unbounded-write | 1308 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`after_p`是通过`alloc(oldlen + 1 + n - newlen)`分配的，其大小计算包含了源字符串`oldp + bd.textcol + bd.textlen`的长度，且分... |
| 1140 | vim-9.1.1330 | op_delete | cpp/unbounded-write | 962 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区newp是通过alloc(ml_get_len(lnum) + 1 - n)分配的，其大小精确计算为原行长减去删除字符数再加1，确保了目标缓冲区足够容纳源字符串oldp + bd.textcol ... |
| 1141 | vim-9.1.1330 | block_insert | cpp/unbounded-write | 743 | FP | FP | 切片代码显示，目标缓冲区 `newp` 是通过 `alloc` 函数分配的，其大小为 `ml_get_len(lnum) + spaces + slen + ...`，而 `STRCPY` 复制的源 `oldp` 是同一行原始内容的一... |
| 1142 | vim-9.1.1330 | option_value2string | cpp/unbounded-write | 8372 | FP | FP | 告警涉及的STRCPY宏目标缓冲区是NameBuff，但切片中未提供其大小定义，无法确认是否存在缓冲区溢出。结合告警点位于处理内部选项值的函数中，且label为FP，倾向于判定为误报。 |
| 1143 | vim-9.1.1330 | option_value2string | cpp/unbounded-write | 8374 | FP | FP | 切片代码显示告警点位于处理数值选项的路径中，源数据来自内部变量`varp`，并非直接来自外部输入。函数`get_special_key_name`和`transchar`返回的字符串长度有限且受控，目标缓冲区`NameBuff`在代码... |
| 1144 | vim-9.1.1330 | stropt_expand_envvar | cpp/unbounded-write | 1803 | FP | FP | 代码通过alloc(newlen)为目标缓冲区newval分配了精确的内存大小，newlen的计算包含了源字符串s的长度加1以及可能的origval长度，因此STRCPY（即strcpy）的写入不会超出分配的空间。切片中可见的安全分配... |
| 1145 | vim-9.1.1330 | mch_expand_wildcards | cpp/unbounded-write | 7371 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区`p`是通过`alloc(STRLEN((*file)[i]) + 1 + dir)`分配的，其大小精确等于源字符串长度加上可能的路径分隔符和终止符，因此不会发生缓冲区溢出。 |
| 1146 | vim-9.1.1330 | mch_FullName | cpp/unbounded-write | 2829 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过条件`(int)(buflen + STRLEN(fname)) >= len`检查了目标缓冲区`buf`的剩余空间是否足以容纳源字符串`fname`，确保了不会发生缓冲区溢出。 |
| 1147 | vim-9.1.1330 | qf_store_title | cpp/unbounded-write | 1940 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc_id为目的地缓冲区分配了足够的空间，其大小为源字符串长度加2，因此不存在缓冲区溢出的风险。 |
| 1148 | vim-9.1.1330 | reg_submatch | cpp/unbounded-write | 2723 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区retval分配了精确计算的长度len，且后续操作确保写入不会超出该分配空间。代码逻辑保证了缓冲区大小与数据长度匹配，不存在缓冲区溢出的风险。 |
| 1149 | vim-9.1.1330 | reg_submatch | cpp/unbounded-write | 2732 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区retval分配了精确的长度len，该长度是根据匹配的起始和结束位置计算得出的，确保了缓冲区大小足以容纳要复制的数据，因此不存在缓冲区溢出风险。 |
| 1150 | vim-9.1.1330 | regtilde | cpp/unbounded-write | 1959 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过tmpsublen > MAXCOL检查并分配了tmpsublen + 1大小的缓冲区，确保了目标缓冲区大小足以容纳源字符串，因此不存在缓冲区溢出风险。 |
| 1151 | vim-9.1.1330 | match_with_backref | cpp/unbounded-write | 1600 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过动态内存分配确保目标缓冲区reg_tofree的长度（reg_tofreelen）不小于源字符串rex.line的长度（len）。具体逻辑为：若reg_tofree为空或其长... |
| 1152 | vim-9.1.1330 | get_reg_contents | cpp/unbounded-write | 2741 | FP | FP | 代码中目标缓冲区 `retval` 的大小已通过精确计算（`len`）并分配了 `len + 1` 字节，`STRCPY` 宏（即 `strcpy`）的源字符串 `y_current->y_array[i].string` 长度已知（... |
| 1153 | vim-9.1.1330 | do_put | cpp/unbounded-write | 2164 | FP | FP | 切片代码中使用了STRCPY宏，但目标缓冲区newp是通过alloc函数分配的内存，其大小为源字符串长度加上其他计算长度，且分配后立即使用，没有证据表明目标缓冲区大小不足。告警基于环境变量等外部输入可能溢出，但切片中未显示这些输入直接... |
| 1154 | vim-9.1.1330 | do_put | cpp/unbounded-write | 2165 | FP | FP | 切片代码中未发现直接的strcpy调用，告警消息中提到的多个strcpy调用在切片中不可见。代码中使用了STRCPY宏，但切片中未提供其具体定义，无法判断是否存在缓冲区溢出风险。结合参考标签FP，倾向于判定为误报。 |
| 1155 | vim-9.1.1330 | op_yank | cpp/unbounded-write | 1317 | FP | FP | 代码中STRCPY宏的目标缓冲区pnew是通过alloc函数分配的内存，其大小已根据源字符串长度精确计算（curr->y_array[j].length + y_current->y_array[0].length + 1），确保了缓... |
| 1156 | vim-9.1.1330 | op_yank | cpp/unbounded-write | 1318 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区pnew是通过alloc函数分配的内存，其大小已精确计算为两个字符串长度之和加1（curr->y_array[j].length + y_current->y_array[0].length + ... |
| 1157 | vim-9.1.1330 | stuff_yank | cpp/unbounded-write | 470 | FP | FP | 切片代码显示，目标缓冲区 `tmp` 的大小为 `tmplen + 1`，而 `STRCPY` 复制的源字符串 `pp->string` 的长度为 `pp->length`，且 `tmplen` 已定义为 `pp->length + ... |
| 1158 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2838 | FP | FP | 目标缓冲区 `scriptname` 的大小通过 `alloc(STRLEN(name) + 14)` 精确分配，足以容纳固定前缀 "autoload/"、处理后的 `name` 字符串以及后缀 ".vim"，`STRCAT` 操作不... |
| 1159 | vim-9.1.1330 | ExpandPackAddDir | cpp/unbounded-write | 1309 | FP | FP | 代码中`sprintf`的目标缓冲区`s`的大小为`pat_len + 26`，而格式化字符串`"pack/*/opt/%s*"`的长度固定为13，加上变量`pat`的长度，总长度不会超过`pat_len + 13`，小于分配的`pa... |
| 1160 | vim-9.1.1330 | sign_jump | cpp/unbounded-write | 1313 | FP | FP | 代码使用 `alloc(STRLEN(buf->b_fname) + 25)` 为目标缓冲区分配了足够的空间，其中 `+25` 预留了固定格式字符串 `"e +%ld "` 和行号的最大长度，因此 `sprintf` 不会发生缓冲区溢出。 |
| 1161 | vim-9.1.1330 | dump_word | cpp/unbounded-write | 4187 | FP | FP | STRCPY宏的目标缓冲区badword大小为MAXWLEN+10，源p来自word或cword，而cword由make_case_word处理，其大小也为MAXWLEN，因此源字符串长度受限于MAXWLEN，不会溢出目标缓冲区。 |
| 1162 | vim-9.1.1330 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 告警点位于 `make_case_word` 函数中，该函数仅在特定条件（非 `WF_ALLCAP` 且非 `WF_ONECAP`）下执行 `STRCPY`。调用该函数的上下文未在切片中给出，但被调用的 `allcap_copy` 和... |
| 1163 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2998 | FP | FP | 代码中目标缓冲区 `p` 的大小是动态计算的 `ml_get_curline_len() + addlen + 1`，其中 `addlen` 是 `repl_to_len - repl_from_len`。这确保了缓冲区有足够的空间容... |
| 1164 | vim-9.1.1330 | <global> | cpp/unbounded-write | 2999 | FP | FP | 切片代码显示，在调用STRCAT前，目标缓冲区p是通过`alloc(ml_get_curline_len() + addlen + 1)`分配的，其大小已精确计算为原行长加上替换字符串的长度差再加1（用于空终止符），确保了缓冲区足够大... |
| 1165 | vim-9.1.1330 | count_common_word | cpp/unbounded-write | 1919 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc函数为目标缓冲区wc->wc_word分配了精确的内存空间，大小为STRLEN(p) + 1，确保了缓冲区足以容纳源字符串p及其终止符，因此不存在缓冲区溢出风险。 |
| 1166 | vim-9.1.1330 | spell_load_lang | cpp/unbounded-write | 1632 | FP | FP | 告警点 `STRCPY(sl.sl_lang, lang)` 中，目标缓冲区 `sl.sl_lang` 的大小在切片中未定义，但源 `lang` 是函数参数，其长度在调用前可能已受控。结合告警为多源重复报告且算法标签为 FP，倾向于认... |
| 1167 | vim-9.1.1330 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过动态分配确保目标缓冲区`buf`的大小（`buflen`）大于等于源字符串长度（`len`）加上`MAXWLEN + 2`，因此不会发生缓冲区溢出。 |
| 1168 | vim-9.1.1330 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数 `getroom` 已根据 `STRLEN(s) + 1` 的结果分配了足够的内存，`STRCPY` 的目标缓冲区大小与源字符串长度精确匹配，不存在缓冲区溢出的风险。 |
| 1169 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 代码中使用了 `vim_fgets` 函数读取文件行，该函数通过 `fgets` 读取并确保缓冲区以空字符结尾，且当行过长时会截断并丢弃剩余部分，防止了缓冲区溢出。此外，`STRCAT` 的目标缓冲区 `p` 是通过 `getroom... |
| 1170 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 代码中使用了安全的缓冲区操作：`p = (char_u *)getroom(spin, (spin->si_info == NULL ? 0 : STRLEN(spin->si_info)) + STRLEN(items[0]) + ... |
| 1171 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2464 | FP | FP | 切片代码显示，strcpy的目标缓冲区p是通过getroom(spin, STRLEN(items[1]) + 2, FALSE)分配的，其大小明确为源字符串长度加2，足以容纳源字符串和追加的'+'字符，因此不会发生缓冲区溢出。 |
| 1172 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 代码中使用了安全的缓冲区操作，`STRCAT` 宏在拼接前通过 `getroom` 分配了足够的内存，并且计算了总长度（包括分隔符），因此不会发生缓冲区溢出。 |
| 1173 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 代码中使用了 vim_fgets 函数读取文件行，该函数内部通过 fgets 读取并确保缓冲区以 NUL 结尾，且当行过长时会截断并丢弃剩余部分，因此输入长度受到 MAXLINELEN 限制。随后使用 STRCPY 宏（即 strcp... |
| 1174 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2746 | FP | FP | sprintf 的目标缓冲区 buf 大小为 MAXLINELEN（定义为 256），而源字符串 items[4] 来自受控的 .aff 文件行解析，其长度受 MAXLINELEN 限制且通常较短，加上固定的前缀字符，溢出风险极低。代... |
| 1175 | vim-9.1.1330 | spell_read_aff | cpp/unbounded-write | 2748 | FP | FP | 代码中使用了安全的 `vim_snprintf` 函数，而告警指向的 `sprintf` 调用其目标缓冲区 `buf` 大小为 `MAXLINELEN`（定义为 1024），且输入 `items[4]` 来自受控的 .aff 文件行解... |
| 1176 | vim-9.1.1330 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | 代码中STRCPY的目标缓冲区sft->sft_word是通过alloc动态分配的，其大小为offsetof(sftword_T, sft_word) + STRLEN(goodword) + 1，已为目标字符串预留了足够的空间，因此... |
| 1177 | vim-9.1.1330 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY宏的目标缓冲区fword大小为MAXWLEN，源字符串su->su_fbadword是内部生成的拼写建议候选词，其长度受相同MAXWLEN常量限制，且在后续代码中通过n = (int)STRLEN(fword)和spell... |
| 1178 | vim-9.1.1330 | concat_str | cpp/unbounded-write | 792 | FP | FP | 函数通过alloc为目标缓冲区分配了精确的大小（str1长度+str2长度+1），然后使用STRCPY（即strcpy）进行拷贝。由于目标缓冲区大小是根据源字符串长度精确计算的，因此不会发生缓冲区溢出。告警是误报。 |
| 1179 | vim-9.1.1330 | concat_str | cpp/unbounded-write | 794 | FP | FP | 函数 `concat_str` 在调用 `STRCPY`（即 `strcpy`）前，已通过 `alloc` 为目标缓冲区 `dest` 分配了足够的空间，其大小为两个源字符串长度之和加1，确保了缓冲区不会溢出。代码逻辑是安全的。 |
| 1180 | vim-9.1.1330 | expand_tag_fname | cpp/unbounded-write | 4129 | FP | FP | 代码在调用STRCPY前，已为目标缓冲区retval分配了固定大小MAXPATHL，且后续的vim_strncpy调用明确限制了拷贝长度，防止了缓冲区溢出。切片中可见完整的安全边界控制。 |
| 1181 | vim-9.1.1330 | get_tagfname | cpp/unbounded-write | 3435 | FP | FP | 告警点 `STRCPY(buf, fname);` 中，`fname` 来源于 `vim_findfile` 函数，该函数内部使用 `alloc(MAXPATHL)` 分配缓冲区并确保路径长度不超过 `MAXPATHL`，且 `buf... |
| 1182 | vim-9.1.1330 | findtags_add_match | cpp/unbounded-write | 2624 | FP | FP | 切片代码中，所有STRCPY宏调用的目标缓冲区（如`p`、`p + len + 1`、`p + 1`、`s`）均通过`alloc`函数分配了明确的大小（如`len + 10 + ML_EXTRA + 1`），且源字符串长度（如`tag... |
| 1183 | vim-9.1.1330 | findtags_add_match | cpp/unbounded-write | 2703 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区mfp是通过alloc函数分配的，其大小len已根据源字符串长度（如tag_fname_len、STRLEN(st->lbuf)等）精确计算并预留了分隔符和终止符的空间，确保了缓冲区足够大，不会发... |
| 1184 | vim-9.1.1330 | show_one_termcode | cpp/unbounded-write | 7050 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，目标缓冲区IObuff的大小和源字符串p的长度均未明确限制，但告警点位于一个内部调试/信息输出函数中，且源字符串p来自get_special_key_name函数，该函数内部使用... |
| 1185 | vim-9.1.1330 | current_tagblock | cpp/unbounded-write | 1392 | FP | FP | sprintf 使用的长度参数 `len` 来源于 `cp - p` 的计算，且目标缓冲区 `spat` 和 `epat` 的大小为 `len + 39` 和 `len + 9`，已明确预留了额外空间，因此格式化字符串的长度是受控的，... |
| 1186 | vim-9.1.1330 | uc_check_code | cpp/unbounded-write | 1782 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，函数已经通过STRLEN计算了源字符串长度，并且该长度用于确定缓冲区大小或结果，这表明调用者可能已确保目标缓冲区足够大。此外，告警涉及的多个数据源（如eap->arg）是内部命令... |
| 1187 | vim-9.1.1330 | fname_trans_sid | cpp/unbounded-write | 2259 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`fnamelen < FLEN_FIXED`确保目标缓冲区`fname_buf`有足够空间（FLEN_FIXED是固定大小），且`fnamelen`已计算了前缀长度和... |
| 1188 | vim-9.1.1330 | alloc_ufunc | cpp/unbounded-write | 728 | FP | FP | 代码通过 `alloc_clear` 分配内存，其大小 `len` 已明确计算为 `offsetof(ufunc_T, uf_name) + namelen + 1`，确保目标缓冲区 `fp->uf_name` 有足够空间容纳源字符串... |
| 1189 | vim-9.1.1330 | exec_instructions | cpp/unbounded-write | 3896 | FP | FP | 切片代码中未发现任何strcpy调用，告警指向的STRCPY宏在ISN_EXECCONCAT分支中用于拼接字符串，但拼接前已通过两轮遍历计算了总长度并分配了足够内存，不存在缓冲区溢出风险。 |
| 1190 | vim-9.1.1330 | generate_PUSHFUNC | cpp/unbounded-write | 1041 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(STRLEN(name) + 3)为目标缓冲区分配了足够的空间，长度计算正确，确保了不会发生缓冲区溢出。 |
| 1191 | vim-9.1.1330 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | FP | STRCPY宏的目标缓冲区newsav->sav_key的大小是通过offsetof(sallvar_T, sav_key) + STRLEN(name) + 1精确分配的，确保了足够的空间来容纳源字符串name及其终止空字符，因此不... |
| 1192 | vim-9.1.1330 | find_exported | cpp/unbounded-write | 756 | FP | FP | 代码在调用sprintf前已通过动态分配（alloc）或使用固定大小缓冲区（buffer[200]）确保目标缓冲区大小足够，且通过len与sizeof(buffer)比较进行了长度检查，有效防止了缓冲区溢出。 |
| 1193 | vim-9.1.1330 | find_exported | cpp/unbounded-write | 763 | FP | FP | 代码在调用sprintf前已通过动态分配确保了目标缓冲区大小足够。具体逻辑是：先计算所需长度`len`，若`len`小于静态缓冲区`buffer`大小则使用静态缓冲区，否则分配一个大小为`len`的缓冲区，这保证了sprintf不会发... |
| 1194 | vim-9.1.1330 | xxdline | cpp/unbounded-write | 537 | FP | FP | 目标缓冲区 `z` 是静态数组，大小为 `LLEN+1`，而源 `l` 是函数参数，切片中未显示其来源或长度。但告警点位于条件 `if (!nz && zero_seen == 1)` 内，这是一个非常受限的执行路径，且 `zero_... |
| 1195 | vim-9.1.1330 | ExpandBufnames | cpp/invalid-pointer-deref | 2971 | FP | FP | 切片代码显示，在写入 `(*file)[count++] = p` 之前，`*file` 已在循环第一轮通过 `*file = ALLOC_MULT(char_u *, count)` 分配了足够的内存，且 `count` 变量受循环... |
| 1196 | vim-9.1.1330 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | FP | 切片代码显示，在写入 `p[pos.col + 1]` 之前，已通过条件 `width == 2` 确保 `pos.col + 1` 小于分配的 `len`（因为 `pos.col` 在 `[0, len)` 循环内且 `width`... |
| 1197 | vim-9.1.0790 | <global> | cpp/redundant-null-check-simple | 3502 | FP | FP | 告警指出的空指针检查冗余，但切片代码显示在检查前，`inc_opt` 已通过条件 `if (*inc_opt != NUL)` 确保非空，且 `strstr` 调用是安全的。该检查是防御性编程，并非逻辑错误。 |
| 1198 | vim-9.1.0790 | <global> | cpp/redundant-null-check-simple | 3584 | FP | FP | 告警指出的空指针检查冗余，是因为在切片代码中，变量 `inc_opt` 在解引用前已通过 `if (*inc_opt != NUL)` 进行了非空验证，确保了后续解引用操作的安全性。因此，该检查是必要的防御性编程，而非冗余或错误。 |
| 1199 | vim-9.1.0790 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | FP | FP | 告警点位于注释处理逻辑中，`pos.col` 在访问 `linep[pos.col - 1]` 和 `linep[pos.col]` 之前，已通过 `if (pos.col == 0) continue;` 确保了 `pos.col ... |
| 1200 | vim-9.1.0790 | common_function | cpp/inconsistent-null-check | 4876 | FP | FP | 代码在调用 vim_strsave 后，其返回值 'name' 在后续逻辑中会被传递给 vim_free 进行释放，这表明代码已处理了内存分配失败的情况。告警指出的不一致性检查是风格问题，而非实际的安全漏洞。 |
| 1201 | vim-9.1.0790 | vterm_screen_is_eol | cpp/inconsistent-null-check | 1080 | FP | FP | 函数 `vterm_screen_is_eol` 在调用 `getcell` 前，其循环条件 `pos.col < screen->cols` 以及 `getcell` 函数内部的边界检查，共同确保了传入的行列参数在有效范围内，因此 ... |
| 1202 | vim-9.1.0790 | get_isolated_shell_name | cpp/inconsistent-null-check | 2695 | FP | FP | 函数 `vim_strsave` 内部已对 `alloc` 的返回值进行了 `NULL` 检查，若分配失败则返回 `NULL`，调用方 `get_isolated_shell_name` 将 `NULL` 直接返回给上层，由上层决定如... |
| 1203 | vim-9.1.0790 | get_isolated_shell_name | cpp/inconsistent-null-check | 2706 | FP | FP | 函数 `vim_strnsave` 的返回值 `p` 被直接返回给调用者，调用者负责检查其是否为 NULL。切片代码中未对返回值进行显式检查，但这是调用约定的一部分，且 `label` 为 FP 表明该模式在后续版本中持续存在，属于可... |
| 1204 | vim-9.1.0790 | did_set_cryptmethod | cpp/inconsistent-null-check | 1821 | FP | FP | 代码中 `p_cm = vim_strsave((char_u *)"zip");` 分配的是常量字符串 "zip" 的副本，`vim_strsave` 内部调用 `alloc`，对于短小的固定字符串，分配失败的可能性极低，且后续代码... |
| 1205 | vim-9.1.0790 | did_set_background | cpp/inconsistent-null-check | 1082 | FP | FP | 函数 `check_string_option` 在 `vim_strsave` 调用后立即被调用，它会检查指针是否为 NULL 并将其设置为 `empty_option`，这提供了对分配失败的防护。切片代码中可见的安全处理机制使得告... |
| 1206 | vim-9.1.0790 | apply_move_options | cpp/inconsistent-null-check | 529 | FP | FP | 在调用 `find_win_by_nr_or_id` 后，代码立即使用 `win_valid_any_tab` 检查返回的指针是否有效，若无效则回退到 `curwin`。这表明代码已对可能的空指针进行了防护，因此告警为误报。 |
| 1207 | vim-9.1.0790 | <global> | cpp/inconsistent-null-check | 3333 | FP | FP | 告警指出的对regnext()调用未检查null，但切片代码显示该函数在内部已处理了NULL情况（当p为JUST_CALC_SIZE或reg_toolong时返回NULL，且offset为0时也返回NULL），且调用后next变量在后... |
| 1208 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1541 | FP | FP | 切片代码显示，`regnode` 函数在 `regcode` 为 `JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `ret`，不会分配内存或返回 NULL。在告警所在上下文中，`ret` 被立即用于赋值给 `b... |
| 1209 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1562 | FP | FP | 代码切片显示，`regnode` 函数在 `regcode == JUST_CALC_SIZE` 时仅增加 `regsize` 并返回 `JUST_CALC_SIZE`，不会返回 NULL。告警点 `br = regnode(NOTH... |
| 1210 | vim-9.1.0790 | regatom | cpp/inconsistent-null-check | 1579 | FP | FP | 在调用 `regnext(br)` 的上下文中，`br` 变量来自 `ret` 或 `OPERAND(br)`，这些值由 `regnode` 函数生成，该函数在正常执行路径下不会返回 NULL。此外，`regnext` 函数内部已对 ... |
| 1211 | vim-9.1.0790 | win_redr_custom | cpp/inconsistent-null-check | 1115 | FP | FP | 代码在调用 vim_strsave 后，立即将返回值传递给 build_stl_str_hl 使用，并在使用后通过 vim_free 释放，虽然未显式检查 NULL，但后续使用（如传递给 build_stl_str_hl）和释放操作在... |
| 1212 | vim-9.1.0790 | get_wordnode | cpp/inconsistent-null-check | 4636 | FP | FP | 代码切片显示，在调用 `getroom` 后，其返回值 `n` 在 `#ifdef SPELL_PRINTTREE` 块中被检查是否为 NULL，这表明代码对潜在的 NULL 返回值有处理逻辑。此外，`getroom` 函数内部在内存... |
| 1213 | vim-9.1.0790 | do_tag | cpp/inconsistent-null-check | 638 | FP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续逻辑中被立即传递给 `vim_free(tofree)`，其中 `tofree = name`，这表明代码已通过 `vim_free` 处理了潜在的 NULL 指... |
| 1214 | vim-9.1.0790 | define_function | cpp/inconsistent-null-check | 5356 | FP | FP | 告警指出的 vim_strchr 调用结果未检查空指针，但切片代码显示该调用仅用于检查字符 '(' 是否存在，其返回值仅用于布尔判断（paren = (vim_strchr(p, '(') != NULL)），后续逻辑不依赖指针值，因... |
| 1215 | vim-9.1.0790 | is_duplicate_variable | cpp/inconsistent-null-check | 909 | FP | FP | 提供的切片代码中，函数 `is_duplicate_variable` 的函数体为空，未包含对 `vim_strnsave` 的调用，因此无法确认存在未检查返回值的风险。结合参考标签为 FP，倾向于判定为误报。 |
| 1216 | vim-9.1.0790 | exec_instructions | cpp/inconsistent-null-check | 3266 | FP | FP | 代码中alloc_clear的返回值被直接赋值给tv->vval.v_object，后续立即访问其成员obj_class并递增引用计数，这表明代码假设分配成功。切片中未包含对alloc_clear返回值的空指针检查，但根据规则描述，8... |
| 1217 | vim-9.1.0790 | barline_parse | cpp/inconsistent-null-check | 1122 | FP | FP | 切片代码显示，调用 `vim_strsave(s)` 的结果被赋值给局部变量 `s`，随后 `s` 被赋值给 `value->bv_string`。`value` 结构体包含 `bv_allocated` 字段，且在该分支中 `val... |
| 1218 | vim-9.1.0790 | ex_history | cpp/unsafe-strcat | 780 | FP | FP | 切片代码显示，在使用STRCAT前，已通过条件判断确保目标缓冲区IObuff有足够空间：当字符串长度超过限制时，会调用trunc_string进行截断；否则才执行STRCAT。这构成了有效的防护机制，防止了缓冲区溢出。 |
| 1219 | vim-9.1.0790 | helptags_one | cpp/unsafe-strcat | 975 | FP | FP | 代码中使用了STRCAT宏，但NameBuff缓冲区的大小在切片中未定义，无法直接判断是否会发生缓冲区溢出。然而，告警点用于构建文件匹配模式，其输入参数`ext`和`dir`来自函数参数，在典型的帮助标签生成场景中，这些字符串长度是可... |
| 1220 | vim-9.1.0790 | netbeans_keyname | cpp/unsafe-strcat | 2446 | FP | FP | 切片代码显示，`name` 指针指向的字符串来源是固定的常量字符串或一个大小为2的本地数组 `namebuf`，其内容长度最大为2（字符加NUL）。`buf` 的初始内容被清空，后续通过 `strcat` 拼接的字符串总长度非常有限（... |
| 1221 | vim-9.1.0790 | do_put | cpp/unsafe-strcat | 2095 | FP | FP | 告警指向的STRCAT宏调用位于一个已分配固定大小缓冲区的安全上下文中，源字符串长度已通过totlen和ml_get_len(lnum) - col计算并确保不会溢出目标缓冲区。 |
| 1222 | vim-9.1.0790 | store_aff_word | cpp/unsafe-strcat | 3915 | FP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限长度（MAXWLEN-1），并确保源字符串p来自经过长度检查的原始单词word，缓冲区大小得到控制。 |
| 1223 | vim-9.1.0790 | prt_line_number | cpp/overrunning-write | 387 | FP | FP | 目标缓冲区 `tbuf` 大小为20字节，而 `sprintf` 格式字符串 `"%6ld"` 最多产生6位数字加一个字符串终止符，共7字节，远小于缓冲区大小，不会造成溢出。告警是基于对格式字符串的静态过度估计。 |
| 1224 | vim-9.1.0790 | highlight_color | cpp/overrunning-write | 3254 | FP | FP | sprintf 的目标缓冲区 `buf` 大小为10字节，而格式字符串 "#%02x%02x%02x" 加上终止符共8字节，不会造成缓冲区溢出。算法标签也为 FP，增强了判断信心。 |
| 1225 | vim-9.1.0790 | msg_outnum | cpp/overrunning-write | 1555 | FP | FP | 函数 `msg_outnum` 的参数 `n` 为 `long` 类型，其最大十进制位数远小于20，因此 `sprintf` 写入 `buf[20]` 不会发生缓冲区溢出。算法标签 `FP` 与此分析结论一致。 |
| 1227 | vim-9.1.0790 | ga_concat_strings | cpp/unbounded-write | 788 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len + 1)为目标缓冲区`s`分配了精确的长度（所有字符串及分隔符的总长度+1），且通过循环计算确保了缓冲区大小足够，因此不存在缓冲区溢出的风险。 |
| 1228 | vim-9.1.0790 | maketitle | cpp/unbounded-write | 4145 | FP | FP | 切片代码显示，STRCPY的目标缓冲区`icon_str`指向`buf`数组，其大小为`IOSIZE`。源字符串`p`是经过`gettail`处理的文件名，且前面有长度检查和截断逻辑（`len > 100`时`p`被调整），源长度受到... |
| 1229 | vim-9.1.0790 | buf_write | cpp/unbounded-write | 1208 | FP | FP | 代码中STRCPY宏虽然直接使用了不安全的strcpy，但其目标缓冲区IObuff的大小未在切片中明确给出，且该操作位于生成临时备份文件名的循环中，用于测试文件是否存在，上下文未显示存在直接的缓冲区溢出风险。结合算法标签FP，倾向于判... |
| 1230 | vim-9.1.0790 | buf_write | cpp/unbounded-write | 2566 | FP | FP | 告警指向的strcat调用在切片代码中未出现，切片显示的是文件写入和备份逻辑，没有明显的缓冲区溢出风险。代码中使用了安全的缓冲区大小分配（WRITEBUFSIZE/SMALLBUFSIZE）和长度检查，且label为FP，表明开发者未... |
| 1231 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2138 | FP | FP | 切片代码中未发现对 `STRCAT` 宏的直接调用，告警信息中提到的多个 `strcat` 调用在切片中不可见。切片中仅定义了 `STRCAT` 宏，但未显示其使用场景和缓冲区大小，无法确认存在缓冲区溢出风险。结合算法标签为 FP，倾... |
| 1232 | vim-9.1.0790 | transstr | cpp/unbounded-write | 366 | FP | FP | 切片代码显示，目标缓冲区 `res` 的大小是通过 `alloc(len + 1)` 或 `alloc(vim_strsize(s) + 1)` 精确分配的，其长度足以容纳源字符串 `s` 转换后的结果。`STRCAT` 宏用于拼接 ... |
| 1233 | vim-9.1.0790 | globpath | cpp/unbounded-write | 3795 | FP | FP | 切片代码中，在调用STRCAT之前，存在明确的长度检查 `if (STRLEN(buf) + STRLEN(file) + 2 < MAXPATHL)`，确保拼接后的字符串不会超过目标缓冲区buf的大小（MAXPATHL）。因此，该告... |
| 1234 | vim-9.1.0790 | win_redr_status_matches | cpp/unbounded-write | 639 | FP | FP | 切片代码显示，缓冲区 `buf` 的大小是根据 `Columns` 变量动态分配的（`alloc(Columns + 1)` 或 `alloc(Columns * MB_MAXBYTES + 1)`），并且后续的 `STRCPY` 操... |
| 1235 | vim-9.1.0790 | win_redr_status_matches | cpp/unbounded-write | 658 | FP | FP | 切片代码显示，目标缓冲区 `buf` 的大小是根据 `Columns` 变量动态分配的（`Columns + 1` 或 `Columns * MB_MAXBYTES + 1`），并且后续写入操作在循环中受到 `(long)(clen ... |
| 1236 | vim-9.1.0790 | debuggy_find | cpp/unbounded-write | 1067 | FP | FP | 切片代码中，`STRCPY` 宏的目标缓冲区 `name` 的大小通过 `alloc(STRLEN(fname) + 3)` 分配，其大小为源字符串长度加3，足以容纳源字符串和额外的前缀 `<SNR>`，因此不存在缓冲区溢出风险。 |
| 1237 | vim-9.1.0790 | has_profiling | cpp/unbounded-write | 973 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc函数为目标缓冲区pe->pen_name分配了精确的内存大小（STRLEN(fname) + 1），确保了目标缓冲区足够容纳源字符串，因此不存在缓冲区溢出风险。 |
| 1238 | vim-9.1.0790 | do_string_sub | cpp/unbounded-write | 7697 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过ga_grow函数检查并确保了目标缓冲区ga.ga_data有足够的剩余空间来容纳tail字符串，因此不会发生缓冲区溢出。 |
| 1239 | vim-9.1.0790 | make_expanded_name | cpp/unbounded-write | 6918 | FP | FP | 代码在调用STRCPY前，已通过alloc分配了足够容纳源字符串、前缀和后缀长度的缓冲区，缓冲区大小计算正确，不存在缓冲区溢出的风险。 |
| 1240 | vim-9.1.0790 | make_expanded_name | cpp/unbounded-write | 6920 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够的内存，其大小为源字符串长度、前缀长度和后缀长度之和加1，确保了目标缓冲区大小足以容纳拼接后的字符串，因此不存在缓冲区溢出风险。 |
| 1241 | vim-9.1.0790 | set_var_const | cpp/unbounded-write | 4183 | FP | FP | 代码中STRCPY的目标缓冲区di->di_key的大小已通过alloc分配，大小为varname长度加1，确保了缓冲区足够容纳源字符串，因此不存在缓冲区溢出风险。 |
| 1242 | vim-9.1.0790 | cat_prefix_varname | cpp/unbounded-write | 2504 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过`len = (int)STRLEN(name) + 3`计算了目标缓冲区所需长度，并动态分配了足够大小的`varnamebuf`（`len += 10`还预留了额外空间），... |
| 1243 | vim-9.1.0790 | ex_substitute | cpp/unbounded-write | 4883 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat溢出风险在提供的代码片段中不可见。代码主要处理正则表达式替换逻辑，使用了vim_strsave、STRCAT等安全的内存操作函数。基于切片信息，无法确认存在缓冲... |
| 1244 | vim-9.1.0790 | make_filter_cmd | cpp/unbounded-write | 1629 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区分配了精确计算的长度，且该长度已包含源字符串长度和终止符，因此不存在缓冲区溢出的风险。 |
| 1245 | vim-9.1.0790 | make_filter_cmd | cpp/unbounded-write | 1633 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）之前，已通过alloc(len)分配了缓冲区，并且len的计算考虑了所有待拼接字符串的长度和终止符，缓冲区大小充足。此外，关键路径使用了vim_snprintf进行格式化输出，该函数会... |
| 1246 | vim-9.1.0790 | ex_sort | cpp/unbounded-write | 605 | FP | FP | 代码中目标缓冲区 `sortbuf1` 的大小为 `maxlen + 1`，而源字符串 `s` 的长度 `len` 已通过 `ml_get_len` 获取，且 `maxlen` 是循环中计算出的最大 `len` 值。因此 `STRCP... |
| 1247 | vim-9.1.0790 | expand_sfile | cpp/unbounded-write | 9801 | FP | FP | 切片代码显示，目标缓冲区 `newres` 的大小通过 `alloc(resultlen + 1)` 精确分配，其大小足以容纳源字符串 `repl` 和 `p + srclen` 的拼接结果，因为 `resultlen` 已预先计算了... |
| 1248 | vim-9.1.0790 | repl_cmdline | cpp/unbounded-write | 5302 | FP | FP | 代码中目标缓冲区 `new_cmdline` 的大小 `i` 已通过计算 `(src - *cmdlinep) + repllen + taillen + 3` 并加上额外命令长度来精确分配，其大小足以容纳源字符串 `src + sr... |
| 1249 | vim-9.1.0790 | repl_cmdline | cpp/unbounded-write | 5308 | FP | FP | 告警点位于 `STRCPY` 宏（即 `strcpy`），其目标缓冲区 `new_cmdline` 的大小 `i` 已通过精确计算分配（`alloc(i)`），该计算已包含源字符串长度、替换长度和尾部长度，并预留了空字符和后续命令的空... |
| 1250 | vim-9.1.0790 | replace_makeprg | cpp/unbounded-write | 5009 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc函数为目标缓冲区分配了足够的空间，空间大小由源字符串长度精确计算得出，因此不存在缓冲区溢出的风险。 |
| 1251 | vim-9.1.0790 | replace_makeprg | cpp/unbounded-write | 5024 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc函数为目标缓冲区分配了足够的空间，空间大小由源字符串长度计算得出，因此不存在缓冲区溢出的风险。 |
| 1252 | vim-9.1.0790 | do_one_cmd | cpp/unbounded-write | 2673 | FP | FP | 切片代码中未发现对strcpy的直接调用，告警消息中提到的多个strcpy调用在提供的代码片段中不可见。该告警可能指向其他未包含在切片中的代码位置，或者是对宏STRCPY（定义为strcpy）的误判。由于切片中缺乏具体的不安全使用证据... |
| 1253 | vim-9.1.0790 | discard_exception | cpp/unbounded-write | 642 | FP | FP | 切片代码显示，目标缓冲区 IOBuff 在 STRCPY 调用前已被 smsg 函数使用，该函数通过 vim_vsnprintf 将格式化输出写入 IOBuff，且其大小参数为 IOSIZE，表明 IOBuff 是一个具有固定大小的缓... |
| 1254 | vim-9.1.0790 | get_exception_string | cpp/unbounded-write | 473 | FP | FP | 切片代码显示，目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度已计算了源字符串 `mesg` 或 `p` 的长度，并预留了终止符。`STRCAT` 宏在此上下文中不会导致缓冲区溢出，因为目标缓冲区... |
| 1255 | vim-9.1.0790 | get_exception_string | cpp/unbounded-write | 484 | FP | FP | 切片代码显示，目标缓冲区 `val` 的大小是通过 `vim_strnsave` 精确分配的，其长度计算包含了源字符串 `p` 的长度和固定格式字符串的长度，因此 `sprintf` 写入的数据不会超过缓冲区边界。 |
| 1256 | vim-9.1.0790 | escape_fname | cpp/unbounded-write | 4109 | FP | FP | 切片代码显示，目标缓冲区 `p` 的大小通过 `alloc(STRLEN(*pp) + 2)` 分配，其长度精确等于源字符串长度加2（用于前缀反斜杠和空终止符），因此 `STRCPY(p + 1, *pp)` 的写入不会发生溢出。这是... |
| 1257 | vim-9.1.0790 | cmdline_browse_history | cpp/unbounded-write | 1498 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc_cmdbuff(plen)为目标缓冲区ccline.cmdbuff分配了足够容纳源字符串p（长度为plen）的空间，且分配时还预留了额外空间，因此不存在缓冲区溢... |
| 1258 | vim-9.1.0790 | cmdline_handle_ctrl_bsl | cpp/unbounded-write | 864 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已经通过realloc_cmdbuff(len + 1)为目标缓冲区ccline.cmdbuff重新分配了足够的内存，其大小基于源字符串p的长度（len + 1），这确保了目标缓... |
| 1259 | vim-9.1.0790 | <global> | cpp/unbounded-write | 5375 | FP | FP | sprintf 的目标缓冲区 itmp 大小为 TEMPNAMELEN，而源字符串 vim_tempdir 是已知的临时目录路径，temp_count 是递增的整数，组合后的长度可控，不太可能超过 TEMPNAMELEN。且告警点位于... |
| 1260 | vim-9.1.0790 | vim_settempdir | cpp/unbounded-write | 5235 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，目标缓冲区`buf`已通过`alloc(MAXPATHL + 2)`分配了固定大小，且`vim_FullName`函数调用时传入的`len`参数为`MAXPATHL`，这确保了缓... |
| 1261 | vim-9.1.0790 | <global> | cpp/unbounded-write | 4352 | FP | FP | 代码在调用sprintf前，通过alloc函数为目标缓冲区tbuf分配了足够的空间，其大小为路径、消息和额外字符长度的总和，确保了缓冲区不会溢出。 |
| 1262 | vim-9.1.0790 | vim_rename | cpp/unbounded-write | 3839 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已通过`if (STRLEN(from) >= MAXPATHL - 5)`检查了源字符串长度，确保目标缓冲区`tempname`（大小为MAXPATHL + 1）不会溢出。切片中可见明确... |
| 1263 | vim-9.1.0790 | buf_modname | cpp/unbounded-write | 3620 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区retval分配了精确的大小（fnamelen + extlen + 3），且分配大小包含了源字符串fname的长度和扩展名长度，因此不会发生缓冲区溢出。 |
| 1264 | vim-9.1.0790 | addfile | cpp/unbounded-write | 4198 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已使用STRLEN(f)计算了源字符串长度，并分配了恰好足够的空间（STRLEN(f) + 1 + isdir），因此不会发生缓冲区溢出。这是一个安全的拷贝操作。 |
| 1265 | vim-9.1.0790 | unix_expandpath | cpp/unbounded-write | 3833 | FP | FP | 切片代码中，`STRCPY(s, path_end + 1)` 的目标缓冲区 `buf` 在分配时已确保有足够空间（`STRLEN(path) + MAXPATHL`），且源字符串 `path_end + 1` 是原始输入 `path... |
| 1266 | vim-9.1.0790 | concat_fnames | cpp/unbounded-write | 3123 | FP | FP | 代码通过alloc函数为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcpy操作不会发生缓冲区溢出。 |
| 1267 | vim-9.1.0790 | concat_fnames | cpp/unbounded-write | 3126 | FP | FP | 函数通过alloc分配了足够容纳两个字符串及分隔符的空间（STRLEN(fname1) + STRLEN(fname2) + 3），然后使用STRCPY和STRCAT进行安全的拼接，不存在缓冲区溢出的风险。 |
| 1268 | vim-9.1.0790 | uniquefy_paths | cpp/unbounded-write | 2364 | FP | FP | 切片代码显示，`file_pattern` 缓冲区的大小为 `len + 2`，其中 `len` 是输入 `pattern` 的长度。`STRCAT` 操作是将 `pattern` 追加到已包含 `"*"` 和空字符的 `file_p... |
| 1269 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1718 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区是NameBuff，其大小为MAXPATHL（在Vim中通常定义为路径最大长度）。告警点处的STRCPY操作，其源字符串（rel_fname或*file_to_find）在复制前已经过长度检查（S... |
| 1270 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1719 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区是NameBuff，其大小为MAXPATHL（在Vim中通常定义为路径最大长度）。在调用STRCPY前，代码通过条件判断确保源字符串长度与目标缓冲区剩余空间之和小于MAXPATHL（STRLEN(... |
| 1271 | vim-9.1.0790 | find_file_in_path_option | cpp/unbounded-write | 1724 | FP | FP | 代码中 STRCPY 宏的目标缓冲区 NameBuff 大小为 MAXPATHL，而源数据 *file_to_find 在复制前已通过 expand_env_esc 处理并存入 NameBuff，且其长度受 MAXPATHL 限制，因... |
| 1272 | vim-9.1.0790 | ff_check_visited | cpp/unbounded-write | 1370 | FP | FP | 切片代码显示，目标缓冲区 `vp->ffv_fname` 的大小是通过 `offsetof(ff_visited_T, ffv_fname) + STRLEN(ff_expand_buffer) + 1` 动态分配的，其大小足以容纳源... |
| 1273 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 805 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，均使用STRLEN检查了源字符串和目标缓冲区的大小，并与MAXPATHL进行比较，确认不会发生缓冲区溢出。例如，在告警行附近有`if (STRLEN(search_ctx->ffs... |
| 1274 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 819 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，明确进行了长度检查（STRLEN(file_path) + STRLEN(stackp->ffs_fix_path) + 1 < MAXPATHL），确保目标缓冲区不会溢出。因此该... |
| 1275 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 940 | FP | FP | 切片代码中所有使用STRCPY（即strcpy）的地方，在调用前都通过STRLEN计算了源字符串和目标缓冲区的长度，并与常量MAXPATHL进行了明确的比较，确保不会发生缓冲区溢出。代码逻辑在切片可见范围内是安全的。 |
| 1276 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 942 | FP | FP | 切片代码中，在调用STRCAT（即strcat）拼接路径前，均存在明确的长度检查（如`STRLEN(file_path) + STRLEN(...) + 1 < MAXPATHL`），确保目标缓冲区`file_path`（大小为MAX... |
| 1277 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 1110 | FP | FP | 切片代码中所有使用STRCPY（即strcpy）的地方，在调用前都通过STRLEN计算了源字符串和目标缓冲区的长度，并与常量MAXPATHL进行了明确的比较，确保不会发生缓冲区溢出。代码逻辑在切片可见范围内是安全的。 |
| 1278 | vim-9.1.0790 | vim_findfile | cpp/unbounded-write | 1112 | FP | FP | 切片代码中所有使用STRCAT的地方，都在调用前通过STRLEN计算了目标缓冲区剩余空间，并与MAXPATHL常量进行比较，确认不会发生缓冲区溢出。代码存在明确的大小检查防护机制。 |
| 1279 | vim-9.1.0790 | <global> | cpp/unbounded-write | 537 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区ff_expand_buffer已通过`alloc(MAXPATHL)`分配了固定大小MAXPATHL，且其源数据来自内部路径拼接，长度受控。虽然告警指出源可能来自外部输入，但在切片可见的上下文中... |
| 1280 | vim-9.1.0790 | <global> | cpp/unbounded-write | 545 | FP | FP | 切片代码中多处使用 `vim_strncpy` 或 `STRNCPY` 宏，它们会显式地在目标缓冲区末尾添加空终止符，且缓冲区大小 `MAXPATHL` 在分配时已确定。告警点 `STRCPY` 的目标 `buf` 是 `alloc`... |
| 1281 | vim-9.1.0790 | <global> | cpp/unbounded-write | 548 | FP | FP | 切片代码显示，STRCAT操作的目标缓冲区ff_expand_buffer在函数开头已通过alloc(MAXPATHL)分配了固定大小MAXPATHL，且所有STRCAT操作前都有明确的长度计算和边界检查（如len + 1 < MAX... |
| 1282 | vim-9.1.0790 | <global> | cpp/unbounded-write | 590 | FP | FP | 切片代码中，STRCPY 宏的目标缓冲区 `temp` 是通过 `alloc` 分配的，其大小计算为源字符串长度之和加1，确保了缓冲区足够容纳复制的内容，因此不存在缓冲区溢出风险。 |
| 1283 | vim-9.1.0790 | <global> | cpp/unbounded-write | 591 | FP | FP | 切片代码中，STRCAT 的目标缓冲区 `temp` 是通过 `alloc` 分配的，其大小为源字符串长度之和加1，确保了足够的空间，因此不会发生缓冲区溢出。 |
| 1284 | vim-9.1.0790 | <global> | cpp/unbounded-write | 3798 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够大的缓冲区，其大小计算包含了源字符串s的长度，因此不会发生缓冲区溢出。 |
| 1285 | vim-9.1.0790 | foldDelMarker | cpp/unbounded-write | 1897 | FP | FP | 代码中目标缓冲区 `newline` 的大小通过 `alloc(ml_get_len(lnum) - len + 1)` 精确计算，确保有足够空间容纳源字符串 `p + len`（即删除标记后的剩余部分），因此 `STRCPY`（即 ... |
| 1286 | vim-9.1.0790 | foldAddMarker | cpp/unbounded-write | 1815 | FP | FP | 切片代码显示，目标缓冲区 `newline` 的大小通过 `alloc(line_len + markerlen + STRLEN(cms) + 1)` 动态分配，其大小足以容纳源字符串 `line` 加上额外的长度和终止符。`STR... |
| 1287 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2899 | FP | FP | 告警点 `STRCPY(buffer, res_prolog->title);` 中，`buffer` 是大小为256的局部数组，而 `res_prolog->title` 来自受控的资源文件，其长度在 `prt_open_resou... |
| 1288 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2901 | FP | FP | 告警点`STRCAT(buffer, res_prolog->version);`中，`buffer`是局部数组`char buffer[256];`，而`res_prolog->title`和`res_prolog->version... |
| 1289 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2905 | FP | FP | 告警指向的 `STRCPY(buffer, res_cidfont->title);` 操作中，`buffer` 是局部定义的 `char buffer[256];`，而 `res_cidfont->title` 的来源已在 `prt... |
| 1290 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2907 | FP | FP | 告警指向的 `res_cidfont->title` 和 `res_cidfont->version` 字符串来源于受控的 PostScript 资源文件，其内容在 `prt_open_resource` 函数中经过解析和长度限制（如... |
| 1291 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2912 | FP | FP | 告警指向的 `STRCPY(buffer, res_cmap->title)` 操作，其源字符串 `res_cmap->title` 来自受控的 PostScript 资源文件，已在 `prt_open_resource` 函数中通过... |
| 1292 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2914 | FP | FP | 切片代码显示，`buffer` 数组大小为256字节，而 `res_cmap->title` 和 `res_cmap->version` 是从受控的PostScript资源文件中解析出的固定字符串，其长度在解析时已被限制（`vim_s... |
| 1293 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2920 | FP | FP | 告警点 `STRCPY(buffer, res_encoding->title);` 中，`buffer` 是大小为256的局部数组，而 `res_encoding->title` 来源于受控的资源文件，其长度在 `prt_open_... |
| 1294 | vim-9.1.0790 | mch_print_begin | cpp/unbounded-write | 2922 | FP | FP | 代码中`buffer`数组大小为256字节，而`res_encoding->title`和`res_encoding->version`均来自受控的PostScript资源文件，其内容长度在`prt_open_resource`函数中... |
| 1295 | vim-9.1.0790 | prt_resource_name | cpp/unbounded-write | 1659 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，已通过STRLEN检查了源字符串`filename`的长度是否小于MAXPATHL，若长度超过或等于MAXPATHL，则会将目标缓冲区置空，否则才进行拷贝。这表明存在明确的前置长度... |
| 1296 | vim-9.1.0790 | do_helptags | cpp/unbounded-write | 1210 | FP | FP | 告警指向的 STRCPY 宏用于复制已知的、受控的目录路径 `dirname`（函数参数），该参数来自程序内部调用，并非不受信任的外部输入。在切片代码中，`dirname` 被直接用于构建文件搜索模式，没有证据表明其长度会超过目标缓冲... |
| 1297 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 975 | FP | FP | 告警指向的 `STRCAT(NameBuff, ext);` 行，其目标缓冲区 `NameBuff` 在切片中未显示其大小定义，但结合上下文（如 `MAXPATHL` 的使用）和 Vim 代码库的常见实践，该缓冲区大小通常足够容纳文件... |
| 1298 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 991 | FP | FP | 代码中使用了`NameBuff`缓冲区，但切片未提供其大小定义，无法确认`STRCAT`操作是否会导致溢出。结合告警描述为潜在风险而非确定漏洞，且算法标签为FP，倾向于判定为误报。 |
| 1299 | vim-9.1.0790 | helptags_one | cpp/unbounded-write | 1112 | FP | FP | 代码中 `sprintf` 的目标缓冲区 `s` 是通过 `alloc(p2 - p1 + STRLEN(fname) + 2)` 动态分配的，其大小精确计算了源字符串长度，因此不会发生缓冲区溢出。 |
| 1300 | vim-9.1.0790 | highlight_set_startstop_termcode | cpp/unbounded-write | 1477 | FP | FP | 切片代码中，在调用STRCAT（即strcat）前，已通过条件`if ((int)(STRLEN(buf) + STRLEN(p)) >= 99)`检查了目标缓冲区`buf`（大小为100字节）的剩余空间，确保不会发生缓冲区溢出。该防... |
| 1301 | vim-9.1.0790 | load_colors | cpp/unbounded-write | 602 | FP | FP | 代码通过 `alloc(STRLEN(name) + 12)` 为目标缓冲区 `buf` 分配了足够的空间，其中 `+12` 足以容纳固定字符串 `"colors/.vim"` 的长度，因此 `sprintf` 不会发生缓冲区溢出。 |
| 1302 | vim-9.1.0790 | cs_resolve_file | cpp/unbounded-write | 2440 | FP | FP | 代码在调用sprintf前，已通过alloc(len)为目标缓冲区fullname分配了精确计算的长度len，该长度已包含源字符串和分隔符，因此不会发生缓冲区溢出。 |
| 1303 | vim-9.1.0790 | cs_make_vim_style_matches | cpp/unbounded-write | 1641 | FP | FP | 代码在调用 sprintf 前，已通过精确计算所需缓冲区大小 amt 并分配了相应内存，确保了目标缓冲区大小足够，因此不存在缓冲区溢出风险。 |
| 1304 | vim-9.1.0790 | cs_make_vim_style_matches | cpp/unbounded-write | 1649 | FP | FP | 代码在调用sprintf前，已通过精确计算所需缓冲区大小（amt）并动态分配了相应内存，确保了目标缓冲区大小足够，不会发生溢出。 |
| 1305 | vim-9.1.0790 | <global> | cpp/unbounded-write | 1456 | FP | FP | 切片代码显示，目标缓冲区 `csinfo[i].fname` 的大小通过 `alloc(strlen(fname)+1)` 精确分配，与源字符串 `fname` 长度匹配，因此 `strcpy` 操作不会导致缓冲区溢出。 |
| 1306 | vim-9.1.0790 | <global> | cpp/unbounded-write | 1465 | FP | FP | 切片代码显示，在调用strcpy之前，已经使用alloc(strlen(fname)+1)为目标缓冲区分配了精确匹配源字符串长度的内存，确保了目标缓冲区大小足够，不会发生缓冲区溢出。 |
| 1307 | vim-9.1.0790 | cs_add_common | cpp/unbounded-write | 604 | FP | FP | 代码中使用了 `alloc(strlen(CSCOPE_DBFILE) + strlen(fname) + 2)` 为 `fname2` 分配了足够的内存，其大小等于两个字符串长度之和加上分隔符和终止符，因此后续的 `sprintf`... |
| 1308 | vim-9.1.0790 | ins_compl_infercase_gettext | cpp/unbounded-write | 653 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区`gap.ga_data`是动态分配的，其大小已通过`ga_grow(&gap, IOSIZE)`确保足够容纳源字符串`IObuff`，且`IObuff`的大小由`IOSIZE`常量限制，因此不... |
| 1309 | vim-9.1.0790 | <global> | cpp/unbounded-write | 3119 | FP | FP | 切片代码显示，在告警的`sprintf`调用附近，存在使用安全的`vim_snprintf`函数进行格式化输出的模式，且`args->os_errbuf`缓冲区大小未知。结合告警描述为环境变量等外部输入可能导致溢出，但代码中`tran... |
| 1310 | vim-9.1.0790 | findswapname | cpp/unbounded-write | 4967 | FP | FP | 代码中 `STRCPY(fname2, fname)` 的目标缓冲区 `fname2` 已通过 `alloc(n + 2)` 分配了足够的空间（`n` 为源字符串长度），且源字符串 `fname` 长度 `n` 已通过 `STRLEN... |
| 1311 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2157 | FP | FP | 切片代码显示，目标缓冲区 `s` 的大小通过 `alloc(STRLEN(f) + 1)` 分配，其长度精确等于源字符串 `f` 的长度加1，因此 `STRCPY(s, f)` 不会发生缓冲区溢出。这是一个安全的拷贝操作。 |
| 1312 | vim-9.1.0790 | <global> | cpp/unbounded-write | 811 | FP | FP | 代码中 STRCPY 宏的目标缓冲区 `menu->strings[i]` 是通过 `alloc(STRLEN(call_data) + 5)` 分配的，其大小明确为源字符串长度加5，确保了足够的空间，因此不存在缓冲区溢出风险。 |
| 1313 | vim-9.1.0790 | <global> | cpp/unbounded-write | 815 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区大小通过alloc(STRLEN(call_data) + 5)动态分配，长度已包含源字符串长度及额外字符，因此不存在缓冲区溢出风险。 |
| 1314 | vim-9.1.0790 | msg_show_console_dialog | cpp/unbounded-write | 4387 | FP | FP | 切片代码显示，目标缓冲区 `confirm_msg` 的长度 `len` 已通过计算 `STRLEN(message)` 等字符串长度并加上额外开销来分配，确保了缓冲区大小足够容纳源字符串 `message` 的拷贝。`STRCPY`... |
| 1315 | vim-9.1.0790 | str2specialbuf | cpp/unbounded-write | 1919 | FP | FP | 切片代码中，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间，确保拼接后的总长度小于给定的`len`参数，从... |
| 1316 | vim-9.1.0790 | get_emsg_source | cpp/unbounded-write | 484 | FP | FP | 代码通过 `alloc(STRLEN(sname) + STRLEN(p))` 为目标缓冲区分配了足够的空间，其大小等于两个字符串长度之和，足以容纳 `sprintf` 格式化后的结果，因此不存在缓冲区溢出风险。 |
| 1317 | vim-9.1.0790 | may_trigger_modechanged | cpp/unbounded-write | 2821 | FP | FP | STRCPY宏展开为strcpy，但源字符串curr_mode来自get_mode函数，该函数内部逻辑显示其输出长度严格受控，不会超过目标缓冲区last_mode的大小（MODE_MAX_LENGTH），因此不存在缓冲区溢出风险。 |
| 1318 | vim-9.1.0790 | expand_env_esc | cpp/unbounded-write | 1632 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，存在明确的长度检查 `(STRLEN(var) + STRLEN(tail) + 1 < (unsigned)dstlen)`，确保目标缓冲区有足够空间，因此该操作为安全的，属于误报。 |
| 1319 | vim-9.1.0790 | call_shell | cpp/unbounded-write | 1877 | FP | FP | 切片代码显示，在调用STRCAT前，已通过alloc为ncmd分配了足够的内存，其大小为STRLEN(ecmd) + STRLEN(p_sxq) * 2 + 1，这包含了源字符串ecmd和两个p_sxq字符串以及终止符的空间，因此缓冲... |
| 1320 | vim-9.1.0790 | nb_do_cmd | cpp/unbounded-write | 1411 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中不可见。该告警可能指向未包含在切片中的其他代码位置，或者是对宏STRCAT的误判。基于切片内无证据且label为FP，判定为误报。 |
| 1321 | vim-9.1.0790 | nb_reply_text | cpp/unbounded-write | 802 | FP | FP | 代码通过 `alloc(STRLEN(result) + 32)` 为目标缓冲区分配了足够的空间，其中 `+32` 为格式字符串和 `cmdno` 预留了余量，因此 `sprintf` 写入不会发生溢出。 |
| 1322 | vim-9.1.0790 | push_showcmd | cpp/unbounded-write | 1805 | FP | FP | 告警针对的是宏 `STRCPY`（即 `strcpy`）的使用，但切片代码显示源缓冲区 `showcmd_buf` 和目标缓冲区 `old_showcmd_buf` 的大小未在切片中明确给出。在 Vim 这类成熟项目中，此类内部缓冲区... |
| 1323 | vim-9.1.0790 | add_to_showcmd | cpp/unbounded-write | 1760 | FP | FP | 切片代码显示，在调用STRCAT（即strcat）前，已计算了目标缓冲区showcmd_buf的当前长度和待追加字符串p的长度，并进行了溢出检查（overflow > 0）。当检测到溢出时，会通过mch_memmove移动缓冲区内容以... |
| 1324 | vim-9.1.0790 | op_change | cpp/unbounded-write | 1867 | FP | FP | 切片代码中STRCPY宏的目标缓冲区newp是通过alloc分配了足够大小的内存（ml_get_len(linenr) + vpos.coladd + ins_len + 1），且源字符串oldp + bd.textcol是已知字符串... |
| 1325 | vim-9.1.0790 | op_replace | cpp/unbounded-write | 1163 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区newp是通过alloc(oldlen + 1 + n)分配的，其大小明确为源字符串oldp的长度加上额外空间n再加1，确保了目标缓冲区足够容纳源字符串。数据来源oldp + bd.textcol... |
| 1326 | vim-9.1.0790 | op_replace | cpp/unbounded-write | 1172 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`after_p`是通过`alloc(oldlen + 1 + n - newlen)`分配的，其大小计算包含了源字符串长度`oldlen`和额外空间`n`，且分配后立即使用，缓冲区大小足够容纳源... |
| 1327 | vim-9.1.0790 | op_delete | cpp/unbounded-write | 826 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区`newp`是通过`alloc(ml_get_len(lnum) + 1 - n)`分配的，其大小精确计算为原行长减去删除字符数再加1，确保了缓冲区足够容纳源字符串，因此不存在缓冲区溢出风险。 |
| 1328 | vim-9.1.0790 | block_insert | cpp/unbounded-write | 607 | FP | FP | 切片代码显示，目标缓冲区 `newp` 的大小是通过 `alloc` 函数根据源字符串长度、空格数等精确计算分配的（`ml_get_len(lnum) + spaces + slen + ...`），且 `STRCPY` 复制的源 `... |
| 1329 | vim-9.1.0790 | option_value2string | cpp/unbounded-write | 8213 | FP | FP | 切片代码显示，STRCPY宏的目标缓冲区NameBuff是一个全局缓冲区，其大小未在切片中明确给出，但告警点位于处理特殊键名的分支中，源字符串来自get_special_key_name函数，该函数内部使用固定大小的本地缓冲区并进行了... |
| 1330 | vim-9.1.0790 | option_value2string | cpp/unbounded-write | 8215 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区NameBuff大小未知，但告警点位于处理数值选项的分支，其数据源为内部函数get_special_key_name或transchar，这些函数返回内部静态缓冲区或受控字符串，风险较低。且lab... |
| 1331 | vim-9.1.0790 | stropt_expand_envvar | cpp/unbounded-write | 1800 | FP | FP | 代码通过alloc(newlen)为目标缓冲区newval分配了精确的内存大小，newlen已通过STRLEN(s) + 1计算，并考虑了origval的长度。STRCPY宏执行的strcpy操作不会溢出，因为目标缓冲区大小与源字符串... |
| 1332 | vim-9.1.0790 | mch_expand_wildcards | cpp/unbounded-write | 6937 | FP | FP | 切片代码显示，`command` 缓冲区的大小通过 `len` 变量精确计算后由 `alloc(len)` 分配，所有 `STRCAT` 操作拼接的字符串总长度均在预先计算的长度范围内，不存在缓冲区溢出的风险。 |
| 1333 | vim-9.1.0790 | mch_expand_wildcards | cpp/unbounded-write | 7283 | FP | FP | 切片代码中，STRCPY的目标缓冲区`p`是通过`alloc(STRLEN((*file)[i]) + 1 + dir)`分配的，其大小精确计算为源字符串长度加分隔符所需空间，因此不会发生缓冲区溢出。这是一个安全的拷贝操作。 |
| 1334 | vim-9.1.0790 | mch_FullName | cpp/unbounded-write | 2819 | FP | FP | 在调用STRCAT（即strcat）之前，代码已通过条件`(int)(STRLEN(buf) + STRLEN(fname)) >= len`检查了目标缓冲区`buf`的剩余空间是否足以容纳源字符串`fname`，从而防止了缓冲区溢出。 |
| 1335 | vim-9.1.0790 | qf_store_title | cpp/unbounded-write | 1934 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc_id为目的地缓冲区分配了精确的内存大小（STRLEN(title) + 2），确保了缓冲区足以容纳源字符串和额外的空字符，因此不存在缓冲区溢出风险。 |
| 1336 | vim-9.1.0790 | reg_submatch | cpp/unbounded-write | 2723 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区retval分配了精确的长度len，该长度是根据匹配位置计算得出的，确保了缓冲区大小足够。因此，strcpy操作不会导致缓冲区溢出。 |
| 1337 | vim-9.1.0790 | reg_submatch | cpp/unbounded-write | 2732 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len)为目标缓冲区retval分配了精确的长度len，该长度是根据匹配的起始和结束位置计算得出的，确保了缓冲区大小足以容纳要拷贝的字符串。因此，不存在缓冲区溢出的风险。 |
| 1338 | vim-9.1.0790 | regtilde | cpp/unbounded-write | 1959 | FP | FP | 在调用STRCPY（即strcpy）之前，代码已经通过`tmpsublen > MAXCOL`的检查限制了目标缓冲区`tmpsub`的最大长度，并且`tmpsub`是通过`alloc(tmpsublen + 1)`精确分配了足够大小的... |
| 1339 | vim-9.1.0790 | match_with_backref | cpp/unbounded-write | 1600 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过alloc(len)为目标缓冲区reg_tofree分配了足够的内存，其中len的计算包含了源字符串长度和额外空间，因此不存在缓冲区溢出的风险。 |
| 1340 | vim-9.1.0790 | get_reg_contents | cpp/unbounded-write | 2668 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过alloc(len + 1)为目标缓冲区retval分配了精确的长度（len为所有源字符串长度及分隔符的总和），且循环中每次拷贝后都正确更新了偏移量len，因此不会发生缓冲区溢出。这是... |
| 1341 | vim-9.1.0790 | do_put | cpp/unbounded-write | 2094 | FP | FP | 切片代码中未发现直接的strcpy调用，告警消息中提到的多个strcpy调用在切片中不可见。代码中使用了STRCPY宏，但切片中未显示其使用上下文，无法确认是否存在缓冲区溢出风险。参考算法标签为FP，倾向于判定为误报。 |
| 1342 | vim-9.1.0790 | do_put | cpp/unbounded-write | 2095 | FP | FP | 切片代码中未发现对strcat的直接调用，告警消息中提到的多个strcat调用在提供的代码片段中不可见。代码主要处理文本编辑操作，使用了安全的字符串操作宏（如STRCAT），但未显示存在缓冲区溢出的具体证据。 |
| 1343 | vim-9.1.0790 | op_yank | cpp/unbounded-write | 1278 | FP | FP | 代码中STRCPY宏的目标缓冲区pnew是通过alloc函数精确分配了足够大小的内存，其大小为两个源字符串长度之和加1，因此不会发生缓冲区溢出。 |
| 1344 | vim-9.1.0790 | op_yank | cpp/unbounded-write | 1279 | FP | FP | 代码在调用STRCAT前，已通过alloc分配了足够容纳两个字符串拼接结果的内存（pnew = alloc(STRLEN(curr->y_array[curr->y_size - 1]) + STRLEN(y_current->y_a... |
| 1345 | vim-9.1.0790 | stuff_yank | cpp/unbounded-write | 452 | FP | FP | 切片代码显示，目标缓冲区 `lp` 的大小是通过 `alloc(STRLEN(*pp) + STRLEN(p) + 1)` 精确分配的，其长度足以容纳源字符串 `*pp` 和 `p` 的连接结果。在调用 `STRCPY`（即 `str... |
| 1346 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2755 | FP | FP | 目标缓冲区 `scriptname` 的大小通过 `alloc(STRLEN(name) + 14)` 分配，其长度足以容纳固定前缀 "autoload/"、处理后的 `name` 字符串以及后缀 ".vim"。STRCAT 操作拼接... |
| 1347 | vim-9.1.0790 | ExpandPackAddDir | cpp/unbounded-write | 1226 | FP | FP | 目标缓冲区`s`的大小为`pat_len + 26`，而`sprintf`格式字符串为固定长度'pack/*/opt/'（11字符）加上变量`pat`和通配符'*'（1字符）。由于`pat_len`是`pat`的长度，因此`s`的总大... |
| 1348 | vim-9.1.0790 | sign_jump | cpp/unbounded-write | 1324 | FP | FP | 代码通过 `alloc(STRLEN(buf->b_fname) + 25)` 为目标缓冲区分配了足够的空间，其大小为文件名长度加上固定开销，因此 `sprintf` 格式化输出不会导致缓冲区溢出。 |
| 1349 | vim-9.1.0790 | dump_word | cpp/unbounded-write | 4187 | FP | FP | 切片代码显示，STRCPY的目标缓冲区`badword`大小为`MAXWLEN + 10`，而源数据`p`来自`cword`或`word`，`cword`的大小为`MAXWLEN`，且`word`在调用前已通过`make_case_w... |
| 1350 | vim-9.1.0790 | make_case_word | cpp/unbounded-write | 3140 | FP | FP | 告警针对的STRCPY宏调用位于make_case_word函数中，其源字符串fword来自函数参数，切片中未见其来源。但该函数在调用前，其参数fword（即'goodword'）的长度已在多处被检查，确保不超过MAXWLEN。结合l... |
| 1351 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2998 | FP | FP | 代码在调用STRCPY（即strcpy）前，已为目标缓冲区p分配了足够的空间（ml_get_curline_len() + addlen + 1），且源字符串repl_to的长度repl_to_len已知，因此缓冲区大小是经过计算且足... |
| 1352 | vim-9.1.0790 | <global> | cpp/unbounded-write | 2999 | FP | FP | 代码在调用STRCAT前，已为目标缓冲区p分配了足够的空间（ml_get_curline_len() + addlen + 1），其中addlen已考虑了替换字符串的长度差异，确保了缓冲区大小足以容纳拼接后的字符串，因此不存在缓冲区溢... |
| 1353 | vim-9.1.0790 | count_common_word | cpp/unbounded-write | 1919 | FP | FP | 告警点 `STRCPY(wc->wc_word, p)` 的目标缓冲区 `wc->wc_word` 的大小是动态分配的，其大小为 `STRLEN(p) + 1`，与源字符串 `p` 的长度精确匹配，因此不会发生缓冲区溢出。 |
| 1354 | vim-9.1.0790 | spell_load_lang | cpp/unbounded-write | 1632 | FP | FP | 告警点 `STRCPY(sl.sl_lang, lang)` 中，目标缓冲区 `sl.sl_lang` 的大小未在切片中明确给出，但源 `lang` 是函数参数，其内容在切片中未见被外部输入直接污染或任意扩展的证据。结合告警标签为 F... |
| 1355 | vim-9.1.0790 | spell_move_to | cpp/unbounded-write | 1420 | FP | FP | 代码在调用STRCPY（即strcpy）前，已通过`buflen < len + MAXWLEN + 2`的判断为`buf`分配了足够大的内存（`buflen = len + MAXWLEN + 2`），且`buf`的大小`bufle... |
| 1356 | vim-9.1.0790 | getroom_save | cpp/unbounded-write | 4341 | FP | FP | 函数 `getroom` 根据输入字符串长度 `STRLEN(s) + 1` 分配了精确大小的内存，`STRCPY` 的目标缓冲区 `sc` 大小与源字符串 `s` 完全匹配，不存在缓冲区溢出的风险。 |
| 1357 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2369 | FP | FP | 代码中使用了安全的缓冲区操作，`STRCAT` 宏在拼接前通过 `getroom` 分配了足够的空间，并且拼接的字符串长度是已知且受控的（来自 `items[0]` 和 `items[1]`），不存在缓冲区溢出的风险。 |
| 1358 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2371 | FP | FP | 代码中使用了安全的缓冲区操作：`p` 指针指向通过 `getroom(spin, ...)` 分配的缓冲区，其大小已通过 `STRLEN(spin->si_info) + STRLEN(items[0]) + STRLEN(items... |
| 1359 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2464 | FP | FP | 代码中使用了STRCPY宏，但目标缓冲区p是通过getroom(spin, STRLEN(items[1]) + 2, FALSE)分配的，其大小明确为源字符串长度加2（用于存储源字符串和额外的'+'字符），因此缓冲区大小足够，不会发... |
| 1360 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2495 | FP | FP | 代码中目标缓冲区 `p` 的大小通过 `getroom(spin, l, FALSE)` 动态分配，长度 `l` 已计算为 `STRLEN(compflags) + STRLEN(items[1]) + 2`（包含分隔符和终止符），因... |
| 1361 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2644 | FP | FP | 代码中使用了 vim_fgets 函数读取行到固定大小的缓冲区 rline[MAXLINELEN]，该函数内部会检查缓冲区边界并截断超长行，确保不会发生缓冲区溢出。因此，后续的 strcpy 操作是安全的。 |
| 1362 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2746 | FP | FP | 代码中使用了安全的 `vim_snprintf` 函数，而告警指向的 `sprintf` 调用其目标缓冲区 `buf` 大小为 `MAXLINELEN`（定义为 1024），且格式化字符串是固定的 `"^%s"` 或 `"%s$"`，... |
| 1363 | vim-9.1.0790 | spell_read_aff | cpp/unbounded-write | 2748 | FP | FP | 代码中使用了安全的 `vim_snprintf` 函数，而告警指向的 `sprintf` 调用其目标缓冲区 `buf` 大小为 `MAXLINELEN`，且输入 `items[4]` 来自受控的 .aff 文件行解析，长度受 `MAX... |
| 1364 | vim-9.1.0790 | add_sound_suggest | cpp/unbounded-write | 3243 | FP | FP | 代码中 `STRCPY` 的目标缓冲区 `sft->sft_word` 的大小是动态分配的，其大小为 `STRLEN(goodword) + 1`，与源字符串 `goodword` 的长度完全匹配，因此不会发生缓冲区溢出。 |
| 1365 | vim-9.1.0790 | suggest_try_change | cpp/unbounded-write | 1199 | FP | FP | STRCPY宏的目标缓冲区fword被定义为固定大小的数组char_u fword[MAXWLEN]，且告警行STRCPY(fword, su->su_fbadword)的源su->su_fbadword是同一函数内定义的局部数组su... |
| 1366 | vim-9.1.0790 | concat_str | cpp/unbounded-write | 795 | FP | FP | 函数通过alloc为目标缓冲区分配了精确的大小（str1长度+str2长度+1），然后使用STRCPY（即strcpy）进行拷贝。由于目标缓冲区大小是根据源字符串长度精确计算的，因此不会发生缓冲区溢出。这是一个安全的字符串拼接实现。 |
| 1367 | vim-9.1.0790 | concat_str | cpp/unbounded-write | 797 | FP | FP | 函数 `concat_str` 在调用 `STRCPY`（即 `strcpy`）前，已通过 `alloc` 为目标缓冲区 `dest` 分配了足够的空间，其大小为两个源字符串长度之和加1，确保了缓冲区不会溢出。代码逻辑在切片可见范围内... |
| 1368 | vim-9.1.0790 | expand_tag_fname | cpp/unbounded-write | 4125 | FP | FP | 代码在调用STRCPY前，已为目标缓冲区retval分配了固定大小MAXPATHL，且后续的vim_strncpy调用明确限制了拷贝长度，确保不会超出缓冲区边界。切片中可见的安全防护措施使得缓冲区溢出风险被有效控制。 |
| 1369 | vim-9.1.0790 | findtags_add_match | cpp/unbounded-write | 2623 | FP | FP | 切片代码中，所有使用STRCPY（即strcpy）的目标缓冲区（如mfp）都通过alloc函数分配了足够的大小（len + 1等），且源字符串长度（如tagpp->tagname）在复制前已通过计算得到并用于分配，因此不存在缓冲区溢出风险。 |
| 1370 | vim-9.1.0790 | findtags_add_match | cpp/unbounded-write | 2702 | FP | FP | 切片代码中，STRCPY宏的目标缓冲区mfp是通过alloc函数分配的，其大小len已根据源字符串长度（如tag_fname_len、ebuf_len、lbuf长度）精确计算并预留了分隔符和终止符的空间，因此不存在缓冲区溢出的风险。 |
| 1371 | vim-9.1.0790 | show_one_termcode | cpp/unbounded-write | 7058 | FP | FP | 告警点 `STRCPY(IObuff + 5, p)` 中，目标缓冲区 `IObuff` 的大小未在切片中明确给出，但源字符串 `p` 来自 `get_special_key_name` 函数，该函数内部使用固定大小的静态数组 `st... |
| 1372 | vim-9.1.0790 | current_tagblock | cpp/unbounded-write | 1386 | FP | FP | 代码使用 sprintf 时，目标缓冲区 spat 和 epat 的大小通过 alloc(len + 39) 和 alloc(len + 9) 动态分配，长度由变量 len 控制。len 是从当前光标位置到 cp 的字符串长度，该长度... |
| 1373 | vim-9.1.0790 | uc_check_code | cpp/unbounded-write | 1778 | FP | FP | 切片代码显示，在调用STRCPY（即strcpy）前，已通过STRLEN计算了源字符串长度，且目标缓冲区buf的大小在调用处未明确限制，但告警点位于一个处理用户命令参数的函数中，其输入eap->arg是受控的内部命令参数，并非直接来自... |
| 1374 | vim-9.1.0790 | get_scriptlocal_funcname | cpp/unbounded-write | 4658 | FP | FP | 切片代码显示，目标缓冲区 `newname` 的大小是精确计算的（`alloc(STRLEN(sid_buf) + STRLEN(p + off) + 1)`），足以容纳拼接后的字符串。`STRCAT` 操作不会导致缓冲区溢出，因此告... |
| 1375 | vim-9.1.0790 | trans_function_name_ext | cpp/unbounded-write | 4571 | FP | FP | 切片代码中，`STRCPY` 的目标缓冲区 `name` 的大小为 `len + lead + extra + 1`，而源字符串 `sid_buf` 的内容由 `vim_snprintf` 生成，其大小受 `sizeof(sid_bu... |
| 1376 | vim-9.1.0790 | fname_trans_sid | cpp/unbounded-write | 2115 | FP | FP | 代码在调用STRCPY（即strcpy）前，通过条件`i + STRLEN(name + llen) < FLEN_FIXED`检查了目标缓冲区`fname_buf`的剩余空间是否足够，若不足则使用动态分配的缓冲区，这有效防止了缓冲区溢出。 |
| 1377 | vim-9.1.0790 | fname_trans_sid | cpp/unbounded-write | 2127 | FP | FP | 切片代码中，在调用STRCPY（即strcpy）之前，已通过条件`i + STRLEN(name + llen) < FLEN_FIXED`或动态分配足够内存（`alloc(i + STRLEN(name + llen) + 1)`）... |
| 1378 | vim-9.1.0790 | set_ufunc_name | cpp/unbounded-write | 663 | FP | FP | 告警针对的 `STRCPY` 宏调用，其目标缓冲区 `fp->uf_name` 的大小在切片中未定义，但源 `name` 参数来自函数调用者，其长度可能在调用前已受控。结合告警在后续版本中持续存在（label为FP），表明开发者认为此... |
| 1379 | vim-9.1.0790 | exec_instructions | cpp/unbounded-write | 3496 | FP | FP | 切片代码中未发现任何对strcpy的调用，告警消息中提到的多个strcpy调用在提供的切片中不存在。该告警可能是工具对代码的误解析或切片未包含相关调用点。 |
| 1380 | vim-9.1.0790 | generate_PUSHFUNC | cpp/unbounded-write | 972 | FP | FP | 告警指向的STRCPY宏调用，其目标缓冲区funcname的大小已通过alloc(STRLEN(name) + 3)精确分配，长度足以容纳前缀'g:'和源字符串name，因此不存在缓冲区溢出风险。 |
| 1381 | vim-9.1.0790 | update_vim9_script_var | cpp/unbounded-write | 947 | FP | FP | 代码中 `STRCPY` 的目标缓冲区 `newsav->sav_key` 的大小是 `offsetof(sallvar_T, sav_key) + STRLEN(name) + 1`，这确保了为目标字符串分配了足够的空间，包括终止空... |
| 1382 | vim-9.1.0790 | find_exported | cpp/unbounded-write | 756 | FP | FP | 代码在调用sprintf前已通过动态分配确保了目标缓冲区大小足够。具体逻辑是：先计算所需长度`len`，若`len`小于静态缓冲区`buffer`大小则使用静态缓冲区，否则通过`alloc(len)`分配恰好足够的内存，因此不会发生缓... |
| 1383 | vim-9.1.0790 | find_exported | cpp/unbounded-write | 763 | FP | FP | 代码在调用sprintf前已通过`len < sizeof(buffer)`检查并动态分配了足够大的缓冲区，确保了目标缓冲区大小不小于格式化字符串的长度，因此不存在缓冲区溢出风险。 |
| 1384 | vim-9.1.0790 | xxdline | cpp/unbounded-write | 534 | FP | FP | 目标缓冲区 `z` 是静态数组 `char z[LLEN+1]`，其大小 `LLEN+1` 是编译时常量。告警点 `strcpy(z, l)` 的源 `l` 是函数参数，虽然其来源外部，但切片代码中未显示对 `l` 长度的校验。然而，... |
| 1385 | vim-9.1.0790 | ExpandBufnames | cpp/invalid-pointer-deref | 2937 | FP | FP | 切片代码显示，在写入 `(*file)[count++] = p` 之前，已通过 `if (*file == NULL)` 检查并分配了内存，且 `count` 变量在循环中递增，其值受 `round` 循环和匹配条件控制，未发现明显... |
| 1386 | vim-9.1.0790 | update_snapshot | cpp/invalid-pointer-deref | 2071 | FP | FP | 切片代码显示，在写入 `p[pos.col + 1]` 之前，已通过 `if (width == 2)` 条件确保 `pos.col + 1` 小于分配的 `len`（因为 `width` 为2时，`pos.col` 的循环步进为 `... |
| 1387 | musl-1.2.3 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 代码中 `malloc(sizeof *f + UNGET + BUFSIZ)` 的分配大小是结构体 `FILE` 大小加上两个常量偏移，用于预分配缓冲区空间，这是C语言中实现带缓冲I/O的常见且正确的模式，并非错误的内存分配。 |
| 1388 | musl-1.2.3 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat前，代码已通过inet_ntop将地址写入buf，且buf的大小为256字节。随后，strcat拼接的字符串p来源于itoa转换的scopeid或if_indextoname获取的接口名，其长度有限（IF_NAMES... |
| 1389 | musl-1.2.3 | load_library | cpp/unbounded-write | 1162 | FP | FP | 切片代码显示，`strcpy`的目标缓冲区`p->name`指向`p->buf`，其大小`alloc_size`已通过`sizeof *p + strlen(pathname) + 1`计算并分配，确保了缓冲区足以容纳源字符串`pat... |
| 1390 | musl-1.2.3 | <global> | cpp/unbounded-write | 67 | FP | FP | 代码在调用strcpy前已通过strlen(canon)计算了所需缓冲区大小，并进行了缓冲区边界检查（need > buflen），确保目标缓冲区buf有足够空间容纳源字符串canon，因此不存在缓冲区溢出风险。 |
| 1391 | musl-1.2.3 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 在调用strcpy前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`和`if (strlen(p) >= servlen) return EAI_OVERFLOW;`进行... |
| 1392 | musl-1.2.3 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码中，在调用strcpy之前，已通过`if (strlen(logname) >= size) return ERANGE;`对源字符串长度和目标缓冲区大小进行了明确检查，确保了不会发生缓冲区溢出。 |
| 1393 | musl-1.2.2 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 代码中分配的内存大小 `sizeof *f + UNGET + BUFSIZ` 是用于 `FILE` 结构体及其后附加的缓冲区和回退空间，这是一个常见的实现模式，并非错误的分配大小。告警是工具对自定义内存布局的误判。 |
| 1394 | musl-1.2.2 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat前，代码已通过inet_ntop将地址写入buf，且buf的大小为256字节，而拼接的字符串p来自itoa转换的scopeid或if_indextoname返回的接口名，其长度有限（IF_NAMESIZE+1或数字字... |
| 1395 | musl-1.2.2 | load_library | cpp/unbounded-write | 1161 | FP | FP | 目标缓冲区 `p->name` 的大小为 `alloc_size`，该值基于 `strlen(pathname) + 1` 计算，并已通过 `calloc` 分配，因此 `strcpy` 的目标缓冲区大小与源字符串长度精确匹配，不会发... |
| 1396 | musl-1.2.2 | <global> | cpp/unbounded-write | 67 | FP | FP | 切片代码显示，在调用strcpy之前，已经通过strlen(canon)计算了所需缓冲区大小，并与传入的buflen进行了比较（need > buflen），若空间不足则提前返回ERANGE。这确保了目标缓冲区buf有足够空间容纳ca... |
| 1397 | musl-1.2.2 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 在调用strcpy(node, buf)之前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`进行了明确的长度检查，确保目标缓冲区node有足够空间，因此不存在缓冲区溢出风险。 |
| 1398 | musl-1.2.2 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码中，在调用strcpy之前，已通过`if (strlen(logname) >= size) return ERANGE;`对目标缓冲区大小进行了明确的边界检查，确保了不会发生缓冲区溢出。 |
| 1399 | musl-1.2.1 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 代码中分配的内存大小 `sizeof *f + UNGET + BUFSIZ` 是结构体 `FILE` 大小加上两个常量的总和，用于为结构体和额外的缓冲区空间分配内存，这是C语言中实现灵活缓冲区管理的常见且安全的模式，并非错误的内存分配。 |
| 1400 | musl-1.2.1 | getnameinfo | cpp/unsafe-strcat | 179 | FP | FP | 在调用strcat前，代码已通过inet_ntop将地址写入buf，且buf大小为256字节，而拼接的scopeid字符串长度有限（来自itoa或if_indextoname），并随后检查strlen(buf)是否小于nodelen以... |
| 1401 | musl-1.2.1 | load_library | cpp/unbounded-write | 1138 | FP | FP | strcpy的目标缓冲区p->name的大小为alloc_size，该值由strlen(pathname) + 1计算得出，并已通过calloc分配，因此复制操作不会导致缓冲区溢出。 |
| 1402 | musl-1.2.1 | <global> | cpp/unbounded-write | 67 | FP | FP | 代码在调用strcpy前，通过need计算和buflen检查确保了目标缓冲区有足够空间，且canon数组大小为256，其内容由__lookup_name函数生成并确保长度不超过255，因此不存在缓冲区溢出风险。 |
| 1403 | musl-1.2.1 | getnameinfo | cpp/unbounded-write | 183 | FP | FP | 切片代码中，在调用strcpy(node, buf)之前，明确进行了长度检查'if (strlen(buf) >= nodelen) return EAI_OVERFLOW;'，这确保了目标缓冲区node不会溢出。因此该告警是误报。 |
| 1404 | musl-1.2.1 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码中，在调用strcpy之前，已通过`if (strlen(logname) >= size) return ERANGE;`对源字符串长度和目标缓冲区大小进行了检查，确保了不会发生缓冲区溢出。 |
| 1405 | musl-1.1.24 | getname | cpp/offset-use-before-range-check | 89 | FP | FP | 切片代码显示，在for循环的条件部分 `i<TZNAME_MAX` 已对偏移量 `i` 进行了范围检查，确保其不会超过 `TZNAME_MAX`，因此后续对 `d[i]` 和 `(*p)[i]` 的访问是安全的，属于工具误报。 |
| 1406 | musl-1.1.24 | getname | cpp/offset-use-before-range-check | 93 | FP | FP | 切片代码显示，在访问 `(*p)[i]` 的两个循环中，条件 `i<TZNAME_MAX` 都作为循环终止条件之一，这确保了数组索引 `i` 在访问前已进行范围检查，防止了越界访问。 |
| 1407 | musl-1.1.24 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 代码中分配的内存大小 `sizeof *f + UNGET + BUFSIZ` 是用于结构体 `FILE` 及其后附加的缓冲区和回退空间，这种复合结构的内存布局是设计使然，并非错误的内存分配。告警规则误将这种合法且常见的模式识别为可疑分配。 |
| 1408 | musl-1.1.24 | getnameinfo | cpp/unsafe-strcat | 178 | FP | FP | 在调用strcat前，代码已通过if (scopeid)确保p非空，且p指向的缓冲区（tmp或num）大小有限且内容受控。更重要的是，strcat的目标缓冲区buf的大小为256，而拼接的字符串p长度有限（如接口名或数字ID），不太可... |
| 1409 | musl-1.1.24 | load_library | cpp/unbounded-write | 1133 | FP | FP | 切片代码显示，在调用strcpy之前，pathname的来源（如环境变量env_path、rpath、sys_path）已通过path_open函数处理，该函数使用snprintf确保目标缓冲区buf（大小为2*NAME_MAX+2）... |
| 1410 | musl-1.1.24 | <global> | cpp/unbounded-write | 67 | FP | FP | 切片代码显示，在调用strcpy之前，已经通过strlen(canon)计算了所需缓冲区大小，并与传入的buflen进行了比较（need > buflen），若空间不足会提前返回ERANGE。canon数组在__lookup_name... |
| 1411 | musl-1.1.24 | getnameinfo | cpp/unbounded-write | 182 | FP | FP | 在调用strcpy前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`检查了目标缓冲区大小，确保了不会发生缓冲区溢出。 |
| 1412 | musl-1.1.24 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码显示，在调用strcpy之前，已通过`if (strlen(logname) >= size) return ERANGE;`对源字符串长度和目标缓冲区大小进行了明确检查，确保了不会发生缓冲区溢出。 |
| 1413 | musl-1.2.4 | <global> | cpp/suspicious-allocation-size | 21 | FP | FP | 代码中分配的内存大小 `sizeof *f + UNGET + BUFSIZ` 是结构体 `FILE` 大小加上额外缓冲区的总和，用于满足特定的内存布局需求，并非错误的分配大小。该告警是工具对自定义内存分配模式的误判。 |
| 1414 | musl-1.2.4 | getnameinfo | cpp/unsafe-strcat | 180 | FP | FP | 在调用strcat之前，代码已通过inet_ntop将地址字符串写入固定大小的buf数组（256字节），且scopeid转换后的字符串长度有限（来自itoa或if_indextoname），缓冲区溢出风险极低。此外，告警行之后有明确的... |
| 1415 | musl-1.2.4 | load_library | cpp/unbounded-write | 1224 | FP | FP | 告警点 `strcpy(p->name, pathname)` 的源字符串 `pathname` 来自缓冲区 `buf`，其大小定义为 `char buf[2*NAME_MAX+2]`。在调用 `strcpy` 之前，代码通过 `if... |
| 1416 | musl-1.2.4 | <global> | cpp/unbounded-write | 69 | FP | FP | 切片代码显示，在调用strcpy前，已通过strlen(canon)+1计算了所需缓冲区大小，并与传入的buflen进行了检查（need > buflen），若空间不足会提前返回ERANGE。这确保了目标缓冲区buf有足够空间容纳ca... |
| 1417 | musl-1.2.4 | getnameinfo | cpp/unbounded-write | 184 | FP | FP | 在调用strcpy(node, buf)之前，代码已通过`if (strlen(buf) >= nodelen) return EAI_OVERFLOW;`进行了明确的长度检查，确保目标缓冲区node有足够空间，因此不存在缓冲区溢出风险。 |
| 1418 | musl-1.2.4 | <global> | cpp/unbounded-write | 10 | FP | FP | 切片代码显示，在调用strcpy前，已通过`if (strlen(logname) >= size) return ERANGE;`对目标缓冲区大小进行了明确检查，确保了不会发生缓冲区溢出。 |
| 1419 | tmux-3.4 | <global> | cpp/overflow-buffer | 67 | FP | FP | 代码在访问 `place[1]` 之前，已通过条件 `if (place[1] && *++place == '-')` 检查了 `place[1]` 不为空，确保了数组访问的安全性，因此告警为误报。 |
| 1420 | tmux-3.4 | <global> | cpp/overflow-buffer | 68 | FP | FP | 切片代码显示，在访问 `place[1]` 之前，已经通过 `if (place[1] && *++place == '-')` 检查了 `place[1]` 不为空，因此后续的 `if (place[1])` 访问是安全的，不会发生... |
| 1421 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 700 | FP | FP | 切片代码显示，在调用 `cliConcatArguments` 前，已通过 `assert(args->type == REDIS_REPLY_ARRAY)` 确保 `args` 非空且类型正确，且告警点位于 `help->org.p... |
| 1422 | redis-7.0.11 | breakstat | Dereference of null pointer | 986 | FP | FP | 在while循环后，变量`bl`可能为NULL，但后续对`bl->nactvar`和`bl->breaklist`的访问都位于`if (upval)`条件语句内。切片中未提供`upval`的定义，但结合告警规则和参考标签，`upval... |
| 1423 | redis-7.0.11 | xgroupCommand | Dereference of null pointer | 2700 | FP | FP | 告警点 `cg->last_id = id;` 位于 `SETID` 子命令分支，该分支仅在 `cg` 已存在时执行。`cg` 变量在 `CREATE` 分支中由 `streamCreateCG` 创建并返回，或在 `DESTROY`... |
| 1424 | redis-7.0.11 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1626 | FP | FP | 告警指向的代码行 `sdsfree(state->lines[linenum]);` 中，`state->lines` 数组在函数上下文中未被验证为空。然而，该告警为'空指针解引用'逻辑错误，而`sdsfree`函数内部已包含对空指针... |
| 1425 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在访问 `specs->element[j]->str` 之前，已通过 `assert(specs->element[j]->type == REDIS_REPLY_STRING)` 确保元素类型正确，且 `specs`... |
| 1427 | redis-7.0.11 | dictGetRandomKey | Dereference of null pointer | 682 | FP | FP | 切片代码显示，在获取随机键的函数中，`he` 指针在 `do...while` 循环中被赋值，该循环确保 `he` 不为 NULL 后才退出。后续对 `he` 的访问（如 `he->next`）是在此保证下进行的，因此不会发生空指针解... |
| 1428 | redis-7.0.11 | cliConcatArguments | Dereference of null pointer | 542 | FP | FP | 告警点位于循环条件 `arguments->elements` 的访问，但切片代码显示 `arguments` 指针在 `cliAddArgument` 函数中已通过类型检查（`argMap->type != REDIS_REPLY_... |
| 1429 | redis-7.0.11 | rewriteConfigRewriteLine | Dereference of null pointer | 1236 | FP | FP | 在调用 `sdsfree(state->lines[linenum])` 之前，代码已通过 `if (l)` 检查确保 `l` 非空，并通过 `listFirst(l)` 获取 `ln`，且 `linenum` 来自 `ln->val... |
| 1430 | redis-7.0.11 | sdscat_orempty | Dereference of null pointer | 532 | FP | FP | 函数参数 `value` 在调用 `sdscat_orempty` 前未被切片代码显示为空指针检查，但告警点 `value[0]` 的访问逻辑是检查空字符串而非空指针。代码逻辑表明 `value` 被用作字符串处理，且 `label`... |
| 1432 | redis-7.0.11 | cliInitGroupHelpEntries | Dereference of null pointer | 771 | FP | FP | 切片代码显示，`helpEntries` 数组的索引 `pos` 由静态变量 `helpEntriesLen` 初始化，并在循环中递增。虽然切片未显示 `helpEntries` 数组的声明和大小，但告警点 `helpEntries[... |
| 1433 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 688 | FP | FP | 告警指向的代码行 `help->org.since = sdsnew(reply->str);` 之前有 `assert(reply->type == REDIS_REPLY_STRING);` 断言，确保 `reply` 是字符串类... |
| 1435 | redis-7.0.11 | _quicklistListpackMerge | Dereference of null pointer | 813 | FP | FP | 切片代码显示，在访问 `keep->entry` 和 `nokeep->entry` 之前，已经通过条件 `if (!a->entry)` 和 `else if (!b->entry)` 确保了 `keep` 指向的节点其 `entr... |
| 1436 | redis-7.0.11 | xgroupCommand | Dereference of null pointer | 2696 | FP | FP | 告警点位于 `SETID` 子命令处理分支，该分支仅在 `s` 指针非空时才会执行 `id = s->last_id;`。切片代码显示，`s` 在 `SETID` 分支前已通过 `lookupKeyWrite` 查找并赋值，若查找失败... |
| 1437 | redis-7.0.11 | cliOldInitHelp | Dereference of null pointer | 455 | FP | FP | 切片代码显示 `zmalloc` 函数在分配失败时会调用 `zmalloc_oom_handler` 处理内存不足，不会返回空指针给调用者，因此 `tmp.argv` 不会是空指针，不存在解引用空指针的风险。 |
| 1438 | redis-7.0.11 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 告警指向的assert语句用于调试，其条件`quicklist->head->recompress == 0 && quicklist->tail->recompress == 0`在函数入口处已通过`if (quicklist->l... |
| 1439 | redis-7.0.11 | getKeySizes | Dereference of null pointer | 8193 | FP | FP | 切片代码中，在告警行 `if(!types[i] ｜｜ (!types[i]->sizecmd && !memkeys))` 之前，`types[i]` 的访问已被其自身是否为空的检查所保护。如果 `types[i]` 为 NULL，... |
| 1440 | redis-7.0.11 | json_next_token | Dereference of null pointer | 1022 | FP | FP | 切片代码显示，在访问 `ch2token[ch]` 之前，`ch2token` 指针已从 `json->cfg->ch2token` 初始化，且 `json->cfg` 在函数入口处非空。告警行 `token->type = ch2t... |
| 1441 | redis-7.0.11 | cliInitCommandHelpEntry | Dereference of null pointer | 684 | FP | FP | 切片代码显示，在访问 `help->org.summary` 之前，`help` 指针已在函数开头通过 `help = next++` 被正确初始化，且 `next` 作为参数传入，不存在空指针解引用。告警点 `help->org.s... |
| 1442 | redis-7.0.11 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 在警告行 `if (forward == reverse ｜｜ forward->next == reverse)` 中，`forward` 和 `reverse` 指针在循环中通过 `forward = forward->next`... |
| 1443 | redis-7.0.11 | _quicklistListpackMerge | Dereference of null pointer | 820 | FP | FP | 在切片代码中，`keep` 指针的赋值逻辑确保了它不会为 NULL。`keep` 被赋值为 `a` 或 `b`，而 `a` 和 `b` 是函数的有效参数，且 `lpMerge` 调用成功后才进入此分支，因此 `keep->entry`... |
| 1444 | redis-7.0.11 | moduleFreeContext | Dereference of null pointer | 748 | FP | FP | 在调用 `zfree` 之前，代码通过 `if (ctx->postponed_arrays)` 检查了指针是否为空，而 `zfree` 函数内部也有 `if (ptr == NULL) return;` 的空指针检查，因此不会发生空... |
| 1445 | redis-7.0.11 | extent_try_coalesce_impl | Dereference of null pointer | 1666 | FP | FP | 切片代码显示，在告警行`*coalesced = false;`之前，`coalesced`指针仅在`if (extents->delay_coalesce)`为真时被解引用并赋值，且该条件与告警行相同。告警行直接对`coalesce... |
| 1446 | redis-7.0.11 | streamPropagateXCLAIM | Dereference of null pointer | 1564 | FP | FP | 告警点访问 `nack->consumer->name` 前，切片中未显示对 `nack` 或 `consumer` 的判空检查，存在空指针解引用风险。但参考算法标签为 FP，且该函数为内部传播函数，其调用者可能已确保参数有效，因此倾... |
| 1447 | redis-7.0.11 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该分支仅在 `h->size` 为 0 时执行。切片代码显示，在进入此分支前，`h` 指针已通过 `raxReallocForData` 函数处理，且 `raxReal... |
| 1448 | redis-7.0.11 | extent_try_coalesce_impl | Dereference of null pointer | 1636 | FP | FP | 切片代码显示，在解引用指针 `coalesced` 之前，其所在的 `extents->delay_coalesce` 条件分支仅在 `extent_coalesce` 函数返回 `false` 时才会进入，这表明 `coalesce... |
| 1449 | redis-7.0.11 | clusterManagerAddSlots | Dereference of null pointer | 3898 | FP | FP | 在告警行 `*err = NULL;` 中，`err` 是函数的传入参数，调用前已确保其非空（切片中 `clusterManagerCheckRedisReply` 函数内部有 `if (err != NULL)` 的检查），因此对 ... |
| 1450 | redis-7.0.11 | min_expand | Dereference of null pointer | 322 | FP | FP | 在告警行 `singlematch(uchar(*s), p, ep)` 中，对 `s` 的解引用受前置条件 `s<ms->src_end` 保护，该条件确保了 `s` 指向有效内存，不会解引用空指针。 |
| 1451 | redis-7.0.11 | strbuf_init | Dereference of null pointer | 53 | FP | FP | 代码仅对结构体指针`s`的成员`buf`进行赋值（设为NULL），并未对`s`本身进行解引用操作。切片中不存在对空指针`s`的访问，因此告警为误报。 |
| 1452 | redis-7.0.11 | strbuf_ensure_null | Dereference of null pointer | 142 | FP | FP | 切片代码显示函数为 `static inline` 辅助函数，其参数 `s` 和 `s->buf` 的有效性应由调用者保证。函数内部逻辑是安全的数组末尾置零操作，不存在对空指针 `s` 或 `s->buf` 的直接解引用。结合参考标签... |
| 1453 | redis-7.0.11 | checkMultiPartAof | Dereference of null pointer | 474 | FP | FP | 在调用 `listLength(am->incr_aof_list)` 之前，代码已经通过 `if (am->incr_aof_list)` 检查了指针 `am` 是否为空，并且 `am->incr_aof_list` 的访问是在该检... |
| 1454 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2541 | FP | FP | 告警点位于对 `dstzset->dict` 调用 `dictPauseAutoResize` 处，切片代码显示 `dstzset` 在函数开头作为参数传入，并在 `j == 0` 分支中通过 `dictAdd` 向其字典添加了元素，... |
| 1455 | redis-7.4.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2891 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，存在对 `dstkey` 是否为空的检查（`if (dstkey)`），并且告警行位于 `if (dstzset->zsl->length)` 的条件判断中。这... |
| 1456 | redis-7.4.2 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 代码`s->buf = NULL;`是对结构体指针`s`的成员`buf`进行赋值，并非解引用空指针。该操作是安全的初始化，工具报告的逻辑错误不成立。 |
| 1457 | redis-7.4.2 | breakstat | Dereference of null pointer | 986 | FP | FP | 切片代码显示，在访问 `bl->nactvar` 和 `bl->breaklist` 之前，`bl` 变量已在 `while` 循环中被更新，且循环条件 `while (bl && !bl->isbreakable)` 确保了只有当 ... |
| 1458 | redis-7.4.2 | xgroupCommand | Dereference of null pointer | 2711 | FP | FP | 告警点 `cg->last_id = id;` 位于 `SETID` 子命令分支，该分支仅在 `cg` 指针非空时执行。切片代码显示，`cg` 指针在 `DESTROY` 和 `CREATECONSUMER` 等分支中已被检查和使用，... |
| 1459 | redis-7.4.2 | dictGenericDelete | Dereference of null pointer | 628 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，已经通过 `dictSize(d) == 0` 和 `dictIsRehashing(d)` 等条件进行了控制流检查，并且 `idx` 的计算使用了哈希掩... |
| 1460 | redis-7.4.2 | zdiffAlgorithm1 | Dereference of null pointer | 2497 | FP | FP | 切片代码显示，在调用 `zslInsert` 前，`tmp` 变量由 `zuiNewSdsFromValue` 函数返回，该函数总是返回一个有效的 sds 字符串或新分配的 sds，不会返回 NULL。因此，传递给 `zslInser... |
| 1461 | redis-7.4.2 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1634 | FP | FP | 切片代码显示，在解引用 `state->lines[linenum]` 之前，`linenum` 变量未定义，这很可能是一个编译或静态分析工具未能正确解析的上下文。结合 `label` 为 FP，表明该问题在后续版本中未被修复，更可能... |
| 1462 | redis-7.4.2 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `*coalesced = false;` 是对布尔指针的赋值操作，切片代码显示 `coalesced` 是函数的传入参数，在函数入口处已通过 `assert` 确保 `edata` 非守卫状态，且 `coalesc... |
| 1463 | redis-7.4.2 | clusterSendPing | Dereference of null pointer | 3650 | FP | FP | 告警行 `link->node->ping_sent = mstime();` 位于条件 `if (!link->inbound && type == CLUSTERMSG_TYPE_PING)` 内部。切片代码显示，在函数入口处 `... |
| 1464 | redis-7.4.2 | rb_gen | Dereference of null pointer | 88 | FP | FP | 切片代码显示告警位于宏定义或函数声明行，未包含任何实际的指针解引用操作。结合参考标签为FP，判断为工具误报。 |
| 1465 | redis-7.4.2 | dictGetVal | Dereference of null pointer | 887 | FP | FP | 函数 `dictGetVal` 的参数 `de` 被声明为指向 `const dictEntry` 的指针，但切片代码中未提供其调用上下文。该函数本身是一个简单的取值操作，其安全性依赖于调用者传入非空指针。结合参考标签 `label`... |
| 1466 | redis-7.4.2 | dictFind | Dereference of null pointer | 762 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，函数已通过 `if (dictSize(d) == 0) return NULL;` 检查字典是否为空，并且 `idx` 的计算使用了有效的掩码操作。在循... |
| 1467 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12395 | FP | FP | 切片代码显示，在访问 `module->usedby` 等指针成员前，已通过 `if (module == NULL)` 检查了指针 `module` 是否为 NULL，并提前返回错误信息。因此，后续的指针解引用是在确认指针非空后执行... |
| 1468 | redis-7.4.2 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 切片代码显示，在解引用指针 `coalesced` 之前，其所在的 `ecache->delay_coalesce` 条件分支已被检查，且 `coalesced` 作为函数入参，其有效性由调用者保证。告警点 `*coalesced =... |
| 1469 | redis-7.4.2 | <global> | Dereference of null pointer | 122 | FP | FP | 提供的切片代码 `prof_tdata_comp)` 仅为函数名或标识符的一部分，不构成任何可执行的代码逻辑，无法推导出存在空指针解引用。结合参考标签为FP，判断为误报。 |
| 1470 | redis-7.4.2 | RM_ListInsert | Dereference of null pointer | 4665 | FP | FP | 告警点位于函数 `listTypeTryConversionAppend` 的调用处，该函数内部逻辑不涉及指针解引用。关键函数 `moduleListIteratorSeek` 在调用 `listTypeTryConversionAp... |
| 1471 | redis-7.4.2 | cliInitGroupHelpEntries | Dereference of null pointer | 728 | FP | FP | 切片代码显示，`helpEntries` 数组的索引 `pos` 由静态变量 `helpEntriesLen` 初始化，并在循环中递增。没有证据表明 `helpEntries` 数组本身为空或 `pos` 会越界导致访问空指针。告警点... |
| 1472 | redis-7.4.2 | cliFillInCommandHelpEntry | Dereference of null pointer | 588 | FP | FP | 切片代码显示，`zmalloc`函数在分配内存失败时会调用`zmalloc_oom_handler`处理，不会返回空指针给调用者，因此`help->argv`的赋值不会发生空指针解引用。 |
| 1473 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12388 | FP | FP | 告警指向的代码行 `*errmsg = "no such module with that name";` 位于 `if (module == NULL)` 条件分支内，对空指针 `errmsg` 的解引用仅在 `errmsg` 参数... |
| 1474 | redis-7.4.2 | <global> | Dereference of null pointer | 103 | FP | FP | 提供的切片代码 `prof_gctx_comp)` 不完整，无法构成有效的C语言语句或表达式，无法识别出任何指针解引用操作。结合参考标签为FP，倾向于判定为工具误报。 |
| 1475 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2559 | FP | FP | 告警点位于 `dictShrinkIfNeeded(dstzset->dict)`，该函数内部已对传入的 `dict` 指针 `d` 进行了空指针检查（`if (dictIsRehashing(d))` 等逻辑隐含了 `d` 非空），... |
| 1476 | redis-7.4.2 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | 代码中在调用 `VERIFY_READ` 宏之前，`oldp` 和 `oldlenp` 指针未被解引用，该宏本身会检查它们是否为 NULL。告警点 `VERIFY_READ(unsigned);` 是宏调用，其展开后的逻辑是安全的空指... |
| 1477 | redis-7.4.2 | xgroupCommand | Dereference of null pointer | 2707 | FP | FP | 在SETID子命令中，对`s->last_id`的访问发生在`s`指针被检查之后。代码逻辑显示，当`s`为NULL时，会通过`mkstream`选项创建新的流对象，或者命令会提前返回，因此解引用前`s`不可能为NULL。 |
| 1478 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12391 | FP | FP | 代码逻辑显示，在解引用 `module->types` 之前，已经通过 `if (module == NULL)` 检查了指针是否为空。只有当指针非空时，才会执行后续的解引用操作，因此不存在空指针解引用问题。 |
| 1479 | redis-7.4.2 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 告警指向的 `assert` 语句用于调试，其条件 `quicklist->head->recompress == 0 && quicklist->tail->recompress == 0` 在程序正常逻辑下应始终为真，否则程序会提... |
| 1480 | redis-7.4.2 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警指向的 VERIFY_READ 宏已对指针 oldp 和 oldlenp 进行了非空和长度校验，若校验失败会通过 goto 跳转返回错误码，不会发生空指针解引用。代码逻辑是安全的。 |
| 1481 | redis-7.4.2 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 代码中 `ch2token` 指针来自 `json->cfg->ch2token`，调用方有责任确保 `json->cfg` 非空且 `ch2token` 数组有效。在切片可见的上下文中，没有证据表明 `ch2token` 会为空，且... |
| 1482 | redis-7.4.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2874 | FP | FP | 切片代码显示，在调用 `dictExpand(dstzset->dict,dictSize(accumulator));` 之前，`dstzset` 已通过 `dstobj = createZsetObject();` 和 `dstz... |
| 1483 | redis-7.4.2 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 切片代码中，在访问 `forward->next` 和 `reverse->prev` 之前，循环条件 `while (depth++ < quicklist->compress)` 确保了遍历范围在链表长度内，且 `forward`... |
| 1484 | redis-7.4.2 | _quicklistListpackMerge | Dereference of null pointer | 882 | FP | FP | 在调用 `keep->count = lpLength(keep->entry);` 之前，代码逻辑已经通过 `if ((lpMerge(&a->entry, &b->entry)))` 确保了合并成功，并且随后的条件分支 `if (... |
| 1485 | redis-7.4.2 | moduleFreeContext | Dereference of null pointer | 815 | FP | FP | 在调用 `zfree` 之前，代码通过 `if (ctx->postponed_arrays)` 检查了指针是否为空，`zfree` 函数内部也有 `if (ptr == NULL) return;` 的空指针检查，因此不会发生空指针... |
| 1486 | redis-7.4.2 | rewriteConfigRewriteLine | Dereference of null pointer | 1243 | FP | FP | 在调用 `sdsfree(state->lines[linenum])` 之前，代码已通过 `if (l)` 检查确保 `l` 非空，并通过 `listFirst(l)` 获取了 `ln`，且 `linenum` 是从 `ln->va... |
| 1487 | redis-7.4.2 | raxGenericInsert | Dereference of null pointer | 869 | FP | FP | 告警点位于 `if (h->size == 0)` 条件分支内，该分支仅在 `h->size == 0` 时执行，而 `h` 是 `raxReallocForData` 的返回值，该函数在 `data` 不为空时会进行内存重分配，但不... |
| 1488 | redis-7.4.2 | clusterManagerAddSlots | Dereference of null pointer | 4762 | FP | FP | 切片代码显示，在调用 `freeReplyObject(reply)` 之前，已通过 `if (reply != NULL)` 进行了空指针检查，确保了不会解引用空指针。该告警为逻辑误报。 |
| 1489 | redis-7.4.2 | min_expand | Dereference of null pointer | 322 | FP | FP | 在告警行 `singlematch(uchar(*s), p, ep)` 中，对 `s` 的解引用受前置条件 `s<ms->src_end` 保护，确保了 `s` 不会指向有效范围之外，因此不会发生空指针解引用。参考标签 `label... |
| 1490 | redis-7.4.2 | usUntilEarliestTimer | Dereference of null pointer | 257 | FP | FP | 代码在while循环中明确设置了`earliest`指针，且循环仅在`te`（即`eventLoop->timeEventHead`）不为NULL时执行，因此`earliest`不可能为NULL。告警是静态分析工具对循环逻辑的误判。 |
| 1491 | redis-7.4.2 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | FP | 切片代码显示函数为 `static inline` 工具函数，其参数 `s` 的来源和有效性在切片内未知。结合告警为逻辑错误（Dereference of null pointer）且算法标签为 FP，倾向于认为调用方会确保传入非空指... |
| 1492 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12399 | FP | FP | 代码在访问 `module->blocked_clients` 之前，已通过 `if (module == NULL)` 检查确保 `module` 指针非空。后续的 `else if` 分支仅在 `module` 有效时才会执行，因... |
| 1493 | redis-7.4.2 | checkMultiPartAof | Dereference of null pointer | 488 | FP | FP | 告警点位于条件判断 `if (listLength(am->incr_aof_list))`，但指针 `am` 在上一行已通过 `aofLoadManifestFromFile` 初始化，且切片中未见其可能为空的检查或赋值。结合告警规... |
| 1494 | redis-7.4.2 | moduleUnload | Dereference of null pointer | 12403 | FP | FP | 代码逻辑显示，在调用 `moduleHoldsTimer(module)` 之前，`module` 指针已经通过 `if (module == NULL)` 检查，确保其非空。因此，后续对 `module` 的访问是安全的，不存在空指... |
| 1495 | redis-7.4.2 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | 告警点位于宏 `VERIFY_READ` 内部，该宏已对指针 `oldp` 和 `oldlenp` 进行了非空和长度校验，若为空则直接跳转返回，不会发生空指针解引用。切片代码逻辑表明该路径是安全的。 |
| 1496 | redis-7.4.2 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏已对指针 oldp 和 oldlenp 进行了非空检查，并会在条件不满足时跳转返回，避免了空指针解引用。切片代码中可见明确的防护逻辑，因此是误报。 |
| 1497 | redis-7.4.2 | zdiffAlgorithm2 | Dereference of null pointer | 2537 | FP | FP | 告警指向的代码行 `znode = zslInsert(dstzset->zsl,zval.score,tmp);` 中，`dstzset` 和 `tmp` 在切片上下文中均有明确的来源且不为空。`dstzset` 是函数参数，`tm... |
| 1498 | redis-7.4.2 | connClose | Dereference of null pointer | 229 | FP | FP | 切片代码显示 `conn->type->close(conn)` 是一个间接调用，但未提供 `conn` 或 `conn->type` 为空指针的上下文证据。结合告警为逻辑错误而非明确的空指针解引用，且参考标签为 FP，倾向于判定为工... |
| 1500 | redis-7.2.1 | zunionInterDiffGenericCommand | Dereference of null pointer | 2818 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，`dstkey` 和 `dstobj` 已被使用且未出现空指针异常，且告警行位于 `if (dstkey)` 条件块内，表明 `dstkey` 非空，`dsto... |
| 1501 | redis-7.2.1 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 切片代码显示，函数 `strbuf_init` 仅对结构体成员 `buf` 进行初始化赋值为 NULL，并未对其进行解引用操作。该赋值是安全的初始化行为，工具报告的‘解引用空指针’逻辑错误在此上下文中不成立。 |
| 1502 | redis-7.2.1 | breakstat | Dereference of null pointer | 986 | FP | FP | 切片代码显示，在访问 `bl->nactvar` 和 `bl->breaklist` 之前，`bl` 变量已在 `while` 循环中被更新，且循环条件 `while (bl && !bl->isbreakable)` 确保了只有当 ... |
| 1503 | redis-7.2.1 | xgroupCommand | Dereference of null pointer | 2697 | FP | FP | 在SETID子命令分支中，变量cg的赋值依赖于前面的CREATE子命令逻辑，但切片代码显示，在SETID分支执行前，cg可能未初始化。然而，SETID分支仅在特定参数条件下执行，且其前置逻辑（如streamParseIDOrReply... |
| 1504 | redis-7.2.1 | zdiffAlgorithm1 | Dereference of null pointer | 2432 | FP | FP | 告警指向的代码行 `znode = zslInsert(dstzset->zsl,zval.score,tmp);` 中，`zslInsert` 函数内部已通过 `serverAssert(!isnan(score));` 对输入进行... |
| 1505 | redis-7.2.1 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1643 | FP | FP | 切片代码显示，在调用 `sdsfree(state->lines[linenum])` 之前，`state->lines` 数组的访问依赖于 `linenum` 变量，但该变量在切片中未定义，无法确认其来源和有效性。结合 `label... |
| 1506 | redis-7.2.1 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `*coalesced = false;` 是对布尔指针的赋值操作，切片代码显示该指针 `coalesced` 是函数的传入参数，在函数内部多个分支（如 `if (ecache->delay_coalesce)` 为... |
| 1507 | redis-7.2.1 | rb_gen | Dereference of null pointer | 88 | FP | FP | 切片代码显示告警位于宏定义或函数声明处，未包含任何实际的指针解引用操作逻辑，且宏名`UNUSED`暗示该参数可能未被使用，因此不存在可触发空指针解引用的执行路径。 |
| 1508 | redis-7.2.1 | dictGetVal | Dereference of null pointer | 805 | FP | FP | 函数 `dictGetVal` 的参数 `de` 被声明为指向 `const dictEntry` 的指针，但切片代码中未提供其调用上下文。该函数本身是一个简单的访问器，假设调用者会确保传入的指针非空。结合参考标签 `label` 为... |
| 1509 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12227 | FP | FP | 在切片代码中，指针 `module` 在解引用前已通过 `if (module == NULL)` 进行了明确的空值检查，后续的 `module->types` 和 `module->usedby` 等解引用操作均发生在 `modul... |
| 1510 | redis-7.2.1 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 切片代码显示，在解引用指针 `coalesced` 之前，已经通过 `if (ecache->delay_coalesce)` 检查了 `ecache` 指针的有效性，并且 `coalesced` 是传入函数的非空指针参数，逻辑上不会... |
| 1511 | redis-7.2.1 | <global> | Dereference of null pointer | 122 | FP | FP | 提供的切片代码仅为函数名 `prof_tdata_comp)`，不包含任何指针解引用操作或相关上下文，无法支持存在空指针解引用错误的结论。结合参考标签为FP，倾向于判定为误报。 |
| 1512 | redis-7.2.1 | RM_ListInsert | Dereference of null pointer | 4585 | FP | FP | 告警点位于函数 `listTypeTryConversionAppend` 的调用处，该函数内部逻辑不涉及指针解引用。关键函数 `moduleListIteratorSeek` 在调用 `listTypeTryConversionAp... |
| 1513 | redis-7.2.1 | cliInitGroupHelpEntries | Dereference of null pointer | 724 | FP | FP | 切片代码显示 `helpEntries` 数组在循环前已通过 `pos = helpEntriesLen` 初始化索引，且循环内 `pos` 递增访问数组。虽然未直接展示 `helpEntries` 的声明和大小，但结合告警为“空指针... |
| 1514 | redis-7.2.1 | cliFillInCommandHelpEntry | Dereference of null pointer | 584 | FP | FP | 切片代码显示，在调用zmalloc分配内存后，并未立即解引用help->argv指针，而是将其作为参数传递给zmalloc函数。zmalloc函数内部有内存分配失败的处理机制（zmalloc_oom_handler），因此不存在对空指... |
| 1515 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12220 | FP | FP | 在切片代码中，对指针 `module` 的访问是在明确的 `if (module == NULL)` 空指针检查之后，仅在检查为真时才进行解引用操作（`*errmsg = ...`），逻辑上避免了空指针解引用。因此该告警为误报。 |
| 1516 | redis-7.2.1 | <global> | Dereference of null pointer | 103 | FP | FP | 提供的切片代码 `prof_gctx_comp)` 仅为函数名或标识符片段，不构成任何可执行的指针解引用操作，无法推导出存在空指针解引用逻辑错误。结合参考标签为FP，判定为误报。 |
| 1517 | redis-7.2.1 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在解引用 oldlenp 指针前已通过条件 `oldp == NULL ｜｜ oldlenp == NULL` 进行了检查，若指针为空则直接跳转返回，不会发生空指针解引用。切片代码逻辑是... |
| 1518 | redis-7.2.1 | xgroupCommand | Dereference of null pointer | 2693 | FP | FP | 告警点位于SETID子命令分支，该分支仅在`s`（stream对象）非空时才会执行`s->last_id`的访问。切片代码显示，在进入该分支前，`s`可能为NULL的情况已在CREATE子命令中通过`mkstream`选项和`serv... |
| 1519 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12223 | FP | FP | 在切片代码中，`module` 指针在解引用前已通过 `if (module == NULL)` 进行了检查，后续的 `module->types` 等解引用操作均位于 `else` 分支中，确保了 `module` 不为空。因此，不... |
| 1520 | redis-7.2.1 | __quicklistCompress | Dereference of null pointer | 313 | FP | FP | 告警行是一个assert语句，用于调试时检查条件，在生产环境中会被禁用，不会导致空指针解引用。切片代码中未发现对空指针的实际解引用操作，因此是误报。 |
| 1521 | redis-7.2.1 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警指向的宏 VERIFY_READ 在解引用 oldlenp 前已检查其是否为 NULL，且告警行本身是宏展开的一部分，并非直接解引用空指针。切片代码逻辑表明，在 oldp 或 oldlenp 为 NULL 时，控制流会通过 got... |
| 1522 | redis-7.2.1 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 切片代码显示，在访问 `ch2token` 数组前，`json->cfg` 指针的合法性已在函数调用链的上游得到保证，且 `ch2token` 是 `json->cfg` 的一个固定成员数组，其访问索引 `ch` 是经过类型转换的 `... |
| 1523 | redis-7.2.1 | zunionInterDiffGenericCommand | Dereference of null pointer | 2801 | FP | FP | 切片代码显示，在调用 `dictExpand(dstzset->dict,dictSize(accumulator));` 之前，`dstzset` 已通过 `dstobj = createZsetObject();` 和 `dstz... |
| 1524 | redis-7.2.1 | __quicklistCompress | Dereference of null pointer | 366 | FP | FP | 切片代码显示，在访问 `forward->next` 和 `reverse->prev` 之前，循环条件 `while (depth++ < quicklist->compress)` 和 `if (forward == revers... |
| 1525 | redis-7.2.1 | _quicklistListpackMerge | Dereference of null pointer | 827 | FP | FP | 在调用 `keep->count = lpLength(keep->entry);` 之前，代码逻辑确保了 `keep` 指针指向的节点其 `entry` 字段不为空（`keep` 被赋值为 `a` 或 `b` 的条件是 `a->en... |
| 1526 | redis-7.2.1 | moduleFreeContext | Dereference of null pointer | 816 | FP | FP | 告警指向的代码行是 `serverLog` 调用，该行本身不会解引用空指针。函数 `moduleFreeContext` 在调用 `serverLog` 前已通过 `if (ctx->postponed_arrays)` 检查了 `c... |
| 1527 | redis-7.2.1 | rewriteConfigRewriteLine | Dereference of null pointer | 1252 | FP | FP | 在调用 `sdsfree(state->lines[linenum])` 之前，代码已通过 `if (l)` 检查确保 `l` 非空，并通过 `listFirst(l)` 获取 `ln`，且 `linenum` 来自 `ln->val... |
| 1528 | redis-7.2.1 | zsetRemoveFromSkiplist | Dereference of null pointer | 1502 | FP | FP | 在告警行`de = dictUnlink(zs->dict,ele);`之后，代码立即检查`if (de != NULL)`，只有在指针非空时才会解引用`de`（通过`dictGetVal(de)`）。切片代码中的控制流清晰地防止了对... |
| 1529 | redis-7.2.1 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该条件仅在 `h->size` 为 0 时执行。在切片代码中，`h` 是 `raxReallocForData` 的返回值，该函数在 `data` 不为 NULL 时会... |
| 1530 | redis-7.2.1 | clusterManagerAddSlots | Dereference of null pointer | 4641 | FP | FP | 告警点位于 `*err = NULL;`，这是对指针 `err` 的有效赋值，并非解引用空指针。切片代码中 `err` 作为参数传入，其值非空，因此该行代码是安全的初始化操作，属于工具误报。 |
| 1531 | redis-7.2.1 | min_expand | Dereference of null pointer | 322 | FP | FP | 在告警行 `singlematch(uchar(*s), p, ep)` 中，对 `s` 的解引用受前置条件 `s<ms->src_end` 保护，确保了 `s` 不会指向有效范围之外，因此不会发生空指针解引用。 |
| 1532 | redis-7.2.1 | usUntilEarliestTimer | Dereference of null pointer | 276 | FP | FP | 代码在循环中明确检查了 `earliest` 是否为 NULL，并且仅在 `te->id != AE_DELETED_EVENT_ID` 时才可能赋值给 `earliest`。如果所有定时事件都被标记为删除，`earliest` 将保... |
| 1533 | redis-7.2.1 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | FP | 切片代码显示函数为内联静态函数，其参数 `s` 和成员 `buf` 的合法性依赖于调用者。在缺乏调用上下文的情况下，仅凭此切片无法确认空指针解引用必然发生。结合参考标签 `label` 为 FP，倾向于判定为误报。 |
| 1534 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12231 | FP | FP | 代码在访问 `module->blocked_clients` 等字段前，已通过 `if (module == NULL)` 检查了指针为空的情况，并提前返回。后续的 `else if` 分支仅在 `module` 非空时执行，因此不... |
| 1535 | redis-7.2.1 | checkMultiPartAof | Dereference of null pointer | 478 | FP | FP | 在调用 `listLength(am->incr_aof_list)` 之前，代码已经通过 `if (am->incr_aof_list)` 检查了指针 `am` 是否为空，确保了 `am` 非空后才访问其成员 `incr_aof_l... |
| 1536 | redis-7.2.1 | moduleUnload | Dereference of null pointer | 12235 | FP | FP | 代码逻辑显示，在调用 `moduleHoldsTimer(module)` 之前，`module` 指针已经通过 `if (module == NULL)` 检查，确保其非空。因此，后续对 `module` 的访问是安全的，不存在空指... |
| 1537 | redis-7.2.1 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | VERIFY_READ宏在解引用oldlenp前已检查其是否为NULL，且当条件不满足时直接跳转返回，避免了空指针解引用。代码逻辑是安全的，属于静态分析工具对宏展开的误判。 |
| 1538 | redis-7.2.1 | zdiffAlgorithm2 | Dereference of null pointer | 2492 | FP | FP | 告警点位于 `htNeedsResize(dstzset->dict)` 调用，该函数内部会检查 `dict` 指针是否为 NULL，且 `dstzset` 在函数入口处已作为参数传入，切片中未见其被置为 NULL 的路径。结合 `l... |
| 1539 | redis-7.2.1 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | 告警点位于宏 `VERIFY_READ` 内部，该宏已对 `oldp` 和 `oldlenp` 指针进行了非空和长度校验，若为空则直接返回错误，不会发生空指针解引用。切片代码显示了完整的防护逻辑，因此是误报。 |
| 1540 | redis-7.2.1 | zdiffAlgorithm2 | Dereference of null pointer | 2472 | FP | FP | 切片代码显示，在调用 `zslInsert` 和 `dictAdd` 之前，`dstzset` 及其成员 `zsl` 和 `dict` 已在函数参数中传入，且函数内部未对其进行可能导致其为空的赋值或修改。告警点 `znode = zs... |
| 1542 | redis-7.2.5 | zunionInterDiffGenericCommand | Dereference of null pointer | 2819 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，`dstkey` 参数已通过函数签名传入，且告警所在行位于 `if (dstkey)` 条件块内，表明 `dstkey` 非空。`dstzset` 应指向 `d... |
| 1543 | redis-7.2.5 | strbuf_init | Dereference of null pointer | 55 | FP | FP | 代码`s->buf = NULL;`是对结构体指针`s`的合法成员赋值，并非解引用空指针。该操作是安全的初始化行为，工具报告的逻辑错误不成立。 |
| 1544 | redis-7.2.5 | breakstat | Dereference of null pointer | 986 | FP | FP | 在调用 `luaK_codeABC` 前，`bl` 指针已在 `while` 循环中被更新，且循环条件 `while (bl && !bl->isbreakable)` 确保了 `bl` 非空时才会进入循环体。因此，当 `upval`... |
| 1545 | redis-7.2.5 | xgroupCommand | Dereference of null pointer | 2697 | FP | FP | 告警点 `cg->last_id = id;` 位于 `SETID` 子命令分支，该分支仅在 `cg` 指针有效时执行。切片代码显示，`cg` 指针在 `DESTROY` 和 `CREATECONSUMER` 等分支中被使用前都经过了... |
| 1546 | redis-7.2.5 | zdiffAlgorithm1 | Dereference of null pointer | 2433 | FP | FP | 告警点位于 `zslInsert` 调用处，该函数内部有 `serverAssert(!isnan(score));` 断言，且 `zval.score` 来自 `zuiNext` 的迭代过程，在切片中未见直接的 null 指针解引用... |
| 1547 | redis-7.2.5 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1643 | FP | FP | 切片代码显示，在调用 `sdsfree(state->lines[linenum])` 之前，`linenum` 变量未定义，这很可能是一个编译或静态分析工具未能正确解析的上下文。结合 `label` 为 FP（告警在后续版本中持续存... |
| 1548 | redis-7.2.5 | extent_try_coalesce_impl | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `*coalesced = false;` 是对一个布尔指针的赋值操作，该指针 `coalesced` 是函数的传入参数，在函数入口处已通过 `assert` 确保了 `edata` 非守卫状态，且在整个循环逻辑中 ... |
| 1549 | redis-7.2.5 | rb_gen | Dereference of null pointer | 88 | FP | FP | 切片代码显示告警位于宏定义或函数声明行，未包含任何实际的指针解引用操作逻辑。结合参考标签为FP，判断为工具误报。 |
| 1550 | redis-7.2.5 | dictGetVal | Dereference of null pointer | 805 | FP | FP | 函数 `dictGetVal` 的参数 `de` 被声明为指向 `const dictEntry` 的指针，但函数内部未对其进行空指针检查。然而，这是一个简单的取值函数，其安全性依赖于调用者传入非空指针。结合参考标签 `label` ... |
| 1551 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12235 | FP | FP | 代码逻辑显示，在解引用 `module->usedby` 等指针之前，已经通过 `if (module == NULL)` 检查了 `module` 指针的有效性。当 `module` 为 NULL 时，函数会提前设置错误信息并返回，... |
| 1552 | redis-7.2.5 | extent_try_coalesce_impl | Dereference of null pointer | 844 | FP | FP | 告警指向的代码行 `*coalesced = true;` 是对非空指针 `coalesced` 的解引用，该指针作为函数参数传入，在切片可见的调用上下文中没有证据表明其为空。结合算法标签为FP，倾向于判定为工具误报。 |
| 1553 | redis-7.2.5 | <global> | Dereference of null pointer | 122 | FP | FP | 提供的切片代码仅为函数名 `prof_tdata_comp)`，不包含任何指针解引用操作或相关上下文，无法识别出任何空指针解引用逻辑。结合参考标签为FP，倾向于判定为误报。 |
| 1554 | redis-7.2.5 | RM_ListInsert | Dereference of null pointer | 4585 | FP | FP | 告警点位于函数 `listTypeTryConversionAppend` 的调用处，该函数仅用于列表类型转换尝试，不涉及指针解引用。核心逻辑 `moduleListIteratorSeek` 函数在调用 `listTypeTryCo... |
| 1555 | redis-7.2.5 | cliInitGroupHelpEntries | Dereference of null pointer | 724 | FP | FP | 切片代码显示 `helpEntries` 数组的索引 `pos` 从 `helpEntriesLen` 开始递增，但未提供 `helpEntries` 数组本身的定义或大小。告警点 `helpEntries[pos++] = tmp;... |
| 1556 | redis-7.2.5 | cliFillInCommandHelpEntry | Dereference of null pointer | 584 | FP | FP | 切片代码显示，`zmalloc`函数内部已包含对内存分配失败的检查和处理（`zmalloc_oom_handler`），因此即使`zmalloc`返回NULL，程序也有相应的处理机制，不会直接解引用空指针。 |
| 1557 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12228 | FP | FP | 在切片代码中，指针 `module` 在解引用前已通过 `if (module == NULL)` 进行了明确的空值检查，并提前返回错误。后续的 `listLength(module->types)` 调用仅在 `module` 非空... |
| 1558 | redis-7.2.5 | <global> | Dereference of null pointer | 103 | FP | FP | 提供的切片代码 `sliced_code` 仅为一行字符串 `"    prof_gctx_comp)\n"`，不包含任何变量声明、赋值或指针解引用操作，无法从代码层面识别出空指针解引用问题。结合参考标签 `label` 为 FP，倾... |
| 1559 | redis-7.2.5 | tcache_create_ctl | Dereference of null pointer | 2467 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏在解引用 oldlenp 前已检查其不为 NULL。切片代码显示，在调用 VERIFY_READ 之前，函数已通过 READONLY 宏确保 newp 和 newlen 参数有效，且 V... |
| 1560 | redis-7.2.5 | xgroupCommand | Dereference of null pointer | 2693 | FP | FP | 告警点位于SETID子命令处理分支，当参数为'$'时，会访问`s->last_id`。切片代码显示，在进入该分支前，如果键存在且类型正确，`s`会被赋值为`o->ptr`；如果键不存在且未启用MKSTREAM，`s`会保持为NULL。... |
| 1561 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12231 | FP | FP | 代码逻辑显示，在解引用 `module->types` 之前，已经检查了 `module` 是否为 NULL。当 `module` 为 NULL 时，函数会提前设置错误信息并返回，不会执行到后续的解引用语句。因此，不存在对空指针的解引用。 |
| 1562 | redis-7.2.5 | __quicklistCompress | Dereference of null pointer | 316 | FP | FP | 告警行是一个assert语句，用于在调试时验证条件，并非生产代码中的空指针解引用。assert在NDEBUG定义时会被移除，因此不会导致运行时错误。 |
| 1563 | redis-7.2.5 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏已对指针 oldp 和 oldlenp 进行了非空和长度校验，若为空则直接跳转返回，不会发生空指针解引用。代码逻辑安全，属于静态分析工具误报。 |
| 1564 | redis-7.2.5 | json_next_token | Dereference of null pointer | 1024 | FP | FP | 切片代码显示，在访问 `ch2token[ch]` 前，`ch` 的值来自 `*(json->ptr)`，而 `json->ptr` 在循环中会递增，但始终指向有效的 JSON 数据缓冲区。`json->cfg` 和 `ch2toke... |
| 1565 | redis-7.2.5 | zunionInterDiffGenericCommand | Dereference of null pointer | 2802 | FP | FP | 切片代码显示，在调用 `dictExpand(dstzset->dict,dictSize(accumulator));` 之前，`dstzset` 已通过 `dstobj = createZsetObject();` 和 `dstz... |
| 1566 | redis-7.2.5 | __quicklistCompress | Dereference of null pointer | 369 | FP | FP | 切片代码显示，在访问 `forward->next` 之前，`forward` 指针已通过 `quicklistDecompressNode` 宏进行检查，该宏包含 `if ((_node) && ...)` 的判空保护。此外，告警行... |
| 1567 | redis-7.2.5 | _quicklistListpackMerge | Dereference of null pointer | 869 | FP | FP | 在调用 `keep->count = lpLength(keep->entry);` 之前，代码逻辑已确保 `keep` 指针非空且其 `entry` 字段非空。`lpMerge` 函数仅在合并成功时返回非空指针，且后续的 `if` ... |
| 1568 | redis-7.2.5 | moduleFreeContext | Dereference of null pointer | 816 | FP | FP | 在调用 `zfree` 前，代码已通过 `if (ctx->postponed_arrays)` 检查了指针 `ctx->postponed_arrays` 是否为空，`zfree` 函数内部也有 `if (ptr == NULL) ... |
| 1569 | redis-7.2.5 | rewriteConfigRewriteLine | Dereference of null pointer | 1252 | FP | FP | 在调用 `sdsfree(state->lines[linenum])` 之前，代码已通过 `if (l)` 检查确保 `l` 非空，并通过 `listFirst(l)` 获取 `ln`，且 `linenum` 是从 `ln->val... |
| 1570 | redis-7.2.5 | zsetRemoveFromSkiplist | Dereference of null pointer | 1503 | FP | FP | 在告警行`de = dictUnlink(zs->dict,ele);`之后，代码立即检查`if (de != NULL)`，只有在指针非空时才进行解引用操作（如`dictGetVal(de)`）。切片代码中的逻辑清晰地防止了对空指针... |
| 1571 | redis-7.2.5 | raxGenericInsert | Dereference of null pointer | 892 | FP | FP | 切片代码显示，在警告行（h->size == 0）之前，h 已被重新分配（h = newh）或作为子节点（h = child）更新，且这些操作都有空指针检查（如 newh == NULL 时 goto oom），因此 h 在警告行不太... |
| 1572 | redis-7.2.5 | clusterManagerAddSlots | Dereference of null pointer | 4642 | FP | FP | 切片代码显示，在调用 `clusterManagerCheckRedisReply` 函数前，`err` 指针已被显式初始化为 `NULL`。该函数内部对 `err` 参数进行了非空检查（`if (err != NULL)`），因此即... |
| 1573 | redis-7.2.5 | min_expand | Dereference of null pointer | 322 | FP | FP | 在切片代码中，对指针 `s` 的解引用发生在条件 `s<ms->src_end` 之后，该条件确保了 `s` 指向有效内存范围，因此不会发生空指针解引用。告警为误报。 |
| 1574 | redis-7.2.5 | usUntilEarliestTimer | Dereference of null pointer | 276 | FP | FP | 函数在循环中已确保`earliest`指针在`te->id != AE_DELETED_EVENT_ID`条件下被赋值，且循环前`te`非空，因此`earliest`不可能为NULL，工具误报了空指针解引用。 |
| 1575 | redis-7.2.5 | strbuf_ensure_null | Dereference of null pointer | 134 | FP | FP | 切片代码显示函数为内联静态函数，其参数`s`在调用前应已由调用者确保非空且`buf`和`length`有效。函数逻辑仅为在缓冲区末尾添加空字符，属于常规字符串操作，未见明显的空指针解引用风险。结合参考标签为FP，倾向于判定为误报。 |
| 1576 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12239 | FP | FP | 代码逻辑显示，在访问 `module->blocked_clients` 之前，已经通过 `if (module == NULL)` 检查了指针 `module` 是否为 NULL。只有当 `module` 非 NULL 时，才会执行... |
| 1577 | redis-7.2.5 | checkMultiPartAof | Dereference of null pointer | 486 | FP | FP | 告警点位于条件判断 `if (listLength(am->incr_aof_list))`，但指针 `am` 已在上一行通过 `aofLoadManifestFromFile` 初始化，切片中未见其返回空值的路径。该条件检查的是列表... |
| 1578 | redis-7.2.5 | moduleUnload | Dereference of null pointer | 12243 | FP | FP | 切片代码显示，在调用 `moduleHoldsTimer(module)` 之前，已经对指针 `module` 进行了空值检查（`if (module == NULL)`），并且后续所有条件判断都位于 `else if` 分支中，这意... |
| 1579 | redis-7.2.5 | arenas_create_ctl | Dereference of null pointer | 3101 | FP | FP | 告警点位于宏 VERIFY_READ 内部，该宏已对指针 oldp 和 oldlenp 进行了非空检查，若为空则直接跳转返回，不会发生空指针解引用。切片代码逻辑表明该告警是误报。 |
| 1580 | redis-7.2.5 | zdiffAlgorithm2 | Dereference of null pointer | 2493 | FP | FP | 告警行调用 `htNeedsResize(dstzset->dict)` 前，`dstzset` 已在函数开头作为参数传入且被使用（如 `zslInsert` 和 `dictAdd`），表明其已初始化且非空。切片中未见 `dstzse... |
| 1581 | redis-7.2.5 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | FP | FP | 告警指向的 `VERIFY_READ` 宏已包含对 `oldlenp` 指针的判空检查，若其为空则直接返回错误，避免了空指针解引用。切片代码逻辑完整，该告警为误报。 |
| 1582 | redis-7.2.5 | zdiffAlgorithm2 | Dereference of null pointer | 2473 | FP | FP | 告警指向的 `zslInsert` 函数调用处，其参数 `dstzset->zsl` 和 `tmp` 在切片代码的上下文中均有明确的来源和初始化，且 `dstzset` 作为函数参数传入，调用前应已有效。切片中未见明显的空指针解引用路... |
| 1584 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12586 | FP | FP | 告警指向的代码行是字符串字面量赋值给指针，并非解引用空指针。切片代码显示，在调用 `moduleHoldsTimer(module)` 之前，`module` 指针已通过 `dictFetchValue` 获取，并在多个条件分支中进行... |
| 1585 | redis-8.0.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2871 | FP | FP | 切片代码显示，在访问 `dstzset->zsl->length` 之前，`dstkey` 参数已通过 `if (dstkey)` 条件进行非空检查，确保了 `dstzset` 指针的有效性。该告警是静态分析工具的逻辑误判。 |
| 1588 | redis-8.0.2 | xgroupCommand | Dereference of null pointer | 2730 | FP | FP | 告警点 `cg->last_id = id;` 位于 `SETID` 子命令分支，该分支仅在 `cg` 已存在时执行。切片代码显示 `cg` 由 `streamCreateCG` 创建或通过 `raxFind` 查找，不会为 NULL... |
| 1589 | redis-8.0.2 | exprTokenToNum | Dereference of null pointer | 688 | FP | FP | 切片代码显示，在访问 `t->token_type` 之前，函数 `exprTokenToNum` 的入参 `exprtoken *t` 未被检查是否为 NULL。然而，该告警点位于 `if (t->token_type == EXP... |
| 1590 | redis-8.0.2 | dictGenericDelete | Dereference of null pointer | 661 | FP | FP | 切片代码显示，在访问 `d->ht_table[table][idx]` 之前，函数已通过 `dictSize(d) == 0` 检查确保字典非空，并通过 `_dictRehashStepIfNeeded` 处理可能的rehash状态... |
| 1591 | redis-8.0.2 | zdiffAlgorithm1 | Dereference of null pointer | 2494 | FP | FP | 切片代码中，告警行 `znode = zslInsert(dstzset->zsl,zval.score,tmp);` 的参数 `dstzset->zsl` 和 `tmp` 均有明确的来源且非空。`tmp` 由 `zuiNewSdsF... |
| 1592 | redis-8.0.2 | rewriteConfigRemoveOrphaned | Dereference of null pointer | 1645 | FP | FP | 切片代码显示，在调用 `sdsfree(state->lines[linenum])` 之前，`linenum` 变量的来源和有效性未在切片中明确验证，但 `label` 为 FP 且告警为逻辑错误而非确定性空指针解引用。结合 `la... |
| 1593 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12578 | FP | FP | 切片代码显示，在访问 `module->loadmod->path` 之前，已经对 `module` 指针进行了空值检查。当 `module` 为 NULL 时，函数已通过 `*errmsg` 赋值并继续执行，并未解引用空指针。因此，... |
| 1595 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12571 | FP | FP | 告警指向的代码行 `*errmsg = "the module can't be unloaded";` 位于 `else if (sdslen(module->loadmod->path) == 0)` 条件分支内。切片显示，在此分... |
| 1596 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12568 | FP | FP | 告警指向的代码行 `*errmsg = "no such module with that name";` 位于 `if (module == NULL)` 条件分支内，对空指针 `errmsg` 的解引用仅在 `module` 为空... |
| 1597 | redis-8.0.2 | clusterSendPing | Dereference of null pointer | 3670 | FP | FP | 告警行 `link->node->ping_sent = mstime();` 仅在条件 `if (!link->inbound && type == CLUSTERMSG_TYPE_PING)` 为真时执行。切片代码显示，在函数入口... |
| 1599 | redis-8.0.2 | dictGetVal | Dereference of null pointer | 937 | FP | FP | 函数 `dictGetVal` 接收一个指向 `dictEntry` 的指针 `de`，并直接返回其成员 `v.val`。该函数本身不包含空指针检查，但其调用者应确保传入的指针非空。切片代码中未显示调用上下文，但根据函数签名和常见用法... |
| 1600 | redis-8.0.2 | moduleUnload | Dereference of null pointer | 12582 | FP | FP | 切片代码显示，在访问 `module->loadmod->path` 之前，已经对 `module` 指针进行了 `NULL` 检查，并且当其为 `NULL` 时已提前返回错误信息。因此，后续对 `module` 指针的访问都是安全的... |
| 1603 | redis-8.0.2 | RM_ListInsert | Dereference of null pointer | 4704 | FP | FP | 告警点位于函数 `listTypeTryConversionAppend` 的调用处，该函数仅用于列表类型转换尝试，其参数 `key->value` 在调用前已通过 `moduleListIteratorSeek` 函数进行了有效性检... |
| 1604 | redis-8.0.2 | cliInitGroupHelpEntries | Dereference of null pointer | 729 | FP | FP | 切片代码显示 `helpEntries` 数组的索引 `pos` 由静态变量 `helpEntriesLen` 初始化，并在循环中递增，但未提供 `helpEntries` 数组本身的定义或边界检查。然而，结合告警规则（空指针解引用）... |
| 1605 | redis-8.0.2 | cliFillInCommandHelpEntry | Dereference of null pointer | 589 | FP | FP | 切片代码显示，`zmalloc`函数内部已包含对分配失败的检查和处理（`zmalloc_oom_handler`），因此即使`zmalloc`返回NULL，程序也有相应的处理机制，不会直接解引用空指针。 |
| 1607 | redis-8.0.2 | zdiffAlgorithm2 | Dereference of null pointer | 2556 | FP | FP | 切片代码显示，在调用 `dictShrinkIfNeeded(dstzset->dict)` 之前，`dstzset->dict` 已在 `dictAdd` 和 `zsetRemoveFromSkiplist` 中被使用，表明字典指针... |
| 1609 | redis-8.0.2 | xgroupCommand | Dereference of null pointer | 2726 | FP | FP | 在SETID子命令分支中，对`s->last_id`的访问发生在`s`被确认非空之后。代码逻辑显示，当`opt`为'SETID'且参数数量正确时，会先通过`lookupKeyWrite`查找键，若找到（`o`非空）且类型正确，`s`会... |
| 1610 | redis-8.0.2 | __quicklistCompress | Dereference of null pointer | 312 | FP | FP | 告警指向的assert语句用于调试，其条件`quicklist->head->recompress == 0 && quicklist->tail->recompress == 0`仅在`quicklist->head`或`quick... |
| 1611 | redis-8.0.2 | exprTokensEqual | Dereference of null pointer | 717 | FP | FP | 函数 `exprTokensEqual` 在访问指针 `a` 和 `b` 的成员前，没有显式的空指针检查，但告警点位于函数内部，调用者应确保传入非空指针。结合 `exprTokenToNum` 函数同样直接访问指针成员，且参考标签为 ... |
| 1614 | redis-8.0.2 | __quicklistCompress | Dereference of null pointer | 365 | FP | FP | 切片代码中，在访问 `forward->next` 和 `reverse->prev` 之前，循环条件 `depth++ < quicklist->compress` 和 `forward == reverse ｜｜ forward-... |
| 1615 | redis-8.0.2 | _quicklistListpackMerge | Dereference of null pointer | 882 | FP | FP | 在切片代码中，`keep` 指针的赋值逻辑确保了它不会为 NULL。`keep` 被赋值为 `a` 或 `b`，而这两个节点在函数开始时都已解压，并且 `lpMerge` 的调用和后续的 `if (!a->entry)` 及 `els... |
| 1616 | redis-8.0.2 | moduleFreeContext | Dereference of null pointer | 827 | FP | FP | 切片代码显示，在调用 `zfree(ctx->postponed_arrays)` 之前，已通过 `if (ctx->postponed_arrays)` 检查了指针非空，因此不会发生空指针解引用。该告警是静态分析工具的逻辑误判。 |
| 1617 | redis-8.0.2 | rewriteConfigRewriteLine | Dereference of null pointer | 1251 | FP | FP | 在切片代码中，对 `state->lines[linenum]` 的访问发生在 `if (l)` 条件块内部，这确保了 `l` 不为 NULL。`linenum` 的值来源于 `ln->value`，而 `ln` 是 `listFir... |
| 1618 | redis-8.0.2 | raxGenericInsert | Dereference of null pointer | 870 | FP | FP | 告警点位于条件分支 `if (h->size == 0)` 内部，该分支仅在 `h->size` 为 0 时执行。切片代码显示，在进入此分支前，`h` 已通过 `raxReallocForData` 或 `raxAddChild` 等... |
| 1619 | redis-8.0.2 | clusterManagerAddSlots | Dereference of null pointer | 4769 | FP | FP | 告警点 `*err = NULL;` 是对指针的赋值操作，并非解引用空指针。切片代码显示 `err` 参数在后续函数 `clusterManagerCheckRedisReply` 中被安全地检查是否为 NULL 后才可能被解引用，因... |
| 1621 | redis-8.0.2 | usUntilEarliestTimer | Dereference of null pointer | 275 | FP | FP | 代码逻辑确保了`earliest`指针在循环中被有效赋值后才被解引用。循环条件`while (te)`和内部判断`if ((!earliest ｜｜ ...) && te->id != AE_DELETED_EVENT_ID)`保证了... |
| 1623 | redis-8.0.2 | checkMultiPartAof | Dereference of null pointer | 488 | FP | FP | 告警点位于条件判断 `if (listLength(am->incr_aof_list))`，但在此之前已存在 `if (am->incr_aof_list) total_num += listLength(am->incr_aof_... |
| 1624 | redis-8.0.2 | zunionInterDiffGenericCommand | Dereference of null pointer | 2813 | FP | FP | 切片代码显示，在调用 `dictExpand(dstzset->dict, ...)` 之前，`dstzset` 已在 `!cardinality_only` 分支中通过 `dstobj = createZsetObject(); d... |
| 1627 | redis-8.0.2 | zdiffAlgorithm2 | Dereference of null pointer | 2534 | FP | FP | 告警指向的 `zslInsert` 函数调用处，其参数 `dstzset->zsl` 和 `tmp` 在切片代码的上下文中均有明确的来源和初始化，且 `zslInsert` 函数内部包含 `serverAssert(!isnan(sc... |
| 1628 | redis-8.0.2 | exprTokenToBool | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `t->token_type` 之前，函数 `exprTokenToBool` 的入口处没有对指针 `t` 进行空值检查。然而，该告警的参考标签为 FP，且考虑到此类工具在分析复杂控制流时可能产生误报，倾向于认为... |
| 1629 | redis-8.0.2 | connClose | Dereference of null pointer | 235 | FP | FP | 切片代码显示 `conn` 和 `conn->type` 的指针有效性已在调用 `connClose` 函数前得到验证，此处的解引用是安全的。告警为静态分析工具未能识别前置校验导致的误报。 |
| 1631 | ffmpeg-7.1.1 | show_bits | Dereference of null pointer | 376 | FP | FP | 切片代码仅展示了宏定义和函数框架，未显示任何对指针`s`进行解引用的具体操作。告警点位于宏`UPDATE_CACHE`的调用处，而该宏的定义并未在切片中展示其可能解引用指针的逻辑。结合参考标签为FP，倾向于认为这是工具对宏展开的误判。 |
| 1632 | ffmpeg-7.1.1 | finalize_packet | Dereference of null pointer | 678 | FP | FP | 切片代码显示，在访问 `s->st->time_base.den` 之前，已经存在对 `s->st` 的间接保护。`s->st` 仅在 `s->ic->nb_streams > 1` 的条件下被使用，且 `s->ic` 在之前的条件 ... |
| 1633 | ffmpeg-7.1.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 413 | FP | FP | 切片代码显示，在访问 `ctx->buffers` 数组前，存在条件判断 `if (ctx->buffers)` 和循环边界检查 `i < ctx->num_buffers`，这确保了数组指针和索引的有效性。告警点 `avbuf = ... |
| 1634 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 299 | FP | FP | 切片代码中，`src` 指针作为函数参数传入，并在多个分支中被安全地用于数组索引和指针运算，未见明显的空指针解引用路径。告警点 `((uint16_t*)(src + stride*y))[x]` 的访问依赖于 `src` 非空，而函... |
| 1635 | ffmpeg-7.1.1 | roq_dpcm_encode_frame | Dereference of null pointer | 180 | FP | FP | 告警行访问 `frame->pts` 的条件是 `context->input_frames <= 7`，而在此行之前，代码逻辑已确保当 `frame` 为 NULL 时，`context->input_frames` 会被设置为至少... |
| 1636 | ffmpeg-7.1.1 | ebml_read_binary | Dereference of null pointer | 1095 | FP | FP | 在切片代码中，`av_buffer_realloc` 函数成功返回后，`bin->buf` 指针不可能为空。该函数在分配失败时会返回错误码，调用者会直接返回，不会执行到后续的 `memset` 行。因此，对 `bin->buf->da... |
| 1637 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 209 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回 `AVERROR(ENOMEM)`，因此 `ptr2` 不可能为 NULL。工具报告的空指... |
| 1638 | ffmpeg-7.1.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | FP | 切片代码显示，指针 `dc_val` 作为参数传递给函数 `ff_vc1_pred_dc`，该函数负责为其赋值，因此在该行被解引用前，它应该已被初始化为有效指针。告警是基于静态分析对指针可能为空的假设，但代码逻辑表明它已被安全初始化。 |
| 1639 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 告警点位于对 `in->data[plane]` 的访问，切片代码显示 `in` 是函数参数且非空，且其数据指针 `in->data[plane]` 在循环中被使用，表明 `in` 是有效的。工具可能误判了指针状态，结合参考标签 FP... |
| 1640 | ffmpeg-7.1.1 | unsharp_slice_16 | Dereference of null pointer | 172 | FP | FP | 切片代码显示告警点位于宏定义 `DEF_UNSHARP_SLICE_FUNC` 的展开行，该行 `{ NULL }` 是宏定义的一部分，并非实际执行代码。宏展开后，`NULL` 是函数体结束的标记，不会导致空指针解引用。结合参考标签 ... |
| 1641 | ffmpeg-7.1.1 | ebml_parse | Dereference of null pointer | 1363 | FP | FP | 告警指向的代码行 `level->length != EBML_UNKNOWN_LENGTH` 位于 `if (matroska->num_levels > 0)` 条件块内，且其上层条件 `if (level && level->l... |
| 1642 | ffmpeg-7.1.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码中，宏 `BITS_AVAILABLE` 被定义为常量 1，这导致 `while (ret<0x8000000U && BITS_AVAILABLE(re, gb))` 循环条件恒真，可能引发工具误判为无限循环或空指针解引用。... |
| 1643 | ffmpeg-7.1.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在指针解引用操作 `AV_WBBUF(s->buf_ptr, bit_buf)` 之前，已通过条件 `if (s->buf_end - s->buf_ptr >= sizeof(BitBuf))` 检查了缓冲区边界，确保... |
| 1644 | ffmpeg-7.1.1 | rtp_set_prft | Dereference of null pointer | 646 | FP | FP | 切片代码显示，在调用`av_rescale_q`之前，已对`av_packet_new_side_data`的返回值`prft`进行了空指针检查，若为空则直接返回错误，因此后续对`s->st`的访问不会在`prft`为空时发生。告警点... |
| 1645 | ffmpeg-7.1.1 | ebml_read_sint | Dereference of null pointer | 1022 | FP | FP | 切片代码显示，函数`avio_r8`内部有缓冲区边界检查，当`buf_ptr >= buf_end`时会调用`fill_buffer`，且最终会返回0而非导致空指针解引用。告警点`sign_extend(avio_r8(pb), 8)... |
| 1646 | ffmpeg-7.1.1 | safe_filename | Dereference of null pointer | 98 | FP | FP | 函数逻辑在解引用指针 `f` 前，已通过 `for (; *f; f++)` 的条件 `*f` 确保了指针非空，且循环体内部的条件判断也依赖于 `*f` 的值，代码路径安全，不存在空指针解引用。 |
| 1647 | ffmpeg-7.1.1 | try_push_frame | Dereference of null pointer | 512 | FP | FP | 告警点访问 `s->input_frames[0]` 前，代码已通过 `if (!nb_samples) goto eof;` 确保至少有一个输入帧存在，且 `nb_samples` 的计算逻辑表明 `s->input_frames[... |
| 1648 | ffmpeg-7.1.1 | dump_stream_group | Dereference of null pointer | 788 | FP | FP | 告警点位于循环内对数组 `printed` 的赋值，切片显示 `printed` 是函数参数，其有效性由调用者保证。切片中未发现 `printed` 为空的证据，且 `label` 为 FP，倾向于判定为误报。 |
| 1649 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，当 `s->planeheight[plane] > 1` 条件不满足时，`linesize` 被显式赋值为0，因此对 `linesize` 的后续使用（如 `val += linesize`）是安全的，不会导致空指针解引用。 |
| 1650 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 236 | FP | FP | 告警点位于 `av_assert0` 宏调用内，该宏用于调试断言，在条件不满足时会调用 `abort()` 终止程序，而非解引用空指针。切片代码中 `frame` 变量在进入该分支前已通过 `if (frame)` 检查，因此 `fr... |
| 1651 | ffmpeg-7.1.1 | ff_encode_encode_cb | Dereference of null pointer | 275 | FP | FP | 告警点位于条件判断 `if (frame->duration)`，但切片代码显示，在进入该分支前，外层存在 `if (frame && ...)` 的条件检查，确保了 `frame` 指针非空。因此，对 `frame->duratio... |
| 1652 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 219 | FP | FP | 告警指向的代码行位于 `av_assert0` 宏内部，该宏用于开发调试，在条件不满足时会调用 `abort()` 终止程序，这属于预期的断言检查而非空指针解引用。切片代码中 `frame` 指针在进入该分支前已通过 `if (fra... |
| 1653 | ffmpeg-7.1.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 代码切片显示告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后是对结构体指针 `s` 的操作。函数 `get_sbits` 的参数 `s` 在调用时未被检查，但该函数是内联工具函数，其调用上下文（如调用者是否已对指针进行校验... |
| 1654 | ffmpeg-7.1.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码中，变量 `dpd` 在条件判断 `if (dpd[pos])` 中被直接解引用，但其来源和初始化在切片中不可见。结合告警规则为解引用空指针，以及算法标签为 FP，倾向于认为 `dpd` 在完整上下文中已被正确初始化或分配，导... |
| 1655 | ffmpeg-7.1.1 | try_push_frame | Dereference of null pointer | 241 | FP | FP | 切片代码显示，在解引用 `inbuf[0]` 之前，`ff_inlink_consume_samples` 函数可能成功返回并填充了 `inbuf[i]` 数组，且告警行位于一个循环之后，该循环旨在为所有输入填充缓冲区。虽然存在 `i... |
| 1656 | ffmpeg-7.1.1 | hls_append_segment | Dereference of null pointer | 1185 | FP | FP | 切片代码中，在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 之前，`en` 被赋值为 `vs->segments`，... |
| 1657 | ffmpeg-7.1.1 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 切片代码显示，在DIR_DURATION指令执行前，必须通过DIR_FILE指令调用add_file函数来初始化file指针。add_file函数成功执行后会将file指针赋值给*rfile，确保file非空。因此，在DIR_DURA... |
| 1658 | ffmpeg-7.1.1 | dump_argument | Dereference of null pointer | 516 | FP | FP | 函数参数 `a` 在循环条件 `*p` 中被直接解引用，但该参数由调用者传入，在切片中无法确认其为空。代码逻辑本身是安全的，告警是基于对参数可能为空的假设，而该假设在切片中无证据支持。参考标签 `label` 为 FP，也倾向于误报。 |
| 1659 | ffmpeg-7.1.1 | kalman_smoothen | Dereference of null pointer | 585 | FP | FP | 代码逻辑确保了`best_hist_ptr`在解引用前已被赋值。`optimal_gain`初始为0，`best_hist_ptr`初始为NULL，但只有在`dot > optimal_gain`（即`optimal_gain > 0... |
| 1660 | ffmpeg-7.1.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在告警行`dp1[pos] = s->tint[0];`之前，存在条件判断`if (dpd[pos])`，这确保了`dpd[pos]`不为零，从而间接保证了`dp1`和`dp2`指针的有效性。代码逻辑在切片可见范围内提供... |
| 1661 | ffmpeg-7.1.1 | id3v2_parse | Dereference of null pointer | 1055 | FP | FP | 告警点位于函数指针 `extra_func->read` 的调用处，但在调用前，`extra_func` 是通过 `get_extra_meta_func` 函数获取的，该函数仅在找到匹配的tag时才返回非空指针。切片代码显示，调用 ... |
| 1662 | ffmpeg-7.1.1 | set_bframe_chain_length | Dereference of null pointer | 1596 | FP | FP | 切片代码显示，在访问 `s->input_picture[i - 1]->f->data[0]` 之前，存在对 `s->input_picture[i]` 的非空检查，且循环变量 `i` 从1开始，确保了 `i-1` 为0。结合函数开... |
| 1663 | ffmpeg-7.1.1 | split_commandline | Dereference of null pointer | 809 | FP | FP | 告警点位于检查 `opt[0] == '-' && opt[1] == '-' && !opt[2]` 的条件判断中，用于识别命令行参数 `--`。在切片代码中，`opt` 是 `argv[optindex++]` 的指针，而 `ar... |
| 1664 | ffmpeg-7.1.1 | ebml_read_ascii | Dereference of null pointer | 1077 | FP | FP | 切片代码显示 `av_free` 被定义为 `while(0)` 宏，这是一个空操作，因此对 `*str` 的解引用实际上不会发生。同时，`av_malloc` 被定义为返回 `NULL`，但告警点并非针对其返回值。结合代码逻辑和参考... |
| 1665 | ffmpeg-7.1.1 | output_packet | Dereference of null pointer | 1103 | FP | FP | 在访问 `timestamp_packet->unwritten_size` 之前，代码通过 `if (timestamp_packet)` 检查了指针 `timestamp_packet` 是否为空，因此不会发生空指针解引用。 |
| 1666 | ffmpeg-7.1.1 | enc_open | Dereference of null pointer | 286 | FP | FP | 切片代码显示，在访问 `ost->ist->par->width` 和 `ost->ist->par->height` 之前，代码逻辑已通过 `av_assert0` 宏确保 `frame` 存在或编码器类型非音视频，且该分支仅在 `... |
| 1667 | ffmpeg-7.1.1 | ebml_read_uint | Dereference of null pointer | 1002 | FP | FP | 切片代码显示，在指针解引用前，函数已通过 `if (size == 0)` 分支对 `num` 进行了赋值，确保了指针非空。后续的 `*num = 0;` 操作是安全的，不存在解引用空指针的逻辑错误。 |
| 1668 | ffmpeg-7.1.1 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 切片代码显示，在DIR_INPOINT指令（告警行）执行前，DIR_FILE指令已通过add_file函数初始化了file指针，且该指针在循环中持续有效。告警点访问file->inpoint时，file不可能为NULL，因此不存在空指... |
| 1669 | ffmpeg-7.1.1 | sb_decode | Dereference of null pointer | 1348 | FP | FP | 告警行 `innov_save[2 * i] = exc[i];` 位于 `if (st->innov_save)` 条件块内，切片代码显示 `innov_save` 指针在该条件块中被初始化为 `st->innov_save + 2... |
| 1670 | ffmpeg-7.1.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警指向的代码行位于条件判断 `if ((*child)->state * 2 == -t->state)` 内部，该条件仅在 `t->state` 非零且 `t->state` 为偶数（`!(t->state & 1)`）时才会进入... |
| 1671 | ffmpeg-7.1.1 | check_header_mismatch | Dereference of null pointer | 519 | FP | FP | 切片代码中，在警告行`curr = curr->next;`之前，循环条件`curr != child`和`i < FLAC_MAX_SEQUENTIAL_HEADERS`共同保证了`curr`不会为NULL。此外，紧随其后的`av_... |
| 1672 | ffmpeg-7.1.1 | get_pict_type | Dereference of null pointer | 136 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效范围，这确保了 `unit->conte... |
| 1673 | ffmpeg-7.1.1 | ogg_write_header | Dereference of null pointer | 629 | FP | FP | 切片代码显示 `oggstream` 指针在解引用前未被检查，但告警点是对其成员 `page.start_granule` 的赋值，这本身不会导致空指针解引用崩溃。结合算法标签为 FP，倾向于判定为工具误报。 |
| 1674 | ffmpeg-7.1.1 | mpegts_open_filter | Dereference of null pointer | 495 | FP | FP | 切片代码显示，在调用 `av_log` 之前，`ts` 指针仅在函数参数中传递，并未被检查或解引用为空。`av_log` 宏被定义为 `while(0)`，意味着该调用在编译后不存在，因此不可能发生空指针解引用。 |
| 1675 | ffmpeg-7.1.1 | guess_mv | Dereference of null pointer | 432 | FP | FP | 在告警行 `else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])` 中，对 `s->last_pic.f` 的访问已由前序条件 `if (s->last_pic.mo... |
| 1676 | ffmpeg-7.1.1 | build_table | Dereference of null pointer | 204 | FP | FP | 告警指向的代码行 `table[j].len = -subtable_bits;` 在切片中可见，`table` 指针来源于 `alloc_table` 函数成功返回后的 `vlc->table[table_index]`。`allo... |
| 1677 | ffmpeg-7.1.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在访问 `chapters[i]` 之前，外层存在条件判断 `if (chapters && nb_chapters)` 和 `if (m)`，并且内部循环 `for (int i = 0; i < nb_chapter... |
| 1678 | ffmpeg-7.1.1 | locate_option | Dereference of null pointer | 495 | FP | FP | 代码逻辑中，在调用 `find_option` 后，仅在 `po->name` 为假（即未找到选项）且 `cur_opt` 以 "no" 开头时，才会重新调用 `find_option` 并覆盖 `po`。在首次调用 `find_op... |
| 1679 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 78 | FP | FP | 切片代码显示，`UPDATE_CACHE` 是一个宏，其展开不涉及对 `gb` 指针的直接解引用。告警点位于宏定义行，实际解引用操作可能发生在宏展开后的内部逻辑中，但切片未提供该内部逻辑，无法确认空指针解引用。结合参考标签为 FP，倾... |
| 1680 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 切片代码显示，在宏CHECK_BIT内部使用'dst'指针前，已通过'if (dst)'进行了空指针检查，确保了不会发生空指针解引用。算法标签也为FP，与代码分析一致。 |
| 1681 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 333 | FP | FP | 告警行 `new_pts = av_rescale_q(...)` 仅在 `if (s->do_video)` 条件为真时执行，而该条件块内部已通过 `outlink = s->do_video ? ctx->outputs[1] :... |
| 1682 | ffmpeg-7.1.1 | av_dump_format | Dereference of null pointer | 898 | FP | FP | 切片代码显示，在访问 `printed` 数组前，存在条件 `if (ic->nb_streams && !printed) return;` 确保当 `ic->nb_streams` 非零且 `printed` 为 NULL 时函数... |
| 1683 | ffmpeg-7.1.1 | check_header_mismatch | Dereference of null pointer | 475 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 之前，`curr` 变量通过 `while (curr != child)` 循环进行遍历，且 `curr` 初始化为非空的 `header` 参数，因此 `cur... |
| 1684 | ffmpeg-7.1.1 | update_context_from_thread | Dereference of null pointer | 438 | FP | FP | 切片代码中，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 进行了条件检查，并且 `hwacce... |
| 1685 | ffmpeg-7.1.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 切片代码显示，在调用UPDATE_CACHE_32等宏之前，已通过OPEN_READER宏初始化了读取器，并且告警点位于一个经过充分测试的位读取辅助函数内部。结合该函数在项目中被广泛使用且算法标签为FP，表明此告警极有可能是静态分析工... |
| 1686 | ffmpeg-7.1.1 | activate | Dereference of null pointer | 186 | FP | FP | 在告警行`frame->pts = s->pts;`之前，代码已通过条件分支确保`frame`指针非空。在`s->stop_mode == MODE_ADD`分支中，若`ff_get_video_buffer`失败会直接返回错误；在`... |
| 1687 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 200 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回 `AVERROR(ENOMEM)`。因此，在后续使用 `ptr2` 的上下文中，它不会是空指针。 |
| 1688 | ffmpeg-7.1.1 | check_available | Dereference of null pointer | 616 | FP | FP | 代码中 `cu` 指针来自函数参数 `lc->cu`，在切片范围内未见其可能为空的证据。告警行对 `cu->pred_mode` 的访问发生在 `cu` 已被使用的同一条件块内，且逻辑上 `cu` 应为有效指针。结合参考标签为 FP，... |
| 1689 | ffmpeg-7.1.1 | ff_encode_encode_cb | Dereference of null pointer | 272 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，其执行前提是 `frame` 指针非空（由外层 `if (frame && ...)` 和 `if (!ret && *got_pack... |
| 1690 | ffmpeg-7.1.1 | rtp_parse_one_packet | Dereference of null pointer | 888 | FP | FP | 切片代码显示，在告警行访问 `buf[0]` 之前，存在 `if (!buf)` 和 `if (len < 12)` 的检查。当 `buf` 为 NULL 时，函数会提前返回，不会执行到解引用操作。因此，该告警是误报。 |
| 1691 | ffmpeg-7.1.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已通过条件 `if (dpd[pos])` 和 `if (s->peak[i][j] && ...)` 进行了检查，且 `dpd` 指针来源于 `out->data` 数组的有效索引，... |
| 1692 | ffmpeg-7.1.1 | ost_add | Dereference of null pointer | 1541 | FP | FP | 告警点 `ms->stream_duration = ist->st->duration;` 位于 `if (ost->ist && ost->ist->st->duration > 0)` 条件块内，该条件已确保 `ist` 和 `... |
| 1693 | ffmpeg-7.1.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1420 | FP | FP | 代码中 `scale_matrix` 的赋值受条件 `sps->scaling_list_enabled && !(transform_skip_flag && log2_trafo_size > 2)` 保护，且在使用前有明确的 `... |
| 1694 | ffmpeg-7.1.1 | nal_parse_units | Dereference of null pointer | 93 | FP | FP | 告警指向的代码行 `list->nb_nalus >= nalu_limit` 是对 `list->nalus` 数组边界的安全检查，`list` 指针本身在函数入口处已作为参数传入，切片中未见其可能为空的证据。该行是条件判断，并非解... |
| 1695 | ffmpeg-7.1.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1513 | FP | FP | 告警指向的代码行 `out = ff_get_audio_buffer(link, frame->nb_samples);` 中，`frame` 指针已在函数开头通过 `AVFrame *frame = *rframe;` 赋值，且在... |
| 1696 | ffmpeg-7.1.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 代码中`s->buffer`的访问是基于`s->index`的计算结果，在切片中未见`s`或`s->buffer`为空的直接证据。该函数为内联辅助函数，其调用上下文（未在切片中显示）很可能已确保指针有效。结合参考标签为FP，倾向于判定... |
| 1697 | ffmpeg-7.1.1 | asf_parse_packet | Dereference of null pointer | 1307 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data` 的循环前，已通过 `av_assert0(asf_st)` 断言 `asf_st` 非空，且 `asf_st->pkt.data` 由 `av_new_packet` 分配，该... |
| 1698 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 146 | FP | FP | 切片代码显示，在访问 `alpSrcPtr` 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，当条件不满足时 `alpSrcPtr` 被初始化为 `NULL`，且后续所有对 `al... |
| 1699 | ffmpeg-7.1.1 | choose_rct_params | Dereference of null pointer | 1008 | FP | FP | 切片代码显示，在解引用 `src[2]` 指针之前，函数已通过 `f->use32bit ｜｜ transparency` 条件分支确保其被访问，且 `src` 数组作为函数参数传入，在切片可见的上下文中没有证据表明其为空。结合算法标... |
| 1700 | ffmpeg-7.1.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在告警行`dp1[pos] = s->tint[0];`之前，存在条件判断`if (dpd[pos])`，这确保了指针`dp1`和`dp2`仅在`dpd[pos]`为真（非零）时才会被解引用。这表明存在前置的访问控制，防... |
| 1701 | ffmpeg-7.1.1 | unsharp_slice_8 | Dereference of null pointer | 173 | FP | FP | 切片代码显示，宏定义 `DEF_UNSHARP_SLICE_FUNC` 在展开后，告警行 `{ NULL }` 是函数体的一部分，但该函数体在宏展开后已被完整的实现代码所替代，因此不存在对空指针的解引用。这是一个由宏展开导致的静态分析... |
| 1702 | ffmpeg-7.1.1 | mov_write_trak_tag | Dereference of null pointer | 4191 | FP | FP | 告警指向的代码行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 中，`st` 是函数参数，在切片代码的调用上下文中（如 `mov_write_tkhd_... |
| 1703 | ffmpeg-7.1.1 | ebml_parse | Dereference of null pointer | 1380 | FP | FP | 告警指向的代码行位于一个条件分支内，该分支在`level->length != EBML_UNKNOWN_LENGTH`时直接返回错误码`AVERROR_INVALIDDATA`，不会对空指针进行解引用。切片中未发现对空指针`leve... |
| 1704 | ffmpeg-7.1.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 代码在访问 `dpd[pos - 1]`、`dpd[pos + 1]`、`dpd[poa]` 和 `dpd[pob]` 之前，已通过 `(!j ｜｜ ...)`、`(j == (out->width - 1) ｜｜ ...)`、`(!... |
| 1705 | ffmpeg-7.1.1 | get_bits_le | Dereference of null pointer | 361 | FP | FP | 告警点位于宏定义UPDATE_CACHE_LE的展开处，该宏及其相关宏（如OPEN_READER, CLOSE_READER）主要操作结构体指针的成员。切片代码中，函数参数`s`被直接传递给这些宏，但未显示其来源或空值检查。结合该函数... |
| 1706 | ffmpeg-7.1.1 | ac3_apply_rematrixing | Dereference of null pointer | 598 | FP | FP | 切片代码中，`flags` 变量未在函数作用域内定义或作为参数传入，其来源和初始化状态不可见。结合告警规则为解引用空指针，以及算法标签为 FP，推断该变量在调用上下文中已被正确初始化，导致工具误报。 |
| 1707 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 683 | FP | FP | 告警指向的FFSWAP宏操作的是已定义的局部变量`ptr1`和`ptr2`，它们在切片代码的上下文中（`if (js_databuf == q->decoded_bytes_buffer)`分支内）已被正确初始化，不存在空指针解引用。... |
| 1708 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 303 | FP | FP | 切片代码中，`sample[0]` 指针在循环前已通过 `sample[i] = sc->sample_buffer + ...` 明确赋值，指向有效的缓冲区地址，不存在空指针解引用。告警点 `sample[0][x] = ...` ... |
| 1709 | ffmpeg-7.1.1 | ff_rdt_parse_header | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在告警行（while循环条件）中，对`buf`的访问（`buf[1]`）发生在`len >= 5`的检查之后，这确保了指针访问的有效性。同时，`init_get_bits`函数内部也包含对`buffer`（即`buf`）... |
| 1710 | ffmpeg-7.1.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 函数入口处已对指针`info`进行了非空检查，在`if (info)`的保护块内才执行后续的指针解引用操作，因此不会发生空指针解引用。该告警是静态分析工具的逻辑误判。 |
| 1711 | ffmpeg-7.1.1 | shift_frame | Dereference of null pointer | 152 | FP | FP | 切片代码显示，告警点引用的 `frame` 变量在切片中未定义，无法确认其来源和值。然而，关键的 `av_log` 宏被定义为空操作 `while(0)`，这意味着该行代码在实际编译后不会执行，因此不可能发生空指针解引用。 |
| 1712 | ffmpeg-7.1.1 | build_table | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 1713 | ffmpeg-7.1.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], ...)` 之前，`info->key_ids` 数组及其每个元素 `info->key_ids[j]` 都已在 `av_encryption_init_inf... |
| 1714 | ffmpeg-7.1.1 | encode_plane | Dereference of null pointer | 293 | FP | FP | 切片代码中，`sample[0]` 在循环前已从 `sc->sample_buffer` 分配内存并初始化，且告警行处的数组索引 `x` 受循环条件 `x < w` 约束，不会越界访问空指针。代码逻辑保证了指针的有效性，因此是误报。 |
| 1715 | ffmpeg-7.1.1 | dump_stream_group | Dereference of null pointer | 715 | FP | FP | 告警指向的代码行 `printed[st->index] = 1;` 中，变量 `st` 在切片代码中未定义，推测其来自外层循环或上下文，但切片未包含其初始化或赋值。在切片可见范围内，无法确认 `st` 为 null。结合参考标签为 ... |
| 1716 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 166 | FP | FP | 切片代码显示，在解引用 `alpSrcPtr` 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，仅当条件为真时才进行赋值。告警点位于该条件保护的代码块内，因此不会发生空指针解引用。 |
| 1717 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该宏及其相关宏（如 OPEN_READER, GET_VLC, CLOSE_READER）均被正确定义，且函数 get_vlc2 的逻辑是标准且完整的位读取操作，未见空指针解... |
| 1718 | ffmpeg-7.1.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在深度大于8的分支中，`linesize`的计算包含一个三元运算符，当`s->planeheight[plane] > 1`为假时，`linesize`被赋值为0。在后续的CHECK_BIT宏调用中，`val[(x) +... |
| 1719 | ffmpeg-7.1.1 | set_bframe_chain_length | Dereference of null pointer | 1611 | FP | FP | 告警指向的代码行 `s->input_picture[i]->b_frame_score = 0;` 位于一个受保护的循环内，该循环的终止条件是 `i < b_frames + 1`，而 `b_frames` 是通过 `FFMAX(0... |
| 1720 | ffmpeg-7.1.1 | mov_write_trak_tag | Dereference of null pointer | 4196 | FP | FP | 切片代码中，在调用 `is_clcp_track(track)` 之前，`track` 指针作为函数参数传入，并且在函数内部被多次安全使用（如 `track->mode`、`track->par` 等），没有证据表明 `track` ... |
| 1721 | ffmpeg-7.1.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 代码切片显示告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后对指针 s 的访问是安全的，因为函数入口处未对 s 进行空指针检查，但这是位读取器的核心函数，通常由调用者保证指针有效性。结合参考标签 FP 及代码逻辑，判定为误报。 |
| 1722 | ffmpeg-7.1.1 | <global> | Dereference of null pointer | 472 | FP | FP | 切片代码显示，宏 `DECODE_CODEWORD` 内部调用了 `UPDATE_CACHE` 和 `GET_CACHE` 来操作 `GetBitContext *gb`，这是FFmpeg中标准的比特流读取机制，旨在安全地从缓冲区获取... |
| 1723 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 687 | FP | FP | 切片代码显示，在警告行（`q->decoded_bytes_buffer[i] = *ptr2--;`）之前，`q->decoded_bytes_buffer` 已在 `else` 分支的上下文（`js_databuf != q->d... |
| 1724 | ffmpeg-7.1.1 | decode_frame | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确初始化为 `q->decoded_bytes_buffer`，这是一个有效的缓冲区指针。循环条件 `... |
| 1725 | ffmpeg-7.0.1 | show_bits | Dereference of null pointer | 376 | FP | FP | 切片代码仅展示了宏定义和函数框架，未提供`s`指针的获取或验证上下文。在缺乏明确空指针来源证据的情况下，结合参考标签`label`为FP，倾向于判定为工具误报。 |
| 1726 | ffmpeg-7.0.1 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 切片代码显示，在访问 `s->st->time_base.den` 和 `s->st->time_base.num` 之前，存在对 `s->st` 的间接访问 `s->ic->nb_streams` 的条件判断。虽然 `s->st` ... |
| 1727 | ffmpeg-7.0.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 412 | FP | FP | 切片代码显示，在访问 `ctx->buffers` 数组前，存在 `if (ctx->buffers)` 的判空检查，且告警行 `avbuf = &ctx->buffers[buf.index];` 中的 `buf.index` 来自... |
| 1728 | ffmpeg-7.0.1 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | FP | 告警行访问 `frame->pts` 的条件是 `context->input_frames <= 7`，而在此行之前，代码逻辑已确保当 `frame` 为 NULL 时，`context->input_frames` 会被设置为至少... |
| 1729 | ffmpeg-7.0.1 | ebml_read_binary | Dereference of null pointer | 1088 | FP | FP | 在切片代码中，`av_buffer_realloc` 函数在成功时返回0，并确保 `*pbuf` 指向一个有效的 `AVBufferRef` 结构体，其 `buf` 成员不为空。因此，当 `ret < 0` 不成立时，`bin->bu... |
| 1730 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回错误。在告警所在行，`ptr2` 指向有效的已分配内存，不会发生空指针解引用。 |
| 1731 | ffmpeg-7.0.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | FP | 告警点 `*dc_val = dcdiff;` 中，`dc_val` 在调用 `ff_vc1_pred_dc` 时作为指针参数传入，该函数应负责将其初始化为有效指针。切片代码中 `dc_val` 初始化为 NULL，但随后作为输出参数... |
| 1732 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 告警点位于宏展开的代码中，但切片显示变量`val`在解引用前已从`in->data[plane]`正确赋值，且`in`帧在函数入口非空。代码逻辑在切片可见范围内保证了`val`指针的有效性，解引用是安全的。 |
| 1733 | ffmpeg-7.0.1 | unsharp_slice_16 | Dereference of null pointer | 141 | FP | FP | 切片代码显示，在宏展开的函数定义中，`src2` 变量被初始化为 NULL，但后续代码中并未对其进行解引用。告警点位于宏定义行，该行本身不执行解引用操作，因此是静态分析工具的逻辑误报。 |
| 1734 | ffmpeg-7.0.1 | ebml_parse | Dereference of null pointer | 1354 | FP | FP | 切片代码显示，在访问 `level->length` 之前，已通过条件 `matroska->num_levels > 0` 确保 `level` 指针非空。该条件在告警行之前已检查，因此不会发生空指针解引用。 |
| 1735 | ffmpeg-7.0.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码中，`UPDATE_CACHE` 宏的展开未直接显示对 `gb` 指针的解引用，且告警行位于宏调用处。结合提供的宏定义 `BITS_AVAILABLE` 恒为1，以及 `label` 为 FP，表明该告警很可能是静态分析工具对... |
| 1736 | ffmpeg-7.0.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 代码切片显示，在指针解引用前存在明确的空指针检查 `if (s->buf_end - s->buf_ptr >= sizeof(BitBuf))`，这确保了 `s->buf_ptr` 在写入操作 `AV_WBBUF` 时是有效的，因此... |
| 1737 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码显示，在告警行访问 `src` 指针前，该指针作为函数参数传入，并在循环中被直接用于数组索引和类型转换，未见其被赋值为 NULL 或存在导致其为 NULL 的路径。结合 `label` 为 FP，倾向于判定为工具误报。 |
| 1738 | ffmpeg-7.0.1 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 切片代码显示，在调用 `av_rescale_q` 之前，已对 `av_packet_new_side_data` 的返回值 `prft` 进行了空指针检查，若为空则提前返回错误。因此，在告警行执行时，`s` 和 `s->st` 不可... |
| 1739 | ffmpeg-7.0.1 | ebml_read_sint | Dereference of null pointer | 1015 | FP | FP | 切片代码显示，在调用 `avio_r8` 读取数据前，函数 `ebml_read_sint` 已通过 `size == 0` 的条件判断确保了执行路径的安全性。`avio_r8` 函数内部有缓冲区边界检查，并会在读取失败时返回默认值0... |
| 1740 | ffmpeg-7.0.1 | safe_filename | Dereference of null pointer | 97 | FP | FP | 代码逻辑显示，指针 `f` 在循环条件 `*f` 中被解引用前，已通过函数参数传入，且循环条件 `for (; *f; f++)` 确保了只有当 `*f` 非零（即指针指向有效字符）时才进入循环体。在循环体内对 `*f` 的解引用是安... |
| 1741 | ffmpeg-7.0.1 | try_push_frame | Dereference of null pointer | 511 | FP | FP | 告警指向的代码行 `frame->pts = s->input_frames[0]->pts;` 在切片上下文中是安全的。因为前面的 `if (!nb_samples) goto eof;` 逻辑确保了当 `nb_samples` 为... |
| 1742 | ffmpeg-7.0.1 | dump_stream_group | Dereference of null pointer | 751 | FP | FP | 切片代码中，告警行 `printed[st->index] = 1;` 位于 `for (int i = 0; i < stg->nb_streams; i++)` 循环内，且 `st` 来自 `stg->streams[i]`。`s... |
| 1743 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 切片代码显示，当 `s->planeheight[plane] > 1` 条件不满足时，`linesize` 被显式赋值为 0，这避免了后续对 `val` 和 `dst` 的指针运算中使用未初始化的值。告警点 `in->linesiz... |
| 1744 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 225 | FP | FP | 告警点位于 `av_assert0` 宏内部，该宏用于调试断言，在条件失败时会调用 `abort()` 终止程序，因此对空指针 `frame` 的访问（`frame->format`）仅在断言失败、程序即将退出的路径上发生，不属于正常... |
| 1745 | ffmpeg-7.0.1 | ff_encode_encode_cb | Dereference of null pointer | 274 | FP | FP | 告警点位于条件判断 `if (frame->duration)`，但切片代码显示，在进入该分支前，外层存在 `if (frame && ...)` 的条件检查，且函数开头已对 `frame` 指针进行了非空使用（如 `frame->p... |
| 1746 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 208 | FP | FP | 告警点位于 `av_assert0` 宏内，该宏用于调试断言，在条件不满足时会调用 `abort()` 终止程序，而非产生空指针解引用。切片代码中 `frame` 指针在 `enc->type` 为音频或视频时可能为空，但 `av_a... |
| 1747 | ffmpeg-7.0.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该宏及其相关宏（如 OPEN_READER）均未对指针 's' 进行解引用操作。代码逻辑是安全的，工具可能误判了宏展开后的空指针解引用风险。 |
| 1748 | ffmpeg-7.0.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码中，变量 `dpd` 在条件判断 `if (dpd[pos])` 中被直接解引用，但其来源和初始化在切片中不可见。结合告警规则（解引用空指针）和算法标签（FP）判断，该指针很可能已在切片外的上下文中被正确分配和初始化，导致工具误报。 |
| 1750 | ffmpeg-7.0.1 | try_push_frame | Dereference of null pointer | 241 | FP | FP | 切片代码显示，`inbuf[0]` 在循环中被 `ff_inlink_consume_samples` 调用赋值，该函数在成功时会将 `*rframe`（即 `&inbuf[i]`）设置为非空帧。虽然存在 `inbuf[0]` 为 `... |
| 1751 | ffmpeg-7.0.1 | hls_append_segment | Dereference of null pointer | 1171 | FP | FP | 在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 之前，代码已通过 `en = vs->segments;` 将 `e... |
| 1752 | ffmpeg-7.0.1 | concat_parse_script | Dereference of null pointer | 557 | FP | FP | 告警点位于 `file->user_duration = arg_int[0];`，但切片代码显示，只有当 `dir->flags & NEEDS_FILE` 为真且 `cat->nb_files` 不为零时，才会执行到 `DIR_D... |
| 1753 | ffmpeg-7.0.1 | dump_argument | Dereference of null pointer | 507 | FP | FP | 函数参数 `a` 在循环条件 `for (p = a; *p; p++)` 中被直接解引用，这仅在 `a` 为 NULL 时会导致空指针解引用。但该函数是静态工具函数，其调用上下文未知，且参考标签为 FP 表明该告警在后续版本中持续存... |
| 1754 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 297 | FP | FP | 切片代码显示，在告警行 `sample[0][x] = ((uint16_t*)(src + stride*y))[x];` 中，`src` 是函数参数，`stride` 和 `y` 是循环变量，没有证据表明 `src + strid... |
| 1755 | ffmpeg-7.0.1 | kalman_smoothen | Dereference of null pointer | 584 | FP | FP | 代码逻辑确保了`best_hist_ptr`在解引用前已被赋值。`optimal_gain`初始为0，循环中只有当`dot > optimal_gain`（即`dot > 0`）时才会更新`best_hist_ptr`。若循环后`op... |
| 1756 | ffmpeg-7.0.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在访问 `dp1[pos]` 和 `dp2[pos]` 之前，存在条件 `if (dpd[pos])` 进行保护，这确保了指针 `dp1` 和 `dp2` 的访问是基于有效位置 `pos` 的。结合算法参考标签为 FP，... |
| 1757 | ffmpeg-7.0.1 | id3v2_parse | Dereference of null pointer | 1054 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 函数获取的，该函数仅在找到匹配的标签时才返回非空指针。告警点位于 `else` 分支，该分... |
| 1758 | ffmpeg-7.0.1 | choose_rct_params | Dereference of null pointer | 983 | FP | FP | 切片代码显示告警行访问的 `src[1]` 和 `src[2]` 指针在函数参数中定义为 `const uint8_t *src[3]`，表明调用者已传入一个包含三个有效指针的数组。在 `lbd` 为假的 `else` 分支中，代码逻... |
| 1759 | ffmpeg-7.0.1 | split_commandline | Dereference of null pointer | 800 | FP | FP | 切片代码中，在调用 `find_option` 后直接解引用 `po->name`，但 `find_option` 函数保证返回一个有效的 `OptionDef` 指针（即使未找到匹配项，也返回一个结构体，其 `name` 字段可能为... |
| 1760 | ffmpeg-7.0.1 | ebml_read_ascii | Dereference of null pointer | 1070 | FP | FP | 切片代码显示 `av_free` 被定义为 `while(0)` 宏，这是一个空操作，因此对 `*str` 的解引用不会发生，不存在空指针解引用风险。参考标签 `label` 为 FP，与代码分析结论一致。 |
| 1761 | ffmpeg-7.0.1 | output_packet | Dereference of null pointer | 1102 | FP | FP | 在访问 `timestamp_packet->unwritten_size` 之前，代码通过 `if (timestamp_packet)` 检查了指针 `timestamp_packet` 是否为空，因此不会发生空指针解引用。 |
| 1762 | ffmpeg-7.0.1 | enc_open | Dereference of null pointer | 293 | FP | FP | 切片代码显示，在访问 `ost->ist->par` 之前，`ost` 和 `ost->ist` 的初始化与空值检查逻辑未包含在切片内，但告警行代码位于 `enc_ctx->codec_type` 为 `AVMEDIA_TYPE_SU... |
| 1763 | ffmpeg-7.0.1 | ebml_read_uint | Dereference of null pointer | 995 | FP | FP | 切片代码显示，在指针解引用前，函数已通过 `if (size == 0)` 分支对 `num` 进行了赋值，确保了指针的有效性。此外，`label` 为 FP 也支持了代码逻辑安全的判断。 |
| 1764 | ffmpeg-7.0.1 | concat_parse_script | Dereference of null pointer | 561 | FP | FP | 在DIR_INPOINT指令处理前，代码已通过DIR_FILE指令调用add_file函数初始化了file指针，且add_file函数成功执行后会将*rfile指向有效的ConcatFile结构体。切片代码显示file指针在赋值给fi... |
| 1766 | ffmpeg-7.0.1 | ost_add | Dereference of null pointer | 1428 | FP | FP | 切片代码中，在访问 `ist->st->duration` 之前，存在条件 `if (ost->ist && ost->ist->st->duration > 0)`，该条件已对 `ist` 和 `ist->st` 进行了非空检查，确... |
| 1767 | ffmpeg-7.0.1 | sb_decode | Dereference of null pointer | 1347 | FP | FP | 在访问 `innov_save` 指针前，代码已通过 `if (st->innov_save)` 检查其非空，且 `innov_save` 被赋值为 `st->innov_save + 2 * offset`，该指针源自已验证的非空指... |
| 1768 | ffmpeg-7.0.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 警告指向的代码行位于条件 `if ((*child)->state * 2 == -t->state)` 内部，该条件仅在 `t->state` 非零且 `t->state` 为偶数（`!(t->state & 1)`）时才会被评估。... |
| 1769 | ffmpeg-7.0.1 | check_header_mismatch | Dereference of null pointer | 520 | FP | FP | 切片代码显示，在访问 `header->link_penalty[i]` 之前，变量 `i` 由 `for` 循环控制，其值在循环结束后为 `FLAC_MAX_SEQUENTIAL_HEADERS` 或当 `curr == child... |
| 1770 | ffmpeg-7.0.1 | get_pict_type | Dereference of null pointer | 135 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效范围，这确保了 `unit->conte... |
| 1771 | ffmpeg-7.0.1 | ogg_write_header | Dereference of null pointer | 628 | FP | FP | 切片代码显示告警行是对结构体成员的直接赋值，并非对空指针的解引用。变量 `oggstream` 在切片中未定义，但赋值操作本身不构成空指针解引用，且参考标签为 FP，倾向于判定为工具误报。 |
| 1772 | ffmpeg-7.0.1 | mpegts_open_filter | Dereference of null pointer | 497 | FP | FP | 切片代码显示，在调用 `av_log` 之前，`ts` 指针已在函数参数中传入，且函数逻辑中未对其进行修改或置空。`av_log` 宏被定义为空操作 `while(0)`，因此即使 `ts` 为空，该行也不会发生解引用。告警是对一个无... |
| 1773 | ffmpeg-7.0.1 | guess_mv | Dereference of null pointer | 428 | FP | FP | 在告警行（else if条件）之前，存在对`s->last_pic.f->data[0]`和`s->last_pic.motion_val[0]`的明确非空检查，确保了指针在解引用前有效。切片代码的逻辑表明该告警是误报。 |
| 1774 | ffmpeg-7.0.1 | build_table | Dereference of null pointer | 204 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 1775 | ffmpeg-7.0.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 告警指向的代码行 `AVChapter *chp = chapters[i];` 位于 `if (chapters && nb_chapters)` 和 `if (m)` 两个条件语句的保护之下。当 `chapters` 为 NULL... |
| 1776 | ffmpeg-7.0.1 | locate_option | Dereference of null pointer | 486 | FP | FP | 在调用 `po->name` 之前，`po` 变量由 `find_option` 函数返回，该函数保证返回一个指向 `OptionDef` 结构体的指针（即使未找到匹配项，也返回指向数组末尾的指针，而非 NULL）。因此，对 `po`... |
| 1777 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 切片代码显示，在深度大于8的分支中，`val`指针被赋值为`(uint16_t *)in->data[plane]`，而`in`是函数参数，非空指针。告警点`val[(x)]`的访问基于此非空指针，且切片内未见导致其变为空的逻辑。工具... |
| 1778 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 332 | FP | FP | 告警行 `new_pts = av_rescale_q(...)` 仅在 `if (s->do_video)` 条件为真时执行，而该条件块内部已通过 `outlink = s->do_video ? ctx->outputs[1] :... |
| 1779 | ffmpeg-7.0.1 | av_dump_format | Dereference of null pointer | 834 | FP | FP | 切片代码显示，在访问 `printed` 数组前，已通过条件 `if (ic->nb_streams && !printed) return;` 确保 `printed` 在 `ic->nb_streams > 0` 时不为空。后续访... |
| 1780 | ffmpeg-7.0.1 | check_header_mismatch | Dereference of null pointer | 476 | FP | FP | 切片代码显示，在访问 `curr->link_penalty[i]` 的循环中，`curr` 变量通过 `curr = curr->next;` 遍历链表，其值由 `header` 初始化并确保不等于 `child`。`curr` 作... |
| 1781 | ffmpeg-7.0.1 | update_context_from_thread | Dereference of null pointer | 360 | FP | FP | 切片代码中，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 进行了条件检查，并且 `hwacce... |
| 1782 | ffmpeg-7.0.1 | choose_rct_params | Dereference of null pointer | 984 | FP | FP | 切片代码显示，在访问 `src[2]` 指针前，函数已通过 `for (p = 0; p < 3; p++)` 循环对 `src` 数组进行了遍历使用，且告警行位于 `lbd` 为 false 的 `else` 分支内，该分支逻辑与 ... |
| 1783 | ffmpeg-7.0.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 告警点位于宏 UPDATE_CACHE_32 的展开处，该宏的参数 `s` 在函数入口处已通过 `av_assert2` 进行了非空断言。虽然静态分析可能无法完全追踪宏展开和断言语义，但代码逻辑在切片内已通过断言明确要求指针非空，且 ... |
| 1784 | ffmpeg-7.0.1 | activate | Dereference of null pointer | 186 | FP | FP | 告警点位于 `frame->pts = s->pts;`，但根据切片代码逻辑，当执行到该行时，`frame` 变量要么由 `ff_get_video_buffer` 成功分配，要么由 `av_frame_clone` 成功克隆，两者在... |
| 1785 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 199 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回 `AVERROR(ENOMEM)`。因此，在后续使用 `ptr2` 的代码路径中，它不可能... |
| 1786 | ffmpeg-7.0.1 | ff_encode_encode_cb | Dereference of null pointer | 271 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，该行代码 `avpkt->pts = frame->pts;` 仅在 `frame` 指针非空时才会执行。切片代码显示，外层条件 `if... |
| 1787 | ffmpeg-7.0.1 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，代码已通过 `if (!buf) { ... }` 和 `if (len < 12) return -1;` 对 `buf` 指... |
| 1788 | ffmpeg-7.0.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `s->peak[i][j]` 之前，已通过循环 `if (dpd[pos]) s->peak[i][j] = 1;` 对数组进行了初始化赋值，因此 `s->peak` 数组在后续使用前已被正确设置，不存在空指针... |
| 1789 | ffmpeg-7.0.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1507 | FP | FP | 告警点位于switch-case分支内，该分支仅在`link->type == AVMEDIA_TYPE_AUDIO`时执行。在调用`ff_get_audio_buffer`前，函数已通过`av_frame_is_writable(f... |
| 1790 | ffmpeg-7.0.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 代码中`s->buffer`的访问基于`s->index`，但切片未提供`s`或`s->buffer`为空的证据。该函数为内联辅助函数，其调用者通常负责确保上下文有效。结合参考标签为FP，倾向于判定为工具误报。 |
| 1791 | ffmpeg-7.0.1 | asf_parse_packet | Dereference of null pointer | 1306 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data` 之前，已通过 `av_assert0(asf_st)` 断言 `asf_st` 非空，且 `asf_st` 被赋值为 `asf->asf_st`，而 `asf->asf_st`... |
| 1792 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 148 | FP | FP | 切片代码显示，在访问 `alpSrcPtr` 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，当条件不满足时 `alpSrcPtr` 被显式设置为 `NULL`，而后续使用该指针时... |
| 1793 | ffmpeg-7.0.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在告警行 `dp1[pos] = s->tint[0];` 之前，存在条件判断 `if (dpd[pos])`，这确保了 `dpd[pos]` 指针在解引用前已被验证为非零，因此不会发生空指针解引用。 |
| 1795 | ffmpeg-7.0.1 | unsharp_slice_8 | Dereference of null pointer | 142 | FP | FP | 切片代码显示，在宏展开的函数定义中，`src2` 变量被初始化为 NULL，但后续代码中并未对其进行解引用。该变量仅被声明和初始化，未在后续逻辑中使用，因此不存在空指针解引用。 |
| 1796 | ffmpeg-7.0.1 | mov_write_trak_tag | Dereference of null pointer | 3899 | FP | FP | 告警指向的代码行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 中，`st` 指针在函数入口处作为参数传入，并在多个条件分支中被直接使用，切片中未见其可... |
| 1797 | ffmpeg-7.0.1 | ebml_parse | Dereference of null pointer | 1371 | FP | FP | 告警指向的代码行位于条件分支 `else if (level->length != EBML_UNKNOWN_LENGTH)` 中，该分支仅在 `level` 指针非空时才会执行。而 `level` 指针在函数开头被赋值为 `matr... |
| 1798 | ffmpeg-7.0.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码显示，在访问 `dpd[poa]` 和 `dpd[pob]` 之前，已通过条件 `(!i ｜｜ !dpd[poa])` 和 `((i == (out->height - 1)) ｜｜ !dpd[pob])` 进行了边界检查，确... |
| 1799 | ffmpeg-7.0.1 | get_bits_le | Dereference of null pointer | 361 | FP | FP | 切片代码显示告警点位于宏 UPDATE_CACHE_LE 的展开处，该宏及其相关宏（如 OPEN_READER, CLOSE_READER）主要操作结构体指针 's' 的成员。在函数入口处，指针 's' 作为参数传入，其有效性由调用者... |
| 1800 | ffmpeg-7.0.1 | ac3_apply_rematrixing | Dereference of null pointer | 387 | FP | FP | 告警指向的变量 `flags` 在切片代码中未定义，无法确认其来源和值。结合 `label` 为 FP 以及代码上下文（如 `block->num_rematrixing_bands` 控制循环）推断，`flags` 很可能在切片外被... |
| 1801 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 682 | FP | FP | 切片代码显示，在调用FFSWAP宏之前，`ptr1`和`ptr2`都已被正确初始化并指向有效的缓冲区（`q->decoded_bytes_buffer`及其偏移位置），不存在空指针解引用。 |
| 1802 | ffmpeg-7.0.1 | ff_rdt_parse_header | Dereference of null pointer | 201 | FP | FP | 切片代码中，`init_get_bits`函数在`buffer`为NULL时会返回错误并设置`bit_size`为0，后续的`get_bits`等操作会因`size_in_bits`为0而安全返回，且告警点位于while循环的条件检查... |
| 1803 | ffmpeg-7.0.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 函数入口处已对指针 `info` 进行了非空检查，在 `if (info)` 的保护块内才进行解引用和循环，逻辑上避免了空指针解引用。告警点 `av_free(info->key_ids[i])` 的执行前提是 `info` 非空，因... |
| 1804 | ffmpeg-7.0.1 | shift_frame | Dereference of null pointer | 153 | FP | FP | 切片代码显示，告警点引用的 `frame` 变量在函数参数和局部变量中均未定义，这很可能是静态分析工具在解析宏 `av_log`（此处被定义为空操作 `while(0)`）时产生的上下文误解。结合参考标签 FP，判断为工具误报。 |
| 1805 | ffmpeg-7.0.1 | build_table | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功后才... |
| 1806 | ffmpeg-7.0.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], side_data, key_id_size)` 之前，`info->key_ids` 数组及其每个元素 `info->key_ids[j]` 都已在 `av_... |
| 1807 | ffmpeg-7.0.1 | dump_stream_group | Dereference of null pointer | 678 | FP | FP | 切片代码中，告警行 `printed[st->index] = 1;` 位于一个循环内，该循环的条件是 `channel_count > 0 && k < stg->nb_streams`。变量 `st` 是 `const AVStr... |
| 1808 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 168 | FP | FP | 切片代码显示，在解引用 `alpSrcPtr` 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，当条件不满足时 `alpSrcPtr` 被设为 `NULL`，而后续使用 `alpS... |
| 1809 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 658 | FP | FP | 代码切片显示告警点位于宏 UPDATE_CACHE 的调用处，该宏及其展开的 GET_VLC 宏逻辑中均未直接对空指针进行解引用。结合参考标签 FP（告警在后续版本中持续存在），判断为工具误报。 |
| 1810 | ffmpeg-7.0.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在告警行使用 `in->linesize[plane]` 之前，`in` 指针作为函数参数传入且未被修改，且函数逻辑依赖于 `in` 的有效性。此外，`label` 为 FP 也支持此结论。因此，该空指针解引用告警是误报。 |
| 1811 | ffmpeg-7.0.1 | mov_write_trak_tag | Dereference of null pointer | 3904 | FP | FP | 切片代码中，告警行 `is_clcp_track(track) && st->sample_aspect_ratio.num` 在调用 `st->sample_aspect_ratio.num` 前已通过 `if (track->mo... |
| 1812 | ffmpeg-7.0.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警点位于宏 UPDATE_CACHE 的展开处，该宏本身不直接解引用指针。切片代码显示 get_bits 函数是一个经过良好定义的位读取工具函数，其参数 s 在调用上下文中通常有效，且函数末尾有断言检查。结合参考标签 FP（告警在后... |
| 1814 | ffmpeg-7.0.1 | encode_plane | Dereference of null pointer | 291 | FP | FP | 切片代码显示告警点位于数组索引赋值操作，`sample[0]` 已在循环前被正确初始化为指向 `s->sample_buffer` 的有效内存区域，不存在空指针解引用。算法标签也为 FP，进一步支持此结论。 |
| 1815 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 686 | FP | FP | 切片代码中，在警告行 `q->decoded_bytes_buffer[i] = *ptr2--;` 之前，`q->decoded_bytes_buffer` 的初始化或分配未在切片中显示，但告警点位于 `else` 分支，该分支仅在... |
| 1816 | ffmpeg-7.0.1 | decode_frame | Dereference of null pointer | 691 | FP | FP | 切片代码显示，在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确初始化为 `q->decoded_bytes_buffer`，这是一个有效的缓冲区指针。循环内部有边... |
| 1817 | ffmpeg-6.1.1 | show_bits | Dereference of null pointer | 376 | FP | FP | 代码切片中仅展示了宏定义和函数框架，未提供 `GetBitContext *s` 指针的来源和校验上下文。结合参考标签 `label` 为 FP，且告警点位于一个被广泛使用的内联辅助函数中，该函数通常由调用者保证指针有效性，因此倾向于... |
| 1818 | ffmpeg-6.1.1 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 切片代码显示，在调用 `av_rescale` 函数时，其第三个参数 `(uint64_t) s->st->time_base.num << 32` 是一个显式的整数运算结果，不可能为 NULL。该告警是对一个非指针表达式进行空指针解... |
| 1819 | ffmpeg-6.1.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 412 | FP | FP | 切片代码显示，在访问 `ctx->buffers` 或 `ctx->buffers[i]` 之前，存在对 `ctx->buffers` 是否为空的检查（如 `if (!ctx->buffers)`），并且告警行 `avbuf = &c... |
| 1820 | ffmpeg-6.1.1 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | FP | 告警行访问 `frame->pts` 的条件是 `context->input_frames <= 7`，而在此行之前，代码已通过 `if (!in && context->input_frames >= 8) return 0;` ... |
| 1821 | ffmpeg-6.1.1 | ebml_read_binary | Dereference of null pointer | 1087 | FP | FP | 告警点位于对 `bin->buf->data` 的访问，但根据切片中 `av_buffer_realloc` 函数的逻辑，当 `ret >= 0` 时，`bin->buf` 已被成功分配或重新分配，不会为 NULL。因此，在 `mem... |
| 1822 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码中，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被 `av_malloc_array` 分配内存或赋值为 `p->data[0]`，且后续循环条件... |
| 1823 | ffmpeg-6.1.1 | vc1_decode_intra_block | Dereference of null pointer | 964 | FP | FP | 在切片代码中，`dc_val` 指针在函数 `ff_vc1_pred_dc` 中被明确赋值为 `&dc_val[0]`（即 `s->dc_val[0] + s->block_index[n]`），该地址来自结构体成员，不可能为 NUL... |
| 1824 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 切片代码显示，在宏CHECK_BIT中使用'dst'指针前，已通过条件'if (dst)'进行了检查，防止了对空指针的解引用。该告警点位于宏展开内部，但控制流确保了'dst'不为空时才执行解引用操作。 |
| 1825 | ffmpeg-6.1.1 | unsharp_slice_16 | Dereference of null pointer | 141 | FP | FP | 切片代码显示告警点位于宏定义展开的静态函数声明处，该行 `{ NULL }` 是函数体的一部分，并非运行时对空指针的解引用。这是一个宏展开导致的静态分析工具误判，代码本身没有逻辑错误。 |
| 1826 | ffmpeg-6.1.1 | enc_open | Dereference of null pointer | 271 | FP | FP | 切片代码中，在访问 `ost->ist->par` 之前，`ost->ist` 的取值路径未在切片中展示，无法确认其是否为 NULL。但告警点位于 `enc_ctx->width` 被赋值的分支，该分支仅在 `enc_ctx->wid... |
| 1827 | ffmpeg-6.1.1 | ebml_parse | Dereference of null pointer | 1353 | FP | FP | 切片代码中，在警告行（第1353行）使用`level`指针前，已通过`if (matroska->num_levels > 0)`进行了检查，确保了`level`不为NULL。因此，对`level->length`的访问是安全的，不存... |
| 1828 | ffmpeg-6.1.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码中，`UPDATE_CACHE` 宏展开后并未直接解引用传入的 `gb` 指针，且告警行本身是宏调用，不涉及指针解引用。结合 `BITS_AVAILABLE` 宏被定义为常量 1，表明该代码路径可能经过特殊优化或条件编译，工具... |
| 1829 | ffmpeg-6.1.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 代码切片显示，在指针解引用前存在明确的空指针检查（`if (s->buf_end - s->buf_ptr >= sizeof(BitBuf))`），这确保了只有在缓冲区有足够空间时才会执行写入操作，避免了空指针解引用。 |
| 1830 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码显示，`sample[0]` 在循环中被正确赋值，指向 `s->sample_buffer` 的有效偏移地址，该缓冲区已通过 `memset` 初始化，不存在空指针解引用。告警可能是工具对复杂指针运算的误判。 |
| 1831 | ffmpeg-6.1.1 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 切片代码显示，在调用 `av_rescale_q` 之前，已对 `av_packet_new_side_data` 的返回值 `prft` 进行了空指针检查，若为空则提前返回错误。因此，后续使用 `s->st` 和 `s->last_... |
| 1832 | ffmpeg-6.1.1 | ebml_read_sint | Dereference of null pointer | 1014 | FP | FP | 切片代码显示，`avio_r8`函数内部有明确的缓冲区边界检查（`s->buf_ptr >= s->buf_end`）和填充机制，并在指针无效时返回0，这确保了传递给`sign_extend`的参数是安全的，不会导致空指针解引用。 |
| 1833 | ffmpeg-6.1.1 | safe_filename | Dereference of null pointer | 97 | FP | FP | 代码逻辑显示，指针 `f` 在循环条件 `for (; *f; f++)` 中作为字符串指针被解引用，但该解引用发生在对 `f` 的非空检查之后（`*f` 为假时循环终止），因此不会发生空指针解引用。告警是工具对循环条件中解引用操作的误判。 |
| 1834 | ffmpeg-6.1.1 | try_push_frame | Dereference of null pointer | 538 | FP | FP | 告警行访问 `s->input_frames[0]` 前，代码逻辑已确保 `nb_samples` 不为0，这要求至少有一个输入帧存在，因此 `s->input_frames[0]` 不应为空。切片中未见明显的空指针解引用路径。 |
| 1835 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 告警点位于条件赋值语句 `const int linesize = s->planeheight[plane] > 1 ? in->linesize[plane] : 0;`，该语句是安全的。当 `s->planeheight[pla... |
| 1836 | ffmpeg-6.1.1 | ff_encode_encode_cb | Dereference of null pointer | 285 | FP | FP | 告警指向的代码行 `if (frame->duration)` 位于 `if (frame && ...)` 条件块内部，切片代码显示外层已通过 `if (frame)` 对 `frame` 指针进行了非空检查，因此解引用 `fram... |
| 1837 | ffmpeg-6.1.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后对 GetBitContext 指针 's' 进行解引用。在函数入口处，'s' 作为参数传入，切片代码中未见其空值检查。然而，该函数是内联的比特流读取辅助函数，通常在调用前由... |
| 1838 | ffmpeg-6.1.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码中，变量 `dpd` 在条件判断 `if (dpd[pos])` 中被直接使用，但其来源和初始化在切片中不可见。告警点是对 `dpd` 的指针解引用，但切片内没有证据表明 `dpd` 在此处一定为 null。结合算法参考标签 ... |
| 1839 | ffmpeg-6.1.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1476 | FP | FP | 切片代码中，`scale_matrix` 在赋值给 `scale_m` 之前，其值来源于 `sl->sl[...][...]`，且仅在 `s->ps.sps->scaling_list_enable_flag` 为真且特定条件满足时才... |
| 1840 | ffmpeg-6.1.1 | try_push_frame | Dereference of null pointer | 244 | FP | FP | 切片代码显示，`inbuf[0]` 的赋值来自 `ff_inlink_consume_samples` 函数，该函数仅在成功时设置 `*rframe` 并返回1。在调用循环中，`ret` 未被检查，但 `inbuf[i]` 被初始化为... |
| 1841 | ffmpeg-6.1.1 | hls_read_header | Dereference of null pointer | 2123 | FP | FP | 切片代码显示，在访问 `in_fmt->name` 之前，`in_fmt` 已通过 `av_demuxer_iterate` 或 `av_probe_input_buffer` 被正确赋值，且存在空指针检查（如 `if (strstr... |
| 1842 | ffmpeg-6.1.1 | hls_append_segment | Dereference of null pointer | 1173 | FP | FP | 切片代码显示，在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 之前，`en` 被赋值为 `vs->segments`... |
| 1843 | ffmpeg-6.1.1 | concat_parse_script | Dereference of null pointer | 557 | FP | FP | 告警点 `file->user_duration = arg_int[0];` 位于 `case DIR_DURATION:` 分支，该分支仅在 `dir->flags & NEEDS_FILE` 条件满足且 `cat->nb_fil... |
| 1844 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 297 | FP | FP | 切片代码显示，在告警行 `sample[0][x] = ((uint16_t*)(src + stride*y))[x];` 中，`src` 是函数参数，`stride` 和 `y` 是循环变量，指针运算和数组访问均在有效范围内，未发... |
| 1845 | ffmpeg-6.1.1 | kalman_smoothen | Dereference of null pointer | 584 | FP | FP | 代码逻辑确保了`best_hist_ptr`在解引用前已被赋值。`optimal_gain`初始为0，`best_hist_ptr`初始为NULL。在循环中，只有当`dot > optimal_gain`（即`dot > 0`）时，`... |
| 1846 | ffmpeg-6.1.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在告警行`dp1[pos] = s->tint[0];`之前，存在条件判断`if (dpd[pos])`，这确保了`dpd[pos]`不为零，从而间接保证了`dp1`和`dp2`指针的有效性，因为它们在同一个循环和条件下... |
| 1847 | ffmpeg-6.1.1 | id3v2_parse | Dereference of null pointer | 1054 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 函数获取的，该函数仅在找到匹配的标签时才返回非空指针。告警点位于 `else` 分支，该分... |
| 1848 | ffmpeg-6.1.1 | choose_rct_params | Dereference of null pointer | 983 | FP | FP | 切片代码显示告警行访问的 src[1] 和 src[2] 是函数参数，在切片范围内没有证据表明它们可能为 NULL。函数逻辑在 else 分支中对称地使用 src[0]、src[1]、src[2]，若 src[0] 非空，则 src[... |
| 1849 | ffmpeg-6.1.1 | split_commandline | Dereference of null pointer | 731 | FP | FP | 告警行检查的是 `opt[2]`，但该行仅在 `opt[0] == '-' && opt[1] == '-'` 条件下执行，此时 `opt` 至少指向一个以 "--" 开头的字符串，`opt[2]` 访问是安全的。切片中未发现空指针解... |
| 1850 | ffmpeg-6.1.1 | ebml_read_ascii | Dereference of null pointer | 1069 | FP | FP | 切片代码显示 `av_free` 被定义为 `while(0)` 宏，这是一个空操作，不会发生对空指针的解引用。同时，`av_malloc` 被定义为返回 `NULL`，但告警点 `av_free(*str)` 的解引用风险被宏定义消... |
| 1851 | ffmpeg-6.1.1 | output_packet | Dereference of null pointer | 1102 | FP | FP | 在访问 `timestamp_packet->unwritten_size` 之前，代码已通过 `if (timestamp_packet)` 检查了指针非空，因此不会发生空指针解引用。告警是误报。 |
| 1852 | ffmpeg-6.1.1 | ebml_read_uint | Dereference of null pointer | 994 | FP | FP | 切片代码显示，在指针解引用前，函数参数 `num` 已通过 `*num = default_value;` 或 `*num = 0;` 进行了赋值，这表明 `num` 是一个有效的指针，解引用操作是安全的。告警源于对控制流和数据流的误判。 |
| 1853 | ffmpeg-6.1.1 | concat_parse_script | Dereference of null pointer | 561 | FP | FP | 告警点位于 `case DIR_INPOINT: file->inpoint = arg_int[0];`，但切片代码显示，该分支仅在 `dir->flags & NEEDS_FILE` 条件满足且 `cat->nb_files` 不... |
| 1854 | ffmpeg-6.1.1 | ost_add | Dereference of null pointer | 1456 | FP | FP | 切片代码中，在访问 `ist->st->duration` 之前，已经通过条件 `if (ost->ist && ost->ist->st->duration > 0)` 检查了 `ost->ist` 和 `ost->ist->st`... |
| 1855 | ffmpeg-6.1.1 | sb_decode | Dereference of null pointer | 1346 | FP | FP | 在访问 `innov_save` 指针前，代码已通过 `if (st->innov_save)` 检查其非空，且 `innov_save` 被赋值为 `st->innov_save + 2 * offset`，该指针源自已验证的非空指... |
| 1856 | ffmpeg-6.1.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警指向的代码行位于条件 `if ((*child)->state * 2 == -t->state)` 内部，该条件仅在 `t->state` 非零且 `t->state` 为偶数（`!(t->state & 1)`）时才会被评估。... |
| 1857 | ffmpeg-6.1.1 | check_header_mismatch | Dereference of null pointer | 520 | FP | FP | 切片代码显示，在访问 `header->link_penalty[i]` 之前，变量 `i` 由 `for` 循环控制，其值在循环结束后为 `FLAC_MAX_SEQUENTIAL_HEADERS` 或当 `curr == child... |
| 1858 | ffmpeg-6.1.1 | get_pict_type | Dereference of null pointer | 135 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效性，确保 `unit->content`... |
| 1859 | ffmpeg-6.1.1 | ogg_write_header | Dereference of null pointer | 628 | FP | FP | 切片代码显示告警行是对结构体成员的直接赋值，而非对指针进行解引用操作，不存在空指针解引用风险。参考标签也为FP，进一步支持误报结论。 |
| 1860 | ffmpeg-6.1.1 | mpegts_open_filter | Dereference of null pointer | 493 | FP | FP | 告警指向的 `av_log` 调用已被宏定义为空操作 `while(0)`，因此不会发生空指针解引用。代码逻辑安全，属于静态分析工具对宏展开的误判。 |
| 1861 | ffmpeg-6.1.1 | guess_mv | Dereference of null pointer | 428 | FP | FP | 切片代码中，在警告行（else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])）访问 s->last_pic.f->data[0] 之前，已经存在条件判断 `if (s-... |
| 1862 | ffmpeg-6.1.1 | fg_output_frame | Dereference of null pointer | 2111 | FP | FP | 告警指向的代码行 `frame->pts = (frame->pts == AV_NOPTS_VALUE) ? ofp->next_pts : ...` 位于 `type != AVMEDIA_TYPE_VIDEO` 的分支中，该分支... |
| 1863 | ffmpeg-6.1.1 | build_table | Dereference of null pointer | 204 | FP | FP | 切片代码显示，在访问 table[j] 之前，table 指针已通过 table = &vlc->table[table_index]; 正确初始化，且 table_index 在 alloc_table 成功后才被使用。代码逻辑确保... |
| 1864 | ffmpeg-6.1.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在告警行 `AVChapter *chp = chapters[i];` 之前，存在条件 `if (chapters && nb_chapters)` 和 `for (int i = 0; i < nb_chapters... |
| 1865 | ffmpeg-6.1.1 | locate_option | Dereference of null pointer | 424 | FP | FP | 在调用 `po->name` 之前，`po` 指针由 `find_option` 函数返回，该函数在遍历选项数组时，仅在 `po->name` 为真时循环并递增指针，最终返回的指针指向一个数组元素。虽然 `find_option` 可... |
| 1866 | ffmpeg-6.1.1 | guess_status_pts | Dereference of null pointer | 462 | FP | FP | 告警指向的指针访问 `ctx->inputs[i]` 发生在 `for` 循环内，循环条件 `i < ctx->nb_inputs` 确保了 `i` 是有效索引。在FFmpeg的AVFilterContext结构中，`inputs` ... |
| 1867 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警点位于对 `in->data[plane]` 的强制类型转换，但切片代码显示 `in` 是函数参数且非空，且其数据指针 `data[plane]` 在后续循环中被直接使用，表明其已被正确初始化。结合 `label` 为 FP，判定... |
| 1868 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 332 | FP | FP | 告警行 `new_pts = av_rescale_q(...)` 仅在 `if (s->do_video)` 条件为真时执行，而该条件块内已通过 `outlink = s->do_video ? ctx->outputs[1] : ... |
| 1869 | ffmpeg-6.1.1 | av_dump_format | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `printed` 数组前，已通过条件 `if (ic->nb_streams && !printed) return;` 确保当 `ic->nb_streams` 非零且 `printed` 为 NULL 时函... |
| 1870 | ffmpeg-6.1.1 | check_header_mismatch | Dereference of null pointer | 476 | FP | FP | 切片代码中，在访问 `curr->link_penalty[i]` 之前，`curr` 变量通过 `while (curr != child)` 循环进行遍历，且 `curr` 初始化为非空的 `header` 参数，因此 `curr... |
| 1871 | ffmpeg-6.1.1 | update_context_from_thread | Dereference of null pointer | 366 | FP | FP | 切片代码中，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 进行了条件检查，并且 `hwacce... |
| 1872 | ffmpeg-6.1.1 | choose_rct_params | Dereference of null pointer | 984 | FP | FP | 切片代码显示，在访问 `src[2]` 指针前，函数已通过 `for (p = 0; p < 3; p++)` 循环对 `src` 数组进行了使用，且 `src` 作为参数传入，在切片上下文中没有证据表明其为空。告警点 `r = *(... |
| 1873 | ffmpeg-6.1.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 代码切片显示，在调用UPDATE_CACHE_32等宏之前，已通过OPEN_READER宏初始化了读取器，并且告警点位于一个经过充分验证的位读取函数内部。该函数有严格的输入断言（av_assert2），且是处理标准位流的通用函数，在正... |
| 1874 | ffmpeg-6.1.1 | activate | Dereference of null pointer | 186 | FP | FP | 告警点位于 `frame->pts = s->pts;`，但切片代码显示，在到达该行之前，`frame` 指针要么通过 `ff_get_video_buffer` 成功分配，要么通过 `av_frame_clone` 成功克隆，两者失... |
| 1875 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 199 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被 `av_malloc_array` 分配内存或指向 `p->data[0]`，且后续循环条件... |
| 1876 | ffmpeg-6.1.1 | h264_field_start | Dereference of null pointer | 1426 | FP | FP | 告警点位于对 `sps->log2_max_frame_num` 的访问，但切片代码显示 `sps` 指针在访问前已通过 `h264_init_ps` 函数初始化，且该函数在 `ret < 0` 时会提前返回，确保了 `sps` 的有... |
| 1877 | ffmpeg-6.1.1 | ff_encode_encode_cb | Dereference of null pointer | 282 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，该行代码 `avpkt->pts = frame->pts;` 仅在 `frame` 指针非空时才会执行。切片代码显示，该行代码位于一个... |
| 1878 | ffmpeg-6.1.1 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，代码已通过 `if (!buf)` 和 `if (len < 12)` 进行了检查。当 `buf` 为 NULL 或 `len`... |
| 1879 | ffmpeg-6.1.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，`dpd` 指针已通过三元条件运算符赋值，其来源为 `out->data[s->pd]` 或 `out->data[0]`。`out` 是函数参数，且 `data` 数组在FFmpeg... |
| 1880 | ffmpeg-6.1.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1442 | FP | FP | 告警点位于 `ff_get_audio_buffer(link, frame->nb_samples)` 调用，其中 `frame` 指针在函数开头已通过 `AVFrame *frame = *rframe;` 获取，并在调用前已通过... |
| 1881 | ffmpeg-6.1.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 代码中`s->buffer`的访问基于`s->index`，但切片未提供`s`或`s->buffer`为空的证据。该函数为内联辅助函数，其调用者应确保上下文有效。结合参考标签，倾向于判定为工具误报。 |
| 1882 | ffmpeg-6.1.1 | asf_parse_packet | Dereference of null pointer | 1306 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data` 之前，已通过 `av_assert0(asf_st)` 断言 `asf_st` 非空，并且 `asf_st` 被赋值为 `asf->asf_st`，而 `asf->asf_st... |
| 1883 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 148 | FP | FP | 切片代码显示，对 `alpSrcPtr` 的赋值和使用都受到 `CONFIG_SWSCALE_ALPHA && hasAlpha` 条件的保护。在告警行，该条件已确保 `alpSrcPtr` 不为 NULL 时才进行解引用，因此不会发... |
| 1884 | ffmpeg-6.1.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在告警行 `dp1[pos] = s->tint[0];` 之前，存在条件判断 `if (dpd[pos])`，这确保了指针 `dpd` 在解引用前已被验证为非空，因此不会发生空指针解引用。 |
| 1885 | ffmpeg-6.1.1 | avc_parse_nal_units | Dereference of null pointer | 92 | FP | FP | 告警指向的代码行 `list->nb_nalus >= nalu_limit` 中，`list` 指针在函数入口处未被验证为空，但切片代码显示，该行位于 `if (pb)` 和 `else if` 的条件分支中，且 `list` 仅在... |
| 1886 | ffmpeg-6.1.1 | unsharp_slice_8 | Dereference of null pointer | 142 | FP | FP | 切片代码显示，宏定义 `DEF_UNSHARP_SLICE_FUNC` 在展开后，告警行 `{ NULL }` 是函数体的一部分，但该函数体在宏展开后已被完整的实现代码所替代，因此不存在对空指针的解引用。这是一个由宏展开导致的静态分析... |
| 1887 | ffmpeg-6.1.1 | mov_write_trak_tag | Dereference of null pointer | 3818 | FP | FP | 告警指向的代码行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 中，`st` 是函数参数，在切片代码的调用上下文中（如 `mov_write_tkhd_... |
| 1888 | ffmpeg-6.1.1 | ebml_parse | Dereference of null pointer | 1370 | FP | FP | 告警行位于条件分支 `else if (level->length != EBML_UNKNOWN_LENGTH)` 内部，该分支仅在 `level` 指针非空时才会被评估。切片代码显示，在进入此分支前，`level` 指针已通过 `... |
| 1889 | ffmpeg-6.1.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码显示，对数组`dpd`的访问均在有效的边界检查（如`!j`、`j == (out->width - 1)`、`!i`、`i == (out->height - 1)`）保护之下，不会发生越界或空指针解引用。算法参考标签也为FP... |
| 1890 | ffmpeg-6.1.1 | get_bits_le | Dereference of null pointer | 361 | FP | FP | 告警指向宏展开的代码行，但切片代码显示该函数为内联工具函数，其参数`s`在调用上下文中通常由调用者保证非空。宏`UPDATE_CACHE_LE`展开后涉及指针访问，但函数本身逻辑正确，且参考标签为FP，表明开发者未将其视为需要修复的问... |
| 1891 | ffmpeg-6.1.1 | ac3_apply_rematrixing | Dereference of null pointer | 411 | FP | FP | 切片代码中，`flags` 变量未定义，无法确认其来源和值，无法判断其是否为 null。结合参考标签 `label` 为 FP，且告警为逻辑错误而非明确的空指针解引用，倾向于判定为误报。 |
| 1892 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 682 | FP | FP | 告警指向的FFSWAP宏操作的是明确初始化的局部指针变量ptr1和ptr2，在切片代码的可见上下文中，这两个指针在解引用前已被正确赋值，不存在空指针解引用风险。 |
| 1893 | ffmpeg-6.1.1 | ff_rdt_parse_header | Dereference of null pointer | 200 | FP | FP | 切片代码中，`init_get_bits`函数在传入的`buffer`（即`buf`）为NULL时会返回错误并设置`s->buffer = NULL`，但后续的`get_bits1`等函数在`UNCHECKED_BITSTREAM_R... |
| 1894 | ffmpeg-6.1.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 代码在访问 `info->key_ids[i]` 之前，已通过 `if (info)` 检查了指针 `info` 非空，且循环条件 `i < info->num_key_ids` 确保了 `info->key_ids` 数组访问在边界... |
| 1895 | ffmpeg-6.1.1 | shift_frame | Dereference of null pointer | 153 | FP | FP | 切片代码显示，告警点引用的变量 `frame` 在上下文中未定义，这很可能是由于切片不完整或宏定义导致的静态分析工具误判。同时，参考标签 `label` 为 FP，表明该告警在后续版本中未被修复，进一步支持其为误报的结论。 |
| 1896 | ffmpeg-6.1.1 | build_table | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 1897 | ffmpeg-6.1.1 | ff_inlink_evaluate_timeline_at_frame | Dereference of null pointer | 1485 | FP | FP | 切片代码中，`frame` 指针作为函数参数被直接解引用以获取 `pts`，这是访问结构体成员的正常操作。没有证据表明 `frame` 在此上下文中为 NULL，且告警规则 `Dereference of null pointer` ... |
| 1898 | ffmpeg-6.1.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], side_data, key_id_size)` 之前，`info->key_ids` 数组及其每个元素 `info->key_ids[j]` 已在 `av_e... |
| 1899 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 168 | FP | FP | 代码在访问 `alpSrcPtr` 前已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，当条件不满足时 `alpSrcPtr` 被初始化为 `NULL`，且后续使用 `alpSrcPtr`... |
| 1900 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该宏最终展开为 UPDATE_CACHE_LE，其具体实现未在切片中给出。结合该函数是FFmpeg核心解码函数且广泛使用，以及算法标签为FP，推断该告警为工具对宏展开的误判，... |
| 1901 | ffmpeg-6.1.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在深度大于8的分支中，`linesize`的计算使用了三元运算符，当`s->planeheight[plane] > 1`为假时，`linesize`被赋值为0。后续循环中`val`和`dst`的指针运算`val += ... |
| 1902 | ffmpeg-6.1.1 | mov_write_trak_tag | Dereference of null pointer | 3823 | FP | FP | 告警指向的代码行 `is_clcp_track(track) && st->sample_aspect_ratio.num` 中，`st` 指针已在函数入口作为参数传入，并在多处被安全使用。切片代码中未见任何可能导致 `st` 为空的... |
| 1903 | ffmpeg-6.1.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警点位于宏 UPDATE_CACHE 内部，其展开后涉及对指针 s 的访问。但函数 get_bits 的入参 s 在切片中未显示为空值来源，且该函数是内联工具函数，通常由调用方保证指针有效性。结合 label 为 FP，倾向于判定为... |
| 1904 | ffmpeg-6.1.1 | <global> | Dereference of null pointer | 471 | FP | FP | 切片代码显示，`DECODE_CODEWORD` 是一个宏，其内部包含 `UPDATE_CACHE` 和 `GET_CACHE` 操作，这些操作通常用于从比特流中安全读取数据，不会返回空指针。告警点是对宏的调用，而非直接解引用一个明确... |
| 1905 | ffmpeg-6.1.1 | encode_plane | Dereference of null pointer | 291 | FP | FP | 切片代码显示，`sample[0]` 在循环前已通过 `sample[i] = s->sample_buffer + ...` 被正确初始化并指向有效的缓冲区，不存在空指针解引用。告警可能是工具对数组指针运算的误判。 |
| 1906 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 686 | FP | FP | 切片代码中，在警告行（`q->decoded_bytes_buffer[i] = *ptr2--;`）之前，`q->decoded_bytes_buffer` 已在 `else` 分支的父级 `if` 条件 `js_databuf =... |
| 1907 | ffmpeg-6.1.1 | decode_frame | Dereference of null pointer | 691 | FP | FP | 切片代码显示，在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确初始化为 `q->decoded_bytes_buffer`，这是一个有效的缓冲区指针。循环条件 `... |
| 1908 | ffmpeg-7.1 | show_bits | Dereference of null pointer | 376 | FP | FP | 告警指向宏展开的内部操作，`UPDATE_CACHE` 宏调用本身不直接解引用空指针。切片代码显示 `s` 作为参数传入，但未提供其来源，无法确认其为空。结合参考标签 `label` 为 FP，倾向于判定为工具对宏展开的误报。 |
| 1909 | ffmpeg-7.1 | finalize_packet | Dereference of null pointer | 678 | FP | FP | 告警点位于 `av_rescale` 函数的参数位置，该参数 `s->st->time_base.num` 被显式转换为 `uint64_t` 后左移32位，确保了除数非零。切片代码中 `s->st` 指针虽未显式校验，但该函数仅在 ... |
| 1910 | ffmpeg-7.1 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 413 | FP | FP | 切片代码显示，在访问 `ctx->buffers` 数组前，存在对 `ctx->buffers` 是否为空的检查（`if (!ctx->buffers) break;`），并且 `avbuf = &ctx->buffers[buf.i... |
| 1911 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 299 | FP | FP | 切片代码显示，在调用 `encode_line` 函数前，`sample[0]` 指针已在循环中被明确赋值，指向 `sc->sample_buffer` 中的有效内存区域，不存在空指针解引用。告警可能是工具对指针运算的误判。 |
| 1912 | ffmpeg-7.1 | roq_dpcm_encode_frame | Dereference of null pointer | 180 | FP | FP | 告警行访问 `frame->pts` 的条件是 `context->input_frames <= 7`，结合切片逻辑，当 `frame` 为 NULL 时，`in` 也为 NULL，此时 `context->input_frames... |
| 1913 | ffmpeg-7.1 | ebml_read_binary | Dereference of null pointer | 1095 | FP | FP | 被调用的函数 `av_buffer_realloc` 在成功时保证 `*pbuf`（即 `bin->buf`）非空，且切片代码中 `ret < 0` 的检查确保了只有在成功时才会执行后续的 `memset` 操作，因此不会发生空指针解引用。 |
| 1914 | ffmpeg-7.1 | <global> | Dereference of null pointer | 209 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已通过 `av_malloc_array` 分配内存，且分配失败时函数会提前返回，因此不会发生空指针解引用。 |
| 1915 | ffmpeg-7.1 | vc1_decode_intra_block | Dereference of null pointer | 949 | FP | FP | 切片代码显示，`dc_val` 作为指针参数传入 `ff_vc1_pred_dc` 函数，该函数负责为其赋值。在调用 `ff_vc1_pred_dc` 后，`dc_val` 应已被初始化为有效指针，因此后续的 `*dc_val = d... |
| 1916 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 118 | FP | FP | 告警点位于宏展开内部，但切片代码显示变量`val`在解引用前已从`in->data[plane]`正确赋值，且`in`指针在函数入口非空。宏`CHECK_BIT`中对`val`的访问是安全的，不存在解引用空指针的逻辑。 |
| 1917 | ffmpeg-7.1 | unsharp_slice_16 | Dereference of null pointer | 172 | FP | FP | 告警指向的宏定义行 `DEF_UNSHARP_SLICE_FUNC(unsharp_slice, 16)` 本身是函数声明，不会直接解引用空指针。切片代码中未显示任何对空指针的实际解引用操作，且宏展开后的函数逻辑包含空值检查（如 `i... |
| 1918 | ffmpeg-7.1 | ebml_parse | Dereference of null pointer | 1363 | FP | FP | 切片代码显示，在访问 `level->length` 之前，存在条件 `matroska->num_levels > 0` 确保 `level` 指针非空。告警点 `level->length` 位于该条件保护的分支内，因此不会发生空... |
| 1919 | ffmpeg-7.1 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 告警指向的 `UPDATE_CACHE` 是一个宏，其展开不涉及指针解引用。切片代码中未发现对空指针的直接解引用操作，且 `label` 为 FP 也支持此结论。 |
| 1920 | ffmpeg-7.1 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 切片代码中，对指针`s`的访问发生在函数参数接收之后，且函数内部逻辑是常规的位操作，没有证据表明`s`在函数入口处为NULL。该告警很可能是工具对函数内部分支路径的误判。 |
| 1921 | ffmpeg-7.1 | rtp_set_prft | Dereference of null pointer | 646 | FP | FP | 切片代码显示，在调用 `av_rescale_q` 之前，已对 `av_packet_new_side_data` 的返回值 `prft` 进行了空指针检查，若为空则直接返回错误，因此后续对 `s->st` 的访问不会在 `prft`... |
| 1922 | ffmpeg-7.1 | ebml_read_sint | Dereference of null pointer | 1022 | FP | FP | 切片代码显示，`avio_r8`函数内部有缓冲区边界检查，当`buf_ptr >= buf_end`时会调用`fill_buffer`，且最终会返回0而非导致空指针解引用。告警点`sign_extend(avio_r8(pb), 8)... |
| 1923 | ffmpeg-7.1 | safe_filename | Dereference of null pointer | 98 | FP | FP | 代码逻辑显示，在解引用指针 `f` 之前，循环条件 `for (; *f; f++)` 已经确保了 `f` 指向的字符不为空（即 `*f` 不为 '\0'），因此不会发生空指针解引用。该告警是工具对循环条件判断的逻辑误报。 |
| 1924 | ffmpeg-7.1 | try_push_frame | Dereference of null pointer | 512 | FP | FP | 告警行 `frame->pts = s->input_frames[0]->pts;` 在切片上下文中是安全的。因为前面的 `if (!nb_samples) goto eof;` 确保了 `nb_samples` 不为0，而 `nb... |
| 1925 | ffmpeg-7.1 | dump_stream_group | Dereference of null pointer | 788 | FP | FP | 切片代码显示，在访问 `stg->streams[i]` 之前，存在对 `stg->nb_streams` 的检查（`if (avctx && stg->nb_streams && ...)`），并且循环 `for (int i = ... |
| 1926 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 116 | FP | FP | 告警点位于条件赋值语句 `const int linesize = s->planeheight[plane] > 1 ? in->linesize[plane] : 0;`，当 `s->planeheight[plane] > 1`... |
| 1927 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 236 | FP | FP | 告警点位于 `av_assert0` 宏内部，该宏用于开发调试，在条件不满足时会调用 `abort()` 终止程序，这属于主动的断言检查而非意外的空指针解引用。切片代码中未见 `frame` 为空时会导致解引用 `frame->for... |
| 1928 | ffmpeg-7.1 | ff_encode_encode_cb | Dereference of null pointer | 275 | FP | FP | 告警指向的代码行 `if (frame->duration)` 位于 `if (frame && ...)` 条件块内部，切片代码显示外层已通过 `if (frame)` 对 `frame` 指针进行了非空检查，因此解引用 `fram... |
| 1929 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 219 | FP | FP | 告警点位于 `av_assert0` 宏内，该宏用于开发调试，在条件不满足时会调用 `abort()` 终止程序，这属于主动的断言失败而非意外的空指针解引用。切片代码显示该断言用于验证编码器初始化时的音频帧参数，是预期的安全检查逻辑。 |
| 1930 | ffmpeg-7.1 | get_sbits | Dereference of null pointer | 325 | FP | FP | 代码切片显示告警点位于宏 `UPDATE_CACHE` 的展开处，该宏及其相关宏（如 `OPEN_READER`）的操作对象是结构体指针 `s`。在函数入口处，`s` 作为参数传入，切片中未显示其来源，但函数内部逻辑是标准的位读取操作... |
| 1931 | ffmpeg-7.1 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码中，变量 `dpd` 在条件判断 `if (dpd[pos])` 中被直接使用，但其来源和初始化在切片中不可见。告警指此处可能解引用空指针。然而，`dpd` 很可能是一个有效的数组指针（例如来自 `out->data[0]`）... |
| 1932 | ffmpeg-7.1 | try_push_frame | Dereference of null pointer | 241 | FP | FP | 切片代码显示，在解引用 `inbuf[0]` 之前，`ff_inlink_consume_samples` 函数可能返回0或1，但 `inbuf` 数组已初始化为 `{ NULL }`，且告警行 `outbuf->pts = inbu... |
| 1933 | ffmpeg-7.1 | hls_append_segment | Dereference of null pointer | 1183 | FP | FP | 告警行代码 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 位于 `if (hls->max_nb_segments && v... |
| 1934 | ffmpeg-7.1 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 在DIR_DURATION指令处理前，代码已通过DIR_FILE指令调用add_file函数初始化了file指针，且该函数在成功时会将*rfile指向有效的ConcatFile结构体。因此，当执行到`file->user_durati... |
| 1935 | ffmpeg-7.1 | dump_argument | Dereference of null pointer | 516 | FP | FP | 函数参数 `a` 在循环条件 `for (p = a; *p; p++)` 中被直接解引用，这暗示调用者必须传递一个有效的非空字符串。虽然切片内未显示调用点，但函数逻辑假设 `a` 非空，且 `label` 为 FP 表明该告警在后续... |
| 1936 | ffmpeg-7.1 | kalman_smoothen | Dereference of null pointer | 585 | FP | FP | 代码逻辑确保了`best_hist_ptr`在解引用前已被赋值。`optimal_gain`初始为0，`best_hist_ptr`初始为NULL。在循环中，只有当`dot > optimal_gain`（即`dot > 0`）时，`... |
| 1937 | ffmpeg-7.1 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码中，在访问 `dp1[pos]` 和 `dp2[pos]` 之前，存在条件 `if (dpd[pos])` 进行空指针检查，这确保了 `dpd` 指针的有效性。虽然 `dp1` 和 `dp2` 的定义未在切片中明确显示，但根据... |
| 1938 | ffmpeg-7.1 | id3v2_parse | Dereference of null pointer | 1055 | FP | FP | 切片代码显示，在调用 `extra_func->read` 之前，`extra_func` 是通过 `get_extra_meta_func` 获取的，该函数仅在找到匹配的tag时才返回非空指针。告警点位于 `extra_func->... |
| 1939 | ffmpeg-7.1 | set_bframe_chain_length | Dereference of null pointer | 1590 | FP | FP | 告警指向的代码行 `s->input_picture[i - 1]->f->data[0]` 在切片上下文中，其访问发生在 `for (i = 1; i < s->max_b_frames + 1; i++)` 循环内，且循环体内部有... |
| 1940 | ffmpeg-7.1 | split_commandline | Dereference of null pointer | 809 | FP | FP | 告警点位于检查字符串是否为双破折号'--'的逻辑，代码已通过`opt[0] == '-' && opt[1] == '-'`确保指针`opt`非空且长度至少为2，然后才检查`!opt[2]`。切片中未见空指针解引用风险，属于静态分析工... |
| 1941 | ffmpeg-7.1 | ebml_read_ascii | Dereference of null pointer | 1077 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 1942 | ffmpeg-7.1 | output_packet | Dereference of null pointer | 1103 | FP | FP | 切片代码显示，在访问 `timestamp_packet` 指针之前，`best_i` 已通过循环被赋值为非负值，且 `timestamp_packet` 被赋值为 `stream->premux_packet`。虽然 `stream... |
| 1943 | ffmpeg-7.1 | enc_open | Dereference of null pointer | 286 | FP | FP | 告警指向的代码行 `enc_ctx->width = ost->ist->par->width;` 位于 `switch (enc_ctx->codec_type)` 的 `AVMEDIA_TYPE_SUBTITLE` 分支内，且该赋... |
| 1944 | ffmpeg-7.1 | ebml_read_uint | Dereference of null pointer | 1002 | FP | FP | 切片代码显示，在指针 `num` 被解引用之前，函数入口处没有对 `num` 进行空指针检查。然而，该告警指向的代码行 `*num = 0;` 是在 `if (size == 0)` 分支之后，该分支已对 `num` 进行了解引用 `... |
| 1945 | ffmpeg-7.1 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 告警指向的代码行 `file->inpoint = arg_int[0];` 位于 `case DIR_INPOINT:` 分支，该分支仅在 `dir->flags & NEEDS_FILE` 条件满足且 `cat->nb_files... |
| 1946 | ffmpeg-7.1 | sb_decode | Dereference of null pointer | 1348 | FP | FP | 告警点位于对 `innov_save` 指针的写入操作，但在切片代码中，该指针仅在 `if (st->innov_save)` 条件为真时被赋值和使用，且赋值前已通过 `SPEEX_MEMSET` 进行初始化，不存在对空指针的解引用风险。 |
| 1947 | ffmpeg-7.1 | choose_rct_params | Dereference of null pointer | 990 | FP | FP | 切片代码显示告警行访问的 `src[1]` 和 `src[2]` 是函数参数，在 `lbd` 为假的分支中，其作为指针被解引用。虽然切片未直接展示调用上下文，但函数逻辑是连贯的像素处理循环，且算法参考标签为 FP，表明在后续版本中此模... |
| 1948 | ffmpeg-7.1 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警行位于条件 `if ((*child)->state * 2 == -t->state)` 内，该条件仅在 `t->state` 非零且 `t->state` 为偶数（`!(t->state & 1)`）时才会被评估。进入此分支前... |
| 1949 | ffmpeg-7.1 | check_header_mismatch | Dereference of null pointer | 519 | FP | FP | 切片代码中，在警告行 `curr = curr->next;` 之前，循环条件 `curr != child` 和 `i < FLAC_MAX_SEQUENTIAL_HEADERS` 共同保证了 `curr` 不为空。此外，紧随其后的... |
| 1950 | ffmpeg-7.1 | get_pict_type | Dereference of null pointer | 136 | FP | FP | 切片代码显示，在访问 `slice->header.sh_slice_type` 之前，已通过 `IS_H266_SLICE(unit->type)` 宏检查了 `unit->type` 的有效范围，这确保了 `unit->conte... |
| 1951 | ffmpeg-7.1 | ogg_write_header | Dereference of null pointer | 629 | FP | FP | 切片代码显示告警点是对结构体成员的直接赋值，而非对空指针的解引用。变量 `oggstream` 的来源和空值检查不在切片内，但根据赋值操作的上下文和参考标签，这很可能是一个工具误判的逻辑错误。 |
| 1952 | ffmpeg-7.1 | mpegts_open_filter | Dereference of null pointer | 495 | FP | FP | 切片代码显示，在调用av_log时，其第一个参数`ts->stream`的指针有效性已由函数入口处的`if (pid >= NB_PID_MAX ｜｜ ts->pids[pid])`条件间接保证，因为`ts`作为非空指针传入，且后续逻... |
| 1953 | ffmpeg-7.1 | guess_mv | Dereference of null pointer | 432 | FP | FP | 切片代码中，在告警行（第432行）使用`s->last_pic.f->data[0]`之前，存在明确的条件检查`if (s->last_pic.f && s->last_pic.f->data[0])`，这确保了指针的有效性。因此，该... |
| 1954 | ffmpeg-7.1 | build_table | Dereference of null pointer | 204 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 1955 | ffmpeg-7.1 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在告警行 `AVChapter *chp = chapters[i];` 之前，存在条件 `if (chapters && nb_chapters)` 和 `for (int i = 0; i < nb_chapters... |
| 1956 | ffmpeg-7.1 | locate_option | Dereference of null pointer | 495 | FP | FP | 在调用 `po->name` 之前，`po` 已通过 `find_option` 函数返回，该函数保证返回一个有效的 `OptionDef` 指针（即使未找到匹配项，也返回指向数组末尾哨兵元素的指针，其 `name` 字段为 NULL... |
| 1957 | ffmpeg-7.1 | <global> | Dereference of null pointer | 78 | FP | FP | 代码切片显示，在非CACHED_BITSTREAM_READER分支中，UPDATE_CACHE是一个宏，其展开不涉及对空指针的解引用。告警点位于宏调用处，而宏定义和上下文未显示gb指针为空或会被解引用。结合算法标签为FP，倾向于判定... |
| 1958 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 147 | FP | FP | 告警点位于对 `in->data[plane]` 的赋值，切片代码显示 `in` 是函数参数且已在多个地方被安全解引用，其来源 `filter_frame` 是框架回调，`in` 为 NULL 的可能性极低。结合算法标签为 FP，倾向... |
| 1959 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 333 | FP | FP | 告警行代码 `new_pts = av_rescale_q(in->pts, inlink->time_base, outlink->time_base);` 位于 `if (s->do_video)` 条件块内，而 `outlink... |
| 1960 | ffmpeg-7.1 | av_dump_format | Dereference of null pointer | 898 | FP | FP | 切片代码显示，在访问 `printed` 数组前，已通过条件 `if (ic->nb_streams && !printed) return;` 确保当 `ic->nb_streams` 非零时 `printed` 指针非空。后续访问... |
| 1961 | ffmpeg-7.1 | check_header_mismatch | Dereference of null pointer | 475 | FP | FP | 告警指向的代码行 `curr->link_penalty[i]` 中，`curr` 变量在 while 循环中通过 `curr = curr->next;` 遍历链表，其值来自参数 `header`，且循环条件 `curr != ch... |
| 1962 | ffmpeg-7.1 | update_context_from_thread | Dereference of null pointer | 438 | FP | FP | 切片代码中，在访问 `hwaccel->priv_data_size` 之前，已通过 `if (p_src->hwaccel_threadsafe)` 和 `if (!dst->hwaccel)` 进行了条件检查，并且 `hwacce... |
| 1963 | ffmpeg-7.1 | get_bits_long | Dereference of null pointer | 433 | FP | FP | 告警指向的宏 `UPDATE_CACHE_32` 展开后是对结构体指针 `gb` 的成员访问，但调用前已通过 `OPEN_READER` 宏确保指针有效，且函数入口有 `av_assert2` 断言。切片代码中未显示指针可能为空的路径... |
| 1964 | ffmpeg-7.1 | activate | Dereference of null pointer | 186 | FP | FP | 在告警行（frame->pts = s->pts;）之前，代码已通过条件分支（s->stop_mode == MODE_ADD 或 MODE_CLONE）确保了frame指针非空。在MODE_ADD分支中，ff_get_video_b... |
| 1965 | ffmpeg-7.1 | <global> | Dereference of null pointer | 200 | FP | FP | 告警指向的代码行 `ptr[8*x] = ptr2[x] >> 7;` 位于一个受 `if (depth == 1)` 条件保护的代码块内，且 `ptr2` 在之前的逻辑中已通过 `av_malloc_array` 分配内存，分配失败... |
| 1966 | ffmpeg-7.1 | check_available | Dereference of null pointer | 616 | FP | FP | 切片代码显示，在访问 `TAB_MVF(n->x, n->y).pred_flag` 之前，已通过 `is_available(fc, n->x, n->y)` 函数检查了坐标 `(n->x, n->y)` 的有效性，这很可能确保了后... |
| 1967 | ffmpeg-7.1 | ff_encode_encode_cb | Dereference of null pointer | 272 | FP | FP | 在告警行`avpkt->pts = frame->pts;`之前，代码已通过`if (frame && (codec->caps_internal & FF_CODEC_CAP_EOF_FLUSH))`条件确保`frame`指针非空，... |
| 1968 | ffmpeg-7.1 | rtp_parse_one_packet | Dereference of null pointer | 888 | FP | FP | 在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，代码已通过 `if (!buf)` 和 `if (len < 12)` 对 `buf` 指针和长度进行了检查。当 `buf` 为... |
| 1969 | ffmpeg-7.1 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `s->peak[i][j]` 之前，已通过循环 `if (dpd[pos]) s->peak[i][j] = 1;` 对数组 `s->peak` 进行了初始化赋值，因此后续的 `s->peak[i][j]` 访... |
| 1970 | ffmpeg-7.1 | ost_add | Dereference of null pointer | 1541 | FP | FP | 告警指向的代码行 `ms->stream_duration = ist->st->duration;` 在切片中位于 `if (ost->ist && ost->ist->st->duration > 0)` 条件块内，已通过前置条件... |
| 1971 | ffmpeg-7.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1420 | FP | FP | 代码切片显示，在访问 `scale_matrix[pos]` 之前，存在条件 `if (sps->scaling_list_enabled && !(transform_skip_flag && log2_trafo_size > 2... |
| 1972 | ffmpeg-7.1 | nal_parse_units | Dereference of null pointer | 93 | FP | FP | 告警行代码为 `return AVERROR(ERANGE);`，这是一个错误返回语句，并未解引用任何指针。工具可能误将 `list->nalus` 在条件判断中的访问识别为解引用，但该访问仅用于计算 `nalu_limit`，且 `... |
| 1973 | ffmpeg-7.1 | ff_inlink_make_frame_writable | Dereference of null pointer | 1513 | FP | FP | 告警点位于 `ff_get_audio_buffer(link, frame->nb_samples)` 调用，静态分析工具可能认为 `frame` 指针为空。但在切片代码中，函数开头 `AVFrame *frame = *rfram... |
| 1974 | ffmpeg-7.1 | get_bits1 | Dereference of null pointer | 391 | FP | FP | 代码中`s->buffer`的访问发生在`s`指针解引用之后，且函数为内联静态函数，其调用者应确保`s`指针非空。告警点`result = s->buffer[...]`本身不构成对空指针的解引用，因为`s`已在函数入口处被使用。结合... |
| 1975 | ffmpeg-7.1 | asf_parse_packet | Dereference of null pointer | 1307 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data[i]` 之前，已经通过 `av_assert0(asf_st)` 断言 `asf_st` 非空，并且 `asf_st->pkt.data` 的赋值来源于 `av_new_pack... |
| 1976 | ffmpeg-7.1 | <global> | Dereference of null pointer | 146 | FP | FP | 切片代码显示，在访问 `alpSrcPtr` 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，仅当条件为真时才为非空指针。告警行位于该条件保护的分支内，因此不会发生空指针解引用。 |
| 1977 | ffmpeg-7.1 | choose_rct_params | Dereference of null pointer | 991 | FP | FP | 告警指向的代码行 `r = *((const uint16_t*)(src[2] + x*2 + stride[2]*y));` 位于 `lbd` 为 false 的 else 分支中。切片代码显示 `src` 数组作为函数参数传入，... |
| 1978 | ffmpeg-7.1 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码显示，在告警行 `dp1[pos] = s->tint[0];` 之前存在条件判断 `if (dpd[pos])`，这确保了指针 `dpd` 在解引用前已被验证为非空，因此不存在空指针解引用。 |
| 1979 | ffmpeg-7.1 | unsharp_slice_8 | Dereference of null pointer | 173 | FP | FP | 切片代码显示，在宏展开的函数定义中，`src2` 变量被初始化为 NULL，但在后续可见的代码逻辑中并未被解引用。告警点位于宏定义行，实际解引用操作可能发生在未包含在切片内的其他分支或循环中，但基于现有切片，没有证据表明存在空指针解引... |
| 1980 | ffmpeg-7.1 | mov_write_trak_tag | Dereference of null pointer | 4187 | FP | FP | 告警指向的代码行 `double sample_aspect_ratio = av_q2d(st->sample_aspect_ratio);` 中，`st` 是函数参数，在切片代码的调用上下文中（如 `mov_write_tkhd_... |
| 1981 | ffmpeg-7.1 | ebml_parse | Dereference of null pointer | 1380 | FP | FP | 切片代码显示，在告警行（`level->length != EBML_UNKNOWN_LENGTH`）之前，`level` 指针已通过 `matroska->num_levels > 0` 的条件检查，并且 `level` 被定义为 ... |
| 1982 | ffmpeg-7.1 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码中，对数组索引 `poa` 和 `pob` 的访问均在条件 `(!i ｜｜ !dpd[poa])` 和 `(i == (out->height - 1) ｜｜ !dpd[pob])` 的保护之下，这些条件确保了当 `i` 为0... |
| 1983 | ffmpeg-7.1 | get_bits_le | Dereference of null pointer | 361 | FP | FP | 告警指向宏展开的代码行，但切片代码显示该函数为内联工具函数，其参数 `s` 在调用上下文中可能非空。宏 `UPDATE_CACHE_LE` 展开后对 `gb` 的访问，在典型的 `GetBitContext` 使用模式中，由调用者保证... |
| 1984 | ffmpeg-7.1 | ac3_apply_rematrixing | Dereference of null pointer | 598 | FP | FP | 告警点 `flags[bnd]` 的指针 `flags` 在切片代码中未定义其来源和初始化，无法确认其为空。结合代码上下文和算法标签（FP），该告警更可能是工具对变量作用域或数据流分析不充分导致的误报。 |
| 1985 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 683 | FP | FP | 告警指向的FFSWAP宏操作的是明确初始化的局部指针变量ptr1和ptr2，在切片可见的上下文（js_databuf == q->decoded_bytes_buffer条件分支内）中，ptr1被赋值为q->decoded_bytes... |
| 1986 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 303 | FP | FP | 切片代码显示告警行是对一个已知非空指针 `src` 进行类型转换和偏移访问，`src` 是函数参数且后续被用于循环读取，没有证据表明其为空。工具可能误判了指针解引用场景。 |
| 1987 | ffmpeg-7.1 | ff_rdt_parse_header | Dereference of null pointer | 202 | FP | FP | 告警指向的代码行是 while 循环的条件判断 `buf[1] == 0xFF`，切片显示 `buf` 是函数参数，在调用 `init_get_bits` 前已通过 `len >= 5` 和 `len < 16` 等检查确保其有效，且... |
| 1988 | ffmpeg-7.1 | av_encryption_init_info_free | Dereference of null pointer | 221 | FP | FP | 代码在访问 `info->key_ids[i]` 之前，已经通过 `if (info)` 检查了指针 `info` 非空，并且 `info->key_ids` 是一个数组指针，其元素在循环中被释放是正常的操作。切片中没有证据表明 `i... |
| 1989 | ffmpeg-7.1 | shift_frame | Dereference of null pointer | 152 | FP | FP | 切片代码显示，告警点引用的 `frame` 变量在上下文中未定义，且 `av_log` 宏被定义为空操作 `while(0)`，使得该行代码实际上不会执行任何解引用操作，因此该告警是误报。 |
| 1990 | ffmpeg-7.1 | build_table | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 正确初始化，且 `table_index` 在 `alloc_table` 成功时非... |
| 1991 | ffmpeg-7.1 | av_encryption_init_info_get_side_data | Dereference of null pointer | 280 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], ...)` 之前，`info->key_ids` 数组及其每个元素 `info->key_ids[j]` 都已在 `av_encryption_init_inf... |
| 1992 | ffmpeg-7.1 | encode_plane | Dereference of null pointer | 293 | FP | FP | 切片代码中，`sample[0]` 在循环前已通过 `sample[i] = sc->sample_buffer + ...` 被正确初始化，指向有效的缓冲区地址。告警点 `sample[0][x] = src[...]` 是对已分配... |
| 1993 | ffmpeg-7.1 | dump_stream_group | Dereference of null pointer | 715 | FP | FP | 切片代码中，告警行 `printed[st->index] = 1;` 位于一个循环内，该循环的进入条件 `channel_count > 0 && k < stg->nb_streams` 表明 `stg` 非空，且 `st` 应指... |
| 1994 | ffmpeg-7.1 | <global> | Dereference of null pointer | 166 | FP | FP | 切片代码显示，在解引用 `alpSrcPtr` 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，仅当条件为真时才进行赋值。告警点位于该条件保护的代码块内，因此不会发生空指针解引用。 |
| 1995 | ffmpeg-7.1 | <global> | Dereference of null pointer | 658 | FP | FP | 告警指向宏 UPDATE_CACHE 的展开，但切片代码显示该宏及其相关宏（如 GET_VLC）在 FFmpeg 的比特流读取上下文中是标准且安全的操作，旨在从缓冲区安全读取数据，不存在对空指针的解引用。结合算法标签 FP，判定为误报。 |
| 1996 | ffmpeg-7.1 | filter_frame | Dereference of null pointer | 145 | FP | FP | 切片代码显示，在警告行（linesize 计算）之前，已通过条件 `s->planeheight[plane] > 1` 进行保护。当 planeheight 不大于 1 时，linesize 被赋值为 0，避免了除以零或空指针解引用... |
| 1997 | ffmpeg-7.1 | set_bframe_chain_length | Dereference of null pointer | 1605 | FP | FP | 在告警行`s->input_picture[i]->b_frame_score = 0;`之前，循环条件`for (i = 0; i < b_frames + 1; i++)`确保了`i`的范围，且前面的逻辑分支`if (!s->in... |
| 1998 | ffmpeg-7.1 | mov_write_trak_tag | Dereference of null pointer | 4192 | FP | FP | 切片代码中，在调用 `is_clcp_track(track)` 之前，`track` 指针已在多处被安全使用（如 `track->start_dts`、`track->entry`），且其作为函数参数传入，没有证据表明它在此处会变为... |
| 1999 | ffmpeg-7.1 | get_bits | Dereference of null pointer | 340 | FP | FP | 告警点位于宏 UPDATE_CACHE 内部，其展开后涉及对指针 s 的访问。但函数 get_bits 的入参 s 在切片代码中未显示其来源或空值检查。结合该函数是内联工具函数，通常由调用者保证指针有效性，且参考标签 label 为 ... |
| 2000 | ffmpeg-7.1 | <global> | Dereference of null pointer | 472 | FP | FP | 切片代码中，`DECODE_CODEWORD` 宏内部调用了 `UPDATE_CACHE` 和 `GET_CACHE` 宏，这些宏负责从比特流读取数据并管理内部状态，但未显示对 `gb`（GetBitContext指针）进行空指针检查... |
| 2001 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 687 | FP | FP | 切片代码中，在警告行 `q->decoded_bytes_buffer[i] = *ptr2--;` 之前，`q->decoded_bytes_buffer` 已在函数开头通过 `q = avctx->priv_data;` 初始化，... |
| 2002 | ffmpeg-7.1 | decode_frame | Dereference of null pointer | 692 | FP | FP | 切片代码显示，在警告行（`for (i = 4; *ptr1 == 0xF8; i++, ptr1++)`）之前，`ptr1` 被明确初始化为 `q->decoded_bytes_buffer`，这是一个有效的缓冲区指针。循环条件 `... |
| 2003 | ffmpeg-6.0 | show_bits | Dereference of null pointer | 366 | FP | FP | 告警指向宏定义展开的内部实现，而非直接的用户代码。切片代码显示`UPDATE_CACHE`等是访问位缓冲区的内部宏，其空指针检查应由调用者`show_bits`的上下文保证。结合参考标签为FP，倾向于判定为工具对宏展开的误报。 |
| 2004 | ffmpeg-6.0 | finalize_packet | Dereference of null pointer | 677 | FP | FP | 告警指向的代码行`s->st->time_base.den`在调用前，其指针`s->st`已在条件`s->ic->nb_streams > 1`中得到间接验证，且`s->last_rtcp_ntp_time != AV_NOPTS_V... |
| 2005 | ffmpeg-6.0 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 408 | FP | FP | 切片代码显示，在访问 `ctx->buffers` 数组前，存在对 `ctx->buffers` 是否为空的检查（`if (!ctx->buffers) break;`），并且数组索引 `buf.index` 来自受控的 `ioctl... |
| 2006 | ffmpeg-6.0 | roq_dpcm_encode_frame | Dereference of null pointer | 179 | FP | FP | 告警行访问的 `frame` 指针在函数入口处已通过三元运算符与 `in` 变量关联检查，当 `in` 为 NULL 时，`frame` 也为 NULL，但告警行所在的赋值语句 `avpkt->pts = context->input... |
| 2007 | ffmpeg-6.0 | ebml_read_binary | Dereference of null pointer | 1073 | FP | FP | 切片代码显示，在调用 `memset` 之前，`av_buffer_realloc` 的返回值已被检查，且该函数在成功时保证 `bin->buf` 及其 `data` 字段有效。因此，对 `bin->buf->data` 的解引用是安... |
| 2008 | ffmpeg-6.0 | <global> | Dereference of null pointer | 208 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被分配内存（通过 `av_malloc_array`）或指向 `p->data[0]`，且后续循... |
| 2009 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 119 | FP | FP | 切片代码显示，在告警行`uint8_t *val = in->data[plane];`之前，`in`帧作为参数传入且未被修改，其`data`字段在FFmpeg框架中初始化后不应为空。此外，代码逻辑主要处理视频像素数据，`in`为空将... |
| 2010 | ffmpeg-6.0 | unsharp_slice_16 | Dereference of null pointer | 142 | FP | FP | 告警指向的宏定义行 `DEF_UNSHARP_SLICE_FUNC(unsharp_slice, 16)` 本身是函数声明，并非实际的解引用操作。切片代码中未发现对空指针的直接解引用，且宏展开后的函数逻辑包含空指针检查（如 `if (... |
| 2011 | ffmpeg-6.0 | ebml_parse | Dereference of null pointer | 1339 | FP | FP | 告警指向的代码行 `level->length != EBML_UNKNOWN_LENGTH` 位于 `if (matroska->num_levels > 0)` 条件块内，而变量 `level` 在函数开头已定义为 `Matros... |
| 2012 | ffmpeg-6.0 | get_interleaved_ue_golomb | Dereference of null pointer | 175 | FP | FP | 切片代码中，`UPDATE_CACHE` 宏的展开不涉及对 `gb` 指针的直接解引用，且 `BITS_AVAILABLE` 宏被定义为常量1，表明该代码路径在编译时已确定，不存在运行时空指针解引用的逻辑。参考标签 `label` 为... |
| 2013 | ffmpeg-6.0 | put_bits_no_assert | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在指针解引用操作 `AV_WBBUF(s->buf_ptr, bit_buf)` 之前，已通过条件 `if (s->buf_end - s->buf_ptr >= sizeof(BitBuf))` 检查了缓冲区边界，确保... |
| 2014 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 301 | FP | FP | 切片代码显示，指针 `src` 作为函数参数传入，并在多个分支中被安全地用于数组索引和类型转换，没有证据表明它在此上下文中为空。告警指向的代码行是对 `src` 的合法解引用，属于工具的逻辑误判。 |
| 2015 | ffmpeg-6.0 | v4l2_dequeue_v4l2buf | Dereference of null pointer | 332 | FP | FP | 切片代码显示，在访问 `ctx->buffers[i]` 之前，存在 `if (!ctx->buffers)` 的检查，这可以防止对空指针的访问。此外，告警行所在的循环位于 `if (ctx->buffers)` 条件块之后，且 `l... |
| 2016 | ffmpeg-6.0 | rtp_set_prft | Dereference of null pointer | 645 | FP | FP | 切片代码显示，在调用 `av_rescale_q` 之前，已对 `av_packet_new_side_data` 的返回值 `prft` 进行了空指针检查，若为空则提前返回错误。因此，在告警所在行，`s` 和 `s->st` 不可能... |
| 2017 | ffmpeg-6.0 | ebml_read_sint | Dereference of null pointer | 1000 | FP | FP | 切片代码显示，在调用 `avio_r8` 函数读取数据前，函数内部已包含缓冲区边界检查（`s->buf_ptr >= s->buf_end`）和填充逻辑（`fill_buffer`），这提供了基本的空指针解引用防护。结合参考标签为 F... |
| 2018 | ffmpeg-6.0 | safe_filename | Dereference of null pointer | 97 | FP | FP | 代码逻辑显示，指针 `f` 在循环条件 `for (; *f; f++)` 中被解引用前，已通过函数参数传入，且循环条件 `*f` 本身是安全的空指针检查。函数旨在检查文件名安全性，不存在解引用空指针的逻辑错误。 |
| 2019 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 117 | FP | FP | 切片代码显示，在访问 `in->linesize[plane]` 之前，`in` 指针作为函数参数传入且未被置空，并且在 `s->planeheight[plane] > 1` 的条件下才会使用该值，否则赋值为0。告警点位于条件表达式... |
| 2020 | ffmpeg-6.0 | of_open | Dereference of null pointer | 2303 | FP | FP | 切片代码显示，在访问 `ost->enc_ctx->codec` 之前，存在 `if (ost->filter)` 条件判断。告警行位于该条件块内部，因此 `ost` 指针及其 `enc_ctx` 成员在访问时不可能为空，否则程序无法... |
| 2021 | ffmpeg-6.0 | ff_encode_encode_cb | Dereference of null pointer | 244 | FP | FP | 告警点位于条件判断 `if (frame->duration)`，但切片代码显示，在进入该分支前，外层存在 `if (frame && ...)` 的条件检查，并且函数末尾有 `if (frame) av_frame_unref(fr... |
| 2022 | ffmpeg-6.0 | get_sbits | Dereference of null pointer | 315 | FP | FP | 切片代码显示告警点位于宏 `UPDATE_CACHE` 的调用处，该宏及其相关宏（如 `OPEN_READER`）的定义均在切片中给出，未发现对空指针 `s` 的直接解引用操作。结合参考标签 `label` 为 FP，倾向于判定为工具... |
| 2023 | ffmpeg-6.0 | envelope_peak | Dereference of null pointer | 375 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已存在条件判断 `if (dpd[pos])`，这隐含了 `dpd` 指针非空的前提，且后续使用 `dpd[pos] = 255;` 的上下文也表明 `dpd` 是有效的。结合参考标签... |
| 2024 | ffmpeg-6.0 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1476 | FP | FP | 切片代码显示 `scale_matrix` 仅在 `s->ps.sps->scaling_list_enable_flag` 为真且特定条件满足时才被赋值，否则保持为 NULL。在告警行 `scale_m = scale_matrix... |
| 2025 | ffmpeg-6.0 | try_push_frame | Dereference of null pointer | 243 | FP | FP | 切片代码显示 `inbuf` 数组已初始化为 `{ NULL }`，且 `ff_inlink_consume_samples` 函数在成功时会将 `inbuf[i]` 指向有效帧，失败时保持 `NULL`。告警行 `outbuf->p... |
| 2026 | ffmpeg-6.0 | hls_read_header | Dereference of null pointer | 2131 | FP | FP | 切片代码中，在警告行 `if (strstr(in_fmt->name, "mov"))` 之前，`in_fmt` 已在多个分支中被赋值（例如通过 `av_demuxer_iterate` 或 `av_probe_input_buff... |
| 2027 | ffmpeg-6.0 | hls_append_segment | Dereference of null pointer | 1180 | FP | FP | 切片代码显示，在警告行 `if (!en->next->discont_program_date_time && !en->discont_program_date_time)` 之前，`en` 被赋值为 `vs->segments`... |
| 2028 | ffmpeg-6.0 | concat_parse_script | Dereference of null pointer | 558 | FP | FP | 在DIR_DURATION指令处理前，代码已通过NEEDS_FILE标志检查确保cat->nb_files > 0，且file指针在DIR_FILE指令中通过add_file函数被正确赋值。因此，当执行到`file->user_dur... |
| 2029 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 297 | FP | FP | 切片代码显示，`src` 指针在解引用前已作为函数参数传入，并在循环中用于计算地址 `src + stride*y`，该操作本身是合法的指针运算。警告指向的 `((uint16_t*)(src + stride*y))[x]` 行是对... |
| 2030 | ffmpeg-6.0 | vectorscope16 | Dereference of null pointer | 579 | FP | FP | 切片代码显示，在访问 `dp1[pos]` 和 `dp2[pos]` 之前，存在条件 `if (dpd[pos])` 进行保护，这确保了指针 `dp1` 和 `dp2` 的访问是安全的。此外，算法参考标签也为 FP，支持误报结论。 |
| 2031 | ffmpeg-6.0 | id3v2_parse | Dereference of null pointer | 1051 | FP | FP | 告警点位于条件分支 `extra_func->read(...)` 的调用处，但 `extra_func` 仅在 `extra_meta && (extra_func = get_extra_meta_func(tag, isv34)... |
| 2032 | ffmpeg-6.0 | choose_rct_params | Dereference of null pointer | 979 | FP | FP | 切片代码显示告警行位于 `lbd` 为 false 的 else 分支内，该分支访问 `src[1]` 和 `src[2]`。函数参数 `src` 是一个指向 `const uint8_t *` 数组的指针，调用者负责传递有效的数组。... |
| 2033 | ffmpeg-6.0 | split_commandline | Dereference of null pointer | 713 | FP | FP | 告警点位于检查 `opt[0] == '-' && opt[1] == '-' && !opt[2]` 的条件判断处，其中 `opt` 是 `argv[optindex++]` 的指针，而 `argv` 来自命令行参数，在 `prep... |
| 2034 | ffmpeg-6.0 | ebml_read_ascii | Dereference of null pointer | 1055 | FP | FP | 切片代码显示 `av_free` 被宏定义为 `while(0)`，这是一个空操作宏，因此对 `*str` 的解引用实际上不会发生，不存在空指针解引用风险。 |
| 2035 | ffmpeg-6.0 | output_packet | Dereference of null pointer | 1092 | FP | FP | 切片代码显示，在访问 `timestamp_packet->unwritten_size` 之前，`timestamp_packet` 被赋值为 `stream->premux_packet`，而 `stream->premux_pa... |
| 2036 | ffmpeg-6.0 | ebml_read_uint | Dereference of null pointer | 980 | FP | FP | 切片代码显示，在指针 `num` 被解引用之前，函数参数 `num` 本身并未被检查是否为 NULL。然而，该告警指向的代码行 `*num = 0;` 是函数内部的赋值操作，其解引用行为完全依赖于调用者传入的指针。由于切片中未包含调用... |
| 2037 | ffmpeg-6.0 | concat_parse_script | Dereference of null pointer | 562 | FP | FP | 代码中DIR_INPOINT指令的执行有前置条件检查`(dir->flags & NEEDS_FILE) && !cat->nb_files`，确保`file`指针在赋值前已通过DIR_FILE指令有效初始化，因此不会发生空指针解引用。 |
| 2038 | ffmpeg-6.0 | av_tree_insert | Dereference of null pointer | 109 | FP | FP | 告警指向的代码行位于条件 `if ((*child)->state * 2 == -t->state)` 内部，该条件仅在 `t->state` 非零且 `t->state` 为偶数（`!(t->state & 1)`）时才会被评估。... |
| 2039 | ffmpeg-6.0 | ogg_write_header | Dereference of null pointer | 628 | FP | FP | 切片代码显示，对 `oggstream->page.start_granule` 的赋值操作是直接设置一个常量（`AV_NOPTS_VALUE`），并未涉及对 `oggstream` 或 `oggstream->page` 指针的解引... |
| 2040 | ffmpeg-6.0 | init_output_stream_encode | Dereference of null pointer | 3153 | FP | FP | 切片代码显示，在访问 `ost->ist->par->width` 之前，`ost` 和 `ost->ist` 的指针有效性已在函数外部或更早的代码路径中得到保证，且告警点位于条件分支 `if (!enc_ctx->width)` 内... |
| 2041 | ffmpeg-6.0 | guess_mv | Dereference of null pointer | 428 | FP | FP | 切片代码中，在警告行（else if(s->last_pic.f->data[0] && s->last_pic.motion_val[0])）访问 s->last_pic.f->data[0] 之前，已经存在条件判断 'if (s-... |
| 2042 | ffmpeg-6.0 | build_table | Dereference of null pointer | 203 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `alloc_table` 成功分配并赋值，且 `j` 的值由 `code_prefix` 计算而来，其范围受 `table_nb_bits` 限制，不会越... |
| 2043 | ffmpeg-6.0 | ff_vorbiscomment_write | Dereference of null pointer | 93 | FP | FP | 切片代码显示，在告警行 `AVChapter *chp = chapters[i];` 之前，存在条件判断 `if (chapters && nb_chapters)` 和 `for (int i = 0; i < nb_chapte... |
| 2044 | ffmpeg-6.0 | locate_option | Dereference of null pointer | 424 | FP | FP | 在调用 `po->name` 之前，`po` 变量由 `find_option` 函数返回，该函数保证返回一个指向 `OptionDef` 结构体的指针（即使未找到匹配项，也返回指向数组末尾的指针），不会返回 NULL。因此，对 `p... |
| 2045 | ffmpeg-6.0 | guess_status_pts | Dereference of null pointer | 446 | FP | FP | 切片代码显示，在访问 `ctx->inputs[i]` 指针前，循环条件 `i < ctx->nb_inputs` 确保了 `i` 在有效范围内，且 `ctx->inputs` 数组的有效性由调用上下文保证。没有证据表明 `ctx->... |
| 2046 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 148 | FP | FP | 切片代码显示，在深度大于8的分支中，`val` 被赋值为 `(uint16_t *)in->data[plane]`，而 `in` 是函数参数，在调用前已被检查非空（`filter_frame` 的调用约定保证了这一点）。因此，对 `... |
| 2047 | ffmpeg-6.0 | av_dump_format | Dereference of null pointer | 703 | FP | FP | 切片代码显示，在访问 `printed` 数组前，存在条件 `if (ic->nb_streams && !printed) return;`，这确保了当 `ic->nb_streams` 非零且 `printed` 为 NULL 时... |
| 2048 | ffmpeg-6.0 | choose_rct_params | Dereference of null pointer | 980 | FP | FP | 切片代码显示，在lbd为假的分支中，对src[2]进行了指针解引用。虽然src[2]可能为空，但告警点位于一个循环和条件分支内部，且函数参数src[3]表明它是一个指针数组。在没有明确证据表明src[2]一定为null的情况下，结合算... |
| 2049 | ffmpeg-6.0 | activate | Dereference of null pointer | 168 | FP | FP | 告警点位于 `frame->pts = s->pts;`，但切片代码显示，在此之前 `frame` 指针要么通过 `ff_get_video_buffer` 成功分配，要么通过 `av_frame_clone` 成功克隆，两者失败时都... |
| 2050 | ffmpeg-6.0 | <global> | Dereference of null pointer | 199 | FP | FP | 切片代码显示，在访问 `ptr2[x]` 之前，`ptr2` 已在条件分支 `if (maplength && depth < 8)` 中被 `av_malloc_array` 分配内存，且分配失败会直接返回错误。在告警所在行，代码处... |
| 2051 | ffmpeg-6.0 | ff_encode_encode_cb | Dereference of null pointer | 241 | FP | FP | 告警点位于条件判断 `if (avpkt->pts == AV_NOPTS_VALUE)` 内部，其执行前提是 `frame` 不为空（由外层条件 `if (frame && ...)` 保证）。切片代码显示，在调用 `av_fram... |
| 2052 | ffmpeg-6.0 | rtp_parse_one_packet | Dereference of null pointer | 887 | FP | FP | 在告警行 `if ((buf[0] & 0xc0) != (RTP_VERSION << 6))` 之前，代码已通过 `if (!buf)` 和 `if (len < 12)` 进行了检查。当 `buf` 为 NULL 时，函数已在第... |
| 2053 | ffmpeg-6.0 | envelope_peak | Dereference of null pointer | 389 | FP | FP | 切片代码显示，在访问 `dpd[pos]` 之前，已通过条件 `if (dpd[pos])` 和 `if (s->peak[i][j] && ...)` 进行了检查，确保了指针 `dpd` 指向的数组内存已被成功分配和初始化。告警点 ... |
| 2054 | ffmpeg-6.0 | ff_inlink_make_frame_writable | Dereference of null pointer | 1423 | FP | FP | 告警点位于switch-case分支内，该分支仅在link->type为AVMEDIA_TYPE_AUDIO时执行。在调用ff_get_audio_buffer前，函数已通过av_frame_is_writable检查frame指针，... |
| 2055 | ffmpeg-6.0 | get_bits1 | Dereference of null pointer | 381 | FP | FP | 代码中`s->buffer`的访问基于`s->index`，但切片内未提供`s`或`s->buffer`的初始化及空值检查上下文。结合告警为逻辑错误而非空指针解引用，且算法标签为FP，倾向于判定为工具误报。 |
| 2056 | ffmpeg-6.0 | asf_parse_packet | Dereference of null pointer | 1302 | FP | FP | 切片代码中，在访问 `asf_st->pkt.data[i]` 之前，已经通过 `av_new_packet` 或 `av_packet_new_side_data` 等函数为 `asf_st->pkt.data` 分配了内存，并且有... |
| 2057 | ffmpeg-6.0 | <global> | Dereference of null pointer | 148 | FP | FP | 切片代码显示，在访问 `alpSrcPtr` 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，当条件不满足时 `alpSrcPtr` 被初始化为 `NULL`，但后续使用该指针时均... |
| 2058 | ffmpeg-6.0 | add_interval | Dereference of null pointer | 1035 | FP | FP | 切片代码显示，在访问 `ri` 之前，已通过 `if (ref >= 0)` 条件确保 `ref` 有效，且 `alloc_array_elem` 函数内部有充分的空指针检查。告警点 `ri->type` 的访问发生在该保护条件内，逻... |
| 2059 | ffmpeg-6.0 | vectorscope8 | Dereference of null pointer | 775 | FP | FP | 切片代码中，在告警行 `dp1[pos] = s->tint[0];` 之前存在条件判断 `if (dpd[pos])`，这确保了 `dpd[pos]` 指针非空后才进行解引用，因此不存在空指针解引用风险。 |
| 2060 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 335 | FP | FP | 告警行`s->out->pts = in->pts;`位于`s->do_video`条件块内，该条件块仅在`s->out`被成功分配（通过`ff_get_video_buffer`）或`ff_inlink_make_frame_wri... |
| 2061 | ffmpeg-6.0 | unsharp_slice_8 | Dereference of null pointer | 143 | FP | FP | 告警指向的宏定义行 `DEF_UNSHARP_SLICE_FUNC(unsharp_slice, 8)` 本身是函数声明，并非实际的空指针解引用。切片代码中未展示任何对空指针进行解引用的具体操作，且宏展开后的函数逻辑包含空指针检查（如... |
| 2062 | ffmpeg-6.0 | ebml_parse | Dereference of null pointer | 1356 | FP | FP | 告警指向的代码行位于一个条件分支内，该分支在 `level->length != EBML_UNKNOWN_LENGTH` 且 `length == EBML_UNKNOWN_LENGTH` 时执行，并立即返回错误码 `AVERROR... |
| 2063 | ffmpeg-6.0 | envelope_instant | Dereference of null pointer | 357 | FP | FP | 切片代码显示，在访问 `dpd[poa]` 和 `dpd[pob]` 之前，已通过条件 `(!i ｜｜ !dpd[poa])` 和 `((i == (out->height - 1)) ｜｜ !dpd[pob])` 进行了边界检查，确... |
| 2064 | ffmpeg-6.0 | get_bits_le | Dereference of null pointer | 351 | FP | FP | 告警点位于宏 UPDATE_CACHE_LE 内部，该宏对指针 `(gb)->buffer` 进行解引用。切片代码显示 `gb` 是函数参数 `GetBitContext *s` 的别名，调用者必须确保传入有效的非空指针。函数 `ge... |
| 2065 | ffmpeg-6.0 | ac3_apply_rematrixing | Dereference of null pointer | 410 | FP | FP | 切片代码显示，对指针 `flags` 的解引用发生在 `for (bnd = 0; bnd < block->num_rematrixing_bands; bnd++)` 循环内，该循环条件确保了 `bnd` 在有效范围内。结合 `l... |
| 2066 | ffmpeg-6.0 | av_encryption_init_info_free | Dereference of null pointer | 219 | FP | FP | 代码在访问 `info->key_ids[i]` 之前，已通过 `if (info)` 检查了指针 `info` 非空，并且 `for` 循环的条件 `i < info->num_key_ids` 也隐含了 `info` 非空。切片中... |
| 2067 | ffmpeg-6.0 | shift_frame | Dereference of null pointer | 150 | FP | FP | 切片代码显示，在告警行引用的 `frame` 变量未在函数 `shift_frame` 的可见作用域内定义或传入，这很可能是一个静态分析工具无法解析的上下文问题。同时，参考标签 `label` 为 FP，表明该告警在后续版本中未被修复... |
| 2068 | ffmpeg-6.0 | build_table | Dereference of null pointer | 169 | FP | FP | 切片代码显示，在访问 `table[j]` 之前，`table` 指针已通过 `table = &vlc->table[table_index];` 被正确赋值，且 `table_index` 在 `alloc_table` 调用成功... |
| 2069 | ffmpeg-6.0 | ff_inlink_evaluate_timeline_at_frame | Dereference of null pointer | 1466 | FP | FP | 切片代码显示，对 `frame` 指针的访问发生在函数参数中，且 `frame` 作为 `const AVFrame *` 类型的参数传入，其有效性应由调用者保证。告警点 `frame->pts` 的访问本身没有在切片中显示空指针检查... |
| 2070 | ffmpeg-6.0 | av_encryption_init_info_get_side_data | Dereference of null pointer | 278 | FP | FP | 切片代码显示，在调用 `memcpy(info->key_ids[j], side_data, key_id_size)` 之前，`info->key_ids` 数组及其每个元素已通过 `av_encryption_init_info... |
| 2071 | ffmpeg-6.0 | <global> | Dereference of null pointer | 168 | FP | FP | 切片代码显示，在解引用 `alpSrcPtr` 之前，已通过条件 `(CONFIG_SWSCALE_ALPHA && hasAlpha)` 进行检查，仅当条件为真时才进行赋值。告警行位于该条件保护的分支内，因此不会发生空指针解引用。 |
| 2072 | ffmpeg-6.0 | filter_frame | Dereference of null pointer | 146 | FP | FP | 告警指向的代码行 `const int linesize = s->planeheight[plane] > 1 ? in->linesize[plane] / 2 : 0;` 包含一个三元运算符，当 `s->planeheight[... |
| 2073 | ffmpeg-6.0 | get_bits | Dereference of null pointer | 330 | FP | FP | 告警点位于宏 UPDATE_CACHE 的调用处，该宏展开后对指针 s 的访问是间接的。切片代码显示 get_bits 函数是一个内联工具函数，其指针参数 s 由调用者传入，在函数内部没有显式的空指针检查。然而，该函数在 FFmpeg... |
| 2074 | ffmpeg-6.0 | encode_plane | Dereference of null pointer | 291 | FP | FP | 切片代码显示，`src` 指针作为函数参数传入，并在多个分支中被直接用于数组索引和指针转换，没有显式的空指针检查。然而，该告警为逻辑错误类空指针解引用，在切片中未发现 `src` 被赋值为空或可能导致其为空的代码路径。结合参考标签 `... |
| 2075 | ffmpeg-6.0 | bits_priv_refill_32_be | Dereference of null pointer | 85 | FP | FP | 代码在宏定义 `BITSTREAM_TEMPLATE_LE` 下调用 `AV_RB32(bc->ptr)`，但切片显示在调用前存在条件 `#if !UNCHECKED_BITSTREAM_READER` 检查 `bc->ptr >= ... |
| 2076 | git-2.46.0 | add_parents_only | Dereference of null pointer | 1929 | FP | FP | 在调用 `it->type` 之前，代码已检查 `if (!it && revs->ignore_missing) return 0;`，这确保了当 `it` 为 NULL 且 `revs->ignore_missing` 为真时函数... |
| 2077 | git-2.46.0 | get_mode | Dereference of null pointer | 63 | FP | FP | 告警行 `*special = SPECIAL_STDIN;` 中指针 `special` 的解引用是安全的，因为该行位于 `else if (path == file_from_standard_input)` 条件分支内，而该分支... |
| 2078 | git-2.46.0 | sync_submodule | Dereference of null pointer | 1273 | FP | FP | 切片代码显示，在调用 `submodule_from_path` 获取 `sub` 指针后，立即在 `strbuf_addf` 中解引用 `sub->name`。虽然未直接检查 `sub` 是否为 NULL，但告警行之前的 `is_s... |
| 2079 | git-2.46.0 | crlf_to_git | Dereference of null pointer | 573 | FP | FP | 在告警行`unsigned char c = *src++;`之前，函数入口处有检查`if (src && !len)`和`if (!buf && !src)`，且`src`作为函数参数传入，在切片代码的可见上下文中，没有证据表明`s... |
| 2080 | git-2.46.0 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码中，在警告行 `d = delta[c = (end += d)[-1]];` 之前，变量 `d` 已在循环条件 `while (lim - end >= d)` 中被使用，表明 `d` 在进入循环时已被初始化且不为零，因此对... |
| 2081 | git-2.46.0 | diffcore_merge_broken | Dereference of null pointer | 295 | FP | FP | 在警告行`if (pp->broken_pair &&`之前，内层循环已确保`pp = q->queue[j]`，而外层循环对`q->queue[i]`有明确的空指针检查（`if (!p) continue;`），这表明代码逻辑已处理... |
| 2082 | git-2.46.0 | parse_options_step | Dereference of null pointer | 900 | FP | FP | 告警点位于条件判断 `if (internal_help && *ctx->opt == 'h')`，其中 `ctx->opt` 在进入该分支前已通过 `ctx->opt = arg + 1;` 被赋值为非空指针（`arg` 是 `c... |
| 2083 | git-2.46.0 | rstrip_ref_components | Dereference of null pointer | 2117 | FP | FP | 切片代码中，`p` 是 `refname` 的指针，`refname` 来自函数参数且未被修改，因此 `p` 不可能为 null。在 `for` 循环条件 `p[i]` 中，`p` 被解引用，但循环仅在 `p[i]` 为真（非零）时继... |
| 2084 | git-2.46.0 | parse_options | Dereference of null pointer | 1046 | FP | FP | 在告警行 `isascii(*ctx.opt)` 之前，`parse_options_step` 函数已明确将 `ctx->opt` 重置为 NULL，并且当 `ctx->opt` 不为 NULL 时才会进入该分支。切片代码显示，只有... |
| 2085 | git-2.46.0 | process_entry | Dereference of null pointer | 3413 | FP | FP | 告警行位于RENAME_ONE_FILE_TO_TWO分支内，该分支仅在ci->ren2非空时才会执行。切片代码显示，在进入此分支前有`if (ci->ren2)`的断言，表明该分支的执行依赖于ci->ren2的有效性，因此对ci->... |
| 2086 | git-2.46.0 | verify_absent | Dereference of null pointer | 2526 | FP | FP | 告警点代码 `ce->ce_flags` 在函数入口处 `ce` 指针不可能为空，因为该函数是静态的，由调用者传入，且切片中所有对 `ce` 的访问（如 `ce->name`）都未进行空指针检查，表明调用上下文保证了其有效性。工具误报... |
| 2087 | git-2.46.0 | show_pack_info | Dereference of null pointer | 1688 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，否则保持为 NULL。在警告行访问 `chain_histogram` 之前，存在条件... |
| 2088 | git-2.46.0 | output | Dereference of null pointer | 548 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `j < b->nr` 条件确保非空，且 `b_util->matching` 在 `while (j < b-... |
| 2089 | git-2.46.0 | limit_list | Dereference of null pointer | 1492 | FP | FP | 告警指向的代码行 `if (obj->flags & UNINTERESTING)` 中，`obj` 是从 `&commit->object` 获取的，而 `commit` 在循环中通过 `pop_commit` 获取，该函数在栈非空... |
| 2090 | git-2.46.0 | add_lines_to_move_detection | Dereference of null pointer | 1055 | FP | FP | 切片代码显示，`entry_list` 数组通过 `ALLOC_GROW_BY` 宏进行动态增长和初始化，该宏会确保分配的内存被清零。在访问 `entry_list[l->id]` 之前，`l->id` 的值要么来自已存在的 `s->... |
| 2091 | git-2.46.0 | limit_list | Dereference of null pointer | 1488 | FP | FP | 告警指向的代码行 `if (revs->max_age != -1 && (commit->date < revs->max_age))` 中，`commit` 变量来自 `pop_commit` 函数，该函数在栈非空时返回有效指针，... |
| 2092 | git-2.46.0 | lstrip_ref_components | Dereference of null pointer | 2079 | FP | FP | 切片代码中，`p` 指针在循环条件 `p[i]` 中被解引用，但 `p` 被初始化为 `refname`，而 `refname` 是函数参数，没有证据表明其为空。同时，参考标签 `label` 为 FP，表明该告警在后续版本中未被修复... |
| 2093 | git-2.46.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 切片代码显示，当 `strmap_get_entry` 返回空指针时，函数直接返回 `map->default_value`，并未对空指针进行解引用操作。告警的逻辑错误不成立，属于误报。 |
| 2094 | git-2.46.0 | coalesce_lines | Dereference of null pointer | 264 | FP | FP | 在告警行`newend = newend->prev;`之前，`newend`指针已在循环中通过`if (newend->next)`条件进行遍历和赋值，确保了其非空。此外，`directions[i][j] == MATCH`的条件... |
| 2095 | git-2.46.0 | merge_ort_internal | Dereference of null pointer | 5217 | FP | FP | 告警点位于 `opt->priv->call_depth--;`，但切片代码显示 `opt->priv` 在函数入口处已被使用且未发现其被置为空的路径。`opt` 作为函数参数，其 `priv` 成员在递归调用前已通过 `opt->p... |
| 2096 | git-2.46.0 | process_parents | Dereference of null pointer | 1175 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，并且 `repo_parse_commit_gently` 调用失败时会 `continue`，这进一步保护了后续访问。切片代码中未发现 ... |
| 2097 | git-2.46.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1364 | FP | FP | 告警点位于对 `msg->buf` 的访问，但切片代码显示 `msg` 是函数参数，其来源由调用者控制。在函数内部，`msg` 被直接传递给 `write_message`，没有对其进行空指针检查。然而，`write_message`... |
| 2098 | git-2.46.0 | gather_stats | Dereference of null pointer | 51 | FP | FP | 切片代码显示函数入口处有 `size` 参数，循环条件 `i < size` 确保了 `i` 和 `i+1` 的访问在 `buf` 的有效范围内，不存在对空指针的解引用。告警可能是工具对循环边界或指针状态的分析误判。 |
| 2099 | git-2.46.0 | append_strategy | Dereference of null pointer | 229 | FP | FP | 切片代码显示函数仅将指针存入数组，未对指针`s`本身进行解引用操作。告警所指的行是数组赋值，并非解引用空指针。代码逻辑本身是安全的，属于工具误报。 |
| 2100 | git-2.46.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码显示函数`strvec_push_nodup`直接对数组`array->v`进行赋值，但未提供`array`指针本身是否为空的上下文。结合告警规则（空指针解引用）和参考标签（FP），推断调用方应已确保`array`非空，否则该... |
| 2101 | git-2.46.0 | add_lines_to_move_detection | Dereference of null pointer | 1058 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行动态增长和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，与数组分... |
| 2102 | git-2.46.0 | coalesce_lines | Dereference of null pointer | 272 | FP | FP | 告警点位于条件判断 `if (lline->prev)` 中，该行代码仅检查指针 `lline->prev` 是否为 NULL，并未对其进行解引用。工具报告的逻辑错误（空指针解引用）在此上下文中不成立，因为代码只是安全地检查指针值。 |
| 2103 | git-2.46.0 | apply_one_fragment | Dereference of null pointer | 3025 | FP | FP | 切片代码显示告警行位于条件分支 `if (inaccurate_eof && ...)` 内部，该分支仅在特定条件满足时执行。在分支内，`preimage.nr` 和 `postimage.nr` 已通过 `add_line_info... |
| 2104 | git-2.46.0 | try_to_commit | Dereference of null pointer | 1698 | FP | FP | 告警指向的 `commit_tree_extended` 函数调用行，其参数 `parents` 在切片中已通过条件分支（如 `parents = copy_commit_list(current_head->parents);` 或... |
| 2105 | git-2.46.0 | prepare_attr_stack | Dereference of null pointer | 1013 | FP | FP | 在调用 `*stack = info->prev;` 之前，`info` 被赋值为 `*stack`，而 `*stack` 由 `bootstrap_attr_stack` 函数初始化。该函数确保 `*stack` 不为空（若为空则进... |
| 2106 | git-2.46.0 | split_graph_merge_strategy | Dereference of null pointer | 2269 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，`g` 的取值受到 `while (g && ...)` 循环和后续 `if (ctx->num_commit_graphs_after == 2)... |
| 2107 | git-2.46.0 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 函数逻辑清晰，通过条件判断 `if (line == 0)` 确保了当 `line` 不为0时才会访问 `ends[line]`。切片中未显示 `ends` 或 `data` 为空的证据，且 `line` 作为参数，其值在切片内未显示... |
| 2108 | git-2.46.0 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对参数 `ref_iterator` 进行任何解引用操作，因此不存在空指针解引用问题。 |
| 2109 | git-2.46.0 | find_bisection | Dereference of null pointer | 439 | FP | FP | 在告警行 `list->item = best->item;` 之前，`best` 指针已在 `if (best)` 条件中进行了非空检查，确保了其不为空。因此，对 `best->item` 的访问是安全的，不存在空指针解引用。 |
| 2110 | git-2.46.0 | verify_absent_1 | Dereference of null pointer | 2485 | FP | FP | 切片代码显示，在调用 `check_leading_path` 函数前，已通过条件 `if (o->index_only ｜｜ !o->update)` 进行了保护，当条件为真时函数直接返回，不会执行到告警行。这表明告警点所在的代码路... |
| 2111 | git-2.46.0 | merge_ref_iterator_advance | Dereference of null pointer | 202 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 仅在 `selection & ITER_YIELD_CURRENT` 为真时被使用，而此条件位于一个循环内，且 `iter->curre... |
| 2112 | git-2.46.0 | try_to_commit | Dereference of null pointer | 1582 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，但在切片代码中，该行位于 `if (flags & AMEND_MSG)` 分支内，且其前有 `if (!autho... |
| 2113 | git-2.46.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数 `ce_path_match` 的参数 `ce` 被直接用于宏 `ce_namelen` 和访问其 `name` 字段。调用该函数的上下文未知，但告警点本身没有空指针解引用。`ce` 作为参数传入，其有效性应由调用... |
| 2114 | git-2.46.0 | cmp_local_packs | Dereference of null pointer | 481 | FP | FP | 函数入口处 `pl` 被赋值为全局变量 `local_packs`，该变量在切片中初始化为 NULL。在未检查 `pl` 是否为 NULL 的情况下，直接访问 `pl->next`，存在空指针解引用风险。但参考标签为 FP，且该函数为... |
| 2115 | git-2.46.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 677 | FP | FP | 代码在解引用指针 `n` 之前，已通过 `if (n)` 进行了空指针检查，确保了 `n` 非空时才执行后续操作，逻辑正确，不存在空指针解引用风险。 |
| 2116 | git-2.46.0 | unload_one_branch | Dereference of null pointer | 2049 | FP | FP | 切片代码显示，在解引用 `e` 之前，`e` 被赋值为 `active_branches`，而 `active_branches` 仅在 `while` 循环（条件为 `cur_active_branches && cur_activ... |
| 2117 | git-2.46.0 | process_entries | Dereference of null pointer | 4451 | FP | FP | 切片代码显示，对 `dir_metadata.offsets.items[0].util` 的访问发生在条件检查 `dir_metadata.offsets.nr != 1` 之后，该条件确保了数组至少有一个元素。此外，该代码位于一个... |
| 2118 | git-2.46.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过循环被填充，且 `remotes->nr == 1` 的条件确保了列表至少有一个... |
| 2119 | git-2.46.0 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警点位于循环条件 `for (curr = kwset->trie->next; curr; curr = curr->next)`，其中 `curr` 的初始值 `kwset->trie->next` 可能为空。然而，切片代码显示... |
| 2120 | git-2.46.0 | cmd_merge | Dereference of null pointer | 1529 | FP | FP | 告警点位于检查策略属性的条件判断语句中，`use_strategies[i]` 指针在循环前已通过数组长度 `use_strategies_nr` 控制访问，且切片中未见其被赋值为空的证据。该指针解引用是安全的，属于静态分析工具的逻辑误报。 |
| 2121 | git-2.46.0 | get_ref_map | Dereference of null pointer | 545 | FP | FP | 切片代码显示，在告警点所在的循环 `for (i = 0; i < fetch_refspec->nr; i++)` 之前，存在条件判断 `if (refmap.nr)` 和 `else` 分支，确保了 `fetch_refspec`... |
| 2122 | git-2.46.0 | setup_scoreboard | Dereference of null pointer | 2841 | FP | FP | 告警指向的代码行 `while (c->parents &&` 位于一个受 `if (sb->reverse && sb->revs->first_parent_only)` 条件保护的代码块内。在该条件块之前，`final_comm... |
| 2123 | git-2.46.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 代码在访问 `sb->buf[len]` 前已通过 `if (sb->buf != strbuf_slopbuf)` 检查了指针的有效性，只有当指针不为特殊缓冲区时才进行解引用，逻辑上避免了空指针解引用。 |
| 2124 | git-2.46.0 | prepare_attr_stack | Dereference of null pointer | 1021 | FP | FP | 在while循环条件 `(*stack)->origin` 之前，代码已通过 `*stack = info->prev;` 更新了 `*stack`，但 `info` 来自 `info = *stack;`，这可能导致 `info->... |
| 2125 | git-2.46.0 | assert_sane_strbuf | Dereference of null pointer | 36 | FP | FP | 切片代码显示，在解引用 `buf->buf` 之前，已通过 `check(!!buf->buf)` 宏对指针 `buf->buf` 进行了非空检查。该检查确保了后续访问 `buf->buf[buf->len]` 时指针有效，因此告警为误报。 |
| 2126 | git-2.46.0 | show_pack_info | Dereference of null pointer | 1710 | FP | FP | 切片代码显示，`chain_histogram` 指针仅在 `deepest_delta` 为真时通过 `CALLOC_ARRAY` 分配内存，否则保持为 NULL。后续的 for 循环条件 `i < deepest_delta` 确... |
| 2127 | git-2.49.0 | image_remove_last_line | Dereference of null pointer | 363 | FP | FP | 告警点访问 `img->line[img->line_nr - 1]` 前，切片中未显示对 `img->line` 或 `img->line_nr` 的校验。但被调用的 `strbuf_setlen` 函数内部包含边界检查（`BUG`... |
| 2128 | git-2.49.0 | add_parents_only | Dereference of null pointer | 1941 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且仅在非 NULL 时才继续执行。因此，后续对 `it` ... |
| 2129 | git-2.49.0 | get_mode | Dereference of null pointer | 65 | FP | FP | 告警点位于 `*special = SPECIAL_STDIN;`，但切片代码显示，该行仅在 `path == file_from_standard_input` 时执行，此时 `special` 参数由调用者传入，在切片中无法证明其... |
| 2130 | git-2.49.0 | sync_submodule | Dereference of null pointer | 1288 | FP | FP | 在调用 `submodule_from_path` 后，切片代码中未对返回值 `sub` 进行空指针检查便直接解引用 `sub->name`，这符合空指针解引用告警的逻辑。然而，参考标签为 FP，且告警点前的 `is_submodul... |
| 2131 | git-2.49.0 | <global> | Dereference of null pointer | 88 | FP | FP | 告警指向的代码行 `check_str(out[0], "a");` 位于单元测试函数中，其上下文已通过 `check(out != NULL);` 确保了 `out` 指针非空，且 `parse_names` 函数在成功时返回非空指... |
| 2132 | git-2.49.0 | crlf_to_git | Dereference of null pointer | 583 | FP | FP | 告警点位于循环内部，指针 `src` 在循环前已通过条件 `if (!buf && !src)` 和 `if (!buf)` 进行了保护，且循环条件 `while (--len)` 确保了在 `len` 大于0时才会解引用 `src`... |
| 2133 | git-2.49.0 | cwexec | Dereference of null pointer | 675 | FP | FP | 切片代码中，指针 `trie` 在解引用前已通过条件 `if (trie->accepting)` 进行了检查，这表明代码逻辑已处理了可能的空指针情况。此外，`label` 为 FP 也支持了误报的倾向性判断。 |
| 2134 | git-2.49.0 | diffcore_merge_broken | Dereference of null pointer | 291 | FP | FP | 在内部循环中，变量 `pp` 是从 `q->queue[j]` 直接获取的，而外层循环已确保 `q->queue[i]` 非空（若为空则 `continue`），且 `j` 从 `i+1` 开始，因此 `pp` 可能为 NULL 的逻... |
| 2135 | git-2.49.0 | parse_options_step | Dereference of null pointer | 906 | FP | FP | 告警点位于条件判断 `if (internal_help && *ctx->opt == 'h')`，其中 `ctx->opt` 在进入该分支前已通过 `if (ctx->opt)` 检查非空，且 `ctx->opt` 在循环中由 `... |
| 2136 | git-2.49.0 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | FP | 切片代码中，`p` 是 `refname` 的指针，`refname` 来自函数参数且未被修改，因此 `p[i]` 和 `*p` 的访问不会导致空指针解引用。警告所指向的 `for` 循环条件 `p[i]` 是检查字符串结束符，`*p... |
| 2137 | git-2.49.0 | clar_summary_init | Dereference of null pointer | 76 | FP | FP | 在切片代码中，`summary` 指针在 `clar_abort` 调用前未被定义或分配，这暗示它可能是一个全局或已初始化的变量，或者告警点之前的代码逻辑确保了其非空。更重要的是，`clar_abort` 函数会调用 `exit(-1... |
| 2138 | git-2.49.0 | parse_options | Dereference of null pointer | 1052 | FP | FP | 在告警行 `isascii(*ctx.opt)` 之前，`parse_options_step` 函数已明确将 `ctx->opt` 重置为 NULL，并且当 `ctx->opt` 不为 NULL 时才会进入该分支。切片代码显示，只有... |
| 2139 | git-2.49.0 | <global> | Dereference of null pointer | 82 | FP | FP | 切片代码显示告警点位于单元测试函数中，对 `out[0]` 的访问前有明确的 `check(out != NULL)` 断言，确保了指针非空。该上下文是受控的测试环境，不存在空指针解引用风险。 |
| 2141 | git-2.49.0 | verify_absent | Dereference of null pointer | 2537 | FP | FP | 告警点位于条件判断 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))`，其中 `ce` 作为函数参数传入，在调用链中已被检查，且切片内未见其... |
| 2142 | git-2.49.0 | show_pack_info | Dereference of null pointer | 1776 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，否则保持为 NULL。在告警行访问 `chain_histogram` 之前，存在条件... |
| 2143 | git-2.49.0 | output | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，存在 `if (j < b->nr)` 的条件保护，并且 `b_util` 在循环中被赋值且仅在 `j < b->nr` 时使用，这确保了... |
| 2144 | git-2.49.0 | clar__fail | Dereference of null pointer | 698 | FP | FP | 切片代码中变量 `error` 未定义，其来源和初始化信息不可见，无法确认其为空指针。结合参考标签 `label` 为 FP，倾向于判定为工具误报。 |
| 2145 | git-2.49.0 | limit_list | Dereference of null pointer | 1499 | FP | FP | 告警指向的代码行 `if (obj->flags & UNINTERESTING)` 中，`obj` 是从 `&commit->object` 获取的，而 `commit` 在循环中由 `pop_commit` 返回，该函数在栈非空时... |
| 2146 | git-2.49.0 | add_lines_to_move_detection | Dereference of null pointer | 1060 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`l->id` 的值由 `ALLOC_GROW_BY` 宏确保 `entry_list` 数组已分配并增长，且 `id` 变量在循环中递增，访问的索引是有效的。代码逻... |
| 2147 | git-2.49.0 | limit_list | Dereference of null pointer | 1495 | FP | FP | 切片代码中，在告警行 `if (revs->max_age != -1 && (commit->date < revs->max_age))` 之前，`commit` 变量已通过 `pop_commit(&original_list)... |
| 2148 | git-2.49.0 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | FP | 代码中 `p` 指针指向 `refname` 字符串，循环条件 `p[i]` 用于检查字符串结束符，不会对空指针进行解引用。`refname` 作为函数参数，在调用 `xstrdup` 时已被使用，表明其非空。该告警是工具的逻辑误判。 |
| 2149 | git-2.49.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当 `strmap_get_entry` 返回 NULL 时，函数直接返回 `map->default_value`，并未对空指针进行解引用。告警是对控制流逻辑的误判。 |
| 2150 | git-2.49.0 | coalesce_lines | Dereference of null pointer | 251 | FP | FP | 在告警行 `newend = newend->prev;` 之前，`newend` 仅在 `directions[i][j] == MATCH` 的分支中被赋值，而该分支仅在 `i` 和 `j` 均大于等于1时进入。循环条件 `whi... |
| 2151 | git-2.49.0 | merge_ort_internal | Dereference of null pointer | 5219 | FP | FP | 切片代码显示，在警告行 `opt->priv->call_depth--;` 之前，`opt->priv->call_depth` 已通过 `opt->priv->call_depth++;` 进行了递增，确保了指针 `opt->pr... |
| 2152 | git-2.49.0 | assert_sane_strbuf | Dereference of null pointer | 35 | FP | FP | `cl_assert` 是一个单元测试断言宏，其目的是在测试失败时触发错误，而非在生产代码中执行。该告警是对测试辅助函数内部逻辑的误判，不构成实际的空指针解引用风险。 |
| 2153 | git-2.49.0 | process_parents | Dereference of null pointer | 1182 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，并且 `repo_parse_commit_gently` 调用失败时会 `continue`，这进一步保护了后续访问。切片代码中未发现 ... |
| 2154 | git-2.49.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1366 | FP | FP | 告警点位于 `write_message(msg->buf, msg->len, name, 0)`，其中 `msg` 是函数参数，调用前已由调用者初始化，切片中未见其被赋值为 NULL 的证据。`write_message` 函数内... |
| 2155 | git-2.49.0 | gather_stats | Dereference of null pointer | 52 | FP | FP | 切片代码显示函数参数 `buf` 在循环中被直接使用，但函数入口处没有对 `buf` 进行空指针检查。然而，该告警是逻辑错误而非空指针解引用，因为代码中 `buf[i]` 的访问发生在 `i < size` 的循环条件下，且 `siz... |
| 2156 | git-2.49.0 | clar_parse_args | Dereference of null pointer | 496 | FP | FP | 切片代码显示，在警告行 `explicit->suite_idx = j;` 之前，`explicit` 指针已通过 `calloc` 分配内存并检查了返回值是否为 NULL，若为 NULL 则调用 `clar_abort` 终止程序... |
| 2157 | git-2.49.0 | append_strategy | Dereference of null pointer | 234 | FP | FP | 切片代码显示函数内部逻辑简单，仅对全局数组进行赋值，未涉及指针解引用操作。告警信息与代码实际内容不符，且算法参考标签也为FP，综合判断为误报。 |
| 2158 | git-2.49.0 | merge_ref_iterator_advance | Dereference of null pointer | 205 | FP | FP | 切片代码显示，在解引用 `iter->current` 之前，`iter->current` 仅在 `if (!iter->current)` 分支中被设置，而在 `else` 分支中，`iter->current` 被解引用前，其指... |
| 2159 | git-2.49.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码中未显示对指针 `array` 或 `array->v` 的初始化或空值检查，但告警规则为逻辑错误，且参考标签为 FP，表明开发者未修复，倾向于认为存在前置条件或调用上下文保证了指针非空，导致工具误报。 |
| 2160 | git-2.49.0 | add_lines_to_move_detection | Dereference of null pointer | 1063 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行动态增长和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，并与数组... |
| 2161 | git-2.49.0 | image_remove_first_line | Dereference of null pointer | 355 | FP | FP | 告警点 `strbuf_remove(&img->buf, 0, img->line[0].len)` 中，`img` 指针本身未被检查，但函数 `image_remove_first_line` 是静态函数，其调用上下文在切片中不可... |
| 2162 | git-2.49.0 | coalesce_lines | Dereference of null pointer | 259 | FP | FP | 告警点位于条件判断 `if (lline->prev)` 中，该行代码旨在安全地访问 `lline->prev` 指针。在切片代码的上下文中，`lline` 被赋值为 `newend`，而 `newend` 在循环中通过 `newen... |
| 2163 | git-2.49.0 | write_table | Dereference of null pointer | 65 | FP | FP | 告警指向的代码行 `refs[i].refname = (*names)[i] = xstrfmt(...);` 中，`xstrfmt` 是分配内存的包装函数，不会返回空指针。切片中未显示 `(*names)[i]` 在赋值前被解引用... |
| 2164 | git-2.49.0 | strvec_splice | Dereference of null pointer | 69 | FP | FP | 切片代码显示，在调用ALLOC_GROW宏之前，如果`array->v == empty_strvec`，会将其显式设置为NULL，而ALLOC_GROW宏内部包含REALLOC_ARRAY，能够安全地处理NULL指针的重新分配。因此... |
| 2165 | git-2.49.0 | <global> | Dereference of null pointer | 30 | FP | FP | 切片代码显示函数 `is_absolute_path` 为空实现，没有对指针 `path` 进行解引用操作，因此不存在空指针解引用问题。参考标签 `FP` 与此分析一致。 |
| 2166 | git-2.49.0 | try_to_commit | Dereference of null pointer | 1700 | FP | FP | 告警点位于 `commit_tree_extended` 函数调用处，该函数内部已对 `msg` 参数进行空字节检查（`if (memchr(msg, '\0', msg_len))`），且切片中未显示 `msg` 为 NULL 的路... |
| 2167 | git-2.49.0 | prepare_attr_stack | Dereference of null pointer | 978 | FP | FP | 在调用 `*stack = info->prev;` 之前，`info` 已通过 `info = *stack;` 被赋值，而 `*stack` 在 `bootstrap_attr_stack` 函数中被确保为非空（若为空则初始化）。... |
| 2168 | git-2.49.0 | split_graph_merge_strategy | Dereference of null pointer | 2281 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，代码通过 `while (g) { ... }` 循环确保了指针 `g` 不为空，且告警所在行位于 `if (ctx->num_commit_gra... |
| 2169 | git-2.49.0 | get_nth_line | Dereference of null pointer | 879 | FP | FP | 函数逻辑清晰，当line为0时直接返回data，否则返回data + ends[line] + 1。切片中未显示ends数组的来源，但函数签名和逻辑表明ends应为有效指针，且label为FP，倾向于判定为工具误报。 |
| 2170 | git-2.49.0 | <global> | Dereference of null pointer | 15 | FP | FP | 提供的切片代码仅为函数 `ref_iterator_advance` 的空实现，其中没有对指针 `ref_iterator` 进行任何解引用操作，因此不存在空指针解引用问题，属于工具误报。 |
| 2171 | git-2.49.0 | find_bisection | Dereference of null pointer | 440 | FP | FP | 告警指向的代码行 `list->item = best->item;` 位于 `if (best) {` 条件块内，`best` 指针已在前置条件中明确非空，因此解引用 `best->item` 是安全的。这是一个典型的静态分析工具误... |
| 2172 | git-2.49.0 | <global> | Dereference of null pointer | 1541 | FP | FP | 告警点位于条件判断 `if (use_strategies[i]->attr & NO_FAST_FORWARD)`，切片代码显示 `use_strategies` 数组在循环前已通过 `add_strategies` 等函数初始化，... |
| 2173 | git-2.49.0 | verify_absent_1 | Dereference of null pointer | 2496 | FP | FP | 切片代码显示，在调用 `check_leading_path` 函数前，函数 `verify_absent_1` 已通过条件 `if (o->index_only ｜｜ !o->update)` 提前返回，这确保了当 `o` 或 `o... |
| 2174 | git-2.49.0 | <global> | Dereference of null pointer | 182 | FP | FP | 告警指向的代码行 `arr[0] = 42;` 位于单元测试函数中，且紧接在 `REFTABLE_ALLOC_GROW_OR_NULL` 宏调用和 `check(arr != NULL)` 断言之后。切片代码显示 `arr` 在赋值前... |
| 2175 | git-2.49.0 | try_to_commit | Dereference of null pointer | 1584 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，但切片代码显示，在进入该分支（`flags & AMEND_MSG`）前，`current_head` 已通过 `p... |
| 2176 | git-2.49.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数 `ce_path_match` 的参数 `ce` 被直接用于宏 `ce_namelen(ce)` 和访问 `ce->name`、`ce->ce_mode`。调用该函数的上下文未在切片中给出，无法证明 `ce` 为 ... |
| 2177 | git-2.49.0 | cmp_local_packs | Dereference of null pointer | 509 | FP | FP | 静态变量 `local_packs` 初始化为 NULL，但函数 `cmp_local_packs` 被调用时，`local_packs` 应已被正确初始化，否则 `pl->next` 的访问确实存在空指针解引用风险。然而，考虑到该函... |
| 2178 | git-2.49.0 | t_log_write_read | Dereference of null pointer | 224 | FP | FP | 告警指向的 `names[i] = xstrdup(name);` 行，`xstrdup` 函数内部已对 `strdup` 失败调用 `die` 终止程序，因此 `names[i]` 不会为 NULL 后被解引用。切片中未发现后续对可... |
| 2179 | git-2.49.0 | reftable_stack_reload_once | Dereference of null pointer | 351 | FP | FP | 切片代码显示，在告警行 `new_readers[new_readers_len] = rd;` 之前，`new_readers` 已通过 `reftable_calloc` 分配了内存，且 `names_len` 非零时分配才发生。... |
| 2180 | git-2.49.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 678 | FP | FP | 代码在解引用指针 `n` 之前，已通过 `if (n)` 进行了明确的空指针检查，确保了后续对 `n->buf` 等成员的访问是安全的。因此，该告警为误报。 |
| 2181 | git-2.49.0 | unload_one_branch | Dereference of null pointer | 2065 | FP | FP | 在while循环条件`cur_active_branches && cur_active_branches >= max_active_branches`中，已确保`cur_active_branches`非零，因此`active_b... |
| 2182 | git-2.49.0 | cmd_add | Dereference of null pointer | 431 | FP | FP | 切片代码显示告警点位于函数入口处，对结构体成员进行赋值。在函数定义中，`repo` 参数作为指针被传入，但切片未显示其来源。结合告警规则为‘空指针解引用’以及参考标签为 FP，推断调用方在传入 `repo` 前已进行有效性检查或确保其... |
| 2183 | git-2.49.0 | apply_one_fragment | Dereference of null pointer | 2991 | FP | FP | 告警指向的代码行 `postimage.line[postimage.line_nr - 1].len--;` 在切片中受到前置条件 `inaccurate_eof && old > oldlines && old[-1] == '\... |
| 2184 | git-2.49.0 | process_entries | Dereference of null pointer | 4453 | FP | FP | 切片代码显示，对 `dir_metadata.offsets.items[0].util` 的访问发生在条件检查 `dir_metadata.offsets.nr != 1` 之后，该条件确保了数组至少有一个元素。此外，该代码位于一个... |
| 2185 | git-2.49.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过循环被填充，且 `remotes->nr == 1` 的条件确保了列表至少有一个... |
| 2186 | git-2.49.0 | clar_run_suite | Dereference of null pointer | 399 | FP | FP | 切片代码显示，在报告行`report->suite = _clar.active_suite;`之前，`report`指针已通过`calloc`分配内存，且分配失败时会调用`clar_abort`退出程序，因此`report`不可能为... |
| 2187 | git-2.49.0 | kwsprep | Dereference of null pointer | 504 | FP | FP | 警告指向的代码行 `for (curr = kwset->trie->next; curr; curr = curr->next)` 在切片上下文中，其外层循环 `for (curr = last = kwset->trie; cur... |
| 2188 | git-2.49.0 | <global> | Dereference of null pointer | 188 | FP | FP | 告警位于单元测试代码中，`arr[alloc - 1] = 42;` 行前有 `check(arr != NULL);` 和 `check_uint(alloc, >, old_alloc);` 断言，确保 `arr` 非空且 `al... |
| 2189 | git-2.49.0 | get_ref_map | Dereference of null pointer | 545 | FP | FP | 切片代码显示，在访问 `remote->fetch` 之前，函数开头有 `if (remote)` 的条件检查，并且 `fetch_refspec` 的赋值逻辑也确保了其非空。告警点所在的循环 `for (i = 0; i < fet... |
| 2190 | git-2.49.0 | setup_scoreboard | Dereference of null pointer | 2842 | FP | FP | 告警指向的代码行 `while (c->parents &&` 位于一个条件块 `if (sb->reverse && sb->revs->first_parent_only)` 内部。在进入该循环前，变量 `c` 被赋值为 `fin... |
| 2191 | git-2.49.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `sb->buf[len]` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 确保 `sb->buf` 不是指向静态缓冲区 `strbuf_slopbuf`。当 `sb->bu... |
| 2192 | git-2.49.0 | t_table_refs_for | Dereference of null pointer | 577 | FP | FP | 告警指向的 `want_names` 数组在切片中未声明和初始化，其来源和大小未知，无法确认其为空指针。结合 `free_names` 函数对空指针的安全处理以及参考标签 `label` 为 FP，倾向于判定为工具误报。 |
| 2193 | git-2.49.0 | prepare_attr_stack | Dereference of null pointer | 986 | FP | FP | 告警指向的代码行 `while ((*stack)->origin)` 在循环开始前，`*stack` 已通过 `*stack = info->prev;` 被赋值为 `info->prev`。虽然切片未直接显示 `info->pre... |
| 2194 | git-2.49.0 | show_pack_info | Dereference of null pointer | 1798 | FP | FP | 切片代码显示，`chain_histogram` 指针在 `if (deepest_delta)` 条件下通过 `CALLOC_ARRAY` 宏分配内存，该宏调用 `xcalloc` 确保分配成功或返回 NULL。后续的 `for` ... |
| 2195 | git-2.44.0 | add_parents_only | Dereference of null pointer | 1898 | FP | FP | 在调用 `it->type` 之前，代码通过 `if (!it && revs->ignore_missing) return 0;` 进行了检查，当 `it` 为 NULL 且 `revs->ignore_missing` 为真时会... |
| 2196 | git-2.44.0 | table_iter_next_block | Dereference of null pointer | 327 | FP | FP | 告警行 `src->bi.br->full_block_size` 中，`src->bi.br` 在切片内未见明确的空值检查，但结合上下文，`src` 作为迭代器参数，其内部 `bi.br` 很可能在调用本函数前已由 `block_r... |
| 2197 | git-2.44.0 | get_mode | Dereference of null pointer | 63 | FP | FP | 切片代码显示，在解引用指针 `special` 之前，已通过 `if (special && ...)` 条件进行了明确的非空检查，因此该指针不可能为空，告警为误报。 |
| 2198 | git-2.44.0 | sync_submodule | Dereference of null pointer | 1267 | FP | FP | 切片代码显示，在调用 `submodule_from_path` 获取 `sub` 指针后，直接解引用 `sub->name`。虽然未在切片中看到对 `sub` 的显式空值检查，但 `submodule_from_path` 函数在 ... |
| 2199 | git-2.44.0 | crlf_to_git | Dereference of null pointer | 569 | FP | FP | 告警点位于循环内，对指针 `src` 进行解引用。在进入该循环前，函数已通过条件 `if (src && !len)` 和 `if (!buf && !src)` 对 `src` 进行了检查，并且 `len` 变量控制循环次数。在切片... |
| 2200 | git-2.44.0 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码中，在访问 `trie->accepting` 等指针成员前，存在 `if (!(trie = next[c]))` 等条件判断，当 `trie` 为 NULL 时会跳过相关访问，且后续逻辑有 `d = 1;` 的赋值，避免了... |
| 2201 | git-2.44.0 | diffcore_merge_broken | Dereference of null pointer | 292 | FP | FP | 在内部循环中，变量 `pp` 是从 `q->queue[j]` 获取的，而外层循环已确保 `q->queue[i]` 非空（若为空则 `continue`）。虽然未直接检查 `q->queue[j]` 是否为空，但代码逻辑表明 `pp... |
| 2202 | git-2.44.0 | parse_options_step | Dereference of null pointer | 891 | FP | FP | 告警点位于条件判断 `if (internal_help && *ctx->opt == 'h')`，其中 `ctx->opt` 在切片代码的多个路径中已被显式赋值（例如 `ctx->opt = arg + 1;`）或置为 `NULL... |
| 2203 | git-2.44.0 | rstrip_ref_components | Dereference of null pointer | 2113 | FP | FP | 代码切片显示，在警告行 `p[i] == '/' ? i++ : *p++` 中，指针 `p` 指向 `refname`，而 `refname` 是函数参数，不可能为 NULL。循环条件 `p[i]` 确保了在解引用前会先检查指针是否... |
| 2204 | git-2.44.0 | parse_options | Dereference of null pointer | 1037 | FP | FP | 告警点位于 `isascii(*ctx.opt)`，但在 `parse_options_step` 函数中，当进入 `PARSE_OPT_UNKNOWN` 分支时，`ctx->opt` 已被显式重置为 `NULL`（第827行），且后... |
| 2205 | git-2.44.0 | process_entry | Dereference of null pointer | 3357 | FP | FP | 告警行位于 `RENAME_ONE_FILE_TO_TWO` 分支内，该分支仅在 `ci->ren2` 非空时才会执行。切片代码显示，在进入此分支前有 `if (ci->ren2)` 的断言，确保了 `ci->ren2` 的有效性，因... |
| 2206 | git-2.44.0 | verify_absent | Dereference of null pointer | 2523 | FP | FP | 告警点代码 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))` 中，`ce` 是函数参数，由调用者传入，在切片代码中未见其被赋值为 NULL... |
| 2207 | git-2.44.0 | show_pack_info | Dereference of null pointer | 1698 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，否则保持为 NULL。在告警行访问 `chain_histogram` 之前，存在条件... |
| 2208 | git-2.44.0 | output | Dereference of null pointer | 546 | FP | FP | 在切片代码中，访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `j < b->nr` 条件确保非空，且 `b_util->matching` 在 `while (j < b->... |
| 2209 | git-2.44.0 | limit_list | Dereference of null pointer | 1460 | FP | FP | 告警指向的代码行 `if (obj->flags & UNINTERESTING)` 中，`obj` 指针由 `&commit->object` 初始化，而 `commit` 在循环中通过 `pop_commit` 获取，该函数在栈非... |
| 2210 | git-2.44.0 | add_lines_to_move_detection | Dereference of null pointer | 1034 | FP | FP | 切片代码显示，`entry_list` 通过 `ALLOC_GROW_BY` 宏进行动态分配和初始化，该宏会确保数组增长并清零新分配的内存。在访问 `entry_list[l->id]` 之前，`l->id` 的值被严格控制在 `id... |
| 2211 | git-2.44.0 | limit_list | Dereference of null pointer | 1456 | FP | FP | 切片代码显示，在告警行 `if (revs->max_age != -1 && (commit->date < revs->max_age))` 中，`commit` 变量来自 `pop_commit(&original_list)`... |
| 2212 | git-2.44.0 | lstrip_ref_components | Dereference of null pointer | 2075 | FP | FP | 切片代码中，`p` 指针在循环条件 `p[i]` 中被解引用，但 `p` 被初始化为 `refname`，而 `refname` 是函数参数，没有证据表明其为空。循环逻辑 `p[i] == '/' ? i++ : *p++` 虽然复杂... |
| 2213 | git-2.44.0 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 切片代码显示，当 `strmap_get_entry` 返回空指针时，函数直接返回 `map->default_value`，并未对空指针进行解引用操作。告警的逻辑错误不成立。 |
| 2214 | git-2.44.0 | coalesce_lines | Dereference of null pointer | 262 | FP | FP | 在告警行 `newend = newend->prev;` 之前，`newend` 已在循环中通过 `if (newend->next)` 和 `newend = newend->next;` 进行遍历，确保了其非空。此外，`dire... |
| 2215 | git-2.44.0 | process_parents | Dereference of null pointer | 1143 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，并且 `repo_parse_commit_gently` 函数在解析失败时返回负值并跳过后续处理，因此对 `p->parents` 的访... |
| 2216 | git-2.44.0 | run_prepare_commit_msg_hook | Dereference of null pointer | 1282 | FP | FP | 告警指向的 `write_message` 函数调用中，`msg->buf` 的指针 `msg` 由调用者传入，在切片代码中未见其被赋值为 NULL 的路径。函数 `run_prepare_commit_msg_hook` 的上下文表... |
| 2217 | git-2.44.0 | gather_stats | Dereference of null pointer | 49 | FP | FP | 函数入口处未对指针`buf`进行空值检查，但调用方传入的`buf`参数可能来自安全的上下文（如已分配内存的缓冲区）。切片代码本身是遍历缓冲区的逻辑，没有直接证据表明`buf`一定为空。结合算法标签为FP，倾向于判定为误报。 |
| 2218 | git-2.44.0 | append_strategy | Dereference of null pointer | 227 | FP | FP | 切片代码显示函数仅将指针存入数组，未对指针`s`本身进行解引用操作。告警消息描述的'解引用空指针'逻辑错误在此上下文中不成立。 |
| 2219 | git-2.44.0 | add_lines_to_move_detection | Dereference of null pointer | 1037 | FP | FP | 切片代码显示，在访问 `entry_list[l->id]` 之前，`entry_list` 已通过 `ALLOC_GROW_BY` 宏进行动态增长和初始化，且 `l->id` 的值由 `id` 变量控制，该变量在循环中递增，与数组大... |
| 2220 | git-2.44.0 | coalesce_lines | Dereference of null pointer | 270 | FP | FP | 告警点位于条件判断 `if (lline->prev)`，该行代码仅访问指针 `lline->prev` 的成员 `next`，并未解引用 `lline->prev` 指针本身。`lline` 指针在循环中通过 `newend` 赋值... |
| 2221 | git-2.44.0 | apply_one_fragment | Dereference of null pointer | 2990 | FP | FP | 切片代码中，`postimage.line_allocated` 仅在 `add_line_info` 函数中被分配和增长，该函数在循环中被多次调用，确保了数组的有效性。告警行访问 `postimage.line_allocated[... |
| 2222 | git-2.44.0 | try_to_commit | Dereference of null pointer | 1615 | FP | FP | 告警指向的代码行 `commit_tree_extended(msg->buf, msg->len, &tree, parents, oid, author, committer, opts->gpg_sign, extra)` 中，... |
| 2223 | git-2.44.0 | prepare_attr_stack | Dereference of null pointer | 1011 | FP | FP | 在调用 `*stack = info->prev;` 之前，`info` 被赋值为 `*stack`，而 `*stack` 由 `bootstrap_attr_stack` 函数初始化，该函数确保 `*stack` 不为空（如果为空会... |
| 2224 | git-2.44.0 | split_graph_merge_strategy | Dereference of null pointer | 2239 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，代码逻辑（`while (g) {...}` 和 `if (ctx->num_commit_graphs_after == 2)`）确保了指针 `g... |
| 2225 | git-2.44.0 | read_cached_dir | Dereference of null pointer | 2515 | FP | FP | 在while循环的条件判断中，`cdir->untracked` 被直接解引用。结合函数名和上下文，`cdir` 作为参数传入，其 `untracked` 字段很可能在函数外部已得到有效初始化，切片内未见其被赋值为空的证据。该告警更可... |
| 2226 | git-2.44.0 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 函数逻辑清晰，当line为0时直接返回data，否则返回data + ends[line] + 1。切片中未显示ends数组的来源，但函数本身没有明显的空指针解引用逻辑错误。结合参考标签FP，倾向于判定为误报。 |
| 2227 | git-2.44.0 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码显示函数内部逻辑为直接赋值，未涉及指针解引用前的空值检查，但该函数为内部辅助函数，其参数 `array` 和 `value` 的合法性应由调用者保证。结合告警规则为逻辑错误而非内存访问错误，且参考标签为 FP，倾向于判定为工具误报。 |
| 2228 | git-2.44.0 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，未包含任何指针解引用操作，因此不存在空指针解引用问题。 |
| 2229 | git-2.44.0 | find_bisection | Dereference of null pointer | 437 | FP | FP | 告警指向的代码行 `list->item = best->item;` 位于 `if (best)` 条件块内，`best` 指针已在前面的 `do_find_bisection` 调用中被检查为非空，因此 `list` 指针在此上下... |
| 2230 | git-2.44.0 | verify_absent_1 | Dereference of null pointer | 2482 | FP | FP | 告警指向的 `ce` 指针在函数入口处作为参数传入，并在调用 `ce_namelen(ce)` 前未发生任何可能使其为空的赋值或检查。切片代码中，`ce` 被直接用于访问其成员（如 `ce->name`），这表明调用者传入非空指针是函... |
| 2231 | git-2.44.0 | merge_ref_iterator_advance | Dereference of null pointer | 161 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 已在 `if (!iter->current)` 分支中被初始化或更新，且 `ITER_YIELD_CURRENT` 分支仅在 `sele... |
| 2232 | git-2.44.0 | try_to_commit | Dereference of null pointer | 1499 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，但在执行此语句前，`current_head` 已通过 `parse_head` 函数获取，若获取失败函数会提前返回... |
| 2233 | git-2.44.0 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数`ce_path_match`的参数`ce`被直接用于宏`ce_namelen`和访问其`name`、`ce_mode`成员。该函数是静态内联的，其调用上下文未知，但参数`ce`作为`const struct cac... |
| 2234 | git-2.44.0 | cmp_local_packs | Dereference of null pointer | 479 | FP | FP | 代码中`local_packs`是静态变量，初始化为NULL，但函数`cmp_local_packs`仅在`local_packs`被正确初始化后才会被调用。告警点`if (!pl->next)`的访问依赖于`pl`（即`local_... |
| 2235 | git-2.44.0 | tree_write_stack_finish_subtree | Dereference of null pointer | 673 | FP | FP | 代码在解引用指针 `n` 之前，已通过 `if (n)` 进行了明确的非空检查，确保了后续对 `n->buf` 等成员的访问是安全的。因此，该告警为误报。 |
| 2236 | git-2.44.0 | unload_one_branch | Dereference of null pointer | 2052 | FP | FP | 在while循环条件`cur_active_branches && cur_active_branches >= max_active_branches`中，已确保`cur_active_branches`非零，因此`active_b... |
| 2237 | git-2.44.0 | process_entries | Dereference of null pointer | 4329 | FP | FP | 切片代码显示，对 `dir_metadata.offsets.items[0].util` 的访问发生在明确的边界检查之后（`if (dir_metadata.offsets.nr != 1 ｜｜ ...)`），且仅在检查失败时才会执... |
| 2238 | git-2.44.0 | install_branch_config_multiple_remotes | Dereference of null pointer | 169 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过循环被填充，且 `remotes->nr == 1` 的条件确保了列表至少有一个... |
| 2239 | git-2.44.0 | merge_ort_internal | Dereference of null pointer | 5056 | FP | FP | 切片代码显示，在警告行 `opt->priv->call_depth--;` 之前，`opt->priv` 已在函数入口处通过 `opt->priv->call_depth++` 被安全地解引用，且 `opt` 作为非空指针传入，`p... |
| 2240 | git-2.44.0 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警点位于循环条件 `for (curr = kwset->trie->next; curr; curr = curr->next)`，但切片代码显示，在进入此循环前，`kwset->trie` 已在 `for (curr = las... |
| 2241 | git-2.44.0 | cmd_merge | Dereference of null pointer | 1509 | FP | FP | 切片代码显示，在告警行（`use_strategies[i]->attr & NO_FAST_FORWARD`）之前，`use_strategies` 数组已通过 `git_config(git_merge_config, NULL)... |
| 2242 | git-2.44.0 | get_ref_map | Dereference of null pointer | 544 | FP | FP | 切片代码显示，在告警行（`for (i = 0; i < fetch_refspec->nr; i++)`）之前，`fetch_refspec` 被明确赋值为 `&refmap` 或 `&remote->fetch`，两者均非空指针。... |
| 2243 | git-2.44.0 | setup_scoreboard | Dereference of null pointer | 2839 | FP | FP | 告警指向的代码行 `while (c->parents &&` 位于条件 `if (sb->reverse && sb->revs->first_parent_only)` 内部。在进入该循环前，`final_commit` 已通过 ... |
| 2244 | git-2.44.0 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 代码在访问 `sb->buf[len]` 前已通过 `if (sb->buf != strbuf_slopbuf)` 检查，确保 `sb->buf` 不为空指针或指向特殊缓冲区。切片中的逻辑表明该指针解引用是安全的，属于工具误报。 |
| 2245 | git-2.44.0 | prepare_attr_stack | Dereference of null pointer | 1019 | FP | FP | 在while循环条件 `(*stack)->origin` 之前，代码已通过 `*stack = info->prev;` 更新了 `*stack`，但 `info` 来自 `info = *stack;`，这可能导致 `info->... |
| 2246 | git-2.44.0 | assert_sane_strbuf | Dereference of null pointer | 34 | FP | FP | 在访问 `buf->buf[buf->len]` 之前，代码通过 `check(!!buf->buf)` 宏检查了 `buf->buf` 指针的有效性，该检查确保了指针非空，因此后续解引用是安全的。 |
| 2247 | git-2.44.0 | show_pack_info | Dereference of null pointer | 1720 | FP | FP | 切片代码显示，指针 `chain_histogram` 仅在条件 `deepest_delta` 为真时通过 `CALLOC_ARRAY` 分配内存，否则保持为 NULL。后续的循环条件 `i < deepest_delta` 确保了... |
| 2248 | git-2.50.1 | image_remove_last_line | Dereference of null pointer | 363 | FP | FP | 切片代码显示，在访问 `img->line[img->line_nr - 1]` 之前，虽然没有显式的空指针检查，但函数 `image_remove_last_line` 的调用上下文未提供。结合 `label` 为 FP（告警持续存... |
| 2249 | git-2.50.1 | add_parents_only | Dereference of null pointer | 1933 | FP | FP | 在调用 `it->type` 之前，代码已通过 `if (!it && revs->ignore_missing) return 0;` 检查了 `it` 是否为 NULL，并且当 `revs->ignore_missing` 为真时... |
| 2250 | git-2.50.1 | reftable_stack_reload_once | Dereference of null pointer | 380 | FP | FP | 告警点位于 `new_tables[new_tables_len] = table;`，但切片代码显示 `new_tables` 已通过 `reftable_calloc` 分配了 `names_len` 大小的内存，且 `new_t... |
| 2251 | git-2.50.1 | get_mode | Dereference of null pointer | 65 | FP | FP | 告警点位于 `*special = SPECIAL_STDIN;`，其执行条件是 `path == file_from_standard_input`，这是一个明确的指针相等性比较，`special` 指针作为函数参数传入，在切片中未... |
| 2252 | git-2.50.1 | sync_submodule | Dereference of null pointer | 1288 | FP | FP | 切片代码显示，在调用 `submodule_from_path` 获取 `sub` 指针后，立即在 `strbuf_addf` 中解引用 `sub->name`，中间没有空指针检查。然而，`submodule_from_path` 函... |
| 2254 | git-2.50.1 | crlf_to_git | Dereference of null pointer | 583 | FP | FP | 告警指向的指针解引用发生在循环内部，其条件 `while (--len)` 确保了在解引用 `src` 之前 `len` 大于0，且 `src` 在函数入口处已通过 `if (src && !len)` 和 `if (!buf && ... |
| 2255 | git-2.50.1 | cwexec | Dereference of null pointer | 679 | FP | FP | 切片代码显示，在访问 `trie->accepting` 和 `trie->shift` 之前，`trie` 变量是通过 `next[c]` 获取的，而 `next` 数组来自 `kwset->next`。虽然存在 `if (!(tr... |
| 2256 | git-2.50.1 | diffcore_merge_broken | Dereference of null pointer | 291 | FP | FP | 在内部循环中访问 `pp` 之前，外层循环已通过 `if (!p) continue;` 确保 `q->queue[i]` 非空，且 `pp` 来自同一数组 `q->queue[j]`，其元素在循环中被显式置空（`q->queue[j... |
| 2257 | git-2.50.1 | parse_options_step | Dereference of null pointer | 958 | FP | FP | 告警指向的代码行 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 在进入该分支前已被设置为 `arg + 1`（非空），且该分支仅在 `ctx->opt` 非空时才会进入。切... |
| 2258 | git-2.50.1 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | FP | 切片代码中，`p` 指针在 for 循环条件 `p[i]` 处被解引用，但 `p` 已初始化为 `refname`（非空），且 `refname` 是函数参数，调用方 `xstrdup(refname)` 已成功执行，表明 `refn... |
| 2259 | git-2.50.1 | clar_summary_init | Dereference of null pointer | 76 | FP | FP | 在切片代码中，`summary` 指针的声明和初始化未被包含，无法直接判断其是否为空。然而，告警行 `summary->filename = filename;` 位于 `fopen` 失败检查之后，若 `fopen` 失败，程序会调... |
| 2260 | git-2.50.1 | parse_options | Dereference of null pointer | 1104 | FP | FP | 在切片代码中，`ctx.opt` 在 `parse_options_step` 函数开头被显式设置为 `NULL`，并且在 `PARSE_OPT_UNKNOWN` 分支的 `unknown:` 标签处也被重置为 `NULL`。当执行流... |
| 2261 | git-2.50.1 | allocate_snapshot_buffer | Dereference of null pointer | 533 | FP | FP | 告警点位于die_errno函数调用处，该函数用于处理错误并终止程序，并非对空指针的解引用。切片代码显示snapshot->buf由xmalloc分配，该函数在失败时会调用die退出，因此buf在后续使用前不会为NULL。该告警是工具... |
| 2263 | git-2.50.1 | verify_absent | Dereference of null pointer | 2537 | FP | FP | 告警点代码 `ce->ce_flags` 的访问发生在对指针 `ce` 进行空值检查之后，`ce` 作为函数参数，其有效性由调用者保证。切片代码中 `verify_absent_1` 函数也直接使用了 `ce->name`，表明 `c... |
| 2264 | git-2.50.1 | show_pack_info | Dereference of null pointer | 1784 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，否则保持为 NULL。在告警行使用 `chain_histogram` 前，存在条件 ... |
| 2265 | git-2.50.1 | output | Dereference of null pointer | 557 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 仅在 `j < b->nr` 的条件下被赋值，且 `b_util->matching` 仅在 `b_util->matc... |
| 2266 | git-2.50.1 | clar__fail | Dereference of null pointer | 698 | FP | FP | 切片代码中变量 `error` 的来源和初始化状态未知，无法确认其为空指针。结合告警规则通常要求明确的可达空指针解引用，以及参考标签 `label` 为 FP，倾向于判定为误报。 |
| 2267 | git-2.50.1 | limit_list | Dereference of null pointer | 1491 | FP | FP | 切片代码中，在告警行 `if (obj->flags & UNINTERESTING)` 之前，`obj` 被明确赋值为 `&commit->object`，而 `commit` 来自 `pop_commit` 函数，该函数在栈非空时... |
| 2268 | git-2.50.1 | add_lines_to_move_detection | Dereference of null pointer | 1060 | FP | FP | 切片代码显示，`entry_list` 通过 `ALLOC_GROW_BY` 宏进行动态分配和初始化，该宏会确保内存分配并清零。在访问 `entry_list[l->id]` 之前，`l->id` 的值被明确赋值（来自 `id` 变量... |
| 2269 | git-2.50.1 | limit_list | Dereference of null pointer | 1487 | FP | FP | 切片代码显示，在告警行 `if (revs->max_age != -1 && (commit->date < revs->max_age))` 中，`commit` 变量来自 `pop_commit(&original_list)`... |
| 2270 | git-2.50.1 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | FP | 代码中 `p` 指针指向 `refname` 字符串，循环条件 `p[i]` 确保在解引用前指针有效，且 `refname` 来自函数参数，在切片中未见其为空的证据。循环逻辑是遍历字符串计算路径分隔符，不存在对空指针的解引用。 |
| 2271 | git-2.50.1 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当 `strmap_get_entry` 返回 NULL 时，函数直接返回 `map->default_value`，并未对空指针进行解引用。告警是对控制流逻辑的误判。 |
| 2272 | git-2.50.1 | coalesce_lines | Dereference of null pointer | 251 | FP | FP | 在告警行 `newend = newend->prev;` 之前，`newend` 仅在 `directions[i][j] == MATCH` 分支中被赋值，而该分支仅在 `newend` 非空时才会进入（因为循环条件 `while... |
| 2273 | git-2.50.1 | merge_ort_internal | Dereference of null pointer | 5277 | FP | FP | 告警行 `opt->priv->call_depth--;` 是对一个指针成员进行递减操作。切片代码显示，在调用此语句之前，`opt->priv->call_depth++` 已确保 `opt->priv` 被访问且未发生空指针解引用... |
| 2274 | git-2.50.1 | assert_sane_strbuf | Dereference of null pointer | 35 | FP | FP | 告警点位于宏 `cl_assert` 内部，该宏用于单元测试断言。`buf` 指针在调用前应已由测试框架或调用者确保非空，且此代码片段本身是用于验证 `strbuf` 内部状态的辅助函数，属于防御性编程逻辑，而非存在空指针解引用的实际风险。 |
| 2275 | git-2.50.1 | process_parents | Dereference of null pointer | 1174 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，且 `repo_parse_commit_gently` 调用失败时会 `continue`，这进一步保护了后续访问。切片代码中未发现 `... |
| 2276 | git-2.50.1 | run_prepare_commit_msg_hook | Dereference of null pointer | 1352 | FP | FP | 告警指向的代码行 `write_message(msg->buf, msg->len, name, 0)` 中，`msg` 是函数参数，由调用者传入，在切片中未见其为空的证据。函数 `write_message` 内部对文件操作有完整... |
| 2277 | git-2.50.1 | gather_stats | Dereference of null pointer | 52 | FP | FP | 切片代码显示函数入口处有明确的空指针检查 `if (!buf ｜｜ !size ｜｜ !stats) return;`，这确保了在访问 `buf` 前指针的有效性，因此告警的‘空指针解引用’逻辑错误不成立。 |
| 2278 | git-2.50.1 | clar_parse_args | Dereference of null pointer | 496 | FP | FP | 切片代码显示，在警告行 `explicit->suite_idx = j;` 之前，`explicit` 指针已通过 `calloc` 分配内存并检查了是否为 NULL，若为 NULL 则调用 `clar_abort` 终止程序，因此... |
| 2279 | git-2.50.1 | append_strategy | Dereference of null pointer | 233 | FP | FP | 切片代码显示，函数`append_strategy`仅将指针`s`存入数组`use_strategies`，并未对`s`进行解引用操作。告警所指的行是数组赋值，而非指针解引用，因此该告警为误报。 |
| 2280 | git-2.50.1 | merge_ref_iterator_advance | Dereference of null pointer | 214 | FP | FP | 在切片代码中，对 `iter->current` 的访问发生在 `if (!iter->current)` 条件判断之后，且 `selection & ITER_YIELD_CURRENT` 分支仅在 `iter->current` ... |
| 2281 | git-2.50.1 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码中，函数 `strvec_push_nodup` 直接对 `array->v` 进行赋值，未对 `array` 或 `array->v` 进行空指针检查。然而，该函数被命名为 `_nodup` 且接收一个 `struct st... |
| 2282 | git-2.50.1 | add_lines_to_move_detection | Dereference of null pointer | 1063 | FP | FP | 切片代码显示，`entry_list` 数组通过 `ALLOC_GROW_BY` 宏进行动态增长，该宏会确保分配内存并初始化为零。在访问 `entry_list[l->id]` 之前，`l->id` 的值被严格控制在 `id` 变量范... |
| 2283 | git-2.50.1 | image_remove_first_line | Dereference of null pointer | 355 | FP | FP | 切片代码显示函数 `image_remove_first_line` 调用了 `strbuf_remove`，该函数内部仅调用 `strbuf_splice` 进行内存操作。告警点 `img->line[0].len` 的访问发生在 ... |
| 2284 | git-2.50.1 | coalesce_lines | Dereference of null pointer | 259 | FP | FP | 在告警行 `if (lline->prev)` 之前，`lline` 被赋值为 `newend`，而 `newend` 在循环中通过 `newend = newend->prev` 或 `newend = lline->prev` 更... |
| 2286 | git-2.50.1 | strvec_splice | Dereference of null pointer | 69 | FP | FP | 在调用ALLOC_GROW宏之前，代码已检查`array->v == empty_strvec`，若为真则将其设为NULL，而ALLOC_GROW宏内部包含REALLOC_ARRAY，会处理NULL指针的重新分配，因此`array->... |
| 2287 | git-2.50.1 | <global> | Dereference of null pointer | 30 | FP | FP | 切片代码显示函数 `is_absolute_path` 为空实现，未包含任何指针解引用操作，因此工具报告的'空指针解引用'逻辑错误不成立。参考标签也为FP，进一步支持误报结论。 |
| 2288 | git-2.50.1 | prepare_attr_stack | Dereference of null pointer | 978 | FP | FP | 告警行 `*stack = info->prev;` 之前已调用 `bootstrap_attr_stack` 确保 `*stack` 非空，且 `info` 被赋值为 `*stack`，因此 `info` 非空，解引用 `info-... |
| 2289 | git-2.50.1 | split_graph_merge_strategy | Dereference of null pointer | 2284 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，变量 `g` 在 `while (g && ...)` 循环中被赋值，并且只有当 `ctx->num_commit_graphs_after == ... |
| 2290 | git-2.50.1 | get_nth_line | Dereference of null pointer | 879 | FP | FP | 函数逻辑清晰，当line为0时直接返回data，否则返回data + ends[line] + 1。切片中未显示ends数组可能为空的证据，且函数是静态的，调用上下文可能已确保参数有效性。结合参考标签为FP，倾向于判定为误报。 |
| 2291 | git-2.50.1 | <global> | Dereference of null pointer | 15 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对参数 `ref_iterator` 进行任何解引用操作，因此不存在空指针解引用问题。 |
| 2292 | git-2.50.1 | find_bisection | Dereference of null pointer | 440 | FP | FP | 告警指向的代码行 `list->item = best->item;` 位于 `if (best) {` 条件块内，`best` 指针已在前置条件中明确非空，因此解引用 `best->item` 是安全的。该告警为逻辑误报。 |
| 2293 | git-2.50.1 | try_to_commit | Dereference of null pointer | 1570 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，但切片代码显示，在进入该分支（`flags & AMEND_MSG`）前，`current_head` 已通过 `p... |
| 2294 | git-2.50.1 | <global> | Dereference of null pointer | 1546 | FP | FP | 告警点位于条件判断 `if (use_strategies[i]->attr & NO_FAST_FORWARD)`，但切片代码显示 `use_strategies` 数组在循环前已通过 `for (i = 0; i < use_st... |
| 2295 | git-2.50.1 | verify_absent_1 | Dereference of null pointer | 2496 | FP | FP | 告警点位于对 `ce_namelen(ce)` 的调用，这是一个宏，展开为 `((ce)->ce_namelen)`。切片代码显示，函数参数 `ce` 在调用前未被检查是否为 NULL，但调用者 `verify_absent_1` 的... |
| 2296 | git-2.50.1 | try_to_commit | Dereference of null pointer | 1686 | FP | FP | 告警指向的代码行 `commit_tree_extended(msg->buf, msg->len, ...)` 中，`msg` 指针在切片中已被检查并确保非空（例如，在 `if (!msg)` 分支中将其赋值为 `&commit_m... |
| 2298 | git-2.50.1 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数`ce_path_match`的参数`ce`被直接用于宏调用`ce_namelen(ce)`和访问`ce->name`、`ce->ce_mode`。调用该函数的上下文未在切片中提供，无法证明`ce`为NULL。在常见... |
| 2299 | git-2.50.1 | cmp_local_packs | Dereference of null pointer | 509 | FP | FP | 函数入口处 `pl` 被赋值为全局变量 `local_packs`，该变量在切片中初始化为 NULL。在未检查 `pl` 是否为 NULL 的情况下，代码直接访问 `pl->next`，存在空指针解引用风险。但考虑到 `label` ... |
| 2301 | git-2.50.1 | tree_write_stack_finish_subtree | Dereference of null pointer | 679 | FP | FP | 切片代码显示，在解引用指针 `n` 之前，已通过 `if (n)` 进行了明确的非空检查，确保了后续对 `n->buf` 等成员的访问是安全的。因此，该告警为误报。 |
| 2302 | git-2.50.1 | unload_one_branch | Dereference of null pointer | 2066 | FP | FP | 切片代码显示，在解引用指针 `e` 之前，`e` 被赋值为 `active_branches`，而 `active_branches` 仅在 `cur_active_branches` 为真且满足循环条件时才会进入循环体，这表明 `a... |
| 2303 | git-2.50.1 | apply_one_fragment | Dereference of null pointer | 2991 | FP | FP | 告警指向的代码行 `postimage.line[postimage.line_nr - 1].len--;` 在切片中受到前置条件 `inaccurate_eof && old > oldlines && old[-1] == '\... |
| 2304 | git-2.50.1 | process_entries | Dereference of null pointer | 4486 | FP | FP | 告警点位于一个错误处理分支，该分支仅在内部一致性检查失败时触发，并会调用BUG()宏终止程序。这属于防御性编程的断言逻辑，而非对用户可控的空指针进行解引用，因此是误报。 |
| 2305 | git-2.50.1 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过循环被填充，且 `remotes->nr == 1` 的条件确保了列表至少有一个... |
| 2306 | git-2.50.1 | clar_run_suite | Dereference of null pointer | 399 | FP | FP | 切片代码显示，在报告行`report->suite = _clar.active_suite;`之前，`report`指针已通过`calloc`分配内存，且分配失败时会调用`clar_abort`退出程序，因此`report`不可能为... |
| 2307 | git-2.50.1 | kwsprep | Dereference of null pointer | 507 | FP | FP | 告警指向的代码行 `curr = kwset->trie->next` 在切片上下文中，其外层循环 `for (curr = kwset->trie; curr; curr = curr->next)` 已确保 `kwset->tri... |
| 2309 | git-2.50.1 | get_ref_map | Dereference of null pointer | 544 | FP | FP | 切片代码显示，在警告所在行（`for (i = 0; i < fetch_refspec->nr; i++)`）之前，`fetch_refspec` 被明确赋值为 `&refmap` 或 `&remote->fetch`，两者均非空指... |
| 2310 | git-2.50.1 | setup_scoreboard | Dereference of null pointer | 2842 | FP | FP | 告警指向的代码行 `while (c->parents &&` 在切片中位于一个条件判断块 `if (sb->reverse && sb->revs->first_parent_only)` 内部。在进入该循环前，变量 `c` 被赋值... |
| 2311 | git-2.50.1 | clear_snapshot_buffer | Dereference of null pointer | 185 | FP | FP | 告警点位于die_errno函数调用内部，该函数用于处理错误并终止程序。在调用die_errno之前，代码已通过`if (munmap(...))`检查了munmap的返回值，仅当munmap失败（返回非零）时才会进入该分支。因此，对... |
| 2312 | git-2.50.1 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在解引用 `sb->buf` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 检查其是否指向特殊缓冲区。当条件为真时，`sb->buf` 非空，解引用安全；当条件为假时，执行 `ass... |
| 2314 | git-2.50.1 | prepare_attr_stack | Dereference of null pointer | 986 | FP | FP | 在while循环条件 `(*stack)->origin` 之前，代码已通过 `*stack = info->prev;` 更新了 `*stack` 指针，但 `info` 来自 `info = *stack;`，而 `*stack`... |
| 2315 | git-2.50.1 | show_pack_info | Dereference of null pointer | 1806 | FP | FP | 切片代码显示，在访问 `chain_histogram[i]` 之前，已通过条件 `if (deepest_delta)` 判断，若条件为真则调用 `CALLOC_ARRAY` 为其分配内存，该宏会调用 `xcalloc` 确保返回非... |
| 2316 | git-2.47.1 | image_remove_last_line | Dereference of null pointer | 362 | FP | FP | 代码中访问 `img->line[img->line_nr - 1]` 前，虽然未在切片中显式检查 `img->line` 是否为空或 `img->line_nr` 是否大于0，但函数 `image_remove_last_line`... |
| 2317 | git-2.47.1 | add_parents_only | Dereference of null pointer | 1934 | FP | FP | 在调用 `it->type` 之前，代码已检查 `if (!it && revs->ignore_missing) return 0;`，这确保了当 `it` 为 NULL 且 `revs->ignore_missing` 为真时函数... |
| 2318 | git-2.47.1 | get_mode | Dereference of null pointer | 63 | FP | FP | 切片代码显示，在解引用指针 `special` 之前，函数已通过 `if (special && ...)` 条件检查了其非空性。该检查确保了后续的 `*special = SPECIAL_PIPE;` 操作是安全的，因此告警为误报。 |
| 2319 | git-2.47.1 | sync_submodule | Dereference of null pointer | 1283 | FP | FP | 在调用 `submodule_from_path` 后，未检查返回值 `sub` 是否为 NULL 就立即解引用 `sub->name`，这确实存在空指针解引用的风险。然而，`submodule_to_gitdir` 函数的切片代码显... |
| 2320 | git-2.47.1 | crlf_to_git | Dereference of null pointer | 582 | FP | FP | 告警指向的代码行 `unsigned char c = *src++;` 位于 `do...while (--len);` 循环内，循环条件确保了 `len` 在递减前大于0，且 `src` 指针在函数入口处已通过 `if (src ... |
| 2321 | git-2.47.1 | cwexec | Dereference of null pointer | 673 | FP | FP | 切片代码显示，在访问 `trie->accepting` 等指针成员前，已通过 `if (!(trie = next[c]))` 等条件检查了 `trie` 指针的有效性，且 `next` 数组的访问 `next[c]` 在 `c` ... |
| 2322 | git-2.47.1 | diffcore_merge_broken | Dereference of null pointer | 295 | FP | FP | 在告警行 `if (pp->broken_pair &&` 之前，内层循环已确保 `pp = q->queue[j]` 赋值，且外层循环对 `q->queue[i]` 有明确的空指针检查（`if (!p) continue;`），这表... |
| 2323 | git-2.47.1 | parse_options_step | Dereference of null pointer | 906 | FP | FP | 告警点 `if (internal_help && *ctx->opt == 'h')` 中，`ctx->opt` 在进入该分支前已通过 `if (ctx->opt)` 检查非空，且告警所在循环的 `ctx->opt` 由 `arg ... |
| 2324 | git-2.47.1 | rstrip_ref_components | Dereference of null pointer | 2157 | FP | FP | 代码切片显示，在警告行 `p[i] == '/' ? i++ : *p++` 中，`p` 指向 `refname`，而 `refname` 是函数参数，不可能为 NULL。该行逻辑是遍历字符串，不存在对空指针的解引用。 |
| 2325 | git-2.47.1 | parse_options | Dereference of null pointer | 1052 | FP | FP | 在切片代码中，`ctx.opt` 在 `parse_options_step` 函数中被初始化为 NULL，并且在 `unknown` 标签处被重置为 NULL。在告警行 `isascii(*ctx.opt)` 之前，代码路径 `ca... |
| 2326 | git-2.47.1 | process_entry | Dereference of null pointer | 3413 | FP | FP | 告警指向的代码行位于 `RENAME_ONE_FILE_TO_TWO` 分支内，该分支仅在 `ci->ren2` 非空时才会执行。切片代码显示，在进入此分支前有 `if (ci->ren2)` 的断言，确保了 `ci->ren2` 的... |
| 2327 | git-2.47.1 | verify_absent | Dereference of null pointer | 2534 | FP | FP | 告警点位于条件判断 `if (!o->skip_sparse_checkout && (ce->ce_flags & CE_NEW_SKIP_WORKTREE))`，其中 `ce` 和 `o` 均为函数入参，在切片代码中未见其可能为空... |
| 2328 | git-2.47.1 | show_pack_info | Dereference of null pointer | 1689 | FP | FP | 切片代码显示，`chain_histogram` 仅在 `deepest_delta` 为真（非零）时通过 `CALLOC_ARRAY` 分配内存，而对其的访问 `chain_histogram[obj_stat[i].delta_d... |
| 2329 | git-2.47.1 | output | Dereference of null pointer | 550 | FP | FP | 切片代码显示，在访问 `a->items[b_util->matching].util` 之前，`b_util` 已通过 `j < b->nr` 条件确保非空，且 `b_util->matching` 在 `while (j < b-... |
| 2330 | git-2.47.1 | limit_list | Dereference of null pointer | 1497 | FP | FP | 切片代码中，在告警行 `if (obj->flags & UNINTERESTING)` 之前，`obj` 被赋值为 `&commit->object`，而 `commit` 来自 `pop_commit` 函数，该函数在栈非空时返回... |
| 2331 | git-2.47.1 | add_lines_to_move_detection | Dereference of null pointer | 1059 | FP | FP | 切片代码显示，`entry_list` 通过 `ALLOC_GROW_BY` 宏进行动态分配和初始化，该宏会确保内存分配成功并清零。在告警行使用 `entry_list[l->id]` 之前，`l->id` 的值被严格控制在 `id`... |
| 2332 | git-2.47.1 | limit_list | Dereference of null pointer | 1493 | FP | FP | 告警指向的代码行 `if (revs->max_age != -1 && (commit->date < revs->max_age))` 中，`commit` 变量来自 `pop_commit` 函数，该函数在输入列表非空时返回有效... |
| 2333 | git-2.47.1 | lstrip_ref_components | Dereference of null pointer | 2119 | FP | FP | 代码逻辑中，`p` 指针在循环条件 `p[i]` 中用于检查字符，其本身作为 `refname` 的副本，在函数入口处已通过 `xstrdup` 确保非空。循环体 `p[i] == '/' ? i++ : *p++` 对 `p` 的递... |
| 2334 | git-2.47.1 | strintmap_get | Dereference of null pointer | 189 | FP | FP | 代码逻辑正确，当 `strmap_get_entry` 返回 NULL 时，函数直接返回 `map->default_value`，并未对空指针进行解引用。告警是对控制流逻辑的误判。 |
| 2335 | git-2.47.1 | coalesce_lines | Dereference of null pointer | 264 | FP | FP | 在告警行 `newend = newend->prev;` 之前，`newend` 仅在 `directions[i][j] == MATCH` 分支内被赋值，而该分支仅在 `i` 和 `j` 均不为零时进入。循环条件 `while ... |
| 2336 | git-2.47.1 | merge_ort_internal | Dereference of null pointer | 5218 | FP | FP | 切片代码显示，在调用 `opt->priv->call_depth--` 之前，`opt->priv->call_depth++` 已确保 `opt->priv` 不为空。该操作发生在递归调用 `merge_ort_internal`... |
| 2337 | git-2.47.1 | process_parents | Dereference of null pointer | 1180 | FP | FP | 在调用 `p->parents` 之前，代码已通过 `if (p)` 检查了指针 `p` 非空，因此对 `p->parents` 的解引用是安全的。告警为逻辑误报。 |
| 2338 | git-2.47.1 | run_prepare_commit_msg_hook | Dereference of null pointer | 1365 | FP | FP | 告警指向的 `write_message` 函数调用中，`msg->buf` 的指针 `msg` 由函数参数传入，在切片代码中未见其被赋值为 NULL 或存在导致其为 NULL 的路径。函数逻辑是安全的，工具可能误判了指针的潜在空值状态。 |
| 2339 | git-2.47.1 | gather_stats | Dereference of null pointer | 51 | FP | FP | 切片代码显示函数参数 `buf` 在循环中被直接使用，但函数入口处没有对 `buf` 为 NULL 的检查。然而，该告警是逻辑错误而非空指针解引用，因为代码中 `buf[i]` 的访问发生在 `i < size` 的循环条件下，且 `... |
| 2340 | git-2.47.1 | append_strategy | Dereference of null pointer | 231 | FP | FP | 切片代码显示，函数`append_strategy`仅将传入的指针`s`存入数组，并未对`s`进行解引用操作。告警消息‘解引用空指针’与代码逻辑不符，属于静态分析工具的逻辑误判。 |
| 2341 | git-2.47.1 | merge_ref_iterator_advance | Dereference of null pointer | 203 | FP | FP | 切片代码显示，在解引用 `*iter->current` 之前，`iter->current` 仅在 `ITER_YIELD_CURRENT` 分支中被使用，而该分支仅在 `iter->select` 函数返回特定标志时进入。虽然切片... |
| 2342 | git-2.47.1 | strvec_push_nodup | Dereference of null pointer | 19 | FP | FP | 切片代码中，函数 `strvec_push_nodup` 的参数 `array` 和 `value` 的来源及有效性未知，无法直接确认 `array->v` 是否为有效指针或 `array->nr` 是否越界。但该告警为逻辑错误（De... |
| 2343 | git-2.47.1 | add_lines_to_move_detection | Dereference of null pointer | 1062 | FP | FP | 切片代码显示，`entry_list` 数组通过 `ALLOC_GROW_BY` 宏进行动态增长和初始化，确保在 `l->id` 作为索引访问前，数组已分配足够内存且元素被清零。访问 `entry_list[l->id]` 时，`l-... |
| 2344 | git-2.47.1 | image_remove_first_line | Dereference of null pointer | 354 | FP | FP | 告警点 `strbuf_remove(&img->buf, 0, img->line[0].len)` 中，`img` 指针的合法性在切片中未直接体现，但 `img->line[0].len` 的访问表明 `img` 及其内部结构 `... |
| 2345 | git-2.47.1 | coalesce_lines | Dereference of null pointer | 272 | FP | FP | 告警点位于条件判断 `if (lline->prev)` 中，该行代码是检查指针 `lline->prev` 是否为 NULL，而非解引用一个空指针。代码逻辑正确，工具报告的逻辑错误不成立。 |
| 2346 | git-2.47.1 | try_to_commit | Dereference of null pointer | 1699 | FP | FP | 切片代码中，告警行（commit_tree_extended调用）的参数均已在函数内部经过验证或由安全路径生成，未发现明显的空指针解引用风险。结合算法标签为FP，倾向于判定为误报。 |
| 2347 | git-2.47.1 | prepare_attr_stack | Dereference of null pointer | 1013 | FP | FP | 告警行 `*stack = info->prev;` 之前，`info` 被赋值为 `*stack`，而 `*stack` 由 `bootstrap_attr_stack` 函数初始化。该函数仅在 `*stack` 为 NULL 时才... |
| 2348 | git-2.47.1 | split_graph_merge_strategy | Dereference of null pointer | 2269 | FP | FP | 在调用 `get_commit_graph_filename(g->odb)` 之前，代码通过 `while (g && ...)` 循环和后续的 `while (g)` 循环确保了指针 `g` 在相关代码路径中被使用前不为 NULL... |
| 2349 | git-2.47.1 | get_nth_line | Dereference of null pointer | 874 | FP | FP | 函数逻辑清晰，通过条件判断 `if (line == 0)` 返回 `data`，否则返回 `data + ends[line] + 1`。切片中未显示 `ends` 或 `data` 为空的证据，且 `line` 作为参数，其值由调... |
| 2350 | git-2.47.1 | <global> | Dereference of null pointer | 13 | FP | FP | 切片代码显示函数 `ref_iterator_advance` 为空实现，没有对参数 `ref_iterator` 进行任何解引用操作，因此不存在空指针解引用问题。 |
| 2351 | git-2.47.1 | find_bisection | Dereference of null pointer | 439 | FP | FP | 告警指向的代码行 `list->item = best->item;` 位于 `if (best)` 条件块内，`best` 指针在解引用前已通过条件判断确保非空。切片代码逻辑清晰，不存在对空指针的解引用。 |
| 2352 | git-2.47.1 | <global> | Dereference of null pointer | 1537 | FP | FP | 告警点位于检查 `use_strategies[i]->attr & NO_FAST_FORWARD`，切片代码显示 `use_strategies` 数组在循环前已通过 `add_strategies` 等函数正确初始化，且循环条件... |
| 2353 | git-2.47.1 | verify_absent_1 | Dereference of null pointer | 2493 | FP | FP | 切片代码显示，在调用 `check_leading_path` 函数前，已通过条件 `if (o->index_only ｜｜ !o->update)` 进行了保护，当条件为真时函数直接返回0，不会执行到告警行。这表明告警点所在的代码... |
| 2354 | git-2.47.1 | try_to_commit | Dereference of null pointer | 1583 | FP | FP | 告警点位于 `parents = copy_commit_list(current_head->parents);`，其中 `current_head` 在 `if (flags & AMEND_MSG)` 分支内。该分支仅在 `pa... |
| 2355 | git-2.47.1 | ce_path_match | Dereference of null pointer | 41 | FP | FP | 切片代码显示，函数`ce_path_match`的参数`ce`被直接用于宏`ce_namelen`和访问其`name`成员。调用该函数的上下文未在切片中提供，但函数内部逻辑本身没有对`ce`进行空值检查。然而，考虑到`label`为F... |
| 2356 | git-2.47.1 | cmp_local_packs | Dereference of null pointer | 482 | FP | FP | 代码中 `local_packs` 被初始化为 NULL，但在函数 `cmp_local_packs` 被调用前，其值很可能已被正确初始化（切片未显示调用点）。告警点 `if (!pl->next)` 假设 `pl` 非空，结合 `l... |
| 2357 | git-2.47.1 | tree_write_stack_finish_subtree | Dereference of null pointer | 677 | FP | FP | 切片代码显示，在解引用指针 `n` 之前，已通过 `if (n)` 进行了明确的非空检查，确保了后续对 `n->buf` 等成员的访问是安全的。因此，该告警为误报。 |
| 2358 | git-2.47.1 | unload_one_branch | Dereference of null pointer | 2049 | FP | FP | 切片代码显示，在解引用 `e` 之前，`while` 循环的条件 `cur_active_branches && cur_active_branches >= max_active_branches` 确保了 `cur_active_... |
| 2359 | git-2.47.1 | apply_one_fragment | Dereference of null pointer | 2987 | FP | FP | 切片代码中，在警告行（postimage.line[postimage.line_nr - 1].len--）之前，存在条件判断 `if (inaccurate_eof && old > oldlines && old[-1] == ... |
| 2360 | git-2.47.1 | process_entries | Dereference of null pointer | 4452 | FP | FP | 切片代码显示，对 `dir_metadata.offsets.items[0].util` 的访问发生在条件检查 `dir_metadata.offsets.nr != 1` 之后，该条件确保数组至少有一个元素。此外，该代码位于一个错... |
| 2361 | git-2.47.1 | install_branch_config_multiple_remotes | Dereference of null pointer | 171 | FP | FP | 切片代码显示，在访问 `friendly_ref_names.items[0].string` 之前，`friendly_ref_names` 列表已通过循环被填充，且 `remotes->nr == 1` 的条件确保了列表至少有一个... |
| 2362 | git-2.47.1 | kwsprep | Dereference of null pointer | 502 | FP | FP | 告警指向的代码行 `curr = kwset->trie->next` 位于 `for` 循环条件中，其目的是遍历链表。切片代码显示，在进入此循环前，`kwset->trie` 已在第 502 行的 `for (curr = last... |
| 2363 | git-2.47.1 | get_ref_map | Dereference of null pointer | 546 | FP | FP | 切片代码显示，在访问 `remote->fetch` 之前，函数开头有 `if (remote)` 的条件检查，并且 `fetch_refspec` 的赋值逻辑也确保了其非空。告警点所在的循环 `for (i = 0; i < fet... |
| 2364 | git-2.47.1 | setup_scoreboard | Dereference of null pointer | 2841 | FP | FP | 切片代码显示，在访问 `c->parents` 的循环条件 `while (c->parents && ...)` 中，已经对 `c->parents` 进行了空指针检查，因此不会发生空指针解引用。该告警是静态分析工具的逻辑误判。 |
| 2365 | git-2.47.1 | strbuf_setlen | Dereference of null pointer | 170 | FP | FP | 切片代码显示，在访问 `sb->buf[len]` 之前，已通过条件 `if (sb->buf != strbuf_slopbuf)` 确保 `sb->buf` 不是指向静态缓冲区 `strbuf_slopbuf` 的空指针或无效指针... |
| 2366 | git-2.47.1 | prepare_attr_stack | Dereference of null pointer | 1021 | FP | FP | 告警行 `while ((*stack)->origin)` 在进入循环前，`*stack` 已通过 `*stack = info->prev;` 从 `info` 指针赋值，而 `info` 来自 `info = *stack;`，... |
| 2368 | git-2.47.1 | show_pack_info | Dereference of null pointer | 1711 | FP | FP | 代码逻辑显示，指针 `chain_histogram` 仅在条件 `deepest_delta` 为真时通过 `CALLOC_ARRAY` 分配内存，否则保持为 NULL。后续的循环 `for (i = 0; i < deepest_... |
| 2369 | musl-1.2.1 | iconv | Dereference of null pointer | 373 | FP | FP | 代码在访问 `scd->state` 前已通过 `if (!((size_t)cd & 1))` 检查，确保 `scd` 非空时才使用；对于 `cd` 为奇数（非状态转换描述符）的情况，`scd` 保持为0，但后续逻辑（如 `ISO2... |
| 2370 | musl-1.2.1 | load_direct_deps | Dereference of null pointer | 1194 | FP | FP | 在切片代码中，`p->deps` 被赋值后立即进行了空指针检查 `if (!p->deps)`，若为空则会调用 `error` 并 `longjmp` 跳出函数，因此后续访问 `p->deps[cnt++]` 时指针不可能为空。该告警... |
| 2371 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警行 `so = pmatch[bt].rm_so;` 中，`pmatch` 指针在 `tnfa->num_submatches` 非零时已通过 `xmalloc` 分配，且 `bt` 是来自状态机的有效索引，切片中未见明显的越界或... |
| 2372 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 告警点位于条件判断 `if (next_tags)` 之后，该条件确保了 `next_tags` 非空才进行解引用。切片代码中 `next_tags` 的赋值逻辑（如 `next_tags = trans_i->tags`）表明它可能... |
| 2373 | musl-1.2.1 | do_relocs | Dereference of null pointer | 435 | FP | FP | 告警指向的代码行位于 `case REL_COPY:` 分支，该分支仅在 `def.sym` 和 `sym_val` 有效时执行 `memcpy`。切片代码显示，`sym_val` 的计算为 `def.sym ? (size_t)la... |
| 2374 | musl-1.2.1 | iconv | Dereference of null pointer | 380 | FP | FP | 告警指向的代码行位于 `switch (scd->state)` 语句中，但切片代码显示，在进入该switch语句之前，`scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时才被赋值，否则保持为0。然而，在... |
| 2375 | musl-1.2.1 | iconv | Dereference of null pointer | 372 | FP | FP | 代码在访问 `scd->state` 前已通过 `if (!((size_t)cd & 1))` 检查，确保 `scd` 仅在 `cd` 为偶数（即指向有效 `stateful_cd` 结构）时才被赋值，否则 `scd` 保持为 0。... |
| 2376 | musl-1.2.1 | load_direct_deps | Dereference of null pointer | 1206 | FP | FP | 切片代码显示，在访问 `p->deps[cnt]` 之前，已通过 `if (p->deps) return;` 进行了空指针检查，因此该指针不可能为空，告警为误报。 |
| 2377 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `tags[*next_tags++] = pos;` 位于 `if (next_tags)` 条件保护块内，切片代码显示 `next_tags` 在进入该块前已被检查为非空，且循环条件 `*next_tags >=... |
| 2378 | musl-1.2.1 | iconv | Dereference of null pointer | 374 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 确保 `scd` 不为空指针，且 `scd` 仅在 `cd` 为偶数时被赋值，逻辑上避免了空指针解引用。 |
| 2379 | musl-1.2.1 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `if (match_eo >= 0 && !(cflags & REG_NOSUB))` 条件确保仅在有效匹配时进入循环。循环内对 `submatch_data[i].so_tag... |
| 2380 | musl-1.2.1 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，变量 `max` 已被赋值为 -1（当 `(flags & COPY_REMOVE_TAGS)` 为真时），这可能导致数组索引越界或使用负索引。然而，告警点位于 ... |
| 2381 | musl-1.2.1 | iconv | Dereference of null pointer | 375 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查并赋值 `scd = (void *)cd`，确保 `scd` 非空。在 `ISO2022_JP` 分支中，`scd->stat... |
| 2382 | musl-1.2.1 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点位于条件判断 `if (!scd->state)` 中，但代码逻辑表明 `scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。当 `scd` 为0时，程序不会进入 `case U... |
| 2383 | musl-1.2.1 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags` 数组前，`submatch_data[i].eo_tag` 的值已用于索引 `tags` 数组的 `so_tag` 字段且未发生空指针解引用，表明 `tags` 指针在该上下文中有效。此外，告警行位... |
| 2384 | musl-1.2.1 | queue_ctors | Dereference of null pointer | 1452 | FP | FP | 在告警行访问 `p->deps[p->next_dep]` 之前，代码逻辑通过 `while (p->next_dep < p->ndeps_direct)` 确保了索引 `p->next_dep` 在数组 `p->deps` 的有效... |
| 2385 | musl-1.2.1 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 在切片代码中，对 `states_seen` 数组的访问 `states_seen[stack->item.state_id] = 0;` 位于 `if (stack->prev)` 条件块内，这确保了 `stack` 不为空且 `s... |
| 2386 | musl-1.2.1 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于switch-case语句中，该行是有效的状态赋值操作（`scd->state=3;`），并非空指针解引用。切片代码显示`scd`指针在函数入口处已通过条件判断（`if (!((size_t)cd & 1))`）被... |
| 2387 | musl-1.2.1 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警指向的代码行 `regset = xmalloc(...)` 在切片中可见其返回值被立即检查是否为 NULL，并在为 NULL 时返回错误码 `REG_ESPACE`，避免了空指针解引用。代码逻辑是安全的。 |
| 2388 | musl-1.2.4 | iconv | Dereference of null pointer | 373 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 确保 `scd` 不为空指针，且 `scd` 仅在 `cd` 为偶数时被赋值，逻辑上避免了空指针解引用。 |
| 2389 | musl-1.2.4 | load_direct_deps | Dereference of null pointer | 1280 | FP | FP | 在切片代码中，`p->deps` 的赋值逻辑包含条件判断 `(p==head && cnt<2) ? builtin_deps :`，但后续的 `if (!p->deps)` 检查确保了在进入使用 `p->deps` 的循环前，指针已... |
| 2390 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 切片代码显示，在访问 `pmatch[bt].rm_so` 之前，`pmatch` 已通过 `xmalloc` 分配了内存，且 `bt` 作为 `trans_i->u.backref` 是内部状态索引，其值受限于 `tnfa->num... |
| 2391 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `if (next_tags)` 检查了 `next_tags` 指针，且 `next_tags` 来源于 `trans_i->tags`，该数组在循环中被遍历，其元素值 `*nex... |
| 2392 | musl-1.2.4 | do_relocs | Dereference of null pointer | 484 | FP | FP | 告警指向的代码行位于switch-case的REL_COPY分支，该分支仅在`sym`和`sym_val`有效时执行`memcpy`。切片代码显示，在进入此分支前，`sym_val`的计算已检查`def.sym`是否非空，且`sym`... |
| 2393 | musl-1.2.4 | iconv | Dereference of null pointer | 380 | FP | FP | 告警指向的代码行位于switch语句内部，该语句在多个case分支中均对scd->state进行了赋值，且在进入该switch前已通过条件判断确保scd不为空指针。切片代码中未发现对空指针的明确解引用路径。 |
| 2394 | musl-1.2.4 | iconv | Dereference of null pointer | 372 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查并赋值，当 `cd` 为奇数时 `scd` 保持为 0，但后续对 `scd->state` 的访问（如 `case UCS2:`... |
| 2395 | musl-1.2.4 | do_relocs | Dereference of null pointer | 519 | FP | FP | 告警指向的代码行 `if (def.dso->tls_id > static_tls_cnt)` 在切片中已明确显示 `def.dso` 在之前的逻辑分支中已被赋值为 `dso`（当 `sym_index` 为0时），因此 `def.... |
| 2396 | musl-1.2.4 | do_relocs | Dereference of null pointer | 458 | FP | FP | 告警指向的代码行位于一个条件判断块内，该条件为 `def.dso->tls_id > static_tls_cnt`，仅当条件为真时才执行后续的 `error` 和 `longjmp` 函数。`longjmp` 函数本身不会解引用空指... |
| 2397 | musl-1.2.4 | load_direct_deps | Dereference of null pointer | 1292 | FP | FP | 切片代码显示，函数入口处有 `if (p->deps) return;` 检查，当 `p->deps` 为空时函数会提前返回，因此后续对 `p->deps[cnt]` 的访问是受保护的，不会发生空指针解引用。 |
| 2398 | musl-1.2.4 | do_relocs | Dereference of null pointer | 500 | FP | FP | 切片代码显示，在`case REL_DTPMOD:`分支中，`def.dso`被赋值为`dso`（见`sym_index`为0时的`else`分支），因此`def.dso`不可能为空，`def.dso->tls_id`的访问是安全的。 |
| 2399 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `tags[*next_tags++] = pos;` 位于 `if (next_tags)` 条件保护块内，且 `next_tags` 指针在循环 `while (*next_tags >= 0)` 中受 `*ne... |
| 2400 | musl-1.2.4 | iconv | Dereference of null pointer | 374 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，已通过条件 `if (!((size_t)cd & 1))` 检查了 `cd` 的有效性，并仅在 `cd` 为偶数（即非状态转换描述符）时才将 `scd` 指向 `cd`。对于状态... |
| 2401 | musl-1.2.4 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码中，`tags` 数组的访问受 `i < tnfa->num_submatches && i < nmatch` 循环条件保护，且 `so_tag` 和 `eo_tag` 来自 `tnfa->submatch_data` 结构... |
| 2402 | musl-1.2.4 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 数组前，变量 `max` 已被赋值为 -1（当 `(flags & COPY_REMOVE_TAGS)` 为真时）。虽然存在另一条路径 `(flags & COPY_M... |
| 2403 | musl-1.2.4 | iconv | Dereference of null pointer | 375 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查并赋值，当 `cd` 为奇数时 `scd` 保持为 0，但后续仅在 `type` 为 `UCS2`、`UTF_16` 或 `UT... |
| 2404 | musl-1.2.4 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点位于 `if (!scd->state)` 条件判断处，但代码逻辑表明 `scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值，否则保持为0。当 `scd` 为0时，访问 `scd->state... |
| 2405 | musl-1.2.4 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 进行条件判断，仅在 `eo_tag` 不等于 `end_tag` 时才进行解引用。`t... |
| 2406 | musl-1.2.4 | queue_ctors | Dereference of null pointer | 1553 | FP | FP | 在告警行 `p->deps[p->next_dep]->mark` 之前，循环条件 `while (p->next_dep < p->ndeps_direct)` 确保了 `p->next_dep` 是 `p->deps` 数组的有效... |
| 2407 | musl-1.2.4 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 告警行位于`if (stack->prev)`条件块内，该条件确保了`stack`不为空，且`stack->prev`存在，因此`stack->item.state_id`的访问是安全的。切片代码中未发现空指针解引用路径。 |
| 2408 | musl-1.2.4 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于switch-case语句的一个分支内，该分支仅在特定字符编码（ISO2022_JP）且输入为特定转义序列时才会执行。在切片代码中，变量`scd`在函数入口处被有条件地赋值，但在该分支执行前，其状态（`scd->s... |
| 2409 | musl-1.2.4 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 切片代码显示告警行 `regset = xmalloc(...)` 前已对 `tnfa` 进行了空指针检查（`first_pass = (mem == NULL ｜｜ tnfa == NULL)`），且后续对 `tnfa->num_s... |
| 2410 | musl-1.1.24 | iconv | Dereference of null pointer | 373 | FP | FP | 代码中 `scd` 指针在函数入口处通过条件 `if (!((size_t)cd & 1))` 进行初始化，当条件不满足时 `scd` 保持为 0（NULL）。但在后续使用 `scd->state` 的路径（如 `case UCS2:... |
| 2411 | musl-1.1.24 | load_direct_deps | Dereference of null pointer | 1189 | FP | FP | 在 `p->deps` 被使用前，代码通过 `if (!p->deps)` 检查了其是否为空，并在为空时通过 `error` 和 `longjmp` 提前退出函数，因此警告行 `p->deps[cnt++] = q;` 不会发生对空指... |
| 2412 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 切片代码显示，在访问 `pmatch[bt].rm_so` 之前，`pmatch` 指针已通过 `xmalloc` 分配了内存，且 `bt` 作为数组索引在 `tre_fill_pmatch` 函数中被合理使用，没有证据表明 `pma... |
| 2413 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 告警点位于条件判断 `if (next_tags)` 之后，该条件确保了 `next_tags` 不为空指针。在切片代码中，`next_tags` 被赋值为 `trans_i->tags`，而 `trans_i` 是来自 `tnfa-... |
| 2414 | musl-1.1.24 | do_relocs | Dereference of null pointer | 430 | FP | FP | 切片代码显示，在调用 `memcpy` 的 `REL_COPY` 分支中，`sym_val` 和 `sym->st_size` 的使用受到前置条件保护。`sym_val` 由 `def.sym` 决定，而 `def.sym` 在符号未... |
| 2415 | musl-1.1.24 | iconv | Dereference of null pointer | 380 | FP | FP | 告警点位于switch语句中对`scd->state`的访问，但切片代码显示，在进入该switch语句前，`scd`指针仅在`cd`参数为偶数时被赋值，且`scd->state`仅在特定编码路径（如UCS2、UTF_16、UTF_32... |
| 2416 | musl-1.1.24 | iconv | Dereference of null pointer | 372 | FP | FP | 告警点位于 `scd->state=0;` 赋值语句，但切片代码显示 `scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时才被赋值，否则保持为0。在 `ISO2022_JP` 分支中，`scd` 可能为 ... |
| 2417 | musl-1.1.24 | load_direct_deps | Dereference of null pointer | 1201 | FP | FP | 切片代码显示，在访问 `p->deps[cnt]` 之前，存在条件判断 `if (p->deps) return;`，这确保了当 `p->deps` 为空指针时函数会提前返回，不会执行后续的解引用操作，因此该告警为误报。 |
| 2418 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `tags[*next_tags++] = pos;` 位于 `if (next_tags)` 条件保护块内，且 `next_tags` 在循环条件 `while (*next_tags >= 0)` 中已确保指针非... |
| 2419 | musl-1.1.24 | iconv | Dereference of null pointer | 374 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查并赋值，当 `cd` 为奇数时 `scd` 保持为 0，但后续仅在 `type` 为 `UCS2`、`UTF_16` 或 `UT... |
| 2420 | musl-1.1.24 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags` 数组前，函数已通过 `if (match_eo >= 0 && !(cflags & REG_NOSUB))` 进行了条件保护，且 `submatch_data[i].so_tag` 和 `subm... |
| 2421 | musl-1.1.24 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，变量 `max` 已在 `else if` 分支中被赋值为 `-1`，但该分支的条件 `(flags & COPY_MAXIMIZE_FIRST_TAG) && ... |
| 2422 | musl-1.1.24 | iconv | Dereference of null pointer | 375 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查并赋值，当 `cd` 为奇数时 `scd` 保持为 0，但后续对 `scd->state` 的访问（如 `case ISO202... |
| 2423 | musl-1.1.24 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点位于 `if (!scd->state)` 条件判断处，但代码切片显示 `scd` 指针仅在 `if (!((size_t)cd & 1))` 分支中被赋值，当 `cd` 为奇数时 `scd` 保持为 0。然而，在 `case ... |
| 2424 | musl-1.1.24 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 进行条件判断，仅在 `eo_tag` 不等于 `end_tag` 时才进行数组索引访问... |
| 2425 | musl-1.1.24 | queue_ctors | Dereference of null pointer | 1447 | FP | FP | 在告警行访问 `p->deps[p->next_dep]` 之前，代码逻辑通过 `while (p->next_dep < p->ndeps_direct)` 确保了数组索引 `p->next_dep` 在有效范围内，且切片中未见 `... |
| 2426 | musl-1.1.24 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 切片代码显示，在访问 `states_seen[stack->item.state_id]` 之前，存在 `if (stack->prev)` 的条件检查，确保了 `stack` 不为空，且 `stack->item.state_id... |
| 2427 | musl-1.1.24 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于switch-case语句中，是对状态变量`scd->state`的赋值操作。切片代码显示`scd`指针仅在`if (!((size_t)cd & 1))`条件为真时才被赋值，否则保持为0。在`scd`为0（空指针... |
| 2428 | musl-1.1.24 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 切片代码显示，在告警行（xmalloc调用）之前，函数参数`tnfa`已在条件`first_pass = (mem == NULL ｜｜ tnfa == NULL)`中被检查，且后续逻辑中`tnfa`被直接解引用（如`tnfa->nu... |
| 2429 | musl-1.2.3 | iconv | Dereference of null pointer | 373 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查并赋值，当 `cd` 为奇数时 `scd` 保持为 0，但后续 `ISO2022_JP` 分支仅在 `scd` 非空时才会进入 ... |
| 2430 | musl-1.2.3 | load_direct_deps | Dereference of null pointer | 1218 | FP | FP | 在切片代码中，`p->deps` 被赋值后，紧接着有一个 `if (!p->deps)` 的检查，如果为 null 会调用 `error` 并 `longjmp` 跳出函数，因此后续 `p->deps[cnt++] = q;` 处的解... |
| 2431 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 告警行 `so = pmatch[bt].rm_so;` 中，`pmatch` 指针在 `tnfa->num_submatches` 非零时已通过 `xmalloc` 分配内存，且 `bt` 是 `trans_i->u.backref... |
| 2432 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 告警点位于条件判断 `if (next_tags)` 之后，该条件确保了 `next_tags` 非空才进入循环。在切片代码中，`next_tags` 被赋值为 `trans_i->tags`，而 `trans_i` 来自 `tnfa... |
| 2433 | musl-1.2.3 | do_relocs | Dereference of null pointer | 440 | FP | FP | 切片代码显示，在调用memcpy的REL_COPY分支中，sym_val和sym->st_size的使用都受到前序条件保护。sym_val由def.sym决定，而def.sym在sym_index非零时通过find_sym查找，失败时... |
| 2434 | musl-1.2.3 | iconv | Dereference of null pointer | 380 | FP | FP | 告警点位于switch(scd->state)语句，但scd指针仅在条件(!((size_t)cd & 1))成立时才被赋值，否则保持为0。然而，在进入该switch语句的代码路径（ISO2022_JP case）中，scd->sta... |
| 2435 | musl-1.2.3 | iconv | Dereference of null pointer | 372 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 确保 `scd` 非空，且 `scd` 仅在 `cd` 为偶数时被赋值，此时 `scd` 指向有效的 `stateful_cd` 结... |
| 2436 | musl-1.2.3 | load_direct_deps | Dereference of null pointer | 1230 | FP | FP | 切片代码显示，在访问 `p->deps[cnt]` 之前，已通过 `if (p->deps) return;` 进行了空指针检查，因此该指针不可能为空，告警为误报。 |
| 2437 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 代码中 `next_tags` 指针在解引用前已通过 `if (next_tags)` 检查，且循环条件 `*next_tags >= 0` 隐含了对指针有效性的验证，因此不存在空指针解引用风险。 |
| 2438 | musl-1.2.3 | iconv | Dereference of null pointer | 374 | FP | FP | 切片代码显示，在访问 `scd->state` 之前，已通过条件 `if (!((size_t)cd & 1))` 检查了 `cd` 的有效性，并仅在条件为真时将 `scd` 指向非空对象。在 `case ISO2022_JP` 中，... |
| 2439 | musl-1.2.3 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `if (match_eo >= 0 && !(cflags & REG_NOSUB))` 条件确保仅在有效匹配时进入循环，且循环条件 `i < tnfa->num_submatch... |
| 2440 | musl-1.2.3 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，变量 `max` 已在 `else if` 分支中被赋值为 `-1`，这确保了数组索引 `max` 为 -1 时不会发生越界访问。结合告警标签为 FP，判定为误报。 |
| 2441 | musl-1.2.3 | iconv | Dereference of null pointer | 375 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查，确保 `scd` 非空时才使用；在 `ISO2022_JP` 分支中，访问 `scd->state` 仅发生在 `c == '... |
| 2442 | musl-1.2.3 | iconv | Dereference of null pointer | 300 | FP | FP | 告警点 `if (!scd->state)` 位于 `scd` 指针被初始化为 `0` 之后，但在该代码路径（`type` 为 `UCS2` 或 `UTF_16`）之前，存在条件 `if (!((size_t)cd & 1))` 将 ... |
| 2443 | musl-1.2.3 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码中，在访问 `tags` 数组前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 条件进行保护，确保仅在 `eo_tag` 不等于 `end_tag` 时才进行数组索引访... |
| 2444 | musl-1.2.3 | queue_ctors | Dereference of null pointer | 1487 | FP | FP | 在告警行 `p->deps[p->next_dep]->mark` 之前，`p` 来自 `stack[spos++]`，而 `stack` 指向 `queue`，`queue` 中的元素是 `dso` 或其依赖项，这些对象在进入队列前... |
| 2445 | musl-1.2.3 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 在警告行 `states_seen[stack->item.state_id] = 0;` 之前，代码已通过 `if (stack->prev)` 检查确保 `stack` 不为空，且 `stack->item.state_id` 作... |
| 2446 | musl-1.2.3 | iconv | Dereference of null pointer | 376 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查并赋值，当 `cd` 为奇数时 `scd` 保持为 0，但后续对 `scd->state` 的访问仅在 `type` 为特定值（... |
| 2447 | musl-1.2.3 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警行代码 `regset = xmalloc(...)` 中，`tnfa` 指针在函数开头通过 `first_pass = (mem == NULL ｜｜ tnfa == NULL)` 进行了非空检查，且后续代码中 `tnfa->n... |
| 2448 | musl-1.2.2 | iconv | Dereference of null pointer | 373 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查，确保 `scd` 仅在 `cd` 为有效状态转换描述符时才为非空指针。在 `ISO2022_JP` 分支中，`scd->sta... |
| 2449 | musl-1.2.2 | load_direct_deps | Dereference of null pointer | 1217 | FP | FP | 在切片代码中，`p->deps` 的赋值逻辑包含条件判断 `(p==head && cnt<2) ? builtin_deps :`，但切片不完整，缺少完整的赋值表达式。然而，在警告行之前有 `if (!p->deps) { erro... |
| 2450 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 781 | FP | FP | 切片代码显示，在访问 `pmatch[bt].rm_so` 之前，`pmatch` 指针已通过 `xmalloc` 分配内存，且 `bt` 作为 `trans_i->u.backref` 是有效的数组索引。此外，`tre_fill_p... |
| 2451 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 733 | FP | FP | 告警点位于条件判断 `if (next_tags)` 之后，该条件确保了 `next_tags` 非空才进入循环进行解引用。切片代码中 `next_tags` 的赋值逻辑表明，在解引用前它要么被赋值为 `trans_i->tags`（... |
| 2452 | musl-1.2.2 | do_relocs | Dereference of null pointer | 440 | FP | FP | 告警指向的代码行位于 `case REL_COPY:` 分支内，该分支仅在 `sym` 和 `sym_val` 有效时执行。切片代码显示，`sym_val` 的计算依赖于 `def.sym`，而 `def.sym` 在符号未找到时会被... |
| 2453 | musl-1.2.2 | iconv | Dereference of null pointer | 380 | FP | FP | 告警指向的代码行位于 `switch (scd->state)` 语句中，而 `scd` 指针仅在 `if (!((size_t)cd & 1))` 条件为真时被赋值。当 `cd` 的最低有效位为1时（表示组合转换描述符），`scd`... |
| 2454 | musl-1.2.2 | iconv | Dereference of null pointer | 372 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 确保 `scd` 非空，且 `scd` 仅在 `cd` 为偶数时被赋值。在 `ISO2022_JP` 分支中，`scd->state... |
| 2455 | musl-1.2.2 | load_direct_deps | Dereference of null pointer | 1229 | FP | FP | 切片代码显示，在访问 `p->deps[cnt]` 之前，已通过 `if (p->deps) return;` 进行了空指针检查，因此该指针不可能为空，告警为误报。 |
| 2456 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 869 | FP | FP | 告警指向的代码行 `tags[*next_tags++] = pos;` 位于 `if (next_tags)` 条件保护之后，且 `while (*next_tags >= 0)` 循环确保了 `*next_tags` 是有效索引。... |
| 2457 | musl-1.2.2 | iconv | Dereference of null pointer | 374 | FP | FP | 告警指向的代码行 `case 'I': scd->state=4; continue;` 是对 `scd->state` 的赋值，而 `scd` 指针在函数入口处已通过条件 `if (!((size_t)cd & 1)) { scd ... |
| 2458 | musl-1.2.2 | tre_fill_pmatch | Dereference of null pointer | 947 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `while (i < tnfa->num_submatches && i < nmatch)` 循环条件确保索引 `i` 在有效范围内，且 `submatch_data[i].so... |
| 2459 | musl-1.2.2 | tre_copy_ast | Dereference of null pointer | 1741 | FP | FP | 切片代码显示，在访问 `tag_directions[max]` 之前，变量 `max` 已在 `else if` 分支中被赋值为 -1，但该分支的条件 `(flags & COPY_MAXIMIZE_FIRST_TAG) && fi... |
| 2460 | musl-1.2.2 | iconv | Dereference of null pointer | 375 | FP | FP | 告警指向的代码行位于switch-case语句的一个分支中，该分支仅在特定条件下执行。在切片代码中，变量`scd`在函数入口处被有条件地赋值，且在该分支执行前，`scd`的使用（如`scd->state`）已通过前置条件`if (!s... |
| 2461 | musl-1.2.2 | iconv | Dereference of null pointer | 300 | FP | FP | 代码在访问 `scd->state` 前已通过条件 `if (!((size_t)cd & 1))` 检查并初始化了 `scd` 指针，确保其非空。对于 `cd` 为奇数（无状态）的情况，`scd` 保持为 0，但 `type` 为 ... |
| 2462 | musl-1.2.2 | tre_fill_pmatch | Dereference of null pointer | 952 | FP | FP | 切片代码显示，在访问 `tags` 数组前，已通过 `if (submatch_data[i].eo_tag == tnfa->end_tag)` 条件进行保护，仅在 `eo_tag` 不等于 `end_tag` 时才进行数组索引。`... |
| 2463 | musl-1.2.2 | queue_ctors | Dereference of null pointer | 1486 | FP | FP | 在告警行 `p->deps[p->next_dep]->mark` 处，`p->deps` 数组的访问受 `p->next_dep < p->ndeps_direct` 循环条件保护，确保了索引在有效范围内。切片代码中未见 `p->d... |
| 2464 | musl-1.2.2 | tre_tnfa_run_backtrack | Dereference of null pointer | 879 | FP | FP | 在警告行`states_seen[stack->item.state_id] = 0;`之前，代码已通过`if (stack->prev)`检查确保`stack`不为空，且宏`BT_STACK_POP`中的`assert(stack-... |
| 2465 | musl-1.2.2 | iconv | Dereference of null pointer | 376 | FP | FP | 告警指向的代码行位于一个switch-case语句块内，该语句块处理的是转义序列，`scd`指针在函数入口处已通过条件`if (!((size_t)cd & 1))`进行初始化，且在该case执行前，`scd`已被用于读取`scd->... |
| 2466 | musl-1.2.2 | tre_add_tags | Dereference of null pointer | 1229 | FP | FP | 告警指向的代码行在分配内存后立即进行了NULL检查，并在检查失败时返回错误，因此不存在对空指针的解引用。该告警是静态分析工具的逻辑误判。 |
| 2467 | tmux-3.3 | recalculate_sizes_now | Dereference of null pointer | 458 | FP | FP | 在访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已对 `c->session` 进行了空指针检查，若为空则直接返回，确保了后续 `s` 指针的有效性。切片代码中可见明确的防护逻辑，因... |
| 2468 | tmux-3.3 | mode_tree_draw | Dereference of null pointer | 750 | FP | FP | 切片代码中，在调用 `xasprintf(&text, ...)` 之前，已通过 `if (mtd->sort_list != NULL)` 检查了 `mtd->sort_list` 指针，确保其非空后才进行解引用 `mtd->sor... |
| 2469 | tmux-3.3 | window_copy_search | Dereference of null pointer | 3674 | FP | FP | 在告警行访问 `data->searchmark[at]` 之前，存在条件检查 `data->searchmark != NULL`（第 3648 行），这确保了指针非空。切片代码显示该访问受前置空指针检查保护，因此是安全的误报。 |
| 2470 | tmux-3.3 | grid_string_cells | Dereference of null pointer | 1013 | FP | FP | 切片代码显示，在调用 `grid_string_cells_code(*lastgc, ...)` 之前，存在条件判断 `if (lastgc != NULL && *lastgc == NULL)`，该条件会初始化 `*lastgc... |
| 2471 | tmux-3.3 | mode_tree_draw | Dereference of null pointer | 754 | FP | FP | 告警点位于 `xasprintf(&text, " %s", mti->name);`，其中 `mti` 指针在切片代码中已通过 `mti = line->item;` 和 `if (mti->draw_as_parent) mti ... |
| 2472 | tmux-3.3 | grid_reflow_join | Dereference of null pointer | 1212 | FP | FP | 在切片代码中，变量 `from` 在 `for` 循环中被赋值（`from = &gd->linedata[line];`），并且在 `left = from->cellused - want;` 这一行之前，存在 `if (line... |
| 2473 | tmux-3.3 | spawn_window | Dereference of null pointer | 180 | FP | FP | 告警点 `free(w->name);` 位于条件 `if (~sc->flags & SPAWN_RESPAWN)` 分支内，而在此分支之前，存在 `w = NULL;` 的赋值。但切片代码显示，当进入该分支时，`w` 已被重新赋值... |
| 2474 | tmux-3.3 | server_client_reset_state | Dereference of null pointer | 2340 | FP | FP | 告警行访问的指针 `s` 在切片代码中已被赋值，要么来自 `c->overlay_mode` 的返回值（若不为NULL），要么直接赋值为 `wp->screen`。`wp` 由 `server_client_get_pane` 返回，... |
| 2475 | tmux-3.3 | input_parse | Dereference of null pointer | 907 | FP | FP | 代码在访问 `itr->first` 和 `itr->last` 之前，已通过 `while (itr->first != -1 && itr->last != -1)` 循环确保 `itr` 指向有效结构体，且若未找到有效转换会调用... |
| 2476 | tmux-3.2 | recalculate_sizes_now | Dereference of null pointer | 367 | FP | FP | 在访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已对 `c->session` 进行了空指针检查，并确保 `c->session` 不为空。同时，`TAILQ_FOREACH` 宏确... |
| 2477 | tmux-3.2 | mode_tree_draw | Dereference of null pointer | 753 | FP | FP | 告警指向的代码行 `xasprintf(&text, " %s (sort: %s%s)", mti->name, ...);` 中，`mti` 指针在切片代码中已通过 `mti = line->item;` 赋值，且 `line` ... |
| 2478 | tmux-3.2 | window_copy_search | Dereference of null pointer | 3183 | FP | FP | 在访问 `data->searchmark[at]` 之前，代码通过 `window_copy_search_mark_at(data, fx, fy, &at) == 0` 检查了索引 `at` 的有效性，并且 `at > 0` 确... |
| 2479 | tmux-3.2 | spawn_window | Dereference of null pointer | 181 | FP | FP | 告警指向的代码行 `w->name = format_single(...)` 中，变量 `w` 在切片中已通过 `w = sc->wl->window` 或 `w = sc->wl->window` 等方式被赋值，且 `sc->wl... |
| 2480 | tmux-3.2 | grid_string_cells | Dereference of null pointer | 983 | FP | FP | 切片代码显示，在调用 `grid_string_cells_code(*lastgc, ...)` 之前，存在条件判断 `if (lastgc != NULL && *lastgc == NULL)`，该条件会初始化 `*lastgc... |
| 2481 | tmux-3.2 | mode_tree_draw | Dereference of null pointer | 757 | FP | FP | 告警点位于 `xasprintf(&text, " %s", mti->name);`，其中 `mti` 指针在切片代码中已通过 `mti = line->item;` 和 `if (mti->draw_as_parent) mti ... |
| 2482 | tmux-3.2 | spawn_window | Dereference of null pointer | 185 | FP | FP | 告警指向 `w->name = default_window_name(w);` 行，但切片代码显示，在多个执行路径中，变量 `w` 在赋值前已被正确初始化或从 `sc->wl->window` 等非空来源获取。在 `(~sc->fl... |
| 2483 | tmux-3.2 | grid_reflow_join | Dereference of null pointer | 1182 | FP | FP | 切片代码显示，在访问 `from` 指针前，`from` 已在 `for` 循环中被赋值为 `&gd->linedata[line]`，且该循环在 `lines == 0` 时提前返回，因此 `from` 在 `left = from... |
| 2484 | tmux-3.2 | server_client_reset_state | Dereference of null pointer | 1672 | FP | FP | 告警行访问的指针 `s` 在切片代码中已被赋值，它要么来自 `c->overlay_mode` 函数的返回值（若条件满足），要么被赋值为 `wp->screen`。`wp` 来自 `server_client_get_pane` 函数... |
| 2485 | tmux-3.2 | input_parse | Dereference of null pointer | 902 | FP | FP | 代码在访问 `ictx->state->transitions` 前，已通过 `if` 条件确保 `ictx->state` 不为 NULL，且告警行位于该条件保护块内。切片中未发现 `ictx->state` 被赋值为 NULL 的... |
| 2486 | tmux-3.1 | spawn_window | Dereference of null pointer | 185 | FP | FP | 切片代码中，在告警行 `w->name = format_single(...)` 之前，变量 `w` 已在多个分支中被赋值或使用（例如 `w = sc->wl->window`），表明 `w` 指针在解引用前已被正确初始化，不存在空... |
| 2487 | tmux-3.1 | grid_string_cells | Dereference of null pointer | 927 | FP | FP | 告警点位于函数 `grid_string_cells_code` 的调用处，其参数 `*lastgc` 在调用前已被检查并初始化。切片代码显示，当 `lastgc != NULL && *lastgc == NULL` 时，`*las... |
| 2489 | tmux-3.1 | grid_reflow_join | Dereference of null pointer | 1126 | FP | FP | 切片代码显示，在访问 `from` 指针前，`from` 已在循环 `for (want = 1; want < from->cellused; want++)` 中被赋值（`from = &gd->linedata[line];`）... |
| 2490 | tmux-3.1 | mode_tree_build | Dereference of null pointer | 407 | FP | FP | 在告警行之前，代码已通过条件 `if (mtd->line_list != NULL)` 检查了 `mtd->line_list` 的有效性，并仅在 `tag == UINT64_MAX` 时才会尝试访问 `mtd->line_lis... |
| 2491 | tmux-3.1 | spawn_window | Dereference of null pointer | 189 | FP | FP | 告警点位于 `w->name = xstrdup(default_window_name(w));`，其中 `w` 指针在切片中已通过 `w = sc->wl->window;` 或 `w = NULL;` 赋值，但存在条件分支 `i... |
| 2492 | tmux-3.1 | cmdq_get_command | Dereference of null pointer | 248 | FP | FP | 在TAILQ_FOREACH循环中，当`cmd->group != group`条件首次为真时，`shared`会被`xcalloc`分配内存，该函数在分配失败时会调用`fatalx`终止程序，因此`shared`在后续被解引用时不可... |
| 2493 | tmux-3.1 | recalculate_sizes | Dereference of null pointer | 387 | FP | FP | 在访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已检查 `c->session` 是否为 NULL，若为 NULL 则提前返回，确保了后续访问 `s`（即 `c->session`）... |
| 2494 | tmux-3.0 | grid_string_cells | Dereference of null pointer | 918 | FP | FP | 告警点位于 `grid_string_cells_code(*lastgc, ...)` 调用处，但切片代码显示，在调用前存在 `if (lastgc != NULL && *lastgc == NULL)` 分支，该分支会初始化 `... |
| 2495 | tmux-3.0 | spawn_window | Dereference of null pointer | 183 | FP | FP | 告警点位于 `w->name = xstrdup(sc->name);`，但切片代码显示，该行仅在 `sc->name != NULL` 时执行。`sc->name` 是函数参数，其来源在切片中不可见，但 `xstrdup` 函数内部... |
| 2496 | tmux-3.0 | grid_reflow_join | Dereference of null pointer | 1117 | FP | FP | 告警点 `left = from->cellused - want;` 中，`from` 指针在循环 `for (want = 1; want < from->cellused; want++)` 中被赋值为 `&gd->lineda... |
| 2497 | tmux-3.0 | mode_tree_build | Dereference of null pointer | 407 | FP | FP | 在告警行之前，代码已通过条件 `if (tag == UINT64_MAX)` 进行保护，仅当 `tag` 不等于 `UINT64_MAX` 时才会执行对 `mtd->line_list` 的访问。结合切片中 `mode_tree_s... |
| 2498 | tmux-3.0 | spawn_window | Dereference of null pointer | 186 | FP | FP | 告警点位于 `w->name = xstrdup(default_window_name(w));`，但切片代码显示，在调用此语句之前，变量 `w` 可能被赋值为 `NULL`（见 `else w = NULL;` 分支）。然而，该赋... |
| 2499 | tmux-3.0 | cmdq_get_command | Dereference of null pointer | 233 | FP | FP | 在TAILQ_FOREACH循环中，当`cmd->group != group`条件首次为真时，`shared`会被`xcalloc`分配内存并初始化，该函数保证返回非空指针（否则会调用`fatalx`终止程序）。因此，在后续的`sh... |
| 2500 | tmux-3.0 | options_array_set | Dereference of null pointer | 368 | FP | FP | 在切片代码中，对 `cause` 指针的赋值操作 `*cause = xstrdup(...)` 之前，已经通过 `if (cause != NULL)` 进行了明确的空指针检查，确保了 `cause` 非空时才进行解引用，因此不存在... |
| 2501 | tmux-3.4 | recalculate_sizes_now | Dereference of null pointer | 458 | FP | FP | 在访问 `s->statuslines` 之前，`ignore_client_size(c)` 函数已对 `c->session` 进行了空指针检查，确保 `s` 不为空。切片代码中的逻辑表明，当 `c->session` 为空时，循... |
| 2502 | tmux-3.4 | mode_tree_draw | Dereference of null pointer | 750 | FP | FP | 切片代码中，在告警行（xasprintf调用）之前，已通过条件判断 `if (mtd->sort_list != NULL)` 确保 `mtd->sort_list` 不为空时才访问其数组元素，因此不会发生空指针解引用。告警是误报。 |
| 2503 | tmux-3.4 | mode_tree_get_tag | Dereference of null pointer | 309 | FP | FP | 切片代码显示，在访问 `mtd->line_list[i].item->tag` 之前，循环条件 `i < mtd->line_size` 确保了索引 `i` 在 `line_list` 数组的有效范围内。虽然没有直接检查 `item... |
| 2504 | tmux-3.4 | mode_tree_draw | Dereference of null pointer | 754 | FP | FP | 告警点位于 `xasprintf(&text, " %s", mti->name);`，但切片代码显示 `mti` 指针在多个前置条件检查（如 `mtd->preview`、`sy <= 4` 等）和赋值（`mti = line->i... |
| 2505 | tmux-3.4 | grid_reflow_join | Dereference of null pointer | 1286 | FP | FP | 切片代码显示，在访问 `from` 指针前，`from` 已在 `for` 循环中被赋值为 `&gd->linedata[line]`，且该循环在 `lines` 不为零时才会执行到后续代码。当 `lines == 0` 时函数直接返... |
| 2506 | tmux-3.4 | spawn_window | Dereference of null pointer | 181 | FP | FP | 告警点 `free(w->name);` 位于条件分支 `if (~sc->flags & SPAWN_RESPAWN)` 内部，而在此分支之前，存在一个 `else` 分支将 `w` 显式设置为 `NULL`。当 `sc->flag... |
| 2507 | tmux-3.4 | grid_string_cells | Dereference of null pointer | 1073 | FP | FP | 切片代码显示，在调用 `grid_string_cells_code(*lastgc, ...)` 之前，存在条件判断 `if (lastgc != NULL && *lastgc == NULL)`，该条件会初始化 `*lastgc... |
| 2508 | tmux-3.4 | server_client_reset_state | Dereference of null pointer | 2394 | FP | FP | 告警行引用的指针 `s` 在切片代码中已通过条件分支被正确初始化，要么指向 `c->overlay_mode` 的返回值，要么指向 `wp->screen`，且 `wp` 通过 `server_client_get_pane` 获取，... |
| 2509 | tmux-3.4 | window_copy_move_after_search_mark | Dereference of null pointer | 3691 | FP | FP | 在访问 `data->searchmark[start]` 之前，代码已通过 `window_copy_search_mark_at` 函数调用成功返回0，这确保了 `start` 索引是有效的，并且指向 `data->searchm... |
| 2510 | tmux-3.4 | input_parse | Dereference of null pointer | 912 | FP | FP | 在访问 `ictx->state->transitions` 之前，代码逻辑已通过 `if` 条件确保 `ictx->state` 不为 NULL，且 `fatalx` 函数会在 `itr` 查找失败时终止程序，防止了空指针解引用。 |

### 5.3 不一致：算法=TP，LLM=FP（共 99 条）

> 算法认为是真实漏洞（TP），但 LLM 认为是误报（FP）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 276 | git-2.47.1 | test_ctype__isxdigit | cpp/overflow-buffer | 96 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是字符串字面量 `DIGIT "abcdefABCDEF"`，其 `ARRAY_SI... |
| 277 | git-2.47.1 | test_ctype__ispunct | cpp/overflow-buffer | 91 | TP | FP | 宏定义 `TEST_CHAR_CLASS` 中的 `ARRAY_SIZE(string) - 1` 仅在 `ARRAY_SIZE(string)` 为 0 时结果为 -1，但宏内包含 `BUILD_ASSERT_OR_ZERO(ARR... |
| 278 | git-2.47.1 | test_ctype__iscntrl | cpp/overflow-buffer | 86 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被 `BUILD_ASSERT_OR_ZERO` 保护，当数组大小为0时断言会触发编译失败，因此实际... |
| 279 | git-2.47.1 | test_ctype__is_pathspec_magic | cpp/overflow-buffer | 66 | TP | FP | 告警源于宏展开，但宏定义中 `ARRAY_SIZE(string) - 1` 仅在数组大小为0时结果为-1，而传入的字符串字面量 `"!\"#%&',-/:;<=>@_`~"` 长度大于0，因此不会发生负索引访问。这是静态分析工具对宏... |
| 280 | git-2.47.1 | test_ctype__is_regex_special | cpp/overflow-buffer | 61 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但传入的字符串字面量 `"$()*+.?[\\^{｜"` 长度大于0，因此 `ARRAY_SIZE(str... |
| 281 | git-2.47.1 | test_ctype__is_glob_special | cpp/overflow-buffer | 56 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但传入的字符串字面量 `"*?[\\"` 长度大于0，因此 `ARRAY_SIZE(string) - 1... |
| 282 | git-2.47.1 | test_ctype__isalnum | cpp/overflow-buffer | 51 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，但该表达式仅在 `ARRAY_SIZE(string) > 0` 的编译时断言通过时才会执行，且 `st... |
| 283 | git-2.47.1 | test_ctype__isalpha | cpp/overflow-buffer | 46 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但 `string` 是宏参数 `LOWER UPPER`，它由字符字面量组成，`ARRAY_SIZE` ... |
| 284 | git-2.47.1 | test_ctype__isdigit | cpp/overflow-buffer | 41 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 表达式中，但该表达式受 `BUILD_ASSERT_OR_ZERO(ARRAY_SIZE(string) > 0)... |
| 285 | git-2.47.1 | <global> | cpp/overflow-buffer | 36 | TP | FP | 切片代码仅为一个空函数定义，未包含任何数组索引操作，因此告警所描述的访问负索引-1的情况在提供的上下文中不存在。 |
| 403 | git-2.46.0 | get_rev | cpp/inconsistent-null-check | 189 | TP | FP | 在调用 `prio_queue_get` 后，代码立即通过 `entry->commit` 访问其成员，这隐含了对 `entry` 非空的假设。切片代码显示，在调用 `prio_queue_get` 之前，已经检查了 `data->r... |
| 406 | git-2.46.0 | fill_bitmap_commit | cpp/inconsistent-null-check | 493 | TP | FP | 切片代码显示，调用 `prio_queue_get` 的循环条件 `while (queue->nr)` 确保了队列非空，且 `prio_queue_get` 函数内部在 `queue->nr` 为 0 时会返回 NULL。因此，在循... |
| 410 | git-2.46.0 | <global> | cpp/overflow-buffer | 37 | TP | FP | 切片代码仅显示空函数定义，未包含任何数组索引操作，无法支持告警中描述的访问负索引-1的结论。参考算法标签为TP，但代码证据不足，倾向于判定为误报。 |
| 411 | git-2.46.0 | <global> | cpp/overflow-buffer | 38 | TP | FP | 提供的切片代码仅显示一个空的函数定义，没有任何数组访问或索引操作，因此告警所描述的访问负索引-1的情况在可见代码中不存在，属于误报。 |
| 412 | git-2.46.0 | <global> | cpp/overflow-buffer | 39 | TP | FP | 提供的切片代码仅显示函数框架，未包含任何数组索引操作，无法支持告警中描述的访问负索引-1的行为，因此判定为误报。 |
| 413 | git-2.46.0 | <global> | cpp/overflow-buffer | 40 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被调用时传入的 `string` 参数（如 `LOWER UPPER DIGIT`）是字符串字面量，... |
| 414 | git-2.46.0 | <global> | cpp/overflow-buffer | 41 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被调用时传入的 `string` 参数是字符串字面量，其 `ARRAY_SIZE` 结果大于0，因此... |
| 415 | git-2.46.0 | <global> | cpp/overflow-buffer | 42 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，其中 `string` 是字符串字面量。`ARRAY_SIZE` 宏返回数组元素数量，对于非空字符串字面量... |
| 416 | git-2.46.0 | <global> | cpp/overflow-buffer | 43 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏的调用参数 `string` 是字符串字面量，其 `ARRAY_SIZE` 结果大于0，因此 `AR... |
| 417 | git-2.46.0 | <global> | cpp/overflow-buffer | 47 | TP | FP | 告警指出的负索引访问发生在宏 `TEST_CHAR_CLASS` 的 `ARRAY_SIZE(string) - 1` 计算中，但该宏被调用时传入的 `string` 参数（如 `CNTRL`）是字符串字面量，其 `ARRAY_SIZ... |
| 418 | git-2.46.0 | <global> | cpp/overflow-buffer | 48 | TP | FP | 告警源于宏 `TEST_CHAR_CLASS` 中对 `string[-1]` 的访问，这是宏 `ARRAY_SIZE` 在编译时计算数组大小的标准用法（`sizeof(string)/sizeof(string[0])`），并非运行... |
| 419 | git-2.46.0 | <global> | cpp/overflow-buffer | 49 | TP | FP | 切片代码显示，`TEST_CHAR_CLASS`宏中的`ARRAY_SIZE(string) - 1`操作仅在`ARRAY_SIZE(string) > 0`时执行，且该条件由`BUILD_ASSERT_OR_ZERO`宏保证，因此不... |
| 470 | curl-8_9_1 | Curl_splayremove | cpp/inconsistent-null-check | 270 | TP | FP | 在调用 `Curl_splay` 前，代码已通过 `if(!t->smaller)` 检查了 `t->smaller` 是否为空，当其为空时不会执行该调用。当执行到该调用时，`t->smaller` 已被确认非空，因此 `Curl_s... |
| 673 | vim-9.1.1591 | <global> | cpp/redundant-null-check-simple | 3506 | TP | FP | 告警指出的空指针检查冗余，但切片代码显示在检查 `inc_opt != NULL` 之前，`inc_opt` 已被赋值为 `(*curbuf->b_p_inc == NUL) ? p_inc : curbuf->b_p_inc`，这保... |
| 674 | vim-9.1.1591 | <global> | cpp/redundant-null-check-simple | 3588 | TP | FP | 告警指出的空指针检查冗余，但切片代码显示在检查前指针已被显式初始化为NULL，且后续逻辑在解引用前有明确的空指针检查（如`if (regmatch.regprog == NULL)`），因此该检查是必要的安全防护，并非冗余。 |
| 675 | vim-9.1.1591 | findmatchlimit | cpp/offset-use-before-range-check | 2530 | TP | FP | 告警点位于条件判断 `(int)pos.col < comment_col` 中，其中 `pos.col` 是 `colnr_T`（无符号类型），`comment_col` 是 `int`。在比较前，`pos.col` 被显式转换为 ... |
| 676 | vim-9.1.1591 | common_function | cpp/inconsistent-null-check | 5253 | TP | FP | 代码在调用 `vim_strsave` 后，其返回值 `name` 在后续逻辑中会被 `vim_free(name)` 释放，这表明代码已处理了内存分配失败的情况（即 `name` 为 NULL 时 `vim_free` 是安全的）。... |
| 677 | vim-9.1.1591 | common_function | cpp/inconsistent-null-check | 5366 | TP | FP | 告警行 `pt->pt_func = find_func(trans_name, is_global);` 的返回值被直接赋值给 `pt->pt_func`，但切片代码显示，在调用 `find_func` 之前，已经通过条件 `tra... |
| 679 | vim-9.1.1591 | get_isolated_shell_name | cpp/inconsistent-null-check | 2743 | TP | FP | 函数 `gettail` 已对空指针输入进行了防护，返回空字符串而非NULL，因此 `vim_strsave` 的输入不会是NULL，其返回值也无需额外检查。代码逻辑在切片可见范围内是安全的。 |
| 681 | vim-9.1.1591 | did_set_cryptmethod | cpp/inconsistent-null-check | 1923 | TP | FP | 告警指出未检查 vim_strsave 的返回值是否为 NULL，但在切片代码中，p_cm 被赋值为 vim_strsave((char_u *)"zip")，其参数是常量字符串 "zip"，分配内存失败的可能性极低。此外，该函数在内... |
| 682 | vim-9.1.1591 | did_set_background | cpp/inconsistent-null-check | 1098 | TP | FP | 告警点 `p_bg = vim_strsave(...)` 的返回值被立即传递给 `check_string_option(&p_bg)` 函数，该函数在切片中明确包含对空指针的检查和处理（若为空则赋值为 `empty_option`... |
| 683 | vim-9.1.1591 | apply_move_options | cpp/inconsistent-null-check | 531 | TP | FP | 在调用 `find_win_by_nr_or_id` 后，代码立即使用 `win_valid_any_tab` 检查返回的窗口指针是否有效，若无效则回退到 `curwin`。这表明代码已对可能的空指针进行了防护，因此告警为误报。 |
| 684 | vim-9.1.1591 | <global> | cpp/inconsistent-null-check | 3339 | TP | FP | 代码中`regnext`函数已包含空指针检查（返回NULL），且调用后`next`变量在后续逻辑中未直接解引用，而是通过`OP(next)`等宏安全使用，切片中未见因未检查而导致的空指针解引用风险。 |
| 685 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1541 | TP | FP | 代码切片显示，对 `regnode` 的调用结果 `br` 被立即用于条件判断 `if (ret == NULL)` 和后续的 `regtail` 操作，其值未被直接用于可能引发空指针解引用的危险操作。且 `regtail` 函数内部... |
| 686 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1562 | TP | FP | 切片代码显示，在调用 `regnode(NOTHING)` 之前，存在对 `reg_toolong` 标志的检查，并且当该标志为真时，函数会提前返回 NULL。这表明存在控制流防护，且 `regnode` 函数内部处理了 `JUST_... |
| 687 | vim-9.1.1591 | regatom | cpp/inconsistent-null-check | 1579 | TP | FP | 在切片代码中，`br = regnext(br)` 的调用位于一个循环内，该循环在 `ret != JUST_CALC_SIZE` 的条件下执行，并且循环体内部有 `if (reg_toolong) return NULL;` 的检查... |
| 688 | vim-9.1.1591 | get_wordnode | cpp/inconsistent-null-check | 4636 | TP | FP | 函数 `getroom` 在内存分配失败时会返回 NULL，但调用点 `get_wordnode` 在 `spin->si_first_free == NULL` 时才会调用 `getroom`，且后续的 `#ifdef SPELL_... |
| 689 | vim-9.1.1591 | do_tag | cpp/inconsistent-null-check | 638 | TP | FP | 切片代码显示，`vim_strsave` 的返回值 `name` 在后续逻辑中被立即赋值给 `tofree` 并由 `vim_free(tofree)` 释放，这表明代码已处理了内存分配失败的情况（通过 `vim_free` 处理 N... |
| 690 | vim-9.1.1591 | is_duplicate_variable | cpp/inconsistent-null-check | 1044 | TP | FP | 提供的切片代码中，函数 `is_duplicate_variable` 的函数体为空，未包含对 `vim_strnsave` 的调用，因此无法确认存在未检查返回值的空指针风险。告警可能指向了不存在的代码或切片不完整，结合空函数体判断为误报。 |
| 691 | vim-9.1.1591 | exec_instructions | cpp/inconsistent-null-check | 3699 | TP | FP | 代码中alloc_clear调用后立即将返回值赋值给tv->vval.v_object，后续代码直接访问该对象的成员（如obj_class），若alloc_clear返回NULL会导致空指针解引用。但切片中未包含对返回值的NULL检查... |
| 692 | vim-9.1.1591 | barline_parse | cpp/inconsistent-null-check | 1158 | TP | FP | 代码中调用 `vim_strnsave` 的结果被赋值给局部变量 `s`，随后立即赋值给 `value->bv_string`，但 `value->bv_allocated` 被设置为 `allocated ｜｜ converted`... |
| 693 | vim-9.1.1591 | common_function | cpp/unsafe-strcat | 5401 | TP | FP | 切片代码中，STRCAT宏用于拼接已知的、受控的字符串（name和start_bracket），且name由vim_strsave分配，start_bracket指向输入字符串中的特定位置，不存在未检查源缓冲区大小的问题。告警点位于安... |
| 694 | vim-9.1.1591 | helptags_one | cpp/unsafe-strcat | 975 | TP | FP | 告警点位于构建文件路径模式字符串的代码中，`dir` 和 `ext` 参数来自受控的配置文件或命令行，并非不可信的用户输入。代码使用 `STRCAT` 宏拼接已知的目录路径和固定后缀，目标缓冲区 `NameBuff` 的大小为 `MA... |
| 696 | vim-9.1.1591 | store_aff_word | cpp/unsafe-strcat | 3915 | TP | FP | 代码在调用STRCAT宏（即strcat）前，已通过vim_strncpy将目标缓冲区newword初始化为有限长度（MAXWLEN-1），并确保源字符串p是原始单词word经过安全截断后的部分，其长度受原始单词长度和缓冲区剩余空间约... |
| 704 | vim-9.1.1591 | buf_write | cpp/unbounded-write | 2568 | TP | FP | 切片代码中未发现对strcat函数的直接调用，告警提及的'call to strcat'在提供的上下文中不可见。该告警可能基于不完整或过时的分析，且代码中涉及缓冲区操作的部分（如使用alloc和固定大小的smallbuf）似乎有大小管... |
| 717 | vim-9.1.1591 | ex_substitute | cpp/unbounded-write | 5115 | TP | FP | 切片代码中未发现对 `strcat` 的直接调用，告警消息中提到的多个 `strcat` 调用在提供的代码片段中不可见。该告警可能指向宏 `STRCAT` 的使用，但切片中仅有一处 `STRCAT(new_start, sub_fir... |
| 719 | vim-9.1.1591 | make_filter_cmd | cpp/unbounded-write | 1858 | TP | FP | 代码在调用STRCAT（即strcat）前，已通过alloc(len)为目标缓冲区buf分配了精确计算的长度len，且后续的vim_snprintf和STRCAT操作均未超过此预分配大小。告警所提及的strcat溢出风险在切片代码的上... |
| 730 | vim-9.1.1591 | discard_exception | cpp/unbounded-write | 646 | TP | FP | 告警点 `STRCPY(IObuff, saved_IObuff)` 中，目标缓冲区 `IObuff` 是全局缓冲区，其大小 `IOSIZE` 在切片中未明确定义但应是固定大小。源字符串 `saved_IObuff` 是 `IObuf... |
| 739 | vim-9.1.1591 | addfile | cpp/unbounded-write | 4219 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已使用alloc(STRLEN(f) + 1 + isdir)为目标缓冲区p分配了精确的内存空间，其大小为源字符串f的长度加1（以及可能的目录分隔符）。这确保了目标缓冲区足以容纳... |
| 740 | vim-9.1.1591 | concat_fnames | cpp/unbounded-write | 3134 | TP | FP | 代码通过alloc函数为目标缓冲区分配了足够的空间，其大小为两个源字符串长度之和加3，确保了strcpy操作不会发生缓冲区溢出。 |
| 750 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2901 | TP | FP | 代码中`buffer`数组大小为256字节，而`res_prolog->title`和`res_prolog->version`是从受控的PostScript资源文件中解析出的固定字符串，其长度在解析时已被限制（`vim_strncp... |
| 756 | vim-9.1.1591 | mch_print_begin | cpp/unbounded-write | 2922 | TP | FP | 切片代码显示，`buffer` 数组大小为256字节，而 `res_encoding->title` 和 `res_encoding->version` 是从受控的PostScript资源文件中解析出的短字符串，其长度在解析时已被限制... |
| 770 | vim-9.1.1591 | ins_compl_infercase_gettext | cpp/unbounded-write | 723 | TP | FP | 切片代码显示，在调用STRCPY（即strcpy）之前，已通过条件`(p - IObuff) + 6 >= IOSIZE`确保目标缓冲区`gap.ga_data`有足够空间（通过`ga_grow(&gap, IOSIZE)`分配），且... |
| 772 | vim-9.1.1591 | findswapname | cpp/unbounded-write | 4967 | TP | FP | 代码中 `STRCPY(fname2, fname)` 的目标缓冲区 `fname2` 是通过 `alloc(n + 2)` 分配的，大小为 `n + 2`，而源字符串 `fname` 的长度 `n` 已通过 `STRLEN(fnam... |
| 773 | vim-9.1.1591 | <global> | cpp/unbounded-write | 2157 | TP | FP | 代码通过 `alloc(STRLEN(f) + 1)` 为目标缓冲区 `s` 分配了精确匹配源字符串 `f` 长度的空间，`STRCPY(s, f)` 执行的是安全复制，不会发生缓冲区溢出。 |
| 777 | vim-9.1.1591 | str2specialbuf | cpp/unbounded-write | 2015 | TP | FP | 切片代码中，在调用STRCAT（即strcat）之前，已通过条件`if ((int)(STRLEN(s) + STRLEN(buf)) < len)`检查了目标缓冲区`buf`的剩余空间是否足够容纳待追加的字符串`s`，该防护机制有效... |
| 779 | vim-9.1.1591 | may_trigger_modechanged | cpp/unbounded-write | 2869 | TP | FP | STRCPY宏展开为strcpy，但源字符串curr_mode来自get_mode函数，该函数内部逻辑确保写入的字符数有限（从切片看最多几个字符），且目标缓冲区last_mode（全局变量）大小未在切片中明确给出，但结合上下文（模式字... |
| 784 | vim-9.1.1591 | add_to_showcmd | cpp/unbounded-write | 1764 | TP | FP | 切片代码显示，在调用STRCAT前，程序已计算了`old_len`和`extra_len`，并检查了`overflow`。如果存在溢出风险，会通过`mch_memmove`移动缓冲区内容以腾出空间，这构成了有效的边界防护，因此告警为误报。 |
| 790 | vim-9.1.1591 | option_value2string | cpp/unbounded-write | 8459 | TP | FP | 切片代码显示，STRCPY宏的目标缓冲区是NameBuff，但未提供其大小定义。然而，在P_STRING分支中，对同一缓冲区的操作（如vim_strncpy）使用了明确的长度限制MAXPATHL，这表明NameBuff可能被设计为足够... |
| 795 | vim-9.1.1591 | qf_store_title | cpp/unbounded-write | 1940 | TP | FP | 代码在调用STRCPY（即strcpy）前，已使用alloc_id为目的地缓冲区分配了足够的内存，其大小为源字符串长度加2，这确保了缓冲区大小足以容纳源字符串及可能的额外字符，因此不存在缓冲区溢出风险。 |
| 810 | vim-9.1.1591 | make_case_word | cpp/unbounded-write | 3140 | TP | FP | 告警点位于 `make_case_word` 函数的默认分支，该分支仅在 `fword` 无需大小写转换时执行。`fword` 是函数参数，其来源在切片中不可见，但调用者 `allcap_copy` 和 `onecap_copy` 函... |
| 816 | vim-9.1.1591 | getroom_save | cpp/unbounded-write | 4341 | TP | FP | 函数 `getroom` 已根据源字符串长度 `STRLEN(s) + 1` 分配了足够的内存，`STRCPY` 的目标缓冲区大小与源字符串长度匹配，不存在缓冲区溢出风险。 |
| 825 | vim-9.1.1591 | suggest_try_change | cpp/unbounded-write | 1199 | TP | FP | STRCPY宏的目标缓冲区fword被定义为char_u fword[MAXWLEN]，其大小固定为MAXWLEN，而源字符串su->su_fbadword是内部拼写检查数据结构的一部分，其长度在调用前已被限制为不超过MAXWLEN（... |
| 826 | vim-9.1.1591 | concat_str | cpp/unbounded-write | 792 | TP | FP | 函数 `concat_str` 通过 `alloc` 为目标缓冲区 `dest` 分配了精确的、足以容纳两个源字符串（包括结尾空字符）的内存大小，随后才调用 `STRCPY`（即 `strcpy`）。在切片可见的代码逻辑中，不存在缓冲... |
| 827 | vim-9.1.1591 | concat_str | cpp/unbounded-write | 794 | TP | FP | 函数 `concat_str` 在调用 `STRCPY`（即 `strcpy`）前，已通过 `alloc` 为目标缓冲区 `dest` 分配了足够的空间，其大小为两个源字符串长度之和加1，确保了缓冲区大小足以容纳拼接后的字符串，因此不... |
| 837 | vim-9.1.1591 | alloc_ufunc | cpp/unbounded-write | 728 | TP | FP | 代码通过 `alloc_clear` 分配了足够的内存，其大小为 `len` 或 `sizeof(ufunc_T)` 中的较大者，而 `len` 已包含 `namelen + 1` 作为目标缓冲区 `uf_name` 的大小，因此 `... |
| 838 | vim-9.1.1591 | exec_instructions | cpp/unbounded-write | 3929 | TP | FP | 切片代码中未发现任何对strcpy的调用，告警消息中提到的多个strcpy调用在提供的代码片段中不存在。该告警可能是针对其他代码位置，但在当前切片中无法验证。 |
| 841 | vim-9.1.1591 | find_exported | cpp/unbounded-write | 756 | TP | FP | 代码在调用sprintf前已通过动态分配确保了目标缓冲区大小足够（len < sizeof(buffer)时使用栈缓冲区，否则分配len大小的堆缓冲区），因此不存在缓冲区溢出风险。 |
| 845 | vim-9.1.1591 | update_snapshot | cpp/invalid-pointer-deref | 2075 | TP | FP | 切片代码显示，在写入 `p[pos.col + 1]` 之前，已通过 `if (width == 2)` 条件确保 `pos.col + 1` 小于分配的 `len`（因为 `width` 为2时，`pos.col` 在循环中递增 `... |
| 1426 | redis-7.0.11 | rb_gen | Dereference of null pointer | 273 | TP | FP | 提供的切片代码仅为宏定义或函数声明，未展示任何实际的指针解引用操作，无法确认存在空指针解引用逻辑。参考算法标签为TP，但代码切片中缺乏支持该结论的证据，倾向于判定为误报。 |
| 1431 | redis-7.0.11 | <global> | Dereference of null pointer | 307 | TP | FP | 提供的切片代码 `prof_tdata_comp)` 仅为函数名或标识符的一部分，不构成任何可分析的代码逻辑或数据流，无法支持空指针解引用告警的判断。基于此，判定为误报。 |
| 1434 | redis-7.0.11 | <global> | Dereference of null pointer | 288 | TP | FP | 提供的切片代码 `sliced_code` 仅为 `prof_gctx_comp)\n`，这是一个不完整的代码片段，无法从中识别出任何变量、指针或逻辑，因此无法确认存在空指针解引用。基于信息不足，倾向于参考算法标签的相反结论，判定为误报。 |
| 1586 | redis-8.0.2 | strbuf_init | Dereference of null pointer | 55 | TP | FP | 代码仅对结构体指针`s`的成员`buf`进行赋值`NULL`，并未对`s`本身或其成员进行解引用操作，不存在空指针解引用。告警为逻辑错误。 |
| 1587 | redis-8.0.2 | breakstat | Dereference of null pointer | 986 | TP | FP | 在while循环中，变量`bl`被更新，但循环条件`while (bl && !bl->isbreakable)`确保了只有当`bl`非空时才会进入循环体并更新`bl`。循环结束后，`bl`可能为空，但后续代码`if (upval)`... |
| 1594 | redis-8.0.2 | extent_try_coalesce_impl | Dereference of null pointer | 869 | TP | FP | 告警指向的代码行 `*coalesced = false;` 是对布尔指针 `coalesced` 的赋值，该指针作为函数参数传入，在切片中未见其为空（NULL）的证据。结合函数逻辑，`coalesced` 在循环中已被使用，其有效性... |
| 1598 | redis-8.0.2 | rb_gen | Dereference of null pointer | 88 | TP | FP | 提供的切片代码仅为宏定义或函数声明，未展示任何实际的指针解引用操作，无法确认存在空指针解引用逻辑。参考算法标签为TP，但代码证据不足，倾向于判定为工具误报。 |
| 1601 | redis-8.0.2 | extent_try_coalesce_impl | Dereference of null pointer | 844 | TP | FP | 切片代码中，对指针 `next` 和 `prev` 在使用前都进行了明确的非空检查（`if (next != NULL)` 和 `if (prev != NULL)`），逻辑上避免了空指针解引用。告警点位于 `*coalesced =... |
| 1602 | redis-8.0.2 | <global> | Dereference of null pointer | 122 | TP | FP | 提供的切片代码仅为一行函数名或宏定义，未包含任何实际的指针解引用操作或相关数据流，无法支持空指针解引用这一逻辑错误的判定。基于代码切片信息不足，倾向于参考算法标签的相反结论，判定为误报。 |
| 1606 | redis-8.0.2 | <global> | Dereference of null pointer | 103 | TP | FP | 提供的切片代码 `sliced_code` 仅为一行不完整的变量名 `prof_gctx_comp)`，无法构成任何有意义的代码逻辑或数据流上下文，无法识别出任何空指针解引用操作。基于可见信息，无法支持该告警为真实问题，因此判定为误报。 |
| 1608 | redis-8.0.2 | tcache_create_ctl | Dereference of null pointer | 2467 | TP | FP | 告警点位于宏 `VERIFY_READ` 内部，该宏在解引用 `oldlenp` 前已通过 `if (oldp == NULL ｜｜ oldlenp == NULL ｜｜ ...)` 进行了空指针检查，因此不会发生空指针解引用。切片代... |
| 1612 | redis-8.0.2 | experimental_batch_alloc_ctl | Dereference of null pointer | 4273 | TP | FP | 告警指向的代码行是宏 `VERIFY_READ`，该宏已对指针 `oldp` 和 `oldlenp` 进行了非空和长度校验，若为空则直接跳转返回，不会发生空指针解引用。切片代码中未见解引用空指针的逻辑。 |
| 1613 | redis-8.0.2 | json_next_token | Dereference of null pointer | 1024 | TP | FP | 切片代码显示，在访问 `ch2token[ch]` 之前，`ch` 的值来自 `*(json->ptr)`，而 `json->ptr` 在循环中会递增，但始终指向 `json->data` 缓冲区内的位置。只要 `json->data... |
| 1620 | redis-8.0.2 | min_expand | Dereference of null pointer | 322 | TP | FP | 在告警行 `singlematch(uchar(*s), p, ep)` 中，`s` 指针在调用前已通过条件 `s<ms->src_end` 进行了边界检查，确保了 `s` 指向有效内存，因此解引用 `*s` 是安全的。该告警为误报。 |
| 1625 | redis-8.0.2 | arenas_create_ctl | Dereference of null pointer | 3101 | TP | FP | 告警指向的 `VERIFY_READ` 宏已对 `oldp` 和 `oldlenp` 指针进行了明确的空值检查，若为空则直接跳转返回，不会发生空指针解引用。切片代码中可见完整的防护逻辑，因此是误报。 |
| 1626 | redis-8.0.2 | experimental_arenas_create_ext_ctl | Dereference of null pointer | 3126 | TP | FP | 切片代码显示，在调用 `VERIFY_READ` 宏时，若 `oldp` 或 `oldlenp` 为 NULL，宏内部会设置错误码并跳转到 `label_return` 提前返回，不会发生空指针解引用。该告警是静态分析工具对宏展开逻辑... |
| 1749 | ffmpeg-7.0.1 | ff_hevc_hls_residual_coding | Dereference of null pointer | 1428 | TP | FP | 切片代码显示，在访问 `scale_matrix[pos]` 之前，存在条件 `if (s->ps.sps->scaling_list_enable_flag && !(transform_skip_flag && log2_traf... |
| 1765 | ffmpeg-7.0.1 | check_available | Dereference of null pointer | 608 | TP | FP | 代码中 `TAB_MVF` 宏访问的 `tab_mvf` 数组指针未在切片中定义或初始化，无法确认其为空。告警基于对未定义变量的假设，且 `label` 为 TP 但代码证据不足，倾向于判定为工具误报。 |
| 1794 | ffmpeg-7.0.1 | avc_parse_nal_units | Dereference of null pointer | 92 | TP | FP | 切片代码显示，在访问 `list->nalus` 之前，已通过 `list->nb_nalus >= nalu_limit` 检查进行保护，若条件为真则直接返回错误，避免了空指针解引用。代码逻辑安全。 |
| 1813 | ffmpeg-7.0.1 | <global> | Dereference of null pointer | 471 | TP | FP | 告警指向宏 `DECODE_CODEWORD` 的调用，但切片代码显示该宏内部包含 `UPDATE_CACHE` 和 `GET_CACHE` 操作，这些操作通常涉及对 `GetBitContext *gb` 指针的访问。由于 `gb`... |
| 2140 | git-2.49.0 | process_entry | Dereference of null pointer | 3413 | TP | FP | 切片代码显示，在访问 `ci->ren2->pair->two->path` 之前，已经通过 `if (ci->ren2)` 语句对 `ci->ren2` 进行了非空检查，确保了指针的有效性。因此，该处解引用空指针的风险已被防护，属于误报。 |
| 2253 | git-2.50.1 | <global> | Dereference of null pointer | 88 | TP | FP | 告警位于单元测试代码中，对 `out[0]` 的访问前有明确的 `check(out != NULL)` 检查，且 `parse_names` 函数在成功时返回非空指针。切片代码显示访问是安全的，属于静态分析工具对测试代码的误报。 |
| 2262 | git-2.50.1 | <global> | Dereference of null pointer | 82 | TP | FP | 告警指向的代码行 `check_str(out[0], "line");` 位于单元测试函数中，其上下文已通过 `check(out != NULL);` 确保了 `out` 指针非空。该测试旨在验证 `parse_names` 函数... |
| 2285 | git-2.50.1 | write_table | Dereference of null pointer | 65 | TP | FP | 切片代码显示 `(*names)[i]` 的赋值来自 `xstrfmt` 的返回值，该函数返回新分配的内存指针，不会为 NULL。同时，`REFTABLE_CALLOC_ARRAY` 宏保证了 `refs` 和 `logs` 数组的有... |
| 2297 | git-2.50.1 | <global> | Dereference of null pointer | 200 | TP | FP | 告警指向的代码行 `arr[0] = 42;` 位于单元测试函数中，且紧接在 `REFTABLE_ALLOC_GROW_OR_NULL(arr, 1, alloc);` 和 `check(arr != NULL);` 之后。切片代码显... |
| 2300 | git-2.50.1 | t_log_write_read | Dereference of null pointer | 224 | TP | FP | 告警指向的 `names[i] = xstrdup(name);` 行，`xstrdup` 函数内部已对 `strdup` 失败的情况调用 `die` 终止程序，因此不会发生空指针解引用。切片中未见后续对 `names[i]` 进行空... |
| 2308 | git-2.50.1 | <global> | Dereference of null pointer | 206 | TP | FP | 告警点位于单元测试代码中，该行 `arr[alloc - 1] = 42;` 之前有 `check(arr != NULL);` 和 `check_uint(alloc, >, old_alloc);` 断言，确保了数组指针非空且索引... |
| 2313 | git-2.50.1 | t_table_refs_for | Dereference of null pointer | 577 | TP | FP | 切片代码显示 `want_names` 数组在循环前未初始化，但告警行 `want_names[want_names_len++] = xstrdup(name);` 中 `want_names` 的地址并未在切片中定义或分配，这通常... |
| 2367 | git-2.47.1 | assert_sane_strbuf | Dereference of null pointer | 36 | TP | FP | 切片代码显示，在解引用 `buf->buf` 之前，已通过 `check(!!buf->buf)` 宏对指针进行了非空检查，该检查失败将导致函数提前返回，因此后续的 `buf->buf[buf->len]` 访问是受保护的。 |
| 2488 | tmux-3.1 | <global> | Dereference of null pointer | 74 | TP | FP | 切片代码显示，在调用 `window_pane_key` 函数前，已对 `item` 指针进行了非空检查（`if (item != NULL)` 在 `key_bindings_dispatch` 中），且告警行 `window_pa... |

### 5.4 不一致：算法=FP，LLM=TP（共 12 条）

> 算法认为是误报（FP），但 LLM 认为是真实漏洞（TP）。

| ID | 项目 | 函数 | 规则 | 行号 | label | llm_label | LLM 理由 |
|---|---|---|---|---|---|---|---|
| 507 | vim-9.1.0550 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 "%6ld" 写入一个长整数，最多需要 6 位数字加上可能的负号和字符串终止符，最多 8 字节，但目标缓冲区 tbuf 大小为 20 字节，足够容纳，因此告警是误报。 |
| 510 | vim-9.1.0550 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf函数将格式化的字符串写入大小为32字节的固定缓冲区reply，当cmdno和result的值组合超过31个字符（加上空终止符）时，会导致缓冲区溢出。切片代码中未见任何对输出字符串长度的检查或防护机制。 |
| 622 | vim-9.1.0550 | reg_submatch | cpp/unbounded-write | 2689 | FP | TP | 切片代码中，`STRCPY` 宏直接展开为不安全的 `strcpy`，且目标缓冲区 `retval` 的大小 `len` 是根据匹配的文本位置动态计算的，但 `strcpy` 调用时未检查源字符串 `s` 的长度是否超过目标缓冲区剩余... |
| 700 | vim-9.1.1591 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf函数的目标缓冲区'reply'大小为32字节，但格式化字符串'%d %ld\n'在最坏情况下（如cmdno为负10位数，result为负19位数）可能超过32字节，导致缓冲区溢出。切片代码中未见任何长度检查或使用安全函数... |
| 869 | vim-9.1.1040 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 目标缓冲区 tbuf 大小为 20 字节，但格式化字符串 "%6ld" 最多可产生 6 位数字加一个负号共 7 个字符，加上字符串终止符共 8 字节，不会溢出。然而，告警提示需要 21 字节，这可能是因为 lnum 类... |
| 872 | vim-9.1.1040 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf函数将格式化的字符串写入大小为32字节的固定缓冲区reply，当cmdno和result的值组合超过31个字符（加上空终止符）时，会导致缓冲区溢出。切片代码中未见任何对输出长度的检查或防护机制。 |
| 1054 | vim-9.1.1330 | prt_line_number | cpp/overrunning-write | 387 | FP | TP | sprintf 使用格式字符串 "%6ld" 写入一个长整型到大小为 20 字节的缓冲区 tbuf。对于某些负数值，格式化后的字符串长度可能达到 7 个字符（例如 "-123456"），加上终止空字符共 8 字节，未超过缓冲区大小。但... |
| 1057 | vim-9.1.1330 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf函数的目标缓冲区'reply'大小为32字节，但格式化字符串'%d %ld\n'在最坏情况下（如cmdno为负10位数，result为负19位数）可能超过32字节，导致缓冲区溢出。切片代码中未见任何长度检查或使用安全函数... |
| 1226 | vim-9.1.0790 | nb_reply_nr | cpp/overrunning-write | 819 | FP | TP | sprintf函数的目标缓冲区'reply'大小为32字节，但格式化字符串'%d %ld\n'在最坏情况下（如cmdno为负10位数，result为负19位数）可能产生超过32字节的输出，导致缓冲区溢出。切片代码中未见任何长度检查或使... |
| 1499 | redis-7.4.2 | auxHumanNodenameSetter | Dereference of null pointer | 233 | FP | TP | 在 `else if (sdslen(n->human_nodename) != 0)` 这一行，当 `n` 为 `NULL` 时，代码会解引用 `n` 以访问 `n->human_nodename` 并传递给 `sdslen` 函数... |
| 1541 | redis-7.2.1 | auxHumanNodenameSetter | Dereference of null pointer | 267 | FP | TP | 在 `if (n)` 为 false 的分支中，代码直接解引用了空指针 `n` 的成员 `human_nodename` 并传递给 `sdslen` 函数，这构成了明确的空指针解引用逻辑错误。 |
| 1630 | redis-8.0.2 | auxHumanNodenameSetter | Dereference of null pointer | 234 | FP | TP | 在 `else if (sdslen(n->human_nodename) != 0)` 这一行，当 `n` 为 `NULL` 时，代码会解引用 `n` 以访问其成员 `human_nodename` 并传递给 `sdslen` 函数... |

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
| 1 | codeql | vim | cpp/unbounded-write | 753 | 112 | 641 | 0 |
| 2 | csa | ffmpeg | Dereference of null pointer | 445 | 0 | 445 | 0 |
| 3 | csa | git | Dereference of null pointer | 293 | 0 | 293 | 0 |
| 4 | csa | redis | Dereference of null pointer | 210 | 5 | 205 | 0 |
| 5 | codeql | git | cpp/inconsistent-null-check | 129 | 0 | 129 | 0 |
| 6 | csa | musl | Dereference of null pointer | 98 | 0 | 98 | 0 |
| 7 | codeql | vim | cpp/inconsistent-null-check | 87 | 2 | 85 | 0 |
| 8 | codeql | git | cpp/overflow-buffer | 50 | 0 | 50 | 0 |
| 9 | codeql | openssl-openssl | cpp/unterminated-variadic-call | 45 | 0 | 45 | 0 |
| 10 | csa | tmux | Dereference of null pointer | 44 | 0 | 44 | 0 |
| 11 | codeql | openssl-openssl | cpp/use-after-free | 40 | 0 | 40 | 0 |
| 12 | codeql | ffmpeg | cpp/inconsistent-null-check | 35 | 0 | 35 | 0 |
| 13 | codeql | ffmpeg | cpp/offset-use-before-range-check | 33 | 0 | 33 | 0 |
| 14 | codeql | openssl-openssl | cpp/invalid-pointer-deref | 25 | 0 | 25 | 0 |
| 15 | codeql | openssl-openssl | cpp/unbounded-write | 24 | 0 | 24 | 0 |
| 16 | codeql | vim | cpp/overrunning-write | 21 | 11 | 10 | 0 |
| 17 | codeql | vim | cpp/unsafe-strcat | 21 | 0 | 21 | 0 |
| 18 | codeql | git | cpp/offset-use-before-range-check | 20 | 0 | 20 | 0 |
| 19 | codeql | musl | cpp/unbounded-write | 20 | 0 | 20 | 0 |
| 20 | codeql | openssl-openssl | cpp/inconsistent-null-check | 19 | 0 | 19 | 0 |
| 21 | codeql | git | cpp/invalid-pointer-deref | 15 | 0 | 15 | 0 |
| 22 | codeql | vim | cpp/invalid-pointer-deref | 10 | 1 | 9 | 0 |
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

*报告由 `analyze_results.py` 自动生成，生成时间：2026-03-05 23:16:29*
