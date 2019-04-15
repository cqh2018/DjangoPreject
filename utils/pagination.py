__author__ = 'Administrator'
from django.utils.safestring import mark_safe

class Page:
    def __init__(self, current_page, data_conut, per_page_count=20, pager_num=7):
        self.current_page = current_page
        self.data_conut = data_conut
        self.per_page_count = per_page_count
        self.pager_num = pager_num

    @property
    def start(self):
        return (self.current_page - 1) * self.per_page_count

    @property
    def end(self):
        return self.current_page * self.per_page_count

    def total_count(self):
        total_count, y = divmod(self.data_conut, self.per_page_count)
        if y:
            total_count += 1
        return total_count

    def pag_str(self, base_url):
        page_list = []
        if self.total_count() < self.pager_num:
            star_index = 1
            end_index = self.total_count() + 1
        else:
            if self.current_page <= (self.pager_num + 1) / 2:
                star_index = 1
                end_index = self.pager_num
            else:
                star_index = self.current_page - (self.pager_num - 1) / 2
                end_index = self.current_page + (self.pager_num + 1) / 2
                if self.current_page + (self.pager_num - 1) / 2 > self.total_count():
                    end_index = self.total_count() + 1
                    star_index = self.total_count() - self.pager_num + 1

        if self.current_page == 1:
            prev = '<a class="page active" href="#">上一页</a>'
        else:
            prev = '<a class="page active" href="%s?p=%s">上一页</a>' % (base_url, self.current_page - 1)
        page_list.append(prev)
        for i in range(int(star_index), int(end_index)):
            if i == self.current_page:
                temp = '<a class="page active" href="%s?p=%s">%s</a>' % (base_url, i, i)
            else:
                temp = '<a class="page" href="%s?p=%s">%s</a>' % (base_url, i, i)

            page_list.append(temp)
        if self.current_page == self.total_count():
            next = '<a class="page active" href="javascript:void(0);">下一页</a>'
        else:
            next = '<a class="page active" href="%s?p=%s">下一页</a>' % (base_url, self.current_page + 1)
        page_list.append(next)

        jump = '''
           <input tpye="text"/><a onclick='jumpTo(this, "?p=");' id='ii1'>GO</a>
               <script>
                   function jumpTo(ths,base){
                       var val = ths.previousSibling.value;
                       location.href = base + val;
                   }
               </script>
           '''
        page_list.append(jump)
        page_str = ''.join(page_list)
        page_str = mark_safe(page_str)
        return page_str
