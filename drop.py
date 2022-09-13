import os
import sys

class TablesManagement(object):
    def __init__(self, tables):
        self.currentPath = os.getcwd()
        self.tables = tables
        for table in self.tables:
            if not os.path.exists(table):
                os.mkdir(table)

    def generateRenameSqlScripts(self):
        for table in self.tables:
            tableManagement = TableManagement(table)
            tableManagement.generateRenameSqlScript()

    def generateRollBackSqlScripts(self):
        for table in self.tables:
            tableManagement = TableManagement(table)
            tableManagement.generateRollBackSqlScript()

    def generateDropSqlScripts(self):
        for table in self.tables:
            tableManagement = TableManagement(table)
            tableManagement.generateDropSqlScript()
            
class TableManagement(object):
    def __init__(self, table):
        self.table = table

    def generateRenameSqlScript(self):
        if os.path.exists(self.table):
            with open(os.path.join(self.table, 'rename.sql'), 'w') as sqlRenameTable:
                sqlRenameTable.write('RENAME ' + self.table + ' TO ' + 'drop_' + self.table + ';')

    def generateRollBackSqlScript(self):
        if os.path.exists(self.table):
            tableComponents = self.table.split('_');
            originalTable = tableComponents[len(tableComponents)-1]
            with open(os.path.join(self.table, 'rollback.sql'), 'w') as sqlRollBackTable:
                sqlRollBackTable.write('RENAME ' + self.table + ' TO ' + originalTable + ';')

    def generateDropSqlScript(self):
        if os.path.exists(self.table):
            with open(os.path.join(self.table, 'drop.sql'), 'w') as sqlDropTable:
                sqlDropTable.write('DROP TABLE ' + self.table + ';')

if __name__ == '__main__':
    args = sys.argv
    argTables = args.pop(0)
    tables = list(set(argTables))
    
    duplicatedTables = [table for table in argTables if table not in tables]
    print('The following duplicated tables have been filtered out: ')
    print(*duplicatedTables)
    
    tablesManagement = TablesManagement(tables)
    tablesManagement.generateRenameSqlScripts()
    tablesManagement.generateRollBackSqlScripts()
    tablesManagement.generateDropSqlScripts()
